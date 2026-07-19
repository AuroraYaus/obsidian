---
type: algorithm
aliases:
  - Turbo
  - Turbo Code
  - Turbo 码
  - LTE Turbo
tags:
  - 3gpp
  - concepts
  - turbo
source_spec: "TS 36.212 Rel-19 §5.1.3 and §5.1.4"
---

# Turbo 码

Turbo 码是 LTE 数据业务使用的主要信道编码家族。接收端通常通过 BCJR/MAP 或 Log-MAP/Max-Log-MAP 在两个组成译码器之间交换外信息。

## 独立解释任务

任务目标：解释 Turbo 码如何通过两个组成译码器和交织外信息实现迭代增益。

## 科学定义

Turbo 码通常由两个递归系统卷积码和一个内部交织器组成。发送端对同一信息序列的原顺序和交织顺序分别编码，形成多路冗余。接收端用两个软输入软输出译码器轮流更新外信息，逐步提高每个 bit 的后验可靠度。

## 直观模型

Turbo 译码像两位审稿人看同一篇文章。一位看原顺序，另一位看打乱后的顺序。每轮二者把“我从自己视角得到的新证据”交给对方，但不能把对方刚给自己的证据原样返还。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| Turbo 译码只输出硬判决 | 迭代内部依赖 LLR 和外信息。 |
| 外信息可以随便相加 | 外信息必须避免重复使用同一证据。 |
| LTE Turbo 和 NR LDPC rate matching 一样 | 二者都有速率匹配，但结构、交织和地址规则不同。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 §5.1.3 Channel coding。
- LTE：TS 36.212 Rel-19 §5.1.4 Rate matching。
- 本地锚点示例：`3GPP_Rel19/processed/TS_36.212_36212-j30/TS_36.212_36212-j30_content.md`。

## 图谱关联

- [[RSC_Code_递归系统卷积码]]
- [[BCJR_Algorithm_BCJR算法]]
- [[QPP_Interleaver_QPP交织器]]
- [[Iterative_Decoding_迭代译码]]
- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[CB_码块]]
- [[Rate_Matching_速率匹配]]
- [[CRC_循环冗余校验]]
- [[Early_Stopping_早停控制]]
- [[T6.1_LTE_Turbo_decoder_chain_overview]]
- [[T6.6_Log_MAP_Max_Log_MAP_Turbo]]
- [[T7.1_LTE_Turbo_de_rate_matching_overview]]
- 关系语义：Turbo 码以 CB 为核心译码对象，依赖 LLR、rate recovery、CRC 和迭代停止控制。
