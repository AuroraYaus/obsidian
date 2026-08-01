---
type: spec
aliases:
  - 2026-06-18-3gpp-word-extraction-design
tags:
  - 3gpp
  - docs
  - superpowers
  - spec
source_spec: "docs/superpowers/specs/2026-06-18-3gpp-word-extraction-design.md"
---
# 3GPP Rel-19 Word Extraction Design

## Goal

Build a repeatable local extraction pipeline for the downloaded 3GPP Rel-19 Word documents so an agent can inspect text, tables, formulas, and embedded media with traceable source metadata.

## Scope

The pipeline processes files under `3GPP_Rel19/specs` and writes structured outputs under `3GPP_Rel19/processed`. It preserves original ZIP downloads and extracted Word files. The first implementation targets `.docx` by reading Word XML directly, and attempts to convert legacy `.doc` files to `.docx` with LibreOffice when available.

## Architecture

The implementation is a small Python package under `tools/word_extract` plus a CLI script. The parser treats `.docx` as a ZIP archive, reads `word/document.xml`, `word/_rels/document.xml.rels`, and `word/media/*`, then emits document-level artifacts and a manifest. It does not rely on Markdown conversion as the authoritative source.

## Outputs

Each source document gets its own directory:

```text
3GPP_Rel19/processed/TS_38.212_38212-j30/
  source.docx
  document.xml
  content.md
  sections.jsonl
  metadata.json
  tables/
    table_0001.html
    table_0001.csv
  equations/
    equation_0001.xml
  media/
```

The top-level output contains:

```text
3GPP_Rel19/processed/manifest.json
3GPP_Rel19/processed/extraction_report.md
```

## Data Preservation

Tables are exported to HTML and CSV. HTML preserves `rowspan` and `colspan` where Word uses vertical or grid span merges. CSV provides a simple rectangular view for search and downstream scripting.

Formulas are exported as raw OMML XML files. If later tooling can convert OMML to MathML or LaTeX, those formats can be added without changing the extraction contract. The first version prioritizes not losing equations.

Media files are copied from `word/media` unchanged. Relationship IDs are read so inline drawings can be associated with media targets when possible.

Text and headings are emitted to `content.md` and `sections.jsonl`. Section detection uses paragraph style names and numbered-heading text patterns as heuristics, so the report clearly calls them "section candidates" rather than claiming perfect semantic structure.

## Error Handling

Each file produces a status in the top-level manifest: `processed`, `converted`, `conversion_failed`, or `failed`. Failures are captured per document with the exception message. A failure for one document does not stop processing of other documents.

## Verification

Unit tests use synthetic `.docx` fixtures built in memory. They verify paragraph extraction, merged table export, OMML formula counting/export, media export, and manifest generation. End-to-end verification checks that the Rel-19 processed manifest covers every source Word document and that generated artifact counts match parser counts.

## Constraints

The implementation should use the Python standard library for core extraction. Optional external tools such as LibreOffice are detected at runtime and used only for legacy `.doc` conversion.
