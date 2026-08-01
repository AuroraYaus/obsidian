---
type: spec
aliases:
  - 2026-06-19-l1-remaining-lessons
tags:
  - 3gpp
  - docs
  - superpowers
  - plan
source_spec: "docs/superpowers/plans/2026-06-19-l1-remaining-lessons.md"
---
# L1 Remaining Lessons Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reconstruct the already-written L1 lessons so they read as zero-foundation teaching lectures with protocol close reading, theory introduction, explanation, and derivation before extending to later modules.

**Architecture:** Each lesson is a standalone Markdown engineering lecture under `docs/L1/`. The writing structure is elastic: section titles and order should follow the topic, not a fixed template. Every lesson must still preserve auditable teaching ingredients: learning goals, prerequisite or concept setup, zero-foundation theory explanation, worked examples, derivation where relevant, receive-side or engineering consequence, verification, self-test answers, protocol/evidence boundary, execution/evidence record, and references. The project-wide 3GPP protocol-close-reading rule in `合规与遵从.md` applies: any 3GPP-related concept must be taught by Rel-19 protocol context, before/after chain, receive-side implications, and evidence boundaries.

**Tech Stack:** Markdown, LaTeX math, Mermaid, Python verification snippets, SystemVerilog snippets, local 3GPP Rel-19 processed artifacts.

---

## Hard Execution Rules

- [ ] Re-read `合规与遵从.md` before writing each module batch.
- [ ] Re-read the L1 task cards in `2026-06-19-lte-nr-decoding-learning-roadmap.md`.
- [ ] Apply the project-wide zero-foundation theory rule to T1-T5: before formulas, provide theory introduction, concept scaffolding, a numerical or life example where useful, formal definition, hand calculation, and engineering consequence. Do not force fixed second-level headings such as `白话直觉`; use natural subsection names that teach the topic clearly.
- [ ] Apply the project-wide depth rule to T1-T2 before writing more T3: each existing lesson must be expanded beyond outline-level coverage, with terminology origin, problem motivation, formal definition, worked example, derivation, receive-side consequence, verification, implementation impact, protocol evidence boundary, and non-goals/misconceptions where relevant.
- [ ] Apply the project-wide 3GPP protocol-close-reading rule to every 3GPP-related knowledge point: start from protocol context and explain the before/after chain, why the protocol defines it, where it sits in the receive decoding chain, what input/output it implies, and which later Turbo/LDPC/Polar task depends on it.
- [ ] Do not present engineering choices as protocol mandates.
- [ ] If only `content.md` or `sections.jsonl` is inspected, record that formulas/tables are not fully reproduced unless `equations/*.xml` or `tables/*.html` was checked.
- [ ] If a lesson depends on a protocol/paper/book formula, table, figure, or algorithm diagram, reproduce the needed content in the lesson body. Use Markdown/Mermaid/LaTeX when stable; when complex formulas, merged cells, large matrices, or diagrams cannot render cleanly in Markdown, generate a PNG/SVG asset with Python, insert it in the lesson, and record the script, input data, and evidence path.
- [ ] Do not force sections `## 1.` through `## 18.` or `### 15.1`. Natural headings are allowed and preferred when they teach the topic more clearly.
- [ ] Every lesson must include execution/evidence records and a protocol evidence table or protocol/evidence boundary table, even when protocol sections are not directly applicable.

## Files

- Create: `docs/L1/T2.1_AWGN_noise_scaling.md`
- Create: `docs/L1/T2.2_BPSK_QPSK_soft_demapping.md`
- Create: `docs/L1/T2.3_QAM_Max_Log_MAP_demapping.md`
- Create: `docs/L1/T2.4_fading_channel_LLR_reliability.md`
- Create: `docs/L1/T2.5_LLR_clipping_scaling_quantization.md`
- Create: `docs/L1/T3.1_LTE_NR_CRC_families.md`
- Create: `docs/L1/T3.2_transport_code_block_filler_bits.md`
- Create: `docs/L1/T3.3_LTE_Turbo_segmentation_rules.md`
- Create: `docs/L1/T3.4_NR_LDPC_segmentation_rules.md`
- Create: `docs/L1/T3.5_NR_Polar_segmentation_crc.md`
- Later only after T1-T3 are approved: `docs/L1/T4.*.md`
- Later only after T1-T3 are approved: `docs/L1/T5.*.md`

## Current Reconstruction Scope

- Modify: `docs/L1/T1.1_GF2_binary_arithmetic_for_decoders.md`
- Modify: `docs/L1/T1.2_GF2_polynomials_crc_remainders.md`
- Modify: `docs/L1/T1.3_GF2_vectors_matrices.md`
- Modify: `docs/L1/T1.4_probability_bayes_soft_decoding.md`
- Modify: `docs/L1/T1.5_LLR_soft_decision.md`
- Modify: `docs/L1/T1.6_information_theory_minimum_for_decoding.md`
- Modify: `docs/L1/T2.1_AWGN_noise_scaling.md`
- Modify: `docs/L1/T2.2_BPSK_QPSK_soft_demapping.md`
- Modify: `docs/L1/T2.3_QAM_Max_Log_MAP_demapping.md`
- Modify: `docs/L1/T2.4_fading_channel_LLR_reliability.md`
- Modify: `docs/L1/T2.5_LLR_clipping_scaling_quantization.md`
- Modify: `docs/L1/T3.1_LTE_NR_CRC_families.md`
- Modify: `docs/L1/T3.2_transport_code_block_filler_bits.md`
- Modify: `docs/L1/T3.3_LTE_Turbo_segmentation_rules.md`
- Modify: `docs/L1/T3.4_NR_LDPC_segmentation_rules.md`
- Modify: `docs/L1/T3.5_NR_Polar_segmentation_crc.md`

