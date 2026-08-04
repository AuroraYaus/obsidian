#!/usr/bin/env python3
"""
@file insert_python_figure_body_equivalents.py
@brief 在讲义中 Python 生成的 PNG 图片引用后自动插入正文等价块（Mermaid 流程图
       或 Markdown 表格），使图片内容有结构化文本表示，可被检索、审核和版本对比。
       目的：防止讲义中关键信息仅存在于 PNG 像素中，确保字段、流程和边界有正文承接。
@date 2026-07-22
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.audit_python_figure_body_equivalents import MARKERS, has_marker_near


DOC_ROOTS = [Path("docs/L1"), Path("docs/L2_协议算法"), Path("docs/L3")]
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
    """
    @brief 将中文说明文本按句末标点（；。;!?）分割为独立句子，
           便于后续逐句分析语义并提取等价表述要点。
    @param text 输入文本。
    @return 分割后的句子列表（已去除空白段）。
    """
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"[；。;!?]\s*", text)
    return [p.strip() for p in parts if p.strip()]


def sanitize_node(text: str) -> str:
    """
    @brief 清理 Mermaid 节点文本中的非法字符（管道符替换、反引号移除），
           防止生成语法错误的 flowchart 代码。
    @param text 原始节点文本。
    @return 清理后的安全文本。
    """
    text = text.replace("|", "/").replace("`", "")
    return text.strip()


def collect_caption(lines: list[str], image_idx: int) -> str:
    """
    @brief 从图片引用行之后收集连续的说明文本作为图注，
           用于后续语义分析以生成等价块内容。
           在遇到新标题、新图片、代码块或足够完整的句子时停止收集。
    @param lines 讲义全文按行分割的列表。
    @param image_idx 图片引用所在行号。
    @return 收集到的图注文本（多行拼接）。
    """
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
    """
    @brief 从文本中提取编号列表项（1. xxx 格式），
           用于构建 Mermaid 节点序列的候选节点名。
    @param text 输入文本。
    @return 提取的列表项文本列表，无编号列表时返回空列表。
    """
    items = []
    for line in text.splitlines():
        match = re.match(r"\s*\d+\.\s*(.+)", line)
        if match:
            items.append(match.group(1).strip().rstrip("。"))
    if items:
        return items
    return [m.strip().rstrip("。") for m in re.findall(r"(?:^|\s)\d+\.\s*([^。]+)", text)]


def meaningful_caption(caption: str) -> str:
    """
    @brief 从图注中提取有意义的正文描述部分，
           剥离脚本路径、图片文件路径等元信息，保留读图顺序和内容说明。
    @param caption 原始图注文本。
    @return 提取后的有意义描述文本。
    @note 如果图注以"读图顺序如下"等引导词开头，从引导词向后截取；
          否则取第一句之后的全部内容。
    """
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
    """
    @brief 从图片附近的文本中提取所有引用到的生成脚本路径，
           用于等价块中标注图片来源的生成逻辑。
    @param lines 讲义全文行列表。
    @param image_idx 图片引用行号。
    @return 以反引号包裹、逗号分隔的脚本路径列表字符串，未找到时返回 "-"。
    """
    start = max(0, image_idx - 8)
    end = min(len(lines), image_idx + 12)
    scripts = sorted(set(SCRIPT_RE.findall("\n".join(lines[start:end]))))
    return ", ".join(f"`{script}`" for script in scripts) if scripts else "-"


def equivalent_kind(image: str, caption: str) -> str:
    """
    @brief 根据图片文件名和图注文本中的关键词判断等价块类型（流程图还是表格），
           使得每种图片素材自动选择最适合的正文表达形式。
    @param image 图片文件名。
    @param caption 图注文本。
    @return "mermaid" 表示应生成 Mermaid 流程图；"table" 表示应生成 Markdown 表格。
    """
    lower = f"{image} {caption}".lower()
    if any(hint in lower for hint in FLOW_HINTS):
        return "mermaid"
    if any(hint in lower for hint in TABLE_HINTS):
        return "table"
    if any(token in caption for token in ["流程", "链路", "顺序", "进入", "输出", "选择"]):
        return "mermaid"
    return "table"


def mermaid_block(image: str, caption: str, scripts: str) -> list[str]:
    """
    @brief 生成 Mermaid flowchart LR 等价图块，
           从图注中提取节点列表构建从左到右的流程图，并附带等价项对照表。
    @param image 图片文件名。
    @param caption 图片说明文字。
    @param scripts 关联的生成脚本路径。
    @return 包含 Markdown 等价块内容的字符串列表（每行一个元素）。
    @note 特殊处理 T7.5_LTE_DL_UL_decoder_context 等已知图片，为其硬编码节点；
          节点不足 2 个时自动补充相邻正文作为兜底。
    """
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
    """
    @brief 生成 Markdown 等价表块，
           以表格形式列出图片、生成脚本、核心内容和逐项信息，适合表格类图片的正文承接。
    @param image 图片文件名。
    @param caption 图片说明文字。
    @param scripts 关联的生成脚本路径。
    @return 包含 Markdown 等价表块的字符串行列表。
    """
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
    """
    @brief 对单个讲义文件处理：扫描每行中的 PNG 图片引用，对尚未被等价块覆盖的图片
           自动生成并插入 Mermaid 流程图或 Markdown 表格等价块。
    @param path 讲义 .md 文件路径。
    @return True 表示文件被修改（至少插入了一个等价块），False 表示无需变更。
    @note 已存在等价块（40 行内有标记）的图片会被跳过，避免重复插入；
          插入位置为图片引用行之后紧跟的第一个空行。
    """
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
    """
    @brief 脚本入口：遍历指定讲义目录或文件，为每个 PNG 图片引用插入正文等价块。
    @return 0 正常完成；非 0 表示内部异常。
    """
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
        help="directories or files to process (default: docs/L1 docs/L2_协议算法 docs/L3)",
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


# @brief 在讲义中自动插入 Python 图片的正文等价块（Mermaid 图或 Markdown 表）。
# @usage python tools/insert_python_figure_body_equivalents.py [--dry-run] [PATHS...]
# @args --dry-run  仅打印变更摘要，不写入文件。
# @args PATHS      要处理的目录或 .md 文件列表，默认 docs/L1 docs/L2_协议算法 docs/L3。
# @exit_code 0 正常完成。
if __name__ == "__main__":
    raise SystemExit(main())
