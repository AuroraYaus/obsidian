---
type: definition
aliases:
  - Chase Combining
  - CC
  - Chase合并
  - 软合并
tags:
  - 3gpp
  - concepts
  - harq
  - combining
source_spec: "TS 36.213; TS 38.214 §5.1.7"
---

# Chase Combining (CC)

Chase Combining 是最简单的 HARQ 软合并：重传使用相同 RV，接收端 LLR 直接相加。

- **实现**：LLR_new = LLR_old + LLR_retx，逐比特累加。
- **增益**：每次重传 ~3 dB 能量增益。
- **限制**：仅能量增益，无编码增益。

## 图谱关联

- [[HARQ_混合自动重传请求]]
- [[LLR_对数似然比]]
- [[Soft_Buffer_软缓存]]
- [[Incremental_Redundancy_增量冗余]]
- [[T4.3_HARQ_soft_combining_basics]]
- 关系语义：CC 是 IR 的退化情况，实现最简单。
