---
type: definition
aliases:
  - BCJR
  - MAP Decoding
  - Forward-Backward Algorithm
  - Log-MAP
  - Max-Log-MAP
tags:
  - 3gpp
  - concepts
  - turbo
  - bcjr
  - algorithm
source_spec: "Bahl-Cocke-Jelinek-Raviv 1974; TS 36.212 algorithmic context"
---

# BCJR / MAP 译码算法

BCJR 是最优逐比特 MAP 译码算法，在网格图上运行前向 α 和后向 β 递归。

- **γ 分支度量**：从 LLR 计算状态转移概率。
- **α 前向递归**：α(s) = Σ α(s')·γ(s'→s)。
- **β 后向递归**：β(s) = Σ β(s')·γ(s→s')。
- **Log-MAP**：log 域计算，max*(a,b)=max+log(1+e^(−|a−b|))，精确。
- **Max-Log-MAP**：max* ≈ max，次优 ~0.5dB 但只需比较和加法。

## 图谱关联

- [[RSC_Code_递归系统卷积码]]
- [[Iterative_Decoding_迭代译码]]
- [[T6.5_BCJR_MAP_decoding_intuition]]
- [[T6.6_Log_MAP_Max_Log_MAP_Turbo]]
- 关系语义：BCJR 是 Turbo 译码的核心引擎。
