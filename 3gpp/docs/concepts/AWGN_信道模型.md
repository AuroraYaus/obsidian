---
type: definition
aliases:
  - AWGN
  - Additive White Gaussian Noise
  - 加性高斯白噪声
  - 噪声方差
  - Eb/N0
tags:
  - 3gpp
  - concepts
  - channel
  - awgn
source_spec: "Communication theory; TS 36.211/38.211 modulation and channel anchors"
---

# AWGN 加性高斯白噪声

AWGN 信道模型是最基本的通信信道：接收信号 y = x + n，其中 n ~ N(0, σ²) 是独立同分布的高斯噪声。所有 LTE/NR 译码器的 BER/BLER 性能基准都在 AWGN 假设下定义。

## 核心子概念

- **噪声方差 σ² = N₀/2**：噪声功率谱密度决定接收信号质量。
- **Eb/N0**：每信息比特能量与噪声谱密度之比，是译码性能的标准度量。与 SNR 的关系取决于调制阶数和码率。
- **Es/N0 = R · Eb/N0**：每符号能量，R 为码率。
- **噪声缩放系数 2/σ²**：将接收信号 y 转换为译码器输入的 LLR 时需要乘以该系数。BPSK 下 LLR = 2y/σ²。

## 协议锚点

- 调制与物理信道：TS 36.211/TS 38.211 定义调制方案和资源映射，不定义信道模型但暗含 AWGN 性能参考假设。
- 本地锚点：`docs/L1/T2.7_AWGN_noise_scaling.md`

## 图谱关联

- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[T2.7_AWGN_noise_scaling]]
- [[T2.8_BPSK_QPSK_soft_demapping]]
- [[T2.10_fading_channel_LLR_reliability]]
- 关系语义：AWGN 是译码器输入 LLR 的噪声模型基础，Eb/N0 是所有 BLER 性能曲线的横轴。
