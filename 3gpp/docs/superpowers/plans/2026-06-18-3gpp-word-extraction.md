---
type: spec
aliases:
  - 2026-06-18-3gpp-word-extraction
tags:
  - 3gpp
  - docs
  - superpowers
  - plan
source_spec: "docs/superpowers/plans/2026-06-18-3gpp-word-extraction.md"
---
# 3GPP Rel-19 Word Extraction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and run a repeatable extraction pipeline for the downloaded 3GPP Rel-19 Word documents.

**Architecture:** A small Python package reads `.docx` ZIP/XML files directly, exports structured artifacts per document, and writes top-level manifests and reports. Legacy `.doc` files are converted with LibreOffice when available, then processed through the same `.docx` path.

**Tech Stack:** Python 3.12 standard library, `unittest`, WordprocessingML XML, optional LibreOffice CLI.

---

## File Structure

- Create `tools/word_extract/__init__.py` for package exports.
- Create `tools/word_extract/docx_parser.py` for parsing `.docx` XML into Python data structures.
- Create `tools/word_extract/exporter.py` for writing per-document artifacts.
- Create `tools/extract_3gpp_word.py` as the CLI entrypoint.
- Create `tests/test_docx_parser.py` for synthetic `.docx` parser tests.
- Write outputs to `3GPP_Rel19/processed`.

## Tasks

### Task 1: Parser Test Fixtures

**Files:**
- Create: `tests/test_docx_parser.py`

- [ ] Write a failing test that builds a minimal `.docx` with one paragraph and expects parsed paragraph text.
- [ ] Run `python3 -m unittest tests.test_docx_parser -v` and verify failure due to missing parser module.
- [ ] Add tests for merged table HTML/CSV structure, equation extraction, and media extraction.

### Task 2: DOCX Parser

**Files:**
- Create: `tools/word_extract/__init__.py`
- Create: `tools/word_extract/docx_parser.py`

- [ ] Implement `parse_docx(path)` returning document metadata, paragraphs, tables, equations, media, and relationship mappings.
- [ ] Run `python3 -m unittest tests.test_docx_parser -v` and verify tests pass.
- [ ] Refactor XML helpers only after tests are green.

### Task 3: Exporter

**Files:**
- Create: `tools/word_extract/exporter.py`
- Modify: `tests/test_docx_parser.py`

- [ ] Add failing tests for artifact writing to a temporary output directory.
- [ ] Implement HTML, CSV, JSONL, metadata, equation XML, and media export.
- [ ] Run `python3 -m unittest tests.test_docx_parser -v` and verify tests pass.

### Task 4: CLI Pipeline

**Files:**
- Create: `tools/extract_3gpp_word.py`

- [ ] Implement source discovery under `3GPP_Rel19/specs`.
- [ ] Implement optional `.doc` conversion through LibreOffice.
- [ ] Implement top-level `manifest.json` and `extraction_report.md`.
- [ ] Run `python3 tools/extract_3gpp_word.py --source 3GPP_Rel19/specs --output 3GPP_Rel19/processed`.

### Task 5: End-to-End Verification

**Files:**
- Generated: `3GPP_Rel19/processed/**`

- [ ] Run unit tests.
- [ ] Run the extraction CLI.
- [ ] Verify manifest source count equals the number of Word files in `3GPP_Rel19/specs`.
- [ ] Verify each `processed` or `converted` document has `metadata.json`, `TS_36.212_36212-j30_content.md`, and `sections.jsonl`.
- [ ] Report any conversion or parsing failures explicitly.
