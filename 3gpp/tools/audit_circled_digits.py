#!/usr/bin/env python3
"""@file audit_circled_digits.py
@brief 检查全库（md/svg/py）是否残留带圈数字序号（U+2460-U+2473 及变体），发现即 FAIL。
@date 2026-08-04
@note 教训来源：2026-08-04 用户要求"禁止使用圈 1 的序号写法"——项目两轮整改中
     带圈数字反复出现（第一次 323 处、第二次 186 处均为子代理/代理写新内容时引入），
     根因是只有一次性替换、没有固化检查规则。序号统一使用 (1)(2)(3) 或 1. 2. 3.。
     带圈数字是 Unicode 字符，在代码/表格/渲染中字体支持不统一，且无法用
     Markdown 有序列表语义表达。
@usage python3 tools/audit_circled_digits.py [路径...]
@args  可选：限定扫描路径（默认 docs/ tools/ sim/）
@exit_code 0 = 无残留，1 = 存在残留
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# 全部圈号变体：U+2460-U+2473（circled 1-20）、U+24EA（circled 0）、
# U+2474-U+247E（parenthesized 1-11）、U+3251-U+325F、U+32B1-U+32BF
CIRCLED = re.compile(r"[\u2460-\u2473\u24EA\u2474-\u247E\u3251-\u325F\u32B1-\u32BF]")


def scan(path: Path) -> list[tuple[int, str]]:
    """@brief 扫描单个文件的带圈数字。
    @param path 文件路径
    @return (行号, 上下文) 列表
    @note 只扫描文本文件（md/svg/py/sh/json/yaml）。"""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []
    hits: list[tuple[int, str]] = []
    for m in CIRCLED.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        ctx = text[max(0, m.start() - 12): m.start() + 12].replace("\n", " ")
        hits.append((line, ctx))
    return hits


def main() -> int:
    """@brief 审计入口。
    @usage python3 tools/audit_circled_digits.py
    @args  可选路径列表（默认 docs tools sim）
    @env   无外部依赖（仅标准库）
    @exit_code 0 = 通过，1 = 存在残留"""
    roots = [Path(p) for p in sys.argv[1:]] or [Path("docs"), Path("tools"), Path("sim")]
    exts = {".md", ".svg", ".py", ".sh", ".json", ".yaml", ".yml"}
    total = 0
    for root in roots:
        for f in sorted(root.rglob("*")):
            if f.suffix not in exts or not f.is_file():
                continue
            hits = scan(f)
            for line, ctx in hits:
                print(f"{f}:{line}: {ctx}")
            total += len(hits)
    if total:
        print(f"CIRCLED_DIGIT_AUDIT_FAIL total={total} —— 序号统一使用 (1)(2)(3) 或 1. 2. 3.")
        return 1
    print("CIRCLED_DIGIT_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
