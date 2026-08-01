#!/usr/bin/env python3
"""
@file _md_utils.py
@brief Markdown 审计脚本的共享工具函数
@date 2025

提供 Markdown 文件遍历、代码块剥离、字符偏移到行号的转换等基础能力，
被 tools/ 下所有审计脚本复用。
"""

from __future__ import annotations

import re
from pathlib import Path

CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def strip_code_fences(text: str) -> str:
    """
    @brief 移除 Markdown 文本中的代码块（```...```）

    用等量空行替换代码块内容，保持行号不变，确保后续基于行号的
    审计报告仍能正确定位到源文件中的对应行。

    @param text  原始 Markdown 文本
    @return      代码块替换为空行后的文本，总行数不变
    """
    return CODE_FENCE_RE.sub(lambda match: "\n" * match.group(0).count("\n"), text)


def line_for_offset(text: str, offset: int) -> int:
    """
    @brief 将字符偏移量转换为 1-based 行号

    统计 offset 之前的换行符数量，加 1 得到对应行号。

    @param text    完整的文本内容
    @param offset  字符偏移量（0-based）
    @return        1-based 行号
    @note          offset 超出文本长度时返回最后一行的行号
    """
    return text.count("\n", 0, offset) + 1


def iter_markdown(paths: list[Path]) -> list[Path]:
    """
    @brief 从给定的路径列表中收集所有 .md 文件

    对每个路径：如果是 .md 文件则直接加入；如果是目录则递归收集
    其下所有 .md 文件。结果去重排序后返回。

    @param paths  文件或目录的 Path 列表
    @return       去重并排序后的 .md 文件 Path 列表
    """
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(set(files))
