---
type: spec
aliases:
  - 2026-06-19-lte-nr-decoding-roadmap-design
tags:
  - 3gpp
  - docs
  - superpowers
  - spec
source_spec: "docs/superpowers/specs/2026-06-19-lte-nr-decoding-roadmap-design.md"
---
# LTE/NR Decoding Learning Roadmap Design

## Goal

Create a detailed 3GPP Rel-19 LTE/NR decoding learning roadmap that matches the depth, task-card style, and engineering orientation of `2026-05-23-ldpc-bp-learning-roadmap-design.md`.

The roadmap focuses on decoding, not full protocol-stack coverage. The three primary algorithm tracks are:

- LTE Turbo decoding.
- NR LDPC decoding for data channels.
- NR Polar decoding for control channels.

The roadmap must guide a communication beginner toward full-stack decoding engineering: theory, floating-point simulation, fixed-point C/C++ model, RTL/ASIC architecture, synthesis, and verification.

## Audience

The learner is a communication beginner with basic programming ability. The roadmap must not assume prior knowledge of linear algebra, probability, random variables, channel models, log-likelihood ratio, soft decisions, fixed-point arithmetic, or hardware microarchitecture.

Every new mathematical, communication, or hardware concept must first be introduced with plain-language intuition and a small countable example before formal notation.

## Source Baseline

The roadmap uses the local Rel-19 corpus as the primary protocol baseline:

| Artifact | Path | Use |
|:---|:---|:---|
| Compliance guide | `合规与遵从.md` | Governs teaching depth, evidence, formatting, and review |
| Reference roadmap | `2026-05-23-ldpc-bp-learning-roadmap-design.md` | Depth and task-card format reference |
| Download manifest | `3GPP_Rel19/manifest.csv` | Protocol number, Rel-19 package, hash, official URL |
| Processed manifest | `3GPP_Rel19/processed/manifest.json` | Extraction status and document counts |
| Processed specs | `3GPP_Rel19/processed/` | Agent-readable text, sections, tables, equations, media |

Current extraction status observed at design time from `3GPP_Rel19/processed/manifest.json`:

| Status | Count |
|:---|---:|
| `processed` | 33 |
| `converted` | 1 |
| Total Word sources | 34 |

Before writing the final roadmap, recheck these counts against `3GPP_Rel19/processed/manifest.json`.

The design depends on the `$3gpp-word-extraction` skill when protocol tables, formulas, raw Word XML, or extraction completeness matter. Markdown `content.md` alone is not enough to claim complete protocol understanding when table or formula semantics are material.

## Protocol Scope

The roadmap centers on LTE and NR decoding.

LTE primary protocol sources:

| Topic | Protocol Source | Local Entry |
|:---|:---|:---|
| Turbo, CRC, code block segmentation, rate matching | TS 36.212 Rel-19 `36212-j30` | `3GPP_Rel19/processed/TS_36.212_36212-j30` |
| Modulation and soft information source | TS 36.211 Rel-19 `36211-j30` | `3GPP_Rel19/processed/TS_36.211_*` |
| MCS, TBS, HARQ, redundancy version | TS 36.213 Rel-19 `36213-j30` | `3GPP_Rel19/processed/TS_36.213_*` |
| MAC HARQ boundary | TS 36.321 Rel-19 `36321-j20` | `3GPP_Rel19/processed/TS_36.321_36321-j20` |
| RRC configuration source | TS 36.331 Rel-19 `36331-j21` | `3GPP_Rel19/processed/TS_36.331_36331-j21` |

NR primary protocol sources:

| Topic | Protocol Source | Local Entry |
|:---|:---|:---|
| CRC, LDPC, Polar, rate matching | TS 38.212 Rel-19 `38212-j30` | `3GPP_Rel19/processed/TS_38.212_38212-j30` |
| Modulation and soft information source | TS 38.211 Rel-19 `38211-j30` | `3GPP_Rel19/processed/TS_38.211_38211-j30` |
| MCS, TBS, CBG, HARQ | TS 38.214 Rel-19 `38214-j30` | `3GPP_Rel19/processed/TS_38.214_38214-j30` |
| PUCCH, PUSCH, PDCCH procedures | TS 38.213 Rel-19 `38213-j30` | `3GPP_Rel19/processed/TS_38.213_38213-j30` |
| MAC HARQ boundary | TS 38.321 Rel-19 `38321-j20` | `3GPP_Rel19/processed/TS_38.321_38321-j20` |
| RRC configuration source | TS 38.331 Rel-19 `38331-j20` | `3GPP_Rel19/processed/TS_38.331_38331-j20` |

RLC, PDCP, and broader architecture topics are included only when they explain decoding boundaries, data recovery after CRC, retransmission context, or configuration flow. The roadmap is not a general LTE/NR protocol-stack course.

## Output Document

Create one final roadmap document in Chinese:

```text
2026-06-19-lte-nr-decoding-learning-roadmap.md
```

This spec under `docs/superpowers/specs/` is only the blueprint. The final roadmap must not be named as another design document.

The roadmap should be comparable in form to the reference LDPC BP roadmap:

- Title and target user profile.
- Hard requirements.
- Formatting standards.
- Rel-19 decoding chapter quick-reference tables.
- Mermaid overview diagram.
- Stage/module/task-card structure.
- Task cards with prompt, output, acceptance, and 3GPP evidence.
- Execution and evidence rules.

Target scale:

- Around 1000 to 1400 lines.
- Around 3 stages.
- Around 15 modules.
- Exactly 91 task cards in the initial approved inventory: `T1.1` through `T15.6`.

Any change to the task count requires explicit review before the final roadmap is written.

## Hard Formatting and Evidence Requirements

The final roadmap must explicitly bind the following rules from `合规与遵从.md`:

| Area | Requirement |
|:---|:---|
| Language | The final roadmap is written in Chinese. First use of an English term must be `中文术语（English term/abbreviation）`. |
| Tables | Use Markdown tables only. Do not use ASCII pseudo-tables or pseudo-architecture diagrams. |
| Diagrams | Use Mermaid with `%%{init: {'theme': 'default'}}%%`. Hardware timing/control diagrams use `stateDiagram-v2` or `sequenceDiagram`. |
| Formulas | Use LaTeX. Block formulas must be independent `$$` blocks with `\tag{}` numbers. Define every symbol before use. |
| Code comments | C/C++ use Doxygen style. Verilog/SystemVerilog must mark clock domain, reset policy, and bit widths. Python/MATLAB key algorithm steps include complexity comments. |
| Protocol evidence | Every protocol-derived claim must cite TS number, Rel-19 package, section, table/figure/formula when applicable, and local path. |
| Unverified anchors | If the exact section/table/formula is not verified, mark the task `待核验` and block final publication until verified. |
| Word formulas | Any task depending on unconverted OMML must mark `公式来源待核验：equations/equation_XXXX.xml`. |
| Zero-basis teaching | Do not assume the learner knows linear algebra, probability, random variables, LLR, SNR, AWGN, matrix rank, fixed-point arithmetic, or RTL timing. |
| Scope | Do not expand into a general LTE/NR protocol-stack course. MAC/RRC/RLC/PDCP appear only as decoding inputs, configuration sources, and system boundaries. |

## Rel-19 Decoding Quick Reference

These anchors seed the final roadmap. Detailed lesson articles must still verify table/formula details in `tables/`, `equations/`, or `document.xml` when the exact values matter. The final roadmap itself must either fully verify every protocol anchor it prints or explicitly mark it `待核验`; unresolved required anchors block final publication.

