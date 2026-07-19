#!/usr/bin/env python3
"""Find citation/table/figure rebuild candidates in roadmap lessons.

This is a triage tool, not a hard pass/fail gate. It prints lines that deserve
manual review under the project rule: formulas, tables, figures, and algorithms
that a lesson actually depends on must be rebuilt in the body or explicitly
marked as background-only.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


RISK_PATTERNS = [
    ("unverified", re.compile(r"未核验|待核验|不复现|不展开|抽取不完整")),
    ("table_or_figure", re.compile(r"\bTable\b|\bFigure\b|表\s*\d|图\s*\d|图表")),
    ("paper_citation", re.compile(r"\[[A-Z][A-Za-z]+(?:\s+and\s+[A-Z][A-Za-z]+|\s+et\s+al\.)?,\s*\d{4}\]")),
    ("formula_ref", re.compile(r"公式|方程|equation|多项式|生成多项式|算法框图")),
]

SAFE_HINTS = re.compile(r"背景阅读|未引用该文献的具体公式|不声明等同|教学例子|只作为.*入口")


def iter_markdown(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(set(files))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--context-safe", action="store_true", help="also print lines that contain safe boundary hints")
    args = parser.parse_args()

    hits: list[tuple[str, Path, int, str]] = []
    for path in iter_markdown(args.paths):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = line.strip()
            if not stripped:
                continue
            if SAFE_HINTS.search(stripped) and not args.context_safe:
                continue
            for label, pattern in RISK_PATTERNS:
                if pattern.search(stripped):
                    hits.append((label, path, lineno, stripped))
                    break

    if not hits:
        print("REFERENCE_REBUILD_AUDIT_NO_CANDIDATES")
        return 0

    print("REFERENCE_REBUILD_AUDIT_CANDIDATES")
    for label, path, lineno, line in hits:
        print(f"{path}:{lineno}: [{label}] {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
