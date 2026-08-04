---
type: definition
aliases:
  - TDL 信道模型
  - Tapped Delay Line
  - TDL-A
  - TDL-B
  - TDL-C
tags:
  - 3gpp
  - concepts
  - channel
  - tdl
source_spec: "TR 38.901 Rel-19 §7.7; TS 38.104 Rel-19 Annex"
---

# TDL 信道模型

TDL（Tapped Delay Line，抽头延迟线）是 3GPP 定义的多径衰落信道模型：信道由若干条不同时延的路径（抽头）叠加，$y(t) = \sum_{l=1}^{L} h_l \cdot x(t - \tau_l) + n(t)$（L 抽头、$\tau_l$ 时延、$h_l$ 复增益）。

## 独立解释任务

任务目标：解释多径信道为什么用"抽头延迟线"建模，以及 TDL-A~E 剖面怎么选。

## 科学定义

- **TDL-A/B/C/D/E 五类剖面**（TR 38.901 §7.7）：TDL-A 稀疏 NLOS、TDL-B 中等、TDL-C 密集 LOS（仿真器默认）、TDL-D/E 变体
- **两个关键参数**：
  - delaySpread（时延扩展）：典型 300 ns（仿真器默认）→ 决定相干带宽 ≈ 1/delaySpread ≈ 3.3 MHz
  - maximumDopplerHz（多普勒）：30 Hz ≈ 9.3 km/h @ 3.5 GHz → 决定相干时间 ≈ 0.423/Doppler ≈ 14 ms
- **对接收的影响**：多径 → 频率选择性衰落 → 需信道估计（DMRS）+ 均衡（MMSE）；衰落使符号幅度随机起伏，深度衰落处噪声放大

## 直观模型

TDL 像"回声山谷"：你喊一句话（发射），山谷从不同距离返回多个回声（多径），每个回声延迟不同、音量不同。山谷的形状（剖面）决定回声模式——TDL-A~E 就是五种标准"山谷形状"。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| TDL 剖面是真实网络的固定配置 | 剖面是仿真用的标准模型，真实信道比它复杂（3D/空间相关） |
| delaySpread 越大越好 | 时延扩展大 → 相干带宽小 → 频率选择性严重 → 均衡压力大 |
| 多普勒只影响高速移动 | 多普勒由相对速度决定，30 Hz 对应约 9 km/h 的低速也会有时间选择性 |
| AWGN 能代替 TDL | AWGN 无多径，无法刻画频率选择性衰落——TDL 是仿真的必要折中 |

## 协议锚点

- 延迟剖面定义：TR 38.901 Rel-19 §7.7；TS 38.104 Rel-19 Annex（TDL-A~E 参数表）。
- 本地锚点：`3GPP_Rel19/processed/TS_38.104_38104-j50/content.md`。
- 仿真器实现：`+phy/+channel/create_tdl_channel.m`（nrTDLChannel，默认 TDL-C/300ns/30Hz）。

## 图谱关联

- [[概念图谱入口]]
- [[Fading_Channel_衰落信道]]
- [[AWGN_信道模型]]
- [[Channel_Estimation_信道估计]]
- [[MMSE_均衡]]
- 关系语义：TDL 是"衰落信道"的具体化模型；TDL 下必须做信道估计与均衡，衰落特性直接决定译码器输入 LLR 的可靠度（衔接 T2.15）。