| Theme | Protocol Anchor | Local Path | Evidence Status |
|:---|:---|:---|:---|
| LTE CRC calculation | TS 36.212 Rel-19 `36212-j30`, §5.1.1 | `3GPP_Rel19/processed/TS_36.212_36212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| LTE code block segmentation and CB CRC | TS 36.212 Rel-19 `36212-j30`, §5.1.2 | `3GPP_Rel19/processed/TS_36.212_36212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| LTE Turbo encoder | TS 36.212 Rel-19 `36212-j30`, §5.1.3.2, Figure 5.1.3-2 | `3GPP_Rel19/processed/TS_36.212_36212-j30` | 章节锚点已从 `content.md` 定位；复现图形前必须核验 figure/media 原始制品 |
| LTE Turbo interleaver | TS 36.212 Rel-19 `36212-j30`, §5.1.3.2.3, Table 5.1.3-3 | `3GPP_Rel19/processed/TS_36.212_36212-j30` | 章节锚点已从 `content.md` 定位；复现参数前必须核验 table 原始制品 |
| LTE Turbo rate matching | TS 36.212 Rel-19 `36212-j30`, §5.1.4.1, Figure 5.1.4-1, Table 5.1.4-1 | `3GPP_Rel19/processed/TS_36.212_36212-j30` | 章节锚点已从 `content.md` 定位；复现参数前必须核验 table 原始制品 |
| LTE UL-SCH Turbo chain | TS 36.212 Rel-19 `36212-j30`, §5.2.2.1-§5.2.2.8 | `3GPP_Rel19/processed/TS_36.212_36212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| LTE DL-SCH Turbo chain | TS 36.212 Rel-19 `36212-j30`, §5.3.2.1-§5.3.2.2 and related coding/rate matching clauses | `3GPP_Rel19/processed/TS_36.212_36212-j30` | 章节锚点已从 `content.md` 定位；最终章节范围必须复核 |
| LTE MCS/TBS/HARQ process context | TS 36.213 Rel-19 `36213-j30`, relevant §7/§8 clauses | `3GPP_Rel19/processed/TS_36.213_36213-j30_*` | 待核验 exact LTE normal-mode anchors before final roadmap |
| NR CRC calculation | TS 38.212 Rel-19 `38212-j30`, §5.1 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；公式细节必须核验原始制品 |
| NR Polar segmentation | TS 38.212 Rel-19 `38212-j30`, §5.2.1 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| NR LDPC segmentation | TS 38.212 Rel-19 `38212-j30`, §5.2.2 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| NR Polar coding | TS 38.212 Rel-19 `38212-j30`, §5.3.1, §5.3.1.2, Table 5.3.1.2-1 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；复现可靠性表前必须核验 table 原始制品 |
| NR LDPC coding | TS 38.212 Rel-19 `38212-j30`, §5.3.2, Table 5.3.2-1/2/3 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；复现基图表前必须核验 table 原始制品 |
| NR Polar rate matching | TS 38.212 Rel-19 `38212-j30`, §5.4.1, §5.4.1.1, Table 5.4.1.1-1 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；复现表格前必须核验 table 原始制品 |
| NR LDPC rate matching and bit interleaving | TS 38.212 Rel-19 `38212-j30`, §5.4.2, §5.4.2.2 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| NR UL-SCH LDPC chain | TS 38.212 Rel-19 `38212-j30`, §6.2.1-§6.2.6 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| NR UCI Polar chain on PUCCH | TS 38.212 Rel-19 `38212-j30`, §6.3.1.2.1, §6.3.1.3.1, §6.3.1.4.1/§6.3.1.4.3 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| NR UCI Polar chain on PUSCH | TS 38.212 Rel-19 `38212-j30`, §6.3.2.2.1, §6.3.2.3.1, §6.3.2.4.1 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| NR DL-SCH LDPC chain | TS 38.212 Rel-19 `38212-j30`, §7.2.1-§7.2.6 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；表格/公式/媒体未核验时不得复现参数 |
| NR DCI Polar context | TS 38.212 Rel-19 `38212-j30`, §7.3 and §7.3.2 | `3GPP_Rel19/processed/TS_38.212_38212-j30` | 章节锚点已从 `content.md` 定位；详细 DCI 映射可能需要核验 TS 38.213/38.214 |
| NR PDSCH MCS/TBS/RV | TS 38.214 Rel-19 `38214-j30`, §5.1.3, §5.1.7 | `3GPP_Rel19/processed/TS_38.214_38214-j30` | 章节锚点已从 `content.md` 定位；复现表格前必须核验 table 原始制品 |
| NR PUSCH MCS/TBS/RV | TS 38.214 Rel-19 `38214-j30`, §6.1.4, §6.1.5 | `3GPP_Rel19/processed/TS_38.214_38214-j30` | 章节锚点已从 `content.md` 定位；复现表格前必须核验 table 原始制品 |

## Roadmap Architecture

The roadmap uses three stages.

| Stage | Modules | Purpose |
|:---|:---|:---|
| L1 beginner stage | M1-M5 | Decoding-specific math, soft information, CRC, iterative decoding, and hardware foundations |
| L2 protocol-algorithm stage | M6-M11 | LTE Turbo, LTE receive chain, NR LDPC, NR LDPC receive chain, NR Polar, LTE/NR decoding comparison |
| L3 engineering stage | M12-M15 | Floating-point models, fixed-point C/C++, RTL/ASIC architecture, synthesis and verification |

Proposed modules:

| Module | Title | Core Purpose |
|:---|:---|:---|
| M1 | Decoding math foundations | GF(2), matrices, probability, Bayesian reasoning, LLR, and information-theory minimum set |
| M2 | Soft demapping and channel models | AWGN, fading, modulation, LLR generation, Max-Log-MAP demapping |
| M3 | CRC, segmentation, and transport-block basics | TB CRC, CB CRC, segmentation, code-block concatenation, LTE/NR differences |
| M4 | Common decoder engineering concepts | Iterative decoding, extrinsic information, early stopping, HARQ soft buffer, quantization |
| M5 | RTL/ASIC prerequisite foundations | Fixed-point arithmetic, memory banking, throughput, latency, pipeline, clock/reset basics |
| M6 | LTE Turbo decoding protocol and algorithms | RSC code, Turbo interleaver, MAP, Log-MAP, Max-Log-MAP, iteration |
| M7 | LTE receive-side decoding chain | De-rate matching, HARQ soft combining, deinterleaving, code block recovery, CRC |
| M8 | NR LDPC decoding protocol and algorithms | Base graph, lifting, parity-check matrix, BP, Min-Sum, NMS, OMS |
| M9 | NR LDPC receive-side decoding chain | Rate recovery, RV, HARQ soft combining, CBG, CRC, early termination |
| M10 | NR Polar decoding protocol and algorithms | Polar construction, frozen bits, reliability sequence, SC, SCL, CRC-aided SCL |
| M11 | LTE/NR decoding comparison | Turbo vs LDPC vs Polar by throughput, latency, area, power, memory, and standard role |
| M12 | Floating-point simulation | Python/MATLAB golden models, BER/BLER curves, seeds, vectors, thresholds |
| M13 | Fixed-point C/C++ models | LLR quantization, saturation, lookup tables, SIMD-aware layout, bit-exact tests |
| M14 | RTL/ASIC decoder architecture | Turbo, LDPC, and Polar microarchitectures, buffers, schedulers, controllers |
| M15 | Synthesis and verification | Testbench, coverage, DC constraints, timing, area, power, regression reports |

## Complete Task-Card Inventory

The final roadmap must include all task cards below in the same Markdown table style. Each task card is a planning card for one future article, not the article body itself.

Prompt calibration rules:

The final roadmap must define the full per-article structure once in a global section named `单节工程讲义统一骨架`. Each task-card `Prompt` should contain task-specific instructions plus the short binding sentence below; do not repeat the full skeleton text in all 91 cards:

```text
写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。
```

| Task Type | Prompt Interpretation |
|:---|:---|
| Foundation tasks | Keep the full article skeleton, but replace non-applicable receive-flow or RTL sections with explicit bridge sections: "how this concept appears in Turbo/LDPC/Polar decoding" and "what later engineering task depends on it". |
| Protocol/algorithm tasks | Use the full skeleton directly. Protocol evidence, receive flow, pseudocode, simulation, fixed-point, RTL/ASIC mapping, and verification are all required unless explicitly marked not applicable with reason. |
| Fixed-point and C/C++ tasks | Emphasize bit-exact interfaces, data types, saturation policy, reproducible tests, and comparison to Python/MATLAB. Protocol sections cite upstream decoder tasks instead of inventing new protocol claims. |
| RTL/ASIC tasks | Emphasize datapath, controller FSM, buffer, timing, reset, throughput, and verification. Formula sections may be architecture equations rather than protocol formulas. |
| Verification/synthesis tasks | Emphasize vector provenance, coverage, reports, tool commands, pass/fail thresholds, and audit evidence. Protocol sections cite upstream vector-generation tasks and exact Rel-19 sources for parameters. |

Task-count summary:

| Module | Count | Range |
|:---|---:|:---|
| M1 | 6 | T1.1-T1.6 |
| M2 | 5 | T2.1-T2.5 |
| M3 | 5 | T3.1-T3.5 |
| M4 | 6 | T4.1-T4.6 |
| M5 | 5 | T5.1-T5.5 |
| M6 | 8 | T6.1-T6.8 |
| M7 | 6 | T7.1-T7.6 |
| M8 | 8 | T8.1-T8.8 |
| M9 | 6 | T9.1-T9.6 |
| M10 | 8 | T10.1-T10.8 |
| M11 | 5 | T11.1-T11.5 |
| M12 | 5 | T12.1-T12.5 |
| M13 | 6 | T13.1-T13.6 |
| M14 | 6 | T14.1-T14.6 |
| M15 | 6 | T15.1-T15.6 |
| Total | 91 | T1.1-T15.6 |

Decoder-family coverage:

| Family | Theory/Protocol | Receive Chain | Simulation | Fixed-Point | RTL/ASIC | Verification |
|:---|:---|:---|:---|:---|:---|:---|
| LTE Turbo | T6.1-T6.8 | T7.1-T7.6 | T12.2 | T13.2 | T14.1, T14.4-T14.6 | T15.1-T15.6 |
| NR LDPC | T8.1-T8.8 | T9.1-T9.6 | T12.3 | T13.3 | T14.2, T14.4-T14.6 | T15.1-T15.6 |
| NR Polar | T10.1-T10.8 | T10.7-T10.8 | T12.4 | T13.4 | T14.3-T14.6 | T15.1-T15.6 |

### L1 Beginner Stage

#### M1 Decoding Math Foundations

##### T1.1 GF(2) Binary Arithmetic for Decoders

| Item | Requirement |
|:---|:---|
| `编号` | T1.1 |
| `前置` | None |
| `Prompt` | Write a zero-basis Chinese article explaining finite field GF(2) for LTE/NR decoders. Cover XOR as addition, AND as multiplication, polynomial representation, why binary channel codes use GF(2), and how CRC and parity checks depend on these operations. Include plain-language intuition before symbols, truth tables, two hand-calculation examples, and a small Python verification snippet with fixed inputs. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T1.1_GF2_binary_arithmetic_for_decoders.md` |
| `验收` | Learner can hand-calculate GF(2) addition, multiplication, polynomial addition, and one polynomial division step used by CRC. |
| `3GPP/证据` | Background task. Protocol linkage to TS 36.212 Rel-19 `36212-j30` §5.1.1 and TS 38.212 Rel-19 `38212-j30` §5.1 must be cited when motivating CRC, with local paths listed below. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T1.2 GF(2) Polynomials and CRC Remainders

| Item | Requirement |
|:---|:---|
| `编号` | T1.2 |
| `前置` | T1.1 |
| `Prompt` | Explain GF(2) polynomial long division as the arithmetic core of cyclic redundancy check. Start from ordinary integer division analogy, then show why subtraction equals XOR in GF(2). Include one 8-bit message plus CRC-4 teaching example and one LTE/NR-motivated example that references CRC generator polynomials without reproducing unchecked Word formulas. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T1.2_GF2_polynomials_crc_remainders.md` |
| `验收` | Learner can compute a short CRC remainder manually and explain why a zero syndrome indicates no detected error. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.1; TS 38.212 Rel-19 `38212-j30` §5.1; local processed directories; formula details must be checked in raw artifacts before final reproduction. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T1.3 Vectors and Matrices over GF(2)

| Item | Requirement |
|:---|:---|
| `编号` | T1.3 |
| `前置` | T1.1 |
| `Prompt` | Teach vectors, matrices, transpose, multiplication, rank intuition, and sparse matrices over GF(2) for decoding. Use small parity-check examples and connect them to LDPC parity-check matrices. Include a 3-by-6 example, hand multiplication, and a Python check. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T1.3_GF2_vectors_matrices.md` |
| `验收` | Learner can multiply a binary vector by a parity-check matrix and interpret a non-zero syndrome. |
| `3GPP/证据` | Background task. Connect to TS 38.212 Rel-19 `38212-j30` §5.3.2, Table 5.3.2-1/2/3, local path `3GPP_Rel19/processed/TS_38.212_38212-j30`. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T1.4 Probability, Conditional Probability, and Bayes for Soft Decoding

| Item | Requirement |
|:---|:---|
| `编号` | T1.4 |
| `前置` | None |
| `Prompt` | Teach probability, conditional probability, prior probability, likelihood, posterior probability, evidence, and Bayes formula for a learner who has not studied probability. Use Chinese term first with English in parentheses. Tie the concepts to deciding whether a received noisy bit was 0 or 1. Include two numeric examples and no unsupported shortcut language. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T1.4_probability_bayes_soft_decoding.md` |
| `验收` | Learner can calculate a simple posterior probability and explain what likelihood means in demapping. |
| `3GPP/证据` | Background task. Cite TS 36.211 Rel-19 `36211-j30_*` / TS 38.211 Rel-19 `38211-j30` only as later soft-information source, exact modulation anchors `待核验`. Local evidence path(s): TS 36.211 -> `3GPP_Rel19/processed/TS_36.211_*` (exact part `待核验`); TS 38.211 -> `3GPP_Rel19/processed/TS_38.211_38211-j30`. |

##### T1.5 Log-Likelihood Ratio and Soft Decision

| Item | Requirement |
|:---|:---|
| `编号` | T1.5 |
| `前置` | T1.4 |
| `Prompt` | Explain hard decision, soft decision, and log-likelihood ratio (LLR) from probability ratios. Derive the sign and magnitude meaning of LLR step by step. Show why decoders prefer LLR over raw probability, including numerical stability and addition of independent evidence. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T1.5_LLR_soft_decision.md` |
| `验收` | Learner can convert probabilities to LLR and interpret positive, negative, zero, large, and saturated LLR values. |
| `3GPP/证据` | Background task. Link to demapper outputs from TS 36.211 Rel-19 `36211-j30_*` / TS 38.211 Rel-19 `38211-j30` with exact anchors `待核验`. Local evidence path(s): TS 36.211 -> `3GPP_Rel19/processed/TS_36.211_*` (exact part `待核验`); TS 38.211 -> `3GPP_Rel19/processed/TS_38.211_38211-j30`. |

##### T1.6 Information-Theory Minimum Set for Decoding

