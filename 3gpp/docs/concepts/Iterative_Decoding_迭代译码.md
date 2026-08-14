---
type: definition
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

## 独立解释任务

任务目标：解释迭代译码（Iterative Decoding）中多个软输入软输出（Soft-Input Soft-Output, SISO）译码器如何通过外信息（Extrinsic Information）在信道观测与编码约束之间反复校正比特置信度，并说明停止准则在收敛与功耗之间折中的作用。在 LTE/NR 译码链路中，迭代译码位于解调输出的信道 LLR 与 CRC 验收之间：Turbo（Turbo 码，Turbo Code）与 LDPC（低密度奇偶校验码，Low-Density Parity-Check Code）译码器在信道对数似然比（Log-Likelihood Ratio, LLR）基础上多轮交换外信息，直到满足停止准则或达到最大迭代次数。

## 科学定义

译码器内四类软信息满足加法分解：后验 LLR 等于信道 LLR、先验信息与外信息之和：

$$
L_{\mathrm{post}}(b_i)=L_{\mathrm{ch}}(b_i)+L_{\mathrm{apr}}(b_i)+L_{\mathrm{ext}}(b_i)
\tag{1}
$$

$L_{\mathrm{ch}}$ 来自解调器，$L_{\mathrm{apr}}$ 是当前模块更新前已有的线索，$L_{\mathrm{ext}}$ 是当前模块利用自身约束新产生的增量证据，$L_{\mathrm{post}}$ 是总置信度。外信息的关键要求是"非回声"：传给下一个模块之前必须扣除信道与先验，只留新增证据：

$$
L_{\mathrm{ext}}=L_{\mathrm{post}}-L_{\mathrm{ch}}-L_{\mathrm{apr}}
\tag{2}
$$

若把后验原样反馈，同一条证据会被重复计数，置信度虚高。LDPC 校验节点给变量节点的消息遵循 Min-Sum 教学近似：

$$
L_{c\rightarrow i}=\left(\prod_{j\in\mathcal{N}(c)\setminus i}\mathrm{sign}(L_{j\rightarrow c})\right)\cdot\min_{j\in\mathcal{N}(c)\setminus i}|L_{j\rightarrow c}|
\tag{3}
$$

式 (3) 中 $\mathcal{N}(c)$ 是参与校验 $c$ 的比特集合，计算时必须排除目标比特 $i$ 自身；符号乘积决定建议方向，最小绝对值表示这条建议受最不可靠邻居限制。变量节点最终合成后验：

$$
L_{\mathrm{post}}(b_i)=L_{\mathrm{ch}}(b_i)+\sum_{c\in\mathcal{N}(i)}L_{c\rightarrow i}
\tag{4}
$$

停止准则作为迭代循环的终止条件分四类：CRC（循环冗余校验，Cyclic Redundancy Check）通过最可靠；最大迭代次数是硬上限；外信息变化量低于阈值可提前停止；LDPC 所有校验方程满足（syndrome 为零）可提前终止。迭代结构上，Turbo 是两个 SISO 译码器经交织/解交织轮流交换外信息；LDPC 是校验节点与变量节点沿 Tanner 图双向传递 LLR 消息。

## 直观模型

用 4 个比特、两条校验关系手算一次置信度更新。信道 LLR 为 $b_0=+4.0$、$b_1=+1.0$、$b_2=-0.6$、$b_3=+3.0$；约束为 $b_0\oplus b_1\oplus b_2=0$ 与 $b_1\oplus b_2\oplus b_3=0$。硬判决 $0,0,1,0$ 代入两条校验都得 1，两条校验都把矛头指向弱比特 $b_2$。第一条校验给 $b_2$ 的外信息只看 $b_0,b_1$：符号乘积 $(+1)\times(+1)=+1$，幅度取 $\min(4.0,1.0)=1.0$，得 $+1.0$；第二条校验只看 $b_1,b_3$：同样得 $+1.0$。合成后验 $L_{\mathrm{post}}(b_2)=-0.6+1.0+1.0=+1.4$，$b_2$ 从"略像 `1`"翻转为"更像 `0`"。这不是魔法，而是两个校验关系都认为 $b_2=0$ 更能解释当前观测。若计算时误把 $b_2$ 自己的输入放进去，$b_2$ 的判断会绕一圈影响自己，造成证据重复计数——这正是外信息必须排除目标变量自身的原因。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 迭代译码就是把同一算法多跑几遍 | 迭代的本质是不同约束之间交换外信息，每轮都改变比特置信度分布。 |
| 外信息就是后验 LLR | 外信息必须扣除信道与先验（式 (2)），否则回声导致证据重复计数。 |
| 3GPP 规定固定迭代次数 | 迭代次数、LLR 位宽与早停门限都是接收机实现策略，3GPP 不强制。 |
| syndrome 为零等于 TB 交付通过 | syndrome 是编码约束检查，TB 交付还要看 CRC 与重组边界。 |
| 迭代次数越多越好 | 增益递减而功耗延迟线性上升，需用早停准则折中。 |

## 协议锚点

- LTE Turbo 编码结构：TS 36.212 Rel-19 `36212-j30` §5.1.3.2（Figure 5.1.3-2 文字锚点），本地 `3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`。
- LTE 分段/码块/速率匹配背景：TS 36.212 Rel-19 `36212-j30` §5.1.2、§5.2.2.2、§5.3.2.2。
- NR LDPC 编码结构：TS 38.212 Rel-19 `38212-j30` §5.3.2（Tables 5.3.2-1/2/3），本地 `3GPP_Rel19/processed/TS_38.212_38212-j30/content.md`。
- NR UL-SCH/DL-SCH 链路：TS 38.212 Rel-19 `38212-j30` §6.2、§7.2。
- 标注：具体 MAP（最大后验概率，Maximum A Posteriori）/Max-Log-MAP、BP/Min-Sum 内部消息更新公式属接收机实现算法，3GPP 不规定厂商迭代次数、LLR 位宽、归一化 Min-Sum 参数或早停门限。
- 本地讲义锚点：`docs/L1_基础/T4.1_iterative_decoding_extrinsic_information.md`。

## 图谱关联

- [[概念图谱入口]]
- [[Turbo_码]]
- [[LDPC_低密度奇偶校验码]]
- [[Early_Stopping_早停控制]]
- [[CRC_循环冗余校验]]
- [[Sum_Product_Algorithm_和积算法]]
- [[Min_Sum_Algorithm_最小和算法]]
- [[RSC_Code_递归系统卷积码]]
- [[QPP_Interleaver_QPP交织器]]
- [[T4.1_iterative_decoding_extrinsic_information]]
- [[T4.2_graphs_trellises_trees_for_decoding]]
- [[T6.7_Turbo_iteration_extrinsic_stopping]]
- [[T8.4_LDPC_Tanner_graph_message_passing]]
- 关系语义：迭代译码定义了 Turbo/LDPC 的收敛动力学，外信息交换是译码增益的来源。
