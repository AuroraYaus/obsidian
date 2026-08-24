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

信息论为通信系统设立根本性能边界。熵度量不确定性，信道容量给出可靠通信的最大速率，香农限是任何译码器都无法超越的 $E_b/N_0$ 下界。

## 独立解释任务

任务目标：解释熵、互信息、信道容量与香农限四个量的定义，以及它们如何划定译码器性能不可逾越的边界。

## 科学定义

- **熵**（不确定性度量，单位 bit）：

$$H(X) = -\sum_{x} p(x)\log_2 p(x)$$

其中 $p(x)$ 为随机变量 $X$ 的概率质量函数，$H(X)$ 是自信息 $-\log_2 p(x)$ 的期望。

- **互信息**：$I(X;Y) = H(X) - H(X|Y)$，表示通过观测 $Y$ 获得的关于 $X$ 的平均信息量。
- **信道容量**：$C = \max_{p(x)} I(X;Y)$，对输入分布求最大值，是可靠传输的最大速率。
- **AWGN 信道容量**：$C = \frac{1}{2}\log_2(1+\mathrm{SNR})$ bit/信道使用，SNR 为信噪比。
- **香农限**：AWGN 信道下可靠通信的最小 $E_b/N_0 \approx -1.59$ dB，是任何译码器的性能下界。

## 直观模型

数值例子：二进制对称信道（Binary Symmetric Channel, BSC）翻转概率 0.1，则 $H_2(0.1)\approx0.469$ bit，容量 $C = 1 - 0.469 \approx 0.531$ bit/次——码率超过 0.531 时无论怎样编码都不可能可靠传输。香农限类比光速极限：任何编码与译码方案都不能在 $E_b/N_0$ 低于约 −1.59 dB 时实现 AWGN 信道下的可靠通信，现代 Turbo/LDPC/Polar 码只能不断逼近它。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 达到香农限等于在任意码率下可靠 | 香农限对应信道容量，码率必须低于容量，且接近容量需要极长码长。 |
| 信道容量是短码的瞬时速率上限 | 容量是码长趋于无穷时的渐近上界，短码实际性能离容量有可观的差距。 |
| 熵就是信息内容 | 熵是平均不确定性的度量；单个符号携带的自信息是 $-\log_2 p(x)$，熵是它的期望。 |
| $E_b/N_0$ 为负值违反能量直觉 | $E_b/N_0$ 是每信息比特能量与噪声功率谱密度之比，强编码下可靠通信的最小值约 −1.59 dB。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 `36212-j30` §5.1.3.2 Turbo coding——信息论冗余结构的协议来源。
- NR：TS 38.212 Rel-19 `38212-j30` §5.3.1 Polar coding、§5.3.2 Low density parity check coding。
- 本地锚点：`3GPP_Rel19/processed/TS_36.212_36212-j30/sections.jsonl`；`3GPP_Rel19/processed/TS_38.212_38212-j30/sections.jsonl`。
- 协议边界：熵、互信息、容量是通用数学概念，非 3GPP 专属规则，协议参数仍需回到 TS 36.212/38.212 核验。

## 图谱关联

- [[LLR_对数似然比]]
- [[AWGN_信道模型]]
- [[LDPC_低密度奇偶校验码]]
- [[Polar_码]]
- [[概念图谱入口]]
- [[T1.6_information_theory_minimum_for_decoding]]
- [[dB_分贝]]（Eb/N0 与香农限的对数读数标度）
- [[T4.5_decoder_performance_metrics]]
- 关系语义：信息论给出译码性能的理论上限。
