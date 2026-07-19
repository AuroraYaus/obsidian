---
type: definition
aliases:
  - Incremental Redundancy
  - IR
  - 增量冗余
tags:
  - 3gpp
  - concepts
  - harq
  - combining
  - ir
source_spec: "TS 36.213; TS 38.214 §5.1.7"
---

# Incremental Redundancy (IR)

IR 是更高效的 HARQ 软合并：每次重传用不同 RV，发送不同校验位，等效于降低码率。

- **原理**：不同 RV→不同校验位→码率逐次降低→同时获得能量+编码增益。
- **k₀(RV)**：每个 RV 在循环缓存中定义唯一起始位置。
- **LTE [0,2,1,3]** vs **NR [0,2,3,1]**。

## 图谱关联

- [[Chase_Combining_Chase合并]]
- [[HARQ_混合自动重传请求]]
- [[RV_冗余版本]]
- [[Circular_Buffer_循环缓存]]
- [[T4.3_HARQ_soft_combining_basics]]
- [[T11.3_HARQ_soft_buffer_comparison]]
- 关系语义：IR 是 LTE/NR HARQ 标准模式，编码增益超越 CC。
