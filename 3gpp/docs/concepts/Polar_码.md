---
type: algorithm
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

Polar 码是 NR 控制信息使用的主要编码家族。接收端常用 SC、SCL 或 CA-SCL 译码，CRC 可辅助在多个候选路径中选择最终控制比特。

## 独立解释任务

任务目标：解释 Polar 如何通过信道极化、冻结位和列表路径选择保护 NR 控制信息。

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
