---
type: definition
aliases:
  - 跟踪参考信号
  - TRS
  - Tracking Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §7.4.1.5; TS 38.214 Rel-19 §5.1.6"
---

# TRS 跟踪参考信号

TRS（跟踪参考信号，Tracking Reference Signal）维持 UE 的时频跟踪环路：接收端需要持续跟踪定时偏移与频偏（移动、时钟漂移、多普勒），TRS 提供可预测的参考信号供跟踪环路使用。NR 的 TRS 不是独立信号——它是配置了 trs-Info 的 CSI-RS（信道状态信息参考信号，Channel State Information Reference Signal）子集（见 [[CSI_RS_信道状态信息参考信号]]），周期性发送、结构紧凑，是定时同步（T2.7）与频偏同步（T2.8）在连接态的持续输入。

## 独立解释任务

任务目标：讲清 TRS 的用途（时频跟踪）、与 CSI-RS 的关系（trs-Info 子集配置）、时频结构与周期，以及它如何衔接定时/频偏同步（T2.7/T2.8）的跟踪环路。

## 科学定义

### 为什么需要持续跟踪

小区搜索（[[PSS_SSS_同步信号与小区搜索]]）只在初始接入做一次粗同步；连接态中 UE 移动、时钟漂移、多普勒使定时/频偏持续变化——需要周期参考信号驱动跟踪环路（PLL（锁相环，Phase-Locked Loop）类）维持细同步。TRS 就是这个"持续参考"。

### TRS = 配置了 trs-Info 的 CSI-RS

NR 协议不定义独立 TRS 信号：RRC 配置 CSI-RS 资源时设 trs-Info = true，该资源即作 TRS 用。特点：
- 周期发送（常见 10/20/40 ms）、固定时频结构（两簇符号对，便于前后相关做时延/频偏估计）。
- 与普通 CSI-RS 的差异在用途与密度优化（TRS 侧重跟踪精度而非宽带 CSI 测量）。

### 与同步链路的衔接

TRS 相关输出驱动：定时跟踪（FFT 窗口微调，T2.7 的跟踪环）、频偏跟踪（CFO（载波频偏，Carrier Frequency Offset）精估计，T2.8 的跟踪环）——是连接态时频同步的"心跳"。

## 直观模型

TRS 像「道路上的里程桩」：初始接入是"问一次路"（PSS/SSS），连接态开车时每隔一段看一次里程桩（TRS）校正车速表（时钟）和方向（频率）——不看会越开越偏。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| TRS 是独立信号 | TRS 是配置了 trs-Info 的 CSI-RS 子集——无独立序列 |
| TRS 用于 CSI 上报 | TRS 用于时频跟踪，CSI 测量用普通 CSI-RS 配置 |
| 同步只在初始接入做 | 初始接入粗同步后，连接态靠 TRS 持续跟踪 |
| TRS 和 PSS/SSS 一样只在固定位置 | TRS 周期/结构由 RRC 配置（trs-Info 资源） |

## 协议锚点

- TRS 配置（trs-Info）：TS 38.211（Rel-19 j30）§7.4.1.5（CSI-RS 含 trs-Info），本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- 跟踪过程：TS 38.214（Rel-19 j30）§5.1.6，本地 `TS_38.214_38214-j30`。
- 同步链路衔接：T2.7（定时同步）/T2.8（CFO/SFO），`docs/L1_基础/`。

## 图谱关联

- [[概念图谱入口]]
- [[CSI_RS_信道状态信息参考信号]]
- [[PSS_SSS_同步信号与小区搜索]]
- [[Timing_Sync_定时同步]]
- 关系语义：TRS 是连接态时频同步的持续输入——作为 CSI-RS 的 trs-Info 子集存在，与初始接入的 PSS/SSS 粗同步衔接，驱动 T2.7/T2.8 的跟踪环路，是全链路"同步保持"环节。
