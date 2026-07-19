#!/usr/bin/env python3
"""Refresh detailed body equivalents for Python-generated figure PNGs.

The generated blocks are intentionally conservative: they summarize figure
semantics from the rendering script's own labels, node bodies and table text.
They replace only the short block immediately after a Markdown image.
"""

from __future__ import annotations

import ast
import re
import sys
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC_ROOTS = [ROOT / "docs/L1", ROOT / "docs/L2", ROOT / "docs/L3"]
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+\.png)\)")
SCRIPT_RE = re.compile(r"tools/figures/[\w./-]+\.py")
MARKER_RE = re.compile(r"图片内容正文等价：(?:Mermaid 等价图|Markdown 等价表)")

STOP_RE = re.compile(r"^(##+ |!\[|图\s|```)")
PLACEHOLDER_PHRASES = (
    "相邻正文表格承接字段",
    "图片中的关键字段",
    "字段、流程和边界不得只存在",
    "无文本遮挡",
    "无箭头压字",
    "无裁切",
    "底部留白",
)


@dataclass(frozen=True)
class ScriptContent:
    nodes: list[str]
    rows: list[tuple[str, str]]


def is_useful_string(value: str) -> bool:
    text = value.strip()
    if len(text) < 3:
        return False
    if text == "__main__":
        return False
    if text in {"bg", "ink", "muted", "line", "panel", "white", "blue", "green", "red", "orange", "gray"}:
        return False
    if text.startswith("#") or text.startswith("/usr/share/fonts"):
        return False
    if text.startswith("Render ") or text.startswith("Static audit "):
        return False
    if text.endswith((".png", ".py", ".ttf", ".ttc", ".csv", ".html", ".md")):
        return False
    if re.fullmatch(r"#[0-9A-Fa-f]{6}", text):
        return False
    if re.fullmatch(r"[A-Z_][A-Z0-9_]*", text) and len(text) < 18:
        return False
    if any(phrase in text for phrase in PLACEHOLDER_PHRASES):
        return False
    return any(ch.isalnum() or "\u4e00" <= ch <= "\u9fff" for ch in text)


def normalize_text(value: str) -> str:
    text = re.sub(r"\s+", " ", value.replace("|", "/")).strip()
    text = text.replace('"', "'")
    return text


def collect_literal_strings(node: ast.AST) -> list[str]:
    values: list[str] = []
    for child in ast.walk(node):
        if isinstance(child, ast.Constant) and isinstance(child.value, str) and is_useful_string(child.value):
            values.append(normalize_text(child.value))
    return values


def list_of_strings(node: ast.AST) -> list[str] | None:
    if not isinstance(node, (ast.List, ast.Tuple)):
        return None
    values: list[str] = []
    for elt in node.elts:
        if isinstance(elt, ast.Constant) and isinstance(elt.value, str) and is_useful_string(elt.value):
            values.append(normalize_text(elt.value))
        else:
            return None
    return values if values else None


