#!/usr/bin/env python3
"""@file audit_python_figure_body_equivalents.py
@brief 审计讲义正文中 Python 生成图片的等价内容是否到位——图片语义必须由
       Mermaid/Markdown 表格/正文文字承接，不能仅存在于像素中。
@date 2026-07-22

本工具检查每张引用的图片是否在附近窗口内附带了等价内容标记
（"Mermaid 等价图""Markdown 等价表""图片内容正文等价"），
并对等价内容的质量进行二次校验：Mermaid 子图必须有足够节点/边，
表格必须有足够数据行，正文等价必须有实质性文字量。
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_DOC_ROOTS = [Path("docs/L1_基础"), Path("docs/L2_协议算法"), Path("docs/L3_工程实现")]
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+\.png)\)")
RETAINED_ASSET_RE = re.compile(r"原图片资产：`([^`]+\.png)`")
MARKERS = ("Mermaid 等价图", "Markdown 等价表", "图片内容正文等价")
META_LABEL_PATTERNS = (
    "原图片资产：",
    "图片内容正文等价",
    "Mermaid 等价图",
    "Markdown 等价表",
    "| 等价项 | 正文表达 |",
    "| 图片 |",
    "| 生成脚本 |",
)
IMAGE_PROSE_PATTERNS = (
    re.compile(r"图\s*T\d[\w.\-]*[^。\n]*(?:由\s*`?tools/figures|生成|输出|读图|图片)"),
    re.compile(r"图片局部视觉几何审计记录"),
    re.compile(r"\|\s*图片(?:脚本|输出|资产|生成|审计)\s*\|"),
    re.compile(r"\|\s*图形证据\s*\|"),
    re.compile(r"Python\s*生成[^。\n]*图"),
    re.compile(r"`tools/figures/[^`]+\.py`[^。\n]*(?:生成|输出|图片|图形)"),
    re.compile(r"`docs/L[123]/assets/[^`]+\.png`"),
)
EVIDENCE_SECTION_HEADINGS = (
    "执行与证据记录",
    "协议证据表",
    "参考文献",
    "证据记录",
    "执行记录",
    "未复现协议资产与关闭条件",
)
GENERIC_PHRASES = (
    "相邻正文表格承接字段、边界和工程检查点",
    "图片中的关键字段、流程或矩阵含义由正文表格化承接",
    "字段、流程和边界不得只存在于图片像素中",
    "输入字段",
    "地址/状态转换",
    "译码器消费",
    "验证输出",
    "图中节点",
    "无文本遮挡",
    "无箭头压字",
    "无裁切",
    "底部留白",
)
SCRIPT_OR_AUDIT_ONLY = (
    "生成脚本",
    "脚本/输出/尺寸",
    "图片资产",
    "图形证据",
    "图片文件检查",
    "图目检",
)


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.path}:{self.line}: {self.rule}: {self.message}"


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    """@brief  从输入路径中递归收集所有 .md 文件，去重排序。
    @param  paths  文件或目录路径列表。
    @return        去重排序后的 Markdown 文件路径列表。"""
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.suffix == ".md":
            files.append(path)
    return sorted(dict.fromkeys(files))


def has_marker_near(lines: list[str], image_line_index: int, window_lines: int) -> bool:
    """@brief  检查图片引用上方指定窗口内是否出现等价内容标记。
    @param  lines             文件的按行列表。
    @param  image_line_index  图片引用所在行号（0-based）。
    @param  window_lines      向上搜索的窗口大小。
    @return                   True 表示附近存在等价内容标记。"""
    start = max(0, image_line_index - window_lines)
    end = min(len(lines), image_line_index + window_lines + 1)
    nearby = "\n".join(lines[start:end])
    return any(marker in nearby for marker in MARKERS)


def equivalent_window(lines: list[str], image_line_index: int, window_lines: int) -> tuple[int, list[str]] | None:
    """@brief  定位图片引用下方的等价内容块——从引用行向下扫描到第一个等价标记，
             收集从标记到块结束之间的所有行。
    @param  lines             文件的按行列表。
    @param  image_line_index  图片引用行号（0-based）。
    @param  window_lines      向下搜索的窗口大小。
    @return                   元组 (标记行号, 块内容行列表)；若无等价标记则返回 None。
    @note   块边界由下一张图片、下一个 ## 标题或其他图的 `图 ` 开头行界定。"""
    start = image_line_index + 1
    end = min(len(lines), image_line_index + window_lines + 1)
    marker_idx = None
    for idx in range(start, end):
        if lines[idx].startswith("## "):
            break
        if any(marker in lines[idx] for marker in MARKERS):
            marker_idx = idx
            break
    if marker_idx is None:
        return None

    block_end = min(len(lines), marker_idx + window_lines + 1)
    for idx in range(marker_idx + 1, block_end):
        line = lines[idx]
        if idx > marker_idx + 3 and line.startswith("!["):
            block_end = idx
            break
        if idx > marker_idx + 3 and line.startswith("## "):
            block_end = idx
            break
        if idx > marker_idx + 5 and line.startswith("图 "):
            block_end = idx
            break
    return marker_idx, lines[marker_idx:block_end]


