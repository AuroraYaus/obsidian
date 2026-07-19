---
type: definition
aliases:
  - Min-Sum
  - MS
  - NMS
  - OMS
  - Normalized Min-Sum
  - Offset Min-Sum
tags:
  - 3gpp
  - concepts
  - ldpc
  - algorithm
  - min-sum
source_spec: "Algorithmic; hardware implementation of LDPC decoding"
---

# Min-Sum 及其变体

Min-Sum 是 SPA 的硬件友好简化：CN 更新用 min 替代 tanh/atanh。

- **MS**：L = Π sign · min|L|。高估可靠度 1-3 dB。
- **NMS**：L = α · Π sign · min|L|，α≈0.75-0.85。乘法修正。
- **OMS**：L = Π sign · max(min|L|−β, 0)，β≈0.5。减法修正，最硬件友好。
- **性能损失**：NMS/OMS ~0.1-0.3 dB vs SPA。

## 图谱关联

- [[Sum_Product_Algorithm_和积算法]]
- [[LDPC_低密度奇偶校验码]]
- [[T8.6_LDPC_MS_NMS_OMS]]
- 关系语义：MS 族是 LDPC 硬件译码主流选择。
