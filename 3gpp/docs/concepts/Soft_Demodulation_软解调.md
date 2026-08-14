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

## 独立解释任务

任务目标：解释软解调（Soft Demodulation）如何把接收符号 $y$ 换算成每个编码比特的 LLR，并说明 Max-Log-MAP 近似如何以最小距离搜索替代指数求和。在 LTE/NR 译码链路中的位置：位于均衡器之后、信道译码器之前，输出译码器直接消费的 LLR 流。

## 科学定义

硬判决（Hard Decision）只输出最近星座点对应的比特 0/1，丢弃可信度信息；软判决（Soft Decision）输出对数似然比（Log-Likelihood Ratio, LLR）：符号是判决、幅度是可信度。二进制相移键控（Binary Phase Shift Keying, BPSK）教学映射 $0\to+1$、$1\to-1$（正 LLR 表示更像 0），有闭式解：

$$
L(y)=\frac{2y}{\sigma^2}
$$

其中 $y$ 为接收值、$\sigma^2$ 为噪声方差。正交相移键控（Quadrature Phase Shift Keying, QPSK）I/Q 两路独立，每符号产生两个 LLR，决策边界为 $y_I=0$ 与 $y_Q=0$。正交幅度调制（Quadrature Amplitude Modulation, QAM）的精确逐比特 LLR 需对两组候选点求和：

$$
L_k(y)=\ln\frac{\sum_{s\in\mathcal{S}_{k,0}}\exp\left(-\frac{|y-s|^2}{2\sigma^2}\right)}{\sum_{s\in\mathcal{S}_{k,1}}\exp\left(-\frac{|y-s|^2}{2\sigma^2}\right)}
$$

其中 $\mathcal{S}_{k,0}$、$\mathcal{S}_{k,1}$ 分别是第 $k$ 个比特为 0、1 的星座点子集。用 $\ln\sum_i e^{z_i}\approx\max_i z_i$ 近似即得 Max-Log-MAP 形式：

$$
L_k(y)\approx\frac{1}{2\sigma^2}\left(\min_{s\in\mathcal{S}_{k,1}}|y-s|^2-\min_{s\in\mathcal{S}_{k,0}}|y-s|^2\right)
$$

## 直观模型

归一化 QPSK 星座每维幅度 $1/\sqrt{2}$，设 $\sigma^2=0.25$、接收样本 $y=0.45-0.20j$，逐步演算：(1) 硬判决：$y_I=0.45>0$ 且 $y_Q=-0.20<0$，落在 `01` 象限，输出 `01`；(2) 逐比特 LLR：$L_0=\sqrt{2}\times0.45/0.25=2.5456$，$L_1=\sqrt{2}\times(-0.20)/0.25=-1.1314$。$L_0>0$ 判 $b_0=0$、$L_1<0$ 判 $b_1=1$，与硬判决一致；$|L_0|>|L_1|$ 说明 $b_0$ 更可靠——I 分量离决策边界 0 更远。硬判决只交出 `01`；软解调把这层可靠度差异交给译码器，这正是软判决比硬判决有 2-3 dB 增益的原因。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 软解调输出比特判决 | 输出 LLR：符号是判决、幅度是可信度。 |
| LLR 都只能近似 | BPSK/QPSK 有闭式精确式；QAM 精确式含指数求和，Max-Log-MAP 只是近似。 |
| Max-Log-MAP 只找最近星座点 | 须对 $b_k=0$ 与 $b_k=1$ 两组分别取最小距离再相减，不能只取全局最近点。 |
| 硬判决损失很小 | 丢弃可靠度使 BLER 损失达 2-3 dB 量级。 |
| 软解调公式是 3GPP 强制 | 3GPP 规定调制映射；LLR 生成与近似算法是接收机实现域。 |

## 协议锚点

- TS 36.211 Rel-19 `36211-j30_s06-s08` §7.1.1（BPSK）、§7.1.2（QPSK）、§7.1.3-§7.1.6（QAM）：`3GPP_Rel19/processed/TS_36.211_36211-j30_s06-s08`。
- TS 38.211 Rel-19 `38211-j30` §5.1.2（BPSK）、§5.1.3（QPSK）、§5.1.4-§5.1.7（QAM）：`3GPP_Rel19/processed/TS_38.211_38211-j30`。
- TS 38.214 Rel-19 `38214-j30` §5.1.3、§6.1.4（调度上下文）：`3GPP_Rel19/processed/TS_38.214_38214-j30`。
- LLR 生成算法本身非 3GPP 标准（接收机实现选择）。

## 图谱关联

- [[Modulation_Constellations_调制星座]]
- [[Modulation_Mapping_调制映射]]
- [[LLR_对数似然比]]
- [[T2.13_BPSK_QPSK_soft_demapping]]
- [[T2.14_QAM_Max_Log_MAP_demapping]]
- [[概念图谱入口]]
- 关系语义：软解调是信道输出到译码器输入的关键转换。
