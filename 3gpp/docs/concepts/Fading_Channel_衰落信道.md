---
type: definition
aliases:
  - Fading Channel
  - 衰落信道
  - Rayleigh
  - Channel Estimation
tags:
  - 3gpp
  - concepts
  - channel
  - fading
source_spec: "TS 36.211/38.211 channel models"
---

# 衰落信道

实际无线信道存在多径衰落。瑞利衰落是最常见的 NLOS 模型。与 AWGN 不同，衰落信道的 LLR 可信度随瞬时信道质量波动。

## 核心概念

- **瑞利衰落**：幅度服从瑞利分布，NLOS 默认模型。
- **信道估计误差**：通过 DMRS 估计，误差→LLR 可信度下降。
- **分集**：多个独立路径→降低中断概率。HARQ 是时间分集。

## 图谱关联

- [[AWGN_信道模型]]
- [[LLR_对数似然比]]
- [[HARQ_混合自动重传请求]]
- [[T2.10_fading_channel_LLR_reliability]]
- 关系语义：衰落信道下 LLR 可信度时变，HARQ 通过分集对抗衰落。
