#!/usr/bin/env python3
"""Audit that Python-rendered figure elements are represented in Markdown.

The audit is intentionally stricter than the earlier body-equivalent check:
it extracts visible text-like elements from figure render scripts and requires
the corresponding lesson body to cover each one. Chinese prose is allowed, but
the script text must still be recoverable through key terms or configured
aliases.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_LEDGER = Path("docs/audits/python_figure_to_body_content_migration.md")
RENDER_CALLS = {"text", "card", "centered", "draw_table", "box"}
NON_VISIBLE_KEYWORDS = {
    "anchor",
    "align",
    "direction",
    "embedded_color",
    "fill",
    "font",
    "gap",
    "language",
    "layout_engine",
    "outline",
    "radius",
    "spacing",
    "stroke_fill",
}
MIN_TOKEN_LEN = 2
SKIP_TEXTS = {
    "",
    "-",
    "#fff",
    "#ffffff",
    "white",
    "black",
}
ENGLISH_STOPWORDS = {
    "and",
    "or",
    "the",
    "a",
    "an",
    "to",
    "of",
    "in",
    "on",
    "for",
    "with",
    "by",
    "from",
    "is",
    "are",
    "as",
    "new",
    "old",
    "current",
    "optional",
}
TERM_ALIASES = {
    "accumulates": ("累加",),
    "access": ("访问",),
    "argmin": ("argmin",),
    "avoids": ("避免",),
    "bank": ("bank",),
    "banks": ("banks", "bank"),
    "connection": ("连接",),
    "debug": ("调试",),
    "descriptor": ("descriptor",),
    "edge": ("edge", "边"),
    "equal": ("一致", "等价"),
    "excludes": ("排除",),
    "forever": ("无限",),
    "hardware": ("硬件",),
    "hash": ("hash",),
    "keeps": ("保证", "保持"),
    "latch": ("锁存",),
    "matters": ("重要",),
    "message": ("message", "消息"),
    "min1": ("min1",),
    "min2": ("min2",),
    "object": ("对象",),
    "parallel": ("并行",),
    "replaces": ("替换",),
    "required": ("必须",),
    "schedule": ("schedule", "调度"),
    "sign": ("sign", "符号"),
    "target": ("目标",),
    "trace": ("trace",),
    "why": ("为什么",),
}


@dataclass(frozen=True)
class Finding:
    script: Path
    lesson: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.lesson}:{self.line}: {self.rule}: {self.script}: {self.message}"


@dataclass(frozen=True)
class Element:
    text: str
    line: int
    source: str


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def flatten_strings(value: ast.AST) -> list[str]:
    if isinstance(value, ast.Constant) and isinstance(value.value, str):
        return [value.value]
    if isinstance(value, ast.JoinedStr):
        parts = []
        for item in value.values:
            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                parts.append(item.value)
        return ["".join(parts)] if parts else []
    if isinstance(value, (ast.List, ast.Tuple, ast.Set)):
        out: list[str] = []
        for item in value.elts:
            out.extend(flatten_strings(item))
        return out
    if isinstance(value, ast.Dict):
        out: list[str] = []
        for item in list(value.keys) + list(value.values):
            if item is not None:
                out.extend(flatten_strings(item))
        return out
    return []


def is_visible_text(text: str) -> bool:
    text = normalize_text(text)
    if text in SKIP_TEXTS:
        return False
    if text.startswith("#") and re.fullmatch(r"#[0-9A-Fa-f]{3,8}", text):
        return False
    if re.fullmatch(r"[(),.\d\s-]+", text):
        return False
    if text.endswith((".png", ".py", ".ttf", ".ttc")):
        return False
    return bool(re.search(r"[A-Za-z\u4e00-\u9fff]", text))


def call_name(node: ast.Call) -> str:
    func = node.func
    if isinstance(func, ast.Attribute):
        return func.attr
    if isinstance(func, ast.Name):
        return func.id
    return ""


def extract_elements(script: Path) -> list[Element]:
    tree = ast.parse(script.read_text(encoding="utf-8"), filename=str(script))
    elements: list[Element] = []

    for node in ast.walk(tree):
        strings: list[str] = []
        source = type(node).__name__
        if isinstance(node, ast.Call) and call_name(node) in RENDER_CALLS:
            source = f"call:{call_name(node)}"
            for arg in node.args:
                strings.extend(flatten_strings(arg))
            for keyword in node.keywords:
                if keyword.arg in NON_VISIBLE_KEYWORDS:
                    continue
                strings.extend(flatten_strings(keyword.value))
        elif isinstance(node, ast.Assign):
            target_names = {target.id for target in node.targets if isinstance(target, ast.Name)}
            if any(name in target_names for name in {"title", "subtitle", "titles", "bodies", "rows", "headers", "fsm_titles", "fsm_bodies"}):
                source = "assignment"
                strings.extend(flatten_strings(node.value))

        for text in strings:
            text = normalize_text(text)
            if is_visible_text(text):
                elements.append(Element(text=text, line=getattr(node, "lineno", 1), source=source))

    return dedupe_elements(elements)


def dedupe_elements(elements: list[Element]) -> list[Element]:
    seen: set[str] = set()
    out: list[Element] = []
    for element in elements:
        key = element.text.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(element)
    return out


def split_terms(text: str) -> list[str]:
    text = text.replace("/", " ")
    raw_terms = re.findall(r"[A-Za-z][A-Za-z0-9_-]*|[0-9]+(?:\.[0-9]+)*|[\u4e00-\u9fff]+", text)
    terms: list[str] = []
    for term in raw_terms:
        clean = term.strip(".,;:()[]{}")
        if len(clean) < MIN_TOKEN_LEN:
            continue
        if clean.lower() in ENGLISH_STOPWORDS:
            continue
        terms.append(clean)
    return terms


def term_present(term: str, lesson_text: str) -> bool:
    candidates = (term,) + TERM_ALIASES.get(term.lower(), ())
    return any(candidate_present(candidate, lesson_text) for candidate in candidates)


def candidate_present(term: str, lesson_text: str) -> bool:
    if re.search(r"[\u4e00-\u9fff]", term):
        return term in lesson_text
    return re.search(rf"(?<![A-Za-z0-9_]){re.escape(term)}(?![A-Za-z0-9_])", lesson_text, re.IGNORECASE) is not None


def element_covered(element: Element, lesson_text: str) -> bool:
    text = element.text
    if text in lesson_text:
        return True
    terms = split_terms(text)
    if not terms:
        return True
    required = max(1, min(len(terms), 4))
    present = sum(1 for term in terms if term_present(term, lesson_text))
    return present >= required


def audit_pair(script: Path, lesson: Path) -> list[Finding]:
    lesson_text = lesson.read_text(encoding="utf-8")
    findings: list[Finding] = []
    for element in extract_elements(script):
        if not element_covered(element, lesson_text):
            findings.append(
                Finding(
                    script=script,
                    lesson=lesson,
                    line=element.line,
                    rule="missing_visible_text_element",
                    message=f"{element.text!r} from {element.source} is not covered in lesson body",
                )
            )
    return findings


def parse_ledger_rows(ledger: Path) -> list[tuple[Path, Path]]:
    rows: list[tuple[Path, Path]] = []
    if not ledger.exists():
        return rows
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        lesson = cells[0].strip("`")
        scripts = cells[2].strip("`")
        status = cells[4]
        if "body_text_represented" not in status:
            continue
        for script in [part.strip() for part in scripts.split(",")]:
            if script.startswith("tools/figures/") and script.endswith(".py"):
                rows.append((Path(script), Path(lesson)))
    return sorted(set(rows))


def audit_ledger(ledger: Path = DEFAULT_LEDGER) -> list[Finding]:
    findings: list[Finding] = []
    for script, lesson in parse_ledger_rows(ledger):
        if not script.exists() or not lesson.exists():
            continue
        findings.extend(audit_pair(script, lesson))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Optional explicit script/lesson pair: SCRIPT LESSON")
    parser.add_argument("--ledger", default=str(DEFAULT_LEDGER), help="Migration ledger to audit")
    parser.add_argument("--summary", action="store_true", help="Print findings grouped by lesson path")
    args = parser.parse_args(argv)

    if args.paths:
        if len(args.paths) != 2:
            parser.error("explicit mode requires exactly SCRIPT LESSON")
        findings = audit_pair(Path(args.paths[0]), Path(args.paths[1]))
    else:
        findings = audit_ledger(Path(args.ledger))

    if findings:
        print(f"PYTHON_FIGURE_ELEMENT_COVERAGE_AUDIT_FAIL count={len(findings)}")
        if args.summary:
            counts: dict[Path, int] = {}
            for finding in findings:
                counts[finding.lesson] = counts.get(finding.lesson, 0) + 1
            for lesson, count in sorted(counts.items(), key=lambda item: (-item[1], str(item[0]))):
                print(f"{lesson}: {count}")
        else:
            for finding in findings:
                print(finding.format())
        return 1
    print("PYTHON_FIGURE_ELEMENT_COVERAGE_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
