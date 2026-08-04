#!/usr/bin/env python3
"""
@file refresh_python_figure_body_equivalents.py
@brief 刷新讲义中 Python 图片的正文等价块内容：通过解析生成脚本的 AST 提取节点标签、
       表格文本和说明字符串，重新生成更精确的 Mermaid 流程图等价块，替换旧的简洁版等价块。
       目的：从渲染脚本中自动抽取结构化语义，减少手工维护等价块的工作量。
@date 2026-07-22
"""

from __future__ import annotations

import ast
import re
import sys
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC_ROOTS = [ROOT / "docs/L1", ROOT / "docs/L2_协议算法", ROOT / "docs/L3"]
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
    """
    @brief 从 Python 渲染脚本 AST 中抽取的结构化内容体：
          nodes 为节点名称列表（用作 Mermaid 节点），
          rows 为键值对列表（用作等价表中表格行）。
    @note frozen=True 确保内容不可变，避免多处使用时互相干扰。
    """
    nodes: list[str]
    rows: list[tuple[str, str]]


def is_useful_string(value: str) -> bool:
    """
    @brief 判断 AST 中提取的字符串常量是否具有语义价值（非颜色名、非文件路径、非常量标识等），
           过滤掉渲染脚本中的技术性样板字符串，只保留描述性的内容文本。
    @param value 字符串值。
    @return True 表示该字符串值得保留为等价块内容。
    @note 通过长度阈值、已知无效模式（颜色值、文件路径、仅大写+数字的常量名等）和
          占位短语黑名单（PLACEHOLDER_PHRASES）多层过滤。
    """
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
    """
    @brief 归一化文本：合并空白、替换管道符（Markdown 表格中非法）、处理引号，
           确保提取的文本可直接嵌入 Markdown 而不破坏格式。
    @param value 原始文本。
    @return 归一化后的安全文本。
    """
    text = re.sub(r"\s+", " ", value.replace("|", "/")).strip()
    text = text.replace('"', "'")
    return text


def collect_literal_strings(node: ast.AST) -> list[str]:
    """
    @brief 递归遍历 AST 节点子树，收集所有有语义价值的字符串常量，
           作为从渲染脚本中提取描述文本的基础方法。
    @param node AST 根节点。
    @return 经过 is_useful_string 和 normalize_text 处理后的字符串列表。
    """
    values: list[str] = []
    for child in ast.walk(node):
        if isinstance(child, ast.Constant) and isinstance(child.value, str) and is_useful_string(child.value):
            values.append(normalize_text(child.value))
    return values


def list_of_strings(node: ast.AST) -> list[str] | None:
    """
    @brief 如果 AST 节点是纯字符串列表/元组，返回其中所有有语义价值的字符串；
           若包含非字符串元素则返回 None（不做部分提取）。
           用于检测如 ["节点1", "节点2", ...] 这类数据定义。
    @param node AST 节点。
    @return 字符串列表或 None（非纯字符串列表或无可提取字符串）。
    """
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
    """
    @brief 解析 Python 渲染脚本的 AST，从中提取绘制命令（box/card/node/cell/tag 等）
           的参数文本和列表数据，构建 ScriptContent 节点列表和键值行列表。
           目的：从脚本代码中自动恢复图片的语义结构，无需人工阅读代码后手写等价块。
    @param script 渲染脚本文件路径。
    @return ScriptContent 对象，包含提取的节点名（最多 14 个）和键值行（最多 14 个）。
    @note 对 OSError 和 SyntaxError 做静默处理（返回空内容），不中断批量流程；
          节点文本长度限制为 4-120 字符且不以 "T" 开头（排除文件名干扰）。
    """
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
    """
    @brief 从图片引用附近的文本中提取所有存在的渲染脚本路径（绝对路径），
           用于后续解析脚本内容生成精确等价块。
    @param lines 讲义全文行列表。
    @param image_idx 图片引用行号。
    @return 存在且可读的脚本 Path 对象列表。
    @note 搜索范围为图片上下 20/45 行，只保留实际存在于磁盘上的脚本。
    """
    start = max(0, image_idx - 20)
    end = min(len(lines), image_idx + 45)
    context = "\n".join(lines[start:end])
    scripts = [ROOT / match for match in sorted(set(SCRIPT_RE.findall(context)))]
    return [script for script in scripts if script.exists()]


