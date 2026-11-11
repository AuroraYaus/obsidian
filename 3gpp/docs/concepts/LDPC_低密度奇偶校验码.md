---
type: definition
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

## 符号与记号约定

本笔记以文字与表格描述机制，不引入 LaTeX 数学公式；文中涉及的带宽、数量与码率等量均以文字就地说明其含义与来源，无需符号表。

LDPC 是 NR 数据业务使用的主要信道编码家族。它用稀疏奇偶校验矩阵描述约束，接收端通过 BP、Min-Sum 或 layered schedule 在 Tanner 图上迭代更新 LLR。一句话本质：**LDPC 是"很多条局部规则组成的推理网络"——每条规则只查少数几个比特，所有规则合起来约束整个码字，可靠比特的置信度沿边传播**。

## 解释目标与范围

本节目标：解释 LDPC 如何用稀疏校验矩阵和软信息迭代恢复 NR 数据块。

## 前置概念

线性分组码与奇偶校验。线性分组码用一组模 2 线性方程约束码字，合法码字构成校验矩阵的零空间，见 [[GF2_伽罗瓦域]]。LDPC 的特殊之处不在约束形式，而在校验矩阵极其稀疏。

稀疏图与迭代消息传递。校验矩阵可以画成变量节点与校验节点之间的二分图，译码即在图上沿边传递置信度并逐轮更新，见 [[Iterative_Decoding_迭代译码]] 与 [[Sum_Product_Algorithm_和积算法]]。稀疏性保证每轮每个节点只处理少量邻居，计算量随码长线性增长。

软信息与码块结构。迭代译码的输入是解调器给出的对数似然比，输出是每个比特的后验可靠度，见 [[LLR_对数似然比]]。NR 的 LDPC 还依赖准循环结构与提升因子把一张小基图展开为长码，见 [[QC_LDPC_准循环LDPC]] 与 [[Base_Graph_基图]]。

## 起源与演进

(1) **起点：Gallager 的遗产与 Turbo 的接力。** LDPC 1962 年由 Gallager 提出，因当时算力不足被遗忘近四十年；Turbo 码的成功重新点燃了迭代译码研究，Mackay 与 Neal 在 90 年代重新发现 LDPC 能以更低复杂度逼近香农极限——NR 最终选它做数据信道主力。

(2) **核心结构：稀疏校验矩阵。** 校验矩阵 H 的绝大多数元素为 0（"低密度"），合法码字满足 H·c=0；稀疏性是图上迭代消息传递高效的根源——每条校验规则只牵涉少数比特。

(3) **译码范式：Tanner 图双向消息。** 变量节点与校验节点沿图边交换 LLR：可靠 bit 的置信度通过边影响相邻 bit 的判断，逐轮逼近满足全部约束的候选码字——和积/最小和/分层调度三族实现（见 [[Sum_Product_Algorithm_和积算法]] 等）。

(4) **NR 的落地。** 基图 BG1/BG2 + 提升 Zc + 前 2Zc 位恒打孔 + CB CRC/HARQ 验收——NR LDPC 是一整套结构化 QC-LDPC，不是"一张大矩阵"。

(5) **与 Turbo 的分工。** Turbo 留在 LTE，LDPC 接管 NR 数据——长码块并行度与吞吐优势明显；NR 控制信道交给 Polar。三族各守一段。

## 科学定义

LDPC 是 Low-Density Parity-Check Code。它用一个稀疏奇偶校验矩阵 `H` 定义合法码字集合，合法码字满足 `H * c = 0`。接收端根据 LLR 和矩阵连接关系，在变量节点和校验节点之间传递消息，逐轮逼近满足校验约束的候选码字。

## 直观模型

LDPC 的结构由一张稀疏二分图描述：一侧是变量节点、对应码字的比特，另一侧是校验节点、对应校验方程，每条边表示某个比特参与某个校验。每个校验只约束少量比特，所有校验合起来约束整个码字。当某些比特的置信度很高时，它们的证据沿边传给相邻校验，再由校验转给同校验内的其它比特，这正是迭代译码的传播机制。

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
- 本地锚点示例：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md`。

## 关键要点

1. LDPC = 稀疏校验矩阵 + 图上迭代译码；"低密度"指矩阵里 1 少，不是速率低。
2. 1962 年 Gallager 提出、90 年代复兴——NR 数据信道主力。
3. 译码在 Tanner 图上双向传 LLR：可靠 bit 影响相邻 bit 的判断。
4. NR LDPC = BG + Zc 提升 + 前 2Zc 打孔 + CB CRC/HARQ 验收。
5. syndrome 全零 ≠ 交付通过：还要 CB/TB CRC 与重组边界。
6. 分工：Turbo 留 LTE、LDPC 管 NR 数据、Polar 管 NR 控制。

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
