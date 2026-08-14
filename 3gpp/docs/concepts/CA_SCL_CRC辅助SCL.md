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

## 独立解释任务

任务目标：解释循环冗余校验辅助逐次消除列表译码（CRC-aided Successive Cancellation List, CA-SCL）如何用 CRC 从 SCL 候选路径中选出最终输出，以及 NR 控制信道 CRC 长度的协议条件与 DCI 的 RNTI 边界。

CA-SCL 是 NR Polar 控制信道接收链的最后一级：位于 SCL 树译码之后、控制比特交付之前，承担候选路径的最终选择。

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
