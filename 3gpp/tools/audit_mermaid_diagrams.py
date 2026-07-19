#!/usr/bin/env python3
"""Audit Mermaid diagrams using local Mermaid skill rules and real rendering.

This intentionally does more than grep for code fences. The local Mermaid skill
requires avoiding ordered-list labels, unsafe subgraph names, ambiguous node
references, and renderer-only surprises. Static rules catch known pitfalls
quickly; optional mmdc rendering verifies actual Mermaid compatibility.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


DEFAULT_PATHS = [Path("docs"), Path("2026-06-19-lte-nr-decoding-learning-roadmap.md")]
MERMAID_BLOCK_RE = re.compile(r"```mermaid\n(.*?)\n```", re.DOTALL)
ORDERED_LIST_LABEL_RE = re.compile(r"[\[\(\{][\"']?[^][(){}\"'\n]*\b\d+\.\s+[^][(){}\"'\n]*[\"']?[\]\)\}]")
SUBGRAPH_RE = re.compile(r"^\s*subgraph\s+(.+?)\s*$")
NODE_DEFINITION_RE = re.compile(r"^\s*([A-Za-z][\w-]*)\s*(?:\[|\(|\{|\[\(|\(\(|>\s*)")
EDGE_RE = re.compile(r"(-->|-.->|==>|<-->|---)")
STYLE_RE = re.compile(r"^\s*(classDef|style|class)\s+")
DECLARATION_RE = re.compile(
    r"^\s*(?:flowchart|graph|sequenceDiagram|stateDiagram-v2|classDiagram|mindmap|erDiagram|journey|gantt)\b"
)


@dataclass(frozen=True)
class MermaidBlock:
    path: Path
    line: int
    index: int
    text: str


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.path}:{self.line}: {self.rule}: {self.message}"


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.suffix == ".md":
            files.append(path)
    return sorted(dict.fromkeys(files))


def extract_blocks(path: Path) -> list[MermaidBlock]:
    text = path.read_text(encoding="utf-8")
    blocks: list[MermaidBlock] = []
    for index, match in enumerate(MERMAID_BLOCK_RE.finditer(text), start=1):
        line = text.count("\n", 0, match.start()) + 1
        blocks.append(MermaidBlock(path=path, line=line, index=index, text=match.group(1)))
    return blocks


def _is_safe_subgraph_name(raw_name: str) -> bool:
    name = raw_name.strip()
    if "[" in name:
        return re.fullmatch(r"[A-Za-z][\w-]*\s*\[.+\]", name) is not None
    return re.fullmatch(r"[A-Za-z][\w-]*", name) is not None


def _node_ids(lines: list[str]) -> set[str]:
    ids: set[str] = set()
    for line in lines:
        match = NODE_DEFINITION_RE.match(line)
        if match:
            ids.add(match.group(1))
    return ids


def _edge_left_is_safe(left: str, ids: set[str]) -> bool:
    if left in ids:
        return True
    if NODE_DEFINITION_RE.match(left):
        return True
    if re.fullmatch(r"[A-Za-z][\w-]*", left):
        return True
    return False


def audit_static(block: MermaidBlock) -> list[Finding]:
    findings: list[Finding] = []
    lines = block.text.splitlines()
    first_content = next((line.strip() for line in lines if line.strip() and not line.strip().startswith("%%")), "")
    if not DECLARATION_RE.match(first_content):
        findings.append(
            Finding(
                block.path,
                block.line,
                "missing_diagram_declaration",
                "Mermaid block should start with an explicit diagram declaration after init comments",
            )
        )

    ids = _node_ids(lines)
    has_edge = False
    has_style = False
    for offset, line in enumerate(lines, start=1):
        line_no = block.line + offset
        stripped = line.strip()
        if ORDERED_LIST_LABEL_RE.search(line):
            findings.append(
                Finding(
                    block.path,
                    line_no,
                    "ordered_list_label",
                    "node text contains 'number. space', which Mermaid can parse as unsupported markdown list syntax",
                )
            )
        subgraph = SUBGRAPH_RE.match(line)
        if subgraph and not _is_safe_subgraph_name(subgraph.group(1)):
            findings.append(
                Finding(
                    block.path,
                    line_no,
                    "subgraph_name_without_id",
                    "subgraph display text with spaces must use id[\"Display Name\"] syntax",
                )
            )
        if EDGE_RE.search(line):
            has_edge = True
            left = re.split(EDGE_RE, stripped, maxsplit=1)[0].strip()
            if " " in left and not _edge_left_is_safe(left, ids) and not left.startswith(("subgraph", "classDef")):
                findings.append(
                    Finding(
                        block.path,
                        line_no,
                        "ambiguous_node_reference",
                        "edge appears to reference display text instead of a node id",
                    )
                )
        if STYLE_RE.match(line):
            has_style = True

    if first_content.startswith(("flowchart", "graph")) and not has_edge:
        findings.append(
            Finding(block.path, block.line, "empty_flowchart", "flowchart/graph block has no visible edges")
        )
    if first_content.startswith(("flowchart", "graph")) and not has_style:
        findings.append(
            Finding(
                block.path,
                block.line,
                "missing_style_declaration",
                "flowchart should include style/class declarations for stable professional rendering",
            )
        )
    return findings


def render_block(block: MermaidBlock, mmdc: str, puppeteer_config: Path, out_dir: Path) -> Finding | None:
    source = out_dir / f"{block.path.name}.{block.index}.mmd"
    output = out_dir / f"{block.path.name}.{block.index}.svg"
    source.write_text(block.text + "\n", encoding="utf-8")
    proc = subprocess.run(
        [mmdc, "-p", str(puppeteer_config), "-i", str(source), "-o", str(output), "-b", "transparent"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=45,
    )
    if proc.returncode == 0 and output.exists() and output.stat().st_size > 0:
        return None
    detail = (proc.stdout + proc.stderr).strip().splitlines()
    message = detail[-1] if detail else f"mmdc exited with {proc.returncode}"
    return Finding(block.path, block.line, "render_failed", message)


def audit_blocks(blocks: list[MermaidBlock], render: bool = True) -> list[Finding]:
    findings: list[Finding] = []
    for block in blocks:
        findings.extend(audit_static(block))

    if not render:
        return findings

    mmdc = shutil.which("mmdc")
    if not mmdc:
        findings.append(Finding(Path("."), 1, "mmdc_missing", "mmdc is not installed or not on PATH"))
        return findings

    with tempfile.TemporaryDirectory(prefix="mermaid-audit-") as tmp:
        tmp_path = Path(tmp)
        puppeteer_config = tmp_path / "puppeteer.json"
        puppeteer_config.write_text(
            '{"args":["--no-sandbox","--disable-setuid-sandbox"]}\n',
            encoding="utf-8",
        )
        out_dir = tmp_path / "rendered"
        out_dir.mkdir()
        for block in blocks:
            finding = render_block(block, mmdc, puppeteer_config, out_dir)
            if finding:
                findings.append(finding)
    return findings


def audit_markdown_files(paths: list[Path], render: bool = True) -> list[Finding]:
    blocks: list[MermaidBlock] = []
    for path in iter_markdown_files(paths):
        blocks.extend(extract_blocks(path))
    return audit_blocks(blocks, render=render)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_PATHS)
    parser.add_argument("--no-render", action="store_true", help="skip mmdc rendering and run static skill rules only")
    args = parser.parse_args(argv)

    findings = audit_markdown_files(args.paths, render=not args.no_render)
    for finding in findings:
        print(finding.format())
    if findings:
        print(f"MERMAID_DIAGRAM_AUDIT_FAIL findings={len(findings)}", file=sys.stderr)
        return 1
    print("MERMAID_DIAGRAM_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
