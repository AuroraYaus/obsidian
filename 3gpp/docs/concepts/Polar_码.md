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

Polar 码是 NR 控制信息使用的主要编码家族。接收端常用 SC、SCL 或 CA-SCL 译码，CRC 可辅助在多个候选路径中选择最终控制比特。一句话本质：**Polar 是"快慢车道改造"——把普通信道改造成可靠与不可靠分明的车道，可靠车道放信息、不可靠车道放约定冻结位，译码时用列表 + CRC 门禁选路径**。

## 独立解释任务

任务目标：解释 Polar 如何通过信道极化、冻结位和列表路径选择保护 NR 控制信息。

## 起源与演进

(1) **起点：2009 年 Arikan 的构造性突破。** Arikan 证明 Polar 是第一个被严格证明可达信道容量（二进制对称信道）的码——靠的是信道极化：N 个相同信道经变换后可靠性向两端分化（见 [[Channel_Polarization_信道极化]]）。

(2) **结构：快慢车道。** 信息位放可靠位置、冻结位（收发双方约定 0）放不可靠位置——编码只需一次 GF(2) 变换，简单到可以严格分析。

(3) **译码演进：SC → SCL → CA-SCL。** SC 逐位贪心译码，早期误判无法挽回；SCL 同时保留 L 条候选路径；CA-SCL 再用 CRC 在候选里选最终路径——"列表扩大 + CRC 门禁"是 Polar 实用可靠性的关键。

(4) **NR 的定位。** 控制信息（DCI/UCI）用 Polar——短块、高可靠、无迭代译码，正好匹配 Polar 特性；数据信道用 LDPC，Turbo 留在 LTE。

(5) **边界。** CRC 主要用于路径选择与验收，纠错来自 Polar 结构本身；列表越大性能越好，但面积、功耗、时延线性上涨。

## 科学定义

Polar 码基于信道极化：经过特定变换后，一部分 bit-channel 变得更可靠，另一部分变得更不可靠。发送端把信息 bit 放在可靠位置，把冻结位固定在不可靠位置。接收端按 SC、SCL 或 CA-SCL 规则逐位恢复候选路径。

## 直观模型

Polar 码像把一条普通道路改造成快慢车道。可靠车道放真实信息，不可靠车道放已知冻结位。SCL 译码会同时保留多条可能路径，CRC 像最后的门禁，帮助选择可信路径。

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
5. frozen bit 是编码结构固定位，不是 filler；CRC 是路径门禁不是纠错本体。
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
