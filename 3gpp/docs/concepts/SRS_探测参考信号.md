---
type: definition
aliases:
  - 探测参考信号
  - SRS
  - Sounding Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §6.4.1; TS 38.214 Rel-19 §6.2"
---

# SRS 探测参考信号

SRS（探测参考信号，Sounding Reference Signal）是 UE 发给基站的「探针」：基站用它测量上行信道质量，获得上行 CSI（信道状态信息，Channel State Information）——用于上行频选调度、上行波束管理，以及在 TDD（时分双工，Time Division Duplexing）下利用信道互易性推算下行预编码。它是参考信号体系（[[DMRS_解调参考信号]] 之外）的上行专属成员，与下行 CSI-RS 遥相呼应。

## 独立解释任务

任务目标：讲清 SRS 的用途（上行探测/频选调度/波束/TDD 互易性）、时频结构（梳状 comb 与符号数）、资源配置（RRC 周期 + DCI 触发非周期），以及它与上行链路自适应（[[Link_Adaptation_链路自适应与CQI]]）的关系。

## 科学定义

### SRS 的用途

1. 上行信道探测：基站从 SRS 估计每 RB（资源块，Resource Block）的上行 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio）——频选调度（把好 RB 分给 UE）与链路自适应的输入。
2. 上行波束管理：多波束场景下基站测各波束质量。
3. **TDD 互易性**：TDD 上下行同频，信道互易——基站用上行 SRS 估计信道，反推下行预编码（无需 UE 报 PMI（预编码矩阵指示，Precoding Matrix Indicator），省反馈开销；见 [[Link_Adaptation_链路自适应与CQI]] 的 TDD 互易性）。

### 时频结构（TS 38.211 §6.4.1）

- 梳状（comb）：SRS 只在每 N 个子载波上发一个（comb 2/4/8）——多个 UE 可交错复用同一符号资源（comb 交错 + 循环移位正交）。
- 时域：1/2/4（可配至 14）个符号，可配周期（1-320 ms，RRC（无线资源控制，Radio Resource Control）配置）+ 非周期触发（DCI 触发）。
- 频域：可宽带（覆盖整个 BWP（带宽部分，Bandwidth Part））或部分带宽（跳频探测）。

### 资源配置

- 周期/半持续 SRS：RRC 配置（SRS-Config，TS 38.331 §6.3.2）周期发送。
- 非周期 SRS：DCI（下行控制信息，Downlink Control Information）触发（TS 38.214 §6.2）——按需探测，省资源。
- 与功率控制：SRS 有独立功控参数集（见 [[Power_Control_上行功率控制]]）。

## 直观模型

SRS 像「给基站的地质探测仪」：每隔一段（comb）打一个探孔（符号），基站看探孔数据（SINR）决定在哪钻井（分配 RB）——探孔太密浪费（资源），太稀看不清（信道估计不准）；TDD 场景下探孔数据还能反推地下的情况（互易性→下行预编码）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| SRS 是下行信号 | SRS 是 UE 发的上行探测信号；下行对应的是 CSI-RS |
| SRS 只用于上行调度 | 还用于波束管理与 TDD 互易性下行预编码 |
| SRS 越多越好 | SRS 占上行资源，周期/触发式按需配置权衡 |
| 互易性对所有场景成立 | 仅 TDD 同频成立；FDD（频分双工，Frequency Division Duplexing）需 PMI 反馈 |

## 协议锚点

- SRS 物理结构：TS 38.211（Rel-19 j30）§6.4.1，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- SRS 触发与用途：TS 38.214（Rel-19 j30）§6.2，本地 `TS_38.214_38214-j30`。
- SRS 配置：TS 38.331（Rel-19 j20）§6.3.2（SRS-Config），本地 `TS_38.331_38331-j20`。
- 参考信号体系：[[DMRS_解调参考信号]]。

## 图谱关联

- [[概念图谱入口]]
- [[Link_Adaptation_链路自适应与CQI]]
- [[Power_Control_上行功率控制]]
- [[DMRS_解调参考信号]]
- [[Channel_Estimation_信道估计]]
- 关系语义：SRS 是上行链路的「眼睛」——为频选调度、波束与 TDD 互易性（下行预编码）提供信道信息，与下行 CSI-RS 构成参考信号体系的上下行对照，是链路自适应闭环的上行测量入口。
