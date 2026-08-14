---
type: definition
aliases:
  - Min-Sum
  - MS
  - NMS
  - OMS
  - Normalized Min-Sum
  - Offset Min-Sum
tags:
  - 3gpp
  - concepts
  - ldpc
  - algorithm
  - min-sum
source_spec: "Algorithmic; hardware implementation of LDPC decoding"
---

# Min-Sum 及其变体

## 独立解释任务

任务目标：解释最小和算法（Min-Sum Algorithm, MS）及其归一化最小和（Normalized Min-Sum, NMS）与偏移最小和（Offset Min-Sum, OMS）变体如何用最小值运算近似 SPA 的 tanh/atanh，并说明 min1/min2 硬件技巧。

Min-Sum 族是 NR LDPC 接收端硬件译码的主流选择，作用于 LDPC 迭代译码的校验节点（Check Node, CN）更新环节。

## 科学定义

Min-Sum 用最小幅度近似 CN 更新的精确 tanh/atanh 公式，输出符号仍由输入符号之积决定：

$$r_{i\to j}^{\mathrm{MS}}=\left(\prod_{j'\in\mathcal{N}(i)\setminus j}\operatorname{sign}(q_{j'\to i})\right)\cdot\min_{j'\in\mathcal{N}(i)\setminus j}|q_{j'\to i}|$$

- NMS 乘缩放系数压低过度自信：$r^{\mathrm{NMS}}=\alpha\cdot r^{\mathrm{MS}}$，$0<\alpha<1$（典型 0.75-0.85），需乘法或移位近似。
- OMS 减固定偏置并截零：$r^{\mathrm{OMS}}=\operatorname{sign}\cdot\max(|r^{\mathrm{MS}}|-\beta,0)$，$\beta\ge 0$（典型 0.5 附近），只需减法与比较，硬件最友好。
- 纯 MS 忽略 SPA 的修正项，会高估可靠度约 1-3 dB；NMS/OMS 与 SPA 差距约 0.1-0.3 dB。$\alpha/\beta$ 是仿真调参的实现参数，不是协议常数。
- min1/min2 技巧：一次扫描得到最小值 min1、其所在边 idx 与次小值 min2；输出给非 idx 边用 min1，输出给 idx 边自身必须用 min2——遵守外信息原则。

## 直观模型

CN 输入 $q_0=+2.4,\ q_1=-0.9,\ q_2=+1.6,\ q_3=-3.1$：min1=0.9 来自 $q_1$，min2=1.6 来自 $q_2$。输出给 $q_0$ 的边：其他输入为 $-0.9,+1.6,-3.1$，符号为负、幅度 0.9，于是 MS=-0.900、NMS($\alpha=0.75$)=-0.675、OMS($\beta=0.4$)=-0.500；输出给 $q_1$ 自身则幅度必须换 min2=1.6。类比：小组评审取"最没把握的那位评委"的意见幅度作为结论强度——最弱证据决定置信度上限，这是对精确概率计算（SPA）的保守近似。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| MS 与 SPA 完全等价 | MS 高估可靠度约 1-3 dB，需 NMS/OMS 修正。 |
| 输出给最小值所在边也用 min1 | 违反外信息原则，必须换用 min2。 |
| $\alpha/\beta$ 是协议规定的常数 | 二者是仿真调参的实现参数，TS 38.212 不规定。 |
| OMS 的 $\beta$ 越大越好 | $\beta$ 过大会把大量弱但有用的消息压成 0，收敛变差。 |
| Min-Sum 是 3GPP 规定的算法 | 3GPP 只规定 LDPC 码结构（§5.3.2），译码算法为实现选择。 |

## 协议锚点

- LDPC 矩阵结构依据：TS 38.212 §5.3.2。本地：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 945-989；Table 5.3.2-2/3 见 `tables/table_0014.csv/html`、`tables/table_0015.csv/html`。MS/NMS/OMS 本身为非 3GPP 标准的接收机算法。
- 讲义：`docs/L2_协议算法/T8.6_LDPC_MS_NMS_OMS.md`；精确 SPA 见 `docs/L2_协议算法/T8.5_LDPC_sum_product_BP.md`。

## 图谱关联

- [[Sum_Product_Algorithm_和积算法]]
- [[LDPC_低密度奇偶校验码]]
- [[Iterative_Decoding_迭代译码]]
- [[Fixed_Point_Numbers_定点数]]
- [[LLR_Quantization_LLR量化]]
- [[概念图谱入口]]
- [[T8.6_LDPC_MS_NMS_OMS]]
- [[T8.5_LDPC_sum_product_BP]]
- 关系语义：MS 族是 LDPC 硬件译码主流选择，是 SPA 的工程近似。
