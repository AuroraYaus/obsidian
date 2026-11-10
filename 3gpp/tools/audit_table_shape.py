#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@file    audit_table_shape.py
@brief   Markdown 表格形状审计（列数一致、数学中的裸竖线不被当成单元格分隔）
@date    2026-11-10

@details
2026-11-10 补符号锚点列时发现：符号表里写 $|f|\\le B$ 会让 GFM 把**数学里的竖线**当成
单元格分隔符，该行被拆成多格、整张表错列，且 Obsidian 渲染会直接错位。这类缺陷肉眼
不易发现，且会随「表格里写绝对值/条件概率/范数」反复出现。

本工具对每个 Markdown 文件：
  1. 识别连续以 `|` 开头的行组成的表格块（含 header 与分隔行）。
  2. 以 header 的单元格数为基准，检查每一行的单元格数是否一致（先按未转义 `|` 切分）。
  3. 若某行格数多于基准，且多出的 `|` 出现在 `$…$` 数学片段内部，则单独标注为
     `MATH_PIPE`（根因明确），修复建议是把 `|` 换成 `\\lvert`/`\\rvert` 或 `\\mid`。
  4. 若某行格数少于基准，标为 `SHORT_ROW`（多半是漏写分隔符）。

@usage
    python3 tools/audit_table_shape.py                    # 全库 docs/
    python3 tools/audit_table_shape.py <file-or-dir> ...
    python3 tools/audit_table_shape.py --ok-list docs/concepts   # 只列通过的文件

@args
    paths       可选；文件或目录，缺省 docs/
    --ok-list   额外打印通过检查的文件

@env
    无（纯静态文本检查）

@exit_code
    0  所有表格列数一致
    1  存在列数不一致的表格行
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = PROJECT_ROOT / "docs"

MATH_SPAN = re.compile(r"\$[^$]*\$")
# 表格中合法的竖线来源：Obsidian 别名 [[target|alias]]、行内代码 `a|b`、数学 $|x|$
KEEP_PIPES = re.compile(r"\[\[[^\]]*\]\]|`[^`]*`|\$[^$]*\$")


def mask_legal_pipes(line: str) -> str:
    """@brief 把 wikilink 别名/行内代码/数学片段内的竖线替换为占位符
    @param line 原始行
    @return 掩码后的行（长度不变，竖线换成 U+2223）
    """
    out: list[str] = []
    last = 0
    for m in KEEP_PIPES.finditer(line):
        out.append(line[last:m.start()])
        out.append(m.group(0).replace("|", "\u2223"))
        last = m.end()
    out.append(line[last:])
    return "".join(out)


def split_cells(line: str) -> list[str]:
    """@brief 按未转义竖线切分单元格
    @param line 表格行
    @return 单元格列表（不含首尾空串）
    """
    line = mask_legal_pipes(line)
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    parts: list[str] = []
    buf: list[str] = []
    i = 0
    while i < len(stripped):
        ch = stripped[i]
        if ch == "\\" and i + 1 < len(stripped):
            buf.append(ch)
            buf.append(stripped[i + 1])
            i += 2
            continue
        if ch == "|":
            parts.append("".join(buf))
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1
    parts.append("".join(buf))
    return parts


def is_separator(cells: list[str]) -> bool:
    """@brief 判断是否为表格分隔行
    @param cells 单元格列表
    @return 是否分隔行
    """
    return all(re.fullmatch(r"\s*:?-{1,}:?\s*", c or "-") for c in cells)


def check_file(path: Path) -> list[str]:
    """@brief 检查单个文件的表格形状
    @param path 文件路径
    @return 问题描述列表
    """
    problems: list[str] = []
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    i = 0
    in_code = False
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if in_code or not line.strip().startswith("|"):
            i += 1
            continue
        # 表格块
        block_start = i
        block: list[tuple[int, str]] = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            block.append((i + 1, lines[i]))
            i += 1
        if len(block) < 2:
            continue
        header_cells = split_cells(block[0][1])
        base = len(header_cells)
        for lineno, raw in block[1:]:
            cells = split_cells(raw)
            if is_separator(cells) and len(cells) == base:
                continue
            if len(cells) == base:
                continue
            if len(cells) > base:
                # 判断多出的竖线是否在数学片段内
                math_pipes = 0
                for m in MATH_SPAN.finditer(raw):
                    math_pipes += m.group(0).count("|")
                kind = "MATH_PIPE" if math_pipes else "EXTRA_CELL"
                problems.append(
                    f"第 {lineno} 行：{kind}（{len(cells)} 格 vs 表头 {base} 格）——"
                    + ("数学里的竖线被当作单元格分隔，建议改用 \\lvert/\\rvert 或 \\mid" if kind == "MATH_PIPE" else "竖线过多")
                )
            else:
                problems.append(f"第 {lineno} 行：SHORT_ROW（{len(cells)} 格 vs 表头 {base} 格）")
        _ = block_start
    return problems


def iter_files(paths: list[str]) -> list[Path]:
    """@brief 展开待检查文件
    @param paths CLI 路径列表
    @return 文件路径列表
    """
    if not paths:
        paths = [str(DEFAULT_ROOT)]
    out: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if not p.is_absolute():
            p = (Path.cwd() / p).resolve()
        if p.is_dir():
            out.extend(sorted(p.rglob("*.md")))
        elif p.is_file():
            out.append(p)
    return out


def main() -> int:
    """@brief 命令入口
    @return 退出码
    """
    ap = argparse.ArgumentParser(description="Markdown 表格形状审计")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--ok-list", action="store_true", help="打印通过检查的文件")
    args = ap.parse_args()

    files = iter_files(args.paths)
    if not files:
        print("NO_INPUT")
        return 1

    bad_files = 0
    total = 0
    for p in files:
        problems = check_file(p)
        rel = p.relative_to(PROJECT_ROOT) if PROJECT_ROOT in p.parents else p
        if problems:
            bad_files += 1
            total += len(problems)
            print(f"FAIL {rel}（{len(problems)} 处）")
            for pr in problems[:6]:
                print(f"     - {pr}")
            if len(problems) > 6:
                print(f"     … 另 {len(problems) - 6} 处")
        elif args.ok_list:
            print(f"OK   {rel}")

    print("---")
    print(f"检查 {len(files)} 个文件：{bad_files} 个文件共 {total} 处表格错列")
    if bad_files:
        print("TABLE_SHAPE_AUDIT_FAIL")
        return 1
    print("TABLE_SHAPE_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
