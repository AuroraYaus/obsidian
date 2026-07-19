---
type: definition
aliases:
  - GF(2) Polynomial
  - GF2多项式
  - 生成多项式
  - Generator Polynomial
tags:
  - 3gpp
  - concepts
  - math
  - gf2
  - polynomial
source_spec: "TS 36.212 §5.1.1; TS 38.212 §5.1"
---

# GF(2) 多项式

GF(2) 多项式是系数在 GF(2) 上的多项式，如 g(x)=x³+x+1。二进制串与多项式系数一一对应，是 CRC 计算和 LDPC 校验矩阵的代数基础。

## 核心概念

- **系数与二进制串**：多项式 x³+x+1 ↔ 二进制串 [1, 0, 1, 1]（高位对应高次项）。
- **多项式次数 degree**：最高非零项的次数，决定 CRC 余数的最大长度。
- **不可约多项式**：类似素数，不能分解为更低次多项式的乘积。
- **生成多项式 g(x)**：CRC 的核心参数，除法求余数时作为除数。

## 图谱关联

- [[GF2_伽罗瓦域]]
- [[CRC_循环冗余校验]]
- [[CRC_Polynomials_CRC生成多项式]]
- [[T1.2_GF2_polynomials_crc_remainders]]
- 关系语义：GF(2) 多项式是 CRC 除法和 LDPC 校验矩阵构造的代数工具。
