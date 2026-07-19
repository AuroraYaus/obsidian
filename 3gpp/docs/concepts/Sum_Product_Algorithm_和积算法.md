---
type: definition
aliases:
  - Sum-Product Algorithm
  - SPA
  - Belief Propagation
  - 和积算法
tags:
  - 3gpp
  - concepts
  - ldpc
  - algorithm
  - spa
source_spec: "Algorithmic; TS 38.212 decoder context"
---

# 和积算法 (SPA)

SPA 是 LDPC 译码标准算法，在 Tanner 图 VN 和 CN 之间迭代传递 LLR 消息。

- **VN→CN**：L_{v→c} = L_ch + Σ_{c'≠c} L_{c'→v}。
- **CN→VN**：L_{c→v} = 2·tanh⁻¹(Π tanh(L_{v'→c}/2))。
- **复杂度**：tanh/atanh 需查表或 CORDIC。

## 图谱关联

- [[LDPC_低密度奇偶校验码]]
- [[Min_Sum_Algorithm_最小和算法]]
- [[T8.5_LDPC_sum_product_BP]]
- 关系语义：SPA 是数学最优，所有简化算法是对 SPA 的逼近。
