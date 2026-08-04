---
type: spec
aliases:
  - 2026-06-21-python-figure-body-equivalents
tags:
  - 3gpp
  - docs
  - superpowers
  - plan
source_spec: "docs/superpowers/plans/2026-06-21-python-figure-body-equivalents.md"
---
# Python Figure Body Equivalents Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix text-fit risks in Python-generated figures and add auditable Mermaid/Markdown equivalents next to every Python PNG used in lesson bodies.

**Architecture:** Add two focused audit scripts, build a migration ledger from existing Markdown/PNG references, fix the highest-risk Python figure scripts first, then migrate lesson bodies in batches. Verification is command-driven and treats PNG assets as visual aids rather than the only expression of teaching content.

**Tech Stack:** Python 3.12 standard library, Markdown text scanning, existing Pillow-based figure scripts, existing `tools/audit_figure_geometry.py` and `tools/audit_figure_readability.py`.

---

## File Structure

- Create `tools/audit_figure_text_fit_static.py`: static risk scanner for `tools/figures/*.py`.
- Create `tools/audit_python_figure_body_equivalents.py`: Markdown scanner requiring nearby body equivalent blocks for Python PNGs.
- Create `tests/test_python_figure_audits.py`: unit tests for both audit scripts using temporary fixtures.
- Create `docs/audits/python_figure_to_body_content_migration.md`: full migration ledger.
- Modify selected `tools/figures/*.py`: remove silent truncation and add text-fit guards.
- Modify `docs/L1_基础/*.md`, `docs/L2_协议算法/*.md`, `docs/L3_工程实现/*.md`: add Mermaid/table equivalents near PNG read guides.
- Modify `docs/audits/image_asset_inventory.md` and `docs/audits/python_figure_textfit_and_body_equivalent_plan.md`: record completion status and commands.

## Tasks

### Task 1: Audit Script Tests

**Files:**
- Create: `tests/test_python_figure_audits.py`

- [ ] Write failing tests for text-fit static audit:
  - A fixture containing `lines[:2]` must be reported.
  - A fixture containing a long direct `draw.text((...), "...very long...")` must be reported.
  - A fixture with `# TEXT_FIT_OK: short coordinate label` before a short direct draw must be accepted.
- [ ] Write failing tests for body equivalent audit:
  - A Markdown fixture with `![x](assets/a.png)` and no nearby marker must be reported.
  - A Markdown fixture with `图片内容正文等价` and a Mermaid block near the image must pass.
  - A Markdown fixture with `Markdown 等价表` near the image must pass.
- [ ] Run `python3 -m unittest tests.test_python_figure_audits -v` and verify failure because the scripts do not exist yet.

### Task 2: Implement Audit Scripts

**Files:**
- Create: `tools/audit_figure_text_fit_static.py`
- Create: `tools/audit_python_figure_body_equivalents.py`
- Modify: `tests/test_python_figure_audits.py`

- [ ] Implement `audit_figure_text_fit_static.py` with a callable `audit_paths(paths: list[Path]) -> list[Finding]`.
- [ ] Detect `lines[:N]`, `wrapped[:N]`, `.splitlines()[:N]`, direct long literal `draw.text(...)`, and fixed table row-height assignments named `row_h`, `row_height`, or `line_h` when no `TEXT_FIT_OK:` appears nearby.
- [ ] Implement CLI output with one finding per line and nonzero exit when findings exist.
- [ ] Implement `audit_python_figure_body_equivalents.py` with `audit_markdown_files(paths: list[Path], window_lines: int = 40) -> list[Finding]`.
- [ ] Treat these nearby markers as valid: `Mermaid 等价图`, `Markdown 等价表`, `图片内容正文等价`.
- [ ] Run `python3 -m unittest tests.test_python_figure_audits -v` and verify tests pass.

### Task 3: Build Migration Ledger

**Files:**
- Create: `docs/audits/python_figure_to_body_content_migration.md`

- [ ] Generate an inventory from Markdown image references under `docs/L1_基础`, `docs/L2_协议算法`, and `docs/L3_工程实现`.
- [ ] Record columns: lesson, image, script, equivalent type, status, body location.
- [ ] Mark existing Mermaid/table equivalents as `present` when they satisfy the audit marker rule.
- [ ] Mark missing equivalents as `missing`.
- [ ] Run `python3 tools/audit_python_figure_body_equivalents.py` and record the initial missing count in the ledger.

### Task 4: Fix P0/P1 Text-Fit Risks

**Files:**
- Modify: `tools/figures/render_lte_nr_rate_matching_comparison.py`
- Modify: `tools/figures/render_nr_polar_channel_polarization.py`
- Modify: `tools/figures/render_nr_polar_ca_scl_selector.py`
- Modify: `tools/figures/render_nr_polar_rate_recovery_flow.py`
- Modify: `tools/figures/render_turbo_ldpc_polar_algorithm_comparison.py`

- [ ] Remove silent truncation such as `lines[:2]`; if space is insufficient, compute row/card height from wrapped text or raise an assertion.
- [ ] Add local text-fit helpers where needed: wrap by measured width, compute line height from `textbbox`, and assert each drawn text bbox stays inside its containing rectangle with padding.
- [ ] Add `TEXT_FIT_OK:` comments only for intentional short labels that do not need wrapping.
- [ ] Regenerate the touched PNGs by running the modified scripts.
- [ ] Run `python3 tools/audit_figure_text_fit_static.py` and fix P0/P1 findings before moving on.
- [ ] Run per-script geometry/readability audits for touched scripts.

