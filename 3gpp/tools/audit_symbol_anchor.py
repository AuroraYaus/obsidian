#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@file    audit_symbol_anchor.py
@brief   概念笔记符号的协议锚点审计（每个数学符号必须能追到 TS 条款或明确标注非标准）
@date    2026-11-10

@details
用户 2026-11-10 要求：数学符号要标注协议锚点。检查口径：

  1. 在 `## 符号与记号约定` 小节的表格中取每一行（行内须含 `$…$`，即一个符号行）。
  2. 该行的符号必须能在文档的某张表里找到带锚点的行——锚点是以下任一形式：
     - `TS 38.212 §5.4.2.1`、`TS 36.212 Table 5.1.4.1-1` 这类条款引用；
     - `由 §x.x 导出` / `本笔记导出`（派生量，如 X、q、R_rem）；
     - `非 3GPP 标准` / `实现域` / `教科书`（非协议量，如 σ²、LLR 的定义选择）。
  3. 锚点可以写在符号行本身（第四列"协议锚点"），也可以写在独立的"符号与协议出处"表里；
     两种写法都认可，因为 E_Value 篇采用后者且已通过人工确认。

@usage
    python3 tools/audit_symbol_anchor.py                     # 全库 docs/concepts
    python3 tools/audit_symbol_anchor.py <file-or-dir> ...
    python3 tools/audit_symbol_anchor.py --list <file>       # 打印每个符号的锚点判定

@args
    paths   可选；文件或目录，缺省 docs/concepts
    --list  打印逐符号判定明细

@env
    无（纯静态文本检查）

@exit_code
    0  全部符号有锚点
    1  存在无锚点符号，或缺少符号小节
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = PROJECT_ROOT / "docs" / "concepts"

SECTION_RE = re.compile(r"^#{2,3}\s*(符号与记号约定|符号约定|符号的约定)\s*$", re.MULTILINE)
# 锚点形式：TS 条款 / Table 号 / 派生 / 非标准
ANCHOR_RE = re.compile(r"TS\s*\d{2}\.\d{3}|TS\s*\d{2}\.\d{2}|Table\s*\d|由\s*§|本笔记导出|非\s*3GPP|实现域|教科书")
SYMBOL_RE = re.compile(r"\$([^$]+)\$")


def split_frontmatter(text: str) -> tuple[str, str]:
    """@brief 拆出 frontmatter 与正文
    @param text 文件全文
    @return (frontmatter, body)
    """
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[3:end], text[end + 4:]


def norm(sym: str) -> str:
    """@brief 归一化符号文本（去空格、去 $）
    @param sym 符号字符串
    @return 归一化结果
    """
    return re.sub(r"\s+", "", sym.replace("$", ""))


def collect_anchored_symbols(body: str) -> set[str]:
    """@brief 收集文档中带锚点表格行里出现的符号
    @param body 正文
    @return 符号归一化集合
    """
    anchored: set[str] = set()
    for line in body.splitlines():
        if not line.strip().startswith("|"):
            continue
        if not ANCHOR_RE.search(line):
            continue
        for m in SYMBOL_RE.finditer(line):
            anchored.add(norm(m.group(1)))
    return anchored


def check_file(path: Path, show: bool = False) -> tuple[bool, list[str]]:
    """@brief 检查单篇笔记的符号锚点
    @param path 笔记路径
    @param show 是否打印明细
    @return (是否通过, 问题列表)
    """
    text = path.read_text(encoding="utf-8")
    _, body = split_frontmatter(text)
    sec = SECTION_RE.search(body)
    if not sec:
        return False, ["缺 `## 符号与记号约定` 小节"]

    level = 2 if sec.group(0).startswith("## ") else 3
    rest = body[sec.end():]
    stop = re.search(r"^#{2,%d}\s" % level, rest, re.MULTILINE)
    sec_text = rest[: stop.start()] if stop else rest

    anchored = collect_anchored_symbols(body)
    problems: list[str] = []
    seen: set[str] = set()
    for line in sec_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if set(stripped) <= set("|-: "):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if not cells:
            continue
        first = cells[0]
        # 表头行（"符号 / 符号名"）不作为符号检查
        if not SYMBOL_RE.search(first):
            continue
        # 定义式行（含 =、\frac、\cdot、\sum 等）是公式而非符号条目，跳过
        if re.search(r"=|\\frac|\\cdot|\\sum|\\min|\\max|\\left|\\right", first):
            continue
        for m in SYMBOL_RE.finditer(first):
            sym = norm(m.group(1))
            if sym in seen:
                continue
            seen.add(sym)
            ok = sym in anchored
            if show:
                print(f"    {sym:26} {'OK' if ok else 'MISSING'}")
            if not ok:
                problems.append(
                    f"符号 ${sym}$ 无协议锚点：其所在行与文档内的出处表都未给出 TS 条款/Table/派生/非标准标注"
                )
    return (len(problems) == 0), problems


def iter_notes(paths: list[str]) -> list[Path]:
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
    ap = argparse.ArgumentParser(description="概念笔记符号协议锚点审计")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--list", action="store_true", help="打印逐符号判定")
    args = ap.parse_args()

    notes = iter_notes(args.paths)
    if not notes:
        print("NO_INPUT")
        return 1

    bad = 0
    for p in notes:
        ok, problems = check_file(p, args.list)
        rel = p.relative_to(PROJECT_ROOT) if PROJECT_ROOT in p.parents else p
        if not ok:
            bad += 1
            print(f"FAIL {rel}")
            for pr in problems[:12]:
                print(f"     - {pr}")
            if len(problems) > 12:
                print(f"     … 另 {len(problems) - 12} 项")

    print("---")
    print(f"检查 {len(notes)} 篇：FAIL {bad} 篇")
    if bad:
        print("SYMBOL_ANCHOR_AUDIT_FAIL")
        return 1
    print("SYMBOL_ANCHOR_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
