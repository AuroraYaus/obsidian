---
type: algorithm
aliases:
  - Iterative Decoding
  - 迭代译码
  - Extrinsic Information
  - 外信息
tags:
  - 3gpp
  - concepts
  - algorithm
  - decoding
  - iterative
source_spec: "Algorithmic concept; TS 36.212/38.212 channel coding context"
---

# 迭代译码与外信息

迭代译码是现代信道译码的核心范式：多个软输入软输出（SISO）译码器反复交换"外信息"（extrinsic information），逐步提升每个比特的置信度，直到满足停止准则或达到最大迭代次数。

## 核心子概念

- **外信息 Le = L_posterior − L_channel − L_prior**：从当前译码器新增的证据，不包含输入侧已经知道的信息。外信息在分量译码器之间传递，但不能反馈自身。
- **Turbo 迭代结构**：两个 SISO 译码器轮流工作，SISO1→交织→SISO2→解交织→SISO1，每轮更新所有比特的 LLR。
- **LDPC 消息传递**：校验节点（CN）和变量节点（VN）之间双向传递 LLR 消息，沿 Tanner 图的边进行。
- **Tanner 图**：变量节点（圆形）代表比特，校验节点（方形）代表校验方程，边代表该比特参与该校验。
- **因子图 / 网格图**：更通用的概率图模型表示，BCJR 算法在网格图上运行前向 α 和后向 β 递归。

## 停止准则

- **CRC 通过**：最可靠。TB CRC 或 CB CRC 校验通过→立即终止。
- **最大迭代次数 I_max**：硬上限，防止无限循环。
- **HDA 准则**：外信息变化量低于阈值→提前停止。
- **LDPC 校验方程全满足**：所有 H·ĉᵀ=0 → 提前终止。

## 图谱关联

- [[概念图谱入口]]
- [[Turbo_码]]
- [[LDPC_低密度奇偶校验码]]
- [[Early_Stopping_早停控制]]
- [[CRC_循环冗余校验]]
- [[T4.1_iterative_decoding_extrinsic_information]]
- [[T4.2_graphs_trellises_trees_for_decoding]]
- [[T6.7_Turbo_iteration_extrinsic_stopping]]
- [[T8.4_LDPC_Tanner_graph_message_passing]]
- 关系语义：迭代译码定义了 Turbo/LDPC 的收敛动力学，外信息交换是译码增益的来源。
