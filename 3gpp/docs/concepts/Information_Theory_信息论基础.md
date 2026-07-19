---
type: definition
aliases:
  - Information Theory
  - 信息论
  - Entropy
  - Channel Capacity
  - Shannon Limit
tags:
  - 3gpp
  - concepts
  - math
  - information-theory
source_spec: "Claude Shannon; communication theory"
---

# 信息论基础

信息论为通信系统设立根本性能边界。熵度量不确定性，信道容量给出可靠通信的最大速率，香农限是任何译码器都无法超越的 Eb/N0 下界。

## 核心概念

- **熵 H(X) = −Σp·log₂p**：随机变量的不确定性（bits）。
- **互信息 I(X;Y) = H(X) − H(X|Y)**：通过 Y 获得的关于 X 的信息量。
- **信道容量 C = max I(X;Y)**：可靠传输的最大速率。
- **香农限**：AWGN 信道下可靠通信最小 Eb/N0 ≈ −1.59 dB。

## 图谱关联

- [[LLR_对数似然比]]
- [[AWGN_信道模型]]
- [[T1.6_information_theory_minimum_for_decoding]]
- [[T4.5_decoder_performance_metrics]]
- 关系语义：信息论给出译码性能的理论上限。
