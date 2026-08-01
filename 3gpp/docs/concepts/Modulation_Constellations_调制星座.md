---
type: definition
aliases:
  - Modulation
  - Constellation
  - BPSK
  - QPSK
  - QAM
  - Gray Mapping
tags:
  - 3gpp
  - concepts
  - channel
  - modulation
source_spec: "TS 36.211 §7.1; TS 38.211 §5.1"
---

# 调制星座

调制星座将比特组映射为复基带符号。LTE/NR 支持 BPSK、QPSK、16QAM、64QAM 和 256QAM（NR DL 最高），使用格雷映射使相邻星座点仅差 1 bit。

## 星座类型

- **BPSK**：1 bit/sym，星座点 ±1。LLR = 2y/σ²。
- **QPSK**：2 bit/sym，格雷映射，可视为两路独立 BPSK。
- **16QAM**：4 bit/sym，十字星座。需 Max-Log-MAP 近似。
- **64QAM**：6 bit/sym，NR 最常用数据调制。
- **256QAM**：8 bit/sym，NR DL 最高阶。

## 图谱关联

- [[AWGN_信道模型]]
- [[LLR_对数似然比]]
- [[Soft_Demodulation_软解调]]
- [[T2.8_BPSK_QPSK_soft_demapping]]
- [[T2.9_QAM_Max_Log_MAP_demapping]]
- 关系语义：调制星座决定软解调算法和 LLR 质量。
