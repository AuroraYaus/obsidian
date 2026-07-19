---
type: definition
aliases:
  - Layered Decoding
  - 分层译码
  - Flooding
  - Row-Layered
tags:
  - 3gpp
  - concepts
  - ldpc
  - algorithm
  - schedule
source_spec: "Algorithmic; hardware implementation of LDPC decoding"
---

# LDPC 分层译码调度

分层调度逐行更新 CN/VN，后一层立即可用前一层结果，收敛速度 ~2× Flooding。

- **Flooding**：全 CN 并行→全 VN 并行。需两套消息存储。
- **Layered**：逐行 CN→立即更新该行 VN→下一行。收敛快 2×。
- **代价**：顺序限制并行度，但每层内仍可并行。

## 图谱关联

- [[Sum_Product_Algorithm_和积算法]]
- [[Min_Sum_Algorithm_最小和算法]]
- [[T8.7_layered_LDPC_decoding_schedule]]
- [[T14.2_NR_LDPC_RTL_microarchitecture]]
- 关系语义：分层调度是 LDPC 硬件关键优化。
