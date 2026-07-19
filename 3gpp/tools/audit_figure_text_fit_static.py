#!/usr/bin/env python3
"""Static audit for Python figure text-fit risks.

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
    path: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.path}:{self.line}: {self.rule}: {self.message}"


def iter_python_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.py")))
        elif path.suffix == ".py":
            files.append(path)
    return sorted(dict.fromkeys(files))


def has_nearby_exemption(lines: list[str], line_no: int, radius: int = 2) -> bool:
    start = max(0, line_no - radius - 1)
    end = min(len(lines), line_no + radius)
    return any(EXEMPT_MARKER in lines[i] for i in range(start, end))


def is_truncating_subscript(node: ast.Subscript) -> bool:
    if not isinstance(node.slice, ast.Slice):
        return False
    upper = node.slice.upper
    if upper is None:
        return False
    if isinstance(upper, ast.Constant) and isinstance(upper.value, int):
        return True
    return False


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{call_name(node.value)}.{node.attr}"
    return ""


def literal_string_arg(node: ast.Call) -> str | None:
    for arg in node.args:
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            return arg.value
    for keyword in node.keywords:
        if isinstance(keyword.value, ast.Constant) and isinstance(keyword.value.value, str):
            return keyword.value.value
    return None


def function_ranges(tree: ast.AST) -> list[tuple[int, int, str]]:
    ranges: list[tuple[int, int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            ranges.append((node.lineno, getattr(node, "end_lineno", node.lineno), node.name))
    return ranges


def enclosing_function_name(ranges: list[tuple[int, int, str]], line_no: int) -> str:
    for start, end, name in sorted(ranges, key=lambda item: item[0], reverse=True):
        if start <= line_no <= end:
            return name
    return ""


def audit_ast(path: Path, tree: ast.AST, lines: list[str]) -> list[Finding]:
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
