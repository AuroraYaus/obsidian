---
type: definition
aliases:
  - 上行波形
  - DFT-s-OFDM
  - SC-FDMA
  - 离散傅里叶变换扩展正交频分复用
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §5.4/§6.3.3; TS 36.211 Rel-19 §5.6"
---

# DFT-s-OFDM 上行波形

DFT-s-OFDM（离散傅里叶变换扩展正交频分复用，Discrete Fourier Transform Spread OFDM）是 NR 上行 PUSCH（物理上行共享信道，Physical Uplink Shared Channel）的一种波形选择——先在频域做 DFT 预编码再走 OFDM 调制，本质是「单载波」传输：峰均比 PAPR（峰均功率比，Peak-to-Average Power Ratio）低，功放效率高。LTE 的 SC-FDMA（单载波频分多址，Single Carrier Frequency Division Multiple Access）是它的前身；NR 同时支持 DFT-s-OFDM 与纯 OFDM（CP-OFDM，循环前缀正交频分复用，Cyclic Prefix OFDM）两种上行波形，按场景切换。

## 独立解释任务

任务目标：讲清 DFT-s-OFDM 的原理（DFT 预编码如何把多子载波变成"等效单载波"）、低 PAPR 优势的根源、与 OFDMA（正交频分多址，Orthogonal Frequency Division Multiple Access）的对比，以及 NR 上行波形选择的配置逻辑。

## 科学定义

### 从 OFDM 到 DFT-s-OFDM

OFDM 多子载波独立调制，时域信号是多路正弦叠加——幅度起伏大（高 PAPR），功放需大回退（back-off）才能线性放大，效率低。DFT-s-OFDM 的改造：在子载波映射之前加一个 DFT（离散傅里叶变换，Discrete Fourier Transform）预编码——把时域符号块整体变换后铺到子载波上，时域波形退化为单载波样式（恒包络近似），PAPR 显著下降。

处理链：数据比特 → 调制符号 → **DFT 预编码（M 点）** → 子载波映射 → IFFT → CP（循环前缀，Cyclic Prefix）插入 → 发射。

### 低 PAPR 的根源与代价

- 根源：单载波信号时域包络近似恒定，PAPR 低（比 OFDM 低 3-6 dB 量级）——功放回退小、效率高，对 UE 电池与功放成本友好。
- 代价：频域分集下降——OFDM 一个符号的错误可以靠纠错跨子载波恢复，DFT-s-OFDM 的符号映射在频域是「展平」的，需要额外考虑（一般靠编码交织补偿）。

### 与 OFDMA 的对比（[[Multiple_Access_多址接入]] 视角）

| 维度 | OFDMA（下行为主） | DFT-s-OFDM（上行可选） |
|:---|:---|:---|
| 波形 | 多载波 | 等效单载波 |
| PAPR | 高（功放回退大） | 低（功放效率高） |
| 频域分集 | 好 | 较弱（编码补偿） |
| 接收机 | 每子载波均衡 | 需 IDFT 解预编码 |
| 使用 | NR 下行 / 上行可选 | LTE 上行 / NR 上行可选 |

### NR 上行波形配置

- NR 上行 PUSCH 由高层配置 transformPrecoding（变换预编码开关）：开 → DFT-s-OFDM，关 → CP-OFDM；PUCCH（物理上行控制信道，Physical Uplink Control Channel）format 4 也用 DFT-s-OFDM（见 [[PUCCH_上行控制信道与UCI]]）。
- LTE 上行全用 SC-FDMA（TS 36.211 §5.6），无选择。

## 直观模型

OFDM 像「多车道并排运输」：每车道（子载波）一辆车（符号），车流起伏大（高 PAPR）；DFT-s-OFDM 像「单车道列车」：货物（符号）排成一列整体出发（DFT 预编码），速度均匀、油耗低（低 PAPR、功放省电）——代价是灵活度不如多车道。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| DFT-s-OFDM 就是 OFDM 加个变换 | 变换改变了波形本质——从多载波变等效单载波，PAPR 特性完全不同 |
| SC-FDMA 与 DFT-s-OFDM 是两种技术 | 同一技术家族：LTE 称 SC-FDMA，NR 称 DFT-s-OFDM（DFT 预编码 OFDM） |
| 低 PAPR 没有代价 | 频域分集下降，靠编码/交织补偿 |
| NR 上行只用 DFT-s-OFDM | NR 上行可配 CP-OFDM（transformPrecoding 关），DFT-s-OFDM 是选项之一 |

## 协议锚点

- DFT-s-OFDM 信号生成：TS 38.211（Rel-19 j30）§5.4，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- PUSCH 物理结构：TS 38.211 §6.3.3，本地同卷。
- transformPrecoding 配置：TS 38.331（Rel-19 j20）§6.3.2（PUSCH-Config），本地 `TS_38.331_38331-j20`。
- LTE SC-FDMA：TS 36.211（Rel-19 j30）§5.6，本地 `TS_36.211_*`。
- PAPR 背景：T2.18（`docs/L1_基础/T2.18_OFDM_PAPR_power_amplifier.md`）。

## 图谱关联

- [[概念图谱入口]]
- [[T15.1_uplink_waveform_DFT_sOFDM|T15.1 上行波形讲义]]
- [[Multiple_Access_多址接入]]
- [[PUCCH_上行控制信道与UCI]]
- [[Spectrum_and_Frequency_Point_频谱与频点]]
- [[T2.18_OFDM_PAPR_power_amplifier]]
- 关系语义：DFT-s-OFDM 是上行链路的数据波形（PUSCH 选项）——与 OFDMA（下行/多址）构成波形对照，低 PAPR 特性衔接 T2.18 功放问题，PUCCH format 4 复用同一波形，是全链路「上行半边」的物理层入口。
