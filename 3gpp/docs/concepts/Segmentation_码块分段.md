---
type: algorithm
aliases:
  - Segmentation
  - Code Block Segmentation
  - 码块分段
  - CB segmentation
tags:
  - 3gpp
  - concepts
  - segmentation
source_spec: "TS 36.212 Rel-19 §5.1.2; TS 38.212 Rel-19 §5.2"
---

# Segmentation 码块分段

码块分段把一个 TB 拆成一个或多个 CB，使每个译码核心处理的块长满足协议和编码器约束。分段还会引入 CB CRC、filler bit 和 CB 顺序重组问题。

## 独立解释任务

任务目标：解释 segmentation 如何把 TB 变成可译码的 CB 集合。

## 科学定义

码块分段是信道编码前的结构化切分。发送端先处理 TB CRC，再根据最大码块大小、编码家族和协议表决定 CB 数量、每个 CB 的长度、filler 数量以及是否附加 CB CRC。接收端必须按同一结构反向重组。

## 直观模型

segmentation 像把一段长数据装进多个固定规格的盒子。盒子太大或太小时都不符合协议；为了对齐盒子大小，可能要在第一个盒子前面加入 filler 占位。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| filler 是业务 0 | filler 是占位，不能交付为 TB 数据。 |
| 分段只是数组切片 | 分段还决定 CRC、filler、CB 长度和重组顺序。 |
| 接收端可以自行猜 CB 边界 | CB 边界必须由协议规则和 descriptor 确定。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 §5.1.2 Code block segmentation and code block CRC attachment。
- NR：TS 38.212 Rel-19 §5.2.1 Polar coding；§5.2.2 LDPC coding。

## 图谱关联

- [[概念图谱入口]]
- [[TB_传输块]]
- [[CB_码块]]
- [[CRC_循环冗余校验]]
- [[LDPC_低密度奇偶校验码]]
- [[Turbo_码]]
- [[Polar_码]]
- [[T3.2_transport_code_block_filler_bits]]
- [[T3.3_LTE_Turbo_segmentation_rules]]
- [[T3.4_NR_LDPC_segmentation_rules]]
- 关系语义：segmentation 定义 TB 到 CB 的结构边界，决定后续译码和 CRC 检查粒度。
