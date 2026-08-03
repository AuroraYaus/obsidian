---
type: definition
aliases:
  - Physical Channels
  - 物理信道
  - PDSCH PDCCH PUSCH PUCCH PRACH
  - 上下行信道边界
tags:
  - 3gpp
  - concepts
  - protocol-stack
  - physical-layer
source_spec: "TS 38.211 Rel-19 §6/§7; TS 38.212 Rel-19 §7.3.1; TS 38.214 Rel-19 §5/§6"
---

# Physical Channels 物理信道

物理信道是空口上不同内容的通道分工：数据（PDSCH/PUSCH）、控制（PDCCH/PUCCH）、接入（PRACH）各走各的通道，接收端按通道类型用不同流程解调。

## 独立解释任务

任务目标：解释为什么必须区分物理信道，以及"先控制后数据"的接收流程。

## 科学定义

| 通道 | 方向 | 内容 | 解调依据 |
|---|---|---|---|
| PDCCH | 下行 | DCI（调度指令） | 搜索空间盲检 |
| PDSCH | 下行 | 用户业务数据（DL-SCH） | DCI 参数 |
| PUSCH | 上行 | 用户业务数据（UL-SCH） | DCI（UL grant） |
| PUCCH | 上行 | 控制反馈（ACK/SR/CSI） | 固定格式 |
| PRACH | 上行 | 随机接入前导（Msg1） | 固定格式 |

- **先控制后数据**：下行接收先解 PDCCH（拿 DCI），再按 DCI 参数解 PDSCH——控制与数据分离解决"鸡生蛋"问题
- **传输信道 vs 物理信道**：DL-SCH（逻辑形态）→ PDSCH（波形）；MAC 层只认识传输信道，物理层只认识物理信道
- **上下行差异**：下行由基站调度；上行由 UE 发起（PRACH）或按 grant 发送

## 直观模型

物理信道分工像"车站分层"：站台（PDSCH）运货（数据）、公告屏（PDCCH）告诉你车次信息（DCI）、服务台（PUCCH）收反馈。先看公告屏才知道货在哪节车厢——"先控制后数据"就是这个流程。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PDCCH 也传数据 | PDCCH 只传控制信息（DCI），数据全走 PDSCH/PUSCH |
| PDSCH 和 DL-SCH 是一回事 | DL-SCH 是传输信道（MAC 概念），PDSCH 是物理信道（空口波形） |
| 手机不用读 PDCCH 就能解 PDSCH | DCI 里有时频位置、MCS、层数、RV——不读无法解 |
| 所有下行都是 PDSCH | 控制（PDCCH）、广播（PBCH）、同步各有独立通道 |

## 协议锚点

- 物理信道结构：TS 38.211 Rel-19 §6/§7。
- DCI 格式：TS 38.212 Rel-19 §7.3.1。
- 数据过程：TS 38.214 Rel-19 §5/§6。
- 本地锚点：`3GPP_Rel19/processed/TS_38.211_38211-j30/content.md` 等。

## 图谱关联

- [[概念图谱入口]]
- [[Gold_序列加扰]]
- [[Channel_Estimation_信道估计]]
- [[MMSE_均衡]]
- 关系语义：物理信道分工是接收链路的入口（先认通道再解调）；PDSCH 是业务数据主干，其他通道是配套（控制/反馈/接入）。