| Item | Requirement |
|:---|:---|
| `编号` | T1.6 |
| `前置` | T1.4, T1.5 |
| `Prompt` | Explain entropy, mutual information, channel capacity, code rate, coding gain, and why Turbo/LDPC/Polar codes matter. Keep this as a decoding-motivated minimum set rather than a full information theory course. Include a BSC example and an AWGN intuition example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T1.6_information_theory_minimum_for_decoding.md` |
| `验收` | Learner can explain code rate, capacity intuition, and why iterative soft decoding improves reliability. |
| `3GPP/证据` | Background task. Connect to LTE Turbo and NR LDPC/Polar channel coding usage in TS 36.212 Rel-19 `36212-j30` and TS 38.212 Rel-19 `38212-j30`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

#### M2 Soft Demapping and Channel Models

##### T2.1 AWGN Channel and Noise Scaling

| Item | Requirement |
|:---|:---|
| `编号` | T2.1 |
| `前置` | T1.4, T1.5 |
| `Prompt` | Explain additive white Gaussian noise (AWGN), Gaussian random variables, SNR, Eb/N0, Es/N0, code rate, modulation order, and noise variance scaling. Include derivation for BPSK LLR in AWGN and a reproducible Python simulation with seed. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T2.1_AWGN_noise_scaling.md` |
| `验收` | Learner can compute noise variance for a given code rate, modulation order, and Eb/N0, and generate reproducible noisy BPSK samples. |
| `3GPP/证据` | Background task. Modulation order linkage to TS 38.214 Rel-19 `38214-j30` §5.1.3/§6.1.4 and LTE equivalent anchors `待核验`. Local evidence path(s): TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`. |

##### T2.2 BPSK and QPSK Soft Demapping

| Item | Requirement |
|:---|:---|
| `编号` | T2.2 |
| `前置` | T1.5, T2.1 |
| `Prompt` | Teach BPSK and QPSK constellation mapping, Gray mapping, received sample model, exact LLR for BPSK, and bit-wise LLR for QPSK. Include diagrams in Mermaid where possible and a small numerical demapper example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T2.2_BPSK_QPSK_soft_demapping.md` |
| `验收` | Learner can derive BPSK LLR and compute QPSK bit LLRs for one received symbol. |
| `3GPP/证据` | TS 36.211 Rel-19 `36211-j30_*` modulation clauses `待核验`; TS 38.211 Rel-19 `38211-j30` modulation clauses `待核验`. Local evidence path(s): TS 36.211 -> `3GPP_Rel19/processed/TS_36.211_*` (exact part `待核验`); TS 38.211 -> `3GPP_Rel19/processed/TS_38.211_38211-j30`. |

##### T2.3 QAM Soft Demapping and Max-Log-MAP

| Item | Requirement |
|:---|:---|
| `编号` | T2.3 |
| `前置` | T2.2 |
| `Prompt` | Explain 16QAM, 64QAM, 256QAM bit mapping, exact bit LLR, and Max-Log-MAP approximation. Show why practical decoders use approximation and lookup/nearest-distance simplifications. Include one 16QAM worked example and one failure case where LLR sign is inverted. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T2.3_QAM_Max_Log_MAP_demapping.md` |
| `验收` | Learner can compute approximate bit LLR for a 16QAM symbol and explain complexity growth for higher QAM. |
| `3GPP/证据` | TS 38.214 Rel-19 `38214-j30` MCS modulation order sections §5.1.3/§6.1.4; TS 38.211 modulation clauses `待核验`; LTE anchors `待核验`. Local evidence path(s): TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`; TS 38.211 -> `3GPP_Rel19/processed/TS_38.211_38211-j30`. |

##### T2.4 Fading Channels and LLR Reliability

| Item | Requirement |
|:---|:---|
| `编号` | T2.4 |
| `前置` | T2.1, T2.2 |
| `Prompt` | Explain Rayleigh/Rician fading at decoder input level, channel equalization output, and how channel gain changes LLR reliability. Keep the focus on what the decoder sees: soft bits plus reliability. Include one single-tap fading example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T2.4_fading_channel_LLR_reliability.md` |
| `验收` | Learner can explain why equalized symbols with low channel gain should have smaller LLR magnitude. |
| `3GPP/证据` | Background task. Link to physical channel and demodulation context in TS 36.211 Rel-19 `36211-j30_*` / TS 38.211 Rel-19 `38211-j30`, exact anchors `待核验`. Local evidence path(s): TS 36.211 -> `3GPP_Rel19/processed/TS_36.211_*` (exact part `待核验`); TS 38.211 -> `3GPP_Rel19/processed/TS_38.211_38211-j30`. |

##### T2.5 LLR Clipping, Scaling, and Quantization Preview

| Item | Requirement |
|:---|:---|
| `编号` | T2.5 |
| `前置` | T1.5, T2.1 |
| `Prompt` | Introduce LLR clipping, scaling, quantization, saturation, and why fixed-point decoders cannot keep infinite precision. Include examples of overconfident LLR, under-scaled LLR, and sign error. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T2.5_LLR_clipping_scaling_quantization.md` |
| `验收` | Learner can explain why LLR magnitude saturation changes decoder behavior and identify a likely LLR sign convention bug. |
| `3GPP/证据` | No direct 3GPP citation required for the quantization concept. Downstream decoder-family articles must cite their own Rel-19 protocol evidence. |

#### M3 CRC, Segmentation, and Transport-Block Basics

##### T3.1 LTE and NR CRC Families

| Item | Requirement |
|:---|:---|
| `编号` | T3.1 |
| `前置` | T1.2 |
| `Prompt` | Explain LTE/NR CRC families used in decoding, including CRC purpose, generator polynomial concept, TB CRC, CB CRC, and control-channel CRC. Do not reproduce polynomial formulas until raw artifacts are verified. Include a small executable CRC example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T3.1_LTE_NR_CRC_families.md` |
| `验收` | Learner can distinguish TB CRC, CB CRC, and control CRC roles in decoder pass/fail decisions. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.1, §5.2.2.1, §5.3.2.1; TS 38.212 Rel-19 `38212-j30` §5.1, §6.2.1, §7.2.1, §7.3.2; local paths listed below. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T3.2 Transport Block, Code Block, and Filler Bits

| Item | Requirement |
|:---|:---|
| `编号` | T3.2 |
| `前置` | T3.1 |
| `Prompt` | Explain transport block, code block, segmentation, filler bits, and why large TBs are split before Turbo/LDPC decoding. Include LTE and NR side-by-side terminology and one small segmentation example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T3.2_transport_code_block_filler_bits.md` |
| `验收` | Learner can explain why decoder works per code block but final pass/fail is per transport block. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.2; TS 38.212 Rel-19 `38212-j30` §5.2.1/§5.2.2; local paths listed below. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T3.3 LTE Turbo Segmentation Rules

| Item | Requirement |
|:---|:---|
| `编号` | T3.3 |
| `前置` | T3.1, T3.2 |
| `Prompt` | Teach LTE Turbo-specific code block segmentation and code block CRC attachment from the receive-side perspective. Explain maximum code block size, filler bits, CB CRC, and how segmentation affects parallel decoding. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T3.3_LTE_Turbo_segmentation_rules.md` |
| `验收` | Learner can map one LTE TB size to code block count and identify where CB CRC is checked. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30`, §5.1.2, §5.2.2.2, §5.3.2.2; local path listed below. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T3.4 NR LDPC Segmentation Rules

| Item | Requirement |
|:---|:---|
| `编号` | T3.4 |
| `前置` | T3.1, T3.2 |
| `Prompt` | Explain NR LDPC code block segmentation, base-graph-dependent maximum block size, lifting-size interaction, and CB CRC. Include one example showing why base graph selection affects segmentation. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T3.4_NR_LDPC_segmentation_rules.md` |
| `验收` | Learner can explain the relationship among TB size, code blocks, base graph, lifting size, and CB CRC. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30`, §5.2.2, §6.2.2, §6.2.3, §7.2.2, §7.2.3; local path listed below. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T3.5 NR Polar Segmentation and CRC Attachment

| Item | Requirement |
|:---|:---|
| `编号` | T3.5 |
| `前置` | T3.1, T3.2 |
| `Prompt` | Explain NR Polar segmentation and CRC attachment for control information. Cover why control-channel payloads have different CRC and segmentation behavior than LDPC transport blocks. Include PUCCH/PUSCH UCI context and DCI context without expanding into a full control-channel course. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T3.5_NR_Polar_segmentation_crc.md` |
| `验收` | Learner can explain when Polar-coded control information gets CRC and how CRC supports SCL path selection. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.2.1, §6.3.1.2.1, §6.3.2.2.1, §7.3.2; local path listed below. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

#### M4 Common Decoder Engineering Concepts

##### T4.1 Iterative Decoding and Extrinsic Information

| Item | Requirement |
|:---|:---|
| `编号` | T4.1 |
| `前置` | T1.5 |
| `Prompt` | Explain iterative decoding, intrinsic information, extrinsic information, and why Turbo and LDPC decoders refine beliefs over iterations. Use a simple two-check example and avoid assuming graph theory. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T4.1_iterative_decoding_extrinsic_information.md` |
| `验收` | Learner can distinguish channel LLR, a priori information, extrinsic information, and posterior LLR. |
| `3GPP/证据` | Algorithm background. Connect to LTE Turbo and NR LDPC tasks; no direct 3GPP formula claim. |

##### T4.2 Factor Graphs, Tanner Graphs, and Trellises

| Item | Requirement |
|:---|:---|
| `编号` | T4.2 |
| `前置` | T1.3, T4.1 |
| `Prompt` | Explain factor graph, Tanner graph, and trellis using decoder-friendly intuition. Contrast Turbo trellis-based decoding with LDPC graph-based decoding and Polar tree-based decoding. Include Mermaid diagrams. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T4.2_graphs_trellises_trees_for_decoding.md` |
| `验收` | Learner can identify which graphical model belongs to Turbo, LDPC, and Polar decoding. |
| `3GPP/证据` | Algorithm background. Link to TS 36.212 Rel-19 `36212-j30` §5.1.3.2 Figure 5.1.3-2 and TS 38.212 Rel-19 `38212-j30` §5.3.2 Table 5.3.2-1/2/3. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T4.3 HARQ Soft Combining Basics

| Item | Requirement |
|:---|:---|
| `编号` | T4.3 |
| `前置` | T1.5, T2.5 |
| `Prompt` | Explain hybrid automatic repeat request (HARQ), redundancy version, soft buffer, Chase combining vs incremental redundancy intuition, and why decoder input accumulates LLRs across transmissions. Include one soft-combining numeric example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T4.3_HARQ_soft_combining_basics.md` |
| `验收` | Learner can explain why retransmission LLRs are added or placed into a circular-buffer-derived soft buffer. |
| `3GPP/证据` | LTE TS 36.212 Rel-19 `36212-j30` §5.1.4.1 and TS 36.213 HARQ/RV anchors `待核验`; NR TS 38.212 Rel-19 `38212-j30` §5.4.2 and TS 38.214 Rel-19 `38214-j30` §5.1.3/§6.1.4/§5.1.7/§6.1.5. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`; TS 36.213 -> `3GPP_Rel19/processed/TS_36.213_*` (exact part `待核验`). |

##### T4.4 Early Stopping and CRC-Gated Decoder Control

| Item | Requirement |
|:---|:---|
| `编号` | T4.4 |
| `前置` | T3.1, T4.1 |
| `Prompt` | Explain decoder early stopping using parity checks and CRC checks. Compare Turbo CRC-gated stopping, LDPC syndrome/CRC stopping, and Polar CRC-aided list selection. Include failure case of false CRC pass probability as a qualitative risk. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T4.4_early_stopping_crc_gated_control.md` |
| `验收` | Learner can design a high-level stop condition for Turbo, LDPC, and Polar decoders. |
| `3GPP/证据` | CRC anchors from TS 36.212 Rel-19 `36212-j30` / TS 38.212 Rel-19 `38212-j30`; algorithmic stopping is implementation guidance unless directly cited. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T4.5 Decoder Performance Metrics

