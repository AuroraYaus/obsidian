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

## 独立解释任务

任务目标：解释加性高斯白噪声（Additive White Gaussian Noise, AWGN）模型中"加性""白""高斯"三个限定词各自的含义，并打通从 $E_b/N_0$ 到噪声方差、再到译码器输入软信息的完整换算链。在 LTE/NR 译码链路中，AWGN 位于软解调（soft demodulation）之前：接收采样经软解调与噪声缩放变成对数似然比（Log-Likelihood Ratio, LLR），噪声方差直接决定 LLR 的幅度，因此 AWGN 假设是全部块错误率（Block Error Rate, BLER）性能曲线的统一基准。

## 科学定义

AWGN 接收模型写为：

$$
y=x+n
\tag{1}
$$

其中 $x$ 是发送符号，$n$ 是噪声样本，$y$ 是接收端观测值。"加性"指噪声直接叠加在信号上；"高斯"指噪声服从均值为 0、方差为 $\sigma^2$ 的高斯分布：

$$
n\sim\mathcal{N}(0,\sigma^2)
\tag{2}
$$

"白"指不同时刻的噪声采样互不相关，每次扰动独立发生。在通信教材的常见约定下，单个实维度噪声方差为：

$$
\sigma^2=\frac{N_0}{2}
\tag{3}
$$

其中 $N_0$ 是噪声功率谱密度。复基带模型中 I/Q 两路各承担 $N_0/2$ 的方差，合成复噪声平均功率为 $N_0$。三个信噪比口径的换算关系是：每调制符号能量 $E_s$ 与每信息比特能量 $E_b$ 之间相差码率 $R$ 与调制阶数 $Q_m$ 的乘积，写成线性比值：

$$
\gamma_s=R Q_m\gamma_b
\tag{4}
$$

$\gamma_s$ 与 $\gamma_b$ 分别是 $E_s/N_0$ 与 $E_b/N_0$ 的线性形式。在归一化符号能量 $E_s=1$ 的约定下，噪声缩放公式为：

$$
\sigma^2=\frac{1}{2R Q_m\gamma_b}
\tag{5}
$$

二进制相移键控（Binary Phase Shift Keying, BPSK）在该模型下可推出最简 LLR：

$$
L(y)=\frac{2y}{\sigma^2}
\tag{6}
$$

式 (6) 的符号含义：$y>0$ 时 LLR 为正，倾向比特 `0`；噪声方差在分母，方差越大，同样的接收值给出的 LLR 幅度越小，译码器越不确定。

## 直观模型

沿用教学约定：$R=0.5$、$Q_m=1$（BPSK）、$E_b/N_0=6$ dB。第一步把 dB 转线性：$\gamma_b=10^{6/10}=10^{0.6}\approx 3.9811$。第二步代入式 (5)：$\sigma^2=1/(2\times0.5\times1\times3.9811)=0.2512$，开方得 $\sigma\approx 0.5012$。若接收采样 $y=0.7$，则 $L(y)=2\times0.7/0.2512\approx 5.5732$，正号且幅度大，说明该比特"更像 `0` 且较可靠"；若 $y=-0.2$，则 $L(y)=2\times(-0.2)/0.2512\approx -1.5924$，负号倾向 `1`，但幅度小得多，可靠度弱。这个例子演示了同一条换算链的三个环节：dB 转线性、码率与调制阶数决定噪声尺度、噪声尺度决定 LLR 的置信度。若实现误把噪声方差写成真实值的一半，LLR 幅度会整体放大 2 倍，译码器过度自信，BLER 曲线出现误差地板。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| dB 值可直接代入线性公式 | 6 dB 不等于线性 6，必须先按 $10^{\gamma_{\mathrm{dB}}/10}$ 转成线性比值。 |
| AWGN 是 3GPP 规定的真实空口信道 | AWGN 是通信理论与链路仿真基准模型，3GPP 协议不定义信道模型。 |
| 噪声方差与码率、调制阶数无关 | $\sigma^2=1/(2R Q_m\gamma_b)$，漏掉 $R$ 或 $Q_m$ 会整体缩放错误。 |
| $E_b/N_0$ 与 $E_s/N_0$ 是同一指标 | 前者归一化到每个信息比特，后者归一化到每个调制符号，相差 $R Q_m$ 倍。 |
| 复噪声每路方差应为 $N_0$ | 复基带 I/Q 每路方差是 $N_0/2$，两路合计功率才是 $N_0$。 |

## 协议锚点

- AWGN 属通信理论，非 3GPP 标准定义：TS 36.211/TS 38.211 定义调制方案和资源映射，不定义信道模型但暗含 AWGN 性能参考假设（链路级 BLER 基准惯例）。
- 调制阶数、目标码率、TBS 等上下文参数入口：TS 38.214 Rel-19 `38214-j30` §5.1.3、§5.1.3.1 与 §6.1.4、§6.1.4.1，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30/sections.jsonl`、`content.md`。
- 调制映射入口：TS 38.211 Rel-19 `38211-j30` §5.1 Modulation mapper，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30/`。
- LTE 等价锚点（TS 36.211/36.214）在讲义中标注待核验，本节不宣称已完成核验。
- 本地讲义锚点：`docs/L1_基础/T2.9_AWGN_noise_scaling.md`。

## 图谱关联

- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[Soft_Demodulation_软解调]]
- [[Fading_Channel_衰落信道]]
- [[Modulation_Constellations_调制星座]]
- [[Channel_Estimation_信道估计]]
- [[T2.9_AWGN_noise_scaling]]
- [[T2.13_BPSK_QPSK_soft_demapping]]
- [[T2.15_fading_channel_LLR_reliability]]
- 关系语义：AWGN 是译码器输入 LLR 的噪声模型基础，Eb/N0 是所有 BLER 性能曲线的横轴。
