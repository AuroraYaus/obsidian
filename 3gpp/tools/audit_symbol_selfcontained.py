#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@file    audit_symbol_selfcontained.py
@brief   符号表自洽审计：解释某个符号时不得使用尚未定义的符号
@date    2026-11-11

@details
用户 2026-11-11 指出：在解释「有限缓存速率匹配」给出的缓存上限时，用
`floor(TBS_LBRM/(C*R_LBRM))` 作为定义，而 `TBS_LBRM`、`C`、`R_LBRM` 三个符号
当时还没有在符号表里出现过——读者读到第一个公式就撞到三个未解释的符号。

规则（与「符号必须先定义后使用」同源）：
  在 `## 符号与记号约定` 的表格中，按行自上而下扫描；
  第 k 行的「含义与取值」「协议锚点」两列里出现的每个数学符号，
  必须满足以下之一，否则记为违规：
    (1) 它就是本行的符号；
    (2) 它已出现在前面某行的符号列中；
    (3) 它属于运算符/常量白名单（由 audit_symbol_table 的 OPERATOR_CMDS 提供）。

@usage
    python3 tools/audit_symbol_selfcontained.py                # 全库 docs/concepts
    python3 tools/audit_symbol_selfcontained.py <file> ...
    python3 tools/audit_symbol_selfcontained.py --list <file>   # 打印逐行判定
    python3 tools/audit_symbol_selfcontained.py --fix <file>    # 按依赖关系重排表格行

@args
    paths   可选；文件或目录，缺省 docs/concepts
    --list  打印每一行的符号使用情况

