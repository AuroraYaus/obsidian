---
type: definition
aliases:
  - 随机接入
  - 随机接入信道
  - PRACH
  - RACH
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.211 Rel-19 §6.3.3; TS 38.213 Rel-19 §8; TS 38.321 Rel-19 §5.1"
---

# PRACH 随机接入

随机接入（Random Access）是 UE 与网络建立上行同步与连接的第一步：UE 在 PRACH（物理随机接入信道，Physical Random Access Channel）上发前导（preamble）——一个精心选择的序列，让基站既能检测「有人来了」又能估计「时间提前量 TA（定时提前，Timing Advance）」。完整的随机接入过程（RACH procedure）分四步（Msg1-Msg4）或两步（MsgA），从「发前导」到「竞争解决」，是 UE 从空闲态进入连接态的必经之路，也是小区搜索（[[PSS_SSS_同步信号与小区搜索]]）之后的下一环。

## 独立解释任务

任务目标：讲清 PRACH 前导的结构与作用（检测/TA 估计）、四步随机接入流程（Msg1-Msg4）每步的语义、两步 RACH 的动机，以及 PRACH 时频资源与根序列配置。

## 科学定义

### 前导（preamble）与 PRACH 物理结构

- 前导：基于 ZC（Zadoff-Chu）序列生成——LTE 长前导 839 长、NR 长前导 139 长（TS 38.211 §6.3.3.1）；同一小区用同一根序列的不同循环移位生成多前导（UE 随机选一个，冲突即竞争）。
- PRACH 时频资源：专用时隙/频域位置（由 SIB1 的 prach-ConfigurationIndex 配置，见 [[PBCH_MIB_广播信道]] 的 SIB1 衔接）；频域有 4-8 个前导资源块（PRB，物理资源块，Physical Resource Block）宽。
- 用途：(1) 检测——基站相关检测识别「有 UE 接入」与哪个前导（竞争解决的基础）；(2) TA 估计——前导到达时间相对期望位置的偏移即 TA，基站随后用 RAR（随机接入响应，Random Access Response）告知 UE 调整发射定时（上行同步）。

### 四步随机接入（Contention-based，CBRA）

```
Msg1: UE 发 PRACH 前导（随机选）
Msg2: 基站回 RAR（RA-RNTI 加扰的 PDCCH/PDSCH：定时提前 + 临时 C-RNTI + UL grant）
Msg3: UE 用 UL grant 发 RRC 连接请求（含 UE 标识）
Msg4: 基站回竞争解决消息（冲突的 UE 中胜者收到确认）
```

竞争的本质：多个 UE 可能选同一前导（Msg1 冲突）——Msg3/Msg4 的 UE 标识交换解决竞争（TS 38.321 §5.1）。

### 两步随机接入（2-step RACH）

MsgA = 前导 + PUSCH 载荷一步发出，MsgB 合并 RAR 与竞争解决——减少信令往返（低时延，URLLC 与大规模 IoT 场景）；代价是前导/PUSCH 资源关联配置更复杂（TS 38.213 §8.1A）。

### 触发场景

初始接入、RRC 重建立、切换（handover 目标小区）、RRC 连接恢复（inactive→active）、上行失步后的数据到达、波束失败恢复（BFR，Beam Failure Recovery）。

## 直观模型

随机接入像「新房客入住登记」：先按门铃（Msg1 前导，让人知道有人来了），门卫回话「我在几号窗口等你」（Msg2 RAR），报上姓名（Msg3 连接请求），门卫确认「好，就是你」（Msg4 竞争解决）；要是两个人同时按同一个门铃（前导冲突），就看谁先报上名（竞争解决）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 随机接入只用于初始接入 | 还用于切换/重建/恢复/失步后数据——任何需要上行同步的场景 |
| 前导是随机数 | 前导是 ZC 序列的循环移位，结构确定、随机性在「选哪个」 |
| 竞争总是坏事 | 竞争是免调度接入的固有代价，Msg3/4 机制解决；还有非竞争接入（切换时基站指定前导） |
| RACH 过程在物理层完成 | 跨层：前导在物理层（PRACH），过程控制（RAR/竞争解决）在 MAC 层（TS 38.321 §5.1） |

## 协议锚点

- PRACH 物理结构与前导序列：TS 38.211（Rel-19 j30）§6.3.3，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30`。
- 随机接入过程：TS 38.213（Rel-19 j30）§8，本地 `TS_38.213_38213-j30`；MAC 层过程 TS 38.321（Rel-19 j20）§5.1，本地 `TS_38.321_38321-j20`。
- 前导配置来源：SIB1（TS 38.331 §6.2.2 RACH-ConfigCommon），本地 `TS_38.331_38331-j20`。
- 与小区搜索衔接：[[PSS_SSS_同步信号与小区搜索]]、[[PBCH_MIB_广播信道]]。

## 图谱关联

- [[概念图谱入口]]
- [[PSS_SSS_同步信号与小区搜索]]
- [[PBCH_MIB_广播信道]]
- [[DCI_下行控制信息]]
- [[PDCCH_物理下行控制信道]]
- 关系语义：随机接入是小区搜索的下一环——PSS/SSS/PBCH 让 UE 找到小区并读到 SIB1（含 PRACH 配置），Msg2/Msg4 经 PDCCH（RA-RNTI）与 PDSCH 下发，TA 与 UL grant 建立上行同步与首个上行传输（Msg3），接入后进入调度（Scheduler）主导的数据传输。
