#!/usr/bin/env python3
"""Audit Markdown headings for formal engineering-lecture style."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


FORBIDDEN_HEADING_PHRASES = [
    "先说",
    "先把",
    "先看",
    "先用",
    "先定位",
    "小故事",
    "你应该",
    "我们来",
    "说清楚",
    "说清",
    "长什么样",
    "是什么",
    "为什么",
    "怎么",
    "怎么办",
    "会怎样",
    "到底",
    "一条线上",
    "平面上",
    "一句话版本",
    "最多两个工业用例",
    "把浮点",
    "变成硬件能保存",
]

EXCLUDED_PARTS = {
    ".git",
    "3GPP_Rel19",
    "docs/archive",
}


def is_excluded(path: Path) -> bool:
    text = path.as_posix()
    return any(part in text for part in EXCLUDED_PARTS)


def iter_markdown(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(p for p in sorted(path.rglob("*.md")) if not is_excluded(p))
        elif path.suffix == ".md" and not is_excluded(path):
            files.append(path)
    return files


def audit_file(path: Path) -> list[str]:
    errors: list[str] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("#"):
            continue
        if not line.lstrip("#").startswith(" "):
            errors.append(
                f"{path}:{line_no}: ATX heading missing space after '#' at: {line}"
            )
            continue
        for phrase in FORBIDDEN_HEADING_PHRASES:
            if phrase in line:
                errors.append(
                    f"{path}:{line_no}: informal heading phrase '{phrase}' in: {line}"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    for path in iter_markdown(args.paths):
        errors.extend(audit_file(path))

    if errors:
        print("MARKDOWN_HEADING_AUDIT_FAIL")
        print("\n".join(errors))
        return 1

    print("MARKDOWN_HEADING_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
