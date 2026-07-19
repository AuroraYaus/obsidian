---
type: definition
aliases:
  - GF(2)
  - Galois Field 2
  - 伽罗瓦域
  - 二元域
  - GF2
tags:
  - 3gpp
  - concepts
  - math
  - gf2
source_spec: "Mathematical foundation; TS 36.212/38.212 CRC polynomial context"
---

# GF(2) 伽罗瓦域

GF(2) 是只含 {0, 1} 两个元素的有限域。加法为 XOR（模2加），乘法为 AND（模2乘）。所有 CRC 计算、LDPC 校验矩阵和 Polar 极化变换都基于 GF(2) 运算。

## 核心子概念

- **GF(2) 加法**：0⊕0=0, 0⊕1=1, 1⊕0=1, 1⊕1=0。等价于 XOR，是线性分组码的基本运算。
- **GF(2) 乘法**：0·0=0, 0·1=0, 1·0=0, 1·1=1。等价于 AND。
- **GF(2) 多项式**：系数在 GF(2) 上的多项式，如 g(x)=x³+x+1。二进制串与多项式系数一一对应。
- **GF(2) 多项式除法**：长除法求余数，是 CRC 计算的核心。可用 LFSR（线性反馈移位寄存器）硬件实现。
- **GF(2) 向量与矩阵**：向量空间、生成矩阵 G（编码）、校验矩阵 H（满足 GHᵀ=0）、校验子 s=rHᵀ（错误检测）。

## 协议锚点

- CRC：TS 36.212/38.212 的 CRC 计算基于 GF(2) 多项式除法。
- LDPC：TS 38.212 的基图（Base Graph）和提升（Lifting）在 GF(2) 上定义 QC-LDPC 校验矩阵。
- Polar：信道极化变换在 GF(2) 上进行。

## 图谱关联

- [[概念图谱入口]]
- [[CRC_循环冗余校验]]
- [[LDPC_低密度奇偶校验码]]
- [[Polar_码]]
- [[T1.1_GF2_binary_arithmetic_for_decoders]]
- [[T1.2_GF2_polynomials_crc_remainders]]
- [[T1.3_GF2_vectors_matrices]]
- 关系语义：GF(2) 是 CRC、LDPC、Polar 的底层代数结构，所有线性校验和极化运算都在 GF(2) 上定义。
