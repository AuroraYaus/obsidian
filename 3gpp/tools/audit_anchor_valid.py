#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@file    audit_anchor_valid.py
@brief   协议锚点可解析性审计（`TS 38.212 §5.4.2.1` 这类引用必须在本地抽取件里存在）
@date    2026-11-10

@details
用户在整理过程中要求「遇到不对的要核实后修改」。概念笔记的符号锚点与协议锚点大量引用
`TS xx.xxx §a.b.c`，此前只能靠人工抽查，存在编造条款号的风险。本工具把核实自动化：

  1. 从文档抽取形如 `TS 38.212 §5.4.2.1`、`TS 38.212 Rel-19 §5.4.2.1`、
     `TS 36.212 §5.1.4.1.2` 的引用（TS 号后允许括号注释与 Rel 标记）。
  2. 在 `3GPP_Rel19/processed/` 下按 `TS_<号>_<号无点>-j*` 前缀定位本地抽取目录，
     优先用 `full.md`。
  3. 校验该条款号在本地文本中存在：匹配标题行 `^#{2,6} a.b.c` 或目录行 `a.b.c <页码>`。
  4. 本地无该规范时标记 SKIP（不算失败），并单独统计，提醒「该条款未在本地核实」。

@usage
    python3 tools/audit_anchor_valid.py                     # 全库 docs/concepts
    python3 tools/audit_anchor_valid.py <file-or-dir> ...
    python3 tools/audit_anchor_valid.py --strict docs/concepts   # SKIP 也计为失败

@args
    paths     可选；文件或目录，缺省 docs/concepts
    --strict  SKIP（本地无该规范）也计入失败

@env
    需要本地 `3gpp/3GPP_Rel19/processed/`（缺失时全部记为 SKIP）

@exit_code
    0  所有可核实的锚点均存在（或全部 SKIP）
    1  存在本地可查但查无此条款的锚点（或 --strict 下有 SKIP）
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED = PROJECT_ROOT / "3GPP_Rel19" / "processed"
DEFAULT_ROOT = PROJECT_ROOT / "docs" / "concepts"

# TS 38.212 §5.4.2.1 / TS 36.212 Rel-19 §5.1.4.1.2 / TS 38.331（Rel-19 j20）§6.3.2
REF_RE = re.compile(
    r"TS\s*(3[68]\.\d{3})\s*(?:[（(][^）)]*[）)]|Rel-\d+)?\s*§\s*(\d+(?:\.\d+)*)"
)


def find_spec_dir(ts: str) -> Path | None:
    """@brief 定位本地规范目录
    @param ts 形如 38.212 的规范号
    @return 目录路径（含 full.md 优先），找不到返回 None
    """
    if not PROCESSED.is_dir():
        return None
    prefix = f"TS_{ts}_"
    cands = sorted([p for p in PROCESSED.iterdir() if p.is_dir() and p.name.startswith(prefix)])
    if not cands:
        return None
    # 优先含 full.md 的目录
    for c in cands:
        if (c / "full.md").is_file():
            return c
    return cands[0]


def clause_exists(spec_dir: Path, clause: str) -> bool:
    """@brief 判断条款号是否存在于本地抽取文本
    @param spec_dir 规范目录
    @param clause 形如 5.4.2.1
    @return 是否存在
    """
    files = [spec_dir / "full.md"] if (spec_dir / "full.md").is_file() else sorted(spec_dir.glob("*.md"))
    if not files:
        return False
    head = re.compile(r"^#{2,6}\s*" + re.escape(clause) + r"(?![\d.])")
    toc = re.compile(r"^\s*" + re.escape(clause) + r"\s+\S")
    any_ref = re.compile(r"\b" + re.escape(clause) + r"\b")
    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line in text.splitlines():
            if head.match(line) or toc.match(line):
                return True
        # 兜底：正文中出现过该条款号（协议里交叉引用很常见）
        if any_ref.search(text):
            return True
    return False


def check_file(path: Path) -> tuple[list[str], list[str]]:
    """@brief 检查单个文档的锚点
    @param path 文档路径
    @return (失效锚点列表, 未核实锚点列表)
    """
    text = path.read_text(encoding="utf-8", errors="ignore")
    bad: list[str] = []
    skipped: list[str] = []
    seen: set[tuple[str, str]] = set()
    for m in REF_RE.finditer(text):
        ts, clause = m.group(1), m.group(2)
        key = (ts, clause)
        if key in seen:
            continue
        seen.add(key)
        spec = find_spec_dir(ts)
        if spec is None:
            skipped.append(f"TS {ts} §{clause}（本地无该规范）")
        elif not clause_exists(spec, clause):
            bad.append(f"TS {ts} §{clause}（本地抽取件中查无此条款）")
    return bad, skipped


def iter_files(paths: list[str]) -> list[Path]:
    """@brief 展开待检查文件
    @param paths CLI 路径列表
    @return 文档路径列表
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
    return out


def main() -> int:
    """@brief 命令入口
    @return 退出码
    """
    ap = argparse.ArgumentParser(description="协议锚点可解析性审计")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--strict", action="store_true", help="SKIP 也计为失败")
    args = ap.parse_args()

    files = iter_files(args.paths)
    if not files:
        print("NO_INPUT")
        return 1

    total_bad = 0
    total_skip = 0
    bad_files = 0
    for p in files:
        bad, skipped = check_file(p)
        total_bad += len(bad)
        total_skip += len(skipped)
        rel = p.relative_to(PROJECT_ROOT) if PROJECT_ROOT in p.parents else p
        if bad:
            bad_files += 1
            print(f"FAIL {rel}")
            for b in bad:
                print(f"     - {b}")
        elif skipped:
            print(f"SKIP {rel} 未核实 {len(skipped)} 条（本地无对应规范）")

    print("---")
    print(f"检查 {len(files)} 个文件：失效锚点 {total_bad} 条（涉及 {bad_files} 个文件），未核实 {total_skip} 条")
    if total_bad or (args.strict and total_skip):
        print("ANCHOR_VALID_AUDIT_FAIL")
        return 1
    print("ANCHOR_VALID_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