def mermaid_stats(block: list[str]) -> tuple[int, int]:
    """@brief  统计等价内容块中 Mermaid 图表的节点数和边数。
    @param  block  等价内容块的按行列表。
    @return        (节点数, 边数) 元组，用于质量门槛判断。
    @note   过浅的图表（<4 节点或 <3 边）被视为低质量等价内容。"""
    in_mermaid = False
    nodes = 0
    edges = 0
    for line in block:
        stripped = line.strip()
        if stripped == "```mermaid":
            in_mermaid = True
            continue
        if in_mermaid and stripped == "```":
            break
        if not in_mermaid:
            continue
        if "-->" in stripped or "---" in stripped:
            edges += 1
        nodes += len(re.findall(r"\b[A-Za-z][\w-]*\s*(?:\[|\()", stripped))
    return nodes, edges


def markdown_table_data_rows(block: list[str]) -> int:
    """@brief  统计等价内容块中 Markdown 表格的有效数据行数（不含表头和分隔行）。
    @param  block  等价内容块的按行列表。
    @return        有效数据行数。
    @note   少于 4 行数据的表格被视为低质量等价内容。"""
    rows = 0
    for line in block:
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        if re.fullmatch(r"\|[:\-\s|]+\|", stripped):
            continue
        if "等价项" in stripped and "正文表达" in stripped:
            continue
        if stripped.count("|") >= 3:
            rows += 1
    return rows


def substantive_lines(block: list[str]) -> list[str]:
    """@brief  过滤等价内容块中的实质性正文行，剔除模板占位语、元标签和审计说明。
    @param  block  等价内容块的按行列表。
    @return        仅含实质性内容的行列表——用于评估等价内容文字量是否充足。
    @note   移除所有 GENERIC_PHRASES（如"相邻正文表格承接字段"等模板套话）、
             标记行和脚本/审计说明行。"""
    useful: list[str] = []
    for line in block:
        stripped = line.strip()
        if not stripped or stripped.startswith("```") or stripped.startswith("flowchart"):
            continue
        if any(phrase in stripped for phrase in GENERIC_PHRASES):
            continue
        if any(marker in stripped for marker in MARKERS):
            continue
        if stripped.startswith("| 图片 |") or stripped.startswith("| 生成脚本 |"):
            continue
        useful.append(stripped)
    return useful