| Item | Requirement |
|:---|:---|
| `编号` | T4.5 |
| `前置` | T1.6, T2.1 |
| `Prompt` | Explain BER, BLER, FER, throughput, latency, iteration count, energy per bit, and area-throughput tradeoff. Include how to plot BLER vs Eb/N0 and how many frames are needed for confidence. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T4.5_decoder_performance_metrics.md` |
| `验收` | Learner can define BLER and explain why decoder studies usually focus on BLER for transport blocks. |
| `3GPP/证据` | Engineering background. Link to transport block CRC pass/fail in TS 36.212 Rel-19 `36212-j30` / TS 38.212 Rel-19 `38212-j30`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T4.6 Decoder Interface Contracts

| Item | Requirement |
|:---|:---|
| `编号` | T4.6 |
| `前置` | T3.2, T4.3 |
| `Prompt` | Define common decoder interfaces: input LLR stream, code block metadata, redundancy version, HARQ process ID, output bits, CRC status, iteration count, and error flags. Include a neutral interface table usable for Turbo, LDPC, and Polar. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T4.6_decoder_interface_contracts.md` |
| `验收` | Learner can specify a decoder input/output contract independent of algorithm internals. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` / TS 38.212 Rel-19 `38212-j30` code block and rate matching anchors; TS 38.214/TS 36.213 HARQ/RV context. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`; TS 36.213 -> `3GPP_Rel19/processed/TS_36.213_*` (exact part `待核验`). |

#### M5 RTL/ASIC Prerequisite Foundations

##### T5.1 Fixed-Point Numbers for LLR Processing

| Item | Requirement |
|:---|:---|
| `编号` | T5.1 |
| `前置` | T2.5 |
| `Prompt` | Teach signed fixed-point representation, two's complement, integer/fraction split, saturation, rounding, and clipping for decoder LLR processing. Include Q-format examples and Python bit-level checks. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T5.1_fixed_point_numbers_for_LLR.md` |
| `验收` | Learner can encode and decode signed fixed-point LLR values and explain saturation. |
| `3GPP/证据` | No direct 3GPP citation required. The article must explicitly state this is an implementation foundation and point to downstream protocol tasks for normative evidence. |

##### T5.2 Memory Banking and Buffering Basics

| Item | Requirement |
|:---|:---|
| `编号` | T5.2 |
| `前置` | T4.6 |
| `Prompt` | Explain SRAM, register file, ping-pong buffer, circular buffer, memory banking, and bank conflict using decoder examples. Include Turbo interleaver memory, LDPC layered memory, and Polar path memory as previews. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T5.2_memory_banking_buffering_basics.md` |
| `验收` | Learner can explain why parallel decoders need banked memory and identify one bank conflict scenario. |
| `3GPP/证据` | Engineering background plus protocol context: LTE circular-buffer rate matching from TS 36.212 Rel-19 `36212-j30` §5.1.4.1, local path `3GPP_Rel19/processed/TS_36.212_36212-j30`; NR LDPC rate matching context from TS 38.212 Rel-19 `38212-j30` §5.4.2 and NR Polar rate matching context from TS 38.212 Rel-19 `38212-j30` §5.4.1, local path `3GPP_Rel19/processed/TS_38.212_38212-j30`. Exact table/figure details remain `待核验` before reproduction. |

##### T5.3 Throughput, Latency, and Parallelism

| Item | Requirement |
|:---|:---|
| `编号` | T5.3 |
| `前置` | T4.5 |
| `Prompt` | Explain decoder throughput, latency, initiation interval, clock frequency, parallelism, and iteration impact. Include formulas with defined symbols and examples for Turbo, LDPC, and Polar at a high level. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T5.3_throughput_latency_parallelism.md` |
| `验收` | Learner can estimate bits per second from block size, cycles, iterations, and clock frequency. |
| `3GPP/证据` | Engineering background. Connect to TS 38.214 Rel-19 `38214-j30` processing/HARQ context where relevant; exact anchors `待核验`. Local evidence path(s): TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`. |

##### T5.4 RTL State Machines and Handshake Basics

| Item | Requirement |
|:---|:---|
| `编号` | T5.4 |
| `前置` | T4.6 |
| `Prompt` | Explain RTL module interfaces, valid/ready handshake, finite-state machine, reset strategy, and clock domain basics for decoder blocks. Use Mermaid `stateDiagram-v2` and SystemVerilog-style interface snippets. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T5.4_RTL_state_machine_handshake_basics.md` |
| `验收` | Learner can draw a decoder controller FSM with idle, load, decode, check, output, and error states. |
| `3GPP/证据` | No direct 3GPP citation required. The article must explicitly state this is an implementation foundation and point to downstream protocol tasks for normative evidence. |

##### T5.5 Verification Mindset for Decoder Hardware

| Item | Requirement |
|:---|:---|
| `编号` | T5.5 |
| `前置` | T4.5, T5.1 |
| `Prompt` | Teach golden model, bit-exact comparison, constrained random testing, corner cases, coverage, regression, and waveform debugging for decoders. Include how CRC pass/fail becomes an observable verification result. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L1/T5.5_decoder_hardware_verification_mindset.md` |
| `验收` | Learner can list a minimum verification plan for a code block decoder. |
| `3GPP/证据` | Engineering background with CRC anchors from TS 36.212 Rel-19 `36212-j30` / TS 38.212 Rel-19 `38212-j30`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

### L2 Protocol-Algorithm Stage

#### M6 LTE Turbo Decoding Protocol and Algorithms

##### T6.1 LTE Turbo Decoder Chain Overview

| Item | Requirement |
|:---|:---|
| `编号` | T6.1 |
| `前置` | T3.3, T4.1 |
| `Prompt` | Present the LTE Turbo receive-side chain from demapper LLRs through de-rate matching, deinterleaving, Turbo decoding, CB CRC, code block concatenation, and TB CRC. Emphasize receiver inverse operations and local protocol evidence. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T6.1_LTE_Turbo_decoder_chain_overview.md` |
| `验收` | Learner can draw the LTE Turbo decoding chain and name each input/output. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.1-§5.1.4.1, §5.2.2, §5.3.2; local path listed below. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T6.2 Recursive Systematic Convolutional Code Foundation

| Item | Requirement |
|:---|:---|
| `编号` | T6.2 |
| `前置` | T1.1, T4.2 |
| `Prompt` | Explain recursive systematic convolutional (RSC) code, state, shift register, generator polynomial intuition, systematic bit, parity bit, and trellis. Include a tiny non-LTE toy RSC example before connecting to LTE Turbo. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T6.2_RSC_code_foundation.md` |
| `验收` | Learner can trace a simple RSC encoder state transition and parity output. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.3.2.1 and Figure 5.1.3-2; local media/figure artifact must be checked before reproduction. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T6.3 LTE Turbo Encoder and Trellis Termination

| Item | Requirement |
|:---|:---|
| `编号` | T6.3 |
| `前置` | T6.2 |
| `Prompt` | Teach LTE Turbo encoder structure, two 8-state constituent encoders, rate 1/3 output streams, internal interleaver input to second encoder, and trellis termination. Explain from decoder perspective why tail bits matter. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T6.3_LTE_Turbo_encoder_trellis_termination.md` |
| `验收` | Learner can identify systematic, parity-1, parity-2, and tail-bit streams in LTE Turbo coding. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.3.2.1, §5.1.3.2.2, Figure 5.1.3-2; local path listed below. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T6.4 LTE Turbo Internal Interleaver

| Item | Requirement |
|:---|:---|
| `编号` | T6.4 |
| `前置` | T6.3 |
| `Prompt` | Explain LTE Turbo internal interleaver, why interleaving creates diversity, how interleaver parameters are selected by block size, and how decoder address generation uses it. Include one small artificial interleaver example and require checking Table 5.1.3-3 before reproducing parameters. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T6.4_LTE_Turbo_internal_interleaver.md` |
| `验收` | Learner can explain how interleaver and deinterleaver address maps are related. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.3.2.3, Table 5.1.3-3; local table artifact must be checked. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T6.5 BCJR and MAP Decoding Intuition

| Item | Requirement |
|:---|:---|
| `编号` | T6.5 |
| `前置` | T1.4, T4.2, T6.2 |
| `Prompt` | Explain BCJR/MAP decoding for convolutional trellises using forward metric, backward metric, branch metric, and posterior LLR. Start with a tiny trellis and derive the update equations carefully. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T6.5_BCJR_MAP_decoding_intuition.md` |
| `验收` | Learner can describe alpha, beta, gamma metrics and their role in bit posterior probability. |
| `3GPP/证据` | Algorithm background for LTE Turbo; no direct 3GPP formula claim. |

##### T6.6 Log-MAP and Max-Log-MAP Turbo Decoding

| Item | Requirement |
|:---|:---|
| `编号` | T6.6 |
| `前置` | T6.5 |
| `Prompt` | Derive Log-MAP from MAP using log-domain arithmetic, explain max-star correction, then derive Max-Log-MAP approximation and its performance/complexity tradeoff. Include a numeric max-star example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T6.6_Log_MAP_Max_Log_MAP_Turbo.md` |
| `验收` | Learner can explain why Max-Log-MAP is simpler and what correction it drops. |
| `3GPP/证据` | Algorithm background for LTE Turbo decoder implementation. |

##### T6.7 Turbo Iteration, Extrinsic Exchange, and Stopping

| Item | Requirement |
|:---|:---|
| `编号` | T6.7 |
| `前置` | T4.1, T6.6 |
| `Prompt` | Explain two SISO decoders, interleaving/deinterleaving of extrinsic information, iteration schedule, posterior decision, CRC early stopping, and maximum iteration limit. Include Mermaid flow. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T6.7_Turbo_iteration_extrinsic_stopping.md` |
| `验收` | Learner can trace one Turbo iteration and identify where CRC early stopping can be applied. |
| `3GPP/证据` | Algorithm implementation task; CRC anchors TS 36.212 Rel-19 `36212-j30` §5.1.1/§5.1.2. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T6.8 LTE Turbo Decoder Numeric Walkthrough

| Item | Requirement |
|:---|:---|
| `编号` | T6.8 |
| `前置` | T6.6, T6.7 |
| `Prompt` | Provide a small toy Turbo-like numeric walkthrough using shortened states, not a full LTE block, to show branch metric, extrinsic update, interleaver exchange, and hard decision. Mark clearly where the example is pedagogical rather than a normative LTE vector. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T6.8_LTE_Turbo_decoder_numeric_walkthrough.md` |
| `验收` | Learner can follow one toy iteration and explain each number's meaning. |
| `3GPP/证据` | Algorithm teaching example; LTE structure referenced from TS 36.212 Rel-19 `36212-j30` §5.1.3.2. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

#### M7 LTE Receive-Side Decoding Chain

##### T7.1 LTE Turbo De-Rate Matching Overview

| Item | Requirement |
|:---|:---|
| `编号` | T7.1 |
| `前置` | T6.1, T4.3 |
| `Prompt` | Explain LTE receive-side inverse of Turbo rate matching: circular buffer, redundancy version, bit collection inversion, sub-block deinterleaving, and soft-buffer update. Include receiver-oriented pseudocode. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T7.1_LTE_Turbo_de_rate_matching_overview.md` |
| `验收` | Learner can explain how received LLRs are placed back into the three Turbo streams. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.4.1, §5.1.4.1.1, Figure 5.1.4-1, Table 5.1.4-1; local table/figure artifacts must be checked. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T7.2 LTE Sub-Block Deinterleaver and Circular Buffer

