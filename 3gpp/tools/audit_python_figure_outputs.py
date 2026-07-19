#!/usr/bin/env python3
"""Run Python figure scripts and verify that real PNG outputs are produced.

Static audits can miss scripts that execute but do not create usable figures.
This audit runs each script from the project root, discovers declared PNG
outputs plus newly modified PNGs, and verifies each image with PIL.
"""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageStat


DEFAULT_PATHS = [Path("tools/figures")]
MIN_WIDTH = 240
MIN_HEIGHT = 160
EDGE_MARGIN = 2


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.path}:{self.line}: {self.rule}: {self.message}"


def iter_python_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_dir():
            files.extend(sorted(path.glob("render_*.py")))
        elif path.suffix == ".py":
            files.append(path)
    return sorted(dict.fromkeys(files))


def _constant_string(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "Path" and node.args:
        return _constant_string(node.args[0])
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        right = _constant_string(node.right)
        if right and right.endswith(".png"):
            return right
    return None


def _assigned_names(node: ast.Assign | ast.AnnAssign) -> list[str]:
    targets: list[ast.expr]
    if isinstance(node, ast.Assign):
        targets = list(node.targets)
    else:
        targets = [node.target]
    names: list[str] = []
    for target in targets:
        if isinstance(target, ast.Name):
            names.append(target.id)
    return names


def declared_png_outputs(script: Path, project_root: Path) -> set[Path]:
    text = script.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text, filename=str(script))
    except SyntaxError:
        return set()
    outputs: set[Path] = set()
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        names = _assigned_names(node)
        if not names or not all(name.isupper() for name in names):
            continue
        value = node.value
        if value is None:
            continue
        literal = _constant_string(value)
        if not literal or not literal.endswith(".png"):
            continue
        path = Path(literal)
        outputs.add(path if path.is_absolute() else project_root / path)
    return outputs


def png_mtimes(project_root: Path) -> dict[Path, int]:
    roots = [project_root / "docs/L1/assets", project_root / "docs/L2/assets", project_root / "docs/L3/assets", project_root / "assets"]
    mtimes: dict[Path, int] = {}
    for root in roots:
        if root.exists():
            for png in root.glob("*.png"):
                mtimes[png.resolve()] = png.stat().st_mtime_ns
    return mtimes


def changed_pngs(before: dict[Path, int], project_root: Path) -> set[Path]:
    after = png_mtimes(project_root)
    changed: set[Path] = set()
    for path, mtime in after.items():
        old = before.get(path)
        if old is None or mtime != old:
            changed.add(path)
    return changed


def image_findings(script: Path, image_path: Path) -> list[Finding]:
    findings: list[Finding] = []
    if not image_path.exists():
        return [Finding(script, 1, "declared_png_missing", f"declared output was not created: {image_path}")]
    try:
        with Image.open(image_path) as img:
            img.load()
            width, height = img.size
            mode = img.mode
            rgb = img.convert("RGB")
    except Exception as exc:  # pragma: no cover - exact PIL errors vary
        return [Finding(script, 1, "invalid_png", f"{image_path}: {exc}")]

    if width < MIN_WIDTH or height < MIN_HEIGHT:
        findings.append(Finding(script, 1, "png_too_small", f"{image_path}: size={width}x{height}"))

    background = Image.new("RGB", rgb.size, rgb.getpixel((0, 0)))
    diff = ImageChops.difference(rgb, background)
    if not diff.getbbox():
        findings.append(Finding(script, 1, "blank_png", f"{image_path}: image appears blank"))
        return findings

    edge_boxes = {
        "top": (0, 0, width, EDGE_MARGIN),
        "bottom": (0, height - EDGE_MARGIN, width, height),
        "left": (0, 0, EDGE_MARGIN, height),
        "right": (width - EDGE_MARGIN, 0, width, height),
    }
    for edge, box in edge_boxes.items():
        crop = ImageChops.difference(rgb.crop(box), background.crop(box))
        stat = ImageStat.Stat(crop)
        if sum(stat.sum) > 0:
            findings.append(Finding(script, 1, "content_touches_edge", f"{image_path}: non-background pixels touch {edge} edge"))

    if mode not in {"RGB", "RGBA", "P", "L"}:
        findings.append(Finding(script, 1, "unexpected_png_mode", f"{image_path}: mode={mode}"))
    return findings


def audit_scripts(paths: list[Path], project_root: Path | None = None, timeout: int = 60) -> list[Finding]:
    root = (project_root or Path.cwd()).resolve()
    findings: list[Finding] = []
    for script in iter_python_files(paths):
        script = script.resolve()
        declared = {path.resolve() for path in declared_png_outputs(script, root)}
        before = png_mtimes(root)
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
        if proc.returncode != 0:
            detail = (proc.stderr or proc.stdout).strip().splitlines()
            message = detail[-1] if detail else f"exit code {proc.returncode}"
            findings.append(Finding(script, 1, "script_failed", message))
            continue

        produced = declared | changed_pngs(before, root)
        if not produced:
            findings.append(Finding(script, 1, "missing_png_output", "script exited 0 but no PNG output was declared or modified"))
            continue
        for output in sorted(produced):
            findings.extend(image_findings(script, output))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_PATHS)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args(argv)

    findings = audit_scripts(args.paths, project_root=args.project_root, timeout=args.timeout)
    for finding in findings:
        print(finding.format())
    if findings:
        print(f"PYTHON_FIGURE_OUTPUT_AUDIT_FAIL findings={len(findings)}", file=sys.stderr)
        return 1
    print("PYTHON_FIGURE_OUTPUT_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
