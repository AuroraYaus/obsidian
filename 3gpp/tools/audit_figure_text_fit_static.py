#!/usr/bin/env python3
"""
@file    audit_figure_text_fit_static.py
@brief   静态审计 Python 教学图脚本中的文本适配风险。
         检测长文本直接传入 draw.text()、静默截断切片、字符级换行等常见
         PIL 文字溢出/裁剪陷阱——这些是迄今为止最频繁的文本渲染错误来源。
@date    2026-07-22

Static audit for Python figure text-fit risks.

The audit is conservative: it flags patterns that often caused clipped or
silently deleted labels in PIL-generated teaching figures. Intentional short
labels can be exempted with a nearby ``TEXT_FIT_OK:`` comment.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_ROOT = Path("tools/figures")
EXEMPT_MARKER = "TEXT_FIT_OK:"
LONG_TEXT_CHARS = 72
LAYOUT_GUARD_TOKENS = (
    "bottom_margin",
    "title_to_node",
    "flow_to_table",
    "assert_text",
    "assert_box",
    "assert_layout",
    "fit",
    "bbox",
)


@dataclass(frozen=True)
class Finding:
    """
    @brief   不可变的审计发现数据结构。
             使用 frozen dataclass 确保发现的完整性——发现一旦创建不可修改，
             避免在聚合/排序/过滤过程中被意外篡改。
    """
    path: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        """
        @brief   将发现格式化为 "path:line: rule: message" 标准输出格式。
                 统一格式化接口，确保所有发现以一致的格式写入终端和日志。
        @return  格式化后的发现字符串。
        """
        return f"{self.path}:{self.line}: {self.rule}: {self.message}"


def iter_python_files(paths: list[Path]) -> list[Path]:
    """
    @brief   从路径列表中递归收集所有 .py 文件。
             递归遍历子目录，确保深层嵌套的渲染脚本也能被审计覆盖。
    @param   paths  路径列表，可混合目录和文件。
    @return  去重排序后的 .py 文件路径列表。
    """
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.py")))
        elif path.suffix == ".py":
            files.append(path)
    return sorted(dict.fromkeys(files))


def has_nearby_exemption(lines: list[str], line_no: int, radius: int = 2) -> bool:
    """
    @brief   检查指定行附近是否有 TEXT_FIT_OK: 豁免标记。
             允许开发者对确实无风险的短标签行标记豁免，避免误报。
    @param   lines    文件按行分割的列表。
    @param   line_no  目标行号（1-based）。
    @param   radius   检查半径（行），默认 ±2 行。
    @return  若半径范围内存在豁免标记则返回 True，否则返回 False。
    """
    start = max(0, line_no - radius - 1)
    end = min(len(lines), line_no + radius)
    return any(EXEMPT_MARKER in lines[i] for i in range(start, end))


def is_truncating_subscript(node: ast.Subscript) -> bool:
    """
    @brief   检查 AST 下标节点是否为可能导致静默截断的切片操作。
             Python 切片 mylist[:N] 会静默截断超出部分——如果用于文本行列表，
             超出 N 行的文字会被无声删除，是教学图中文字丢失的常见根因。
    @param   node  AST Subscript 节点。
    @return  若切片上界是整数常量（存在截断风险）则返回 True。
    """
    if not isinstance(node.slice, ast.Slice):
        return False
    upper = node.slice.upper
    if upper is None:
        return False
    if isinstance(upper, ast.Constant) and isinstance(upper.value, int):
        return True
    return False


def call_name(node: ast.AST) -> str:
    """
    @brief   从 AST 节点提取可调用的名称字符串。
             递归处理属性链（如 draw.text）和简单变量名，统一返回完整调用路径。
    @param   node  AST 节点。
    @return  调用的完整名称字符串（如 "ImageDraw.ImageDraw.text"），
             无法解析时返回空字符串。
    """
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{call_name(node.value)}.{node.attr}"
    return ""


def literal_string_arg(node: ast.Call) -> str | None:
    """
    @brief   从 AST 函数调用中提取第一个字符串字面量参数。
             用于检测 draw.text("very long string...") 这类直接将长文本
             硬编码传入的情况。
    @param   node  AST Call 节点。
    @return  字符串字面量值，若不存在则返回 None。
    """
    for arg in node.args:
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            return arg.value
    for keyword in node.keywords:
        if isinstance(keyword.value, ast.Constant) and isinstance(keyword.value.value, str):
            return keyword.value.value
    return None


def function_ranges(tree: ast.AST) -> list[tuple[int, int, str]]:
    """
    @brief   提取 AST 树中所有函数定义的起止行号和名称。
             用于后续确定任意行号属于哪个函数，辅助上下文感知的审计判断。
    @param   tree  完整的 AST 语法树。
    @return  三元组列表：(起始行号, 结束行号, 函数名)。
    @note    Python 3.8 之前没有 end_lineno 属性，回退到 lineno。
    """
    ranges: list[tuple[int, int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            ranges.append((node.lineno, getattr(node, "end_lineno", node.lineno), node.name))
    return ranges


def enclosing_function_name(ranges: list[tuple[int, int, str]], line_no: int) -> str:
    """
    @brief   确定指定行号所属的包裹函数名。
             用于判断当前审计位置是否在 wrap/line 等文本处理函数内部，
             以决定是否触发字符级换行检测。
    @param   ranges   函数范围列表。
    @param   line_no  目标行号（1-based）。
    @return  包含该行的函数名；若不在任何函数中则返回空字符串。
    """
    for start, end, name in sorted(ranges, key=lambda item: item[0], reverse=True):
        if start <= line_no <= end:
            return name
    return ""


def audit_ast(path: Path, tree: ast.AST, lines: list[str]) -> list[Finding]:
    """
    @brief   基于 AST 对单个 Python 脚本执行文本适配审计。
             检查三项核心风险：(1) 逐字符换行（切断英文/协议缩写），
             (2) 静默切片截断（丢失文本行），(3) 长文本直接传入 draw.text()，
             (4) 固定文本/表格高度过小（bbox 驱动布局缺失）。
    @param   path   被审计脚本的文件路径。
    @param   tree   脚本的 AST 语法树。
    @param   lines  脚本文件按行分割的列表（用于豁免标记检查）。
    @return  文本适配审计发现列表。
    @note    所有发现都会先检查 TEXT_FIT_OK: 豁免标记——若发现行附近存在豁免
             标记，则不报告该问题。
    """
    findings: list[Finding] = []
    ranges = function_ranges(tree)
    for node in ast.walk(tree):
        line_no = getattr(node, "lineno", 1)
        if has_nearby_exemption(lines, line_no):
            continue

        if isinstance(node, ast.For):
            target = call_name(node.target)
            iter_name = call_name(node.iter)
            function_name = enclosing_function_name(ranges, line_no).lower()
            is_wrapping_function = "wrap" in function_name or "line" in function_name
            is_tokenizer = "token" in function_name
            if iter_name == "text" and re.search(r"^(ch|char|c)$", target) and is_wrapping_function and not is_tokenizer:
                findings.append(
                    Finding(
                        path,
                        line_no,
                        "character_wrap",
                        "wrapping text one character at a time can split English/protocol tokens and hide fit failures",
                    )
                )

        if isinstance(node, ast.Subscript) and is_truncating_subscript(node):
            src = ast.unparse(node) if hasattr(ast, "unparse") else "subscript"
            if re.search(r"(lines|wrapped|splitlines|rows|cell_lines)", src):
                findings.append(
                    Finding(
                        path,
                        line_no,
                        "silent_truncation",
                        f"slice truncation can silently delete drawn text: {src}",
                    )
                )

        if isinstance(node, ast.Call):
            name = call_name(node.func)
            text = literal_string_arg(node)
            if name.endswith(".text") and text and len(text) >= LONG_TEXT_CHARS:
                findings.append(
                    Finding(
                        path,
                        line_no,
                        "long_direct_text",
                        "long literal passed directly to draw.text without visible wrapping or bbox check",
                    )
                )

        if isinstance(node, ast.Assign):
            targets = [call_name(t) for t in node.targets]
            risky_names = {"row_h", "row_height", "line_h", "line_height", "cell_h", "cell_height"}
            if any(t in risky_names or t.endswith(tuple(f".{n}" for n in risky_names)) for t in targets):
                if isinstance(node.value, ast.Constant) and isinstance(node.value.value, int):
                    if node.value.value < 90:
                        findings.append(
                            Finding(
                                path,
                                line_no,
                                "fixed_text_height",
                                f"fixed text/table height {targets[0]}={node.value.value} needs bbox-driven sizing or TEXT_FIT_OK",
                            )
                        )
    return findings


def audit_text_patterns(path: Path, text: str, lines: list[str]) -> list[Finding]:
    """
    @brief   基于正则模式对换行文本进行布局守卫审计。
             检测 draw_wrapped() 等换行文本绘制是否缺少 bbox/fit/margin 等
             布局守卫——无守卫的情况下，换行文本可能超出容器或覆盖相邻元素。
    @param   path   被审计脚本的文件路径。
    @param   text   脚本的完整源代码文本。
    @param   lines  文件按行分割的列表。
    @return  布局守卫缺失的发现列表。
    @note    仅当脚本包含换行相关调用且缺少布局守卫时产生发现。
             每次只报告第一个匹配（用 break），避免对同一脚本重复报告。
    """
    findings: list[Finding] = []
    if "draw_wrapped" not in text and "wrap_lines" not in text and "wrapped" not in text:
        return findings
    if any(token in text for token in LAYOUT_GUARD_TOKENS):
        return findings
    for idx, line in enumerate(lines, start=1):
        if "draw_wrapped(" in line or "wrap_lines(" in line or "draw_centered_wrapped(" in line:
            findings.append(
                Finding(
                    path,
                    idx,
                    "wrapped_without_layout_guard",
                    "wrapped text is drawn without visible bbox/fit/bottom-margin layout guard",
                )
            )
            break
    return findings


def audit_paths(paths: list[Path]) -> list[Finding]:
    """
    @brief   对多个路径下的所有 Python 脚本执行文本适配审计。
             每个文件先做 AST 审计再做正则模式审计，汇总全部发现。
    @param   paths  待审计的路径列表。
    @return  所有文件的所有文本适配发现列表。
    @throws  不会向上抛异常——SyntaxError 被捕获并转为 Finding 报告。
    """
    findings: list[Finding] = []
    for path in iter_python_files(paths):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        try:
            tree = ast.parse(text, filename=str(path))
        except SyntaxError as exc:
            findings.append(Finding(path, exc.lineno or 1, "syntax_error", exc.msg))
            continue
        findings.extend(audit_ast(path, tree, lines))
        findings.extend(audit_text_patterns(path, text, lines))
    return findings


def main(argv: list[str] | None = None) -> int:
    """
    @brief   文本适配静态审计入口——检测渲染脚本中文本溢出、截断和布局缺失。
    @param   argv  命令行参数列表（sys.argv）。
    @usage   python audit_figure_text_fit_static.py [paths...]
    @args    paths  待审计的 .py 文件或目录路径，默认为 tools/figures。
    @exit_code  0 = 无阻断性发现（可能仍有建议性发现），1 = 存在阻断性发现
                （静默截断、语法错误、长文本、固定高度、字符换行、无守卫换行）。
    @note    发现分为阻断性 (blocking) 和建议性 (advisory) 两类。
             只有阻断性发现会导致非零退出码。
             TEXT_FIT_OK: 注释可用于豁免局部行。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=[DEFAULT_ROOT])
    args = parser.parse_args(argv)

    findings = audit_paths(args.paths)
    for finding in findings:
        print(finding.format())
    blocking = [
        f
        for f in findings
        if f.rule
        in {
            "silent_truncation",
            "syntax_error",
            "long_direct_text",
            "fixed_text_height",
            "character_wrap",
            "wrapped_without_layout_guard",
        }
    ]
    if blocking:
        print(
            f"FIGURE_TEXT_FIT_STATIC_AUDIT_FAIL blocking={len(blocking)} advisory={len(findings) - len(blocking)}",
            file=sys.stderr,
        )
        return 1
    if findings:
        print(f"FIGURE_TEXT_FIT_STATIC_AUDIT_OK advisory={len(findings)}")
    else:
        print("FIGURE_TEXT_FIT_STATIC_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
