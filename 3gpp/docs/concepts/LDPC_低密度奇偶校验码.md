---
type: algorithm
aliases:
  - LDPC
  - Low-Density Parity-Check Code
  - 低密度奇偶校验码
  - NR LDPC
tags:
  - 3gpp
  - concepts
  - ldpc
source_spec: "TS 38.212 Rel-19 §5.2.2, §5.3.2, §5.4.2"
---

# LDPC 低密度奇偶校验码

LDPC 是 NR 数据业务使用的主要信道编码家族。它用稀疏奇偶校验矩阵描述约束，接收端通过 BP、Min-Sum 或 layered schedule 在 Tanner 图上迭代更新 LLR。

## 独立解释任务

任务目标：解释 LDPC 如何用稀疏校验矩阵和软信息迭代恢复 NR 数据块。

## 科学定义

LDPC 是 Low-Density Parity-Check Code。它用一个稀疏奇偶校验矩阵 `H` 定义合法码字集合，合法码字满足 `H * c = 0`。接收端根据 LLR 和矩阵连接关系，在变量节点和校验节点之间传递消息，逐轮逼近满足校验约束的候选码字。

## 直观模型

LDPC 像一个由很多局部规则组成的推理网络。每条规则只检查少量 bit，所有规则合起来约束整个码字。某些 bit 的 LLR 很可靠时，会通过图上的边影响相邻 bit 的判断。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 低密度表示低速率 | 低密度指矩阵中 `1` 少，不是业务速率低。 |
| LDPC 只是一张大矩阵 | NR LDPC 还涉及 BG、Zc、rate matching、CB CRC 和 HARQ。 |
| syndrome pass 可直接交付 TB | 仍需 CB/TB CRC 和重组边界。 |

## 协议锚点

- NR：TS 38.212 Rel-19 §5.2.2 LDPC segmentation。
- NR：TS 38.212 Rel-19 §5.3.2 LDPC channel coding。
- NR：TS 38.212 Rel-19 §5.4.2 LDPC rate matching。
- 本地锚点示例：`3GPP_Rel19/processed/TS_38.212_38212-j30/TS_38.212_38212-j30_content.md`。

## 图谱关联

- [[Base_Graph_基图]]
- [[QC_LDPC_准循环LDPC]]
- [[Sum_Product_Algorithm_和积算法]]
- [[Min_Sum_Algorithm_最小和算法]]
- [[Layered_LDPC_Schedule_分层LDPC调度]]
- [[Iterative_Decoding_迭代译码]]
- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[CB_码块]]
- [[CBG_码块组]]
- [[Rate_Matching_速率匹配]]
- [[CRC_循环冗余校验]]
- [[T8.1_NR_LDPC_decoder_chain_overview]]
- [[T8.4_LDPC_Tanner_graph_message_passing]]
- [[T8.5_LDPC_sum_product_BP]]
- 关系语义：LDPC 以 CB 为译码粒度，接收 LLR/rate recovery 输出，并用 CRC/HARQ 验收链路结果。
