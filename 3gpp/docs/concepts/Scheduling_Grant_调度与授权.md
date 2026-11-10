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

调度授权（Scheduling Grant）是调度决策在空口上的**下达形式**：基站把「这次给你多少资源、怎么收/发」写进 DCI（下行控制信息，Downlink Control Information）——下行叫 DL assignment（下行调度分配），上行叫 UL grant（上行授权）。授权有动态与半静态两种形态：动态授权每个时隙（slot）由 DCI 逐次下发；半静态（SPS/configured grant）一次配置、周期复用，省去重复信令。Grant 是 [[Scheduler_MAC调度器与资源分配]] 的输出、[[PDCCH_物理下行控制信道]] 盲检的收获、[[DCI_下行控制信息]] 字段的用途落地。一句话本质：**Grant 是"工作单"——动态授权每单派一次，SPS/configured grant 签长期合同周期执行，免授权连单都不用等**。

## 解释目标与范围

本节目标：讲清动态授权与半静态授权（SPS/configured grant）的机制与区别、DL assignment 与 UL grant 的处理差异、DCI 资源分配字段如何解析成实际资源，以及免授权（grant-free）在低时延场景的定位。

## 起源与演进

(1) **起点：调度决策必须被终端获得。** 调度器做出决策时终端并不知情，因此需要一个信令载体把「本次分配多少资源、以什么参数收发」传递给它。这个载体就是授权：决策写入 DCI，经控制信道盲检下发。

(2) **动态授权：每单派一次。** 每个 slot 的每次传输都由 DCI 逐次授权——灵活精确，但每单都要付一次 PDCCH 盲检与 DCI 开销。对周期小包业务（VoIP）来说，这笔开销重复且浪费。

(3) **半静态授权：签长期合同。** SPS（下行）与 configured grant（上行）把"周期 + 资源位置"一次配好：Type 1 纯 RRC 配置连 DCI 都不需要；Type 2 与 SPS 由 DCI（CS-RNTI 加扰）激活/释放。周期执行、省去重复信令——VoIP 与 URLLC 的主流省信令机制。

(4) **免授权：以碰撞风险换时延。** configured grant 的进一步扩展：终端在配置好的资源池内自行选择传输机会，不必等待逐次授权——时延被压到极限，代价是多个终端可能占用同一资源，冲突由 HARQ 重传与资源池管理消化。

(5) **时序与多用户收尾。** 授权内的 k0/k1/k2 决定 PDCCH→PDSCH→HARQ-ACK→PUSCH 的时隙链条；MU-MIMO 下同一个 RB 可以同时承载多个 UE 的不同层——一个 DCI 只管一个 UE，一个资源却能服务多个。

## 科学定义

### 动态调度与授权流程

1. 调度器决策（见 [[Scheduler_MAC调度器与资源分配]]）→ 生成 DCI（0_x 上行/1_x 下行，见 [[DCI_下行控制信息]]）→ PDCCH 盲检下发。
2. UE 在搜索空间盲检到 DCI（RNTI（无线网络临时标识，Radio Network Temporary Identifier）匹配）→ 解析资源分配字段（频域/时域/MCS/HARQ（混合自动重传请求，Hybrid Automatic Repeat Request）进程号/NDI（新数据指示，New Data Indicator）/RV（冗余版本，Redundancy Version）/TPC（发射功率控制命令，Transmit Power Control Command））→ 按字段在对应 slot 收（DL assignment 指示 PDSCH（物理下行共享信道，Physical Downlink Shared Channel））或发（UL grant 指示 PUSCH（物理上行共享信道，Physical Uplink Shared Channel））。
3. 时序由 DCI 时域字段的 k0（PDSCH 相对 PDCCH 的 slot 偏移）/k1（HARQ-ACK 相对 PDSCH 的 slot 偏移）/k2（PUSCH 相对 PDCCH 的 slot 偏移）决定（见 [[HARQ_Process_HARQ进程管理]]）。

### 半静态授权：SPS 与 configured grant

| 机制 | 下行 | 上行 | 配置方式 |
|:---|:---|:---|:---|
| SPS（半静态调度，Semi-Persistent Scheduling） | PDSCH 周期资源 | — | RRC 配置周期 + DCI 激活/释放 |
| configured grant Type 1 | — | PUSCH 周期资源 | RRC 配置全部参数（周期/时频/MCS），无需 DCI |
| configured grant Type 2 | — | PUSCH 周期资源 | RRC 配置半参 + DCI 激活 |

用途：VoIP（IP 语音，Voice over IP）周期小包、URLLC（超可靠低时延通信，Ultra-Reliable Low-Latency Communication）低时延——省去每包一次 PDCCH 盲检与 DCI 开销。SPS 与 configured grant Type 2 的激活/释放经 DCI（CS-RNTI（配置调度 RNTI，Configured Scheduling RNTI）加扰）确认；Type 1 纯 RRC 配置，无 DCI。

### 免授权（grant-free）与多用户调度

- 免授权：configured grant 的扩展——UE 按配置直接发，无需等 grant（URLLC 时延关键场景）；冲突时靠 HARQ 重传与免授权资源池管理。
- MU-MIMO（多用户 MIMO，Multi-User MIMO）配对：调度器把同一 RB 分给多个 UE 的不同层（依赖 PMI（预编码矩阵指示，Precoding Matrix Indicator）/RI（秩指示，Rank Indicator），见 [[Link_Adaptation_链路自适应与CQI]]）——一个 DCI 只对一个 UE，但一个 RB 可承载多个 UE 的层。

## 直观模型

三种授权的差别在于「决策下发的时机与频次」。动态授权每次传输都由一条控制信息即时下发资源；半静态授权（SPS 与 configured grant）由高层配置一次周期与资源，之后按周期重复使用，变更或释放时才再发指示；免授权（grant-free）则连周期分配也不预先指定，终端在配置好的资源池内自行选择传输机会，代价是可能与其他终端碰撞。

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

## 关键要点

1. Grant 是调度决策在空口上的下达形式：DL assignment（1_x）调度下行，UL grant（0_x）调度上行。
2. 动态授权每 slot 逐次下发；半静态（SPS/configured grant）一次配置周期复用。
3. configured grant Type 1 纯 RRC 配置无 DCI；Type 2 与 SPS 需 DCI（CS-RNTI）激活/释放。
4. 免授权把时延压到极限，冲突靠 HARQ 重传与资源池兜底。
5. k0/k1/k2 决定授权链条的时隙时序。
6. MU-MIMO：同一 RB 可承载多个 UE 的不同层。

## 图谱关联

- [[概念图谱入口]]
- [[Scheduler_MAC调度器与资源分配]]
- [[DCI_下行控制信息]]
- [[PDCCH_物理下行控制信道]]
- [[HARQ_Process_HARQ进程管理]]
- 关系语义：Grant 是调度链路的中枢——调度器产出决策（Scheduler）、DCI 承载字段（DCI）、经 PDCCH 盲检下发（PDCCH）、HARQ 进程与 k 时序执行（HARQ_Process）、UE 侧按 grant 收发的数据流进入译码链路（T9.0）。
