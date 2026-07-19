#!/usr/bin/env python3
"""Triage whether lessons look like teachable notes rather than protocol indexes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "## 本节学习目标",
    "## 前置知识检查",
    "## 自测题",
    "## 自测题参考答案",
    "## 资料与协议边界",
    "## 执行与证据记录",
    "## 参考文献",
]

THEORY_HINTS = [
    "名称",
    "来源",
    "历史",
    "解决",
    "问题",
    "误解",
    "直观",
    "例子",
    "手算",
    "定义",
    "推导",
    "符号",
    "接收端",
    "工程后果",
]

BOUNDARY_PATTERNS = [
    "只定位",
    "只作为",
    "只标出",
    "不展开",
    "不复现",
    "不要求",
    "未核验",
    "待后续",
    "后续.*再",
    "后续.*展开",
    "后续.*精读",
    "留到",
]


def audit_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []
    for section in REQUIRED_SECTIONS:
        if section not in text:
            findings.append(f"{path}: missing required section {section}")

    theory_score = sum(text.count(hint) for hint in THEORY_HINTS)
    boundary_score = sum(len(re.findall(pattern, text)) for pattern in BOUNDARY_PATTERNS)
    protocol_hits = len(re.findall(r"TS\s+3[68]\.\d+|§\d|Table\s+\d|协议定位|协议证据", text))
    chars = len(text)

    if chars < 9000:
        findings.append(f"{path}: very short lesson ({chars} chars)")
    if theory_score < 16:
        findings.append(f"{path}: weak zero-foundation theory signals (score={theory_score})")
    if protocol_hits >= 20 and theory_score < 24:
        findings.append(
            f"{path}: protocol-index risk (protocol_hits={protocol_hits}, theory_score={theory_score})"
        )
    if boundary_score >= 12:
        findings.append(f"{path}: too many deferral/boundary phrases (count={boundary_score})")

    # A lesson can be long but still thin if it has no concrete example language.
    if not re.search(r"手算例子|数值例子|教学例子|小型.*例子|例题", text):
        findings.append(f"{path}: missing concrete worked example marker")

    return findings


def iter_markdown(paths: list[Path]) -> list[Path]:
    """Collect lesson .md files, recursing into subdirectories."""
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("T*.md")))
    return sorted(set(files))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="return non-zero when triage findings are present",
    )
    args = parser.parse_args()

    findings: list[str] = []
    for path in iter_markdown(args.paths):
        findings.extend(audit_file(path))

    if findings:
        print("LESSON_DEPTH_AUDIT_TRIAGE")
        print("\n".join(findings))
        return 1 if args.strict else 0

    print("LESSON_DEPTH_AUDIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
