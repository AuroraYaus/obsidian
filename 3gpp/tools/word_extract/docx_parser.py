from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile


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


@dataclass(frozen=True)
class Paragraph:
    index: int
    text: str
    style: str | None
    is_heading: bool


@dataclass(frozen=True)
class TableCell:
    text: str
    rowspan: int = 1
    colspan: int = 1
    omitted: bool = False


@dataclass(frozen=True)
class Table:
    index: int
    rows: list[list[TableCell]]


@dataclass(frozen=True)
class Equation:
    index: int
    xml: str
    text: str


@dataclass(frozen=True)
class Media:
    name: str
    path: str
    data: bytes
    relationship_id: str | None
    target: str | None


@dataclass(frozen=True)
class ParsedDocx:
    source_path: Path
    source_name: str
    document_xml: str
    paragraphs: list[Paragraph]
    tables: list[Table]
    equations: list[Equation]
    media: list[Media]
    relationships: dict[str, str]


def parse_docx(path: str | Path) -> ParsedDocx:
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


def _read_relationships(zf: zipfile.ZipFile) -> dict[str, str]:
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
    style = paragraph.find("./w:pPr/w:pStyle", NS)
    if style is None:
        return None
    return style.attrib.get(f"{{{NS['w']}}}val")


def _is_heading(style: str | None, text: str) -> bool:
    if style and style.lower().startswith("heading"):
        return True
    return bool(re.match(r"^\d+(?:\.\d+)*\s+\S+", text))


def _extract_tables(root: ET.Element) -> list[Table]:
    tables: list[Table] = []
    for table_el in root.findall(".//w:body/w:tbl", NS):
        rows = _table_rows(table_el)
        _apply_vertical_merges(rows)
        tables.append(Table(index=len(tables) + 1, rows=rows))
    return tables


def _table_rows(table_el: ET.Element) -> list[list[TableCell]]:
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
    parts: list[str] = []
    for text_el in element.findall(".//w:t", NS) + element.findall(".//m:t", NS):
        if text_el.text:
            parts.append(text_el.text)
    return "".join(parts).strip()
