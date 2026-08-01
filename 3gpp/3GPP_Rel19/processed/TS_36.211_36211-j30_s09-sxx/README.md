# TS 36.211 36211-j30_s09-sxx

## Files

- `source.docx`: normalized source copy for this document directory.
- `document.xml`: WordprocessingML main document body extracted from the DOCX container.
- `content.md`: paragraph-oriented text export for quick reading.
- `full.md`: **agent 友好全文**——公式内联 LaTeX、表格内联 GFM、OLE 公式 SVG+文本注释（首选阅读文件）。
- `sections.jsonl`: heading and section candidates for retrieval/indexing.
- `metadata.json`: machine-readable counts and paths.
- `tables/`: table exports in HTML and CSV.
- `equations/`: raw OMML equation XML files.
- `media/`: embedded media copied from the source package.

## Counts

- Paragraphs: 753
- Heading candidates: 125
- Table artifacts: 32
- Equation artifacts: 220
- Media artifacts: 509

## Reading Notes

- **首选 `full.md`**：公式（LaTeX/SVG+文本）、表格、标题全部内联，agent 与检索直接可读。
-
- Prefer `equations/*.xml` when formulas matter; `content.md` is not authoritative for math.
- Use `sections.jsonl` to anchor answers to section candidates before citing protocol details.
- This directory preserves structure better than raw Markdown conversion, but it does not prove full semantic understanding by a model.
