---
type: definition
aliases:
  - 带宽部分
  - BWP
  - Bandwidth Part
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §4.4.5; TS 38.213 Rel-19 §12"
---

# BWP 带宽部分

BWP（带宽部分，Bandwidth Part）是载波内的子带：UE 只在激活 BWP 内工作（收发都在这个子带内），载波总带宽可远大于 UE 的工作带宽。它的价值在"适配"——UE 能力适配（窄带 UE 用窄 BWP）、省电（低流量时切到窄 BWP）、灵活配置（BWP 间切换无需重配小区）。NR 每载波可配多个 BWP、激活一个；调度（[[Scheduler_MAC调度器与资源分配]]）的 RB（资源块，Resource Block）编号在 BWP 内进行。

## 独立解释任务

任务目标：讲清 BWP 的概念与作用（能力适配/省电/灵活）、BWP 配置（初始/默认/激活、切换）、BWP 与调度/资源网格的关系，以及它与载波聚合（[[Carrier_Aggregation_载波聚合]]）的层级关系。

## 科学定义

### BWP 的定义

- 定义：载波内的一段连续频域资源（子载波集合），有独立 numerology（子载波间隔/CP（循环前缀，Cyclic Prefix）配置）。
- UE 在任意时刻只在一个激活 BWP 内工作（收发 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel））——UE 不需要支持整个载波带宽。

### 作用

1. 能力适配：不同能力 UE 用不同宽度 BWP（窄带物联网 UE 用窄 BWP）。
2. 省电：低流量时切换到窄 BWP（接收带宽小、功耗低）。
3. 灵活：BWP 切换（RRC 配置 + DCI（下行控制信息，Downlink Control Information）指示或定时器）无需重配小区级参数。

### BWP 配置与切换

- 初始 BWP：UE 初始接入用的默认配置（SIB1（系统信息块 1，System Information Block 1）提供，见 [[PBCH_MIB_广播信道]] 的 pdcch-ConfigSIB1 关联）。
- 默认/激活 BWP：RRC 配置多个候选 BWP，激活一个；DCI 的 BWP 指示字段或 bwp-InactivityTimer（不活动定时器）触发切换。
- 切换含时延（TS 38.213 §12 给出切换时间）——切换期间不调度。

### 与 CA 的层级

载波聚合（[[Carrier_Aggregation_载波聚合]]）是载波级聚合（多 CC（分量载波，Component Carrier）），BWP 是载波内子带（每 CC 内独立配置）——两级频域组织：CC 决定"聚几个载波"，BWP 决定"每个载波内用多宽"。

## 直观模型

BWP 像「商场里的移动电梯」：商场（载波）很大，但你只站在电梯覆盖的区段（激活 BWP）——想逛别的区（切 BWP）就坐电梯过去（切换），电梯只在必要区段运行（省电）；商场还可以把几栋楼连起来（载波聚合）扩大范围。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| BWP 是 UE 能力上限 | BWP 是网络配置的激活工作带宽——可小于也可等于 UE 能力 |
| BWP 切换要重新接入 | BWP 切换是 RRC/DCI 触发的快速切换（含时延但无需重接入） |
| 一个载波同时激活多个 BWP | 每载波一次激活一个 BWP（DL/UL 各一个） |
| BWP 和 CA 是一回事 | BWP 是载波内子带，CA 是载波级聚合——两级不同 |

## 协议锚点

- BWP 定义：TS 38.211（Rel-19 j30）§4.4.5，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- BWP 操作与切换时延：TS 38.213（Rel-19 j30）§12，本地 `TS_38.213_38213-j30`。
- BWP 配置：TS 38.331（Rel-19 j20）§6.3.2（BWP-Config），本地 `TS_38.331_38331-j20`。
- 频域网格基础：T2.3（`docs/L1_基础/T2.3_NR_frequency_resource_grid.md`，讲义级详解）。

## 图谱关联

- - [[M16.3_CA_BWP|M16.3 载波聚合与 BWP 讲义]]
[[概念图谱入口]]
- [[Carrier_Aggregation_载波聚合]]
- [[Spectrum_and_Frequency_Point_频谱与频点]]
- [[Scheduler_MAC调度器与资源分配]]
- [[PBCH_MIB_广播信道]]
- 关系语义：BWP 是载波内的工作子带——能力适配/省电/灵活的载体，调度 RB 编号在 BWP 内进行，与 CA（载波级）构成两级频域组织，初始 BWP 由 SIB1 提供（广播信道衔接）。
