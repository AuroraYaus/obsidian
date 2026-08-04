---
type: spec
aliases:
  - 2026-07-27-lte-nr-phy-t2-implementation
tags:
  - 3gpp
  - docs
  - superpowers
  - plan
source_spec: "docs/superpowers/plans/2026-07-27-lte-nr-phy-t2-implementation.md"
---
# T2.x PHY 系统背景讲义实现计划

> **For agentic workers:** 使用 `superpowers:subagent-driven-development` 或 `superpowers:executing-plans` 逐任务实施。步骤使用 checkbox (`- [ ]`) 语法跟踪。

**Goal:** 在 `docs/L1/` 中新增 6 篇 PHY 系统背景讲义（T2.1–T2.6），现有 T2.1–T2.5 后移至 T2.7–T2.11，同步更新全部交叉引用。

**Architecture:** 纯文档操作——文件重命名（git mv）、引用字符串替换、6 篇新讲义按 spec 逐篇撰写。无代码逻辑变更。

**Spec:** `docs/superpowers/specs/2026-07-27-lte-nr-phy-t2-design.md`

## Global Constraints

- 风格：技术手册体，避免教学腔和"学生""本节"等口语化表述
- 协议优先级：与 TS 38.211/36.211 冲突时以协议为准，标注差异
- 参考源：TS 38.211 §4、TS 36.211 §4/§6、参考书（`references/5G移动通信系统设计与标准详解.pdf`）第 4 章
- DOXYGEN 风格注释：每个脚本/函数需 `@brief` `@param` `@return`
- 英文术语首次出现须加中文标注
- LaTeX 公式须可渲染
- 零基础保护：概念需从定义出发，不假定前置通信知识
- audit/superpowers 目录中的历史记录文件不修改

---

## Phase 1: 文件搬迁

### Task 1: 重命名 5 个现有文件

**Files:**
- Rename: `docs/L1/T2.1_AWGN_noise_scaling.md` → `docs/L1/T2.7_AWGN_noise_scaling.md`
- Rename: `docs/L1/T2.2_BPSK_QPSK_soft_demapping.md` → `docs/L1/T2.8_BPSK_QPSK_soft_demapping.md`
- Rename: `docs/L1/T2.3_QAM_Max_Log_MAP_demapping.md` → `docs/L1/T2.9_QAM_Max_Log_MAP_demapping.md`
- Rename: `docs/L1/T2.4_fading_channel_LLR_reliability.md` → `docs/L1/T2.10_fading_channel_LLR_reliability.md`
- Rename: `docs/L1/T2.5_LLR_clipping_scaling_quantization.md` → `docs/L1/T2.11_LLR_clipping_scaling_quantization.md`

- [ ] **Step 1: 批量 git mv**

```bash
cd /home/yys/AGENT/3gpp
git mv docs/L1/T2.1_AWGN_noise_scaling.md docs/L1/T2.7_AWGN_noise_scaling.md
git mv docs/L1/T2.2_BPSK_QPSK_soft_demapping.md docs/L1/T2.8_BPSK_QPSK_soft_demapping.md
git mv docs/L1/T2.3_QAM_Max_Log_MAP_demapping.md docs/L1/T2.9_QAM_Max_Log_MAP_demapping.md
git mv docs/L1/T2.4_fading_channel_LLR_reliability.md docs/L1/T2.10_fading_channel_LLR_reliability.md
git mv docs/L1/T2.5_LLR_clipping_scaling_quantization.md docs/L1/T2.11_LLR_clipping_scaling_quantization.md
```

- [ ] **Step 2: 验证重命名**

```bash
ls docs/L1/T2.[7-9]_*.md docs/L1/T2.1[0-1]_*.md && echo "OK: all 5 files renamed"
ls docs/L1/T2.[1-5]_*.md 2>/dev/null && echo "FAIL: old files still exist" || echo "OK: old files gone"
```

---

### Task 2: 更新各文件内部标题与交叉引用

