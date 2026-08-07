#!/usr/bin/env python3
"""
@file    audit_figure_readability.py
@brief   静态审计 Python 教学图脚本中的可读性风险。
         检测过小的字体大小、表格行高不足、全局小字体等问题——确保渲染到
         Markdown 报告中的讲义插图在屏幕和打印场景下都能清晰阅读。
@date    2026-07-22

Static readability-risk audit for Python-generated curriculum figures.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_PATHS = [Path("tools/figures")]
MIN_TABLE_FONT = 24
MIN_TABLE_ROW_H = 56

FONT_CALL_RE = re.compile(r"font\(\s*(\d+)\s*(?:,|\))")
CONST_RE = re.compile(r"^([A-Z][A-Z0-9_]*)\s*=\s*font\(\s*(\d+)", re.MULTILINE)
TABLE_HINT_RE = re.compile(
    r"(def\s+\w*table\w*\s*\(|row_h|headers|cell\(|draw_cell|Comparison|Descriptor|矩阵|表)",
    re.IGNORECASE,
)
SMALL_TABLE_FONT_RE = re.compile(
    r"(?:cell|draw_cell|center_text|line_centered_text|draw\.text|wrapped|draw_wrapped)"
    r"[\s\S]{0,160}?font\(\s*((?:1[0-9]|2[0-3]))\s*(?:,|\))",
    re.MULTILINE,
)
SMALL_CONST_USE_RE = re.compile(
    r"(?:cell|draw_cell|center_text|line_centered_text|draw\.text|wrapped|draw_wrapped)"
    r"[\s\S]{0,180}?\b([A-Z][A-Z0-9_]*)\b",
    re.MULTILINE,
)
ROW_H_RE = re.compile(r"row_h\s*=\s*(\d+)|row_h:\s*int\s*=\s*(\d+)")
GLOBAL_SMALL_FONT_RE = re.compile(r"font\(\s*(1[3-9]|2[0-3])\s*(?:,|\))")
SMALL_FONT_EXEMPTION_RE = re.compile(
    r"(axis_font|readability-exception|辅助标注|短索引|刻度)",
    re.IGNORECASE,
)


def collect_files(paths: list[Path]) -> list[Path]:
    """
    @brief   从路径列表中收集所有 .py 文件。
             统一文件入口，避免每个审计函数重复实现遍历逻辑。
    @param   paths  路径列表，可混合目录和文件。
    @return  按文件名排序的 .py 文件路径列表。
    @note    不存在的路径被静默跳过。
    """
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_dir():
            files.extend(sorted(path.glob("*.py")))
        elif path.suffix == ".py":
            files.append(path)
    return files


def line_for_offset(text: str, offset: int) -> int:
    """
    @brief   将字符偏移量转换为行号（1-based）。
             正则匹配返回字符位置，审计报告需要人类可读的行号。
    @param   text    源文本。
    @param   offset  字符偏移量（0-based）。
    @return  1-based 行号。
    """
    return text.count("\n", 0, offset) + 1


def audit_file(path: Path) -> list[str]:
    """
    @brief   对单个 Python 渲染脚本执行全部可读性审计规则。
             检查所有 font() 调用的大小是否符合教学图的最小字体标准（24px），
             表格行高是否足够（≥56px），以及是否存在全局过小字体。
    @param   path  待审计的 .py 文件路径。
    @return  该文件的所有可读性发现列表（已去重排序）。
    @note    发现列表使用 sorted(set(...)) 去重，避免同一问题被多次报告。
             SMALL_FONT_EXEMPTION_RE 匹配的行（如坐标轴标注）可被豁免。
    """
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []

    for match in GLOBAL_SMALL_FONT_RE.finditer(text):
        line_start = text.rfind("\n", 0, match.start()) + 1
        line_end = text.find("\n", match.start())
        if line_end == -1:
            line_end = len(text)
        line = text[line_start:line_end]
        if SMALL_FONT_EXEMPTION_RE.search(line):
            continue
        size = int(match.group(1))
        findings.append(
            f"{path}:{line_for_offset(text, match.start())}: figure text uses font({size}); "
            "raise teaching/table text to 24px+ or mark a justified auxiliary-label exception"
        )

    if not TABLE_HINT_RE.search(text):
        return sorted(set(findings))

    constants = {name: int(size) for name, size in CONST_RE.findall(text)}

    for match in SMALL_TABLE_FONT_RE.finditer(text):
        size = int(match.group(1))
        findings.append(
            f"{path}:{line_for_offset(text, match.start())}: table-like drawing uses font({size}); "
            "verify rendered Markdown readability or increase font/row height/split the table"
        )

    for match in SMALL_CONST_USE_RE.finditer(text):
        name = match.group(1)
        size = constants.get(name)
        if size is None or size >= MIN_TABLE_FONT:
            continue
        findings.append(
            f"{path}:{line_for_offset(text, match.start())}: table-like drawing may use {name}=font({size}); "
            "verify rendered Markdown readability or increase font/row height/split the table"
        )

    for match in ROW_H_RE.finditer(text):
        value = int(match.group(1) or match.group(2))
        if value < MIN_TABLE_ROW_H:
            findings.append(
                f"{path}:{line_for_offset(text, match.start())}: row_h={value} is a readability risk for table figures; "
                "increase row height unless this is a tiny axis/tick label table"
            )

    return sorted(set(findings))


def main() -> int:
    """
    @brief   图可读性审计入口——检测渲染脚本中字体大小和表格行高的可读性风险。
    @usage   python audit_figure_readability.py [paths...]
    @args    paths  待审计的 .py 文件或目录路径，默认为 tools/figures。
    @env     无外部依赖（仅标准库）
    @exit_code  0 = 无发现或仅有建议，1 = 存在可读性风险。
    @note    输出包含格式化发现列表和聚合状态行。
             表格检测仅在脚本包含 TABLE_HINT_RE 标记时才激活，
             避免对非表格脚本误报。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_PATHS)
    args = parser.parse_args()

    findings: list[str] = []
    for path in collect_files(args.paths):
        findings.extend(audit_file(path))

    if findings:
        print("FIGURE_READABILITY_AUDIT_FINDINGS")
        print("\n".join(findings))
        return 1

    print("FIGURE_READABILITY_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
