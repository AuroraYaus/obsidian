---
type: definition
aliases:
  - 功率控制
  - 上行功率控制
  - Power Control
  - TPC PHR
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.213 Rel-19 §7; TS 38.321 Rel-19 §5.4.6"
---

# Power Control 上行功率控制

上行功率控制（Power Control）决定 UE 用多大功率发射：既不能太小（基站收不到），也不能太大（干扰邻区、浪费电池）。它分两层——开环（open-loop）按路损补偿粗略定功率，闭环（closed-loop）用 TPC（发射功率控制命令，Transmit Power Control Command）逐次微调；PHR（功率余量报告，Power Headroom Report）把 UE 的功率余量反馈给调度器。功控是上行链路与下行最大的机制差异之一（下行固定功率、上行闭环调节）。

## 独立解释任务

任务目标：讲清开环/闭环两层功控机制、功控公式的组成项（P0/α/PL/ΔTF/f）、TPC 命令的累计与 DCI 携带方式、PHR 的作用，以及功控与调度（Scheduler）的联动。

## 科学定义

### 上行功控的必要性

下行功率由基站统一管理（多用户共享、干扰可控）；上行每个 UE 独立发射——近处 UE 功率过大淹没远处 UE（远近效应，见 [[Multiple_Access_多址接入]]），功率过小基站收不到。功控让每个 UE 的到达功率恰到好处。

### 开环与闭环

- 开环（open-loop）：UE 测量下行路损（PL，路径损耗，Path Loss，从 RS 功率与实测接收功率推算），按 `P0 + α·PL` 补偿——粗略对齐，无反馈。
- 闭环（closed-loop）：基站根据实际接收 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio）发 TPC 命令（+1/-1 dB 等），UE 累计调整（f 累计项）——精细校正。

### 功控公式（PUSCH 为例，TS 38.213 §7.1 简化式——省略带宽/子载波间隔项与闭环进程索引）

$$
P_{\mathrm{PUSCH}} = P_0 + \alpha \cdot PL + \Delta_{\mathrm{TF}} + f(\mathrm{TPC})
$$

| 项 | 含义 | 来源 |
|:---|:---|:---|
| P0 | 目标接收功率基准 | RRC 配置（开环偏置） |
| α | 路损补偿系数（0-1，部分补偿省干扰） | RRC 配置 |
| PL | 下行路径损耗估计 | UE 测量 |
| ΔTF | 传输格式补偿（MCS（调制与编码方案，Modulation and Coding Scheme）相关） | 按 MCS 查表 |
| f(TPC) | 闭环累计项（TPC 命令累加，含饱和） | DCI 的 TPC 字段（见 [[DCI_下行控制信息]]） |

PUCCH（物理上行控制信道，Physical Uplink Control Channel）/SRS（探测参考信号，Sounding Reference Signal）/PRACH（物理随机接入信道，Physical Random Access Channel）各有独立功控参数集（TS 38.213 §7.2/§7.3/§7.4）。

### TPC 与 PHR

- TPC：DCI 里的 2-bit 字段（见 [[DCI_下行控制信息]] 字段表），发 TPC 命令（-1/0/+1/+3 dB 等），UE 按累积项 f 调整——这就是「闭环」的执行通道。
- PHR（功率余量报告，Power Headroom Report）：UE 周期性/触发式上报「最大功率 - 当前发射功率」的余量（MAC 层，TS 38.321 §5.4.6）——调度器据此决定是否给 UE 分配更多资源（余量足=可加大 MCS/带宽）。

## 直观模型

功控像「对讲机音量调节」：开环是「按距离估算音量」（P0+α·PL），闭环是「对方说大点/小点」（TPC 命令），PHR 是「我还能再大声多少」（余量报告）——三者配合让通话质量刚好够用又不吵到邻居。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 上行功控和下行一样 | 下行固定功率+调度控制，上行闭环功控（开环+闭环两层） |
| 功控只在物理层 | TPC 在 DCI（物理层），PHR 在 MAC 层（TS 38.321）——跨层机制 |
| α=1 一定最好 | 部分补偿（α<1）在干扰受限场景反而更优（减少对邻区干扰） |
| PHR 越大越好 | PHR 大说明有功率余量，调度器可加大资源；但长期满功率说明覆盖边缘 |

## 协议锚点

- 功控公式与参数：TS 38.213（Rel-19 j30）§7，本地 `3GPP_Rel19/processed/TS_38.213_38213-j30`。
- PHR：TS 38.321（Rel-19 j20）§5.4.6，本地 `TS_38.321_38321-j20`。
- TPC 字段：[[DCI_下行控制信息]]（`docs/concepts/DCI_下行控制信息.md`）、TS 38.212 §7.3。
- 与调度联动：[[Scheduler_MAC调度器与资源分配]]。

## 图谱关联

- [[概念图谱入口]]
- [[DCI_下行控制信息]]
- [[Scheduler_MAC调度器与资源分配]]
- [[Multiple_Access_多址接入]]
- [[PUCCH_上行控制信道与UCI]]
- 关系语义：上行功控是链路自适应（[[Link_Adaptation_链路自适应与CQI]]）的上行镜像——TPC 命令经 DCI 闭环微调，PHR 反馈给调度器（[[Scheduler_MAC调度器与资源分配]]）决定资源，PUCCH/SRS/PRACH 各有功控参数集，是上行链路「功率维度」的完整闭环。
