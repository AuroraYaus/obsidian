---
type: definition
aliases:
  - 载波聚合
  - Carrier Aggregation
  - CA CC SCell
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.300 Rel-19 §5.2; TS 38.213 Rel-19 §10"
---

# Carrier Aggregation 载波聚合

载波聚合（Carrier Aggregation, CA）把多个载波（CC，分量载波，Component Carrier）聚合起来服务同一 UE：一个主载波（PCell，主小区，Primary Cell）管连接与移动性，多个辅载波（SCell，辅小区，Secondary Cell）加带宽提吞吐。CA 是吞吐扩展的机制——单载波带宽受限（FR1 100 MHz），聚合多个 CC 可达数百 MHz。每载波有独立的 HARQ（混合自动重传请求，Hybrid Automatic Repeat Request）进程与调度，跨载波调度经 CIF（载波指示字段，Carrier Indicator Field）指示。

## 独立解释任务

任务目标：讲清 CA 的原理（多 CC 聚合）、PCell/SCell 的角色分工、跨载波调度（CIF）机制、每载波独立 HARQ/调度的含义，以及 CA 与 BWP（带宽部分，Bandwidth Part）的关系。

## 科学定义

### CA 原理与小区结构

- CC（分量载波）：每个 CC 是独立带宽的载波（有独立 numerology/带宽配置）；UE 聚合 2-N 个 CC（NR 最多 16 CC）。
- PCell（主小区）：承载 RRC（无线资源控制，Radio Resource Control）连接与随机接入（[[PRACH_随机接入]]）的小区——移动性锚点。
- SCell（辅小区）：纯数据承载——加带宽；激活/去激活由 MAC CE（媒体接入控制控制单元，MAC Control Element）控制。
- 双连接（DC，Dual Connectivity）是 CA 的演进：不同基站的小区组聚合（MCG/SCG）。

### 跨载波调度（CIF）

DCI（下行控制信息，Downlink Control Information）默认调度本载波；配置 CIF（3-bit）后，PDCCH（物理下行控制信道，Physical Downlink Control Channel）在载波 A 上可调度载波 B 的 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel）——跨载波调度的意义：控制信道集中在一个载波（省 UE 盲检负担），数据信道分散。

### 每载波独立 HARQ/调度

每个 CC 是独立调度域：MCS（调制与编码方案，Modulation and Coding Scheme）/资源分配/HARQ 进程（见 [[HARQ_Process_HARQ进程管理]]）逐载波独立配置——一个 TB（传输块，Transport Block）通常在一个 CC 上传输（跨载波 TB 调度是特殊场景）。

### CA 与 BWP 的关系

每个 CC 内还有 BWP（带宽部分，Bandwidth Part）概念（见 [[BWP_带宽部分]]）——CA 是"载波级聚合"，BWP 是"载波内子带"：聚合后每个 CC 可独立配置 BWP。

## 直观模型

CA 像「多车道并道」：单车道（单载波）限速低（带宽窄），把多条车道并成高速（聚合 CC）；主车道（PCell）负责指挥（连接/移动性），辅车道（SCell）纯跑车（数据）；每条车道独立计程（每载波 HARQ/调度），可以远程遥控辅车道（跨载波调度）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CA 只在 FR2 | CA 在 FR1/FR2 都用（FR1 聚合 100 MHz CC、FR2 聚合 400 MHz CC） |
| SCell 也管连接 | SCell 纯数据承载；连接/移动性由 PCell 管理 |
| 跨载波调度没有代价 | 需配置 CIF 且控制信道集中——增加 PDCCH 设计复杂度 |
| CA 和双连接一样 | 双连接是跨基站聚合（MCG/SCG），CA 是同基站多 CC |

## 协议锚点

- CA 架构：TS 38.300（Rel-19 j20）§5.2，本地 `3GPP_Rel19/processed/TS_38.300_38300-j20`。
- 跨载波调度：TS 38.213（Rel-19 j30）§10（CIF），本地 `TS_38.213_38213-j30`。
- SCell 配置：TS 38.331（Rel-19 j20）§6.3.2（SCellConfig），本地 `TS_38.331_38331-j20`。
- 每载波 HARQ：[[HARQ_Process_HARQ进程管理]]。

## 图谱关联

- [[概念图谱入口]]
- [[HARQ_Process_HARQ进程管理]]
- [[Scheduler_MAC调度器与资源分配]]
- [[BWP_带宽部分]]
- [[PRACH_随机接入]]
- 关系语义：CA 是吞吐扩展的载波级机制——PCell/SCell 分工（连接 vs 数据）、跨载波调度（CIF）、每载波独立 HARQ，与 BWP（载波内子带）构成"聚合-子带"两级频域组织。
