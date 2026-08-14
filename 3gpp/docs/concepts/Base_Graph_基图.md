---
type: definition
aliases:
  - Base Graph
  - BG
  - BG1
  - BG2
  - 基图
tags:
  - 3gpp
  - concepts
  - ldpc
  - base-graph
source_spec: "TS 38.212 §5.2.2"
---

# LDPC 基图 BG1/BG2

## 独立解释任务

任务目标：解释 NR LDPC 码的基图（Base Graph, BG）BG1/BG2 的矩阵规模、选择规则，以及基图与完整校验矩阵 $H$、提升大小 $Z_c$ 的关系。

基图选择位于 NR 共享信道发送/接收链的码块分段之后、LDPC 编码（或译码）之前，是决定译码器使用哪套校验矩阵结构、层循环边界和移位值表的协议分支点。

## 科学定义

基图是 LDPC 校验矩阵 $H$ 的模板：TS 38.212 §5.3.2 规定 BG1 基矩阵为 46 行 × 68 列，BG2 为 42 行 × 52 列；行列是"行列组"（group），每个位置经提升大小 $Z_c$ 展开成 $Z_c\times Z_c$ 的循环移位子矩阵，完整 $H$ 规模为 $(46\cdot Z_c)\times(68\cdot Z_c)$（BG1）。移位值从 Table 5.3.2-2（BG1）/Table 5.3.2-3（BG2）按 $i_{\mathrm{LS}}$ 列选取，实际循环移位 $P_{i,j}=V_{i,j}\bmod Z_c$。

选择规则（TS 38.212 §6.2.2 UL-SCH、§7.2.2 DL-SCH/PCH）按 TB 载荷 $A$ 与目标码率 $R$ 判定，满足以下任一条件选 BG2，否则选 BG1：

1. $A\le 292$；
2. $A\le 3824$ 且 $R\le 0.67$；
3. $R\le 0.25$。

BG1 偏大载荷高吞吐（信息列数 $K_b=22$），BG2 偏短块低延迟低码率（$K_b=10$）；$R$ 来自 TS 38.214 §5.1.3.1 的 MCS 表。

## 直观模型

分支走读：$A=5000,\ R=0.50$——$A>292$、$A>3824$、$R>0.25$ 三条 BG2 分支均不满足，选 BG1；$A=3000,\ R=0.50$——满足 $A\le 3824$ 且 $R\le 0.67$，选 BG2；$A=6000,\ R=0.20$——低码率分支 $R\le 0.25$，选 BG2。若误选，译码器会用 42×52 结构解释本应按 46×68 处理的码块，消息地址与层边界全错。类比：BG 像服装纸样的基础版型——按体型（$A$、$R$）选版型，再按 $Z_c$ 放大到实际尺码；版型选错，后面所有裁剪都错。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| BG1 是 22×68、BG2 是 10×42 | 那是信息列数 $K_b$ 与行数的混淆；协议矩阵尺寸是 BG1 46×68、BG2 42×52。 |
| 基图就是完整校验矩阵 $H$ | 基图是模板，完整 $H$ 还要按 $Z_c$ 逐位展开。 |
| BG 选择看 $B$ 或 $E$ | 选择只看 TB 载荷 $A$ 与码率 $R$；把 $B/E$ 当 $A$ 会错判 292/3824 边界。 |
| BG2 是性能更差的次品 | BG2 是短块低码率分支的协议选择，是适配性分工而非质量分级。 |
| 移位值直接使用表中数字 | 实际循环移位 $P_{i,j}=V_{i,j}\bmod Z_c$，$Z_c$ 变化时需取模。 |

## 协议锚点

- TS 38.212 §5.2.2 与 §5.3.2：LDPC 基图矩阵尺寸、Table 5.3.2-1/2/3。本地：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 717-775、945-989。
- TS 38.212 §6.2.2（UL-SCH）与 §7.2.2（DL-SCH/PCH）基图选择。本地：`content.md` 行 1371-1379、3747-3755。
- 码率 $R$ 来源：TS 38.214 §5.1.3.1 与 §6.1.4.1。本地：`3GPP_Rel19/processed/TS_38.214_38214-j30/content.md` 行 1259-1383、6891-7027。
- 讲义：`docs/L2_协议算法/T8.2_NR_LDPC_base_graph_selection.md`；提升与 QC 展开见 `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md`。

## 图谱关联

- [[LDPC_低密度奇偶校验码]]
- [[QC_LDPC_准循环LDPC]]
- [[Segmentation_码块分段]]
- [[Rate_Matching_速率匹配]]
- [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]
- [[概念图谱入口]]
- [[T8.2_NR_LDPC_base_graph_selection]]
- [[T8.3_NR_LDPC_lifting_QC_matrix]]
- 关系语义：BG 决定 LDPC 码结构，经 Zc 提升后得完整 QC-LDPC 矩阵。
