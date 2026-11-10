---
type: definition
aliases:
  - 跨时隙调度
  - Cross-slot Scheduling
  - 跨slot调度
  - crossSlot
tags:
  - 3gpp
  - concepts
  - scheduling
  - power-saving
source_spec: "TS 38.213 Rel-19 §10.1; TS 38.214 Rel-19 §5.1.2.1/§6.1.2.1"
queries: 1
---

# Cross-slot Scheduling 跨时隙调度

跨时隙调度是 PDCCH（物理下行控制信道，Physical Downlink Control Channel）与其调度的数据信道不在同一个时隙（slot）的调度方式：基站在第 n 个时隙下发 DCI（下行控制信息，Downlink Control Information），数据在第 n+k0（下行）或第 n+k2（上行）个时隙才出现。它与同时隙调度（k0=0）相对，核心动机是 UE（用户设备，User Equipment）节能。一句话本质：**跨时隙调度是"下单与送达分开"的调度——用调度时延换 UE 关射频省电的机会**。

## 解释目标与范围

本节目标：解释 k0/k2 时序参数的含义、跨时隙调度与同时隙调度的取舍、minimumSchedulingOffsetK0/K2 的节能机制，并与 DCI/PDCCH 概念和 T14.1 盲检讲义衔接。

## 起源与演进

(1) **起点：同时隙调度的待机功耗。** 同时隙调度（k0=0）下，UE 每个时隙都要先把 PDCCH 译完才知道有没有自己的数据——射频与译码器几乎常开，待机功耗高。

(2) **解法：数据晚 k0/k2 个时隙出现。** DCI 的时域资源分配字段从 RRC 配置的分配表里选一行（起始符号 S、长度 L 与时隙偏移），数据在 PDCCH 之后第 k0（下行）/k2（上行）个时隙出现。

(3) **节能机制：最小偏移承诺。** Rel-16 引入 minimumSchedulingOffsetK0/K2，承诺"数据最早 k 个时隙后才到"——UE 收到 DCI 后即可关闭射频休眠、到点再醒；配套还有 PDCCH 跳过（skipping）与搜索空间组切换。

(4) **代价与适用边界。** 调度时延变大，适合 eMBB 这类时延不敏感业务；URLLC 仍需同时隙调度。LTE 时代无此机制，Rel-16 之前的 NR 也没有——它是 5G 节能演进的一环。

## 科学定义

DCI 的时域资源分配字段从 RRC（无线资源控制，Radio Resource Control）配置的分配表中选出起始符号 S 与长度 L，并携带时隙偏移 k0（PDSCH）或 k2（PUSCH）：k0=0 即同时隙调度，k0>0 即跨时隙调度。Rel-16 起 RRC 可配置 minimumSchedulingOffsetK0/K2，向 UE 承诺"数据最早 k 个时隙之后才到"。

## 直观模型

跨时隙调度像点外卖：下单（DCI）和外卖送达（PDSCH）不在同一分钟。平台承诺"最快 40 分钟后送达"（minimumSchedulingOffset）——等餐的人就可以先睡一觉，到点再醒。UE 也一样：收到 DCI 后知道数据还有 k0 个时隙才来，中间可以关闭射频与部分译码电路省电。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 跨时隙调度降低时延 | 恰恰相反，它增加时延——用时延换 UE 省电，适合对时延不敏感的 eMBB 业务 |
| k0/k2 由 DCI 自由指示任意值 | DCI 只从 RRC 配置的时域分配表（几行候选）里选一行；minimumSchedulingOffset 只给下界 |
| 只有下行有跨时隙概念 | 上行同样有：PUSCH 在 slot n+k2，k2 语义与 k0 对称 |
| 配置了 minimumSchedulingOffset 就禁止跨时隙 | 它只禁止 k0 小于该下界；分配表中比下界大的跨时隙项仍可被 DCI 选中 |

## 协议锚点

- PDCCH 分配与时序：TS 38.213 Rel-19 §10.1（UE procedure for determining PDCCH assignment），本地 `3GPP_Rel19/processed/TS_38.213_38213-j30/content.md`。
- k0/k2 时域分配表：TS 38.214 Rel-19 §5.1.2.1（PDSCH）/§6.1.2.1（PUSCH），本地 `TS_38.214_38214-j30`。
- minimumSchedulingOffsetK0/K2：TS 38.331（IE `PDSCH-Config`/`PUSCH-ConfigCommon`，-r16/-r17），本地 `TS_38.331_38331-j20`。

## 跨时隙调度在协议族中的分布（五层职责）

| 协议层 | 回答的问题 | 代表 TS（本地 Rel-19 资料） |
|:---|:---|:---|
| 物理层过程 | k0/k2 **取什么值**（时域分配表、S+L 定义） | TS 38.214 §5.1.2.1/§6.1.2.1 |
| 物理层控制 | PDCCH **怎么监听**、DCI 与时序怎么配合 | TS 38.213 §10.1 |
| 信道编码 | DCI 里**时域资源分配字段与候选表** | TS 38.212 §7.3.1 |
| RRC 信令 | 分配表、minimumSchedulingOffsetK0/K2 **怎么配** | TS 38.331（PDSCH-Config/PUSCH-ConfigCommon） |
| UE 能力 | 节能相关能力声明 | TS 38.306（节能特征集，泛提） |

**联系链**：331 配置"候选偏移表 + 最小偏移承诺"→ 212 在 DCI 里留字段指向表项 → 213 规定监听与时序规则 → 214 定义每张表里 k0/k2 的具体含义 → 306 声明 UE 能利用承诺省多少电。整条链让"UE 何时可以放心关射频"成为收发双方的共同认知。

## 关键要点

1. 跨时隙调度 = PDCCH 与数据不同 slot（k0/k2 > 0），与同时隙调度（k0=0）相对。
2. 核心动机是 UE 节能：知道数据晚到，中间可关射频休眠。
3. k0/k2 从 RRC 配置的时域分配表里选，不是 DCI 自由指示任意值。
4. minimumSchedulingOffsetK0/K2 是"最早到货时间"承诺，Rel-16 引入。
5. 代价是调度时延，适用 eMBB；URLLC 不适合。
6. 上行 k2 与下行 k0 语义对称。

## 图谱关联

- [[概念图谱入口]]
- [[DCI_下行控制信息]]
- [[PDCCH_物理下行控制信道]]
- [[Scheduling_Grant_调度与授权]]
- [[BWP_带宽部分]]
- [[T14.1_PDCCH_blind_decoding]]
- 关系语义：跨时隙调度是 DCI 时域资源分配字段的时序语义——PDCCH 盲检拿到 DCI 后，k0/k2 决定译码链路何时启动、UE 射频何时可休眠。
