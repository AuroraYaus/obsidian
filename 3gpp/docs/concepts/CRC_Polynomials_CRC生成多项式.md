---
type: definition
aliases:
  - CRC Polynomial
  - CRC多项式
  - Generator Polynomial
  - CRC24A
  - CRC24B
  - CRC24C
tags:
  - 3gpp
  - concepts
  - crc
  - polynomial
source_spec: "TS 36.212 §5.1.1; TS 38.212 §5.1"
---

# CRC 生成多项式

3GPP 定义了 7 种 CRC（循环冗余校验，Cyclic Redundancy Check）生成多项式，长度 6-24 bit，用于不同 TB（传输块，Transport Block）/CB（码块，Code Block）/控制信息场景。

| CRC | 多项式 | 用途 |
|:---|:---|:---|
| CRC24A | D²⁴+D²³+D¹⁸+D¹⁷+...+1 | LTE TB 级 |
| CRC24B | D²⁴+D²³+D⁶+D⁵+D+1 | LTE/NR CB 级 |
| CRC24C | D²⁴+D²³+D²¹+D²⁰+...+1 | NR TB 级 |
| CRC16 | D¹⁶+D¹²+D⁵+1 | LTE/NR 短 TB |
| CRC11 | D¹¹+D¹⁰+D⁹+D⁵+1 | NR Polar DCI/UCI |
| CRC8 | D⁸+D⁷+D⁴+D³+D+1 | LTE PDCCH |
| CRC6 | D⁶+D⁵+1 | NR Polar 短控制 |

## 独立解释任务

任务目标：解释 CRC 生成多项式如何决定校验余数的长度与漏检概率，以及 3GPP 为什么按场景定义多个多项式。

## 科学定义

发送端把输入比特串视为 GF(2) 多项式 $a(D)$，左移 $L$ 位后除以生成多项式 $g(D)$，把余数 $p(D)$ 附在数据之后：

$$p(D) = \left(a(D) \cdot D^{L}\right) \bmod g(D)$$

其中 $L = \deg g(D)$ 是校验比特数。例如 CRC24A 的生成多项式为 $D^{24}+D^{23}+D^{18}+D^{17}+D^{14}+D^{11}+D^{10}+D^7+D^6+D^5+D^4+D^3+D+1$，附加 24 bit 校验位。接收端对收到的完整序列再做同一次除法，余数非零即判定检出错误。

## 直观模型

生成多项式像一把"校验梳子"：非零系数（抽头）的位置决定哪些比特参与校验运算，次数 $L$ 决定校验余数的长度，也决定漏检概率的量级——随机错误图样恰好是 $g(D)$ 的倍数而被漏掉的概率约为 $2^{-L}$。数值例子：CRC24A 的 $L=24$，漏检概率约 $6\times10^{-8}$；CRC8 的 $L=8$，约 $3.9\times10^{-3}$。因此 TB 级校验用 24 bit，短控制信息用 8/11 bit 以减少开销。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 长度相同的 CRC 规则相同 | CRC24A、CRC24B、CRC24C 都是 24 bit，但抽头位置不同，校验规则完全不同。 |
| 多项式可随意更换 | 收发两端必须使用同一个生成多项式，各场景多项式由协议写死。 |
| 漏检概率恒等于 $2^{-L}$ | $2^{-L}$ 是随机错误漏检的近似上界，突发错误等特定图样下行为不同。 |
| 多项式次数决定纠错能力 | CRC 只检测不纠错，次数只决定校验长度与检测能力。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 `36212-j30` §5.1.1 CRC calculation（生成多项式家族入口）。
- LTE：TS 36.212 Rel-19 §5.1.2 Code block segmentation and code block CRC attachment。
- NR：TS 38.212 Rel-19 `38212-j30` §5.1 CRC calculation。
- NR：TS 38.212 Rel-19 §5.2 Code block segmentation and code block CRC attachment。
- 本地锚点：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`；`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md`。

## 图谱关联

- [[CRC_循环冗余校验]]
- [[GF2_Polynomials_GF2多项式]]
- [[GF2_伽罗瓦域]]
- [[TB_传输块]]
- [[CB_码块]]
- [[概念图谱入口]]
- [[T3.1_LTE_NR_CRC_families]]
- 关系语义：多项式长度决定漏检概率约 $2^{-L}$。
