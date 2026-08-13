---
type: definition
aliases:
  - MAC 层映射
  - 信道映射
  - MAC Layer Mapping
  - 逻辑信道 传输信道
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.321 Rel-19 §4-§6; TS 38.300 Rel-19 §5-§6"
---

# MAC Layer Mapping MAC 层映射

MAC（媒体接入控制层，Medium Access Control）层映射（MAC Layer Mapping）是信道三层体系的连接机制：逻辑信道（Logical Channel，按内容类型分，如数据/信令）→ 传输信道（Transport Channel，按传输方式分，如 DL-SCH（下行共享信道，Downlink Shared Channel）/UL-SCH（上行共享信道，Uplink Shared Channel））→ 物理信道（Physical Channel，空口承载，如 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）/PUSCH（物理上行共享信道，Physical Uplink Shared Channel））。MAC 层在中间做映射与复用：把多个逻辑信道的数据按优先级组装进 MAC PDU（协议数据单元，Protocol Data Unit），交给传输信道。

## 独立解释任务

任务目标：讲清逻辑→传输→物理三层的映射关系、MAC PDU 的组装结构（MAC 头/LCID/复用）、LCP（逻辑信道优先级，Logical Channel Prioritization）在复用中的作用，以及常见信道（BCH/PCCH/CCCH 等）的映射特例。

## 科学定义

### 三层信道体系与映射

| 逻辑信道（内容） | → 传输信道（方式） | → 物理信道（承载） |
|:---|:---|:---|
| DTCH（专用业务信道，Dedicated Traffic Channel） | DL-SCH / UL-SCH | PDSCH / PUSCH |
| DCCH（专用控制信道，Dedicated Control Channel） | DL-SCH / UL-SCH | PDSCH / PUSCH |
| CCCH（公共控制信道，Common Control Channel） | DL-SCH / UL-SCH | PDSCH / PUSCH |
| BCCH（广播控制信道，Broadcast Control Channel） | BCH（广播信道，Broadcast Channel）/ DL-SCH | PBCH（物理广播信道，Physical Broadcast Channel）/ PDSCH |
| PCCH（寻呼控制信道，Paging Control Channel） | PCH（寻呼信道，Paging Channel） | PDSCH（寻呼调度经 PDCCH（物理下行控制信道，Physical Downlink Control Channel）） |

MAC 层职责：逻辑信道 → 传输信道的映射与复用；传输信道 → 物理信道由物理层完成（MAC 经传输块 TB（传输块，Transport Block）接口交付）。

### MAC PDU 组装

- MAC PDU = MAC 头（一个或多个子头）+ 若干 MAC SDU（服务数据单元，Service Data Unit）。
- 子头含 LCID（逻辑信道标识，Logical Channel Identity）——接收端凭 LCID 知道这段数据属于哪个逻辑信道（哪些数据归哪个业务/信令）。
- 复用：一个 MAC PDU 可含多个逻辑信道的数据（按 LCP 优先级组装，见 [[Scheduler_MAC调度器与资源分配]] 的 LCP 规则）——高优先级信令先装，PBR（优先级比特率，Prioritized Bit Rate）约束防饿死。

### 特殊映射

BCCH→BCH→PBCH 是"最小系统信息"专用路径（MIB（主信息块，Master Information Block）不经 MAC 复用，见 [[PBCH_MIB_广播信道]]）；PCCH→PCH 走寻呼流程（寻呼时机由 PDCCH 指示）。

## 直观模型

MAC 层映射像「邮局分拣」：信件按类型贴不同标签（逻辑信道 LCID），邮局（MAC）把多个寄件人的信装进一个包裹（MAC PDU 复用），按运输方式（传输信道）打包，交给运输公司（物理信道）发出；收件人按标签拆包（解复用）分发给各收件人（上层）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 逻辑信道=传输信道 | 逻辑信道按内容分、传输信道按传输方式分——MAC 在中间映射复用 |
| MAC PDU 只能装一个业务的数据 | 一个 MAC PDU 可复用多个逻辑信道（LCP 按优先级组装） |
| PBCH 走 MAC 复用 | MIB 经 BCH 直通 PBCH，不经 MAC PDU 组装 |
| LCID 是物理层概念 | LCID 是 MAC 头字段（逻辑信道标识） |

## 协议锚点

- 信道结构与映射：TS 38.300（Rel-19 j20）§5-§6，本地 `3GPP_Rel19/processed/TS_38.300_38300-j20`。
- MAC PDU 与复用：TS 38.321（Rel-19 j20）§4-§6，本地 `3GPP_Rel19/processed/TS_38.321_38321-j20`。
- LCP 规则：TS 38.321 §5.4.3，本地同卷。
- 物理承载：[[Physical_Channels_物理信道]]、[[PBCH_MIB_广播信道]]。

## 图谱关联

- - [[M16.4_MAC_layer_mapping|M16.4 MAC 层映射讲义]]
[[概念图谱入口]]
- [[Scheduler_MAC调度器与资源分配]]
- [[Protocol_Stack_协议栈]]
- [[Physical_Channels_物理信道]]
- [[PBCH_MIB_广播信道]]
- 关系语义：MAC 层映射是全链路的"内容-方式-承载"三层桥——逻辑信道（业务/信令）经 MAC 复用（LCP）进传输信道、物理信道承载（PDSCH/PUSCH/PBCH），是调度器（Scheduler）与译码链路（TB 接口）之间的协议枢纽。