| Item | Requirement |
|:---|:---|
| `编号` | T7.2 |
| `前置` | T7.1 |
| `Prompt` | Teach LTE sub-block interleaver inverse, inter-column permutation, null/filler handling, and circular buffer indexing. Include an artificial small matrix example and a failure case with wrong column permutation. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T7.2_LTE_subblock_deinterleaver_circular_buffer.md` |
| `验收` | Learner can invert a toy sub-block interleaver and identify null-bit positions. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.4.1.1, Table 5.1.4-1; local table artifact must be checked before reproduction. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T7.3 LTE HARQ Soft Buffer and Redundancy Version

| Item | Requirement |
|:---|:---|
| `编号` | T7.3 |
| `前置` | T4.3, T7.1 |
| `Prompt` | Explain LTE HARQ soft buffer size, redundancy version, incremental redundancy, and how retransmission LLRs update the buffer. Include one small circular-buffer combining example and discuss saturation. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T7.3_LTE_HARQ_soft_buffer_RV.md` |
| `验收` | Learner can describe how RV changes the selected circular-buffer region and how combining affects LLR reliability. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.4.1 soft buffer/rate matching; TS 36.213 HARQ/RV anchors `待核验`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 36.213 -> `3GPP_Rel19/processed/TS_36.213_*` (exact part `待核验`). |

##### T7.4 LTE Code Block Reassembly and TB CRC

| Item | Requirement |
|:---|:---|
| `编号` | T7.4 |
| `前置` | T3.3, T6.7 |
| `Prompt` | Explain receiver code block CRC checks, removal of filler and CB CRC, code block concatenation, transport block CRC, and final ACK/NACK decision. Include failure cases: one CB fails, TB CRC fails after all CB pass, and filler handling error. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T7.4_LTE_code_block_reassembly_TB_CRC.md` |
| `验收` | Learner can describe final LTE TB pass/fail logic from decoded code blocks. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.1, §5.1.2, §5.2.2, §5.3.2; local path listed below. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T7.5 LTE Downlink vs Uplink Decoding Differences

| Item | Requirement |
|:---|:---|
| `编号` | T7.5 |
| `前置` | T7.4 |
| `Prompt` | Compare LTE DL-SCH and UL-SCH decoding from the receiver perspective: channel path, HARQ timing/config context, code block handling, and where TS 36.213/36.321 boundaries matter. Keep focus on decoder input/control, not scheduler design. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T7.5_LTE_DL_UL_decoding_differences.md` |
| `验收` | Learner can explain which parameters a decoder needs from MAC/PHY control for LTE DL and UL. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.2.2/§5.3.2; TS 36.213 exact anchors `待核验`; TS 36.321 Rel-19 `36321-j20` HARQ boundary `待核验`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 36.213 -> `3GPP_Rel19/processed/TS_36.213_*` (exact part `待核验`); TS 36.321 -> `3GPP_Rel19/processed/TS_36.321_36321-j20`. |

##### T7.6 LTE Turbo Decoder Edge Cases

| Item | Requirement |
|:---|:---|
| `编号` | T7.6 |
| `前置` | T7.1-T7.5 |
| `Prompt` | Catalog LTE Turbo decoder edge cases: small blocks, filler bits, maximum code blocks, soft buffer limit, RV sequence mismatch, LLR sign mismatch, CRC false pass risk, and timeout. Provide diagnosis steps. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T7.6_LTE_Turbo_decoder_edge_cases.md` |
| `验收` | Learner can use a checklist to debug a failing LTE Turbo decode. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.1-§5.1.4.1; TS 36.213/36.321 anchors `待核验`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 36.213 -> `3GPP_Rel19/processed/TS_36.213_*` (exact part `待核验`). |

#### M8 NR LDPC Decoding Protocol and Algorithms

##### T8.1 NR LDPC Decoder Chain Overview

| Item | Requirement |
|:---|:---|
| `编号` | T8.1 |
| `前置` | T3.4, T4.1 |
| `Prompt` | Present the NR LDPC receive-side chain from demapper LLRs through rate recovery, LDPC decoding, CB CRC, code block concatenation, TB CRC, and optional CBG handling. Include both UL-SCH and DL-SCH anchors. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T8.1_NR_LDPC_decoder_chain_overview.md` |
| `验收` | Learner can draw NR LDPC decoding chain and map each step to a TS 38.212 clause. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.2.2, §5.3.2, §5.4.2, §6.2.1-§6.2.6, §7.2.1-§7.2.6; TS 38.214 Rel-19 `38214-j30` §5.1.7/§6.1.5. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`. |

##### T8.2 NR LDPC Base Graph Selection

| Item | Requirement |
|:---|:---|
| `编号` | T8.2 |
| `前置` | T3.4 |
| `Prompt` | Explain Base Graph 1 and Base Graph 2, why NR uses two base graphs, and how payload size and code rate guide selection. Include uplink/downlink protocol references and one decision-tree example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T8.2_NR_LDPC_base_graph_selection.md` |
| `验收` | Learner can choose BG1/BG2 for representative A/R conditions and explain the engineering reason. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §6.2.2, §7.2.2; local path listed below. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T8.3 Lifting Size and QC-LDPC Matrix Construction

| Item | Requirement |
|:---|:---|
| `编号` | T8.3 |
| `前置` | T1.3, T8.2 |
| `Prompt` | Explain lifting size, quasi-cyclic LDPC, base matrix, circulant permutation matrix, and parity-check matrix expansion. Include a tiny toy base matrix example and require checking Tables 5.3.2-1/2/3 before reproducing actual NR values. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T8.3_NR_LDPC_lifting_QC_matrix.md` |
| `验收` | Learner can expand a toy QC-LDPC base matrix into a parity-check matrix. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.3.2, Table 5.3.2-1/2/3; local table artifacts must be checked. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T8.4 LDPC Tanner Graph and Message Passing

| Item | Requirement |
|:---|:---|
| `编号` | T8.4 |
| `前置` | T4.2, T8.3 |
| `Prompt` | Teach Tanner graph, variable node, check node, edge messages, syndrome, and iterative message passing. Use a small parity-check matrix and show one iteration with numeric LLR messages. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T8.4_LDPC_Tanner_graph_message_passing.md` |
| `验收` | Learner can map a parity-check matrix to a Tanner graph and describe VN/CN messages. |
| `3GPP/证据` | Algorithm background linked to TS 38.212 Rel-19 `38212-j30` §5.3.2 base graph tables. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T8.5 Sum-Product Belief Propagation for LDPC

| Item | Requirement |
|:---|:---|
| `编号` | T8.5 |
| `前置` | T8.4, T1.5 |
| `Prompt` | Derive LDPC belief propagation in LLR domain, including variable-node update, check-node update, posterior LLR, and syndrome check. Explain tanh/atanh intuitively and numerically. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T8.5_LDPC_sum_product_BP.md` |
| `验收` | Learner can write BP update equations and explain why check-node update is nonlinear. |
| `3GPP/证据` | Algorithm implementation task; NR LDPC structure from TS 38.212 Rel-19 `38212-j30` §5.3.2. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T8.6 Min-Sum, Normalized Min-Sum, and Offset Min-Sum

| Item | Requirement |
|:---|:---|
| `编号` | T8.6 |
| `前置` | T8.5 |
| `Prompt` | Explain Min-Sum approximation, sign product, minimum and second minimum trick, Normalized Min-Sum, Offset Min-Sum, and performance/complexity tradeoff. Include numeric examples and hardware-friendly reasoning. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T8.6_LDPC_MS_NMS_OMS.md` |
| `验收` | Learner can compute one check-node Min-Sum update and explain normalization/offset effects. |
| `3GPP/证据` | Algorithm implementation task; not a normative 3GPP decoder algorithm. |

##### T8.7 Layered LDPC Decoding Schedule

| Item | Requirement |
|:---|:---|
| `编号` | T8.7 |
| `前置` | T8.6 |
| `Prompt` | Explain flooding vs layered LDPC decoding, why layered schedule converges faster, how QC rows map to layers, and how message memory changes. Include a small layer update example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T8.7_layered_LDPC_decoding_schedule.md` |
| `验收` | Learner can distinguish flooding and layered schedules and state hardware tradeoffs. |
| `3GPP/证据` | Algorithm implementation task linked to TS 38.212 Rel-19 `38212-j30` §5.3.2 QC structure. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T8.8 NR LDPC Decoder Numeric Walkthrough

| Item | Requirement |
|:---|:---|
| `编号` | T8.8 |
| `前置` | T8.4-T8.7 |
| `Prompt` | Provide a toy LDPC numeric walkthrough: channel LLRs, parity-check matrix, CN update, VN update, hard decision, syndrome, and early stop. Mark the example as pedagogical and not an NR production matrix. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T8.8_NR_LDPC_decoder_numeric_walkthrough.md` |
| `验收` | Learner can complete one toy Min-Sum iteration and check syndrome. |
| `3GPP/证据` | Algorithm teaching example; NR matrix structure referenced from TS 38.212 Rel-19 `38212-j30` §5.3.2. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

#### M9 NR LDPC Receive-Side Decoding Chain

##### T9.1 NR LDPC Rate Recovery Overview

| Item | Requirement |
|:---|:---|
| `编号` | T9.1 |
| `前置` | T8.1, T4.3 |
| `Prompt` | Explain NR LDPC receive-side inverse of rate matching: bit selection inverse, circular buffer, redundancy version, bit interleaving inverse, limited buffer rate matching, and soft buffer update. Include pseudocode. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T9.1_NR_LDPC_rate_recovery_overview.md` |
| `验收` | Learner can explain where received LLRs are inserted in the LDPC soft buffer. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.4.2, §5.4.2.2, §6.2.5, §7.2.5; TS 38.214 Rel-19 `38214-j30` §5.1.3/§6.1.4. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`. |

##### T9.2 NR LDPC Bit Interleaving and Deinterleaving

| Item | Requirement |
|:---|:---|
| `编号` | T9.2 |
| `前置` | T9.1, T2.3 |
| `Prompt` | Explain NR LDPC bit interleaving by modulation order and its receiver inverse. Show how Qm affects bit order, LLR grouping, and deinterleaver addresses. Include a small Qm=4 example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T9.2_NR_LDPC_bit_deinterleaving.md` |
| `验收` | Learner can invert a toy LDPC bit interleaver for Qm=2 or Qm=4. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.4.2.2; local path listed below. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T9.3 NR LDPC HARQ Soft Buffer and RV k0

| Item | Requirement |
|:---|:---|
| `编号` | T9.3 |
| `前置` | T4.3, T9.1 |
| `Prompt` | Explain NR LDPC redundancy version, k0, circular buffer start, HARQ soft combining, limited buffer behavior, and retransmission handling. Include one toy k0-based placement example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0.md` |
| `验收` | Learner can explain how RV changes the selected code-bit region and why soft buffer consistency matters. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.4.2; TS 38.214 Rel-19 `38214-j30` §5.1.3/§6.1.4; exact k0 table references must be checked before reproduction. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`. |

##### T9.4 NR Code Block Group Handling

| Item | Requirement |
|:---|:---|
| `编号` | T9.4 |
| `前置` | T8.1, T9.3 |
| `Prompt` | Explain code block group (CBG) concepts, CBG-based retransmission, receive-side masking, and how CBG changes HARQ buffer and CRC decision handling. Keep scheduler details out except where needed for decoder control. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T9.4_NR_code_block_group_handling.md` |
| `验收` | Learner can explain why a subset of code blocks may be retransmitted and how decoder control tracks it. |
| `3GPP/证据` | TS 38.214 Rel-19 `38214-j30` §5.1.7, §6.1.5; TS 38.212 Rel-19 `38212-j30` §5.4.2 CBG-related rate matching text; local paths listed below. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`. |

##### T9.5 NR LDPC Code Block Reassembly and TB CRC

| Item | Requirement |
|:---|:---|
| `编号` | T9.5 |
| `前置` | T3.4, T8.8, T9.1 |
| `Prompt` | Explain NR LDPC decoded code block handling: filler removal, CB CRC, code block concatenation, TB CRC, and pass/fail reporting. Include CB failure, CBG partial retransmission, and TB CRC failure cases. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T9.5_NR_LDPC_reassembly_TB_CRC.md` |
| `验收` | Learner can define final NR LDPC TB pass/fail logic and CBG interaction. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.1, §5.2.2, §6.2.1-§6.2.6, §7.2.1-§7.2.6. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T9.6 NR LDPC Decoder Edge Cases

