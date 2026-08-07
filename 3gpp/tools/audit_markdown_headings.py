#!/usr/bin/env python3
"""@file audit_markdown_headings.py
@brief 审计 Markdown 讲义的标题格式——禁止口语化、问答式、故事化标题，
       确保所有标题符合正式工程讲义风格（禁止短语、ATX 空格规范）。
@date 2026-07-22

本项目规则要求标题必须是陈述式表达，不允许出现"先说""是什么""怎么办"
等面向读者的口语结构。本审计强制执行这一写作规范，在 CI 中提供硬阻断。
"""

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
    """@brief  判断路径是否落在审计排除区内（归档、协议原始资料等）。
    @param  path  待判断的文件路径。
    @return       True 表示该文件不应被审计。"""
    text = path.as_posix()
    return any(part in text for part in EXCLUDED_PARTS)


def iter_markdown(paths: list[Path]) -> list[Path]:
    """@brief  从输入路径列表中递归收集所有需审计的 Markdown 文件。
    @param  paths  用户提供的文件或目录路径列表。
    @return        去重后的 `.md` 文件路径列表。
    @note   自动跳过排除区目录和文件，避免误报归档内容。"""
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(p for p in sorted(path.rglob("*.md")) if not is_excluded(p))
        elif path.suffix == ".md" and not is_excluded(path):
            files.append(path)
    return files


def audit_file(path: Path) -> list[str]:
    """@brief  对单文件执行标题格式审计：
              1) ATX 标题 `#` 后必须有一个空格（Markdown 标准）
              2) 标题中不得包含口语化禁止短语。
    @param  path  待审计的 Markdown 文件路径。
    @return       违规行列表；空列表表示标题格式完全合规。
    @note   检查顺序为"空格→短语"：空格违规先报，避免修正后再报短语。"""
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
    """@brief    脚本入口：审计讲义的 Markdown 标题是否满足正式工程写作规范。
    @usage    python audit_markdown_headings.py <path> [<path> ...]
    @args     paths  一个或多个 Markdown 文件或目录路径。
    @env      无外部依赖（仅标准库）
    @exit_code        0 = 所有标题合规；1 = 发现口语化标题或格式违规。
    @note    排除 `.git`、`3GPP_Rel19`、`docs/archive` 等非讲义路径。"""
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
