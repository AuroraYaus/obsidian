#!/usr/bin/env python3
"""Shared utilities for Markdown-based audit scripts."""

from __future__ import annotations

import re
from pathlib import Path

CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def strip_code_fences(text: str) -> str:
    """Remove code fences, preserving line count for accurate line numbers."""
    return CODE_FENCE_RE.sub(lambda match: "\n" * match.group(0).count("\n"), text)


def line_for_offset(text: str, offset: int) -> int:
    """Return 1-based line number for a character offset in text."""
    return text.count("\n", 0, offset) + 1


def iter_markdown(paths: list[Path]) -> list[Path]:
    """Collect .md files from paths, recursing into directories."""
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(set(files))