def quality_findings(path: Path, line: int, image: str, block: list[str]) -> list[Finding]:
    """@brief  对图片的等价内容块执行质量门槛检查——
             检测模板占位语、Mermaid 过浅、表格过空、正文过短、仅含审计说明。
    @param  path   所属 Markdown 文件路径。
    @param  line   等价标记所在行号。
    @param  image  原始图片引用字符串。
    @param  block  等价内容块的按行列表。
    @return        质量问题 Findings 列表。
    @note   四个维度：占位语检测、Mermaid 深度、表格行数、实质性文字量。"""
    findings: list[Finding] = []
    block_text = "\n".join(block)
    if any(phrase in block_text for phrase in GENERIC_PHRASES):
        findings.append(
            Finding(
                path,
                line,
                "low_quality_body_equivalent",
                f"{image} body equivalent contains placeholder/audit prose instead of figure content",
            )
        )

    has_mermaid = "```mermaid" in block_text
    has_table = re.search(r"^\|.+\|$", block_text, re.MULTILINE) is not None
    if has_mermaid:
        nodes, edges = mermaid_stats(block)
        if nodes < 4 or edges < 3:
            findings.append(
                Finding(
                    path,
                    line,
                    "low_quality_body_equivalent",
                    f"{image} Mermaid equivalent is too shallow: nodes={nodes}, edges={edges}",
                )
            )
    if has_table:
        rows = markdown_table_data_rows(block)
        if rows < 4:
            findings.append(
                Finding(
                    path,
                    line,
                    "low_quality_body_equivalent",
                    f"{image} Markdown table equivalent has too few data rows: rows={rows}",
                )
            )

    useful = substantive_lines(block)
    useful_text = "\n".join(useful)
    if len(useful_text) < 160:
        findings.append(
            Finding(
                path,
                line,
                "low_quality_body_equivalent",
                f"{image} body equivalent is too short to preserve figure details",
            )
        )
    if useful and all(any(token in line for token in SCRIPT_OR_AUDIT_ONLY) for line in useful):
        findings.append(
            Finding(
                path,
                line,
                "low_quality_body_equivalent",
                f"{image} body equivalent only describes scripts/audits, not figure semantics",
            )
        )
    return findings


def audit_markdown_files(
    paths: list[Path],
    window_lines: int = 40,
    allow_body_image_embeds: bool = True,
    forbid_meta_labels: bool = False,
    forbid_image_prose: bool = False,
) -> list[Finding]:
    """@brief  对一组 Markdown 文件执行图片正文等价内容的完整审计。
    @param  paths                    待扫描的文件或目录路径。
    @param  window_lines             搜索等价标记的窗口行数（默认 40）。
    @param  allow_body_image_embeds  是否允许正文中嵌入图片（默认允许，用于迁移过渡期）。
    @param  forbid_meta_labels       是否禁止正文中出现等价元标签（严格模式）。
    @param  forbid_image_prose       是否禁止正文中出现图片生成/审计相关描述（严格模式）。
    @return                          所有发现问题 Findings 的汇总列表。
    @note   三个独立维度：等价内容存在性、等价内容质量、元标签/审计文案位置合规。"""
    findings: list[Finding] = []
    for path in iter_markdown_files(paths):
        lines = path.read_text(encoding="utf-8").splitlines()
        in_evidence_section = False
        if forbid_meta_labels:
            for idx, line in enumerate(lines):
                if any(pattern in line for pattern in META_LABEL_PATTERNS):
                    findings.append(
                        Finding(
                            path,
                            idx + 1,
                            "body_meta_label_disallowed",
                            "lesson body must use Mermaid/tables as normal content, not image-equivalent metadata labels",
                        )
                    )
        if forbid_image_prose:
            for idx, line in enumerate(lines):
                if line.startswith("## "):
                    heading = line.lstrip("#").strip()
                    in_evidence_section = any(token in heading for token in EVIDENCE_SECTION_HEADINGS)
                if in_evidence_section:
                    continue
                if any(pattern.search(line) for pattern in IMAGE_PROSE_PATTERNS):
                    findings.append(
                        Finding(
                            path,
                            idx + 1,
                            "body_image_prose_disallowed",
                            "lesson body must present diagram/table semantics directly; image generation, asset, and visual-audit prose belongs in audit ledgers",
                        )
                    )
        for idx, line in enumerate(lines):
            for match in IMAGE_RE.finditer(line):
                image = match.group(1)
                if not allow_body_image_embeds:
                    findings.append(
                        Finding(
                            path,
                            idx + 1,
                            "body_image_embed_disallowed",
                            f"{image} must be represented by nearby Mermaid/Markdown body content, not embedded as an image",
                        )
                    )
                if allow_body_image_embeds:
                    findings.extend(audit_equivalent_for_asset(path, lines, idx, image, window_lines))
            for match in RETAINED_ASSET_RE.finditer(line):
                image = match.group(1)
                findings.extend(audit_equivalent_for_asset(path, lines, idx, image, window_lines))
    return findings


