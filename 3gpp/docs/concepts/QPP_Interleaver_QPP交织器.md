---
type: definition
aliases:
  - QPP
  - Quadratic Permutation Polynomial
  - QPP交织器
  - Turbo Internal Interleaver
tags:
  - 3gpp
  - concepts
  - turbo
  - interleaver
  - qpp
source_spec: "TS 36.212 §5.1.3-2"
---

# QPP 内部交织器

QPP（二次置换多项式）交织器是 LTE Turbo 编码器的内部交织器：Π(i) = (f₁·i + f₂·i²) mod K。

- **无冲突特性**：支持并行 Turbo 译码，多 SISO 同时读取不冲突。
- **f₁, f₂**：3GPP 为每个有效 K（≤6144）预定义最优参数对。
- **打散突发错误**：使两个 RSC 编码器看到近似独立的输入。

## 图谱关联

- [[RSC_Code_递归系统卷积码]]
- [[Iterative_Decoding_迭代译码]]
- [[T6.4_LTE_Turbo_internal_interleaver]]
- 关系语义：QPP 交织是 Turbo 接近香农限的关键设计。
