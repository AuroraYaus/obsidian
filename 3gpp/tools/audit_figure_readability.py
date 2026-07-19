#!/usr/bin/env python3
"""Static readability-risk audit for Python-generated curriculum figures."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_PATHS = [Path("tools/figures")]
MIN_TABLE_FONT = 24
MIN_TABLE_ROW_H = 56

FONT_CALL_RE = re.compile(r"font\(\s*(\d+)\s*(?:,|\))")
CONST_RE = re.compile(r"^([A-Z][A-Z0-9_]*)\s*=\s*font\(\s*(\d+)", re.MULTILINE)
TABLE_HINT_RE = re.compile(
    r"(def\s+\w*table\w*\s*\(|row_h|headers|cell\(|draw_cell|Comparison|Descriptor|矩阵|表)",
    re.IGNORECASE,
)
SMALL_TABLE_FONT_RE = re.compile(
    r"(?:cell|draw_cell|center_text|line_centered_text|draw\.text|wrapped|draw_wrapped)"
    r"[\s\S]{0,160}?font\(\s*((?:1[0-9]|2[0-3]))\s*(?:,|\))",
    re.MULTILINE,
)
SMALL_CONST_USE_RE = re.compile(
    r"(?:cell|draw_cell|center_text|line_centered_text|draw\.text|wrapped|draw_wrapped)"
    r"[\s\S]{0,180}?\b([A-Z][A-Z0-9_]*)\b",
    re.MULTILINE,
)
ROW_H_RE = re.compile(r"row_h\s*=\s*(\d+)|row_h:\s*int\s*=\s*(\d+)")
GLOBAL_SMALL_FONT_RE = re.compile(r"font\(\s*(1[3-9]|2[0-3])\s*(?:,|\))")
SMALL_FONT_EXEMPTION_RE = re.compile(
    r"(axis_font|readability-exception|辅助标注|短索引|刻度)",
    re.IGNORECASE,
)


def collect_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_dir():
            files.extend(sorted(path.glob("*.py")))
        elif path.suffix == ".py":
            files.append(path)
    return files


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def audit_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []

    for match in GLOBAL_SMALL_FONT_RE.finditer(text):
        line_start = text.rfind("\n", 0, match.start()) + 1
        line_end = text.find("\n", match.start())
        if line_end == -1:
            line_end = len(text)
        line = text[line_start:line_end]
        if SMALL_FONT_EXEMPTION_RE.search(line):
            continue
        size = int(match.group(1))
        findings.append(
            f"{path}:{line_for_offset(text, match.start())}: figure text uses font({size}); "
            "raise teaching/table text to 24px+ or mark a justified auxiliary-label exception"
        )

    if not TABLE_HINT_RE.search(text):
        return sorted(set(findings))

    constants = {name: int(size) for name, size in CONST_RE.findall(text)}

    for match in SMALL_TABLE_FONT_RE.finditer(text):
        size = int(match.group(1))
        findings.append(
            f"{path}:{line_for_offset(text, match.start())}: table-like drawing uses font({size}); "
            "verify rendered Markdown readability or increase font/row height/split the table"
        )

    for match in SMALL_CONST_USE_RE.finditer(text):
        name = match.group(1)
        size = constants.get(name)
        if size is None or size >= MIN_TABLE_FONT:
            continue
        findings.append(
            f"{path}:{line_for_offset(text, match.start())}: table-like drawing may use {name}=font({size}); "
            "verify rendered Markdown readability or increase font/row height/split the table"
        )

    for match in ROW_H_RE.finditer(text):
        value = int(match.group(1) or match.group(2))
        if value < MIN_TABLE_ROW_H:
            findings.append(
                f"{path}:{line_for_offset(text, match.start())}: row_h={value} is a readability risk for table figures; "
                "increase row height unless this is a tiny axis/tick label table"
            )

    return sorted(set(findings))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_PATHS)
    args = parser.parse_args()

    findings: list[str] = []
    for path in collect_files(args.paths):
        findings.extend(audit_file(path))

    if findings:
        print("FIGURE_READABILITY_AUDIT_FINDINGS")
        print("\n".join(findings))
        return 1

    print("FIGURE_READABILITY_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
