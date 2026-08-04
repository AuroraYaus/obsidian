---
type: definition
aliases:
  - Soft Buffer
  - soft buffer
  - 软缓存
  - HARQ buffer
tags:
  - 3gpp
  - concepts
  - soft-buffer
source_spec: "TS 36.212 Rel-19 §5.1.4.1; TS 38.212 Rel-19 §5.4.2; TS 38.214 Rel-19 HARQ/CBG anchors"
---

# Soft Buffer 软缓存

Soft buffer 保存译码前的软信息，而不是保存硬判决 bit。它让接收端能在 HARQ 重传之间累积同一编码位置的 LLR 证据。

## 独立解释任务

任务目标：解释 soft buffer 为什么保存 LLR 坐标化证据，而不是保存 hard bit。

## 科学定义

soft buffer 是 HARQ 接收端为未完成 TB/CB 保存软信息的缓存。它的地址通常对应 rate matching 或母码坐标，而不是空口 LLR 流的原始顺序。新传输到来时，相同编码位置的 LLR 可以累加，不同位置则补充此前未知的证据。

## 直观模型

soft buffer 像一张证据表。每个格子对应一个编码位置。第一次传输填了一些格子，第二次传输可能填新格子，也可能给旧格子加更多证据。CRC pass 后证据表可释放；CRC fail 时通常继续保留。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| soft buffer 存 hard bit | 它保存软信息和观测状态，不是最终 bit。 |
| 重传直接覆盖旧 LLR | 重复观测通常应累加并饱和。 |
| 一个 CB id 就能定位缓存 | 还需要 HARQ process、TB、codeword、CBG 等上下文。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 §5.1.4.1 Turbo rate matching 和 circular buffer。
- NR：TS 38.212 Rel-19 §5.4.2 LDPC rate matching。
- NR：TS 38.214 Rel-19 §5.1.7/§6.1.5 CBG 和部分重传上下文。

## 图谱关联

- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[HARQ_混合自动重传请求]]
- [[RV_冗余版本]]
- [[CBG_码块组]]
- [[Rate_Matching_速率匹配]]
- [[T4.3_HARQ_soft_combining_basics]]
- [[T19.5_soft_buffer_HARQ_memory_architecture]]
- 关系语义：soft buffer 把跨重传 LLR 证据按 RV、CB、CBG 和 HARQ process 组织起来。
