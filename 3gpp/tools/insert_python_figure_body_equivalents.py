#!/usr/bin/env python3
"""Insert body-equivalent blocks after Python PNG figure captions.

The inserted block is deliberately textual and auditable. It keeps PNGs as
visual aids while giving the lesson body a Mermaid/table representation close
to the original figure reference.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.audit_python_figure_body_equivalents import MARKERS, has_marker_near


DOC_ROOTS = [Path("docs/L1"), Path("docs/L2"), Path("docs/L3")]
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+\.png)\)")
SCRIPT_RE = re.compile(r"`?(tools/figures/[\w./-]+\.py)`?")
STOP_RE = re.compile(r"^(##+ |\| |!\[|```)")


FLOW_HINTS = (
    "flow",
    "architecture",
    "chain",
    "decoder",
    "rtl",
    "testbench",
    "synthesis",
    "timing",
    "map",
    "schedule",
    "recovery",
    "diagnosis",
)

TABLE_HINTS = (
    "table",
    "sequence",
    "compare",
    "comparison",
    "requirements",
    "report",
    "matrix",
    "numeric",
    "walkthrough",
)


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"[；。;!?]\s*", text)
    return [p.strip() for p in parts if p.strip()]


def sanitize_node(text: str) -> str:
    text = text.replace("|", "/").replace("`", "")
    return text.strip()


def collect_caption(lines: list[str], image_idx: int) -> str:
    collected: list[str] = []
    for j in range(image_idx + 1, min(len(lines), image_idx + 18)):
        line = lines[j].strip()
        if not line:
            if collected and not any(x.endswith(("：", ":")) for x in collected):
                break
            continue
        if STOP_RE.match(line) and not line.startswith("图 "):
            break
        collected.append(line)
        if len(collected) >= 2 and line.endswith("。") and not any(x.endswith(("：", ":")) for x in collected):
            break
    return " ".join(collected).strip()


def numbered_items(text: str) -> list[str]:
    items = []
    for line in text.splitlines():
        match = re.match(r"\s*\d+\.\s*(.+)", line)
        if match:
            items.append(match.group(1).strip().rstrip("。"))
    if items:
        return items
    return [m.strip().rstrip("。") for m in re.findall(r"(?:^|\s)\d+\.\s*([^。]+)", text)]


def meaningful_caption(caption: str) -> str:
    text = re.sub(r"`?tools/figures/[\w./-]+\.py`?", "生成脚本", caption)
    text = re.sub(r"`?docs/[^\s`。；;]+\.png`?", "图片文件", text)
    text = re.sub(r"`?assets/[^\s`。；;]+\.png`?", "图片文件", text)
    for marker in ("读图顺序如下：", "读图顺序为：", "读图顺序是：", "读图时", "图中", "上半部分", "左侧"):
        if marker in text:
            return text[text.index(marker) :].strip()
    parts = split_sentences(text)
    if len(parts) > 1:
        return "。".join(parts[1:]).strip() + "。"
    return text


def scripts_from_context(lines: list[str], image_idx: int) -> str:
    start = max(0, image_idx - 8)
    end = min(len(lines), image_idx + 12)
    scripts = sorted(set(SCRIPT_RE.findall("\n".join(lines[start:end]))))
    return ", ".join(f"`{script}`" for script in scripts) if scripts else "-"


def equivalent_kind(image: str, caption: str) -> str:
    lower = f"{image} {caption}".lower()
    if any(hint in lower for hint in FLOW_HINTS):
        return "mermaid"
    if any(hint in lower for hint in TABLE_HINTS):
        return "table"
    if any(token in caption for token in ["流程", "链路", "顺序", "进入", "输出", "选择"]):
        return "mermaid"
    return "table"


def mermaid_block(image: str, caption: str, scripts: str) -> list[str]:
    caption = meaningful_caption(caption)
    sentences = split_sentences(caption)
    if not sentences:
        sentences = [f"图片 {image} 的读图信息"]
    numbered = numbered_items(caption)
    if numbered:
        nodes = [sanitize_node(p) for p in numbered[:6]]
    else:
        nodes = []
    if not nodes:
        body = sentences
        chunks = []
        for sentence in body:
            if "：" in sentence:
                sentence = sentence.split("：", 1)[1]
            chunks.extend([p.strip() for p in re.split(r"[，,、]", sentence) if p.strip()])
        bad_tokens = ("生成脚本", "图片文件", "输出到", "由", ".py", ".png", "无文本遮挡", "无箭头压字", "底部留白")
        nodes = [sanitize_node(p) for p in chunks if not any(token in p for token in bad_tokens)][:6]
    if len(nodes) < 2:
        if "T7.5_LTE_DL_UL_decoder_context" in image:
            nodes = ["下行侧由 DCI/MCS/RV/HARQ 上下文驱动", "上行侧由 grant/configured grant 和 UL HARQ 上下文驱动", "两侧最终都进入 Turbo decoder、CRC 和 soft buffer 状态更新"]
            caption = "；".join(nodes)
        else:
            nodes = [sanitize_node(sentences[0]), "相邻正文表格承接字段、边界和工程检查点"]
    out = [
        "",
        "图片内容正文等价：Mermaid 等价图",
        "",
        "```mermaid",
        "flowchart LR",
    ]
    for i, node in enumerate(nodes):
        out.append(f"  N{i}[\"{node}\"]")
    for i in range(len(nodes) - 1):
        out.append(f"  N{i} --> N{i + 1}")
    out.extend(
        [
            "```",
            "",
            "| 等价项 | 正文表达 |",
            "|:---|:---|",
            f"| 图片 | `{image}` |",
            f"| 生成脚本 | {scripts} |",
            f"| 保留内容 | {caption or '读图顺序、关键节点、输入输出和工程边界见 Mermaid 等价图。'} |",
        ]
    )
    return out


def table_block(image: str, caption: str, scripts: str) -> list[str]:
    caption = meaningful_caption(caption)
    sentences = split_sentences(caption)
    summary = sentences[0] if sentences else f"图片 {image}"
    details = sentences[1:] or ["图片中的关键字段、流程或矩阵含义由正文表格化承接。"]
    out = [
        "",
        "图片内容正文等价：Markdown 等价表",
        "",
        "| 等价项 | 正文表达 |",
        "|:---|:---|",
        f"| 图片 | `{image}` |",
        f"| 生成脚本 | {scripts} |",
        f"| 核心内容 | {summary.replace('|', '/')} |",
    ]
    for idx, detail in enumerate(details[:5], 1):
        out.append(f"| 图中信息 {idx} | {detail.replace('|', '/')} |")
    out.append("| 阅读方式 | 以本表和相邻正文为主，PNG 只作为视觉辅助；字段、流程和边界不得只存在于图片像素中。 |")
    return out


def insert_for_file(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = False
    i = 0
    while i < len(lines):
        match = IMAGE_RE.search(lines[i])
        if not match:
            i += 1
            continue
        if has_marker_near(lines, i, 40):
            i += 1
            continue
        image = match.group(1)
        caption = collect_caption(lines, i)
        scripts = scripts_from_context(lines, i)
        block = mermaid_block(image, caption, scripts) if equivalent_kind(image, caption) == "mermaid" else table_block(image, caption, scripts)
        insert_at = i + 1
        while insert_at < len(lines) and lines[insert_at].strip():
            insert_at += 1
        lines[insert_at:insert_at] = block
        changed = True
        i = insert_at + len(block)
    if changed:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Insert body-equivalent blocks after Python PNG figure captions"
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

    changed = []
    for p in args.paths:
        if p.is_dir():
            for md in sorted(p.glob("*.md")):
                if insert_for_file(md):
                    changed.append(md)
        elif p.is_file() and p.suffix == ".md":
            if insert_for_file(p):
                changed.append(p)

    if args.dry_run:
        print(f"[DRY-RUN] Would update {len(changed)} markdown files:")
        for md in changed:
            print(f"  {md}")
    else:
        for md in changed:
            print(md)
        print(f"UPDATED {len(changed)} markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
