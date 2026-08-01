---
type: definition
aliases:
  - Soft Demodulation
  - 软解调
  - Max-Log-MAP
  - Soft Decision
tags:
  - 3gpp
  - concepts
  - channel
  - demodulation
source_spec: "TS 36.211/38.211; algorithmic receiver concept"
---

# 软解调

软解调将接收符号 y 映射为每个编码比特的 LLR，保留软信息（幅度=可信度），而非直接输出 0/1。

## 关键算法

- **硬判决**：最近星座点→比特→0/1。丢失可信度，BLER 损失 2-3 dB。
- **软判决**：输出 LLR。符号=判决，幅度=可信度。
- **Max-Log-MAP**：LLR(b_k) ≈ (min⁰||y−s||² − min¹||y−s||²) / 2σ²。QAM 标准做法。

## 图谱关联

- [[Modulation_Constellations_调制星座]]
- [[LLR_对数似然比]]
- [[T2.8_BPSK_QPSK_soft_demapping]]
- [[T2.9_QAM_Max_Log_MAP_demapping]]
- 关系语义：软解调是信道输出到译码器输入的关键转换。