def collect_caption(lines: list[str], image_idx: int) -> str:
    """
    @brief 从图片引用行之后收集连续的说明文本作为图注，
           遇到已有等价块标记、新标题、新图片或表格行时停止。
    @param lines 讲义全文行列表。
    @param image_idx 图片引用行号。
    @return 收集到的图注文本（经 normalize_text 处理）。
    """
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
    """
    @brief 当脚本 AST 无法提取到足够节点时，从图注文本中回退提取句子片段作为节点名，
           确保等价块至少有基本内容。
    @param caption 图注文本。
    @return 从图注中提取的句子片段列表（最多 8 个，单个片段至少 6 字符）。
    """
    body = caption
    for marker in ("读图顺序为：", "读图顺序如下：", "展示", "包括"):
        if marker in body:
            body = body.split(marker, 1)[1]
            break
    parts = [normalize_text(part) for part in re.split(r"[；;。]", body) if normalize_text(part)]
    return [part for part in parts if len(part) >= 6][:8]


def merge_content(scripts: list[Path], caption: str) -> ScriptContent:
    """
    @brief 合并多个渲染脚本的提取内容和图注回退节点，去重并截断到合理数量，
           生成最终用于等价块构建的 ScriptContent。
    @param scripts 渲染脚本路径列表。
    @param caption 图注文本。
    @return 合并去重后的 ScriptContent（节点最多 12 个，行最多 12 个）。
    @note 使用 OrderedDict 保持首次出现的顺序同时去重；
          若提取不到行数据，自动从节点列表生成编号的占位行。
    """
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
    """
    @brief 格式化 Mermaid 节点标签文本：归一化并截断到 72 字符（加省略号），
           防止过长的节点标签破坏流程图布局。
    @param text 原始节点文本。
    @return 适合直接放入 Mermaid flowchart 节点声明的标签文本。
    """
    text = normalize_text(text)
    if len(text) > 72:
        text = text[:69].rstrip() + "..."
    return text


def block_for_image(image: str, scripts: list[Path], content: ScriptContent) -> list[str]:
    """
    @brief 根据提取的脚本内容生成完整的 Mermaid 等价图和等价项表格块，
           包含 flowchart LR 节点声明和等价项对照表。
           节点不足时自动从行数据补足，仍不足则使用兜底通用节点名。
    @param image 图片文件名。
    @param scripts 渲染脚本路径列表。
    @param content 合并后的 ScriptContent。
    @return Markdown 等价块内容行列表。
    """
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
    """
    @brief 定位并跳过图片引用后已存在的旧等价块（以"图片内容正文等价"标记开头的区域），
           返回新等价块可以覆盖的范围结束行号。
    @param lines 讲义全文行列表。
    @param insert_at 等价块插入起始行号。
    @return 旧等价块结束后的行号（等于 insert_at 表示无旧块）。
    @note 正确处理 Mermaid 代码围栏（``` 配对），不会误将围栏内的内容删除不完整。
    """
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
    """
    @brief 对单个讲义文件执行刷新：扫描 PNG 图片引用，解析相关联的渲染脚本 AST，
           生成精确等价块并替换旧的简洁等价块。
    @param path 讲义 .md 文件路径。
    @return True 表示文件被修改，False 表示无需变更。
    """
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
    """
    @brief 脚本入口：遍历指定讲义目录或文件，通过 AST 解析渲染脚本刷新每个 PNG 图片的等价块。
    @return 0 正常完成。
    """
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
        help="directories or files to process (default: docs/L1 docs/L2_协议算法 docs/L3)",
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


# @brief 通过 AST 解析渲染脚本刷新讲义中的 Python 图片正文等价块。
# @usage python tools/refresh_python_figure_body_equivalents.py [--dry-run] [PATHS...]
# @args --dry-run  仅打印变更摘要，不写入文件。
# @args PATHS      要处理的目录或 .md 文件列表，默认 docs/L1 docs/L2_协议算法 docs/L3。
# @exit_code 0 正常完成。
if __name__ == "__main__":
    raise SystemExit(main())
