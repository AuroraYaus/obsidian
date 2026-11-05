---
type: definition
aliases:
  - 物理下行控制信道
  - PDCCH
  - 盲检
tags:
  - 3gpp
  - concepts
  - physical-layer
  - l2
source_spec: "TS 38.213 Rel-19 §10; TS 38.211 Rel-19 §7.3.2"
queries: 1
---

# PDCCH 物理下行控制信道

PDCCH（物理下行控制信道，Physical Downlink Control Channel）承载 DCI（下行控制信息，Downlink Control Information）——基站调度指令的载体。UE 在每个监测时机（monitor occasion）对一组候选 PDCCH 做盲检测（blind decoding）：不知道 DCI 发给谁、多大、放在哪，就按聚合等级逐个试，用 CRC（循环冗余校验，Cyclic Redundancy Check）加扰的 RNTI（无线网络临时标识，Radio Network Temporary Identifier）判断"这是不是给我的"。一句话本质：**PDCCH 是信封、DCI 是信，收件人地址不在信封上而在锁芯（RNTI）里——UE 靠盲检拆封认领**。盲检是全链路调度入口的核心机制，也是控制面最独特的工程问题。

## 独立解释任务

任务目标：讲清 PDCCH 的时频结构（CORESET/REG/CCE/聚合等级）、搜索空间、盲检流程与 RNTI 机制，说明为什么控制信道需要盲检而数据信道不需要，并与 Polar（极化码，Polar Code）控制译码（T10.6）和 DCI 解析（[[DCI_下行控制信息]]）衔接。

## 起源与演进

PDCCH 与控制信息同步诞生：控制信息要有物理载体，UE 收数据前必须先拿到调度指令，PDCCH 就是这条专属信道。它的资源按三级组织——CORESET（频域 RB 集 + 时域 1~3 符号）套 REG（1 PRB × 1 符号）、6 个 REG 组成一个 CCE（最小分配单位）；聚合等级 1/2/4/8/16 决定一个 PDCCH 占几个 CCE，等级越高码率越低越可靠。整个结构围绕一个问题设计：UE 不知道 DCI 发给谁、多大、放在哪，只能盲检——DCI 没有显式收件人字段，身份藏在 CRC 的 RNTI 加扰里，UE 按搜索空间候选集逐个解调、译码、用自己的一串 RNTI 解扰 CRC，解开了才是"我的"。

协议用盲检换取零配置开销，代价是接收复杂度（候选 × RNTI × DCI 尺寸），于是用搜索空间限候选、UE 能力限盲检上限——这是控制面最独特的工程矛盾。编码上两代分工：NR DCI 经 24 bit CRC（RNTI 加扰）+ Polar 编码；LTE 经 16 bit CRC + 咬尾卷积码（TBCC）。

## 科学定义

### 时频结构（NR，TS 38.213 §10 / TS 38.211 §7.3.2）

| 概念 | 定义 |
|:---|:---|
| CORESET | 控制资源集（Control Resource Set）：PDCCH 可占用的时频资源块（频域 RB 集 + 时域 1-3 符号） |
| REG | 资源元素组（Resource Element Group）：1 个 PRB（物理资源块，Physical Resource Block） × 1 个 OFDM 符号 |
| CCE | 控制信道单元（Control Channel Element）：6 个 REG（REG 束大小 L∈{2,6}，3 符号 CORESET 可为 3），CCE 是 PDCCH 分配的最小单位 |
| 聚合等级 | 1/2/4/8/16——一个 PDCCH 占用的 CCE 数，决定编码率（聚合越大码率越低越可靠） |
| 搜索空间 | 一组候选 PDCCH 位置（monitor occasion + 聚合等级组合），分 CSS（公共搜索空间，Common Search Space）与 USS（UE 专用搜索空间，UE-specific Search Space） |

### 盲检流程

1. UE 在每个监测时机，按搜索空间配置的候选集（特定 CCE 位置组合），对每个候选做：解调 → Polar 译码 → CRC 校验。
2. 候选的 CRC 用某个 RNTI（无线网络临时标识，Radio Network Temporary Identifier）加扰——UE 用自己的 RNTI 集（C-RNTI/SI-RNTI/RA-RNTI 等）逐个解扰尝试，CRC 通过即"这是我的 DCI"。
3. DCI 大小（payload 长度）预先由配置限定（多个 DCI 格式候选），盲检在不同 DCI 大小间也需尝试。
4. 复杂度：候选数 × RNTI 数 × DCI 大小数——这就是"盲"的代价，工程上用搜索空间配置与聚合等级限制候选总数（UE 能力约束盲检次数上限）。

### 盲检的必要性

UE 没有专用寻址信道，DCI 也没有显式"收件人地址"——收件人信息藏在 CRC 加扰的 RNTI 里。协议选择盲检换取信令简洁：不做"先分配再通知"的两步过程，UE 自己试错。代价是接收复杂度，收益是控制信令零配置开销。