**Files to modify (16 total):**
- `docs/L1/T2.7_AWGN_noise_scaling.md` — 标题 `T2.1` → `T2.7`
- `docs/L1/T2.8_BPSK_QPSK_soft_demapping.md` — 标题 `T2.2` → `T2.8`，正文内部引用 T2.1→T2.7
- `docs/L1/T2.9_QAM_Max_Log_MAP_demapping.md` — 标题 `T2.3` → `T2.9`，正文内部引用 T2.1→T2.7, T2.2→T2.8, T2.5→T2.11
- `docs/L1/T2.10_fading_channel_LLR_reliability.md` — 标题 `T2.4` → `T2.10`，正文内部引用 T2.1→T2.7, T2.2→T2.8, T2.3→T2.9
- `docs/L1/T2.11_LLR_clipping_scaling_quantization.md` — 标题 `T2.5` → `T2.11`，正文内部引用 T2.1→T2.7, T2.4→T2.10
- `docs/L1/T1.4_probability_bayes_soft_decoding.md` — T2.2→T2.8, T2.3→T2.9
- `docs/L1/T1.5_LLR_soft_decision.md` — T2.2→T2.8, T2.3→T2.9
- `docs/L1/T3.4_NR_LDPC_segmentation_rules.md` — T2.5→T2.11
- `docs/L1/T3.5_NR_Polar_segmentation_crc.md` — T2.5→T2.11
- `docs/L1/T4.5_decoder_performance_metrics.md` — T2.1→T2.7
- `docs/L2/T9.1_NR_LDPC_rate_recovery_overview.md` — T2.5→T2.11
- `docs/L2/T9.2_NR_LDPC_circular_buffer_states.md` — T2.5→T2.11
- `docs/L2/T9.4_NR_LDPC_bit_deinterleaving.md` — T2.2→T2.8, T2.3→T2.9, T2.5→T2.11
- `docs/L2/T10.7_NR_Polar_rate_recovery.md` — T2.5→T2.11
- `docs/L3/T17.2_LTE_Turbo_float_sim_plan.md` — T2.2→T2.8
- `docs/L3/T18.1_fixed_point_decoder_requirements.md` — T2.5→T2.11

- [ ] **Step 1: 更新 5 篇重命名文件自身的标题**

```bash
cd /home/yys/AGENT/3gpp
sed -i '1s/^# T2\.1 /# T2.7 /' docs/L1/T2.7_AWGN_noise_scaling.md
sed -i '1s/^# T2\.2 /# T2.8 /' docs/L1/T2.8_BPSK_QPSK_soft_demapping.md
sed -i '1s/^# T2\.3 /# T2.9 /' docs/L1/T2.9_QAM_Max_Log_MAP_demapping.md
sed -i '1s/^# T2\.4 /# T2.10 /' docs/L1/T2.10_fading_channel_LLR_reliability.md
sed -i '1s/^# T2\.5 /# T2.11 /' docs/L1/T2.11_LLR_clipping_scaling_quantization.md
```

- [ ] **Step 2: 逐文件更新正文内的交叉引用**

对每个文件，使用 Edit 工具精确替换：
- wikilink `[[T2.1_AWGN...]]` → `[[T2.7_AWGN...]]`
- 正文引用 `T2.1`（在非文件名的上下文中）→ `T2.7`
- 同理处理 T2.2→T2.8, T2.3→T2.9, T2.4→T2.10, T2.5→T2.11

**重点注意：** 外部文件中的 wikilink 以旧文件名匹配（如 `[[T2.1_AWGN_noise_scaling]]`），需要替换为目标文件名。

- [ ] **Step 3: 全文扫描验证**

```bash
cd /home/yys/AGENT/3gpp
# 搜索 docs/（排除 audits/superpowers）中的残留旧引用
grep -rn "T2\.1[^0-9]" docs/L1/ docs/L2/ docs/L3/ docs/L0/ --include="*.md" | grep -v "T2\.1[0-1]" && echo "WARNING" || echo "OK"
grep -rn "T2\.[2-5][^0-9]" docs/L1/ docs/L2/ docs/L3/ docs/L0/ --include="*.md" | grep -v "T2\.2[^0-9]\|T2\.3[^0-9]\|T2\.4[^0-9]\|T2\.5[^0-9]" && echo "WARNING" || echo "OK"
```

