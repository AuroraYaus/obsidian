#!/usr/bin/env python3
"""
@file normalize_abbreviation_tables.py
@brief 扫描讲义中实际使用的技术缩写，确保每篇讲义的"本节缩写说明"表格包含该节用到的所有标准术语，
       并补充缺失项。目的：维护各节缩写表的完整性，避免读者在无定义的情况下遇到缩写。
@date 2026-07-22
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from audit_lesson_terms import TECH_TERM_RE, TECH_TERMS, strip_code_fences


def used_terms(text: str) -> list[str]:
    """
    @brief 从讲义正文中检测实际出现的技术缩写（排除代码块内的假阳性），
           返回该节真正需要解释的缩写列表。
    @param text 讲义 Markdown 全文。
    @return 在正文中出现过的标准缩写列表。
    @note 检测前先通过 strip_code_fences 移除代码块，避免代码中的变量名或注释被误判为缩写。
    """
    stripped = strip_code_fences(text)
    return [abbr for abbr in TECH_TERMS if TECH_TERM_RE[abbr].search(stripped)]


def normalize_table(text: str) -> tuple[str, int]:
    """
    @brief 规范化单篇讲义的缩写说明表格：若缺少"本节缩写说明"小节则追加，
           若已有但缺少术语则补充缺失行。幂等：若表格已包含全部术语则不做修改。
    @param text 讲义 Markdown 全文。
    @return (new_text, added_count) 元组，added_count 为新增缩写行数（0 表示无需修改）。
    @note 新插入的缩写说明表格紧随大标题（第一个 # 标题行）之后；
          已有表格若已覆盖所有需求术语则跳过写入磁盘。
    """
    marker = "## 本节缩写说明"
    needed_terms = used_terms(text)
    if not needed_terms:
        return text, 0

    marker_pos = text.find(marker)
    if marker_pos < 0:
        lines = text.splitlines()
        keep_trailing_newline = text.endswith("\n")
        if not lines or not lines[0].startswith("# "):
            return text, 0
        table = [
            "",
            marker,
            "",
            "| 完整写法 | 缩写 |",
            "| :--- | :--- |",
            *[f"| {TECH_TERMS[abbr]} | {abbr} |" for abbr in needed_terms],
            "",
        ]
        new_text = "\n".join([lines[0], *table, *lines[1:]])
        if keep_trailing_newline:
            new_text += "\n"
        return new_text, len(needed_terms)

    lines = text.splitlines()
    keep_trailing_newline = text.endswith("\n")

    heading_idx = next((i for i, line in enumerate(lines) if line.strip() == marker), None)
    if heading_idx is None:
        return text, 0

    first_row = heading_idx + 1
    while first_row < len(lines) and not lines[first_row].strip():
        first_row += 1
    if first_row + 1 >= len(lines) or not lines[first_row].lstrip().startswith("|"):
        return text, 0

    end = first_row
    while end < len(lines) and lines[end].lstrip().startswith("|"):
        end += 1

    existing_block = "\n".join(lines[first_row:end])
    existing_terms = {abbr for abbr, expansion in TECH_TERMS.items() if expansion in existing_block}
    rows = [f"| {TECH_TERMS[abbr]} | {abbr} |" for abbr in needed_terms]

    if existing_terms.issuperset(needed_terms):
        return text, 0

    new_table = [
        "| 完整写法 | 缩写 |",
        "| :--- | :--- |",
        *rows,
    ]
    new_lines = lines[:first_row] + new_table + lines[end:]
    new_text = "\n".join(new_lines)
    if keep_trailing_newline:
        new_text += "\n"
    return new_text, len(set(needed_terms) - existing_terms)


def main() -> int:
    """
    @brief 脚本入口：对指定文件列表逐一执行缩写表格规范化，
           输出每文件新增行数和总计统计。
    @usage python tools/normalize_abbreviation_tables.py FILE...
    @args FILE...  要处理的一个或多个 .md 文件路径。
    @env  无外部依赖（仅标准库）
    @exit_code 0 正常完成。
    @return 0 正常完成。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    total = 0
    for path in args.paths:
        if not path.is_file():
            continue
        old = path.read_text(encoding="utf-8")
        new, added = normalize_table(old)
        if added:
            path.write_text(new, encoding="utf-8")
            total += added
            print(f"{path}: added {added} abbreviation row(s)")
    print(f"added_rows={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
