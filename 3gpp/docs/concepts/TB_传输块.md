---
type: definition
aliases:
  - TB
  - Transport Block
  - 传输块
tags:
  - 3gpp
  - concepts
  - transport-block
source_spec: "TS 36.212 Rel-19 §5.1.2; TS 38.212 Rel-19 §6.2 and §7.2"
---

# TB 传输块

TB 是物理层信道编码链路最终要交付或拒绝的整体数据对象。接收端通常在所有 CB 译码和重组完成后检查 TB CRC，决定是否把结果交给上层。一句话本质：**TB 是"整件快递"——CB 是拆开的包裹，最终要按顺序装回整件，由 TB CRC 验收后才算交付**。

## 独立解释任务

任务目标：解释 TB 为什么是交付和 HARQ 成败判断的主对象。

## 起源与演进

(1) **起点：MAC 与 PHY 之间的"交货单位"。** MAC 把一次调度的数据以 TB 的形式交给物理层，物理层编码链路的全部工作——CRC、分段、编码、速率匹配——都围绕这一个对象展开。

(2) **打包：加 TB CRC 与可能的分段。** 发送端先挂 24 bit TB CRC（NR 大 TB 再挂 16 bit），块长超限时按编码器约束切成 CB——但切开的只是"运输形态"，交付对象仍是整块。

(3) **验收：重组 + TB CRC 才是最终判据。** 接收端把所有 CB 译完、按顺序重组、删 filler，再做一次 TB CRC。所有 CB 通过只是必要条件而非充分条件——拼接、filler、顺序处理任一环节出错都只能由整块复核抓出。

(4) **影响面：一个数字牵动全链路。** TBS 决定 CB 数、译码预算、软缓存大小与 HARQ 行为——TB 是调度器与译码器之间的"总开关"。

## 科学定义

TB 是 MAC/PHY 之间进入信道编码流程的主要数据块。发送端对 TB 附加 TB CRC，再根据块长和编码规则决定是否分段为 CB。接收端最终恢复的也不是单个 CB，而是重组后的 TB 候选。

## 直观模型

TB 是一整件快递，CB 是快递拆开的包裹。每个包裹可以先检查，但最终还要把所有包裹按顺序装回整件快递，再检查整件快递是否完整。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| TB 和 CB 是同一层对象 | TB 是最终交付对象，CB 是编码/译码工作单元。 |
| 所有 CB pass 就一定 TB pass | 拼接顺序、filler 删除和 TB CRC 输入仍可能出错。 |
| TBS 只是数组长度 | TBS 会影响 CB 数量、译码预算、HARQ 和 buffer 需求。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 §5.1.2；§5.2/§5.3 的共享信道处理链路。
- NR：TS 38.212 Rel-19 §6.2 UL-SCH；§7.2 DL-SCH/PCH。
- 本地锚点示例：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`；`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md`。

## 关键要点

1. TB 是 MAC/PHY 之间的主数据块，一次调度至多两个（双码字配置）。
2. CB 是编码/译码工作单元，TB 是交付与 HARQ 成败判断对象——层级不同。
3. 所有 CB pass ≠ TB pass：拼接、filler、顺序错误只有 TB CRC 能抓。
4. TBS 牵动全局：CB 数、译码预算、软缓存、HARQ 行为。
5. 发送链路：TB CRC → 分段 → CB CRC → 编码；接收链路反向。
6. TB CRC 的结果直接驱动 HARQ 的 ACK/NACK。

## 图谱关联

- [[概念图谱入口]]
- [[CB_码块]]
- [[Segmentation_码块分段]]
- [[CRC_循环冗余校验]]
- [[HARQ_混合自动重传请求]]
- [[T3.2_transport_code_block_filler_bits]]
- [[T7.4_LTE_code_block_reassembly_TB_CRC]]
- [[T9.5_NR_LDPC_reassembly_TB_CRC]]
- 关系语义：TB 通过 segmentation 形成 CB，经过 CB 译码和重组后由 TB CRC 决定交付边界。
