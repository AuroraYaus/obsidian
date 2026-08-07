"""
@file exporter.py
@brief 将 ParsedDocx 结构化内容导出为文件目录
@date 2026-07-19

将 docx_parser 解析得到的 ParsedDocx 对象导出为可浏览的目录结构：
- source.docx           — 源文件副本
- document.xml          — WordprocessingML 主文档体
- content.md            — 段落文本导出（可读浏览）
- sections.jsonl        — 标题/章节候选（供检索索引）
- tables/               — 表格导出（HTML + CSV 双格式）
- equations/            — 公式 OMML XML
- media/                — 内嵌媒体文件
- metadata.json         — 统计元数据
- README.md             — 目录说明

典型用途：将 3GPP 协议 .docx 转换为结构化知识库素材。

@see docx_parser.py — 解析器（生成 ParsedDocx 输入）
"""

from __future__ import annotations

import csv
import html
import json
import re
import shutil
from pathlib import Path

from .docx_parser import ParsedDocx, Table


def export_document(doc: ParsedDocx, output_root: str | Path) -> dict:
    """
    @brief 将 ParsedDocx 导出为结构化文件目录

    在 output_root 下创建以规范编号+文档名命名的子目录，
    包含源文件副本、段落/表格/公式/媒体的分类导出和元数据。

    @param doc         已解析的文档对象
    @param output_root 输出根目录
    @return            元数据字典（含 source_name, spec, 各类 artifact 计数）
    """
    output_root = Path(output_root)
    spec = _spec_from_name(doc.source_name)
    stem = doc.source_path.stem
    doc_dir = output_root / f"{spec.replace(' ', '_')}_{stem}"
    tables_dir = doc_dir / "tables"
    equations_dir = doc_dir / "equations"
    media_dir = doc_dir / "media"
    for directory in (doc_dir, tables_dir, equations_dir, media_dir):
        directory.mkdir(parents=True, exist_ok=True)

    shutil.copy2(doc.source_path, doc_dir / f"source{doc.source_path.suffix}")
    (doc_dir / "document.xml").write_text(doc.document_xml, encoding="utf-8")
    _write_content_md(doc, doc_dir / "content.md")
    _write_sections_jsonl(doc, doc_dir / "sections.jsonl")
    for table in doc.tables:
        _write_table_html(table, tables_dir / f"table_{table.index:04d}.html")
        _write_table_csv(table, tables_dir / f"table_{table.index:04d}.csv")
    for equation in doc.equations:
        (equations_dir / f"equation_{equation.index:04d}.xml").write_text(
            equation.xml, encoding="utf-8"
        )
    for media in doc.media:
        (media_dir / media.name).write_bytes(media.data)

    metadata = {
        "source_name": doc.source_name,
        "spec": spec,
        "output_dir": str(doc_dir),
        "paragraph_count": len(doc.paragraphs),
        "heading_candidate_count": len([p for p in doc.paragraphs if p.is_heading]),
        "table_count": len(doc.tables),
        "equation_count": len(doc.equations),
        "media_count": len(doc.media),
    }
    (doc_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    _write_readme(doc, metadata, doc_dir)
    return metadata


def _spec_from_name(name: str) -> str:
    """
    @brief 从 3GPP 文档文件名中提取规范编号

    匹配模式 "SSNNN-..." 其中 SS=系列号，NNN=规范号。
    例如 "38212-..." → "TS 38.212"。

    @param name  文件名（如 "38212-g40.docx"）
    @return      规范字符串（如 "TS 38.212"）或 "TS unknown"
    """
    match = re.match(r"([0-9]{2})([0-9]{3})-", name)
    if not match:
        return "TS unknown"
    return f"TS {match.group(1)}.{match.group(2)}"


def _write_content_md(doc: ParsedDocx, path: Path) -> None:
    """
    @brief 导出段落文本为 Markdown（标题用 ##，正文为纯文本）

    非标题段落间用空行分隔，便于快速浏览文档内容。

    @param doc   已解析的文档
    @param path  输出 Markdown 文件路径
    """
    lines = [f"# {_spec_from_name(doc.source_name)} {doc.source_path.stem}", ""]
    for paragraph in doc.paragraphs:
        if not paragraph.text:
            continue
        if paragraph.is_heading:
            lines.extend([f"## {paragraph.text}", ""])
        else:
            lines.extend([paragraph.text, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_sections_jsonl(doc: ParsedDocx, path: Path) -> None:
    """
    @brief 导出章节标题为 JSONL（每行一个 JSON 对象）

    提取所有标题段落，解析章节编号（如 "5.1.3"）和标题文本，
    输出为 JSONL 格式，供后续的语义检索和索引使用。

    @param doc   已解析的文档
    @param path  输出 JSONL 文件路径
    """
    rows = []
    for paragraph in doc.paragraphs:
        if not paragraph.is_heading or not paragraph.text:
            continue
        match = re.match(r"^(\d+(?:\.\d+)*)\s+(.*)$", paragraph.text)
        section = match.group(1) if match else ""
        title = match.group(2) if match else paragraph.text
        rows.append(
            {
                "source": doc.source_name,
                "section": section,
                "title": title,
                "paragraph_index": paragraph.index,
                "style": paragraph.style,
            }
        )
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )


def _write_table_html(table: Table, path: Path) -> None:
    """
    @brief 导出表格为 HTML

    保留 rowspan/colspan 属性，正确处理合并单元格。
    跳过 omitted 单元格（垂直合并中的续行占位符）。

    @param table  表格对象
    @param path   输出 HTML 文件路径
    """
    lines = ["<table>"]
    for row in table.rows:
        lines.append("  <tr>")
        for cell in row:
            if cell.omitted:
                continue
            attrs = []
            if cell.rowspan > 1:
                attrs.append(f'rowspan="{cell.rowspan}"')
            if cell.colspan > 1:
                attrs.append(f'colspan="{cell.colspan}"')
            attr_text = (" " + " ".join(attrs)) if attrs else ""
            lines.append(f"    <td{attr_text}>{html.escape(cell.text)}</td>")
        lines.append("  </tr>")
    lines.append("</table>")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_table_csv(table: Table, path: Path) -> None:
    """
    @brief 导出表格为 CSV

    将 colspan 展开为多个空列，使 CSV 列数对齐到表格的最大宽度。
    omitted 单元格输出为空字符串。

    @param table  表格对象
    @param path   输出 CSV 文件路径
    """
    width = max((sum(cell.colspan for cell in row) for row in table.rows), default=0)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for row in table.rows:
            values: list[str] = []
            for cell in row:
                values.append(cell.text if not cell.omitted else "")
                values.extend([""] * (cell.colspan - 1))
            values.extend([""] * (width - len(values)))
            writer.writerow(values)


def _write_readme(doc: ParsedDocx, metadata: dict, path: Path) -> None:
    """
    @brief 生成导出目录的 README.md 说明文件

    包含目录结构说明、各文件用途、artifact 计数和使用建议。

    @param doc       已解析的文档
    @param metadata  统计元数据字典
    @param path      输出目录路径（README.md 写入此目录下）
    """
    lines = [
        f"# {metadata['spec']} {doc.source_path.stem}",
        "",
        "## Files",
        "",
        f"- `source{doc.source_path.suffix}`: normalized source copy for this document directory.",
        "- `document.xml`: WordprocessingML main document body extracted from the DOCX container.",
        "- `content.md`: paragraph-oriented text export for quick reading.",
        "- `sections.jsonl`: heading and section candidates for retrieval/indexing.",
        "- `metadata.json`: machine-readable counts and paths.",
        "- `tables/`: table exports in HTML and CSV.",
        "- `equations/`: raw OMML equation XML files.",
        "- `media/`: embedded media copied from the source package.",
        "",
        "## Counts",
        "",
        f"- Paragraphs: {metadata['paragraph_count']}",
        f"- Heading candidates: {metadata['heading_candidate_count']}",
        f"- Table artifacts: {metadata['table_count']}",
        f"- Equation artifacts: {metadata['equation_count']}",
        f"- Media artifacts: {metadata['media_count']}",
        "",
        "## Reading Notes",
        "",
        "- Prefer `tables/*.html` when merged cells matter.",
        "- Prefer `equations/*.xml` when formulas matter; `content.md` is not authoritative for math.",
        "- Use `sections.jsonl` to anchor answers to section candidates before citing protocol details.",
        "- This directory preserves structure better than raw Markdown conversion, but it does not prove full semantic understanding by a model.",
        "",
    ]
    (path / "README.md").write_text("\n".join(lines), encoding="utf-8")
