---
type: definition
aliases:
  - HARQ 进程
  - 进程管理
  - HARQ Process
  - NDI
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.321 Rel-19 §5.3; TS 38.214 Rel-19 §5.1"
---

# HARQ Process HARQ 进程管理

HARQ（混合自动重传请求，Hybrid Automatic Repeat Request）进程管理解决「重传怎么组织」：每次传输属于哪个进程、是新传还是重传、软缓存写哪个地址、何时反馈——这些语义由 DCI（下行控制信息，Downlink Control Information）里的 HARQ 进程号与 NDI（新数据指示，New Data Indicator）字段驱动。它是软合并（T4.3/T7.3/T9.3）的调度侧伴侣：没有进程管理，软缓存就不知道把 LLR（对数似然比，Log-Likelihood Ratio）累加到哪。

## 独立解释任务

任务目标：讲清 HARQ 进程的编号与状态机、进程数（LTE/NR 差异）、NDI 翻转语义、k0/k1/k2 时序链，以及同步/异步 HARQ 的区别，并衔接软合并与软缓存（T7.3/T9.3/T9.7）。

## 科学定义

### HARQ 进程：状态机与编号

一个 HARQ 进程跟踪一条「传输-反馈-重传」链：进程处于空（idle）或进行中（占用，等待 ACK/NACK 或已调度重传）。DCI 的 HARQ process number 字段（3-4 bit）指示本次传输用哪个进程；同一进程的重传与初传共享软缓存地址（LLR 证据相加，见 [[Chase_Combining_Chase合并]]/[[Incremental_Redundancy_增量冗余]]）。

### 进程数（LTE vs NR）

| 制式 | DL 进程数 | UL 进程数 | 时序 |
|:---|:---|:---|:---|
| LTE | FDD 8（TDD 4-15） | FDD 8（TDD 1-7） | 同步 HARQ（固定时序） |
| NR | 2-16（高层配置，常见 16） | 2-16 | 异步 HARQ（灵活时序） |

同步 HARQ：重传在固定时间（如 8 ms 后）发生，进程号可由时间推导；异步 HARQ：重传时间由调度器自由安排，进程号必须显式携带——NR 用异步换调度灵活性。

### NDI 翻转语义

NDI（新数据指示，New Data Indicator）是 DCI 里 1 bit：与**同一进程**上次传输相比，NDI 翻转（0→1 或 1→0）= 新传（清空软缓存、覆盖写）；NDI 不翻转 = 重传（增量写、LLR 相加，见 T9.7）。**关键**：NDI 必须与 HARQ 进程号联合看——不同进程的 NDI 无比较意义。

### k0/k1/k2 时序链

DCI 时域资源分配字段（TDRA，时域资源分配，Time Domain Resource Allocation）从高层配置表索引出 k0 与起始符号/时长，k1 由独立 DCI 字段指示（TS 38.214 §5.1.2.1，slot 粒度）：

```
slot n: PDCCH(DCI) ──k0──→ PDSCH (DL assignment)
slot n+k0: PDSCH 接收与译码
slot n+k0+k1: PUCCH HARQ-ACK 上报（k1 在 DCI 中指示）
slot n: PDCCH(UL grant) ──k2──→ PUSCH
```

HARQ-ACK 上报承载于 PUCCH（物理上行控制信道，Physical Uplink Control Channel）[[PUCCH_上行控制信道与UCI]]，或随 PUSCH 捎带（piggyback）。

默认值：k0=0（默认 PDSCH 表 A 首行）；k2=j（默认 PUSCH 表 A，15/30 kHz 下 j=1）；k1 无固定默认——由 DCI 字段或 RRC（无线资源控制，Radio Resource Control）的 dl-DataToUL-ACK 指示。

### 重传限制与失败

- maxHARQ-Tx：同一进程最大传输次数（超过后停止重传，数据交上层处理）。
- HARQ 失败 ≠ 数据丢失：RLC（无线链路控制层，Radio Link Control）层还有 ARQ（自动重传请求，Automatic Repeat Request）重传兜底（见 [[Protocol_Stack_协议栈]] 的层2 结构）。

## 直观模型

HARQ 进程像「快递单号」：每个包裹（TB（传输块，Transport Block））一个单号（进程号），「是否换新包裹」看单子上的标记翻转（NDI）——同一个单号（同进程）不翻转就是补发（重传合并），翻转就是新包裹（新传清缓存）。快递员（调度器）可以自由安排补发时间（异步）或固定时间补发（同步）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| NDI 翻转就一定新传 | 必须结合 HARQ 进程号——同进程内比较才有意义 |
| 进程数 = 软缓存数 | 软缓存按进程×TB 分配（T9.3），但进程数是协议概念、软缓存大小是工程概念 |
| NR 也是同步 HARQ | LTE 是同步（固定 8 ms），NR 是异步（调度自由安排，进程号显式携带） |
| HARQ 失败 = 数据丢失 | 层2 的 RLC ARQ 在 HARQ 之上兜底（AM（确认模式，Acknowledged Mode）模式） |

## 协议锚点

- HARQ 实体与进程：TS 38.321（Rel-19 j20）§5.3，本地 `3GPP_Rel19/processed/TS_38.321_38321-j20`。
- k0/k1/k2 时域分配：TS 38.214（Rel-19 j30）§5.1.2.1（PDSCH）/§6.1.2.1（PUSCH），本地 `TS_38.214_38214-j30`。
- HARQ-ACK 时序：TS 38.213（Rel-19 j30）§9.1，本地 `TS_38.213_38213-j30`。
- 软合并语义：[[HARQ_混合自动重传请求]]、T7.3/T9.3（`docs/L2_协议算法/`）、T9.7（CB 增量写）。

## 图谱关联

- - [[T16.1_scheduler_HARQ_process|T16.1 调度与 HARQ 讲义]]
[[概念图谱入口]]
- [[HARQ_混合自动重传请求]]
- [[DCI_下行控制信息]]
- [[PUCCH_上行控制信道与UCI]]
- [[Chase_Combining_Chase合并]]
- 关系语义：HARQ 进程管理是软合并的调度侧语义——DCI 的进程号/NDI/RV（冗余版本，Redundancy Version）决定软缓存地址与读写模式（T9.7 覆盖写 vs 增量写），k1 决定 HARQ-ACK 反馈时序（PUCCH），是下行译码闭环到上行反馈的关键一环。
