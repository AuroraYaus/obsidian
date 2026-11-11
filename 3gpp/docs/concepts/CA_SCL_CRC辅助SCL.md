---
type: definition
aliases:
  - CA-SCL
  - CRC-Aided SCL
  - CRC辅助SCL
  - Path Selection
tags:
  - 3gpp
  - concepts
  - polar
  - algorithm
  - ca-scl
  - crc
source_spec: "Algorithmic; TS 38.212 Polar decoder context"
---

# CA-SCL CRC辅助SCL

## 符号与记号约定

| 符号 | 含义与取值 | 协议锚点 |
|:---|:---|:---|
| $A$ | 控制信息载荷的比特数，即进入 CRC 附加之前的信息位个数；取非负整数，单位 bit | TS 38.212 §6.3.1.2.1 |
| $r$ | CRC 校验位的长度，单位 bit；UCI 场景取 6 或 11，DCI 场景取 24 | 由 TS 38.212 §5.1 导出 |
| $D$ | CRC 生成多项式的形式变量，无量纲；多项式按 $D$ 的幂次书写，$D^{11}$ 这类写法表示第 11 级寄存器的抽头 | TS 38.212 §5.1 |
| $g_{\mathrm{CRC11}}(D)$ | 11 位 CRC 的生成多项式，系数取 0 或 1、最高次幂为 11，由 $D^{11}$、$D^{10}$、$D^{9}$、$D^{5}$ 与常数项 1 相加而成，量纲一 | TS 38.212 §5.1 |
| $g_{\mathrm{CRC6}}(D)$ | 6 位 CRC 的生成多项式，系数取 0 或 1、最高次幂为 6，由 $D^{6}$、$D^{5}$ 与常数项 1 相加而成，量纲一 | TS 38.212 §5.1 |
| $L$ | SCL 译码保留的候选路径条数；取正整数，常用 8，量纲一 | 实现域（接收机译码器配置） |

多项式括号中的 `bit` 是长度单位标签，不是变量；$D$ 的幂次只表示寄存器级数。各行来源统一写在第三列：协议量给 TS 条款号，派生量给「由 TS … §… 导出」，非协议量给「非 3GPP 标准」或「实现域」。

CA-SCL（CRC 辅助 SCL）是 NR Polar 控制信道接收链的最后一级：SCL 输出 L 条候选路径后，按 PM 升序逐条做 CRC 检查，输出第一条通过的路径。一句话本质：**CA-SCL 是"海选+背景核查"——初试按分数（PM）排名，录用必须过背景核查（CRC）；核查不过，分数再高也不录用**。

## 解释目标与范围

本节目标：解释循环冗余校验辅助逐次消除列表译码（CRC-aided Successive Cancellation List, CA-SCL）如何用 CRC 从 SCL 候选路径中选出最终输出，以及 NR 控制信道 CRC 长度的协议条件与 DCI 的 RNTI 边界。

CA-SCL 是 NR Polar 控制信道接收链的最后一级：位于 SCL 树译码之后、控制比特交付之前，承担候选路径的最终选择。

## 前置概念

**列表译码**（List Decoding）指译码器在每一步保留若干条候选路径、而不是只保留一条的译码方式，保留条数记作 $L$。列表译码用并行度换取纠错能力：正确路径只要在某一刻未被剪掉，就有机会在后续步骤中胜出；代价是每步要做 $L$ 份度量更新与排序，复杂度随 $L$ 线性增长。

**路径度量**（Path Metric）是列表译码给每条候选路径打的分数，通常取该路径上各步分支度量的累加，数值越小表示该路径与接收证据越吻合。路径度量是软量，它只说明"哪条更像"，不说明"哪条一定对"；因此按度量排序得到的首条路径仍需要一道独立的硬检错来确认。

**循环冗余校验**（Cyclic Redundancy Check, CRC）指发送端用生成多项式对信息位做模 2 除法、把余数作为校验位附在信息位之后的检错机制。接收端对收到的整段比特重做一次除法，余数为零则通过；校验位长度 $r$ 决定检错强度，长度越长，随机错误被漏过的概率越小。

**误检概率**（False Alarm Probability）指一段错误比特恰好通过 CRC 检查的概率。对随机错误，该概率约等于校验位所能区分状态数的倒数，随 $r$ 增大而指数下降；它描述的是"检错漏过"的风险，与"译码选错路径"是两回事，两者共同决定最终块错误率。

**控制信息载荷**（Control Information Payload）指承载在控制信道上的比特集合，上行称 UCI、下行称 DCI，其比特数就是 $A$。载荷长度决定 CRC 是否附加以及附加几位：短载荷的检错需求可由编码本身承担，长载荷则需要独立的 CRC 边界，这一分档由协议按 $A$ 的取值给出。

## 起源与演进

(1) **起点：PM 会被骗。** PM 是软度量，PM 最小的路径不一定是正确路径——需要一个硬检错边界做最终把关。

(2) **机制：CRC 逐条核查。** 发送端把信息位连同 CRC parity bits 一起送入 Polar 编码（TS 38.212 §5.2.1）；接收端 SCL 输出 L 条候选，按 PM 升序逐条查 CRC，输出第一条通过的——不是无脑取 PM 最小。

