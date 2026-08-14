---
type: definition
aliases:
  - Fading Channel
  - 衰落信道
  - Rayleigh
  - Channel Estimation
tags:
  - 3gpp
  - concepts
  - channel
  - fading
source_spec: "TS 36.211/38.211 channel models"
---

# 衰落信道

## 独立解释任务

任务目标：解释多径衰落如何使接收信号幅度与相位时变，以及衰落信道下 LLR 为什么必须按信道增益缩放。在 LTE/NR 译码链路中的位置：位于空口传播与均衡之后、软解调之前——衰落决定的瞬时信道质量直接决定软解调输出 LLR 的可信度。

## 科学定义

单抽头教学模型把接收符号写成：

$$
y=h\cdot x+n
$$

其中 $x$ 为发送符号，$h$ 为复信道增益（幅度 $|h|$ 表示强弱，相位 $\theta$ 表示旋转），$n$ 为加性噪声。衰落信道（Fading Channel）指 $h$ 随时间变化的信道：瑞利衰落（Rayleigh Fading）没有占支配地位的直达路径，多条反射/散射路径相量叠加，$|h|$ 服从瑞利分布、频繁出现深衰落；莱斯衰落（Rician Fading）存在较强直达路径，包络围绕直达分量起伏。均衡（Equalization）除以 $h$ 恢复符号位置的同时把噪声放大为 $n/h$，等效噪声方差 $\sigma_{\mathrm{eq}}^2=\sigma^2/|h|^2$。对 BPSK 单抽头衰落模型，正确 LLR 为：

$$
L=\frac{2hy}{\sigma^2}
$$

与 AWGN 情形的差别是多了信道增益 $h$：信道越弱，同样的接收值对应的 LLR 幅度应越小。

## 直观模型

设 $h=0.5$、接收值 $y=0.60$、噪声方差 $\sigma^2=0.04$，逐步演算：(1) 正确公式 $L=2hy/\sigma^2=2\times0.5\times0.60/0.04=15.0$；(2) 若忽略信道增益直接用 AWGN 公式 $2y/\sigma^2$，得 $30.0$——恰好高估一倍。深衰落时偏差更大：信道越弱，均衡放大噪声越严重，朴素 LLR 越过度自信，会把"不可靠的符号"报告成"非常可靠的 0"，译码器据此错误加权导致性能恶化。对抗手段是分集（Diversity）：HARQ 重传在时间上采样不同的衰落实现，多个近似独立的衰落样本合并后深衰落的概率显著下降。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 衰落只降低信号强度 | 相位旋转同样需要均衡校正，且弱信道下均衡会放大噪声（噪声增强）。 |
| 衰落信道下 LLR 公式与 AWGN 相同 | 必须按 $h$ 缩放：$L=2hy/\sigma^2$；忽略 $h$ 在深衰落时严重过度自信。 |
| 瑞利衰落是 3GPP 规定的译码步骤 | 信道统计模型是文献/工程模型（非 3GPP 标准）；3GPP 只规定参考信号与测量入口。 |
| 深衰落无法对抗 | 时间/频率/空间分集与 HARQ 重传利用独立衰落样本降低中断概率。 |
| 译码器知道当前是瑞利还是莱斯 | 译码器只看到 LLR；信道类型通过信道估计与可靠度缩放间接体现。 |

## 协议锚点

瑞利/莱斯信道模型本身非 3GPP 标准（统计信道模型）。3GPP 相关入口（T2.15 已定位，协议不强制 LLR 公式）：
- TS 38.214 Rel-19 `38214-j30` §5.1、§5.1.6.1、§5.1.6.2（PDSCH 接收过程、信道状态信息参考信号（Channel State Information Reference Signal, CSI-RS）/解调参考信号（Demodulation Reference Signal, DM-RS）接收过程）：`3GPP_Rel19/processed/TS_38.214_38214-j30`。
- TS 38.215 Rel-19 `38215-j20` §5.1.1/§5.1.2（参考信号接收功率，Reference Signal Received Power, RSRP）、§5.1.5/§5.1.6（信干噪比，Signal-to-Interference-plus-Noise Ratio, SINR）：`3GPP_Rel19/processed/TS_38.215_38215-j20`。
- TS 38.211 Rel-19 `38211-j30`（物理信道、参考信号与资源映射背景）：`3GPP_Rel19/processed/TS_38.211_38211-j30`。

## 图谱关联

- [[AWGN_信道模型]]
- [[LLR_对数似然比]]
- [[Channel_Estimation_信道估计]]
- [[DMRS_解调参考信号]]
- [[Diversity_Combining_分集与合并]]
- [[Coherence_Bandwidth_Time_相干带宽与时间]]
- [[TDL_信道模型]]
- [[HARQ_混合自动重传请求]]
- [[T2.15_fading_channel_LLR_reliability]]
- [[概念图谱入口]]
- 关系语义：衰落信道下 LLR 可信度时变，HARQ 通过分集对抗衰落。
