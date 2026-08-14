---
type: definition
aliases:
  - Incremental Redundancy
  - IR
  - 增量冗余
tags:
  - 3gpp
  - concepts
  - harq
  - combining
  - ir
source_spec: "TS 36.213; TS 38.214 §5.1.7"
---

# Incremental Redundancy (IR)

## 独立解释任务

任务目标：解释增量冗余（Incremental Redundancy, IR）如何通过每次重传选取不同冗余版本（Redundancy Version, RV）、发送不同校验位，让有效码率随重传逐次降低，从而同时获得能量增益与编码增益。在 LTE/NR 译码链路中的位置：位于混合自动重传请求（Hybrid Automatic Repeat Request, HARQ）软合并（Soft Combining）环节——解速率匹配按 RV 计算起点 $k_0$，把本次 LLR 回填到循环缓存（Circular Buffer）正确位置并与旧 LLR 合并。

## 科学定义

IR 的核心是重传不同位置的编码比特：发送端把母码比特放入循环缓存，每次传输按 RV 决定读取起点。LTE Turbo 的起点公式为：

$$
k_0=R_{\mathrm{TC}}^{\mathrm{subblock}}\left[2\left\lceil\frac{N_{\mathrm{cb}}}{8R_{\mathrm{TC}}^{\mathrm{subblock}}}\right\rceil\mathrm{rv}_{\mathrm{idx}}+2\right]
$$

其中 $R_{\mathrm{TC}}^{\mathrm{subblock}}$ 为子块交织（Sub-Block Interleaver）行数、$N_{\mathrm{cb}}$ 为循环缓存长度、$\mathrm{rv}_{\mathrm{idx}}\in\{0,1,2,3\}$。接收端按编码位置合并各次 LLR：重复位置相加、未出现位置保留旧值、新位置补充全新校验证据。合并后等效码率随重传次数下降——初传码率 $3/4$ 的码块补充新校验位后等效码率可降至 $3/8$，译码器同时获得更多接收能量（能量增益，Energy Gain）与更低码率带来的编码增益（Coding Gain）。典型 RV 使用顺序：LTE 常为 $[0,2,1,3]$、NR 常为 $[0,2,3,1]$（常见序列，协议不强制）。

## 直观模型

把母码想成一圈货架。初传码率 $3/4$ 时只能取走四分之三的货物，剩下四分之一的校验货留在架上。第一次重传不重复取同一批货，而从货架另一起点取新的校验货物；接收端把两批货物拼在一起，码字码率更低、证据更全。若重传仍取同一批货（Chase 合并），码率不变，只增加接收能量；IR 则同时增加覆盖范围。接收端对重复覆盖的货位把新旧 LLR 相加、对本次没取到的货位保留旧 LLR，绝不能把"没收到"当成比特 0。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| IR 只是把同一份数据再发一遍 | IR 每次用不同 RV 发送不同校验位；重复相同位置的是 Chase 合并。 |
| 新 RV 的位置一定无重叠 | 窗口长度与 $N_{\mathrm{cb}}$ 限制可能造成重叠；重叠位置相加、未出现位置保留旧值。 |
| RV 顺序固定为 0,1,2,3 | 调度可选用其他序列（LTE 常 $[0,2,1,3]$、NR 常 $[0,2,3,1]$）；译码器必须按 $\mathrm{rv}_{\mathrm{idx}}$ 计算 $k_0$。 |
| 重传只带来能量增益 | IR 同时带来编码增益（等效码率降低），这是它优于 Chase 的根本原因。 |
| IR 只适用于 LTE Turbo | NR LDPC 同样通过 TS 38.212 §5.4.2.1 的 $k_0$ 规则实现 IR。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 `36212-j30` §5.1.4.1、§5.1.4.1.2（bit collection、circular buffer、$k_0$ 与 `rvidx`）：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md` 行 777-789、817-923。
- LTE 过程侧：TS 36.213 §8.3、§8.6、§8.6.1 与 TS 36.321 §5.3.2（HARQ 过程与 MAC 层 HARQ 实体）。
- NR：TS 38.212 Rel-19 `38212-j30` §5.4.2.1（LDPC bit selection，Table 5.4.2.1-2 给出 $k_0$）：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 1179-1309；调度上下文见 TS 38.214 §5.1.3、§6.1.4。

## 图谱关联

- [[Chase_Combining_Chase合并]]
- [[HARQ_混合自动重传请求]]
- [[RV_冗余版本]]
- [[Circular_Buffer_循环缓存]]
- [[Soft_Buffer_软缓存]]
- [[Rate_Matching_速率匹配]]
- [[T4.3_HARQ_soft_combining_basics]]
- [[T11.3_HARQ_soft_buffer_comparison]]
- [[T7.3_LTE_HARQ_soft_buffer_RV]]
- [[概念图谱入口]]
- 关系语义：IR 是 LTE/NR HARQ 标准模式，编码增益超越 CC。
