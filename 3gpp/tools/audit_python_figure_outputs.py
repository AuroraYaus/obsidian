#!/usr/bin/env python3
"""@file audit_python_figure_outputs.py
@brief 实际执行 Python 图片生成脚本，验证其能否产出生效的 PNG 输出——
       静态审计可能漏过能运行但不生成可用图片的脚本，
       本工具通过真实执行 + PIL 图片检查弥合这一差距。
@date 2026-07-22

验证流程：
1. 运行脚本（30s/60s 超时）
2. 发现脚本声明的 PNG 输出及磁盘上被修改的 PNG
3. 用 PIL 验证每张 PNG：存在性、尺寸门槛、空白检测、边缘裁剪检测
4. 全验证通过才算 PASS
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
    """@brief  从输入路径中收集所有 `render_*.py` 图片生成脚本。
    @param  paths  文件或目录路径列表。
    @return        去重排序后的脚本文件路径列表。"""
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
    """@brief  从 AST 节点中提取 PNG 路径常量——处理普通字符串、Path() 调用和
             除法拼接（如 `OUTDIR / "name.png"`）三种常见形式。
    @param  node  AST 节点（通常在赋值语句右侧）。
    @return       以 `.png` 结尾的路径字符串；无法提取则返回 None。
    @note   仅处理可在不运行时确定的编译期常量路径。"""
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
    """@brief  从赋值/注释赋值节点中提取所有被赋值的变量名。
    @param  node  ast.Assign 或 ast.AnnAssign 节点。
    @return       变量名字符串列表；如 `x = y = ...` 则返回两个名字。"""
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
    """@brief  通过 AST 分析脚本顶层赋值语句，提取所有声明的 PNG 输出路径——
             识别全大写常量赋值（如 `OUTPUT = Path("foo.png")`）中含 `.png` 结尾的值。
    @param  script        图片生成脚本路径。
    @param  project_root  项目根目录，用于将相对路径转为绝对路径。
    @return               声明的绝对 PNG 路径集合。
    @note   仅处理顶层全大写常量赋值，函数内部的局部变量不在此列。"""
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
    """@brief  快照 L1/L2/L3/assets 目录下所有 PNG 文件的修改时间（纳秒级）。
    @param  project_root  项目根目录。
    @return               路径到修改时间（ns）的映射，用于前后对比发现新生成的文件。
    @note   使用纳秒级 mtime 确保高精度对比，避免秒级精度漏报快速生成的同秒文件。"""
    roots = [project_root / "docs/L1/assets", project_root / "docs/L2_协议算法/assets", project_root / "docs/L3/assets", project_root / "assets"]
    mtimes: dict[Path, int] = {}
    for root in roots:
        if root.exists():
            for png in root.glob("*.png"):
                mtimes[png.resolve()] = png.stat().st_mtime_ns
    return mtimes


def changed_pngs(before: dict[Path, int], project_root: Path) -> set[Path]:
    """@brief  对比脚本执行前后的 PNG mtime 快照，找出被修改或新创建的 PNG。
    @param  before        脚本执行前的 mtime 快照。
    @param  project_root  项目根目录。
    @return               新增或 mtime 变化的 PNG 绝对路径集合。
    @note   变化检测覆盖：新文件出现、旧文件时间戳变化（重新生成）。"""
    after = png_mtimes(project_root)
    changed: set[Path] = set()
    for path, mtime in after.items():
        old = before.get(path)
        if old is None or mtime != old:
            changed.add(path)
    return changed


def image_findings(script: Path, image_path: Path) -> list[Finding]:
    """@brief  用 PIL 对单张 PNG 图片执行质量验证——
             检查文件存在性、尺寸门槛（≥240x160）、空白检测、边缘裁剪、色彩模式。
    @param  script      生成该 PNG 的脚本路径（用于错误关联）。
    @param  image_path  待验证的 PNG 文件路径。
    @return             质量问题 Findings 列表；空列表表示图片质量合格。
    @note   空白检测：以左上角像素为背景色，若全图与该色无差异则判为空白。
             边缘检测：检查上下左右 2px 边缘是否有非背景像素（内容裁剪风险）。
    @throws OSError/PIL.UnidentifiedImageError  PIL 读取失败时被上层捕获。"""
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
    """@brief  批量执行图片生成脚本并验证输出——对每个脚本依次执行、检测产物、
             用 PIL 验证图片质量。
    @param  paths         脚本文件或目录路径列表。
    @param  project_root  项目根目录（脚本执行的工作目录，默认当前目录）。
    @param  timeout       单个脚本执行超时秒数（默认 60 秒）。
    @return               所有问题 Findings 汇总；包含脚本崩溃、无输出、图片质量缺陷。
    @note   对于每个脚本，实际产物由"声明的输出 + mtime 变化检测"联合确定，
             因为部分脚本的输出路径可能无法通过静态分析完全预测。"""
    root = project_root if project_root is not None else Path.cwd()
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
    """@brief    脚本入口：执行图片生成脚本并验证 PNG 输出质量。
    @param    argv  命令行参数列表（sys.argv）。
    @usage    python audit_python_figure_outputs.py [paths...] [--project-root <dir>] [--timeout <N>]
    @args     paths            待审计的脚本文件或目录（默认 tools/figures）。
    @args     --project-root   项目根目录（脚本执行的工作目录）。
    @args     --timeout        单个脚本执行超时秒数（默认 60）。
    @exit_code                 0 = 所有脚本通过；1 = 存在问题。
    @note    需要 PIL/Pillow 库和可执行的 Python 环境（脚本在子进程中运行）。"""
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
