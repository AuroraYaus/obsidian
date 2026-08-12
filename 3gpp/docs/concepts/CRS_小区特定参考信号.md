---
type: definition
aliases:
  - 小区特定参考信号
  - CRS
  - Cell-specific Reference Signal
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 36.211 Rel-19 §6.10"
---

# CRS 小区特定参考信号

CRS（小区特定参考信号，Cell-specific Reference Signal）是 LTE 的下行参考信号：每个子帧、几乎全带宽发送，供解调、测量与同步使用。它「广播式」存在——小区内所有 UE 共用同一 CRS，这与 NR 的设计哲学（[[DMRS_解调参考信号]]/[[CSI_RS_信道状态信息参考信号]] 按 UE/用途专用化）形成鲜明代际对比。CRS 是 LTE 专属制式（TS 36.211），理解它是读懂「为什么 NR 抛弃 CRS」的关键。

## 独立解释任务

任务目标：讲清 CRS 的结构（端口/位置/周期）与用途（解调/测量/同步）、与 NR 参考信号体系（DMRS/CSI-RS）的设计对比，以及 NR 弃用 CRS 的动机（开销与灵活性）。

## 科学定义

### CRS 结构与用途（TS 36.211 §6.10）

- 结构：端口 0-3（最多 4 天线端口）、每子帧发送（1 ms 周期）、全带宽（与小区带宽同宽）、固定频域位置（按小区 ID（物理小区标识，Physical Cell Identity）偏移）。
- 用途三合一：(1) 解调——LTE 无专用 DMRS（Rel-8 起），PDSCH（物理下行共享信道，Physical Downlink Shared Channel）解调依赖 CRS 信道估计；(2) 测量——RSRP（参考信号接收功率，Reference Signal Received Power）/RSRQ 测量；(3) 同步——时间/频率跟踪。

### 与 NR 参考信号体系的对比

| 维度 | LTE CRS | NR DMRS/CSI-RS |
|:---|:---|:---|
| 覆盖 | 小区级广播（所有 UE 共用） | UE 专用/按需配置 |
| 发送 | 每子帧、全带宽 | 按需（时隙内、分配带宽内） |
| 开销 | 恒定（最高 4 端口 × 全带宽） | 随配置（低开销） |
| 波束 | 全向（无波束概念） | 可波束成形（DMRS/CSI-RS 随波束） |
| 解调 | CRS 兼任 | DMRS 专用（数据同传） |

### NR 弃用 CRS 的动机

(1) 开销：CRS 恒定占用资源，NR 按需配置省资源；(2) 灵活性：NR 支持多波束/多用户（MU-MIMO，多用户 MIMO，Multi-User MIMO），UE 专用 DMRS 可随波束与调度变化，CRS 无法适配；(3) 前向兼容：CRS 全带宽发送限制带宽动态扩展。代价：NR 接收端必须依赖 DMRS 解调（每传输都要做信道估计，见 [[Channel_Estimation_信道估计]]）。

## 直观模型

CRS 像「24 小时全城广播的电台」：所有居民（UE）共用同一信号（解调/测量/同步全靠它）——简单但费电（开销恒定）；NR 像「按需点播」：每次节目（数据传输）配专属字幕（DMRS），不定期插播路况（CSI-RS 测量）——省资源但每次都要现配。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| NR 也有 CRS | NR 无 CRS——LTE 专属（TS 36.211）；NR 用 DMRS/CSI-RS/PTRS/TRS |
| CRS 是 UE 专用信号 | CRS 是小区级广播（所有 UE 共用），NR 才 UE 专用化 |
| CRS 和 DMRS 一样只用于解调 | CRS 三合一（解调/测量/同步），DMRS 只管解调 |
| LTE 没有测量参考信号 | CRS 兼任测量（RSRP/RSRQ），NR 用 CSI-RS 专职测量 |

## 协议锚点

- CRS 结构：TS 36.211（Rel-19 j30）§6.10，本地 `3GPP_Rel19/processed/TS_36.211_*`。
- CRS 用途（RSRP 测量）：TS 36.214（Rel-19 j30）§5.1.1，本地 `TS_36.214_*`。
- **制式边界**：CRS 为 LTE 专属，NR 体系见 [[DMRS_解调参考信号]]/[[CSI_RS_信道状态信息参考信号]]——勿混用。

## 图谱关联

- [[概念图谱入口]]
- [[DMRS_解调参考信号]]
- [[CSI_RS_信道状态信息参考信号]]
- [[Channel_Estimation_信道估计]]
- [[PSS_SSS_同步信号与小区搜索]]
- 关系语义：CRS 是 LTE 参考信号体系的代表——理解它与 NR（DMRS/CSI-RS）的设计对比，就是理解「广播式 vs 按需式」两代物理层哲学的分水岭；信道估计（Channel_Estimation）在 LTE 以 CRS 为源、在 NR 以 DMRS 为源。
