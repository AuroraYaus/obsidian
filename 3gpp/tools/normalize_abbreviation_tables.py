#!/usr/bin/env python3
"""Ensure lesson abbreviation tables contain all used standard terms."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from audit_lesson_terms import TECH_TERM_RE, TECH_TERMS, strip_code_fences


def used_terms(text: str) -> list[str]:
    stripped = strip_code_fences(text)
    return [abbr for abbr in TECH_TERMS if TECH_TERM_RE[abbr].search(stripped)]


def normalize_table(text: str) -> tuple[str, int]:
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
