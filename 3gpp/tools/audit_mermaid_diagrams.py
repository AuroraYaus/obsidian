#!/usr/bin/env python3
"""@file audit_mermaid_diagrams.py
@brief 审计 Mermaid 图表在 Markdown 中的质量——静态规则检查 + 可选真实渲染验证。
@date 2026-07-22

本工具不仅扫描代码围栏中的 Mermaid 块，还通过本地 mmdc 渲染器验证
图表的实际兼容性（可选）。静态规则覆盖：缺少图表声明、有序列表标签
冲突、不安全 subgraph 名称、歧义节点引用、空流程图、缺少样式声明。

若 mmdc 未安装则降级为仅静态检查，不阻断通过但给出警告。
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
    """@brief  从输入路径中收集所有 .md 文件，文件去重后按字典序排列。
    @param  paths  文件或目录路径列表（不存在的路径静默跳过）。
    @return        去重排序后的 .md 文件路径列表。"""
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
    """@brief  从单个 Markdown 文件中提取所有 ```mermaid``` 代码块。
    @param  path  Markdown 文件路径。
    @return       包含行号、序号和纯文本内容的 MermaidBlock 列表。"""
    text = path.read_text(encoding="utf-8")
    blocks: list[MermaidBlock] = []
    for index, match in enumerate(MERMAID_BLOCK_RE.finditer(text), start=1):
        line = text.count("\n", 0, match.start()) + 1
        blocks.append(MermaidBlock(path=path, line=line, index=index, text=match.group(1)))
    return blocks


def _is_safe_subgraph_name(raw_name: str) -> bool:
    """@brief  判断 subgraph 声明是否使用了安全命名格式——
             纯字母数字 ID，或 ID[\"显示文本\"] 双参数语法。
    @param  raw_name  subgraph 行中 subgraph 关键字之后的原始文本。
    @return           True 表示名称格式安全，不会导致渲染歧义。"""
    name = raw_name.strip()
    if "[" in name:
        return re.fullmatch(r"[A-Za-z][\w-]*\s*\[.+\]", name) is not None
    return re.fullmatch(r"[A-Za-z][\w-]*", name) is not None


def _node_ids(lines: list[str]) -> set[str]:
    """@brief  从 Mermaid 行列表中提取所有已声明的节点 ID。
    @param  lines  Mermaid 源码的按行列表。
    @return        去重的节点 ID 集合，用于后续边引用的合法性校验。"""
    ids: set[str] = set()
    for line in lines:
        match = NODE_DEFINITION_RE.match(line)
        if match:
            ids.add(match.group(1))
    return ids


def _edge_left_is_safe(left: str, ids: set[str]) -> bool:
    """@brief  检查边表达式左侧是否引用了已知节点 ID 或合法匿名节点定义。
    @param  left  边表达式中箭头左侧的文本。
    @param  ids   已声明的节点 ID 集合。
    @return       True 表示引用安全，不会在渲染时产生歧义节点。
    @note  空格在左侧中有风险——可能是未引用的显示文本而不是 ID。"""
    if left in ids:
        return True
    if NODE_DEFINITION_RE.match(left):
        return True
    if re.fullmatch(r"[A-Za-z][\w-]*", left):
        return True
    return False


def audit_static(block: MermaidBlock) -> list[Finding]:
    """@brief  对单个 Mermaid 代码块执行全套本地静态规则检查，
             涵盖声明缺失、标签冲突、subgraph 安全、节点歧义、空图和样式缺失。
    @param  block  待检查的 Mermaid 代码块。
    @return        静态规则发现的问题列表；空列表表示静态检查全部通过。
    @note   所有规则基于本项目的 Mermaid 编写指南和 mmdc 渲染器已知陷阱。"""
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
    """@brief  使用本地 mmdc 将单个 Mermaid 块渲染为 SVG，验证真实兼容性。
    @param  block              待渲染的 Mermaid 代码块。
    @param  mmdc               mmdc 可执行文件的路径。
    @param  puppeteer_config   Puppeteer 配置文件路径（--no-sandbox）。
    @param  out_dir            临时输出目录。
    @return                    None 表示渲染成功；否则返回包含错误详情的 Finding。
    @note   渲染超时 45 秒，超时将被捕获并转为 Finding。"""
    source = out_dir / f"{block.path.name}.{block.index}.mmd"
    output = out_dir / f"{block.path.name}.{block.index}.svg"
    source.write_text(block.text + "\n", encoding="utf-8")
    try:
        proc = subprocess.run(
            [mmdc, "-p", str(puppeteer_config), "-i", str(source), "-o", str(output), "-b", "transparent"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=45,
        )
    except subprocess.TimeoutExpired:
        return Finding(block.path, block.line, "render_failed", "mmdc render timed out (45s)")
    except FileNotFoundError:
        return Finding(block.path, block.line, "render_failed", "mmdc binary not found")
    if proc.returncode == 0 and output.exists() and output.stat().st_size > 0:
        return None
    detail = (proc.stdout + proc.stderr).strip().splitlines()
    message = detail[-1] if detail else f"mmdc exited with {proc.returncode}"
    return Finding(block.path, block.line, "render_failed", message)


def audit_blocks(blocks: list[MermaidBlock], render: bool = True) -> list[Finding]:
    """@brief  对一批 Mermaid 代码块执行静态检查，并可选择性地进行真实渲染验证。
    @param  blocks  待审计的 Mermaid 代码块列表。
    @param  render  True 时启动 mmdc 渲染验证（需 mmdc 在 PATH 中）。
    @return         所有问题 Findings 的汇总列表。
    @note   若 mmdc 未安装，渲染验证降级为一条警告而非阻断通过。"""
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
    """@brief  对一组 Markdown 文件中的所有 Mermaid 图表执行完整审计流程。
    @param  paths   待扫描的文件或目录路径。
    @param  render  是否启用 mmdc 真实渲染（默认开启）。
    @return         所有发现问题的汇总。"""
    blocks: list[MermaidBlock] = []
    for path in iter_markdown_files(paths):
        blocks.extend(extract_blocks(path))
    return audit_blocks(blocks, render=render)


def main(argv: list[str] | None = None) -> int:
    """@brief    脚本入口：审计 Markdown 文件中的 Mermaid 图表质量。
    @param    argv  命令行参数列表（sys.argv）。
    @usage    python audit_mermaid_diagrams.py [paths...] [--no-render]
    @args     paths       可选的文件或目录路径（默认扫描 docs/ 和 roadmap）。
    @args     --no-render  跳过 mmdc 渲染，仅执行静态规则检查。
    @exit_code             0 = 全部通过；1 = 发现问题。"""
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
