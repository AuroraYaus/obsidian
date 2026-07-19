---
type: definition
aliases:
  - Base Graph
  - BG
  - BG1
  - BG2
  - 基图
tags:
  - 3gpp
  - concepts
  - ldpc
  - base-graph
source_spec: "TS 38.212 §5.2.2"
---

# LDPC 基图 BG1/BG2

基图是 NR LDPC 码的模版矩阵。BG1 用于大 TB（高吞吐），BG2 用于小 TB（低延迟）。

- **BG1**：22×68，K>3824 或 R>2/3。最大 TBS ~10⁶ bits。
- **BG2**：10×42，K≤3824 且 R≤2/3。行数少→延迟低。
- **选择规则**（TS 38.212 §5.2.2）：按 TBS 和码率自动选择。

## 图谱关联

- [[LDPC_低密度奇偶校验码]]
- [[QC_LDPC_准循环LDPC]]
- [[T8.2_NR_LDPC_base_graph_selection]]
- [[T8.3_NR_LDPC_lifting_QC_matrix]]
- 关系语义：BG 决定 LDPC 码结构，Zc 提升后得完整 QC-LDPC 矩阵。
