---
type: definition
aliases:
  - Fixed-Point
  - 定点数
  - Q-format
  - 2s Complement
tags:
  - 3gpp
  - concepts
  - implementation
  - fixed-point
source_spec: "Engineering methodology; TS 36.212/38.212 decoder requirements"
---

# 定点数表示

定点数用固定位宽整数表示实数，是硬件实现基础。Qm.n 格式决定动态范围和精度。

- **Qm.n**：m 位整数+n 位小数+1 位符号。动态范围 ≈ 6m dB，精度 ε = 2^(−n)。
- **2's Complement**：−x = ~x + 1，统一加减法。
- **LLR 位宽**：4bit(粗~0.3dB)/5bit(平衡~0.1dB)/6bit(精细~0.05dB)。

## 图谱关联

- [[LLR_对数似然比]]
- [[LLR_Quantization_LLR量化]]
- [[T5.1_fixed_point_numbers_for_LLR]]
- [[T13.1_fixed_point_decoder_requirements]]
- 关系语义：定点数是浮点算法到硬件整数运算的桥梁。
