---
type: spec
aliases:
  - 2026-06-25-docs-terminology-consolidation
tags:
  - 3gpp
  - docs
  - superpowers
  - plan
source_spec: "docs/superpowers/plans/2026-06-25-docs-terminology-consolidation.md"
---
# Centralized Docs Terminology Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move all repeated terminology explanations out of `docs/` lesson chapters into a single standalone glossary chapter, then remove redundant full-name explanations from the other lesson chapters.

**Architecture:** Add one canonical glossary chapter under `docs/` that becomes the sole home for recurring abbreviations and brief definitions. Update the lesson chapters in `docs/L1`, `docs/L2`, and `docs/L3` to keep only the shorthand terms they need for readability, while removing the per-chapter term tables and first-use expansion boilerplate. Preserve chapter-specific semantic explanations only where the term is part of the lesson content itself, not where it is acting as a glossary entry.

**Tech Stack:** Markdown, Python scripts under `tools/`, existing lesson audit scripts.

## Global Constraints

- Scope is limited to `docs/` author lesson chapters; do not modify `3GPP_Rel19/processed/`.
- The new standalone glossary must be the single independent chapter that collects recurring term explanations.
- Remove redundant per-chapter term tables and first-use full-name expansions from the other lesson chapters.
- Keep only the shorthand term where needed for readability in lesson prose.
- Preserve existing lesson structure, heading order, and non-terminology content unless required for the terminology migration.

---

### Task 1: Add canonical glossary chapter

**Files:**
- Create: `docs/L0_terminology_glossary.md`
- Modify: `docs/L1/T0.1_LTE_NR_decoder_protocol_reading_map.md`

**Interfaces:**
- Consumes: the recurring abbreviations and definitions already present across `docs/L1`, `docs/L2`, and `docs/L3`
- Produces: a single glossary chapter linked from the reading map

- [ ] **Step 1: Write the glossary content**

Create `docs/L0_terminology_glossary.md` with a title like `# 译码讲义术语总表`, a short scope note, and grouped Markdown tables for the shared abbreviations and lesson terms. Include the canonical short definitions for terms such as `3GPP`, `LTE`, `NR`, `LLR`, `CRC`, `HARQ`, `TB`, `CB`, `LDPC`, `Turbo`, `Polar`, `BLER`, `MCS`, `TBS`, `MAC`, `UL-SCH`, `DL-SCH`, `UCI`, `DCI`, `AWGN`, `BPSK`, `QPSK`, `QAM`, `SRAM`, `PRB`, `RE`, `RV`, `CBG`, and the non-acronym lesson terms already used in `docs` such as `向量`, `矩阵`, `奇偶校验矩阵`, `校验子`, `概率`, `条件概率`, `先验概率`, `似然`, `后验概率`, `证据`, `贝叶斯公式`, `硬判决`, `软判决`, `似然比`, `对数似然比`, `裁剪`, `饱和`, `熵`, `互信息`, `信道容量`, `码率`, `编码增益`, `加性白高斯噪声`, `高斯随机变量`, `噪声方差`, `噪声标准差`, `信噪比`, `每比特能量与噪声谱密度比`, `每符号能量与噪声谱密度比`, `调制阶数`, `星座图`, `同相分量`, `正交分量`, `Gray 映射`, `软解调`, and `逐比特 LLR`.

- [ ] **Step 2: Link the glossary from the reading map**

Update `docs/L1/T0.1_LTE_NR_decoder_protocol_reading_map.md` so the protocol map points to the new glossary chapter in its boundary or navigation section. Keep the chapter itself concise and avoid reintroducing the removed repeated tables.

- [ ] **Step 3: Verify the glossary renders cleanly**

Run a focused Markdown readback on `docs/L0_terminology_glossary.md` and the updated T0.1 file to ensure headings, tables, and links are valid and readable.

### Task 2: Remove redundant terminology tables from lesson chapters

**Files:**
- Modify every `docs/L1/T*.md`, `docs/L2/T*.md`, and `docs/L3/T*.md` lesson chapter that currently contains a `## 术语登场` or `## 本节缩写说明` section

**Interfaces:**
- Consumes: the canonical glossary chapter from Task 1
- Produces: lesson chapters without duplicated term tables

- [ ] **Step 1: Remove the local term section blocks**

Delete the `## 术语登场` or `## 本节缩写说明` section and its table from each lesson chapter. Keep the remaining lesson content intact.

- [ ] **Step 2: Remove leftover first-use full-name boilerplate**

In the same chapters, delete repeated first-use patterns such as `长期演进（Long Term Evolution）`, `新空口（New Radio）`, and similar acronym expansions when they only restate the glossary. Keep only the shorthand term unless the sentence needs a local definition for the lesson itself.

- [ ] **Step 3: Preserve semantic explanations that are not glossary rows**

Retain short in-context explanations when the chapter is teaching the concept itself, such as an algorithm name or a special case explanation that is not just a term-definition pair.

- [ ] **Step 4: Leave the audit hooks intact**

Do not change non-terminology audit lines unless they mention removed glossary content directly.

### Task 3: Run audits and clean residual duplicates

**Files:**
- Modify: any lesson chapter that still fails the terminology audit after Task 2
- Test: `tools/audit_lesson_terms.py`, `tools/audit_markdown_headings.py`

**Interfaces:**
- Consumes: the updated glossary chapter and cleaned lesson chapters
- Produces: passing terminology and heading audits for the docs tree

- [ ] **Step 1: Run terminology audit over `docs/L1 docs/L2 docs/L3`**

Execute `python3 tools/audit_lesson_terms.py docs/L1 docs/L2 docs/L3` and inspect any remaining failures.

- [ ] **Step 2: Fix any residual false positives or missed local definitions**

Adjust the affected lesson chapter if the remaining failure is caused by a removed expansion that the audit still expects or by a genuinely duplicated glossary row.

- [ ] **Step 3: Re-run the audit plus a heading check**

Re-run `python3 tools/audit_lesson_terms.py docs/L1 docs/L2 docs/L3` and `python3 tools/audit_markdown_headings.py docs/L1 docs/L2 docs/L3` to confirm the docs tree remains structurally valid.

- [ ] **Step 4: Commit the terminology migration**

Commit the glossary chapter and the cleaned lesson chapters together with a message that describes the docs terminology consolidation.