### 编码：Polar（NR）/ TBCC（LTE）

- NR：DCI → CRC（24 bit，RNTI 加扰）→ Polar 编码（见 [[Polar_码]] 与 T10.6 的 CRC/RNTI 边界）。
- LTE：DCI → CRC（16 bit，RNTI 加扰）→ TBCC 编码（见 [[TBCC_咬尾卷积码]]）。

## 直观模型

PDCCH 盲检像"信箱没有门牌号的集体邮箱"：邮差（基站）把信（DCI）放进某个格子（CCE），居民（UE）每天按固定时段（monitor occasion）检查自己常看的格子组合（搜索空间），用钥匙（RNTI）试开——能打开的就是自己的信。收件人地址不在信封上，而在锁芯里。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PDCCH 只在下行 | PDCCH 是下行信道，但承载的 DCI 也调度上行（UL grant） |
| 盲检 = 随机猜 | 盲检按搜索空间配置的确定候选集试，非随机——复杂度受候选数约束 |
| RNTI 是用户地址 | RNTI 是临时标识，加扰在 CRC 上，不是 DCI 里的地址字段 |
| 聚合等级越大越好 | 聚合大=更可靠但占用 CCE 多，调度器按信道质量选择——1/2/4/8/16 自适应 |

## 协议锚点

- PDCCH 监测与搜索空间：TS 38.213（Rel-19 j30）§10，本地 `3GPP_Rel19/processed/TS_38.213_38213-j30`。
- PDCCH 结构与 CCE/REG：TS 38.211（Rel-19 j30）§7.3.2，本地 `TS_38.211_38211-j30`。
- RNTI 类型：TS 38.321（Rel-19 j20）§7.1（RNTI 值表），本地 `3GPP_Rel19/processed/TS_38.321_38321-j20`。
- LTE PDCCH：TS 36.211 §6.8（物理结构）、TS 36.212 §5.3.3（DCI 编码 TBCC），本地 `TS_36.211_*`/`TS_36.212_36212-j30`。
- 与译码衔接：Polar 控制译码的 CRC/RNTI 边界见 T10.6/T10.8（`docs/L2_协议算法/`）。

## PDCCH 在协议族中的分布（五层职责）

PDCCH 横跨五层规范，每层回答不同问题——理解协议间联系的关键是"分层职责"：

| 协议层 | 回答的问题 | 代表 TS（本地 Rel-19 资料） |
|:---|:---|:---|
| 物理信道 | PDCCH **长什么样**（CORESET/REG/CCE 结构与 Polar 编码） | TS 38.211 §7.3.2 |
| 信道编码 | 承载的 DCI **有哪些格式、字段是什么、CRC 怎么加扰** | TS 38.212 §7.3 |
| 物理层控制 | **什么时候监听、按什么候选集试**（监测时机、搜索空间、聚合等级） | TS 38.213 §10 |
| RRC 信令 | **去哪找**（SearchSpace/CORESET/PDCCH-Config 配置） | TS 38.331 |
| MAC | **身份怎么定**（RNTI 值表） | TS 38.321 §7.1 |

**联系链**：331 配好"去哪找"→ 211 定物理结构 → 212 定 DCI 内容 → 213 定"何时、按什么候选试"→ 321 用 RNTI 回答"是不是我的"。接收端闭环：盲检（T14.1）产出 DCI → 字段解析（T14.2）→ 译码器 descriptor（T9.0）。

## 关键要点

1. PDCCH 承载 DCI，是全链路调度入口；是下行信道，但同样下发上行授权。
2. CCE 是最小分配单位，聚合等级 1/2/4/8/16 按信道质量自适应。
3. 盲检不是随机猜：按搜索空间候选集 + RNTI 集 + DCI 尺寸逐个试。
4. RNTI 加扰在 CRC 上，不在 DCI 字段里。
5. NR 用 Polar + 24 bit CRC；LTE 用 TBCC + 16 bit CRC。
6. 工程核心矛盾：盲检复杂度 vs 零配置开销。

## 图谱关联

- [[概念图谱入口]]
- [[DCI_下行控制信息]]
- [[TBCC_咬尾卷积码]]
- [[Polar_码]]
- [[Physical_Channels_物理信道]]
- [[PBCH_MIB_广播信道]]
- [[PCFICH_物理控制格式指示信道]]（LTE 控制域 OFDM 符号数指示，解 PDCCH 的前提）
- [[Scheduling_Grant_调度与授权]]
- [[Scheduler_MAC调度器与资源分配]]
- [[T14.1_PDCCH_blind_decoding|T14.1 PDCCH 盲检]]
- 关系语义：PDCCH 是控制面调度入口——盲检拿到 DCI（下行控制信息）→ 解析出 descriptor 字段（T9.0）；其编码随制式（NR Polar/LTE TBCC）挂到两个编码家族；MIB 的 pdcch-ConfigSIB1 把广播信道接到这里的 CORESET 0 盲检。