## Module Tasks

### Task 1: T2 Soft Demapping and Channel Model Lessons

**Files:** T2.1-T2.5 listed above.

- [ ] Expand and formal-title-review T2.1 with AWGN, Eb/N0, Es/N0, BPSK LLR, and TS 38.214 modulation-order context.
- [ ] Review T2.1 depth, protocol boundary, formulas, Python verification, and answer table.
- [ ] Expand and formal-title-review T2.2 with BPSK/QPSK constellation, TS 36.211/38.211 modulation context, LLR flow into decoders.
- [ ] Review T2.2 depth and protocol close-reading bridge.
- [ ] Expand and formal-title-review T2.3 with QAM LLR and Max-Log-MAP, TS 38.214 MCS modulation-order context.
- [ ] Review T2.3 depth, terminology first-use coverage, and protocol evidence boundary.
- [ ] Expand and formal-title-review T2.4 with fading reliability, equalizer-output-to-LLR engineering flow, and protocol context.
- [ ] Review T2.4 depth and protocol bridge.
- [ ] Expand and formal-title-review T2.5 with LLR clipping, scaling, quantization, sign convention, and downstream decoder bridge.
- [ ] Review T2.5 depth, terminology first-use coverage, and protocol evidence boundary.

### Task 1A: T1 Foundation Lesson Depth Repair

**Files:** T1.1-T1.6 listed above.

- [ ] Expand and formal-title-review T1.1 GF(2) binary arithmetic.
- [ ] Review T1.1 depth and zero-foundation clarity.
- [ ] Expand and formal-title-review T1.2 GF(2) polynomial CRC remainder.
- [ ] Review T1.2 depth and CRC teaching completeness.
- [ ] Expand and formal-title-review T1.3 GF(2) vectors and matrices.
- [ ] Review T1.3 depth and NR LDPC bridge honesty.
- [ ] Expand and formal-title-review T1.4 probability and Bayes.
- [ ] Review T1.4 depth and soft-decision bridge.
- [ ] Expand and formal-title-review T1.5 LLR soft decision.
- [ ] Review T1.5 depth and protocol boundary.
- [ ] Expand and formal-title-review T1.6 information theory minimum set.
- [ ] Review T1.6 depth and coding-protocol bridge.

### Task 2: T3 CRC, Segmentation, and Transport Block Lessons

**Files:** T3.1-T3.5 listed above.

- [ ] Write T3.1 with LTE/NR CRC family roles, TS 36.212/38.212 close reading, and honest formula evidence boundaries.
- [ ] Review T3.1.
- [ ] Write T3.2 with TB, CB, filler bits, segmentation cause/effect, and receive-side reassembly.
- [ ] Review T3.2.
- [ ] Write T3.3 with LTE Turbo segmentation, CB CRC, parallel code-block decoding, and TS 36.212 evidence.
- [ ] Review T3.3.
- [ ] Write T3.4 with NR LDPC segmentation, base graph/lifting bridge, CB CRC, and TS 38.212 evidence.
- [ ] Review T3.4.
- [ ] Write T3.5 with NR Polar control-information CRC/segmentation context and TS 38.212 evidence.
- [ ] Review T3.5.

### Task 3: T4 Common Decoder Engineering Lessons

**Files:** T4.1-T4.6 listed above.

- [ ] Write T4.1 iterative decoding and extrinsic information.
- [ ] Review T4.1.
- [ ] Write T4.2 factor/Tanner/trellis/tree graph comparison with protocol bridges.
- [ ] Review T4.2.
- [ ] Write T4.3 HARQ soft combining with RV/soft-buffer protocol context.
- [ ] Review T4.3.
- [ ] Write T4.4 early stopping and CRC-gated control.
- [ ] Review T4.4.
- [ ] Write T4.5 BER/BLER/throughput/latency metrics.
- [ ] Review T4.5.
- [ ] Write T4.6 neutral decoder interface contract.
- [ ] Review T4.6.

### Task 4: T5 RTL/ASIC Foundation Lessons

**Files:** T5.1-T5.5 listed above.

- [ ] Write T5.1 fixed-point LLR numbers.
- [ ] Review T5.1.
- [ ] Write T5.2 memory banking and buffering with protocol buffer bridges.
- [ ] Review T5.2.
- [ ] Write T5.3 throughput, latency, and parallelism.
- [ ] Review T5.3.
- [ ] Write T5.4 RTL state machine and valid/ready handshake.
- [ ] Review T5.4.
- [ ] Write T5.5 decoder hardware verification mindset.
- [ ] Review T5.5.

### Task 5: L1 Whole-Stage Review and Commit

- [ ] Verify all 27 L1 lessons exist.
- [ ] Verify all L1 lessons have the required teaching ingredients: goals, concept setup, theory explanation, worked examples, derivation where relevant, verification, self-test answers, protocol/evidence boundary, execution/evidence record, and references.
- [ ] Verify formula tags are unique and ascending per file.
- [ ] Run Python verification snippets for all L1 executable examples or a consolidated equivalent.
- [ ] Scan for forbidden placeholders and jump words.
- [ ] Review protocol evidence honesty across T1-T5.
- [ ] Review the receive-side continuity from demapper LLR to decoder interface and hardware verification.
- [ ] Commit the plan and all L1 lesson files.