(3) **NR 的 CRC 长度条件。** UCI：$A\ge 20$ 附加 CRC11、$12\le A\le 19$ 附加 CRC6、$A\le 11$ 不附加；DCI 用 24 bit 且与 RNTI 相关。随机错误候选误通过的概率量级约 $2^{-r}$。

(4) **性能与边界。** 工程上 $L=8$ 时 CA-SCL 已接近最大似然译码；但 CRC 不能替代列表——正确路径若在 SCL 剪枝时被删除，CRC 检查根本看不到它。

(5) **分工总结。** CRC 是硬检错边界、PM 是软度量——各司其职；CA-SCL 是接收机实现选择，协议只规定 CRC 与 Polar 编码。

## 科学定义

CA-SCL 是 SCL 加 CRC 选择器的组合。发送端把信息位连同 CRC parity bits 一起送入 Polar 编码（TS 38.212 §5.2.1）；CRC 生成多项式由 §5.1 给出：

$$g_{\mathrm{CRC11}}(D)=D^{11}+D^{10}+D^9+D^5+1 \quad (11\ \mathrm{bit})$$

$$g_{\mathrm{CRC6}}(D)=D^6+D^5+1 \quad (6\ \mathrm{bit})$$

接收端 SCL 输出 $L$ 条候选路径与路径度量（Path Metric, PM），按 PM 升序逐条做 CRC 检查，输出第一条通过 CRC 的路径。UCI 的 CRC 长度条件（TS 38.212 §6.3.1.2.1/§6.3.1.2.2）：$A\ge 20$ 附加 CRC11；$12\le A\le 19$ 附加 CRC6；$A\le 11$ 小负载不附加 CRC。DCI 使用 24 bit CRC，且 CRC parity bits 与对应无线网络临时标识（Radio Network Temporary Identifier, RNTI）相关。随机错误候选误通过 CRC 的概率量级约为 $2^{-r}$（$r$ 为 CRC 长度）。工程上 $L=8$ 时 CA-SCL 性能已接近最大似然译码。

## 直观模型

$L=8$ 的 SCL 译出 8 条候选路径：PM 最小的路径 CRC 不过，PM 第 3 小的路径 CRC 通过——此时输出第 3 条而非 PM 最小的路径。这正是 CA-SCL 的价值：PM 是软度量、可能被骗，CRC 是硬检错边界。类比：招聘海选按初试分数（PM）排名，但录用必须通过背景核查（CRC）；核查不过，分数再高也不录用，顺延到核查通过的最高分。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 最终输出就是 PM 最小的路径 | 必须过 CRC；PM 最小路径 CRC 不过时顺延到下一条通过的路径。 |
| CRC 可以替代 list size | 若正确路径在 SCL 剪枝时已被删除，CRC 检查根本看不到它。 |
| 所有控制信息都用 CRC11 | UCI 按 $A$ 条件用 6/11 bit 或不用；DCI 用 24 bit 并与 RNTI 相关。 |
| CRC 通过则一定正确 | CRC 存在误通过概率（约 $2^{-r}$），检错不是绝对零错误。 |
| CA-SCL 是 3GPP 规定的译码算法 | 协议规定 CRC 与 Polar 编码，CA-SCL 是接收机实现选择。 |

## 协议锚点

- TS 38.212 §5.1 CRC calculation（g_CRC6/g_CRC11 等）。本地：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 637-657。
- TS 38.212 §5.2.1 Polar 分段与 CRC attachment。本地：`content.md` 行 665-715。
- TS 38.212 §6.3.1.2.1（PUCCH UCI）、§6.3.2.2.1（PUSCH UCI）与 §7.3.2/§7.3.3（DCI）。本地：`content.md` 行 2325-2335、2863-2865、7177-7207。CA-SCL 算法本身为非 3GPP 标准的接收机算法。
- 讲义：`docs/L2_协议算法/T10.6_CRC_aided_SCL_control_reliability.md`；CRC 多项式家族见 `docs/L1_基础/T3.1_LTE_NR_CRC_families.md`。

## 关键要点

1. 最终输出必须过 CRC——PM 最小路径 CRC 不过时顺延到下一条通过的。
2. CRC 长度条件：UCI A≥20→CRC11、12-19→CRC6、≤11→无；DCI 24 bit 与 RNTI 相关。
3. 误通过概率约 2^-r；CRC 检错不是绝对零错误。
4. CRC 不能替代 list size——正确路径被剪枝删了就找不回来。
5. L=8 时 CA-SCL 接近最大似然译码。
6. CA-SCL 是接收机实现选择，非 3GPP 规定算法。

## 图谱关联

- [[SCL_Decoding_SCL译码]]
- [[CRC_循环冗余校验]]
- [[CRC_Polynomials_CRC生成多项式]]
- [[Polar_码]]
- [[DCI_下行控制信息]]
- [[PUCCH_上行控制信道与UCI]]
- [[概念图谱入口]]
- [[T10.6_CRC_aided_SCL_control_reliability]]
- [[T3.1_LTE_NR_CRC_families]]
- 关系语义：CA-SCL 是 NR Polar 控制信道接收端的标准译码选择方案。
