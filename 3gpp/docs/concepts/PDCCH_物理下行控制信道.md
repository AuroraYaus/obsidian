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
---

# PDCCH 物理下行控制信道

PDCCH（物理下行控制信道，Physical Downlink Control Channel）承载 DCI（下行控制信息，Downlink Control Information）——基站调度指令的载体。UE 在每个监测时机（monitor occasion）对一组候选 PDCCH 做盲检测（blind decoding）：不知道 DCI 发给谁、多大、放在哪，就按聚合等级逐个试，用 CRC（循环冗余校验，Cyclic Redundancy Check）加扰的 RNTI（无线网络临时标识，Radio Network Temporary Identifier）判断"这是不是给我的"。盲检是全链路调度入口的核心机制，也是控制面最独特的工程问题。

## 独立解释任务

任务目标：讲清 PDCCH 的时频结构（CORESET/REG/CCE/聚合等级）、搜索空间、盲检流程与 RNTI 机制，说明为什么控制信道需要盲检而数据信道不需要，并与 Polar（极化码，Polar Code）控制译码（T10.6）和 DCI 解析（[[DCI_下行控制信息]]）衔接。

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

## 图谱关联

- [[概念图谱入口]]
- [[DCI_下行控制信息]]
- [[TBCC_咬尾卷积码]]
- [[Polar_码]]
- [[Physical_Channels_物理信道]]
- [[PBCH_MIB_广播信道]]
- [[Scheduling_Grant_调度与授权]]
- [[Scheduler_MAC调度器与资源分配]]
- 关系语义：PDCCH 是控制面调度入口——盲检拿到 DCI（下行控制信息）→ 解析出 descriptor 字段（T9.0）；其编码随制式（NR Polar/LTE TBCC）挂到两个编码家族；MIB 的 pdcch-ConfigSIB1 把广播信道接到这里的 CORESET 0 盲检。
