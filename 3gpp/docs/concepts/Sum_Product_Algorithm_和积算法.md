---
type: definition
aliases:
  - Sum-Product Algorithm
  - SPA
  - Belief Propagation
  - 和积算法
tags:
  - 3gpp
  - concepts
  - ldpc
  - algorithm
  - spa
source_spec: "Algorithmic; TS 38.212 decoder context"
---

# 和积算法 (SPA)

## 独立解释任务

任务目标：解释 LDPC 译码的和积算法（Sum-Product Algorithm, SPA，亦称置信传播（Belief Propagation, BP））如何在 Tanner 图上迭代传递对数似然比（Log-Likelihood Ratio, LLR）消息，并给出变量节点与校验节点的更新公式与收敛判据。

SPA 位于 NR 数据信道接收链中解速率匹配之后、硬判决与 CRC 校验之前的 LDPC 迭代译码核心，是低密度奇偶校验码（Low-Density Parity-Check Code, LDPC）软判决译码的标准算法形态。

## 科学定义

SPA 在 Tanner 图的变量节点（Variable Node, VN）与校验节点（Check Node, CN）之间迭代传递 LLR 消息，第 $t$ 次迭代的更新规则为：

VN→CN：

$$L_{v\to c} = L_{ch} + \sum_{c'\in\mathcal{N}(v)\setminus\{c\}} L_{c'\to v}$$

CN→VN：

$$L_{c\to v} = 2\,\operatorname{atanh}\!\left(\prod_{v'\in\mathcal{N}(c)\setminus\{v\}} \tanh\frac{L_{v'\to c}}{2}\right)$$

- $L_{ch}$：信道 LLR；$\mathcal{N}(v)$：变量节点 $v$ 的邻居校验节点集合；求和/求积排除目标节点自身，即外信息（extrinsic）原则。
- $\tanh$ 把 LLR 压到 $(-1,1)$ 区间，$\operatorname{atanh}$ 转回 LLR 域；输出符号由输入符号之积决定，输出幅度受"最不可靠的输入"限制。
- 收敛判据：总 LLR（信道 LLR + 所有 CN 消息）符号硬判决，用 syndrome 检查 $H\hat{\mathbf{x}}^T=\mathbf{0}$ 决定早停；最终是否可信由 CRC 边界判定。

## 直观模型

一个度为 3 的校验节点收到两条输入 $L_{q_1}=0.7$、$L_{q_2}=-1.0$，向第三条边输出：

$$2\operatorname{atanh}\!\left(\tanh\frac{0.7}{2}\cdot\tanh\frac{-1.0}{2}\right)\approx -0.313$$

输出幅度 0.313 小于两个输入的最小幅度 0.7：校验节点不会"过度自信"，只有其余输入都强可靠时输出才强。类比：多位证人独立作证，只有其余证人都可信时你对某人的判断才坚定；只要有一位证人含糊，结论就跟着含糊。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| VN 更新把自身消息也加回去 | 必须排除自身（外信息原则），否则形成正反馈发散。 |
| CN 输出幅度可以超过最小输入幅度 | tanh/atanh 组合后输出幅度总小于输入的最小幅度。 |
| SPA 是 3GPP 规定的译码算法 | 协议只规定码结构，译码算法是接收机实现选择。 |
| tanh/atanh 可直接定点实现 | 输入接近 ±1 时 atanh 发散，需查表/CORDIC/裁剪，这正是 Min-Sum 近似出现的动机。 |
| 迭代次数越多越好 | syndrome 通过或达到最大迭代数即可停止，继续迭代只增加功耗。 |

## 协议锚点

- 码结构依据：TS 38.212 §5.3.2 LDPC 矩阵与基图。本地：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 945-989；Table 5.3.2-1 见 `tables/table_0013.csv/html`。SPA 公式本身为非 3GPP 标准的接收机算法。
- 讲义：`docs/L2_协议算法/T8.5_LDPC_sum_product_BP.md`；Tanner 图消息传递见 `docs/L2_协议算法/T8.4_LDPC_Tanner_graph_message_passing.md`。

## 图谱关联

- [[LDPC_低密度奇偶校验码]]
- [[Min_Sum_Algorithm_最小和算法]]
- [[Iterative_Decoding_迭代译码]]
- [[LLR_对数似然比]]
- [[Layered_LDPC_Schedule_分层LDPC调度]]
- [[概念图谱入口]]
- [[T8.5_LDPC_sum_product_BP]]
- [[T8.4_LDPC_Tanner_graph_message_passing]]
- 关系语义：SPA 是数学最优的 LDPC 消息传递形式，所有简化算法（Min-Sum 族）都是对它的逼近。
