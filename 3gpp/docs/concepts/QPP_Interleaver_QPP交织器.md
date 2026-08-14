---
type: definition
aliases:
  - QPP
  - Quadratic Permutation Polynomial
  - QPP交织器
  - Turbo Internal Interleaver
tags:
  - 3gpp
  - concepts
  - turbo
  - interleaver
  - qpp
source_spec: "TS 36.212 §5.1.3-2"
---

# QPP 内部交织器

## 独立解释任务

任务目标：把 LTE Turbo 内部交织器（Internal Interleaver）解释为一个由二次置换多项式（Quadratic Permutation Polynomial, QPP）定义的确定性地址置换，说明它为什么同时满足伪随机打散与并行译码无冲突。在 LTE/NR 译码链路中的位置：位于 LTE Turbo 编码器的两个 RSC 组成编码器之间；译码侧对应两个软输入软输出（Soft-Input Soft-Output, SISO）译码器之间外信息交换的地址映射。

## 科学定义

QPP 交织器的地址公式为：

$$
\Pi(j)=\left(f_1 j+f_2 j^2\right)\bmod K,\quad 0\le j<K
$$

其中 $j$ 为输入比特索引，$K$ 为码块（Code Block, CB）长度（交织深度），$f_1$、$f_2$ 为该 $K$ 对应的多项式参数，$\Pi(j)$ 为第 $j$ 个输入比特在交织后序列中的位置。本课程约定输出序列由 $c'_j=c_{\Pi(j)}$ 生成。参数对由 TS 36.212 Table 5.1.3-3 逐行规定：共 188 组 $(K,f_1,f_2)$，$K$ 从 40 到 6144；例如 $K=6144$ 时 $f_1=263$、$f_2=480$。二次项使置换具有足够随机性，同时满足无冲突（contention-free）条件：并行 Turbo 译码中多个 SISO 同时读写不同存储分块时地址互不冲突。

## 直观模型

以玩具参数 $K=8$、$f_1=3$、$f_2=2$ 逐步演算 $\Pi(j)=(3j+2j^2)\bmod 8$：(1) $j=0$ 得 0；(2) $j=1$ 得 $5\bmod 8=5$；(3) $j=2$ 得 $14\bmod 8=6$；(4) $j=3$ 得 $27\bmod 8=3$；(5) $j=4$ 得 $44\bmod 8=4$；(6) $j=5$ 得 $65\bmod 8=1$；(7) $j=6$ 得 $90\bmod 8=2$；(8) $j=7$ 得 $119\bmod 8=7$。于是 $\Pi=[0,5,6,3,4,1,2,7]$，每个输出位置恰好出现一次，构成合法置换。若输入为 $c=[c_0,c_1,\dots,c_7]$，则交织输出 $c'=[c_0,c_5,c_6,c_3,c_4,c_1,c_2,c_7]$：相邻输入比特被打散到不相邻的位置，接收端解交织只需按同一公式反查即可无损恢复。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| QPP 是随机交织器 | 地址由多项式确定性生成；相同 $(K,f_1,f_2)$ 必须产生完全相同的置换（bit-exact）。 |
| $f_1$、$f_2$ 可以自行调优 | 3GPP 为 188 个合法 $K$ 逐行固定参数；参数取错会出现位置重复或漏读。 |
| 交织会改变码率 | 交织只改变比特顺序，不改变比特数量与码率。 |
| 正反向记法可以混用 | 编码器、译码器、测试脚本必须统一 $c'_j=c_{\Pi(j)}$ 约定，否则解交织错位。 |
| 地址越界会自动纠错 | $\Pi(j)$ 必须落在 $0..K-1$ 且构成一一对应，越界或重复都必须显式报错。 |

## 协议锚点

- TS 36.212 Rel-19 `36212-j30` §5.1.3.2.3（内部交织器地址公式）：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md` 行 761-773（`sections.jsonl` paragraph 428）。
- TS 36.212 Table 5.1.3-3（188 组 $K/f_1/f_2$ 参数表）：`tables/table_0009.csv` 和 `table_0009.html`。
- TS 36.212 §5.1.3.2.1（Turbo 编码器结构与 Figure 5.1.3-2）：`content.md` 行 721-745。

## 图谱关联

- [[RSC_Code_递归系统卷积码]]
- [[Turbo_码]]
- [[Iterative_Decoding_迭代译码]]
- [[BCJR_Algorithm_BCJR算法]]
- [[T6.4_LTE_Turbo_internal_interleaver]]
- [[T6.3_LTE_Turbo_encoder_trellis_termination]]
- [[概念图谱入口]]
- 关系语义：QPP 交织是 Turbo 接近香农限的关键设计。
