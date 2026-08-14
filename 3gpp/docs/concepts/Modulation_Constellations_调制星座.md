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

调制星座将比特组映射为复基带符号。LTE/NR 支持 BPSK（二进制相移键控，Binary Phase Shift Keying）、QPSK（正交相移键控，Quadrature Phase Shift Keying）、16QAM、64QAM 和 256QAM（正交幅度调制，Quadrature Amplitude Modulation, QAM；NR 下行最高阶），使用格雷映射（Gray Mapping）使相邻星座点仅差 1 bit。

## 独立解释任务

任务目标：解释各阶星座的结构与能量归一化，以及星座几何如何决定软解调 LLR 的计算方式。

## 科学定义

$M$-QAM 把 $m=\log_2 M$ 个比特映射为一个复符号 $s$，星座点归一化后平均能量为 1。16QAM 的 I/Q 坐标取 $\{\pm1/\sqrt{10},\ \pm3/\sqrt{10}\}$，因为未归一化坐标 $\{\pm1,\pm3\}$ 的平均能量为 $(4\times2+8\times10+4\times18)/16=10$。接收端软解调由 Max-Log-MAP 近似给出逐比特 LLR：

$$L(b_k) \approx \frac{1}{\sigma^2}\left( \min_{s:\; b_k=0} |y-s|^2 - \min_{s:\; b_k=1} |y-s|^2 \right)$$

其中 $y$ 为接收符号，$\sigma^2$ 为噪声功率，$b_k$ 为符号携带的第 $k$ 个比特，两个最小化分别在 $b_k=0$ 与 $b_k=1$ 的星座子集上进行；BPSK 特例退化为 $L = 2y/\sigma^2$。

## 星座类型

- **BPSK**：1 bit/sym，星座点 ±1。LLR = 2y/σ²。
- **QPSK**：2 bit/sym，格雷映射，可视为两路独立 BPSK。
- **16QAM**：4 bit/sym，十字星座。需 Max-Log-MAP 近似。
- **64QAM**：6 bit/sym，NR 最常用数据调制。
- **256QAM**：8 bit/sym，NR DL 最高阶。

## 直观模型

星座像城市地图上的规则格点，格雷编码让相邻"门牌"只差一位数字：噪声把符号推到相邻格点时最多只错 1 个比特。数值例子：QPSK 的四个点落在 $(\pm1\pm j)/\sqrt{2}$，接收符号 $y=0.9+0.8j$ 最接近 $(1+j)/\sqrt{2}\approx0.71+0.71j$，判决为该点即可正确恢复 2 个比特；若同一噪声幅度作用于 16QAM，符号可能被推到相邻格点，但格雷映射保证只错 1 bit。星座阶数越高格点越密，同样噪声下越容易越界，因此高阶调制需要更高的信噪比（Signal-to-Noise Ratio, SNR）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 星座阶数越高越好 | 阶数提高频谱效率，但格点间距变小，相同 SNR 下误码率升高。 |
| 格雷映射消除误码 | 格雷映射只保证相邻点错误时仅错 1 bit，不能消除符号错误本身。 |
| 16QAM 可与 QPSK 一样拆成两路独立 BPSK | 16QAM 及以上 I/Q 不再独立，LLR 需在星座子集上求最小距离。 |
| $L=2y/\sigma^2$ 对所有调制通用 | 该式只对 BPSK 成立，QAM 需按 Max-Log-MAP 分集计算。 |

## 协议锚点

- LTE：TS 36.211 Rel-19 `36211-j30_s06-s08` §7.1.1 BPSK、§7.1.2 QPSK、§7.1.3 16QAM、§7.1.4 64QAM、§7.1.5 256QAM。
- NR：TS 38.211 Rel-19 `38211-j30` §5.1.2 BPSK、§5.1.3 QPSK、§5.1.4 16QAM、§5.1.5 64QAM、§5.1.6 256QAM。
- 本地锚点：`3GPP_Rel19/processed/TS_36.211_36211-j30_s06-s08/sections.jsonl`、`content.md`；`3GPP_Rel19/processed/TS_38.211_38211-j30/sections.jsonl`、`content.md`。

## 图谱关联

- [[AWGN_信道模型]]
- [[LLR_对数似然比]]
- [[Soft_Demodulation_软解调]]
- [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]
- [[Modulation_Mapping_调制映射]]
- [[概念图谱入口]]
- [[T2.13_BPSK_QPSK_soft_demapping]]
- [[T2.14_QAM_Max_Log_MAP_demapping]]
- 关系语义：调制星座决定软解调算法和 LLR 质量。
