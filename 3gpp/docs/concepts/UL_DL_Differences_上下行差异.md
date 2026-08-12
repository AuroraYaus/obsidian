---
type: definition
aliases:
  - 上下行差异
  - UL DL Differences
  - 上行链路 下行链路
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.211/38.213 综合; T7.5 先例对照"
---

# UL DL Differences 上下行差异

上行（UL，上行链路，Uplink）与下行（DL，下行链路，Downlink）共享同一套译码核心（Turbo/LDPC/Polar、软解调、HARQ），但物理层与协议机制差异显著：波形（OFDMA 下行 vs DFT-s-OFDM 上行可选）、功率（下行固定 vs 上行闭环功控）、定时（下行同步 vs 上行 TA 定时提前）、参考信号（下行 CSI-RS/DMRS vs 上行 SRS/DMRS）、调度（DL assignment vs UL grant）、反馈方向（HARQ-ACK/CSI 全部上行承载）。理解这些差异是「全链路」视角的收束——LTE 有 T7.5（译码差异）先例，本篇做 NR 物理层/协议层全景对照。

## 独立解释任务

任务目标：系统对照 NR 上下行在波形、功率、定时、参考信号、调度、反馈、多址七个维度的差异，衔接批内四篇（DFT-s-OFDM/功控/PRACH/SRS）与既有控制面/调度笔记，形成上行链路的全景收束。

## 科学定义

### 七维度对照表

| 维度 | 下行（DL） | 上行（UL） |
|:---|:---|:---|
| 波形 | CP-OFDM（多载波，见 [[DFT_sOFDM_上行波形]]） | DFT-s-OFDM（低 PAPR）或 CP-OFDM（可配） |
| 功率控制 | 基站固定功率+调度分配 | 开环+闭环功控（[[Power_Control_上行功率控制]]） |
| 定时 | UE 被动同步（PSS/SSS 跟踪） | TA（定时提前）主动对齐基站接收窗（[[PRACH_随机接入]] 建立） |
| 参考信号 | CSI-RS（测量）/DMRS（解调） | SRS（探测）/DMRS（解调，见 [[SRS_探测参考信号]]） |
| 调度 | DL assignment（1_x DCI） | UL grant（0_x DCI，见 [[Scheduling_Grant_调度与授权]]） |
| 反馈 | —（反馈全在上行） | HARQ-ACK/CSI/SR 经 PUCCH/PUSCH（[[PUCCH_上行控制信道与UCI]]） |
| 多址 | 广播/共享（OFDMA 全网） | 多用户复用（comb/时频分，见 [[Multiple_Access_多址接入]]） |

### 差异的根源

1. **发射端不对称**：下行一个基站服务多 UE（功控/调度集中化），上行多 UE 各自发射（功率/定时/干扰各自管理）——这是波形（低 PAPR）、功控（闭环）、TA（同步）三类差异的共同根源。
2. **反馈方向单一**：所有控制反馈（ACK/CSI/SR）只能上行承载——上行是「控制信息汇聚方向」，PUCCH/PUSCH 的复用设计由此而来。
3. **信道互易**：TDD 同频使上行测量（SRS）可服务下行（预编码）——FDD 无此便利（PMI 反馈）。

### 与 LTE T7.5 的对照

LTE 已有 T7.5（LTE 下行与上行译码差异，`docs/L2_协议算法/T7.5_LTE_DL_UL_decoding_differences.md`）——从译码器视角对照 DL/UL 的协议链路、参数来源与 HARQ 上下文。本篇是物理层/协议层全景对照，两者互补：T7.5 讲「同一译码核心在 DL/UL 的接收差异」，本篇讲「物理层与协议机制的全景差异」。

## 直观模型

下行像「广播电台」：一个台（基站）发，所有收音机（UE）收，功率统一、时间统一；上行像「多对讲机同时说话」：每个人（UE）自己调节音量（功控）、对齐通话节奏（TA）、报自己的位置（SRS）——不对称的两端，机制自然不同。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 上行下行只有波形不同 | 波形只是七维度之一——功率/定时/参考信号/调度/反馈机制全不同 |
| TA 是下行概念 | TA 是上行发射定时调整（UE 提前发射抵消传播时延），由 RACH 建立 |
| 上下行译码完全一样 | 译码核心一样，但速率匹配/HARQ 上下文/descriptor 来源有差异（T7.5 详述） |
| TDD 互易性所有场景可用 | 仅 TDD 同频；FDD 上行探测不能直接用于下行（需 PMI） |

## 协议锚点

- 波形：TS 38.211 §5.3/§5.4（CP-OFDM/DFT-s-OFDM），本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- 功控：TS 38.213 §7（本地 `TS_38.213_38213-j30`）。
- 定时提前：TS 38.213 §4.2（TA 命令）、TS 38.321 §5.2（MAC 层 TA 处理）。
- 参考信号：TS 38.211 §7.4.1（DL）/§6.4.1（UL SRS）。
- LTE 先例：T7.5（`docs/L2_协议算法/T7.5_LTE_DL_UL_decoding_differences.md`）。

## 图谱关联

- [[概念图谱入口]]
- [[DFT_sOFDM_上行波形]]
- [[Power_Control_上行功率控制]]
- [[PRACH_随机接入]]
- [[SRS_探测参考信号]]
- [[Multiple_Access_多址接入]]
- 关系语义：上下行差异是全链路的收束视角——波形/功控/TA/参考信号/调度/反馈七维度对照（本批四篇 + 控制面批次），与 LTE T7.5 的译码视角互补，为「上行链路」的知识闭环画上句号。
