---
type: definition
aliases:
  - CB
  - Code Block
  - 码块
tags:
  - 3gpp
  - concepts
  - code-block
source_spec: "TS 36.212 Rel-19 §5.1.2; TS 38.212 Rel-19 §5.2"
---

# CB 码块

CB 是 TB 分段后交给 Turbo、LDPC 或 Polar 相关处理的工作单元。接收端通常逐 CB 做 rate recovery、译码和条件性 CB CRC 检查，再按顺序重组回 TB。

## 独立解释任务

任务目标：解释 CB 为什么是译码核心的最小主要工作单元。

## 科学定义

当 TB CRC 后的序列超过编码器或协议允许的单块规模时，协议把它分成多个 CB。每个 CB 按对应编码家族独立编码、速率匹配、传输和译码；如果协议附加了 CB CRC，接收端还要逐 CB 做局部验收。

## 直观模型

CB 是把一本厚书拆成几册交给不同人校对。每册可以独立检查，但交付时必须按原顺序装回一本书，不能按完成先后拼接。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CB 可以脱离 TB 单独交付 | CB 是中间处理对象，最终交付仍回到 TB。 |
| 每个 CB 一定都有 CRC | CB CRC 是否存在取决于协议场景和分段条件。 |
| CB 完成顺序就是重组顺序 | 重组必须按 CB 编号和分段顺序。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 §5.1.2 Code block segmentation and code block CRC attachment。
- NR：TS 38.212 Rel-19 §5.2.1 Polar coding；§5.2.2 Low density parity check coding。
- 本地锚点示例：`3GPP_Rel19/processed/TS_36.212_36212-j30/TS_36.212_36212-j30_content.md`；`3GPP_Rel19/processed/TS_38.212_38212-j30/TS_38.212_38212-j30_content.md`。

## 图谱关联

- [[概念图谱入口]]
- [[TB_传输块]]
- [[CBG_码块组]]
- [[CRC_循环冗余校验]]
- [[Rate_Matching_速率匹配]]
- [[LDPC_低密度奇偶校验码]]
- [[Turbo_码]]
- [[T3.2_transport_code_block_filler_bits]]
- [[T8.1_NR_LDPC_decoder_chain_overview]]
- 关系语义：CB 是译码核心的粒度，承接 TB 分段、速率恢复、译码、CB CRC 和重组。
