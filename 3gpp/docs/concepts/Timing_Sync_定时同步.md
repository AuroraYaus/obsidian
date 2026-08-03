---
type: definition
aliases:
  - Timing Synchronization
  - 定时同步
  - 时间同步
  - PSS/SSS 检测
tags:
  - 3gpp
  - concepts
  - rx-chain
source_spec: "接收机实现（非协议算法）; evaluation-link-simulator"
---

# Timing Sync 定时同步

定时同步（Timing Synchronization）是 OFDM 接收的第一关——FFT 窗口必须对准符号边界，否则整帧解调错位；仿真器用理想定时，实际系统靠 PSS/SSS 或 CP 相关自己找。

## 独立解释任务

任务目标：解释 OFDM 解调为什么需要先对齐符号边界、理想定时与实际定时的差距、以及定时误差如何进入估计误差预算。

## 科学定义

- **为什么需要**：OFDM 解调要求 FFT 窗口对准符号边界；CP（Cyclic Prefix）提供一定容差——窗口落在 CP 内只有相位旋转，落出 CP 则破坏子载波正交性
- **理想定时**（仿真）：`nrPerfectTimingEstimate` 由 path_gains/path_filters 直接合成零误差定时——性能上界参考
- **实际定时**：PSS/SSS 相关峰检测（主/辅同步序列相关）或 CP 相关（CP 与符号尾部重复结构）；滑动窗相关器复杂度约 O(N_fft × N_cp) MACs
- **定时误差后果**：FFT 窗口偏移 → 子载波间干扰（ICI）+ 相位旋转 → 折算进信道估计误差（理想/实际定时差是估计误差来源之一）

## 直观模型

"对表"：开会前先校准钟表。OFDM 符号像一列按固定节拍行驶的车厢，每节车厢长度相同；FFT 窗口是站台上的检票口——只有对准节拍线，检票人才能完整检过一节车厢。窗口对不准，检票人就会把车厢里的人错配到相邻车厢（符号间泄漏），整个编组秩序被打乱。接收端和发射端各有各的钟，接收端必须先把自己的钟校准到对方的节拍上，才能开始"检票"（解调）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 定时同步是协议规定的步骤 | 协议只定义 PSS/SSS 位置与序列，检测算法是接收机自由度 |
| 仿真里不需要定时同步 | 仿真假设 nrPerfectTimingEstimate 理想定时，实际系统必须自己找 |
| 定时误差只影响幅度 | 会引入相位旋转与载波间泄漏（ICI），并进入估计误差预算 |

## 协议锚点

- PSS/SSS：TS 38.211 Rel-19 §7.4.2。
- 本地锚点：`3GPP_Rel19/processed/TS_38.211_38211-j30/content.md`。
- 仿真器实现：`receive_grid.m`（nrPerfectTimingEstimate）、PHY01 §1.5。

## 图谱关联

- [[概念图谱入口]]
- [[Coherence_Bandwidth_Time_相干带宽与时间]]
- [[Channel_Estimation_信道估计]]
- [[TDL_信道模型]]
- [[MMSE_均衡]]
- [[Physical_Channels_物理信道]]
- 关系语义：定时同步是 OFDM 解调的第一关，定时误差进入信道估计误差预算，是"理想假设 vs 实际实现"差距的一部分。