def audit_equivalent_for_asset(
    path: Path,
    lines: list[str],
    asset_line_index: int,
    image: str,
    window_lines: int,
) -> list[Finding]:
    """@brief  对单个图片资产检查是否存在等价内容块，如有则进一步检查质量。
    @param  path             所属 Markdown 文件路径。
    @param  lines            文件的按行列表。
    @param  asset_line_index  图片引用行号（0-based）。
    @param  image             图片引用字符串（用于错误消息）。
    @param  window_lines      搜索窗口大小。
    @return                   Findings 列表；包含 missing_body_equivalent 或质量问题。"""
    block = equivalent_window(lines, asset_line_index, window_lines)
    if block is None:
        return [
            Finding(
                path,
                asset_line_index + 1,
                "missing_body_equivalent",
                f"{image} has no nearby Mermaid/Markdown body equivalent marker",
            )
        ]
    marker_idx, block_lines = block
    return quality_findings(path, marker_idx + 1, image, block_lines)


def main(argv: list[str] | None = None) -> int:
    """@brief    脚本入口：审计讲义正文中 Python 图片的等价内容是否到位。
    @param    argv  命令行参数列表（sys.argv）。
    @usage    python audit_python_figure_body_equivalents.py [paths...] [--window-lines <N>]
              [--allow-body-image-embeds] [--allow-meta-labels] [--allow-image-prose]
    @args     paths                      可选的扫描路径（默认 L1/L2/L3）。
    @args     --window-lines <N>          等价标记搜索窗口大小（默认 40 行）。
    @args     --allow-body-image-embeds   允许正文嵌入图片（过渡期选项）。
    @args     --allow-meta-labels         允许正文出现等价元标签（过渡期选项）。
    @args     --allow-image-prose         允许正文出现图片生成/审计描述（过渡期选项）。
    @env      无外部依赖（仅标准库）
    @exit_code                            0 = 全部通过；1 = 发现问题。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_DOC_ROOTS)
    parser.add_argument("--window-lines", type=int, default=40)
    parser.add_argument(
        "--allow-body-image-embeds",
        action="store_true",
        help="Allow Markdown image embeds when auditing legacy body-equivalent migrations.",
    )
    parser.add_argument(
        "--allow-meta-labels",
        action="store_true",
        help="Allow legacy image-equivalent metadata labels in lesson bodies.",
    )
    parser.add_argument(
        "--allow-image-prose",
        action="store_true",
        help="Allow legacy image generation, asset, and visual-audit prose in lesson bodies.",
    )
    args = parser.parse_args(argv)

    findings = audit_markdown_files(
        args.paths,
        window_lines=args.window_lines,
        allow_body_image_embeds=args.allow_body_image_embeds,
        forbid_meta_labels=not args.allow_meta_labels,
        forbid_image_prose=not args.allow_image_prose,
    )
    for finding in findings:
        print(finding.format())
    if findings:
        print(f"PYTHON_FIGURE_BODY_EQUIVALENT_AUDIT_FAIL findings={len(findings)}", file=sys.stderr)
        return 1
    print("PYTHON_FIGURE_BODY_EQUIVALENT_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
