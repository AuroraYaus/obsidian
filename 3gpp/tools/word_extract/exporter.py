from __future__ import annotations

import csv
import html
import json
import re
import shutil
from pathlib import Path

from .docx_parser import ParsedDocx, Table


def export_document(doc: ParsedDocx, output_root: str | Path) -> dict:
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
    match = re.match(r"([0-9]{2})([0-9]{3})-", name)
    if not match:
        return "TS unknown"
    return f"TS {match.group(1)}.{match.group(2)}"


def _write_content_md(doc: ParsedDocx, path: Path) -> None:
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
