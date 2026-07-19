---
type: definition
aliases:
  - LLR
  - Log-Likelihood Ratio
  - 对数似然比
  - 软信息
tags:
  - 3gpp
  - concepts
  - llr
source_spec: "Algorithmic receiver concept; TS 36.211/38.211 modulation anchors; TS 36.212/38.212 decoder input context"
---

# LLR 对数似然比

LLR 用一个有符号数表达某个 bit 更像 `0` 还是 `1`，以及这个判断有多可靠。本知识库约定正 LLR 更像 `0`，负 LLR 更像 `1`；具体实现必须在接口契约中声明符号约定。

## 独立解释任务

任务目标：解释 LLR 如何把概率判断变成译码器可累加、可量化的软信息。

## 科学定义

LLR 是两个假设概率的对数比值，常写成 `log(P(bit=0|y)/P(bit=1|y))`。符号表达硬判决方向，绝对值表达可靠度。把概率比转成对数后，多个独立观测的证据可以用加法合并。

## 直观模型

LLR 像一个带方向的置信度刻度。`+8` 表示强烈相信 `0`，`+0.2` 表示略偏 `0`，`-5` 表示强烈相信 `1`，`0` 表示两边证据相当。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| LLR 是概率 | LLR 可以为负，也可以大于 1，它不是概率。 |
| LLR 符号天然固定 | 不同实现可能符号相反，接口必须声明。 |
| 只要硬判决对就够了 | 译码器需要可靠度幅度，不能只看 `0/1`。 |

## 协议锚点

- 调制与软解调来源：TS 36.211/TS 38.211 的调制、物理信道和资源映射章节。
- 译码链路上下文：TS 36.212/TS 38.212 的 channel coding、rate matching 和接收侧逆操作说明。
- 本地锚点示例：`docs/L1/T1.5_LLR_soft_decision.md`；`docs/L1/T2.2_BPSK_QPSK_soft_demapping.md`；`docs/L1/T2.3_QAM_Max_Log_MAP_demapping.md`。

## 图谱关联

- [[AWGN_信道模型]]
- [[Modulation_Constellations_调制星座]]
- [[Soft_Demodulation_软解调]]
- [[LLR_Quantization_LLR量化]]
- [[Probability_Bayes_概率与贝叶斯]]
- [[概念图谱入口]]
- [[Soft_Buffer_软缓存]]
- [[Rate_Matching_速率匹配]]
- [[LDPC_低密度奇偶校验码]]
- [[Turbo_码]]
- [[Polar_码]]
- [[T1.5_LLR_soft_decision]]
- [[T9.4_NR_LDPC_bit_deinterleaving]]
- 关系语义：LLR 是 demapper 输出和译码器输入之间的软信息载体，进入 soft buffer、rate recovery 和译码核心。
