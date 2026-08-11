---
type: definition
aliases:
  - 频谱与频点
  - Spectrum and Frequency Point
  - ARFCN 频点定位
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l1
source_spec: "docs/L1_基础/T2.3_NR_frequency_resource_grid.md"
---

# Spectrum and Frequency Point 频谱与频点

频谱是电磁波按频率的连续范围，频段是 3GPP 对它的划分块，频点是频段内一个具体的载波中心频率，ARFCN（绝对射频信道号，Absolute Radio Frequency Channel Number）把这个频率编码成整数，信道栅格（channel raster）规定频点合法放置的离散位置，同步栅格（synchronization raster）是 UE（用户设备，User Equipment）盲检 SSB（同步信号块，Synchronization Signal Block）的稀疏搜索位置。这条链是接收端在时间同步之外首先要完成的频率定位——「频点怎么从连续频率变成协议整数」是本节要回答的问题。

## 独立解释任务

任务目标：讲清频谱 → 频段 → 频点 → ARFCN → 信道栅格/同步栅格的完整关系链，回答「频点如何从连续频率变成协议整数」，并说明 UE 开机找小区时沿哪条栅格搜索。

## 科学定义

| 概念 | 定义 | 协议载体 |
|:---|:---|:---|
| 频谱 | 电磁波按频率的连续排列；3GPP 划分 FR1（Frequency Range 1，450 MHz–6 GHz）与 FR2（Frequency Range 2，24.25–52.6 GHz） | TS 38.101-1 §5.2 |
| 频段 | 频谱的划分块：NR n1–n104、LTE 1–105；如 n78 = 3300–3800 MHz（TDD，时分双工，Time Division Duplexing）、n1 上下行成对（FDD，频分双工，Frequency Division Duplexing） | TS 38.101-1 表 5.2-1 / TS 36.101 表 5.5-1 |
| 频点 | 频段内具体的载波中心频率（如 3450 MHz） | RRC（无线资源控制，Radio Resource Control）信令（absoluteFrequencyPointA 等） |
| ARFCN | 频点的整数编号：NR-ARFCN（绝对射频信道号，N_REF）与 E-UTRA ARFCN（N_DL） | TS 38.101-1 §5.4.2.1 / TS 36.101 §5.7.3 |
| 信道栅格 | 频点合法放置的离散位置集（ΔF_Global 整数倍） | TS 38.104 §5.4.2 |
| 同步栅格 | SSB 中心可放置的更稀疏位置集，用 GSCN（全球同步信道号，Global Synchronization Channel Number）编号 | TS 38.101-1 §5.4.3.1 / TS 38.104 §5.4.3 |

**ARFCN 公式**（频率 ↔ 编号互转）：

NR（TS 38.101-1 §5.4.2.1，ΔF_Global 随频段 5/15/60/100 kHz 不等）：

$$
F_{\mathrm{ref}} = F_{\mathrm{REF\_Offs}} + \Delta F_{\mathrm{Global}} \times (N_{\mathrm{REF}} - N_{\mathrm{REF\_Offs}})
$$

LTE（TS 36.101 §5.7.3，步长固定 100 kHz）：

$$
F_{\mathrm{DL}} = F_{\mathrm{DL\_Low}} + 0.1 \times (N_{\mathrm{DL}} - N_{\mathrm{Offs\_DL}})
$$

信令里传的是编号而不是浮点频率——精确、省比特、无浮点歧义。

## 直观模型

街道类比：频谱是整个城市的街道网络（连续范围）；频段是街区（n78 小区）；频点是具体的门牌位置；ARFCN 是邮政编码规则（把位置变成整数编号）；信道栅格是门牌号的允许步进（只能挂奇数号）；同步栅格是只有大街口才有的大地址标记牌（GSCN）——找小区先找大街口，再精确定位门牌。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 频谱 = 频段 | 频段是 3GPP 对频谱的划分块（n78…），频谱是整个连续范围 |
| 频点 = ARFCN | ARFCN 是频点的整数编号，频率与编号靠公式互转 |
| 信道栅格 = 同步栅格 | 同步栅格是信道栅格的稀疏子集（SSB 专用），用 GSCN 编号 |
| UE 盲检沿信道栅格全扫 | 沿同步栅格（GSCN 列表）扫，把搜索空间收敛到几十个候选 |

## 协议锚点

- NR 频段表：TS 38.101-1 §5.2（表 5.2-1），本地 `3GPP_Rel19/processed/TS_38.101_38101-1-j60_s00-0504/content.md`。
- NR-ARFCN：TS 38.101-1 §5.4.2.1（表 5.4.2.1-1），本地 `3GPP_Rel19/processed/TS_38.101_38101-1-j60_s00-0504/content.md`（§5.4.2.1 在 1085 行、§5.4.3.1 在 1141 行起，已核验）。
- 同步栅格/GSCN：TS 38.101-1 §5.4.3.1（表 5.4.3.1-1），本地同卷 1141 行起（已核验）。
- 信道栅格：TS 38.104 §5.4.2，本地 `3GPP_Rel19/processed/TS_38.104_38104-j50`。
- LTE 频段/ARFCN：TS 36.101 §5.7.3（表 5.7.3-1），本地 `3GPP_Rel19/processed/TS_36.101_36101-j60_s00-07`。

## 图谱关联

- [[概念图谱入口]]
- [[T2.3_NR_frequency_resource_grid]]
- [[T2.8_OFDM_CFO_SFO_frequency_synchronization]]
- 关系语义：频谱定位是资源网格（T2.3）与频率同步（T2.8）的公共前置——先知道「频点在哪」，才能谈资源网格对齐与频偏校正；ARFCN 是信令侧的频率坐标语言。
