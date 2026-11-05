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

Soft buffer 保存译码前的软信息，而不是保存硬判决 bit。它让接收端能在 HARQ 重传之间累积同一编码位置的 LLR 证据。一句话本质：**soft buffer 是"证据表"——每个格子对应一个编码位置，重传往旧格子里加证据、往新格子里补证据，CRC 通过才清表**。

## 独立解释任务

任务目标：解释 soft buffer 为什么保存 LLR 坐标化证据，而不是保存 hard bit。

## 起源与演进

(1) **起点：HARQ 合并需要一个"证据仓库"。** 重传的 LLR 必须与旧证据合并，仓库必须按编码坐标组织——不能按空口 LLR 流的原始顺序存，否则每次重传的坐标都对不上。

(2) **为什么存软信息而不是硬判决。** 硬判决 bit 丢掉了可靠度信息：LLR=+0.1 和 LLR=+10 硬判都是 1，但前者几乎不可信。合并时只有软信息能正确加权——这就是"软"字的意义。

(3) **地址语义：坐标化。** 地址对应 rate matching/母码坐标，靠 RV、CB 编号、HARQ process、CBG 上下文共同定位——单一 CB id 不够，上下文缺失会把新旧 TB 混到同一个缓存。

(4) **生命周期：CRC 是开关。** TB CRC pass → 释放缓存；fail → 保留等待重传；NDI 翻转表示新数据 → 覆盖旧缓存。

(5) **工程代价。** 软缓存是译码器最大的内存开销之一——NR 用有限缓存速率匹配（LBRM）限制缓存大小，LTE 全缓存 vs NR 有限缓存的取舍正是 T11.3/T19.5 硬件视角的主题。

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

## 关键要点

1. soft buffer 存 LLR 软信息，不是 hard bit。
2. 地址对应母码坐标，定位需要 RV/CB/HARQ process/CBG 全套上下文。
3. 重复位置累加（饱和加法）、新位置补充——绝不覆盖。
4. 生命周期由 CRC 结果驱动：pass 释放、fail 保留、NDI 翻转覆盖。
5. "软"的意义 = 保留可靠度信息，合并时能正确加权。
6. 它是译码器最大内存开销之一（T11.3/T19.5 硬件视角）。

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
