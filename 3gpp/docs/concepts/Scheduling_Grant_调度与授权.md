---
type: definition
aliases:
  - 调度授权
  - Grant
  - UL grant
  - DL assignment
  - 半静态调度 SPS
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.214 Rel-19 §5.1/§6.1; TS 38.321 Rel-19 §5.4"
---

# Scheduling Grant 调度与授权

调度授权（Scheduling Grant）是调度器决策的「送达方式」：基站把「这次给你多少资源、怎么收/发」写进 DCI（下行控制信息，Downlink Control Information）——下行叫 DL assignment（下行调度分配），上行叫 UL grant（上行授权）。授权有动态与半静态两种形态：动态授权每个时隙（slot）由 DCI 逐次下发；半静态（SPS/configured grant）一次配置、周期复用，省去重复信令。Grant 是 [[Scheduler_MAC调度器与资源分配]] 的输出、[[PDCCH_物理下行控制信道]] 盲检的收获、[[DCI_下行控制信息]] 字段的用途落地。

## 独立解释任务

任务目标：讲清动态授权与半静态授权（SPS/configured grant）的机制与区别、DL assignment 与 UL grant 的处理差异、DCI 资源分配字段如何解析成实际资源，以及免授权（grant-free）在低时延场景的定位。

## 科学定义

### 动态调度与授权流程

1. 调度器决策（见 [[Scheduler_MAC调度器与资源分配]]）→ 生成 DCI（0_x 上行/1_x 下行，见 [[DCI_下行控制信息]]）→ PDCCH 盲检下发。
2. UE 在搜索空间盲检到 DCI（RNTI 匹配）→ 解析资源分配字段（频域/时域/MCS/HARQ 进程号/NDI/RV/TPC）→ 按字段在对应 slot 收（DL assignment 指示 PDSCH）或发（UL grant 指示 PUSCH）。
3. 时序由 DCI 时域字段的 k0（PDSCH 相对 PDCCH 的 slot 偏移）/k1（HARQ-ACK 相对 PDSCH 的 slot 偏移）/k2（PUSCH 相对 PDCCH 的 slot 偏移）决定（见 [[HARQ_Process_HARQ进程管理]]）。

### 半静态授权：SPS 与 configured grant

| 机制 | 下行 | 上行 | 配置方式 |
|:---|:---|:---|:---|
| SPS（半静态调度，Semi-Persistent Scheduling） | PDSCH 周期资源 | — | RRC 配置周期 + DCI 激活/释放 |
| configured grant Type 1 | — | PUSCH 周期资源 | RRC 配置全部参数（周期/时频/MCS），无需 DCI |
| configured grant Type 2 | — | PUSCH 周期资源 | RRC 配置半参 + DCI 激活 |

用途：VoIP 周期小包、URLLC 低时延——省去每包一次 PDCCH 盲检与 DCI 开销。激活/释放都经 DCI（CS-RNTI 加扰）确认。

### 免授权（grant-free）与多用户调度

- 免授权：configured grant 的扩展——UE 按配置直接发，无需等 grant（URLLC 时延关键场景）；冲突时靠 HARQ 重传与免授权资源池管理。
- MU-MIMO（多用户 MIMO，Multi-User MIMO）配对：调度器把同一 RB 分给多个 UE 的不同层（依赖 PMI/RI，见 [[Link_Adaptation_链路自适应与CQI]]）——一个 DCI 只对一个 UE，但一个 RB 可承载多个 UE 的层。

## 直观模型

Grant 像「工作单」：动态授权是「每单派一次」（经理每次打电话交代）；SPS/configured grant 是「签订长期合同」（一次签约，周期执行，取消时发通知）；免授权是「自由职业」（不用等单，但可能撞单）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| UL grant 是给下行的 | UL grant（0_x DCI）调度上行 PUSCH，DL assignment（1_x）调度下行 PDSCH |
| SPS 已过时 | SPS/configured grant 仍是 VoIP/URLLC 的主流省信令机制 |
| 授权一定是动态的 | 半静态授权周期复用，激活/释放经 DCI；免授权连 DCI 都不需要 |
| 一个 RB 同时只给一个 UE | MU-MIMO 下同一 RB 可多 UE 多层（PMI/RI 决定） |

## 协议锚点

- 资源分配与 grant：TS 38.214（Rel-19 j30）§5.1/§6.1，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30`。
- configured grant：TS 38.321（Rel-19 j20）§5.4，本地 `TS_38.321_38321-j20`。
- SPS 配置：TS 38.331（Rel-19 j20）§6.3.2（SPS-Config/ConfiguredGrantConfig），本地 `TS_38.331_38331-j20`。
- DCI 字段解析：[[DCI_下行控制信息]]（`docs/concepts/DCI_下行控制信息.md`）。

## 图谱关联

- [[概念图谱入口]]
- [[Scheduler_MAC调度器与资源分配]]
- [[DCI_下行控制信息]]
- [[PDCCH_物理下行控制信道]]
- [[HARQ_Process_HARQ进程管理]]
- 关系语义：Grant 是调度链路的中枢——调度器产出决策（Scheduler）、DCI 承载字段（DCI）、PDCCH 盲检送达（PDCCH）、HARQ 进程与 k 时序执行（HARQ_Process）、UE 侧按 grant 收发的数据流进入译码链路（T9.0）。
