---
type: definition
aliases:
  - Chase Combining
  - CC
  - Chase合并
  - 软合并
tags:
  - 3gpp
  - concepts
  - harq
  - combining
source_spec: "TS 36.213; TS 38.214 §5.1.7"
---

# Chase Combining (CC)

## 独立解释任务

任务目标：解释混合自动重传请求（Hybrid Automatic Repeat reQuest, HARQ）中最简单的软合并方式——Chase 合并（Chase Combining, CC）：重传相同编码比特、接收端按编码位置累加 LLR 的原理、增益来源与适用边界。

CC 位于接收端解速率匹配之后、信道译码之前：把多次传输的对数似然比（Log-Likelihood Ratio, LLR）在软缓存（Soft Buffer）中按编码位置合并后送入译码器。

## 科学定义

Chase 合并假设每次重传发送相同（或高度相同）的编码比特，同一编码位置的 LLR 直接相加：

$$LLR_{\mathrm{combined}}(p) = LLR_{\mathrm{old}}(p) + LLR_{\mathrm{retx}}(p)$$

$p$ 是解速率匹配后得到的编码位置。物理含义：独立观测的证据按对数似然的可加性合并，同号证据相加增强、异号证据相加抵消（绝对值变小）。每次重传使同一位置的接收能量翻倍，等效信噪比提升约 3 dB（$10\cdot\log_{10} 2\approx 3.01$ dB）——这是纯能量增益。硬件上用饱和加法防止多次合并溢出。CC 与增量冗余（Incremental Redundancy, IR）的本质区别：CC 只叠加能量、不引入新校验比特，因此没有编码增益。

## 直观模型

第一次接收某编码位置 LLR=+0.8（略偏向 0），译码后 TB CRC 失败；重传同一位置得到 LLR=+1.5。合并后 +2.3，判决明显更可信。若重传给出 −1.5，合并后 −0.7——原判决反而被动摇。类比：两位证人独立描述同一事件，说法一致时信心倍增，说法矛盾时整体置信度下降，而不是"取更相信的那位"。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CC 是重发整包并替换旧数据 | 接收端必须保留旧 LLR 并逐位置相加，而不是覆盖。 |
| CC 能带来编码增益 | CC 只有能量增益（约 3 dB/次），编码增益来自 IR 的新增校验比特。 |
| 合并后 LLR 幅度一定变大 | 符号冲突的证据相加后绝对值可能变小。 |
| 接收端可以随意决定怎么加 | 必须先按协议 RV（冗余版本，Redundancy Version）规则确定每个 LLR 的编码位置，否则合并错位。 |
| CC 与 IR 是互斥的两条路 | 真实 LTE/NR rate matching 常同时出现重复位置（相加）与新增位置（写入空位）。 |

## 协议锚点

- LTE：TS 36.212 §5.1.4.1 Turbo rate matching 使用 circular buffer 与 `rvidx`。本地：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`。
- NR：TS 38.212 §5.4.2 LDPC rate matching，RV 取 `0,1,2,3` 决定起点 `k0`。本地：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 1175-1309。
- NR：TS 38.214 §5.1 规定 HARQ process 数量、NDI 与调度边界。本地：`3GPP_Rel19/processed/TS_38.214_38214-j30/content.md`。
- LLR 相加公式为接收端工程模型，非 3GPP 原文公式；讲义：`docs/L1_基础/T4.3_HARQ_soft_combining_basics.md`。

## 图谱关联

- [[HARQ_混合自动重传请求]]
- [[LLR_对数似然比]]
- [[Soft_Buffer_软缓存]]
- [[Incremental_Redundancy_增量冗余]]
- [[HARQ_Process_HARQ进程管理]]
- [[RV_冗余版本]]
- [[概念图谱入口]]
- [[T4.3_HARQ_soft_combining_basics]]
- [[T7.3_LTE_HARQ_soft_buffer_RV]]
- 关系语义：CC 是 IR 的退化情况，实现最简单，是软合并机制的教学入口。
