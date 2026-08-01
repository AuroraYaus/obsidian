"""
@file docx_parser.py
@brief 3GPP DOCX 文档解析引擎 — 段落、表格、公式、媒体的结构化提取
@date 2025

从 Word .docx（Office Open XML / WordprocessingML）容器中提取：
- Paragraph  — 段落文本、样式名、是否标题候选
- Table       — 含合并单元格（rowspan/colspan）的表格
- Equation    — OMML（Office Math Markup Language）公式
- Media       — 内嵌图片等媒体文件

DOCX 本质是一个 ZIP 包，内含 XML 文件。本模块使用 Python 标准库
（zipfile + xml.etree.ElementTree）直接解析，无外部依赖。

@note DOCX 的 XML 命名空间较多（w, m, r, a, rel），解析时需注意
      命名空间前缀注册和查找。

@see exporter.py — 将 ParsedDocx 导出为结构化目录
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile


# ── XML 命名空间注册 ──────────────────────────────────────────────
# DOCX 内部 XML 使用多个命名空间，必须在解析前注册，
# 否则 ElementTree 会生成 ns0: 前缀导致查找失败。

ET.register_namespace("w", "http://schemas.openxmlformats.org/wordprocessingml/2006/main")
ET.register_namespace("m", "http://schemas.openxmlformats.org/officeDocument/2006/math")
ET.register_namespace("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships")
ET.register_namespace("a", "http://schemas.openxmlformats.org/drawingml/2006/main")

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}


# ── 数据模型（frozen dataclass，不可变） ──────────────────────────


@dataclass(frozen=True)
class Paragraph:
    """
    @brief 文档段落

    @ivar index      段落序号（1-based，从文档开头计数）
    @ivar text       纯文本内容（已去除 XML 标记和格式信息）
    @ivar style      Word 样式名（如 "Heading1", "Normal"），可能为 None
    @ivar is_heading 是否为标题候选（基于样式名或文本模式判断）
    """
    index: int
    text: str
    style: str | None
    is_heading: bool


@dataclass(frozen=True)
class TableCell:
    """
    @brief 表格单元格

    @ivar text    单元格文本内容
    @ivar rowspan 垂直合并行数（默认 1）
    @ivar colspan 水平合并列数（默认 1）
    @ivar omitted 是否为垂直合并中被省略的续行单元格
    """
    text: str
    rowspan: int = 1
    colspan: int = 1
    omitted: bool = False


@dataclass(frozen=True)
class Table:
    """
    @brief 文档表格

    @ivar index  表格序号（1-based，从文档开头计数）
    @ivar rows   行列表，每行是 TableCell 列表
    """
    index: int
    rows: list[list[TableCell]]


@dataclass(frozen=True)
class Equation:
    """
    @brief OMML 数学公式

    @ivar index  公式序号（1-based）
    @ivar xml    OMML XML 原文（可重新渲染或转换为 MathML/LaTeX）
    @ivar text   公式的纯文本表示
    """
    index: int
    xml: str
    text: str


@dataclass(frozen=True)
class Media:
    """
    @brief 内嵌媒体文件（图片等）

    @ivar name             文件名（如 "image1.png"）
    @ivar path             ZIP 内的完整路径（如 "word/media/image1.png"）
    @ivar data             文件二进制内容
    @ivar relationship_id  关系 ID（rId），用于关联到文档中的引用
    @ivar target           关系目标路径
    """
    name: str
    path: str
    data: bytes
    relationship_id: str | None
    target: str | None


@dataclass(frozen=True)
class ParsedDocx:
    """
    @brief 解析完成的 DOCX 文档

    包含文档的全部结构化内容。由 parse_docx() 生成，传递给
    export_document() 导出。

    @ivar source_path   源文件路径
    @ivar source_name   源文件名（不含目录）
    @ivar document_xml   主文档 body 的 XML 原文
    @ivar paragraphs     段落列表
    @ivar tables         表格列表
    @ivar equations      公式列表
    @ivar media          媒体文件列表
    @ivar relationships  rId → target 映射
    """
    source_path: Path
    source_name: str
    document_xml: str
    paragraphs: list[Paragraph]
    tables: list[Table]
    equations: list[Equation]
    media: list[Media]
    relationships: dict[str, str]


# ── 公开 API ──────────────────────────────────────────────────────


def parse_docx(path: str | Path) -> ParsedDocx:
    """
    @brief 解析 .docx 文件，返回结构化内容

    打开 DOCX（ZIP 容器），依次提取：关系映射、段落、表格、公式、媒体。

    @param path  .docx 文件路径
    @return      包含全部结构化内容的 ParsedDocx 对象
    """
    source_path = Path(path)
    with zipfile.ZipFile(source_path) as zf:
        document_xml = zf.read("word/document.xml").decode("utf-8")
        rels = _read_relationships(zf)
        root = ET.fromstring(document_xml)
        paragraphs = _extract_paragraphs(root)
        tables = _extract_tables(root)
        equations = _extract_equations(root)
        media = _extract_media(zf, rels, root)
    return ParsedDocx(
        source_path=source_path,
        source_name=source_path.name,
        document_xml=document_xml,
        paragraphs=paragraphs,
        tables=tables,
        equations=equations,
        media=media,
        relationships=rels,
    )


# ── 内部实现 ──────────────────────────────────────────────────────


def _read_relationships(zf: zipfile.ZipFile) -> dict[str, str]:
    """
    @brief 读取 DOCX 的关系文件（.rels），构建 rId → target 映射

    DOCX 中的图片、超链接等通过 rId 引用。此映射用于后续
    将文档中的 rId 引用解析为实际的媒体文件路径。

    @param zf  已打开的 ZIP 文件对象
    @return    rId → target 路径的字典（如 {"rId4": "media/image1.png"}）
    """
    try:
        xml = zf.read("word/_rels/document.xml.rels")
    except KeyError:
        return {}
    root = ET.fromstring(xml)
    rels: dict[str, str] = {}
    for rel in root.findall("rel:Relationship", NS):
        rel_id = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rel_id and target:
            rels[rel_id] = target
    return rels


def _extract_paragraphs(root: ET.Element) -> list[Paragraph]:
    """
    @brief 从文档 XML 中提取所有段落

    遍历 w:body 下的所有 w:p 元素，提取文本、样式，判断是否为标题。

    @param root  文档 XML 的根元素
    @return      段落列表（1-based index）
    """
    paragraphs: list[Paragraph] = []
    for paragraph in root.findall(".//w:body/w:p", NS):
        text = _text_from_element(paragraph)
        style = _paragraph_style(paragraph)
        paragraphs.append(
            Paragraph(
                index=len(paragraphs) + 1,
                text=text,
                style=style,
                is_heading=_is_heading(style, text),
            )
        )
    return paragraphs


def _paragraph_style(paragraph: ET.Element) -> str | None:
    """
    @brief 提取段落的 Word 样式名

    @param paragraph  w:p 元素
    @return           样式名（如 "Heading1"），无样式时返回 None
    """
    style = paragraph.find("./w:pPr/w:pStyle", NS)
    if style is None:
        return None
    return style.attrib.get(f"{{{NS['w']}}}val")


def _is_heading(style: str | None, text: str) -> bool:
    """
    @brief 判断段落是否为标题候选

    两种判断策略：
    1. Word 样式名以 "heading" 开头（大小写不敏感）
    2. 文本模式匹配 "数字.数字... 文字"（如 "5.1.3 Overview"）
       用于捕获使用自定义样式但格式上仍是标题的段落。

    @param style  Word 样式名，可能为 None
    @param text   段落文本
    @return       True 如果判断为标题
    """
    if style and style.lower().startswith("heading"):
        return True
    return bool(re.match(r"^\d+(?:\.\d+)*\s+\S+", text))


def _extract_tables(root: ET.Element) -> list[Table]:
    """
    @brief 从文档 XML 中提取所有表格

    遍历 w:body 下的所有 w:tbl 元素，提取行和单元格，
    并处理垂直合并单元格（vMerge）。

    @param root  文档 XML 的根元素
    @return      表格列表（1-based index）
    """
    tables: list[Table] = []
    for table_el in root.findall(".//w:body/w:tbl", NS):
        rows = _table_rows(table_el)
        _apply_vertical_merges(rows)
        tables.append(Table(index=len(tables) + 1, rows=rows))
    return tables


def _table_rows(table_el: ET.Element) -> list[list[TableCell]]:
    """
    @brief 提取单个表格的所有行和单元格

    处理 gridSpan（水平合并）和 vMerge（垂直合并标记）。
    垂直合并中被省略的后续行标记为 omitted=True，在
    _apply_vertical_merges() 中统一处理。

    @param table_el  w:tbl 元素
    @return          行列表，每行是 TableCell 列表
    """
    rows: list[list[TableCell]] = []
    for tr in table_el.findall("./w:tr", NS):
        row: list[TableCell] = []
        for tc in tr.findall("./w:tc", NS):
            tc_pr = tc.find("./w:tcPr", NS)
            colspan = 1
            omitted = False
            if tc_pr is not None:
                grid_span = tc_pr.find("./w:gridSpan", NS)
                if grid_span is not None:
                    colspan = int(grid_span.attrib.get(f"{{{NS['w']}}}val", "1"))
                v_merge = tc_pr.find("./w:vMerge", NS)
                if v_merge is not None and v_merge.attrib.get(f"{{{NS['w']}}}val") != "restart":
                    omitted = True
            row.append(TableCell(text=_text_from_element(tc), colspan=colspan, omitted=omitted))
        rows.append(row)
    return rows


def _apply_vertical_merges(rows: list[list[TableCell]]) -> None:
    """
    @brief 处理垂直合并单元格 — 将 omitted 单元格的 rowspan 累加到起始单元格

    Word 的 vMerge 机制：合并区域中第一个单元格标记 val="restart"，
    后续单元格省略文本并标记 omitted。此函数将这些后续单元格的
    rowspan 累加到第一个（restart）单元格。

    @param rows  表格行列表（原地修改）
    """
    max_cols = max((len(row) for row in rows), default=0)
    for col in range(max_cols):
        restart_row: int | None = None
        span = 1
        for row_index, row in enumerate(rows):
            if col >= len(row):
                restart_row = None
                span = 1
                continue
            cell = row[col]
            if cell.omitted:
                if restart_row is not None:
                    span += 1
                    rows[restart_row][col] = TableCell(
                        text=rows[restart_row][col].text,
                        rowspan=span,
                        colspan=rows[restart_row][col].colspan,
                    )
                continue
            restart_row = row_index
            span = 1


def _extract_equations(root: ET.Element) -> list[Equation]:
    """
    @brief 从文档 XML 中提取所有 OMML 数学公式

    查找 m:oMath（行内公式）和 m:oMathPara（段落公式）元素。

    @param root  文档 XML 的根元素
    @return      公式列表（1-based index）
    """
    equations: list[Equation] = []
    for element in root.findall(".//m:oMath", NS) + root.findall(".//m:oMathPara", NS):
        equations.append(
            Equation(
                index=len(equations) + 1,
                xml=ET.tostring(element, encoding="unicode"),
                text=_text_from_element(element),
            )
        )
    return equations


def _extract_media(
    zf: zipfile.ZipFile, rels: dict[str, str], root: ET.Element
) -> list[Media]:
    """
    @brief 提取文档中所有内嵌的媒体文件

    扫描 ZIP 中 word/media/ 目录的所有文件，通过关系文件（.rels）
    和文档中的 a:blip 引用匹配关系 ID。

    @param zf    已打开的 ZIP 文件对象
    @param rels  rId → target 映射
    @param root  文档 XML 的根元素（用于提取 a:blip 引用）
    @return      媒体对象列表
    """
    embeds = {
        blip.attrib.get(f"{{{NS['r']}}}embed")
        for blip in root.findall(".//a:blip", NS)
        if blip.attrib.get(f"{{{NS['r']}}}embed")
    }
    media: list[Media] = []
    for name in sorted(n for n in zf.namelist() if n.startswith("word/media/")):
        short = name.removeprefix("word/")
        relationship_id = None
        for rel_id, target in rels.items():
            if target == short or target == short.removeprefix("media/"):
                relationship_id = rel_id
                break
        if relationship_id is None:
            for rel_id in embeds:
                if rels.get(rel_id) == short:
                    relationship_id = rel_id
                    break
        media.append(
            Media(
                name=Path(name).name,
                path=name,
                data=zf.read(name),
                relationship_id=relationship_id,
                target=rels.get(relationship_id) if relationship_id else None,
            )
        )
    return media


def _text_from_element(element: ET.Element) -> str:
    """
    @brief 从 XML 元素中提取纯文本

    收集所有 w:t（Word 文本域）和 m:t（Math 文本域）的文本内容，
    拼接后去除首尾空白。

    @param element  XML 元素
    @return         拼接后的纯文本
    """
    parts: list[str] = []
    for text_el in element.findall(".//w:t", NS) + element.findall(".//m:t", NS):
        if text_el.text:
            parts.append(text_el.text)
    return "".join(parts).strip()
