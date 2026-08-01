---
type: spec
aliases:
  - 36.133_36133-j50_sA.8-A.8
tags:
  - 3gpp
  - rel19
  - processed
  - index
source_spec: "3GPP_Rel19/processed/TS_36.133_36133-j50_sA.8-A.8/README.md"
---
# TS 36.133 36133-j50_sA.8-A.8

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

- Paragraphs: 6921
- Heading candidates: 1158
- Table artifacts: 1037
- Equation artifacts: 14
- Media artifacts: 65

## Reading Notes

- Prefer `tables/*.html` when merged cells matter.
- Prefer `equations/*.xml` when formulas matter; `content.md` is not authoritative for math.
- Use `sections.jsonl` to anchor answers to section candidates before citing protocol details.
- This directory preserves structure better than raw Markdown conversion, but it does not prove full semantic understanding by a model.
