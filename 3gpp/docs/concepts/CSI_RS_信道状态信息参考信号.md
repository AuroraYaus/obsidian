---
type: definition
aliases:
  - 信道状态信息参考信号
  - CSI-RS
  - Channel State Information Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §7.4.1.5; TS 38.214 Rel-19 §5.2"
---

# CSI-RS 信道状态信息参考信号

CSI-RS（信道状态信息参考信号，Channel State Information Reference Signal）是下行测量参考信号：基站周期性/按需发送已知序列，UE 测量它得到下行信道状态，进而生成 CSI（信道状态信息，Channel State Information）报告（CQI（信道质量指示，Channel Quality Indicator）/PMI（预编码矩阵指示，Precoding Matrix Indicator）/RI（秩指示，Rank Indicator），见 [[Link_Adaptation_链路自适应与CQI]]）。它是链路自适应闭环的测量源，同时服务波束管理（[[Beam_Management_波束管理]]）与时频跟踪（[[TRS_跟踪参考信号]]）。一句话本质：**CSI-RS 是下行信道的已知测量参考——基站在约定时频资源上发送已知序列，终端由接收值估计等效信道并折算为 CQI/PMI/RI 上报；测量按配置周期重复或由 DCI 按需触发，结果作用于后续传输的参数选择，本次解调则由与数据同传的 DMRS 承担**。

## 解释目标与范围

本节目标：讲清 CSI-RS 的三大用途（CSI 测量/波束管理/跟踪）、时频结构与端口配置（端口数/密度/NZP-CSI-RS 资源集），以及与 DMRS（解调参考信号，Demodulation Reference Signal）和 SRS（探测参考信号，Sounding Reference Signal）在参考信号体系中的分工。

## 起源与演进

(1) **起点：链路自适应需要测量源。** 基站要选 MCS/波束/秩，必须先知道下行信道状态——CSI-RS 提供这一测量所需的已知序列及其时频位置，终端据此估计下行等效信道。

(2) **三大用途。** CSI 测量（SINR → CQI/PMI/RI 上报）、波束管理（L1-RSRP 波束报告）、时频跟踪（trs-Info 配置兼作 TRS）。

(3) **时频结构与配置。** 端口 1-32、密度 0.5/1/3 RE/PRB/端口；NZP-CSI-RS 由 RRC 配置，周期/半持续/非周期三类（非周期由 DCI 触发）。

(4) **与 DMRS 的分工。** DMRS 与数据同传、服务当次解调；CSI-RS 独立发送、服务后续调度——前者决定当次传输块如何解调，后者决定下一次传输的参数配置。

(5) **上下行对照。** 下行 CSI-RS（基站发、UE 测）↔ 上行 SRS（UE 发、基站测）——参考信号体系的两半边。

## 科学定义

### 三大用途

1. CSI 测量：UE 测 CSI-RS 的 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio）→ 折算 CQI/PMI/RI 上报（Link_Adaptation 闭环的输入，见 [[Link_Adaptation_链路自适应与CQI]]）。
2. 波束管理：多波束场景下 UE 测各 CSI-RS 波束的 L1-RSRP（层 1 参考信号接收功率，Layer 1 Reference Signal Received Power）→ 波束报告（[[Beam_Management_波束管理]]）。
3. 时频跟踪：配置 trs-Info 的 CSI-RS 兼作 TRS（跟踪参考信号，Tracking Reference Signal）——为定时/频偏跟踪环路提供参考（[[TRS_跟踪参考信号]]、T2.7/T2.8）。

### 时频结构与配置

- 端口数：1/2/4/8/12/16/24/32（协议表给出每端口密度组合）；密度：0.5/1/3 RE（资源元素，Resource Element）/PRB（物理资源块，Physical Resource Block）/端口。
- 配置：NZP-CSI-RS（非零功率 CSI-RS，Non-Zero-Power CSI-RS）资源由 RRC（无线资源控制，Radio Resource Control）配置（CSI-ResourceConfig，TS 38.331），周期/半持续/非周期三类（非周期由 DCI（下行控制信息，Downlink Control Information）触发）。
- 与 DMRS 分工：DMRS 用于 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel）解调（与数据同传、UE 专用），CSI-RS 用于测量（独立发送、可多用户共用）——前者决定当次传输块如何解调，后者决定下一次传输的参数配置。

## 直观模型

CSI-RS 的测量关系可分解为三层。第一层是发送侧：基站在 RRC 配置的时频资源（周期、半持续或非周期）上发送已知序列，端口数与密度决定测量开销。第二层是测量侧：终端在相同资源上取接收值与已知序列之比，得到该时频点的等效信道，再按端口与资源集汇总为 SINR 或 L1-RSRP。第三层是上报侧：终端把测量结果折算为 CQI/PMI/RI 或波束指示，在 CSI 上报时机反馈给基站。三层的时序关系是单向的：本次测量结果只进入下一次调度的参数选择，不参与当次数据的解调——当次解调由与数据同传的 DMRS 承担。测量密度与开销同向：单位带宽内参考资源越多，估计越准，可用于数据的资源越少。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CSI-RS 只用于 CSI 上报 | 还用于波束管理与时频跟踪（trs-Info 配置） |
| CSI-RS 是 UE 发的 | CSI-RS 是基站下行发送、UE 测量；上行对应 SRS（UE 发） |
| DMRS 和 CSI-RS 可以互换 | DMRS 解调（与数据同传），CSI-RS 测量（独立配置）——分工不同 |
| CSI-RS 密度越高越好 | 密度高测量准但开销大——按场景配置（移动性/多用户） |

## 协议锚点

- CSI-RS 结构与配置：TS 38.211（Rel-19 j30）§7.4.1.5，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- CSI 报告：TS 38.214（Rel-19 j30）§5.2，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30`。
- 配置参数：TS 38.331（Rel-19 j20）§6.3.2（CSI-ResourceConfig），本地 `3GPP_Rel19/processed/TS_38.331_38331-j20`。
- 测量衔接：[[CSI_SINR]]、T2.11（`docs/L1_基础/`）。

## 关键要点

1. CSI-RS 是基站下行发送、UE 测量的参考信号——上行对应 SRS。
2. 三大用途：CSI 测量/波束管理/时频跟踪（trs-Info）。
3. 端口 1-32、密度 0.5/1/3 RE/PRB/端口；非周期由 DCI 触发。
4. 与 DMRS 分工：解当次（DMRS）vs 配下次（CSI-RS）。
5. 密度高测量准但开销大——按场景配置。
6. CSI 报告（CQI/PMI/RI）是链路自适应闭环的输入。

## 图谱关联

- [[概念图谱入口]]
- [[Link_Adaptation_链路自适应与CQI]]
- [[DMRS_解调参考信号]]
- [[SRS_探测参考信号]]
- [[Beam_Management_波束管理]]
- [[TRS_跟踪参考信号]]
- 关系语义：CSI-RS 是下行测量体系的核心——为链路自适应（CSI 报告）供数、为波束管理（L1-RSRP）供测、经 trs-Info 兼任跟踪（TRS），与 DMRS（解调）/SRS（上行探测）构成参考信号体系的下行测量半边。
