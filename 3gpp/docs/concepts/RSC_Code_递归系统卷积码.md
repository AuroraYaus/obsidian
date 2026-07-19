---
type: definition
aliases:
  - RSC
  - Recursive Systematic Convolutional Code
  - 递归系统卷积码
tags:
  - 3gpp
  - concepts
  - turbo
  - rsc
  - encoder
source_spec: "TS 36.212 §5.1.3"
---

# RSC 递归系统卷积码

RSC 码是 Turbo 码的组成编码器，含反馈回路（递归），系统位直接输出。LTE Turbo 使用两个 8-state RSC 编码器并行级联。

- **LTE RSC**：G = [1, (1+D+D³)/(1+D²+D³)]。8 状态，3 个存储单元。
- **系统位直接输出**：保证原始比特在码字中。
- **递归性**：反馈回路→更好的距离谱→Turbo 码优异性能的来源。

## 图谱关联

- [[Turbo_码]]
- [[BCJR_Algorithm_BCJR算法]]
- [[Iterative_Decoding_迭代译码]]
- [[T6.2_RSC_code_foundation]]
- [[T6.3_LTE_Turbo_encoder_trellis_termination]]
- 关系语义：RSC 是 Turbo 编码的基本单元。
