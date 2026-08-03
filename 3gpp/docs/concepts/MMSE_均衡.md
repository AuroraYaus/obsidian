---
type: definition
aliases:
  - MMSE 均衡
  - Minimum Mean Square Error
  - MMSE Equalizer
  - 线性均衡
tags:
  - 3gpp
  - concepts
  - rx-chain
  - equalization
source_spec: "接收机实现（非协议算法）; 参考：TS 38.211 调制接口"
---

# MMSE 均衡

MMSE（最小均方误差）均衡是接收链路的核心步骤：用线性滤波器 $W = \mathbf{H}^H(\mathbf{H}\mathbf{H}^H + \sigma^2\mathbf{I})^{-1}$ 作用于接收信号 y，使输出 $\hat{x} = Wy$ 与发送符号 x 的均方误差最小。

## 独立解释任务

任务目标：解释 MMSE 如何在"消除干扰"和"不放大噪声"之间折中，以及它的归一化为什么有风险。

## 科学定义

- **两种线性均衡**：
  - ZF：$W = H^{-1}$——完全消除干扰，但深度衰落处噪声被放大
  - MMSE：$W = H^H(HH^H+\sigma^2 I)^{-1}$——允许少量残留干扰，换取噪声不放大——**工程上几乎总选 MMSE**
- **归一化危险点**：MMSE 输出是有偏的，仿真器做 `normalize_mmse_demod_input`（$\hat{s}_{\text{norm}} = \hat{s}/(\max(\text{csi}-\sigma^2,0)/\text{csi})$）把输出无偏化（ZF 化）；csi→0（深度衰落）时倍数理论上无界，靠硬限幅 + LLR 裁剪（±31）吸收
- **复杂度**：每 RE 一次矩阵求逆，维度 = min(Nrx, Nlayers)——4 层是 4×4 求逆（O(M³)）

## 直观模型

MMSE 像"戴降噪耳机调音量"：你想听清一个人的话（目标符号），但背景有噪音和其他人说话（干扰+噪声）。ZF 是把其他人完全压掉（但噪音也放大了）；MMSE 是"稍微留一点干扰声，但把整体音量压到合适"——总听感更好。深度衰落（对方声音太小）时，怎么调音量都容易爆音（归一化放大）——所以要限幅。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| MMSE 输出就是发送符号 | MMSE 输出是估计值，还带残留干扰和噪声 |
| ZF 一定比 MMSE 差 | 无噪声极限下两者相同；有噪声时 MMSE 更优，但 ZF 简单 |
| 归一化放大是安全的 | csi→0 时放大理论上无界，必须限幅——这是位宽设计的关键约束 |
| 均衡只做一次 | 每 RE、每符号都要做，MIMO 时每 RE 一次矩阵求逆 |

## 协议锚点

- 均衡算法：接收机实现，非协议规定（协议只定义发射侧与参考信号）。
- 仿真器实现：`nrEqualizeMMSE`（MATLAB 5G Toolbox）、`normalize_mmse_demod_input`。

## 图谱关联

- [[概念图谱入口]]
- [[Channel_Estimation_信道估计]]
- [[CSI_SINR]]
- [[Soft_Demodulation_软解调]]
- [[MIMO_多天线系统]]
- [[T12.3_linear_detectors_mf_zf_mmse]]
- 关系语义：信道估计提供 H → MMSE 均衡分离符号（输出 soft 符号 + CSI）→ 软解调算 LLR → 译码。MMSE 是接收链路的"分离器"，其归一化危险点是位宽设计的边界（衔接 T21.1）。
