---
type: definition
aliases:
  - 下行控制信息
  - DCI
  - DCI 格式
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.212 Rel-19 §7.3; TS 36.212 §5.3.3"
---

# DCI 下行控制信息

DCI（下行控制信息，Downlink Control Information）是基站下发给 UE 的调度指令——"这次传输给你什么、在哪、怎么收"。它由 PDCCH（物理下行控制信道，Physical Downlink Control Channel）承载（[[PDCCH_物理下行控制信道]] 盲检获得），解析出的字段直接生成译码器的 descriptor（T9.0）：MCS（调制与编码方案，Modulation and Coding Scheme）、资源分配、HARQ（混合自动重传请求，Hybrid Automatic Repeat Request）进程号、NDI、RV 等。DCI 是控制面与译码链路的接口——不理解 DCI 字段，就不知道 LLR（对数似然比，Log-Likelihood Ratio）从哪来、译码结果交给谁。

## 独立解释任务

任务目标：讲清 DCI 的格式体系（0_0/0_1/1_0/1_1/2_x）、核心字段语义（资源分配/MCS/HARQ/NDI/RV/TPC）、CRC 与 RNTI（无线网络临时标识，Radio Network Temporary Identifier）加扰，以及 DCI 解析如何映射到译码器 descriptor（与 T9.0 衔接）。

## 科学定义

### DCI 格式体系（NR，TS 38.212 §7.3）

| 格式 | 用途 | 关键差异 |
|:---|:---|:---|
| 0_0 / 0_1 | UL grant（上行授权） | 0_1 支持更多配置（波束/CBG（码块组，Code Block Group）/多载波） |
| 1_0 / 1_1 | DL assignment（下行调度分配） | 1_1 支持更多配置 |
| 2_0/2_1/2_2/2_3 | 组公共（Group Common） | 时隙格式/抢占指示/功率控制，发给一组 UE |

### 核心字段语义（以 DL assignment 1_x 为例）

| 字段 | 语义 | 与译码链路的关系 |
|:---|:---|:---|
| 频域资源分配 | RB（资源块，Resource Block）分配位图/起始 RB+长度 | 决定 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）在网格哪里（T2.3） |
| 时域资源分配 | 时域资源索引 → 起始符号+长度 | 决定符号位置 |
| MCS | 调制阶数 + 目标码率（T2.5/T9.0） | 直接进 descriptor |
| HARQ 进程号 | 进程索引（0-N） | 软缓存地址（T9.3） |
| NDI | 新数据指示（New Data Indicator） | 新传/重传判定（覆盖写 vs 增量写，T9.7） |
| RV | 冗余版本（Redundancy Version） | 循环缓存读取起点（T7.3/T9.3） |
| TPC | 发射功率控制命令（Transmit Power Control Command） | 上行功率控制 |

### CRC 与 RNTI

DCI 附 CRC（循环冗余校验，Cyclic Redundancy Check；NR 24 bit / LTE 16 bit），CRC 用 RNTI 加扰（XOR，异或，Exclusive OR）——盲检时 UE 用候选 RNTI 解扰，CRC 通过即匹配。不同 RNTI（C-RNTI/SI-RNTI/RA-RNTI/TC-RNTI 等）区分 DCI 发给谁/给什么用（详见 [[PDCCH_物理下行控制信道]] 与 T10.6）。

### DCI → Descriptor 映射（与 T9.0 衔接）

DCI 解析不是译码算法的一部分，但它生产译码器消费的元数据：T9.0 的 descriptor（MCS/Qm/R/TBS（传输块大小，Transport Block Size）/RV/CBG）几乎全部来自 DCI 字段 + RRC（无线资源控制，Radio Resource Control）配置。接收链路：PDCCH 盲检 → DCI 解析 → descriptor 生成 → PDSCH 软解调 → 译码。

## 直观模型

DCI 像"运单"：收货人（RNTI）、货物规格（MCS/TBS）、发车时间（时域资源）、车辆编号（HARQ 进程号）、是否返厂（NDI/RV）都写在上面。运单（DCI）先于货物（PDSCH）到达，收货人按运单验收（descriptor 配置译码器）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| DCI 只用于下行 | 0_x 格式调度上行（UL grant），下行用 1_x |
| DCI 里直接有 TBS | DCI 给 MCS+资源分配，TBS 由 T9.0 的公式/查表算出 |
| NDI 翻转=重传 | NDI 翻转表示新传，不翻转表示重传（与 HARQ 进程号联合判定） |
| DCI 是数据信道 | DCI 是控制信息，承载于 PDCCH，不占 PDSCH |

## 协议锚点

- NR DCI 格式：TS 38.212（Rel-19 j30）§7.3，本地 `3GPP_Rel19/processed/TS_38.212_38212-j30`。
- LTE DCI 格式：TS 36.212（Rel-19 j30）§5.3.3，本地 `TS_36.212_36212-j30`。
- descriptor 生成：T9.0（`docs/L2_协议算法/T9.0_TS38214_MCS_TBS_decoder_descriptor.md`）。
- RNTI 定义：TS 38.321（Rel-19 j20）§7.1（RNTI 值表），本地 `3GPP_Rel19/processed/TS_38.321_38321-j20`。

## 图谱关联

- [[概念图谱入口]]
- [[PDCCH_物理下行控制信道]]
- [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]
- [[HARQ_混合自动重传请求]]
- [[RV_冗余版本]]
- 关系语义：DCI 是控制面与译码链路的接口——PDCCH 盲检产出 DCI，DCI 字段解析产出 descriptor（T9.0），MCS/HARQ/RV 字段分别挂到调度表、HARQ 合并与速率恢复的知识节点。
