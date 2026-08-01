#!/usr/bin/env python3
"""
@file    audit_latex_render.py
@brief   审计 Markdown 讲义中的 LaTeX 公式，验证 KaTeX 能否正确渲染。
         检测不平衡的块级公式定界符、多行内联数学模式、公式标签连续性、
         以及使用外部 KaTeX 二进制文件的实际渲染错误——这是确保所有
         数学表达式在 Obsidian 和 Web 平台上都能正常显示的最终防线。
@date    2026-07-22

Audit Markdown LaTeX formulas and verify KaTeX can render them.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from _md_utils import iter_markdown, line_for_offset, strip_code_fences


BLOCK_RE = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", re.DOTALL)


@dataclass
class Formula:
    """
    @brief   一条从 Markdown 文件中提取的 LaTeX 公式记录。
             使用可变 dataclass（非 frozen）以便在聚合后按需修改。
    """
    path: Path
    line: int
    body: str
    display: bool


def extract_formulas(path: Path) -> tuple[list[Formula], list[str]]:
    """
    @brief   从单个 Markdown 文件中提取所有 LaTeX 公式。
             解析 $$ 块级公式和 $ 内联公式，屏蔽代码围栏区域，
             同时检查定界符平衡、多行内联违规和标签连续性。
    @param   path  Markdown 文件路径。
    @return  (公式列表, 错误列表) 二元组。
             公式列表包含所有成功提取的 Formula 对象；
             错误列表包含定界符不平衡、多行内联、标签不连续等语法问题。
    @note    先提取 $$ 块公式区域并将其替换为空格，再在剩余文本中提取 $ 内联公式，
             避免块公式内部的 $ 符号被误判为内联公式。
    """
    raw = path.read_text(encoding="utf-8")
    text = strip_code_fences(raw)
    errors: list[str] = []
    formulas: list[Formula] = []

    if text.count("$$") % 2:
        errors.append(f"{path}: unbalanced block math fences '$$' count={text.count('$$')}")

    block_spans: list[tuple[int, int]] = []
    for match in BLOCK_RE.finditer(text):
        body = match.group(1).strip()
        block_spans.append(match.span())
        formulas.append(Formula(path, line_for_offset(text, match.start()), body, True))

    masked = list(text)
    for start, end in block_spans:
        for idx in range(start, end):
            if masked[idx] != "\n":
                masked[idx] = " "
    no_blocks = "".join(masked)

    for match in INLINE_RE.finditer(no_blocks):
        body = match.group(1).strip()
        if not body:
            continue
        if "\n" in body:
            errors.append(
                f"{path}:{line_for_offset(no_blocks, match.start())}: multiline inline math; use $$ block"
            )
            continue
        formulas.append(Formula(path, line_for_offset(no_blocks, match.start()), body, False))

    tags = [int(x) for x in re.findall(r"\\tag\{(\d+)\}", text)]
    if tags and tags != list(range(1, len(tags) + 1)):
        errors.append(f"{path}: non-contiguous formula tags {tags}")

    return formulas, errors


def render_with_katex(formula: Formula, katex_bin: str) -> str | None:
    """
    @brief   使用外部 KaTeX CLI 二进制文件验证单条公式的实际渲染。
             将公式写入临时 .tex 文件，调用 katex 命令行工具，
             捕获渲染错误——返回渲染失败信息而非让错误沉默。
    @param   formula   待验证的公式对象。
    @param   katex_bin  KaTeX 二进制文件路径或命令名。
    @return  若渲染成功返回 None；若失败返回格式化的错误消息字符串。
    @note    使用 subprocess 调用外部进程，设置 10 秒超时防止挂起。
             临时文件在 finally 块中确保删除（含 missing_ok 处理）。
    """
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".tex", delete=False) as handle:
        handle.write(formula.body)
        input_path = Path(handle.name)
    try:
        cmd = [katex_bin, "--input", str(input_path)]
        if formula.display:
            cmd.append("--display-mode")
        proc = subprocess.run(cmd, text=True, capture_output=True, timeout=10)
        if proc.returncode != 0:
            snippet = " ".join(formula.body.split())[:160]
            detail = (proc.stderr or proc.stdout).strip().splitlines()
            message = detail[0] if detail else "KaTeX render failed"
            return f"{formula.path}:{formula.line}: KaTeX failed: {message}; formula={snippet!r}"
        return None
    finally:
        input_path.unlink(missing_ok=True)


def main() -> int:
    """
    @brief   LaTeX 渲染审计入口——提取 Markdown 公式并验证 KaTeX 可渲染性。
    @usage   python audit_latex_render.py <paths...> [--katex-bin PATH] [--syntax-only]
    @args    paths         必选，待审计的 Markdown 文件或目录路径。
             --katex-bin   KaTeX CLI 二进制路径，默认为 "katex"。
             --syntax-only 跳过 KaTeX 渲染验证，仅检查定界符/标签/提取。
    @exit_code  0 = 无错误，1 = 存在定界符不平衡、标签不连续或渲染失败。
    @note    需要 katex CLI 二进制文件已安装在 PATH 中。
             --syntax-only 模式可用于快速 CI 预检（不需要完整 LaTeX 环境）。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--katex-bin", default="katex")
    parser.add_argument(
        "--syntax-only",
        action="store_true",
        help="skip KaTeX rendering and only check fences/tags/extraction",
    )
    args = parser.parse_args()

    errors: list[str] = []
    formulas: list[Formula] = []
    for path in iter_markdown(args.paths):
        found, file_errors = extract_formulas(path)
        formulas.extend(found)
        errors.extend(file_errors)

    if not args.syntax_only:
        for formula in formulas:
            error = render_with_katex(formula, args.katex_bin)
            if error:
                errors.append(error)

    if errors:
        print("LATEX_RENDER_AUDIT_FAIL")
        print("\n".join(errors))
        return 1

    print(f"LATEX_RENDER_AUDIT_OK formulas={len(formulas)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
