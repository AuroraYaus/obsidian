---
type: definition
aliases:
  - 广播信道
  - PBCH MIB
  - 主信息块
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l1
source_spec: "TS 38.331 Rel-19 §6.2.2; TS 38.212 §7.1; TS 36.211 §6.6"
---

# PBCH MIB 广播信道

PBCH（物理广播信道，Physical Broadcast Channel）承载 MIB（主信息块，Master Information Block）——小区搜索的最后一步：UE 解出 PSS/SSS（主同步信号/辅同步信号，Primary/Secondary Synchronization Signal）拿到小区 ID 后，再解 PBCH 读出 MIB，MIB 里给出接入小区所需的最少系统参数，并指向 SIB1（系统信息块 1，System Information Block 1）的调度位置。NR 的 PBCH 用 Polar（极化码，Polar Code）编码、LTE 的 PBCH 用 TBCC（咬尾卷积码，Tail Biting Convolutional Code）编码——两代广播信道编码不同，但"MIB → SIB1 → 其他 SIB"的层级结构一致。

## 独立解释任务

任务目标：讲清 MIB 承载哪些字段、PBCH 的编码与加扰（NR Polar / LTE TBCC）、MIB 如何指向 SIB1，以及 PBCH 在 SSB（同步信号块，Synchronization Signal Block）内的位置与接收端解调流程。

## 科学定义

### MIB 内容（TS 38.331 §6.2.2，NR）

| 字段 | 含义 | 用途 |
|:---|:---|:---|
| systemFrameNumber | 系统帧号（System Frame Number, SFN）高 6 位 | 帧定时（低 4 位由 PBCH 载荷附加位携带） |
| subCarrierSpacingCommon | SIB1/PRACH（物理随机接入信道，Physical Random Access Channel）的公共子载波间隔 | 接入配置 |
| ssb-SubcarrierOffset | SSB 与资源网格的频域偏移 | 网格对齐 |
| dmrs-TypeA-Position | DM-RS（解调参考信号，Demodulation Reference Signal）Type A 位置 | PDSCH（物理下行共享信道，Physical Downlink Shared Channel）解调配置 |
| pdcch-ConfigSIB1 | SIB1 的 PDCCH（物理下行控制信道，Physical Downlink Control Channel）调度配置（CORESET（控制资源集，Control Resource Set）0 + 搜索空间 0） | 指向 SIB1 |

### PBCH 编码与加扰

- NR：PBCH 载荷 32 bit（MIB 24 bit（传输块口径；TS 38.331 ASN.1 为 23 bit 含备用位）+ 8 bit 额外位（SFN 低 4 位、半帧位及 Lmax 相关的 SSB 索引/k_SSB 位）），加 24 bit CRC（gCRC24C）后 Polar 编码（与 PDCCH 同族，见 [[Polar_码]] 与 [[PDCCH_物理下行控制信道]]）；加扰序列初始化仅依赖物理小区 ID，半帧指示位与 SSB 索引位属载荷比特；承载于 SSB 内 PBCH 符号。
- LTE：MIB（14 bit 含 10 bit 保护间隔）→ TBCC 编码（见 [[TBCC_咬尾卷积码]]），40 ms 周期（4 帧），承载于 PBCH 资源（传输信道为 BCH）。
- 接收端：解 PBCH 需要先有小区 ID（PSS/SSS 给出，用于解扰）与信道估计（PBCH DM-RS）。

### MIB → SIB1 衔接

MIB 中的 pdcch-ConfigSIB1 直接给出 SIB1 的 PDCCH（CORESET 0/搜索空间 0）配置——UE 解完 MIB 立刻去盲检 SIB1 的 PDCCH，拿到 SIB1 的 PDSCH 调度后解 SIB1；SIB1 再给出其他 SIB 的调度。这就是"最小系统信息（MIB+SIB1）→ 其他系统信息"的层级。

## 直观模型

MIB 像"电台的频率报时"：报出频道号（SFN）、信号制式（子载波间隔）和"下一档节目在哪个台"（PDCCH-ConfigSIB1）；听众按提示换台才能听到完整节目（SIB1 及后续系统信息）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| MIB 包含全部系统信息 | MIB 只有最少接入参数，其余在 SIB1 与后续 SIB（SIB2 起）里 |
| PBCH 是数据信道 | PBCH 是广播控制信道，不承载用户数据 |
| NR 与 LTE 的 PBCH 编码相同 | NR 用 Polar、LTE 用 TBCC——两代编码不同 |
| 解 PBCH 不需要小区 ID | PBCH 加扰依赖小区 ID，必须先解 PSS/SSS |

## 协议锚点

- MIB 字段：TS 38.331（Rel-19 j20）§6.2.2，本地 `3GPP_Rel19/processed/TS_38.331_38331-j20`。
- PBCH 编码（Polar）：TS 38.212（Rel-19 j30）§7.1，本地 `TS_38.212_38212-j30`。
- PBCH 物理结构与位置：TS 38.211（Rel-19 j30）§7.3.3/§7.4.3，本地 `TS_38.211_38211-j30`。
- LTE PBCH：TS 36.211（Rel-19 j30）§6.6（物理结构）、TS 36.212 §5.1.3.1（TBCC 咬尾卷积编码），本地 `TS_36.211_*`/`TS_36.212_*`。
- SIB 调度：TS 38.321（Rel-19 j20）§5.3.1（MAC 层系统信息调度），本地 `3GPP_Rel19/processed/TS_38.321_38321-j20`。

## 图谱关联

- [[概念图谱入口]]
- [[PSS_SSS_同步信号与小区搜索]]
- [[TBCC_咬尾卷积码]]
- [[Polar_码]]
- [[PDCCH_物理下行控制信道]]
- 关系语义：PBCH 是小区搜索流程的终点产出（MIB），其编码随制式不同（NR Polar/LTE TBCC）分别挂到两个编码家族；pdcch-ConfigSIB1 字段把广播信道接到控制信道（PDCCH）盲检。
