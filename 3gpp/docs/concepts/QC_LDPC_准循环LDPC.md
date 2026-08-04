---
type: definition
aliases:
  - QC-LDPC
  - Quasi-Cyclic LDPC
  - Lifting Size
  - Zc
  - 循环移位
tags:
  - 3gpp
  - concepts
  - ldpc
  - qc-ldpc
  - lifting
source_spec: "TS 38.212 §5.2.2"
---

# QC-LDPC 与提升大小 Zc

QC-LDPC 是 NR LDPC 实现形式：基图元素→Zc×Zc 循环移位子矩阵。硬件友好。

- **Zc**：∈ {2,3,...,384}，8 组提升值集合（i_LS=0..7）。
- **循环移位**：P_ij→Zc×Zc 单位阵循环右移 P_ij 位。P_ij=0→单位阵，P_ij=−1→全零阵。
- **码长 N**：22·Zc (BG1) 或 10·Zc (BG2)，减去打孔的 2Zc。

## 图谱关联

- [[Base_Graph_基图]]
- [[LDPC_低密度奇偶校验码]]
- [[T8.3_NR_LDPC_lifting_QC_matrix]]
- [[T19.2_NR_LDPC_RTL_microarchitecture]]
- 关系语义：Zc 提升决定码长、校验矩阵尺寸和硬件并行度。
