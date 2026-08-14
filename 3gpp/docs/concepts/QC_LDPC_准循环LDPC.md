---
type: definition
aliases:
  - QC-LDPC
  - Quasi-Cyclic LDPC
  - Lifting Size
  - Zc
  - 循环移位
tags:
  - 3gpp
  - concepts
  - ldpc
  - qc-ldpc
  - lifting
source_spec: "TS 38.212 §5.2.2"
---

# QC-LDPC 与提升大小 Zc

## 独立解释任务

任务目标：把 TS 38.212 基图中的"一格"解释成一个 $Z_c\times Z_c$ 的循环移位子矩阵，并说明准循环结构为什么让 NR LDPC 能被硬件高效实现。在 LTE/NR 译码链路中的位置：准循环低密度奇偶校验码（Quasi-Cyclic Low-Density Parity-Check Code, QC-LDPC）是 NR 信道译码器直接消费的校验矩阵形态——LDPC 译码器读取的完整校验矩阵 $H$ 正是基图（Base Graph, BG）经提升大小 $Z_c$ 展开后的准循环矩阵。

## 科学定义

QC-LDPC 的核心是提升（lifting）操作：把基图的每个元素替换成 $Z_c\times Z_c$ 子矩阵，得到 bit-level 校验矩阵：

$$
H \in \{0,1\}^{m_b Z_c \times n_b Z_c}
$$

其中 $m_b$ 为基图行数、$n_b$ 为基图列数。TS 38.212 §5.3.2 给出 BG1 为 $46\times68$、BG2 为 $42\times52$，即 $H_{\mathrm{BG1}}\in\{0,1\}^{46Z_c\times68Z_c}$、$H_{\mathrm{BG2}}\in\{0,1\}^{42Z_c\times52Z_c}$。替换规则由基图元素 $P_{ij}$（循环移位值）决定：$P_{ij}=0$ 替换为单位阵；$P_{ij}=-1$（表内空白）替换为全零矩阵；其余 $P_{ij}=p$ 替换为单位阵循环右移 $p$ 位得到的循环置换矩阵。

提升大小 $Z_c\in\{2,3,\dots,384\}$，由 TS 38.212 Table 5.3.2-1 按 8 个集合（set index $i_{\mathrm{LS}}=0..7$）组织，例如 set 0 含 $\{2,4,8,16,32,64,128,256\}$、set 1 含 $\{3,6,12,24,48,96,192,384\}$。信息位列数为 22（BG1）与 10（BG2），即信息位长度 $K=22Z_c$（BG1）或 $K=10Z_c$（BG2）；速率匹配（Rate Matching）不发送前 $2Z_c$ 个系统位列（穿孔，Puncturing）。

## 直观模型

取 $Z_c=4$、移位值 $P_{ij}=1$，该基图元素展开为 $4\times4$ 循环移位矩阵：

$$
\begin{pmatrix}
0&1&0&0\\
0&0&1&0\\
0&0&0&1\\
1&0&0&0
\end{pmatrix}
$$

第 0 行在第 1 列有 1、第 1 行在第 2 列有 1，依此类推，最后一行回到第 0 列——每行的 1 都比上一行右移一列，首尾相接形成循环。移位值为 0 时退化为单位阵（对角线上全 1）；移位值为 $-1$ 时矩阵全 0，表示该位置没有连接。基图决定"哪些 $Z_c\times Z_c$ 块相连"，$Z_c$ 决定"每个块内有多少条 bit-level 边"：$Z_c=4$ 时一个基图连接是 4 条边，$Z_c=384$ 时是 384 条边。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| $Z_c$ 越大纠错能力越强 | $Z_c$ 只放大矩阵尺寸；纠错能力由基图结构决定，$Z_c$ 由码块长度与 Table 5.3.2-1 选择。 |
| 基图中 0 表示发送比特 0 | 基图元素是子矩阵指令：0 表示单位阵，$-1$（空白）表示全零矩阵。 |
| 循环移位值越大校验越强 | 移位值只是块内连接位置的参数，不同移位值对应不同边连接，不直接映射可靠性。 |
| 穿孔的前 $2Z_c$ 位可填 0 | 穿孔位置语义为 unknown，强制填 0 会污染译码器对系统位的推断。 |

## 协议锚点

- TS 38.212 Rel-19 `38212-j30` §5.2.2（lifting size 选择入口）：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 747-775。
- TS 38.212 §5.3.2（基图与 QC 展开、替换规则）：`content.md` 行 948-989。
- Table 5.3.2-1（lifting size set）：`tables/table_0013.csv/html`；Table 5.3.2-2（BG1 移位表）：`tables/table_0014.csv/html`；Table 5.3.2-3（BG2 移位表）：`tables/table_0015.csv/html`。

## 图谱关联

- [[Base_Graph_基图]]
- [[LDPC_低密度奇偶校验码]]
- [[Rate_Matching_速率匹配]]
- [[CB_码块]]
- [[Segmentation_码块分段]]
- [[T8.3_NR_LDPC_lifting_QC_matrix]]
- [[T8.2_NR_LDPC_base_graph_selection]]
- [[T19.2_NR_LDPC_RTL_microarchitecture]]
- [[概念图谱入口]]
- 关系语义：Zc 提升决定码长、校验矩阵尺寸和硬件并行度。
