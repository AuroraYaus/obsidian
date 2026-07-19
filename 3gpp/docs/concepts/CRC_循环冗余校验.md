---
type: definition
aliases:
  - CRC
  - Cyclic Redundancy Check
  - 循环冗余校验
  - TB CRC
  - CB CRC
tags:
  - 3gpp
  - concepts
  - crc
source_spec: "TS 36.212 Rel-19 §5.1.1; TS 38.212 Rel-19 §5.1"
---

# CRC 循环冗余校验

CRC 是错误检测机制。发送端按生成多项式给比特串附加校验余数，接收端用同一规则复核；余数通过表示“未检测到错误”，不表示绝对无错，也不负责纠错。

## 独立解释任务

任务目标：解释 CRC 为什么是验收边界，而不是纠错算法。

## 科学定义

CRC 把一串 bit 看成 GF(2) 多项式，并用约定的生成多项式计算余数。发送端把余数附加到 payload 或控制信息后面，使完整比特串满足“被生成多项式整除”的规则。接收端重新做同一检查，余数不满足规则时判定错误。

## 直观模型

CRC 像包裹封条。封条完整不能证明包裹绝对没问题，但封条对不上时可以快速拒收。TB CRC 是整包封条，CB CRC 是分包封条，控制信息 CRC 是控制候选是否可信的封条。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CRC 能纠错 | CRC 只检测，不定位也不修正错误。 |
| CRC pass 等于绝对正确 | CRC 有漏检概率，只能说未检测到错误。 |
| CB CRC 可以替代 TB CRC | CB 局部通过后仍可能在拼接、filler 或顺序处理处出错。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 `36212-j30` §5.1.1 CRC calculation。
- LTE：TS 36.212 Rel-19 §5.1.2 Code block segmentation and code block CRC attachment。
- NR：TS 38.212 Rel-19 `38212-j30` §5.1 CRC calculation。
- NR：TS 38.212 Rel-19 §5.2 Code block segmentation and code block CRC attachment。
- 本地锚点示例：`3GPP_Rel19/processed/TS_36.212_36212-j30/TS_36.212_36212-j30_content.md`；`3GPP_Rel19/processed/TS_38.212_38212-j30/TS_38.212_38212-j30_content.md`。

## 图谱关联

- [[CRC_Polynomials_CRC生成多项式]]
- [[GF2_伽罗瓦域]]
- [[GF2_Polynomials_GF2多项式]]
- [[概念图谱入口]]
- [[TB_传输块]]
- [[CB_码块]]
- [[HARQ_混合自动重传请求]]
- [[Polar_码]]
- [[Early_Stopping_早停控制]]
- [[T3.1_LTE_NR_CRC_families]]
- [[T4.4_early_stopping_crc_gated_control]]
- 关系语义：CRC 定义 TB/CB/control candidate 的错误检测边界，并驱动 HARQ ACK/NACK 或 Polar CA-SCL 路径选择。
