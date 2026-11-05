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

CRC 是错误检测机制。发送端按生成多项式给比特串附加校验余数，接收端用同一规则复核；余数通过表示“未检测到错误”，不表示绝对无错，也不负责纠错。一句话本质：**CRC 是"封条"不是"修补匠"——只负责验收说"对/错"，纠错交给信道码**。

## 独立解释任务

任务目标：解释 CRC 为什么是验收边界，而不是纠错算法。

## 起源与演进

(1) **起点：信道会引入错误，接收端需要验收边界。** 无线信道必然使比特翻转，接收端译码后必须回答"这包对不对"。CRC 是最通用的检测工具：把整串比特看作 GF(2) 上的多项式，除以约定的生成多项式取余数——发送端附上余数，接收端用同一规则复核，余数对不上即判错。

(2) **为什么只检测不纠错。** 纠错是信道码（Turbo/LDPC/Polar）的职责，CRC 的职责是在正确的位置"说停/说错"：实现只是一条移位寄存器异或链，成本极低，一个多项式通吃任意长度——这是它能铺满协议各层的原因。

(3) **协议里的三层封条。** 3GPP 在三个层面部署 CRC：TB CRC（24 bit，整包验收，直接驱动 HARQ 的 ACK/NACK）、CB CRC（每个码块分包验收，兼作译码早停判据）、控制信息 CRC（NR 24 bit / LTE 16 bit，且用 RNTI 加扰兼作"收件人身份"）。

(4) **边界与盲区。** CRC pass 不等于绝对正确——长度为 L 的 CRC 漏检概率约为 $2^{-L}$；所有 CB CRC 全过仍可能在拼接、filler 或顺序处理处出错，所以 TB CRC 不可省。NR 的大 TB 还额外附加 16 bit 第二 CRC 降低漏检。

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
- 本地锚点示例：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`；`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md`。

## 关键要点

1. CRC 是检测不是纠错——纠错是信道码（Turbo/LDPC/Polar）的活。
2. 机制：GF(2) 多项式除法，发送附余数、接收复核；实现为移位寄存器异或链。
3. 协议三层封条：TB CRC（24 bit，ACK/NACK 依据）、CB CRC（早停）、控制 CRC（RNTI 加扰兼身份）。
4. CRC pass 有漏检概率（约 $2^{-L}$），不表示绝对正确。
5. CB CRC 替代不了 TB CRC——拼接/filler/顺序错误只有整块复核能抓。
6. NR 大 TB 再挂 16 bit 附加 CRC 降低漏检。

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
