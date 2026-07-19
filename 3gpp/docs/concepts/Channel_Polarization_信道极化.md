---
type: definition
aliases:
  - Channel Polarization
  - 信道极化
  - Polar Transform
  - Frozen Bits
tags:
  - 3gpp
  - concepts
  - polar
  - polarization
source_spec: "Arikan 2009; TS 38.212 §5.3"
---

# 信道极化

信道极化是 Polar 码核心原理：N=2ⁿ 独立信道经 G₂⊗ⁿ 变换后，部分趋于完美（容量→1），部分趋于完全噪声（容量→0）。

- **G₂** = $\begin{bmatrix}1 & 0 \\ 1 & 1\end{bmatrix}$，N 阶 G_N = G₂^{⊗n}。
- **NR N_max**：DL=1024，UL=512。
- **好信道放信息位，差信道放冻结位（=0）**。

## 图谱关联

- [[Polar_码]]
- [[SCL_Decoding_SCL译码]]
- [[T10.2_channel_polarization_frozen_bits]]
- [[T10.3_NR_Polar_reliability_sequence]]
- 关系语义：信道极化是 Polar 码理论基石。
