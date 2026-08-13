---
type: definition
aliases:
  - 物理上行控制信道
  - PUCCH UCI
  - 上行控制信息
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.213 Rel-19 §9; TS 38.212 §6.3"
---

# PUCCH 上行控制信道与UCI

PUCCH（物理上行控制信道，Physical Uplink Control Channel）承载 UCI（上行控制信息，Uplink Control Information）——UE（用户设备，User Equipment）回传给基站的控制反馈：HARQ-ACK（混合自动重传请求确认，Hybrid Automatic Repeat Request Acknowledgment，即下行数据收没收对的回执）、SR（调度请求，Scheduling Request，申请上行资源）与 CSI（信道状态信息，Channel State Information，报告信道质量）。PUCCH 是下行译码链路的"回执"，没有它 HARQ 重传无法闭环。

## 独立解释任务

任务目标：讲清 UCI 三兄弟（HARQ-ACK/SR/CSI）的内容、PUCCH format 0-4 的划分逻辑（短/长格式、承载容量）、UCI 在 PUCCH 与 PUSCH（物理上行共享信道，Physical Uplink Shared Channel）间的承载选择，以及 HARQ-ACK 时序（k1）如何与下行译码的 HARQ 进程衔接。

## 科学定义

### UCI 内容

| 类型 | 内容 | 大小量级 |
|:---|:---|:---|
| HARQ-ACK | 每个 TB（传输块，Transport Block）/CBG（码块组，Code Block Group）的 ACK/NACK | 1-2 bit（TB）/多 bit（CBG） |
| SR | 是否有上行数据要发（0/1 bit） | 1 bit |
| CSI | CQI（信道质量指示，Channel Quality Indicator）/PMI（预编码矩阵指示，Precoding Matrix Indicator）/RI（秩指示，Rank Indicator） | 数 bit-数十 bit |

### PUCCH format 0-4（NR，TS 38.213 §9）

| Format | 时长 | 承载能力 | 用途 |
|:---|:---|:---|:---|
| 0 | 短（1-2 符号） | ≤2 bit | HARQ-ACK/SR（序列选择编码） |
| 1 | 长（4-14 符号） | ≤2 bit | HARQ-ACK/SR（低速率扩展） |
| 2 | 短 | >2 bit | 多 bit CSI/UCI（DMRS（解调参考信号，Demodulation Reference Signal）辅助相干解调） |
| 3 | 长 | 中等 | 多 bit UCI |
| 4 | 长 | 单 PRB（物理资源块，Physical Resource Block）+ OCC（正交覆盖码，Orthogonal Cover Code）复用 | 大 UCI（含 DFT-s-OFDM（离散傅里叶变换扩展正交频分复用，Discrete Fourier Transform Spread OFDM）预编码；OCC 支持 2/4 UE 共用资源） |

### 承载选择与复用

- UCI 少且无 PUSCH → PUCCH；UCI 多或有 PUSCH → 搭 PUSCH 传输（PUSCH 内 UCI 复用，交织见 T10.9 三角交织器）。
- HARQ-ACK/SR/CSI 同时存在时按优先级与容量复用进同一 PUCCH 资源。
- HARQ-ACK 时序：下行 PDSCH（物理下行共享信道，Physical Downlink Shared Channel）在 slot n 收到 → UCI 在 slot n+k1 的 PUCCH 上报（k1 由 DCI（下行控制信息，Downlink Control Information）时域字段指示）——这就是下行译码到上行反馈的时延链路。

### PUCCH 资源分配

PUCCH 资源由高层配置（PUCCH resource set）+ DCI 的 PUCCH resource indicator 动态选择——上行反馈信道的位置由下行调度指令决定。

## 直观模型

PUCCH 像"收货确认单"：收到货（PDSCH）后回一张单子（UCI），写明"货到了没（ACK/NACK）、还有没有货要发（SR）、道路怎么样（CSI）"；单子格式按内容多少选（明信片/挂号信/快递），发货渠道（PUCCH/PUSCH）按包裹大小选。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PUCCH 只传 ACK/NACK | 还传 SR 与 CSI——三类控制信息都在 PUCCH/UCI 里 |
| UCI 只能走 PUCCH | UCI 可复用进 PUSCH（有上行数据时），交织规则见 T10.9 |
| PUCCH format 越大越好 | format 0-4 按容量与场景选择，短格式省资源、长格式抗覆盖 |
| HARQ 反馈时序固定 | k1 由 DCI 指示，可动态调整（时延与重传及时性权衡） |

## 协议锚点

- PUCCH 格式与资源：TS 38.213（Rel-19 j30）§9，本地 `3GPP_Rel19/processed/TS_38.213_38213-j30`。
- UCI 编码：TS 38.212（Rel-19 j30）§6.3（PUCCH 上 UCI 的 Reed-Muller/极化分段），本地 `TS_38.212_38212-j30`。
- UCI 在 PUSCH 的复用与交织：T10.9（`docs/L2_协议算法/T10.9_NR_UCI_interleaving_triangular.md`）。
- LTE PUCCH：TS 36.211 §5.4（物理结构）、TS 36.212 §5.2.3（UCI 编码），本地 `3GPP_Rel19/processed/TS_36.211_*`/`TS_36.212_36212-j30`。
- HARQ 反馈语义：T9.3/T9.8（HARQ 软缓存与 CBG 反馈）。

## 图谱关联

- [[概念图谱入口]]
- [[Physical_Channels_物理信道]]
- [[HARQ_混合自动重传请求]]
- [[T14.3_PUCCH_UCI_formats|T14.3 PUCCH 与 UCI]]
- [[DCI_下行控制信息]]
- [[PDCCH_物理下行控制信道]]
- [[Link_Adaptation_链路自适应与CQI]]
- [[HARQ_Process_HARQ进程管理]]
- 关系语义：PUCCH 是下行译码链路的回执通道——HARQ-ACK 由译码结果（T7.4/T9.5 的 CRC（循环冗余校验，Cyclic Redundancy Check）判决）驱动，按 DCI 指示的 k1 时序上报，UCI 编码与交织挂到 T10.9；与 PDCCH（物理下行控制信道，Physical Downlink Control Channel）构成控制面双向闭环。