---

## Phase 2: 新建 6 篇讲义

### Task 3: 创建 T2.1 — OFDM 原理与子载波间隔基础

**Files:**
- Create: `docs/L1/T2.1_OFDM_subcarrier_spacing_basics.md`

**Spec reference:** `docs/superpowers/specs/2026-07-27-lte-nr-phy-t2-design.md` §T2.1

内容按 spec §T2.1 编写，包含：6 个知识要点（特别注意要点 6 的 OFDM 符号 vs 调制符号区分）、协议入口、核心公式表、前置知识、与后续衔接、图示（占位）、证据记录。

- [ ] **Step 1: 撰写正文**
- [ ] **Step 2: 验证** `wc -l docs/L1/T2.1_OFDM_subcarrier_spacing_basics.md`

### Task 4: 创建 T2.2 — NR Numerology 与时域层级

**Files:**
- Create: `docs/L1/T2.2_NR_numerology_time_domain_hierarchy.md`

**Spec reference:** spec §T2.2

- [ ] **Step 1: 撰写正文**
- [ ] **Step 2: 验证**

### Task 5: 创建 T2.3 — NR 频域资源网格

**Files:**
- Create: `docs/L1/T2.3_NR_frequency_resource_grid.md`

**Spec reference:** spec §T2.3

- [ ] **Step 1: 撰写正文**
- [ ] **Step 2: 验证**

### Task 6: 创建 T2.4 — MCS、调制阶数与目标码率

**Files:**
- Create: `docs/L1/T2.4_MCS_modulation_order_target_code_rate.md`

**Spec reference:** spec §T2.4

- [ ] **Step 1: 撰写正文**
- [ ] **Step 2: 验证**

### Task 7: 创建 T2.5 — LTE 帧结构与时频资源

**Files:**
- Create: `docs/L1/T2.5_LTE_frame_structure_time_frequency.md`

**Spec reference:** spec §T2.5

- [ ] **Step 1: 撰写正文**
- [ ] **Step 2: 验证**

### Task 8: 创建 T2.6 — 从资源网格到译码器输入

**Files:**
- Create: `docs/L1/T2.6_from_resource_grid_to_decoder_LLR.md`

**Spec reference:** spec §T2.6

- [ ] **Step 1: 撰写正文**
- [ ] **Step 2: 验证**

---

## Phase 3: 导航更新

### Task 9: 更新 T0.1 阅读地图

**Files:**
- Modify: `docs/L0/T0.1_LTE_NR_decoder_protocol_reading_map.md`

在"资料与协议边界"表中为 TS 36.211/38.211 添加新讲义入口；在"三条学习路径"中将 `T1-T5 基础` 更新为包含 PHY 背景。

---

## Phase 4: 验证与提交

### Task 10: 全项目引用审计

- [ ] 搜索残留旧引用
- [ ] 验证新编号文件名与内部标题一致
- [ ] 验证 T0.1 阅读地图引用完整

### Task 11: Git 提交（3 批）

```bash
# Phase 1: 搬迁 + 引用更新
git add docs/L1/T2.[7-9]_*.md docs/L1/T2.1[0-1]_*.md
git add docs/L1/T1.*.md docs/L1/T3.*.md docs/L1/T4.*.md docs/L2/ docs/L3/
git commit -m "refactor: relocate T2.1-T2.5 to T2.7-T2.11, update all cross-references

Co-Authored-By: Claude <noreply@anthropic.com>"

# Phase 2: 新建 6 篇讲义
git add docs/L1/T2.[1-6]_*.md
git commit -m "docs: add T2.1-T2.6 PHY system background lectures

T2.1 OFDM principles, T2.2 NR numerology, T2.3 resource grid,
T2.4 MCS, T2.5 LTE frame structure, T2.6 grid-to-decoder flow

Co-Authored-By: Claude <noreply@anthropic.com>"

# Phase 3: 导航更新
git add docs/L0/T0.1_LTE_NR_decoder_protocol_reading_map.md
git commit -m "docs: update T0.1 reading map with T2.1-T2.6 entries

Co-Authored-By: Claude <noreply@anthropic.com>"
```
