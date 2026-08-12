---
type: definition
aliases:
  - MAC 调度器
  - 调度器
  - Scheduler
  - 资源分配
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.214 Rel-19 §5.1/§6.1.2; TS 38.321 Rel-19 §5.4/§6.1"
---

# Scheduler MAC 调度器与资源分配

调度器（Scheduler）是 MAC 层每时隙（slot）都要做一次的核心决策单元：决定哪个用户（UE，用户设备，User Equipment）在哪个时频资源上、用多大 MCS（调制与编码方案，Modulation and Coding Scheme）、发多少数据。它把「信道质量（CQI）、业务优先级、QoS 需求、缓冲区状态」综合成资源分配（Resource Allocation）指令，经 DCI（下行控制信息，Downlink Control Information）下发。调度是「从协议到物理资源」的决策层——不理解调度器，就无法理解 DCI 资源字段为什么长那样、descriptor（T9.0）从哪来。

## 独立解释任务

任务目标：讲清调度器在 MAC 层的角色与决策输入、资源分配的单位体系（RBG/VRB 与 PRB 的关系）、NR 资源分配类型（Type 0/1）、频域与时域调度的权衡，以及逻辑信道优先级（LCP）在 MAC 复用中的作用。

## 科学定义

### 调度器角色与决策输入

调度器在 MAC 层、每个 slot 运行一次，输入四类信息：(1) 信道质量——每个 UE 上报的 CQI（信道质量指示，Channel Quality Indicator）/PMI/RI（见 [[Link_Adaptation_链路自适应与CQI]]）；(2) 缓冲区状态——UE 通过 BSR（缓冲区状态报告，Buffer Status Report）告知上行数据量；(3) QoS 需求——逻辑信道的优先级与时延预算；(4) 可用资源——RB（资源块，Resource Block）总数与干扰情况。输出：资源分配 + MCS 选择 + HARQ 进程分配（见 [[HARQ_Process_HARQ进程管理]]）。

### 资源分配的单位体系：RBG 与 VRB

- **PRB（物理资源块，Physical Resource Block）**：网格上的实际频域单位（12 子载波，见 [[Spectrum_and_Frequency_Point_频谱与频点]] 与 T2.3）。
- **RBG（资源块组，Resource Block Group）**：频域分配的最小粒度——一组 PRB（尺寸 P 由 BWP 带宽查表，TS 38.214 §6.1.2.2），位图分配时每 bit 对应一个 RBG。
- **VRB（虚拟资源块，Virtual Resource Block）**：调度器分配的「虚拟编号」，经交织映射到物理 PRB——交织（interleaved VRB 映射，TS 38.214 §6.1.2.3）把连续的虚拟编号打散到不同 PRB，获得频率分集。

### 资源分配类型（NR，TS 38.214 §5.1.2）

| 类型 | 机制 | 使用 |
|:---|:---|:---|
| Type 0 | 位图逐 RBG 指示（每 bit 一个 RBG 是否分配） | DCI 1_1/0_1（非回退） |
| Type 1 | RIV（资源指示值，Resource Indication Value）编码「起始 RB + 长度」 | DCI 1_1/0_1；DCI 1_0/0_0（回退） |
| 动态切换 | 由 DCI 的 frequency domain resource assignment 字段最高位指示 Type 0/1 | 高层配置后动态选择 |

### 频域与时域调度

- 频域调度：把信道质量好的 RB 分给相应 UE（频率选择性调度）——PF（比例公平，Proportional Fair）调度器在「吞吐最大化」与「用户公平」间折中：$P_{i,k}$ 分数 = 瞬时速率/平均速率，取分最高的配对。
- 时域调度：NR 支持 slot 级调度与 mini-slot（1-13 符号）低时延调度；DCI 的时域资源分配字段（TDRA，时域资源分配，Time Domain Resource Allocation）从高层配置表索引出起始符号+长度。

### 逻辑信道优先级（LCP）与 MAC 复用

一个 UE 的上行数据可能来自多个逻辑信道（数据/信令），MAC 复用器按 LCP（逻辑信道优先级，Logical Channel Prioritization）规则组装 MAC PDU：先装高优先级逻辑信道，受优先级比特率（PBR，Prioritized Bit Rate）约束——保证控制信令不被大流量数据饿死。

## 直观模型

调度器像餐厅经理：每桌（UE）报「今天胃口（CQI）、想吃什么（BSR）、几点的预约（QoS）」；经理在餐桌布局（资源网格）上排座（分配 RBG），大桌（低码率）坐宽位置，熟客（高优先级）优先——每桌的「点菜单」（DCI）就是调度结果。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 调度器在物理层 | 调度器在 MAC 层，PHY 只负责执行 DCI 指定的参数 |
| VRB 就是 PRB | VRB 是虚拟分配单位，经交织映射到 PRB——两者编号不同 |
| Type 0 一定优于 Type 1 | Type 0 位图灵活但 DCI 开销大、粒度粗（RBG）；Type 1 紧凑（RIV）——按场景选 |
| 调度只看信道质量 | 还看 QoS 优先级、公平性、缓冲区状态、功率约束——多目标优化 |

## 协议锚点

- 资源分配类型：TS 38.214（Rel-19 j30）§5.1.2，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30`。
- RBG 尺寸与 VRB 交织：TS 38.214 §6.1.2.2/§6.1.2.3，本地同卷。
- 调度与优先级处理：TS 38.321（Rel-19 j20）§5.4/§6.1，本地 `TS_38.321_38321-j20`。
- descriptor 衔接：T9.0（`docs/L2_协议算法/T9.0_TS38214_MCS_TBS_decoder_descriptor.md`）。
- 与 MCS/TBS 关系：[[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]。

## 图谱关联

- [[概念图谱入口]]
- [[DCI_下行控制信息]]
- [[PDCCH_物理下行控制信道]]
- [[HARQ_Process_HARQ进程管理]]
- [[Link_Adaptation_链路自适应与CQI]]
- 关系语义：调度器是控制面与数据面的汇合点——它消费 CQI（链路自适应）产出 DCI（PDCCH 盲检的对象），决定 HARQ 进程与 RV（进程管理），最终生成译码器 descriptor（T9.0）的源头。
