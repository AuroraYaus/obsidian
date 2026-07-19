---
type: definition
aliases:
  - SIMD
  - Memory Layout
  - Cache-Friendly
  - SoA
tags:
  - 3gpp
  - concepts
  - implementation
  - simd
  - optimization
source_spec: "Engineering methodology; C/C++ implementation"
---

# SIMD 与内存布局

SIMD 一条指令同时处理多数据。译码器 CN/VN 并行更新天然适合 SIMD。

- **宽度**：SSE 128bit / AVX2 256bit / AVX-512 512bit。
- **int8 vs int16**：int8 吞吐翻倍有精度损失，int16 平衡。
- **SoA > AoS**：逐层连续存储→缓存友好。
- **对齐**：16/32/64 字节对齐 + padding。

## 图谱关联

- [[Fixed_Point_Numbers_定点数]]
- [[RTL_Microarchitecture_RTL微架构]]
- [[T13.5_SIMD_memory_layout_decoders]]
- 关系语义：SIMD 优化决定定点模型实际吞吐。