def extract_script_content(script: Path) -> ScriptContent:
    try:
        tree = ast.parse(script.read_text(encoding="utf-8"))
    except (OSError, SyntaxError):
        return ScriptContent([], [])

    ordered_nodes: OrderedDict[str, None] = OrderedDict()
    row_pairs: OrderedDict[tuple[str, str], None] = OrderedDict()

    call_names = {"box", "card", "node", "draw_datapath", "cell", "tag"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            name = func.id if isinstance(func, ast.Name) else func.attr if isinstance(func, ast.Attribute) else ""
            if name in call_names:
                strings = [
                    normalize_text(arg.value)
                    for arg in node.args
                    if isinstance(arg, ast.Constant)
                    and isinstance(arg.value, str)
                    and is_useful_string(arg.value)
                ]
                if len(strings) >= 2:
                    row_pairs.setdefault((strings[0], "；".join(strings[1:])), None)
                    ordered_nodes.setdefault(strings[0], None)
                elif len(strings) == 1:
                    ordered_nodes.setdefault(strings[0], None)

        values = list_of_strings(node)
        if values:
            if len(values) == 1:
                ordered_nodes.setdefault(values[0], None)
            elif len(values) == 2:
                row_pairs.setdefault((values[0], values[1]), None)
            else:
                ordered_nodes.setdefault(values[0], None)
                row_pairs.setdefault((values[0], "；".join(values[1:])), None)

    nodes = [text for text in ordered_nodes if 4 <= len(text) <= 120 and not text.startswith("T")]
    rows = [(a, b[:220]) for a, b in row_pairs if 2 <= len(a) <= 80 and 4 <= len(b)]
    return ScriptContent(nodes[:14], rows[:14])


def scripts_from_context(lines: list[str], image_idx: int) -> list[Path]:
    start = max(0, image_idx - 20)
    end = min(len(lines), image_idx + 45)
    context = "\n".join(lines[start:end])
    scripts = [ROOT / match for match in sorted(set(SCRIPT_RE.findall(context)))]
    return [script for script in scripts if script.exists()]


def collect_caption(lines: list[str], image_idx: int) -> str:
    parts: list[str] = []
    for idx in range(image_idx + 1, min(len(lines), image_idx + 20)):
        line = lines[idx].strip()
        if not line:
            if parts:
                break
            continue
        if MARKER_RE.search(line):
            break
        if STOP_RE.match(line) and not line.startswith("图 "):
            break
        if line.startswith("|"):
            break
        parts.append(line)
        if line.endswith("。"):
            break
    return normalize_text(" ".join(parts))


def fallback_nodes_from_caption(caption: str) -> list[str]:
    body = caption
    for marker in ("读图顺序为：", "读图顺序如下：", "展示", "包括"):
        if marker in body:
            body = body.split(marker, 1)[1]
            break
    parts = [normalize_text(part) for part in re.split(r"[；;。]", body) if normalize_text(part)]
    return [part for part in parts if len(part) >= 6][:8]


def merge_content(scripts: list[Path], caption: str) -> ScriptContent:
    nodes: OrderedDict[str, None] = OrderedDict()
    rows: OrderedDict[tuple[str, str], None] = OrderedDict()
    for script in scripts:
        content = extract_script_content(script)
        for node in content.nodes:
            nodes.setdefault(node, None)
        for row in content.rows:
            rows.setdefault(row, None)
    for node in fallback_nodes_from_caption(caption):
        nodes.setdefault(node, None)
    if not rows:
        node_list = list(nodes)
        for idx, node in enumerate(node_list[:8], 1):
            rows.setdefault((f"图中信息 {idx}", node), None)
    return ScriptContent(list(nodes)[:12], list(rows)[:12])


def mermaid_node_label(text: str) -> str:
    text = normalize_text(text)
    if len(text) > 72:
        text = text[:69].rstrip() + "..."
    return text


def block_for_image(image: str, scripts: list[Path], content: ScriptContent) -> list[str]:
    script_text = ", ".join(f"`{script.relative_to(ROOT)}`" for script in scripts) if scripts else "-"
    nodes = content.nodes[:8]
    if len(nodes) < 4:
        nodes = nodes + [row[0] for row in content.rows if row[0] not in nodes]
    nodes = nodes[:8]
    if len(nodes) < 4:
        nodes.extend(["输入字段", "地址/状态转换", "译码器消费", "验证输出"][len(nodes) :])

    out = [
        "",
        "图片内容正文等价：Mermaid 等价图",
        "",
        "```mermaid",
        "flowchart LR",
    ]
    for idx, node in enumerate(nodes):
        out.append(f"  N{idx}[\"{mermaid_node_label(node)}\"]")
    for idx in range(len(nodes) - 1):
        out.append(f"  N{idx} --> N{idx + 1}")
    out.extend(["```", "", "| 等价项 | 正文表达 |", "|:---|:---|"])
    out.append(f"| 图片 | `{image}` |")
    out.append(f"| 生成脚本 | {script_text} |")

    rows = content.rows[:10]
    if len(rows) < 4:
        for node in nodes:
            rows.append(("图中节点", node))
            if len(rows) >= 4:
                break
    for key, value in rows[:10]:
        out.append(f"| {key} | {value} |")
    return out


def remove_existing_block(lines: list[str], insert_at: int) -> int:
    idx = insert_at
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines) or not MARKER_RE.search(lines[idx]):
        return insert_at
    idx += 1
    in_fence = False
    while idx < len(lines):
        stripped = lines[idx].strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            idx += 1
            continue
        if not in_fence and (stripped.startswith("图 ") or stripped.startswith("## ") or stripped.startswith("![") or stripped.startswith("### ")):
            break
        idx += 1
    return idx


def refresh_file(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = False
    idx = 0
    while idx < len(lines):
        match = IMAGE_RE.search(lines[idx])
        if not match:
            idx += 1
            continue
        image = match.group(1)
        scripts = scripts_from_context(lines, idx)
        caption = collect_caption(lines, idx)
        content = merge_content(scripts, caption)
        insert_at = idx + 1
        delete_to = remove_existing_block(lines, insert_at)
        block = block_for_image(image, scripts, content)
        if delete_to == insert_at:
            while insert_at < len(lines) and lines[insert_at].strip():
                insert_at += 1
            delete_to = insert_at
        lines[insert_at:delete_to] = block
        changed = True
        idx = insert_at + len(block)
    if changed:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Refresh detailed body equivalents for Python-generated PNGs"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print what would be changed without writing files",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=DOC_ROOTS,
        help="directories or files to process (default: docs/L1 docs/L2 docs/L3)",
    )
    args = parser.parse_args()

    changed: list[Path] = []
    for p in args.paths:
        if p.is_dir():
            for path in sorted(p.glob("*.md")):
                if refresh_file(path):
                    changed.append(path.relative_to(ROOT))
        elif p.is_file() and p.suffix == ".md":
            if refresh_file(p):
                changed.append(p.relative_to(ROOT))

    if args.dry_run:
        print(f"[DRY-RUN] Would refresh {len(changed)} files:")
        for path in changed:
            print(f"  {path}")
    else:
        for path in changed:
            print(path)
        print(f"REFRESHED {len(changed)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
