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

3GPP 定义了 7 种 CRC 生成多项式，长度 6-24 bit，用于不同 TB/CB/控制信息场景。

| CRC | 多项式 | 用途 |
|:---|:---|:---|
| CRC24A | D²⁴+D²³+D¹⁸+D¹⁷+...+1 | LTE TB 级 |
| CRC24B | D²⁴+D²³+D⁶+D⁵+D+1 | LTE/NR CB 级 |
| CRC24C | D²⁴+D²³+D²¹+D²⁰+...+1 | NR TB 级 |
| CRC16 | D¹⁶+D¹²+D⁵+1 | LTE/NR 短 TB |
| CRC11 | D¹¹+D¹⁰+D⁹+D⁵+1 | NR Polar DCI/UCI |
| CRC8 | D⁸+D⁷+D⁴+D³+D+1 | LTE PDCCH |
| CRC6 | D⁶+D⁵+1 | NR Polar 短控制 |

## 图谱关联

- [[CRC_循环冗余校验]]
- [[GF2_Polynomials_GF2多项式]]
- [[T3.1_LTE_NR_CRC_families]]
- 关系语义：多项式长度决定漏检概率 ≈ 2^(−L)。
