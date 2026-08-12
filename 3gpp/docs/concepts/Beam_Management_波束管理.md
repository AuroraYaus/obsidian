---
type: definition
aliases:
  - 波束管理
  - Beam Management
  - 波束失败恢复 BFR
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.213 Rel-19 §6; TS 38.331 Rel-19 §6.3.2"
---

# Beam Management 波束管理

波束管理（Beam Management）管理高频段（FR2（频率范围 2，Frequency Range 2））的定向传输：基站与 UE 用窄波束收发，需要先找到最佳波束对（beam pair），并在波束失效时快速恢复。流程分四步——波束测量（SSB/CSI-RS 波束的 L1-RSRP（层 1 参考信号接收功率，Layer 1 Reference Signal Received Power））、波束报告（UE 上报最佳波束）、波束指示（TCI（传输配置指示，Transmission Configuration Indication）状态切换下行波束）、波束失败恢复（BFR，Beam Failure Recovery，检测+恢复）。它是 FR2 可靠性的核心机制，与 [[PSS_SSS_同步信号与小区搜索]]（SSB 波束扫描）、[[CSI_RS_信道状态信息参考信号]]（波束测量源）、[[PRACH_随机接入]]（BFR 专用前导）紧密衔接。

## 独立解释任务

任务目标：讲清波束管理的四步流程（测量/报告/指示/恢复）、SSB 与 CSI-RS 在波束测量中的分工、TCI 状态机制，以及 BFR 的检测与恢复过程。

## 科学定义

### 波束管理的必要性

FR2 毫米波路径损耗大，需窄波束定向增益；但窄波束意味着「盲区」——波束对准错误/被遮挡（人体/建筑）即信号中断。波束管理就是「找到、保持、恢复」最佳波束对的全流程。

### 四步流程

1. 波束测量：基站周期发 SSB 波束（同步栅格扫描，见 [[PSS_SSS_同步信号与小区搜索]]）与 CSI-RS 波束（[[CSI_RS_信道状态信息参考信号]]）——UE 测各波束的 L1-RSRP（层 1 参考信号接收功率，Layer 1 Reference Signal Received Power）。
2. 波束报告：UE 上报最佳波束（SSBRI（SSB 资源指示，SSB Resource Indicator）/CRI（CSI-RS 资源指示，CSI-RS Resource Indicator）+ L1-RSRP）。
3. 波束指示：基站用 TCI（传输配置指示，Transmission Configuration Indication）状态切换 PDSCH/PDCCH 的准共址（QCL，Quasi Co-Location）假设——「这次传输与哪个参考信号同方向」。
4. 波束失败恢复（BFR）：波束失败检测（下行参考信号质量低于门限）→ UE 用专用 PRACH 前导（或免竞争资源）发恢复请求 → 基站配置新波束（TCI 更新）——与随机接入（[[PRACH_随机接入]]）的 BFR 触发场景衔接。

### TDD 互易性

TDD（时分双工，Time Division Duplexing）下上下行同频，可用上行 SRS（探测参考信号，Sounding Reference Signal）探测替代下行波束测量（互易性，见 [[SRS_探测参考信号]]）——省下行测量开销。

## 直观模型

波束管理像「手电筒照路」：初始不知道路在哪，先四面八方扫一遍（SSB 波束扫描），找到最亮的照法（波束报告）；走路时定期确认方向（CSI-RS 波束测量），手电筒坏了（波束失败）就换备用方案（BFR 恢复请求）——方向对了才走得快（吞吐），方向错了寸步难行（中断）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 波束管理只在初始接入 | 初始扫描后连接态持续测量/指示/恢复——四步是循环不是一次性 |
| BFR 就是重做随机接入 | BFR 用专用前导/资源快速恢复，与初始随机接入（竞争）不同 |
| 波束只与下行有关 | 上行也有波束（SRS 探测/上行 TCI），TDD 互易性联动 |
| TCI 是物理层参数 | TCI 由 RRC/MAC-CE 配置、DCI 指示（跨层机制） |

## 协议锚点

- 波束管理过程：TS 38.213（Rel-19 j30）§6（波束失败检测/恢复），本地 `3GPP_Rel19/processed/TS_38.213_38213-j30`。
- TCI/QCL 配置：TS 38.331（Rel-19 j20）§6.3.2（TCI-State），本地 `TS_38.331_38331-j20`。
- 波束测量报告：TS 38.214（Rel-19 j30）§5.2（CSI 报告含 L1-RSRP），本地 `TS_38.214_38214-j30`。
- 衔接：[[PSS_SSS_同步信号与小区搜索]]、[[CSI_RS_信道状态信息参考信号]]、[[PRACH_随机接入]]。

## 图谱关联

- [[概念图谱入口]]
- [[PSS_SSS_同步信号与小区搜索]]
- [[CSI_RS_信道状态信息参考信号]]
- [[PRACH_随机接入]]
- [[SRS_探测参考信号]]
- [[Link_Adaptation_链路自适应与CQI]]
- 关系语义：波束管理是 FR2 可靠性的核心——SSB 波束扫描（初始）+ CSI-RS 波束测量（持续）+ TCI 指示（切换）+ BFR（恢复）四步闭环，与随机接入（BFR 前导）、SRS（TDD 互易性）、链路自适应（L1-RSRP 报告）联动，是参考信号体系与移动性机制的汇合点。
