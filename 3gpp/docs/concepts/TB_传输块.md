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

TB 是物理层信道编码链路最终要交付或拒绝的整体数据对象。接收端通常在所有 CB 译码和重组完成后检查 TB CRC，决定是否把结果交给上层。

## 独立解释任务

任务目标：解释 TB 为什么是交付和 HARQ 成败判断的主对象。

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
- 本地锚点示例：`3GPP_Rel19/processed/TS_36.212_36212-j30/TS_36.212_36212-j30_content.md`；`3GPP_Rel19/processed/TS_38.212_38212-j30/TS_38.212_38212-j30_content.md`。

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
