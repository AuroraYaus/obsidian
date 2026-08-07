#!/usr/bin/env python3
"""
@file remove_markdown_table_column.py
@brief 从 Markdown 管道表格中按列名删除指定列（含表头、分隔行、数据行），
       用于批量清理讲义表格中的冗余或废弃列，避免手工逐个修改每张表格。
@date 2026-07-22
"""

from __future__ import annotations

import argparse
from pathlib import Path


def split_row(line: str) -> list[str] | None:
    """
    @brief 将 Markdown 管道表格行拆分为单元格列表，
           非表格行返回 None，确保只处理实际表格数据。
    @param line 文本中的一行。
    @return 单元格字符串列表（已 strip），非表格行返回 None。
    """
    stripped = line.rstrip("\n")
    if not stripped.lstrip().startswith("|") or "|" not in stripped[1:]:
        return None
    cells = stripped.strip().strip("|").split("|")
    return [cell.strip() for cell in cells]


def is_separator(cells: list[str]) -> bool:
    """
    @brief 判断单元格列表是否为 Markdown 表格的分隔行（如 |:---|:---|），
           用于精确识别表头和分隔行边界，避免误识别内容行。
    @param cells split_row 产出的单元格列表。
    @return True 表示该行仅包含 :、-、空格，是表格分隔行。
    """
    if not cells:
        return False
    for cell in cells:
        text = cell.replace(" ", "")
        if not text:
            return False
        if set(text) - set("-:"):
            return False
        if "-" not in text:
            return False
    return True


def format_row(cells: list[str]) -> str:
    """
    @brief 将单元格列表格式化为标准 Markdown 管道表格行，
           与 split_row 互为逆操作。
    @param cells 单元格字符串列表。
    @return "| cell1 | cell2 | ... |" 格式的表格行字符串。
    """
    return "| " + " | ".join(cells) + " |"


def remove_column(text: str, column_name: str) -> tuple[str, int]:
    """
    @brief 从 Markdown 文本中删除所有表格的指定列，
           保持表格格式完整（表头、分隔行、数据行同步删除）。
           若指定列名在表头中不存在则不修改该表格。
    @param text 原始 Markdown 全文。
    @param column_name 要删除的列名（必须与表头单元格精确匹配）。
    @return (new_text, changed_tables) 元组，changed_tables 为被修改的表格数量。
    @note 保持原始文本的尾随换行符状态（\n 结尾与否）；
          数据行单元格数与表头不一致时该数据行不被修改（安全跳过）。
    """
    lines = text.splitlines()
    keep_trailing_newline = text.endswith("\n")
    out: list[str] = []
    i = 0
    changed_tables = 0

    while i < len(lines):
        header = split_row(lines[i])
        sep = split_row(lines[i + 1]) if i + 1 < len(lines) else None
        if header is None or sep is None or not is_separator(sep):
            out.append(lines[i])
            i += 1
            continue

        if column_name not in header:
            out.append(lines[i])
            out.append(lines[i + 1])
            i += 2
            continue

        remove_idx = header.index(column_name)
        out.append(format_row([cell for idx, cell in enumerate(header) if idx != remove_idx]))
        out.append(format_row([cell for idx, cell in enumerate(sep) if idx != remove_idx]))
        changed_tables += 1
        i += 2

        while i < len(lines):
            cells = split_row(lines[i])
            if cells is None:
                break
            if len(cells) == len(header):
                out.append(format_row([cell for idx, cell in enumerate(cells) if idx != remove_idx]))
            else:
                out.append(lines[i])
            i += 1

    new_text = "\n".join(out)
    if keep_trailing_newline:
        new_text += "\n"
    return new_text, changed_tables


def main() -> int:
    """
    @brief 脚本入口：按列名批量删除指定文件（支持 glob 模式）中所有 Markdown 表格的目标列。
    @usage python tools/remove_markdown_table_column.py COLUMN_NAME PATHS...
    @args COLUMN_NAME  要删除的列名（表头精确匹配）。
    @args PATHS        文件路径（支持 * ? [] glob 模式）。
    @env  无外部依赖（仅标准库）
    @exit_code 0 正常完成。
    @return 0 正常完成。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("column_name")
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()

    total = 0
    for arg in args.paths:
        for path in sorted(Path().glob(arg) if any(ch in arg for ch in "*?[") else [Path(arg)]):
            if not path.is_file():
                continue
            old = path.read_text(encoding="utf-8")
            new, changed = remove_column(old, args.column_name)
            if changed:
                path.write_text(new, encoding="utf-8")
                total += changed
                print(f"{path}: removed {changed} table column(s)")
    print(f"removed_tables={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