| Item | Requirement |
|:---|:---|
| `编号` | T9.6 |
| `前置` | T9.1-T9.5 |
| `Prompt` | Catalog NR LDPC decoder edge cases: BG selection boundary, lifting size boundary, filler bits, punctured systematic bits, limited buffer, RV mismatch, CBG retransmission mismatch, LLR saturation, and syndrome vs CRC disagreement. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T9.6_NR_LDPC_decoder_edge_cases.md` |
| `验收` | Learner can debug a failing NR LDPC decode using a structured checklist. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.2.2/§5.3.2/§5.4.2; TS 38.214 Rel-19 `38214-j30` §5.1.7/§6.1.5. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`. |

#### M10 NR Polar Decoding Protocol and Algorithms

##### T10.1 NR Polar Decoder Chain Overview

| Item | Requirement |
|:---|:---|
| `编号` | T10.1 |
| `前置` | T3.5, T4.2 |
| `Prompt` | Present NR Polar receive-side chain for control information: demapper LLRs, rate recovery, sub-block deinterleaving, Polar decoding, CRC-aided path selection, and output control bits. Cover UCI and DCI at roadmap level. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T10.1_NR_Polar_decoder_chain_overview.md` |
| `验收` | Learner can draw NR Polar decoding chain and name UCI/DCI contexts. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.2.1, §5.3.1, §5.4.1, §6.3, §7.3; TS 38.213 context anchors `待核验`. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T10.2 Channel Polarization and Frozen Bits

| Item | Requirement |
|:---|:---|
| `编号` | T10.2 |
| `前置` | T1.6 |
| `Prompt` | Explain channel polarization, reliable and unreliable bit channels, frozen bits, information bits, and why Polar codes are suitable for short control blocks. Use a small N=4 or N=8 example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T10.2_channel_polarization_frozen_bits.md` |
| `验收` | Learner can identify frozen and information bit positions in a toy Polar code. |
| `3GPP/证据` | Algorithm background; TS 38.212 Rel-19 `38212-j30` §5.3.1/§5.3.1.2 and Table 5.3.1.2-1 for NR construction. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T10.3 NR Polar Reliability Sequence

| Item | Requirement |
|:---|:---|
| `编号` | T10.3 |
| `前置` | T10.2 |
| `Prompt` | Explain the NR Polar reliability sequence, how information indices are selected, and why implementation uses a table. Require checking Table 5.3.1.2-1 before reproducing any values. Include a toy reliability-order example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T10.3_NR_Polar_reliability_sequence.md` |
| `验收` | Learner can explain how reliability ordering determines frozen bit positions. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.3.1.2, Table 5.3.1.2-1; local table artifact must be checked. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T10.4 Successive Cancellation Decoding

| Item | Requirement |
|:---|:---|
| `编号` | T10.4 |
| `前置` | T10.2 |
| `Prompt` | Derive successive cancellation (SC) decoding with f and g LLR functions, partial sums, frozen-bit decisions, and tree traversal. Include a small N=4 numeric example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T10.4_Polar_SC_decoding.md` |
| `验收` | Learner can trace SC decoding decisions through a toy Polar tree. |
| `3GPP/证据` | Algorithm implementation task; NR construction references TS 38.212 Rel-19 `38212-j30` §5.3.1. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T10.5 Successive Cancellation List Decoding

| Item | Requirement |
|:---|:---|
| `编号` | T10.5 |
| `前置` | T10.4 |
| `Prompt` | Explain successive cancellation list (SCL) decoding, path branching, path metric, pruning, list size, and complexity. Include a toy path metric example and hardware implications of sorting. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T10.5_Polar_SCL_decoding.md` |
| `验收` | Learner can explain how list decoding keeps multiple candidate paths and prunes them. |
| `3GPP/证据` | Algorithm implementation task; NR Polar use in TS 38.212 Rel-19 `38212-j30` §5.3.1. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T10.6 CRC-Aided SCL and Control-Channel Reliability

| Item | Requirement |
|:---|:---|
| `编号` | T10.6 |
| `前置` | T3.5, T10.5 |
| `Prompt` | Explain CRC-aided SCL decoding: CRC bits as path-selection aid, false pass risk, list-size tradeoff, and why control channels need low latency and high reliability. Include failure case where best metric path fails CRC. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T10.6_CRC_aided_SCL_control_reliability.md` |
| `验收` | Learner can explain how CRC selects among SCL candidate paths. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.1, §5.2.1, §6.3.1.2.1, §6.3.2.2.1, §7.3.2. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T10.7 NR Polar Rate Recovery

| Item | Requirement |
|:---|:---|
| `编号` | T10.7 |
| `前置` | T10.1 |
| `Prompt` | Explain receive-side inverse of Polar rate matching: sub-block deinterleaving, bit collection, puncturing/shortening/repetition intuition, and bit interleaving when configured. Include one small circular-buffer example. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T10.7_NR_Polar_rate_recovery.md` |
| `验收` | Learner can explain how received control-channel LLRs are mapped back to Polar codeword positions. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.4.1, §5.4.1.1, Table 5.4.1.1-1; UCI rate matching §6.3.1.4.1/§6.3.2.4.1; local artifacts must be checked before reproduction. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T10.8 NR Polar Decoder Edge Cases

| Item | Requirement |
|:---|:---|
| `编号` | T10.8 |
| `前置` | T10.3-T10.7 |
| `Prompt` | Catalog NR Polar decoder edge cases: small payload without CRC, CRC length choices, list-size exhaustion, path metric tie, puncturing/shortening mismatch, frozen-bit mask error, and DCI/UCI context mismatch. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T10.8_NR_Polar_decoder_edge_cases.md` |
| `验收` | Learner can debug a failing NR Polar decode with a checklist. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.2.1/§5.3.1/§5.4.1/§6.3/§7.3; exact context anchors verified before final article. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

#### M11 LTE/NR Decoding Comparison

##### T11.1 Turbo vs LDPC vs Polar Algorithm Comparison

| Item | Requirement |
|:---|:---|
| `编号` | T11.1 |
| `前置` | T6.7, T8.7, T10.6 |
| `Prompt` | Compare Turbo, LDPC, and Polar decoding algorithms by graph model, iteration/list behavior, complexity, memory, latency, and suitability for data/control channels. Use Chinese-first terminology and a concise comparison table. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T11.1_Turbo_LDPC_Polar_algorithm_comparison.md` |
| `验收` | Learner can explain why LTE data used Turbo, NR data uses LDPC, and NR control uses Polar. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` Turbo usage; TS 38.212 Rel-19 `38212-j30` LDPC/Polar usage Table 5.3-1/5.3-2; local table artifacts must be checked before reproduction. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T11.2 LTE vs NR Rate Matching Comparison

| Item | Requirement |
|:---|:---|
| `编号` | T11.2 |
| `前置` | T7.1, T9.1, T10.7 |
| `Prompt` | Compare LTE Turbo rate matching, NR LDPC rate matching, and NR Polar rate matching from receiver perspective. Focus on circular buffers, interleaving, RV, and inverse mapping. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T11.2_LTE_NR_rate_matching_comparison.md` |
| `验收` | Learner can state key differences in de-rate matching for Turbo, LDPC, and Polar. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.4.1; TS 38.212 Rel-19 `38212-j30` §5.4.1/§5.4.2; local paths listed below. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T11.3 HARQ and Soft Buffer Comparison

| Item | Requirement |
|:---|:---|
| `编号` | T11.3 |
| `前置` | T7.3, T9.3 |
| `Prompt` | Compare LTE and NR HARQ soft-buffer handling, RV meaning, CBG support, and decoder control implications. Keep scheduler details outside scope except when they affect decoder state. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T11.3_HARQ_soft_buffer_comparison.md` |
| `验收` | Learner can explain how NR CBG changes retransmission granularity compared with LTE TB/CB flow. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.4.1; TS 36.213 anchors `待核验`; TS 38.212 Rel-19 `38212-j30` §5.4.2; TS 38.214 Rel-19 `38214-j30` §5.1.7/§6.1.5. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`; TS 36.213 -> `3GPP_Rel19/processed/TS_36.213_*` (exact part `待核验`). |

##### T11.4 Decoder Hardware Tradeoff Comparison

| Item | Requirement |
|:---|:---|
| `编号` | T11.4 |
| `前置` | T5.3, T6.7, T8.7, T10.5 |
| `Prompt` | Compare Turbo, LDPC, and Polar hardware architecture tradeoffs: parallelism, memory access, sorting, iteration/list depth, latency, throughput, and power. Include an engineering decision matrix. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T11.4_decoder_hardware_tradeoff_comparison.md` |
| `验收` | Learner can justify why LDPC is high-throughput friendly and why Polar SCL sorting is latency-sensitive. |
| `3GPP/证据` | Engineering comparison; protocol usage evidence from TS 36.212 Rel-19 `36212-j30` / TS 38.212 Rel-19 `38212-j30`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T11.5 Decoder Selection by Channel Type

| Item | Requirement |
|:---|:---|
| `编号` | T11.5 |
| `前置` | T11.1 |
| `Prompt` | Map LTE/NR channel and information types to decoder families: LTE transport channels, NR UL-SCH/DL-SCH, NR UCI/DCI, and boundary cases. Include a quick-reference table. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L2/T11.5_decoder_selection_by_channel_type.md` |
| `验收` | Learner can choose Turbo, LDPC, or Polar decoder for each covered LTE/NR decoding task. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` channel coding usage; TS 38.212 Rel-19 `38212-j30` Table 5.3-1 and Table 5.3-2; local artifacts must be checked before reproducing table values. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

### L3 Engineering Stage

#### M12 Floating-Point Simulation

##### T12.1 Python Golden Model Project Layout

| Item | Requirement |
|:---|:---|
| `编号` | T12.1 |
| `前置` | T4.6, T5.5 |
| `Prompt` | Specify a Python golden-model project layout for LTE Turbo, NR LDPC, and NR Polar decoders. Include package structure, config files, vector files, random seeds, logging, and reproducible command examples. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T12.1_python_golden_model_project_layout.md` |
| `验收` | Learner can scaffold a reproducible decoder simulation project. |
| `3GPP/证据` | Engineering task; protocol vector generation later cites TS 36.212 Rel-19 `36212-j30` / TS 38.212 Rel-19 `38212-j30`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T12.2 LTE Turbo Floating-Point Simulation Plan

| Item | Requirement |
|:---|:---|
| `编号` | T12.2 |
| `前置` | T6.7, T7.4, T12.1 |
| `Prompt` | Define the LTE Turbo floating-point simulation plan: encoder reference, AWGN channel, de-rate matching, Log-MAP/Max-Log-MAP decoder, CRC checks, BLER curve, seed, outputs, and thresholds. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T12.2_LTE_Turbo_float_sim_plan.md` |
| `验收` | Learner can run or implement a plan that produces LTE Turbo BLER curves and decoder traces. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.1-§5.1.4.1; TS 36.213 MCS/TBS anchors `待核验`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 36.213 -> `3GPP_Rel19/processed/TS_36.213_*` (exact part `待核验`). |

