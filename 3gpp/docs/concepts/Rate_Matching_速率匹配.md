---
type: definition
aliases:
  - Rate Matching
  - Rate Recovery
  - 速率匹配
  - 解速率匹配
  - de-rate matching
tags:
  - 3gpp
  - concepts
  - rate-matching
source_spec: "TS 36.212 Rel-19 §5.1.4; TS 38.212 Rel-19 §5.4.1 and §5.4.2"
---

# Rate Matching 速率匹配

速率匹配把编码后比特适配到本次可发送资源；接收端的 rate recovery 则把收到的 LLR 放回编码器母码或 circular buffer 坐标。它是 HARQ/RV 和译码核心之间的地址桥。

## 独立解释任务

任务目标：解释速率匹配如何连接无线资源数量、RV 和译码器输入坐标。

## 科学定义

编码器输出的母码长度通常不等于本次无线资源承载的 bit 数。速率匹配通过 puncturing、repetition、shortening、interleaving 和 bit selection 等操作选择实际发送序列。接收端执行 rate recovery，把空口顺序 LLR 恢复到译码器需要的母码位置。

## 直观模型

速率匹配像从一本完整教材里按本次课时挑页打印。RV 告诉你从哪里开始挑，资源数量告诉你挑多少页。接收端拿到打印页后，要按页码放回原书，而不是按收到顺序直接阅读。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| rate recovery 只是补零 | 它是带地址和 mask 的反向映射。 |
| RV 只影响 HARQ | RV 直接影响 rate recovery 地址。 |
| punctured、filler、unknown 都一样 | 三者 LLR 语义不同，必须用 mask 区分。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 §5.1.4 Turbo rate matching。
- NR Polar：TS 38.212 Rel-19 §5.4.1。
- NR LDPC：TS 38.212 Rel-19 §5.4.2。

## 图谱关联

- [[Circular_Buffer_循环缓存]]
- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[RV_冗余版本]]
- [[Soft_Buffer_软缓存]]
- [[LDPC_低密度奇偶校验码]]
- [[Turbo_码]]
- [[Polar_码]]
- [[T7.1_LTE_Turbo_de_rate_matching_overview]]
- [[T9.1_NR_LDPC_rate_recovery_overview]]
- [[T10.7_NR_Polar_rate_recovery]]
- 关系语义：rate matching/recovery 决定 LLR 从空口顺序到译码核心坐标的映射。
