#!/usr/bin/env python3
"""Audit Markdown LaTeX formulas and verify KaTeX can render them."""

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
    path: Path
    line: int
    body: str
    display: bool


def extract_formulas(path: Path) -> tuple[list[Formula], list[str]]:
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
