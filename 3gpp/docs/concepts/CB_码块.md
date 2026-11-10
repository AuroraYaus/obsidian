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

CB 是 TB 分段后交给 Turbo、LDPC 或 Polar 相关处理的工作单元。接收端通常逐 CB 做 rate recovery、译码和条件性 CB CRC 检查，再按顺序重组回 TB。一句话本质：**CB 是"厚书拆成的分册"——每册独立校对，但必须按原顺序装回一本书**。

## 独立解释任务

任务目标：解释 CB 为什么是译码核心的最小主要工作单元。

## 起源与演进

(1) **起点：编码器一次吃不下整个 TB。** Turbo、LDPC、Polar 的单块长度都有协议上限，超限必须切——CB 就是切出来的工作单元。

(2) **每块自足：独立 CRC 与独立编码。** 每个 CB 独立附加 CB CRC（LTE Turbo 与 NR LDPC 恒有；NR Polar 无 CB CRC）、独立编码、独立速率匹配——接收端可逐块译码，这是并行处理与逐块早停的根基。

(3) **收尾：条件验收与按序重组。** 接收端逐 CB 做 rate recovery、译码、CB CRC 检查，然后**按 CB 编号**重组回 TB——完成顺序不等于重组顺序。

(4) **与 CBG 的关系。** NR 在 CB 之上再加一层分组（CBG），把部分重传粒度从整 TB 细化到一组 CB——CB 是分组的原料（见 [[CBG_码块组]]）。

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
- 本地锚点示例：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`；`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md`。

## 关键要点

1. CB 是译码核心的最小主要工作单元，由 TB 分段而来。
2. 每个 CB 独立编码/速率匹配——并行译码与逐块早停的根基。
3. CB CRC 是否附加取决于协议场景（LTE Turbo/NR LDPC 有；NR Polar 无）。
4. 重组必须按 CB 编号顺序，不是完成顺序。
5. CB 不能脱离 TB 单独交付。
6. CB 是 CBG 的分组原料（NR 部分重传）。

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
- [[E_Value_G_Value_E值与G值]]
- 关系语义：CB 是译码核心的粒度，承接 TB 分段、速率恢复、译码、CB CRC 和重组。