### Task 5: Add L1/L2 Body Equivalents

**Files:**
- Modify: `docs/L1_基础/*.md`
- Modify: `docs/L2_协议算法/*.md`

- [ ] For each Python PNG in L1 and L2, add a nearby `图片内容正文等价` section.
- [ ] Use Mermaid for flow/architecture/state images.
- [ ] Use Markdown tables for protocol tables, numeric walkthroughs, descriptors, comparison matrices, and edge-case matrices.
- [ ] For mixed images, add both `Mermaid 等价图` and `Markdown 等价表`.
- [ ] Keep equations and protocol claims consistent with existing lesson text and evidence rows; do not introduce new unverified protocol facts.
- [ ] Run `python3 tools/audit_python_figure_body_equivalents.py docs/L1_基础 docs/L2_协议算法` and resolve all L1/L2 findings.

### Task 6: Add L3 Body Equivalents

**Files:**
- Modify: `docs/L3_工程实现/*.md`

- [ ] For each Python PNG in L3, add a nearby `图片内容正文等价` section.
- [ ] Use Mermaid for project layouts, simulation flows, microarchitectures, testbench flows, synthesis/timing/evidence flows.
- [ ] Use Markdown tables for engineering matrices, register groups, checkpoints, directed cases, coverage bins, sign-off evidence, and constraints.
- [ ] Preserve each lesson's existing warnings about template-only evidence, unrun tools, or protocol-vs-implementation boundaries.
- [ ] Run `python3 tools/audit_python_figure_body_equivalents.py docs/L3_工程实现` and resolve all L3 findings.

### Task 7: Final Verification and Records

**Files:**
- Modify: `docs/audits/python_figure_to_body_content_migration.md`
- Modify: `docs/audits/python_figure_textfit_and_body_equivalent_plan.md`
- Modify: `docs/audits/image_asset_inventory.md`

- [ ] Update the migration ledger so every row is `present` or `not_applicable` with body location.
- [ ] Update the text-fit/body-equivalent plan completion records with exact commands and outcomes.
- [ ] Update the image asset inventory to mention the new audit scripts and final counts.
- [ ] Run:

```bash
python3 -m unittest tests.test_python_figure_audits -v
python3 tools/audit_figure_text_fit_static.py
python3 tools/audit_python_figure_body_equivalents.py
python3 tools/audit_figure_geometry.py tools/figures
python3 tools/audit_figure_readability.py tools/figures
```

- [ ] Report any residual manual-review risk explicitly.

### Task 8: Whole-Project Image Audit Closure

**Files:**
- Modify: `docs/audits/image_asset_inventory.md`
- Modify: `docs/audits/python_figure_textfit_and_body_equivalent_plan.md`
- Modify: `docs/audits/python_figure_to_body_content_migration.md`
- Optionally create: `tools/audit_project_image_inventory.py`

- [ ] Build a whole-project image reference ledger for `docs/L1_基础`, `docs/L2_协议算法`, and `docs/L3_工程实现` with: lesson path, line number, raw PNG reference, resolved asset path, asset existence, unique/reused status, source type, generating script, and inventory row.
- [ ] Classify each unique PNG as `python_pil_drawn`, `python_pdf_crop`, `python_generated_from_table`, or `external_or_unknown`; PDF/Word protocol table crops must be reviewed separately from hand-drawn PIL teaching figures.
- [x] Check Markdown references against `docs/audits/image_asset_inventory.md`: every referenced PNG must exist and have an inventory row; every inventory PNG must record whether it is body-referenced; repeated references must list all use sites. 2026-06-22 新增 `tools/audit_project_image_inventory.py` 后输出 `PROJECT_IMAGE_INVENTORY_AUDIT_OK`，覆盖 68 个实物 PNG、66 个 Markdown PNG 引用、65 个唯一正文引用 PNG 和 3 个 evidence/compatibility 保留 PNG。
- [x] Run body-equivalent quality audit for every body PNG reference, not just marker presence. Rows in `docs/audits/python_figure_to_body_content_migration.md` now distinguish `present_quality_pass; body_referenced` and `evidence_only; compatibility_retained; not_current_body_reference`; `python3 tools/audit_python_figure_body_equivalents.py docs/L1_基础 docs/L2_协议算法 docs/L3_工程实现` 输出 `PYTHON_FIGURE_BODY_EQUIVALENT_AUDIT_OK`。
- [x] Run script-level checks for all `tools/figures/*.py`: `audit_figure_text_fit_static.py`, `audit_figure_readability.py`, `audit_figure_geometry.py --focus-only`, and `audit_figure_geometry.py`. 2026-06-22 最新规则复跑均输出 OK；逐个执行 58 个 Python 文件结果 `FIGURE_SCRIPT_RUNS total=58 failures=0`，其中 57 个为 `render_*.py` 绘图脚本，1 个为 `figure_text_fit.py` helper。
- [ ] Record manual visual review evidence for all 68 physical PNGs: font top/bottom margin, adjacent box spacing, arrow shape/direction, connector endpoints, table cell centering, bottom-note area, protocol-source/crop quality, and residual risk.
- [ ] Add a PDF/Word crop-specific review line for long protocol tables: source page/table number, crop rectangle, split-image readability, stitching boundary, and rule forbidding replacement by old CSV/PIL redraws unless explicitly approved.
- [ ] Final records must include command outputs, failure counts, manual-review boundary, and any remaining risk in `docs/audits/image_asset_inventory.md` or a dedicated whole-project image audit report.
