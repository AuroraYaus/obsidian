#!/usr/bin/env python3
"""
@file build_full_md.py
@brief 从 3GPP 协议 .docx 生成 agent 友好的全文 Markdown（full.md）。
       与 extract_3gpp_word.py 的差异：本脚本将 OMML 公式内联为
       LaTeX（$...$ / $$...$$）、表格内联为 GFM Markdown、标题按
       层级输出，产出"公式/表格就地可读"的完整文档，供 agent 与
       检索直接阅读。
@date 2026-08-01
@usage python3 build_full_md.py --source specs/38212-j30.docx \
        --output processed/TS_38.212_38212-j30/full.md
@args --source  源 .docx 文件路径（必填）。
@args --output  输出 full.md 路径（默认 stdout 旁 <source>.full.md）。
@note 依赖 tools/omml2latex.py 的 omml_to_latex；图片以
       ![](media/<name>) 引用保留，不内嵌二进制。
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

ET.register_namespace("m", M_NS)
ET.register_namespace("w", W_NS)

NS = {"m": M_NS, "w": W_NS}

sys.path.insert(0, str(Path(__file__).resolve().parent))
from omml2latex import omml_to_latex  # noqa: E402

HEADING_STYLE_RE = re.compile(r"^heading(\d+)$", re.IGNORECASE)
NUMERIC_HEADING_RE = re.compile(r"^(\d+(?:\.\d+)*)\s+\S+")


R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

# 公式文本提取（import 同目录 extract_formula_text）
_EXTRACT_MODULE = None


def _extractor():
    """@brief 惰性导入公式文本提取模块（避免循环依赖与启动开销）。"""
    global _EXTRACT_MODULE
    if _EXTRACT_MODULE is None:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "extract_formula_text", Path(__file__).resolve().parent / "extract_formula_text.py"
        )
        _EXTRACT_MODULE = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_EXTRACT_MODULE)
    return _EXTRACT_MODULE


def parse_document_xml(docx_path: Path) -> tuple[ET.Element, dict[str, str]]:
    """
    @brief 打开 docx（ZIP 容器）并解析 word/document.xml 的 body。
    @param docx_path  源 .docx 路径。
    @return           (w:body 元素, rId → 目标路径映射)。
    @throws FileNotFoundError  ZIP 内缺少 word/document.xml 时抛出。
    @note 关系映射用于把 w:object 内 v:imagedata 的 rId 解析为 media 文件名。
    """
    rels: dict[str, str] = {}
    with zipfile.ZipFile(docx_path) as zf:
        xml_text = zf.read("word/document.xml").decode("utf-8")
        try:
            rels_xml = zf.read("word/_rels/document.xml.rels").decode("utf-8")
            rel_root = ET.fromstring(rels_xml)
            for rel in rel_root:
                rid = rel.attrib.get("Id", "")
                target = rel.attrib.get("Target", "")
                if rid and target:
                    rels[rid] = target
        except KeyError:
            pass
    root = ET.fromstring(xml_text)
    body = root.find("w:body", NS)
    if body is None:
        raise ValueError("word/document.xml 缺少 w:body")
    return body, rels


def paragraph_text(p: ET.Element, inline_math: bool = True) -> str:
    """
    @brief 提取段落文本，公式位置内联 LaTeX。
    @param p             w:p 元素。
    @param inline_math   是否将 m:oMath 内联为 $...$（False 时跳过公式）。
    @return              拼接后的 Markdown 文本。
    @note 处理 w:t 文本、w:tab、w:br、超链接内文本，以及 m:oMath 公式。
    """
    parts: list[str] = []
    for child in p:
        tag = _local(child.tag)
        if tag == "r":
            parts.append(_run_text(child))
        elif tag == "hyperlink":
            for r in child.findall("w:r", NS):
                parts.append(_run_text(r))
        elif tag == "tab":
            parts.append(" ")
        elif tag == "br":
            parts.append("\n")
        elif tag == "oMath" and inline_math:
            latex = omml_to_latex(ET.tostring(child, encoding="unicode"))
            parts.append(f"${latex}$" if latex else "")
        elif tag == "oMathPara" and inline_math:
            latex = omml_to_latex(ET.tostring(child, encoding="unicode"))
            parts.append(f"$${latex}$$" if latex else "")
    return "".join(parts)


_OLE_RELS: dict[str, str] = {}
_SVG_DIR: Path | None = None  # 公式 SVG 目录（main() 按 --output 设置）


def set_ole_rels(rels: dict[str, str]) -> None:
    """
    @brief 注入 rId → media 路径映射（由 parse_document_xml 提供）。
    @param rels  关系映射。
    @note 模块级缓存，避免在 _run_text 内层层传参。
    """
    _OLE_RELS.clear()
    _OLE_RELS.update(rels)


def set_svg_dir(output_path: Path) -> None:
    """
    @brief 按输出路径设置公式 SVG 目录（与 full.md 同目录的 media_svg/）。
    @param output_path  full.md 输出路径。
    @note SVG 目录不存在时置 None（跳过文本提取，仅输出图片引用）。
    """
    global _SVG_DIR
    cand = output_path.parent / "media_svg"
    _SVG_DIR = cand if cand.is_dir() else None


def _run_text(r: ET.Element) -> str:
    """
    @brief 提取单个 w:r 的可见文本。
    @param r  w:r 元素。
    @return  文本（保留 xml:space="preserve" 语义）。
    @note OLE 对象（w:object 内的公式图片）输出 ![](media/<file>) 引用，
           标记公式位置而非留空白。
    """
    parts: list[str] = []
    for child in r:
        tag = _local(child.tag)
        if tag == "t":
            text = child.text or ""
            if child.attrib.get("{http://www.w3.org/XML/1998/namespace}space") != "preserve":
                text = text.replace(" ", " ").strip()
            parts.append(text)
        elif tag == "tab":
            parts.append(" ")
        elif tag == "br":
            parts.append("\n")
        elif tag == "drawing" or tag == "pict":
            # 图片/嵌入对象：提取文件名作为引用
            name = _image_name(child)
            if name:
                parts.append(f"![](media/{name})")
        elif tag == "object":
            # OLE 公式对象（3GPP 部分公式以 wmf 图片嵌入，无 OMML 文本）。
            # 输出分级：
            #   简单公式（≤2 层、无未知字符）→ [公式: 文本]（agent 直接读）
            #   复杂公式（多层/未知字符）→ SVG 引用 + [公式: 近似文本]
            #      （Obsidian 显示结构，agent 读大意）
            rid = ""
            for el in child.iter():
                if _local(el.tag) == "imagedata":
                    rid = el.attrib.get(f"{{{R_NS}}}id", "") or el.attrib.get("r:id", "")
                    break
            target = _OLE_RELS.get(rid, "")
            if target:
                base = target.split("/")[-1]
                if base.lower().endswith(".wmf"):
                    svg_name = base[:-4] + ".svg"
                    if _SVG_DIR is not None and (_SVG_DIR / svg_name).exists():
                        result = _extractor().extract_file(_SVG_DIR / svg_name)
                        if result["text"]:
                            is_complex = result.get("unreliable", False)
                            if is_complex:
                                parts.append(
                                    f"![](media_svg/{svg_name}) [公式≈: {result['text']}]"
                                )
                            else:
                                parts.append(f"[公式: {result['text']}]")
                        else:
                            parts.append(f"![](media_svg/{svg_name})")
                    else:
                        parts.append(f"![](media_svg/{svg_name})")
                else:
                    parts.append(f"![](media/{base})")
            else:
                parts.append("[公式对象]")
    return "".join(parts)


def _image_name(drawing: ET.Element) -> str:
    """
    @brief 从 w:drawing/w:pict 提取内嵌图片文件名。
    @param drawing  w:drawing 或 w:pict 元素。
    @return         文件名（如 image5.wmf），无则空字符串。
    @note 遍历所有 descr/name 属性，取非空值。
    """
    for el in drawing.iter():
        for attr in ("descr", "name"):
            v = el.attrib.get(attr, "")
            if v and ("." in v or v.lower().startswith("image")):
                return v
    return ""


def paragraph_heading_level(p: ET.Element, text: str) -> int | None:
    """
    @brief 判断段落是否为标题并返回层级。
    @param p     w:p 元素。
    @param text  段落文本。
    @return      标题层级（1-9），非标题返回 None。
    @note 优先取 pStyle HeadingN；否则按"数字.数字 文本"模式。
    """
    style = p.find("w:pPr/w:pStyle", NS)
    if style is not None:
        m = HEADING_STYLE_RE.match(style.attrib.get(f"{{{W_NS}}}val", ""))
        if m:
            return min(int(m.group(1)), 6)
    m = NUMERIC_HEADING_RE.match(text)
    if m:
        # TOC 目录行特征：标题后跟页码（如 "5.3.1 Polar coding 15"），跳过
        if re.search(r"\s+\d+$", text):
            return None
        return 2
    return None


def render_table(tbl: ET.Element) -> str:
    """
    @brief 将 w:tbl 渲染为 GFM Markdown 表格。
    @param tbl  w:tbl 元素。
    @return     Markdown 表格文本（含前后空行）。
    @note 单元格内公式内联；gridSpan 按列数展开；表头取首行；
           块级公式（$$）在单元格内降级为行内 $，避免破坏表格渲染。
    """
    rows: list[list[str]] = []
    for tr in tbl.findall("w:tr", NS):
        cells: list[str] = []
        for tc in tr.findall("w:tc", NS):
            cell_text = "".join(
                paragraph_text(p, inline_math=True) for p in tc.findall("w:p", NS)
            ).strip()
            # 单元格内块级公式降级为行内公式（Obsidian 表格不支持 $$）
            cell_text = re.sub(r"\$\$(.+?)\$\$", r"$\1$", cell_text, flags=re.S)
            # gridSpan：内容只保留一次，其余跨列留空
            # （Markdown 表格无 colspan；若展开成 N 个相同单元格会撑爆表格）
            span = 1
            tc_pr = tc.find("w:tcPr", NS)
            if tc_pr is not None:
                gs = tc_pr.find("w:gridSpan", NS)
                if gs is not None:
                    span = int(gs.attrib.get(f"{{{W_NS}}}val", "1"))
            cell_text = cell_text.replace("\n", " ")
            cell_text = cell_text.replace("|", "\\|")
            cells.append(cell_text)
            cells.extend([""] * (span - 1))
        rows.append(cells)
    if not rows:
        return ""
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |",
             "| " + " | ".join(["---"] * ncols) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(lines)


def build_full_md(body: ET.Element) -> str:
    """
    @brief 遍历 body 生成完整 Markdown。
    @param body  w:body 元素。
    @return      full.md 全文。
    @note 段落/表格按文档顺序输出；连续标题自动降级（避免无 # 顶级标题
           时正文段落被误判为标题）；结尾的 sectPr 节属性跳过。
    """
    out: list[str] = []
    for child in body:
        tag = _local(child.tag)
        if tag == "sectPr":
            continue
        if tag == "p":
            text = paragraph_text(child).strip()
            if not text:
                continue
            level = paragraph_heading_level(child, text)
            if level:
                out.append(f"{'#' * level} {text}")
            elif text.startswith("$$") and text.endswith("$$"):
                out.append(text)  # 块级公式
            else:
                out.append(text)
        elif tag == "tbl":
            table = render_table(child)
            if table:
                out.append(table)
        out.append("")
    text = "\n".join(out)
    # 公式边界修复：$ 前/后紧跟字母数字时 Obsidian 不识别行内数学
    # （如 "4$x$"、"$x$4"），在 $ 与字母数字之间补空格。
    # 注意避免破坏 $$ 块级公式：块级公式独占一行（行首/行尾），不受影响。
    text = re.sub(r"(?<=[A-Za-z0-9])\$", " $", text)
    text = re.sub(r"\$(?=[A-Za-z0-9])", "$ ", text)
    # 相邻行内公式间补空格（$a$$b$ 会被 Obsidian 误判为块级公式）。
    # 块级 $$...$$ 不受影响：$$ 后跟非 $ 内容才匹配，块级结尾的 $$ 后是行尾。
    text = re.sub(r"\$([^$\n]+?)\$(?=\$[^$\n])", r"$\1$ ", text)
    return text


def _local(tag: str) -> str:
    """@brief 提取 XML 标签本地名（去命名空间）。"""
    return tag.split("}")[-1] if "}" in tag else tag


def main() -> int:
    """
    @brief 脚本入口。
    @usage python3 build_full_md.py --source specs/38212-j30.docx \
            --output processed/TS_38.212_38212-j30/full.md
    @args --source  源 .docx 路径（必填）。
    @args --output  输出路径（默认 <source 目录>/<stem>.full.md）。
    @exit_code 0 = 成功；1 = 参数错误或解析失败。
    """
    parser = argparse.ArgumentParser(description="Build agent-friendly full.md from 3GPP docx")
    parser.add_argument("--source", required=True, help="Source .docx file")
    parser.add_argument("--output", default=None, help="Output full.md path")
    args = parser.parse_args()

    src = Path(args.source)
    if not src.exists():
        print(f"源文件不存在: {src}", file=sys.stderr)
        return 1
    out = Path(args.output) if args.output else src.with_name(src.stem + ".full.md")

    body, rels = parse_document_xml(src)
    set_ole_rels(rels)
    set_svg_dir(out)
    full = build_full_md(body)
    out.write_text(full, encoding="utf-8")
    print(f"已生成: {out} ({len(full.splitlines())} 行)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