##### T12.3 NR LDPC Floating-Point Simulation Plan

| Item | Requirement |
|:---|:---|
| `编号` | T12.3 |
| `前置` | T8.8, T9.5, T12.1 |
| `Prompt` | Define the NR LDPC floating-point simulation plan: base graph selection, lifting, rate matching/recovery, Min-Sum variants, CRC checks, BLER curves, seeds, outputs, and thresholds. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T12.3_NR_LDPC_float_sim_plan.md` |
| `验收` | Learner can specify a reproducible NR LDPC BLER simulation and compare BP/MS/NMS/OMS. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.2.2/§5.3.2/§5.4.2/§6.2/§7.2; TS 38.214 Rel-19 `38214-j30` §5.1.3/§6.1.4. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`. |

##### T12.4 NR Polar Floating-Point Simulation Plan

| Item | Requirement |
|:---|:---|
| `编号` | T12.4 |
| `前置` | T10.6, T10.7, T12.1 |
| `Prompt` | Define the NR Polar floating-point simulation plan: reliability sequence, rate recovery, SC/SCL/CA-SCL decoder, list size sweep, CRC checks, latency proxy metrics, seeds, outputs, and thresholds. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T12.4_NR_Polar_float_sim_plan.md` |
| `验收` | Learner can specify a reproducible CA-SCL performance experiment with list-size comparison. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.2.1/§5.3.1/§5.4.1/§6.3/§7.3. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T12.5 BER/BLER Curve Generation and Reporting

| Item | Requirement |
|:---|:---|
| `编号` | T12.5 |
| `前置` | T12.2, T12.3, T12.4 |
| `Prompt` | Teach how to generate, store, plot, and interpret BER/BLER curves. Include confidence limits, minimum frame count, early stopping criteria for simulations, CSV/PNG output naming, and failure diagnostics. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T12.5_BER_BLER_curve_reporting.md` |
| `验收` | Learner can produce a report-ready BLER curve with reproducible seeds and metadata. |
| `3GPP/证据` | Engineering task; transport block CRC anchors from TS 36.212 Rel-19 `36212-j30` / TS 38.212 Rel-19 `38212-j30`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

#### M13 Fixed-Point C/C++ Models

##### T13.1 Fixed-Point Decoder Requirements

| Item | Requirement |
|:---|:---|
| `编号` | T13.1 |
| `前置` | T5.1, T12.1 |
| `Prompt` | Define fixed-point decoder requirements: LLR width, internal message width, saturation rules, rounding, scaling, performance loss budget, and bit-exact comparison policy. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T13.1_fixed_point_decoder_requirements.md` |
| `验收` | Learner can write fixed-point requirements for one decoder block and identify comparison tolerances. |
| `3GPP/证据` | No direct 3GPP citation required for fixed-point methodology. Any protocol-specific fixed-point requirement must cite upstream Rel-19 evidence from T7, T9, T10, and related simulation/vector tasks. |

##### T13.2 LTE Turbo Fixed-Point Model Plan

| Item | Requirement |
|:---|:---|
| `编号` | T13.2 |
| `前置` | T6.6, T7.3, T13.1 |
| `Prompt` | Plan a C/C++ fixed-point LTE Turbo decoder model: branch metrics, alpha/beta metrics, extrinsic scaling, interleaver addresses, saturation, max-log correction option, and bit-exact tests against Python. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T13.2_LTE_Turbo_fixed_point_model_plan.md` |
| `验收` | Learner can specify C/C++ structures and tests for a fixed-point Turbo decoder. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.3.2/§5.1.4.1; algorithm implementation evidence. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T13.3 NR LDPC Fixed-Point Model Plan

| Item | Requirement |
|:---|:---|
| `编号` | T13.3 |
| `前置` | T8.6, T9.3, T13.1 |
| `Prompt` | Plan a C/C++ fixed-point NR LDPC decoder model: LLR/message widths, min/second-min storage, normalization/offset, layered schedule, saturation, syndrome checks, and bit-exact tests. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T13.3_NR_LDPC_fixed_point_model_plan.md` |
| `验收` | Learner can define fixed-point NMS/OMS experiments and compare BLER loss to floating point. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.3.2/§5.4.2; algorithm implementation evidence. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T13.4 NR Polar Fixed-Point Model Plan

| Item | Requirement |
|:---|:---|
| `编号` | T13.4 |
| `前置` | T10.5, T10.6, T13.1 |
| `Prompt` | Plan a C/C++ fixed-point NR Polar decoder model: f/g functions, path metric width, partial sums, list pruning, sorter effects, CRC-aided selection, and bit-exact tests. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T13.4_NR_Polar_fixed_point_model_plan.md` |
| `验收` | Learner can specify fixed-point CA-SCL data structures and path metric saturation checks. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.3.1/§5.4.1; algorithm implementation evidence. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T13.5 SIMD and Memory Layout for C/C++ Decoders

| Item | Requirement |
|:---|:---|
| `编号` | T13.5 |
| `前置` | T13.2, T13.3, T13.4 |
| `Prompt` | Explain C/C++ memory layout, alignment, SIMD-friendly arrays, cache locality, and vectorization opportunities for Turbo, LDPC, and Polar decoders. Include profiling plan and failure case of non-coalesced memory. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T13.5_SIMD_memory_layout_decoders.md` |
| `验收` | Learner can propose an array layout for one decoder and justify cache/SIMD behavior. |
| `3GPP/证据` | No direct 3GPP citation required for this engineering method. The article must cite upstream protocol-vector tasks when it uses generated LTE/NR vectors. |

##### T13.6 Bit-Exact Regression Harness

| Item | Requirement |
|:---|:---|
| `编号` | T13.6 |
| `前置` | T13.2, T13.3, T13.4 |
| `Prompt` | Design a bit-exact regression harness comparing Python floating/fixed reference, C/C++ fixed model, and later RTL outputs. Include vector format, metadata, seed tracking, tolerances, pass/fail policy, and CI command. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T13.6_bit_exact_regression_harness.md` |
| `验收` | Learner can define a regression vector format and pass/fail policy for all three decoders. |
| `3GPP/证据` | Engineering task; protocol vectors link to TS 36.212 Rel-19 `36212-j30` / TS 38.212 Rel-19 `38212-j30`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

#### M14 RTL/ASIC Decoder Architecture

##### T14.1 LTE Turbo RTL Microarchitecture

| Item | Requirement |
|:---|:---|
| `编号` | T14.1 |
| `前置` | T5.2, T5.4, T13.2 |
| `Prompt` | Design an LTE Turbo RTL microarchitecture: SISO datapath, alpha/beta memory, extrinsic memory, interleaver/deinterleaver address generator, ping-pong iteration control, CRC early stop, clock/reset strategy, and throughput estimate. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T14.1_LTE_Turbo_RTL_microarchitecture.md` |
| `验收` | Learner can draw the Turbo decoder block diagram and FSM and estimate memory size. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.3.2/§5.1.4.1; RTL design is implementation guidance. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`. |

##### T14.2 NR LDPC RTL Microarchitecture

| Item | Requirement |
|:---|:---|
| `编号` | T14.2 |
| `前置` | T5.2, T5.4, T13.3 |
| `Prompt` | Design an NR LDPC RTL microarchitecture: layered schedule controller, check-node units, variable-node update, min/second-min datapath, message memory, LLR memory, bank conflict handling, syndrome/CRC early stop, and throughput estimate. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T14.2_NR_LDPC_RTL_microarchitecture.md` |
| `验收` | Learner can draw a layered LDPC decoder architecture and identify memory banking constraints. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.3.2 table-driven QC structure; RTL design is implementation guidance. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T14.3 NR Polar RTL Microarchitecture

| Item | Requirement |
|:---|:---|
| `编号` | T14.3 |
| `前置` | T5.2, T5.4, T13.4 |
| `Prompt` | Design an NR Polar RTL microarchitecture: SC/SCL tree traversal, LLR memory, partial-sum memory, path memory, path metric update, sorter/pruner, CRC checker, and low-latency control. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T14.3_NR_Polar_RTL_microarchitecture.md` |
| `验收` | Learner can draw a CA-SCL decoder architecture and explain sorter bottleneck. |
| `3GPP/证据` | TS 38.212 Rel-19 `38212-j30` §5.3.1/§5.4.1; RTL design is implementation guidance. Local evidence path(s): TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T14.4 Unified Decoder Subsystem Architecture

| Item | Requirement |
|:---|:---|
| `编号` | T14.4 |
| `前置` | T14.1, T14.2, T14.3 |
| `Prompt` | Design a unified decoder subsystem containing Turbo, LDPC, and Polar engines, shared input/output DMA, soft buffer, configuration registers, interrupt/status, and error handling. Define clean boundaries so each engine remains independently testable. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T14.4_unified_decoder_subsystem_architecture.md` |
| `验收` | Learner can define top-level registers and dataflow for a multi-decoder accelerator. |
| `3GPP/证据` | Context evidence only, not a source for specific register-field claims until verified: LTE configuration inputs from TS 36.213 Rel-19 `36213-j30_*`, TS 36.321 Rel-19 `36321-j20`, TS 36.331 Rel-19 `36331-j21`; NR configuration inputs from TS 38.214 Rel-19 `38214-j30`, TS 38.321 Rel-19 `38321-j20`, TS 38.331 Rel-19 `38331-j20`. Local paths: `3GPP_Rel19/processed/TS_36.213_*` (`待核验` exact part), `3GPP_Rel19/processed/TS_36.321_36321-j20`, `3GPP_Rel19/processed/TS_36.331_36331-j21`, `3GPP_Rel19/processed/TS_38.214_38214-j30`, `3GPP_Rel19/processed/TS_38.321_38321-j20`, `3GPP_Rel19/processed/TS_38.331_38331-j20`. |

##### T14.5 Soft Buffer and HARQ Memory Architecture

| Item | Requirement |
|:---|:---|
| `编号` | T14.5 |
| `前置` | T7.3, T9.3, T14.4 |
| `Prompt` | Design soft buffer and HARQ memory architecture: process ID, TB/CB/CBG indexing, RV placement, saturation, memory bank partition, eviction, and recovery after failed CRC. Include LTE and NR differences. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T14.5_soft_buffer_HARQ_memory_architecture.md` |
| `验收` | Learner can propose a soft-buffer address map for LTE Turbo and NR LDPC. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` §5.1.4.1; TS 38.212 Rel-19 `38212-j30` §5.4.2; TS 38.214 Rel-19 `38214-j30` §5.1.7/§6.1.5; TS 36.213 anchors `待核验`. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`; TS 38.214 -> `3GPP_Rel19/processed/TS_38.214_38214-j30`; TS 36.213 -> `3GPP_Rel19/processed/TS_36.213_*` (exact part `待核验`). |

##### T14.6 Decoder Register Map and Configuration Flow