@exit_code
    0  无「解释时使用未定义符号」的行
    1  存在违规行
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_symbol_table import (  # noqa: E402
    MATH_RE,
    OPERATOR_CMDS,
    TOKEN_RE,
    canonical,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = PROJECT_ROOT / "docs" / "concepts"
SECTION_RE = None  # 延迟导入避免循环

# 数学函数与常数的白名单：它们在解释式里出现不需要单独定义
FUNCTION_WORDS = {
    "tanh", "exp", "ln", "log", "lg", "max", "min", "sum", "prod",
    "sin", "cos", "tan", "sqrt", "sign", "arg", "argmax", "argmin",
    "erf", "erfc", "mod", "floor", "ceil", "abs",
}
CONSTANT_WORDS = {"e", "j", "pi", "infty"}


def symbol_section(text: str) -> str:
    """@brief 取符号与记号约定小节正文
    @param text 全文件文本
    @return 小节正文（不含标题行）
    """
    m = re.search(r"^##\s*符号与记号约定\s*$", text, re.MULTILINE)
    if not m:
        return ""
    rest = text[m.end():]
    stop = re.search(r"^##\s", rest, re.MULTILINE)
    return rest[: stop.start()] if stop else rest


def row_symbol(line: str) -> str | None:
    """@brief 取表格行第一列中的符号（规范键）
    @param line 表格行
    @return 规范键或 None
    """
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if not cells:
        return None
    first = cells[0]
    m = re.search(r"\$([^$]+)\$", first)
    if not m:
        return None
    body = m.group(1)
    tm = TOKEN_RE.search(body)
    if not tm:
        return None
    base = tm.group(1)
    sub = tm.group(2) or tm.group(3) or ""
    sup = tm.group(4) or tm.group(5) or ""
    return canonical(base, sub.strip(), sup.strip())


def tokens_in(cells: list[str], formula_only: bool = False) -> list[tuple[str, str]]:
    """@brief 抽取若干单元格中的符号
    @param cells 单元格列表
    @param formula_only 只检查含运算符的定义式片段
    @return [(规范键, 原始记号)]
    """
    out: list[tuple[str, str]] = []
    for cell in cells:
        for m in MATH_RE.finditer(cell):
            body = m.group(1) or m.group(2) or ""
            if formula_only and not any(k in body for k in ("=", "\\lfloor", "\\frac", "\\approx", "\\cdot")):
                continue
            for tm in TOKEN_RE.finditer(body):
                base = tm.group(1)
                if base.startswith("\\") and base[1:] in OPERATOR_CMDS:
                    continue
                if base.lstrip("\\") in FUNCTION_WORDS or base in CONSTANT_WORDS:
                    continue
                sub = tm.group(2) or tm.group(3) or ""
                sup = tm.group(4) or tm.group(5) or ""
                if len(base) == 1 and base.isdigit():
                    continue
                out.append((canonical(base, sub.strip(), sup.strip()), tm.group(0)))
    return out


def reorder_rows(path: Path) -> int:
    """@brief 按依赖关系重排符号表数据行（被依赖的行排到前面）
    @param path 笔记路径
    @return 移动的行数（0 表示无需重排）
    """
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^##\s*符号与记号约定\s*$", text, re.MULTILINE)
    if not m:
        return 0
    head, sec_and_rest = text[: m.end()], text[m.end():]
    stop = re.search(r"^##\s", sec_and_rest, re.MULTILINE)
    sec = sec_and_rest[: stop.start()] if stop else sec_and_rest
    tail = sec_and_rest[len(sec):]

    lines = sec.splitlines()
    # 找到表格块
    start = next((i for i, l in enumerate(lines) if l.strip().startswith("|")), None)
    if start is None:
        return 0
    end = start
    while end < len(lines) and lines[end].strip().startswith("|"):
        end += 1
    header = lines[start:start + 2]          # 表头 + 分隔行
    body = lines[start + 2:end]              # 数据行
    rest = lines[end:]

    keys = [row_symbol(l) for l in body]
    pairs = list(zip(keys, body))
    order = {k: i for i, k in enumerate(keys) if k}
    dep = {}
    for k, l in pairs:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        deps = {d for d, _ in tokens_in(cells[1:]) if d in order and d != k}
        dep[k] = deps

    # 稳定的拓扑排序：反复把「依赖都已就位」的行按原顺序取出
    done: list[str] = []
    remaining = [k for k in keys if k]
    while remaining:
        ready = [k for k in remaining if dep.get(k, set()) <= set(done)]
        if not ready:
            break  # 存在环，保持剩余原序
        for k in ready:
            done.append(k)
            remaining.remove(k)
    done.extend(remaining)

    new_body = []
    used = set()
    for k in done:
        for kk, l in pairs:
            if kk == k and k not in used:
                new_body.append(l)
                used.add(k)
                break
    # 没有符号键的行（如小结行）附在末尾，保持原序
    for kk, l in pairs:
        if kk is None:
            new_body.append(l)

    if new_body == body:
        return 0
    moved = sum(1 for a, b in zip(body, new_body) if a != b)
    out = "\n".join(header + new_body + rest)
    path.write_text(head + out + tail, encoding="utf-8")
    return moved


def check_file(path: Path, show: bool = False) -> list[str]:
    """@brief 检查单篇笔记的符号表自洽性
    @param path 笔记路径
    @param show 是否打印明细
    @return 违规描述列表
    """
    text = path.read_text(encoding="utf-8")
    sec = symbol_section(text)
    if not sec:
        return []

    defined: set[str] = set()
    problems: list[str] = []
    for lineno, line in enumerate(sec.splitlines(), 1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if set(stripped) <= set("|-: "):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        cur = row_symbol(line)
        if cur is None:
            # 表头或表内说明行
            continue
        deps = tokens_in(cells[1:], formula_only=True)
        for key, raw in deps:
            if key == cur or key in defined:
                continue
            problems.append(
                f"第 {lineno} 行解释 ${cur}$ 时使用了尚未定义的 ${raw}$"
            )
            if show:
                print(f"    {cur:24} 用到了未定义 {raw}")
        defined.add(cur)
    return problems


def iter_files(paths: list[str]) -> list[Path]:
    """@brief 展开待检查文件
    @param paths CLI 路径列表
    @return 笔记路径列表
    """
    if not paths:
        paths = [str(DEFAULT_ROOT)]
    out: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if not p.is_absolute():
            p = (Path.cwd() / p).resolve()
        if p.is_dir():
            out.extend(sorted(p.glob("*.md")))
        elif p.is_file():
            out.append(p)
    return [p for p in out if p.name not in {"概念图谱入口.md", "README.md"}]


def main() -> int:
    """@brief 命令入口
    @return 退出码
    """
    ap = argparse.ArgumentParser(description="符号表自洽审计")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--fix", action="store_true", help="按依赖关系重排表格行")
    args = ap.parse_args()

    files = iter_files(args.paths)
    if not files:
        print("NO_INPUT")
        return 1

    if args.fix:
        changed = 0
        for p in files:
            if reorder_rows(p):
                changed += 1
        print(f"重排 {changed} 篇的符号表行序")
        return 0

    bad = 0
    total = 0
    for p in files:
        problems = check_file(p, args.list)
        if problems:
            bad += 1
            total += len(problems)
            rel = p.relative_to(PROJECT_ROOT) if PROJECT_ROOT in p.parents else p
            print(f"FAIL {rel}（{len(problems)} 处）")
            for pr in problems[:6]:
                print(f"     - {pr}")
            if len(problems) > 6:
                print(f"     … 另 {len(problems) - 6} 处")

    print("---")
    print(f"检查 {len(files)} 篇：{bad} 篇共 {total} 处「解释时使用未定义符号」")
    if bad:
        print("SYMBOL_SELFCONTAINED_AUDIT_FAIL")
        return 1
    print("SYMBOL_SELFCONTAINED_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
