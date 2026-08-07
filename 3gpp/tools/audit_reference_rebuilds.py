#!/usr/bin/env python3
"""@file audit_reference_rebuilds.py
@brief 在讲义中定位需要手动审查的参考文献/表格/公式重建候选行——
       这不是硬阻断审计，而是 triage（分诊）工具：
       标记出可能违反"依赖的有效内容必须在正文中重建"规则的行。
@date 2026-07-22

扫描四种风险模式：
1. 未核验/待核验/不复现/未展开标记 → 内容可能缺失
2. 引用 Table/Figure/图表 → 外部材质未重建
3. 论文引用 [Author, YYYY] → 依赖外部文献的公式/算法
4. 公式/方程/算法框图引用 → 数学内容未在正文中重建

安全边界（SAFE_HINTS）中的行默认跳过：如"背景阅读""未引用具体公式"
等明确声明不依赖的标记。输出供人工审查决策。
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


RISK_PATTERNS = [
    ("unverified", re.compile(r"未核验|待核验|不复现|不展开|抽取不完整")),
    # 表/图引用加词边界：前非数字/字母/汉字（排除"代表2""量表3"等词内子串），
    # 后非数字（排除"表123"这类长数字段）
    ("table_or_figure", re.compile(r"\bTable\b|\bFigure\b|(?<![0-9A-Za-z一-鿿])表\s*\d(?![0-9])|图\s*\d|图表")),
    ("paper_citation", re.compile(r"\[[A-Z][A-Za-z]+(?:\s+and\s+[A-Z][A-Za-z]+|\s+et\s+al\.)?,\s*\d{4}\]")),
    ("formula_ref", re.compile(r"公式|方程|equation|多项式|生成多项式|算法框图")),
]

SAFE_HINTS = re.compile(r"背景阅读|未引用该文献的具体公式|不声明等同|教学例子|只作为.*入口")


def iter_markdown(paths: list[Path]) -> list[Path]:
    """@brief  从输入路径中收集所有 .md 文件，去重排序。
    @param  paths  文件或目录路径列表。
    @return        去重排序后的 Markdown 文件路径列表。"""
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(set(files))


def main() -> int:
    """@brief    脚本入口：扫描讲义中的引用/表格/公式重建候选行。
    @usage    python audit_reference_rebuilds.py <path> [<path> ...] [--context-safe]
    @args     paths            一个或多个 Markdown 文件或目录路径。
    @args     --context-safe   同时输出安全边界提示行（背景阅读等），
                               默认跳过这些行以减少噪音。
    @env      无外部依赖（仅标准库）
    @exit_code                 始终返回 0（分诊工具，不做硬阻断）。
    @note    输出格式：`<file>:<line>: [<risk_type>] <content>`。"""
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
