---
type: definition
aliases:
  - Polar
  - Polar Code
  - 极化码
  - NR Polar
  - CA-SCL
tags:
  - 3gpp
  - concepts
  - polar
source_spec: "TS 38.212 Rel-19 §5.2.1, §5.3.1, §5.4.1, §6.3, §7.3"
---

# Polar 码

## 符号与记号约定

本笔记以文字与表格描述机制，不引入 LaTeX 数学公式；文中涉及的带宽、数量与码率等量均以文字就地说明其含义与来源，无需符号表。

Polar 码是 NR 控制信息使用的主要编码家族。接收端常用 SC、SCL 或 CA-SCL 译码，CRC 可辅助在多个候选路径中选择最终控制比特。一句话本质：**Polar 通过极化把一组子信道分成可靠与不可靠两类，信息位放在可靠位置、冻结位放在不可靠位置；译码用列表保留多条候选路径，再由 CRC 在候选中筛选**。

## 解释目标与范围

本节目标：解释 Polar 如何通过信道极化、冻结位和列表路径选择保护 NR 控制信息。

## 前置概念

信道极化。把若干相同的二进制输入信道经线性变换组合，可使一部分子信道的容量趋近于一、另一部分趋近于零，见 [[Channel_Polarization_信道极化]]。Polar 码正是利用这种分化，把信息放在可靠子信道上。

线性分组码与生成矩阵。Polar 码是模 2 线性分组码，编码可写成信息比特与生成矩阵的乘积，见 [[GF2_伽罗瓦域]]。冻结位是收发双方约定的固定比特，不携带信息，只参与构造码字。

串行抵消译码与 CRC 辅助。串行抵消译码按位依次判决，早期误判无法挽回；列表译码同时保留多条候选路径，CRC 再在候选中筛选，见 [[SCL_Decoding_SCL译码]] 与 [[CA_SCL_CRC辅助SCL]]。列表长度与 CRC 长度共同决定性能与实现代价。

## 起源与演进

(1) **起点：2009 年 Arikan 的构造性突破。** Arikan 证明 Polar 是第一个被严格证明可达信道容量（二进制对称信道）的码——靠的是信道极化：N 个相同信道经变换后可靠性向两端分化（见 [[Channel_Polarization_信道极化]]）。

(2) **结构：按可靠度分配位置。** 信息位放在可靠度高的位置、冻结位（收发双方约定为 0）放在可靠度低的位置——编码只需一次 GF(2) 线性变换，结构简单到可以严格分析。

(3) **译码演进：SC → SCL → CA-SCL。** SC 逐位贪心译码，早期误判无法挽回；SCL 同时保留 L 条候选路径；CA-SCL 再用 CRC 在候选里选最终路径——列表保留多条候选、CRC 做筛选，是 Polar 实用可靠性的关键。

(4) **NR 的定位。** 控制信息（DCI/UCI）用 Polar——短块、高可靠、无迭代译码，正好匹配 Polar 特性；数据信道用 LDPC，Turbo 留在 LTE。

(5) **边界。** CRC 主要用于路径选择与验收，纠错来自 Polar 结构本身；列表越大性能越好，但面积、功耗、时延线性上涨。

## 科学定义

Polar 码基于信道极化：经过特定变换后，一部分 bit-channel 变得更可靠，另一部分变得更不可靠。发送端把信息 bit 放在可靠位置，把冻结位固定在不可靠位置。接收端按 SC、SCL 或 CA-SCL 规则逐位恢复候选路径。

## 直观模型

极化把一组子信道分成可靠与不可靠两类：可靠位置承载真实信息，不可靠位置承载收发双方约定的冻结位。串行抵消列表译码会同时保留若干条候选路径，路径度量随译码推进而更新；附加的 CRC 用于在这些候选路径中筛选，只有通过校验的路径才被采纳。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| Polar 只靠 CRC 纠错 | CRC 主要用于候选路径选择和验收，纠错来自 Polar 结构和搜索。 |
| frozen bit 是 filler | frozen bit 是编码结构中的固定已知位，不等于分段 filler。 |
| SCL 列表越大一定越好 | 列表大小提高性能但增加面积、功耗和时延。 |

## 协议锚点

- NR：TS 38.212 Rel-19 §5.2.1 Polar segmentation and CRC。
- NR：TS 38.212 Rel-19 §5.3.1 Polar coding。
- NR：TS 38.212 Rel-19 §5.4.1 Polar rate matching。
- NR：TS 38.212 Rel-19 §6.3 UCI；§7.3 DCI。

## 关键要点

1. Polar 是首个被证明可达容量的码（Arikan 2009）——NR 控制信道主力。
2. 结构：信息位放可靠位置、冻结位放不可靠位置（收发约定 0）。
3. 译码演进：SC（贪心）→ SCL（保留 L 条路径）→ CA-SCL（CRC 选路径）。
4. NR 分工：Polar 管控制、LDPC 管数据、Turbo 留 LTE。
5. frozen bit 是编码结构固定位，不是 filler；CRC 用于在候选路径中筛选，不是纠错本体。
6. 列表越大性能越好，代价是面积/功耗/时延。

## 图谱关联

- [[Channel_Polarization_信道极化]]
- [[SCL_Decoding_SCL译码]]
- [[CA_SCL_CRC辅助SCL]]
- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[CRC_循环冗余校验]]
- [[Rate_Matching_速率匹配]]
- [[Early_Stopping_早停控制]]
- [[T10.1_NR_Polar_decoder_chain_overview]]
- [[T10.5_Polar_SCL_decoding]]
- [[T10.6_CRC_aided_SCL_control_reliability]]
- 关系语义：Polar 码用 LLR 和 rate recovery 构造候选路径，CRC 在 CA-SCL 中承担路径选择和可靠性门控。