| Item | Requirement |
|:---|:---|
| `编号` | T14.6 |
| `前置` | T4.6, T14.4 |
| `Prompt` | Define a decoder register map and configuration flow: algorithm select, block size, code rate, BG, Zc, RV, Qm, HARQ ID, list size, iteration limit, start/status/error interrupts. Trace which fields come from PHY/MAC/RRC. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T14.6_decoder_register_map_configuration_flow.md` |
| `验收` | Learner can map high-level protocol parameters to hardware registers. |
| `3GPP/证据` | Context evidence only, not a source for specific register-field claims until verified: decoder algorithm parameters from TS 36.212 Rel-19 `36212-j30` and TS 38.212 Rel-19 `38212-j30`; scheduling/HARQ context from TS 36.213 Rel-19 `36213-j30_*` and TS 38.214 Rel-19 `38214-j30`; MAC/RRC configuration context from TS 36.321 Rel-19 `36321-j20`, TS 36.331 Rel-19 `36331-j21`, TS 38.321 Rel-19 `38321-j20`, TS 38.331 Rel-19 `38331-j20`. Exact RRC/MAC fields remain `待核验`. Local paths: `3GPP_Rel19/processed/TS_36.212_36212-j30`, `3GPP_Rel19/processed/TS_38.212_38212-j30`, `3GPP_Rel19/processed/TS_36.213_*` (`待核验` exact part), `3GPP_Rel19/processed/TS_38.214_38214-j30`, `3GPP_Rel19/processed/TS_36.321_36321-j20`, `3GPP_Rel19/processed/TS_36.331_36331-j21`, `3GPP_Rel19/processed/TS_38.321_38321-j20`, `3GPP_Rel19/processed/TS_38.331_38331-j20`. |

#### M15 Synthesis and Verification

##### T15.1 Decoder Testbench Architecture

| Item | Requirement |
|:---|:---|
| `编号` | T15.1 |
| `前置` | T13.6, T14.1-T14.3 |
| `Prompt` | Design a SystemVerilog testbench architecture for Turbo, LDPC, and Polar decoder engines. Include driver, monitor, scoreboard, reference vector loader, assertions, reset tests, and timeout policy. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T15.1_decoder_testbench_architecture.md` |
| `验收` | Learner can write a testbench plan that compares RTL output to golden vectors. |
| `3GPP/证据` | No direct 3GPP citation required for testbench methodology. Generated vectors must cite upstream Rel-19 evidence from T7, T9, T10, and T15.2. |

##### T15.2 Protocol Vector and Corner-Case Suite

| Item | Requirement |
|:---|:---|
| `编号` | T15.2 |
| `前置` | T7.6, T9.6, T10.8, T13.6 |
| `Prompt` | Define protocol vector and corner-case suite for LTE Turbo, NR LDPC, and NR Polar: minimum/maximum sizes, filler, CRC fail, RV mismatch, CBG, list-size stress, LLR saturation, and reset mid-operation. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T15.2_protocol_vector_corner_case_suite.md` |
| `验收` | Learner can list required directed tests for all three decoders and explain what each catches. |
| `3GPP/证据` | TS 36.212 Rel-19 `36212-j30` / TS 38.212 Rel-19 `38212-j30` anchors for sizes/rate matching/CRC; exact corner tables must be verified. Local evidence path(s): TS 36.212 -> `3GPP_Rel19/processed/TS_36.212_36212-j30`; TS 38.212 -> `3GPP_Rel19/processed/TS_38.212_38212-j30`. |

##### T15.3 Coverage and Regression Strategy

| Item | Requirement |
|:---|:---|
| `编号` | T15.3 |
| `前置` | T15.1, T15.2 |
| `Prompt` | Define functional coverage, code coverage, regression tiers, random seeds, nightly runs, failure triage, and sign-off criteria for decoder verification. Include coverage points for algorithm family, block size, RV, Qm, CRC status, and reset. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T15.3_coverage_regression_strategy.md` |
| `验收` | Learner can define coverage bins and regression pass criteria for a decoder subsystem. |
| `3GPP/证据` | No direct 3GPP citation required for coverage methodology. Coverage bins that depend on protocol parameters must reference upstream Rel-19 evidence from T7/T9/T10/T15.2. |

##### T15.4 Synopsys Design Compiler Synthesis Flow

| Item | Requirement |
|:---|:---|
| `编号` | T15.4 |
| `前置` | T14.1-T14.6 |
| `Prompt` | Teach a Synopsys Design Compiler synthesis flow for decoder RTL: file list, clock constraints, reset assumptions, compile strategy, timing report, area report, power estimate, and common decoder critical paths. State tool availability limitations if DC is not installed. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T15.4_DC_synthesis_flow_decoders.md` |
| `验收` | Learner can prepare a DC script skeleton and interpret timing/area reports. |
| `3GPP/证据` | No direct 3GPP citation required for this engineering method. The article must cite upstream protocol-vector tasks when it uses generated LTE/NR vectors. |

##### T15.5 Timing Closure and Critical Path Debug

| Item | Requirement |
|:---|:---|
| `编号` | T15.5 |
| `前置` | T15.4 |
| `Prompt` | Explain timing closure for decoder RTL: critical path identification, LDPC check-node min tree, Polar sorter, Turbo ACS/metric update, pipelining, retiming, register duplication, and area/timing tradeoff. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T15.5_timing_closure_decoder_critical_paths.md` |
| `验收` | Learner can diagnose one plausible timing violation and propose a pipeline or architecture fix. |
| `3GPP/证据` | No direct 3GPP citation required for this engineering method. The article must cite upstream protocol-vector tasks when it uses generated LTE/NR vectors. |

##### T15.6 Final Decoder Verification and Evidence Report

| Item | Requirement |
|:---|:---|
| `编号` | T15.6 |
| `前置` | T15.1-T15.5 |
| `Prompt` | Define the final verification and evidence report format: protocol evidence table, simulation summary, fixed-point loss, RTL regression, coverage, synthesis timing/area/power, known limitations, and sign-off checklist. 写作时必须套用本文“单节工程讲义统一骨架”；若协议、接收流程、仿真、定点或 RTL 部分不适用，必须说明原因并保留验收与证据记录。 |
| `产出` | `docs/L3/T15.6_final_decoder_verification_evidence_report.md` |
| `验收` | Learner can assemble an audit-ready final report for LTE Turbo, NR LDPC, and NR Polar decoder work. |
| `3GPP/证据` | Aggregates exact Rel-19 evidence from all protocol tasks. Final report must list concrete TS package names, sections, table/figure/formula anchors when applicable, and `3GPP_Rel19/processed/...` local paths rather than using aggregate wording. |

## Task Card Format

Each task card should use the table style from the reference roadmap.

Required fields:

| Field | Requirement |
|:---|:---|
| `编号` | Stable task identifier such as `T8.4` |
| `前置` | Earlier task identifiers needed before this task |
| `Prompt` | Detailed task-specific writing instruction plus the short binding sentence that points to `单节工程讲义统一骨架`. The full article skeleton must be written once globally, not repeated in every task card. |
| `产出` | Markdown path under `docs/L1`, `docs/L2`, or `docs/L3` |
| `验收` | Concrete learning, simulation, or implementation acceptance criteria |
| `3GPP/证据` | TS number, Rel-19 package, section, table/figure/formula when applicable, and local path. If an anchor is not verified, mark `待核验`; final publication is blocked until verified. |

Each task prompt must preserve the compliance guide constraints:

- Explain background, theory, formulas, protocol basis, software verification, and hardware mapping when relevant.
- Use at most 2 industrial representative cases.
- For each case, include input, output, boundary condition, verification method, and failure case.
- Use Chinese term first, with English in parentheses on first appearance.
- Do not use skip words such as "obvious", "trivial", or "omitted" as a substitute for derivation.
- Include reproducibility requirements for simulation and code.

## Per-Article Content Plan / 单节工程讲义统一骨架

Each article produced from a task card should follow this default structure unless the task is explicitly a short checklist or index:

| Section | Content Requirement |
|:---|:---|
| 1. Learning goals | State the decoding problem the learner can solve after the article |
| 2. Prerequisite check | List required concepts and 3-5 self-check questions |
| 3. Protocol basis and local paths | Cite TS number, Rel-19 package, section/table/figure/formula, local path |
| 4. Engineering motivation | Explain where the block sits in the receive chain, with inputs and outputs |
| 5. Plain-language intuition | Explain the idea before notation |
| 6. Mathematical definitions and derivation | Define symbols and derive formulas step by step |
| 7. Protocol flow breakdown | Convert 3GPP text into receive-side steps |
| 8. Algorithm pseudocode | Provide implementation-oriented pseudocode with input/output |
| 9. Industrial cases | Include at most 2 cases with input, output, boundary, verification, failure |
| 10. Floating-point simulation | Define Python/MATLAB model, command, seed, outputs, thresholds |
| 11. Fixed-point strategy | Define LLR width, saturation, quantization, table approximations, loss budget |
| 12. RTL/ASIC mapping | Explain datapath, control FSM, buffers, parallelism, timing and reset concerns |
| 13. Verification method | Cover unit tests, protocol vectors, random tests, BER/BLER, bit-exact checks |
| 14. Common mistakes | List likely implementation and interpretation failures |
| 15. Engineering questions | Ask architecture and trade-off questions |
| 16. Protocol evidence table | Summarize all protocol sources used |
| 17. Execution and evidence record | Record local files, scripts, skills, checks, and review result |
| 18. References | Use `[Author, Year]` style with full reference list |

Complex topics should be split into theory, protocol, simulation, fixed-point, RTL, and verification articles rather than forced into a single oversized article.

## Core Topic Treatment

LTE Turbo articles should emphasize:

- TS 36.212 as the main evidence source.
- Recursive systematic convolutional code structure.
- LTE Turbo interleaver.
- MAP, Log-MAP, and Max-Log-MAP derivations.
- Extrinsic information exchange and iterative decoding.
- LTE de-rate matching and HARQ soft combining.
- Code block CRC and transport block CRC.
- Fixed-point LLR scaling, SISO memory, interleaver address generation, and ping-pong architecture.

NR LDPC articles should emphasize:

- TS 38.212 as the main evidence source, with TS 38.214 for MCS, TBS, HARQ, and CBG context.
- Base Graph 1 and Base Graph 2 selection.
- Lifting size and quasi-cyclic parity-check construction.
- Belief propagation, Min-Sum, Normalized Min-Sum, and Offset Min-Sum.
- Receive-side rate recovery, redundancy version, HARQ soft buffer, CBG, CRC, and early termination.
- Layered decoding architecture, check-node and variable-node updates, memory banking, bank conflicts, and throughput estimates.

NR Polar articles should emphasize:

- TS 38.212 as the main evidence source, with TS 38.213 for control channel context.
- Channel polarization, frozen bits, information bits, and reliability sequence.
- Successive Cancellation and Successive Cancellation List decoding.
- CRC-aided SCL path selection.
- Receive-side rate recovery and control-channel latency constraints.
- Tree traversal, path copying/pruning, LLR memory, partial-sum memory, and sorter design.

## Verification Strategy

The roadmap document itself is verified by inspection:

- It must include all three decoder families: LTE Turbo, NR LDPC, NR Polar.
- It must include Rel-19 protocol quick-reference tables.
- It must include a Mermaid overview.
- It must use Markdown tables rather than ASCII pseudo-tables.
- It must include task-card output paths and acceptance criteria.
- It must avoid broad protocol-stack expansion outside the decoding boundary.
- It must include execution and evidence rules.

Follow-on articles generated from the roadmap must use stronger verification:

- Unit tests for algorithms.
- End-to-end floating-point tests with fixed random seeds.
- Bit-exact C/C++ vs Python comparisons.
- RTL simulation against golden vectors.
- BLER/BER regression thresholds.
- Synthesis reports for timing, area, and power where tools are available.

## Known Constraints

The local extraction pipeline preserves equations as raw OMML XML. It does not provide a publication-grade OMML-to-LaTeX conversion capability. If a later task requires verified formula conversion from Word equations, create a dedicated script or skill rather than claiming the capability exists.

The roadmap can cite protocol section targets that are known at the roadmap level, but detailed task articles must verify section/table/formula references against the processed Word artifacts before making final claims.

## Approval Gate

After this design spec is reviewed, implement the roadmap document as a Markdown file in the project root. Do not proceed to generating all downstream lesson articles until the roadmap itself has been reviewed and approved.
