#!/usr/bin/env python3
"""Remove a named column from Markdown pipe tables."""

from __future__ import annotations

import argparse
from pathlib import Path


def split_row(line: str) -> list[str] | None:
    stripped = line.rstrip("\n")
    if not stripped.lstrip().startswith("|") or "|" not in stripped[1:]:
        return None
    cells = stripped.strip().strip("|").split("|")
    return [cell.strip() for cell in cells]


def is_separator(cells: list[str]) -> bool:
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
    return "| " + " | ".join(cells) + " |"


def remove_column(text: str, column_name: str) -> tuple[str, int]:
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
