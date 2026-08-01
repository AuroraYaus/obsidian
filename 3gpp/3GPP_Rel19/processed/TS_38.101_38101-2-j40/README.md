# TS 38.101 38101-2-j40

## Files

- `source.docx`: normalized source copy for this document directory.
- `document.xml`: WordprocessingML main document body extracted from the DOCX container.
- `content.md`: paragraph-oriented text export for quick reading.
- `sections.jsonl`: heading and section candidates for retrieval/indexing.
- `metadata.json`: machine-readable counts and paths.
- `tables/`: table exports in HTML and CSV.
- `equations/`: raw OMML equation XML files.
- `media/`: embedded media copied from the source package.

## Counts

- Paragraphs: 3311
- Heading candidates: 572
- Table artifacts: 289
- Equation artifacts: 86
- Media artifacts: 114

## Reading Notes

- Prefer `tables/*.html` when merged cells matter.
- Prefer `equations/*.xml` when formulas matter; `content.md` is not authoritative for math.
- Use `sections.jsonl` to anchor answers to section candidates before citing protocol details.
- This directory preserves structure better than raw Markdown conversion, but it does not prove full semantic understanding by a model.
