---
type: definition
aliases:
  - 链路自适应
  - Link Adaptation
  - CQI PMI RI
  - 信道状态信息 CSI
tags:
  - 3gpp
  - concepts
  - protocol
  - l2
source_spec: "TS 38.214 Rel-19 §5.2; TS 38.213 Rel-19 §9; TS 38.331 Rel-19 §6.3.2"
---

# Link Adaptation 链路自适应与CQI

链路自适应（Link Adaptation）让传输速率跟着信道走：UE（用户设备，User Equipment）测量下行 CSI-RS（信道状态信息参考信号，Channel State Information Reference Signal）的 SINR（信干噪比，Signal-to-Interference-plus-Noise Ratio），折算成 CQI（信道质量指示，Channel Quality Indicator）上报，基站据此选择 MCS（调制与编码方案，Modulation and Coding Scheme）——信道好就传得快、信道差就传得稳。它由 CSI（信道状态信息，Channel State Information）反馈环路驱动，是 [[Scheduler_MAC调度器与资源分配]] 的频率选择性调度与 MCS 选择的上游输入。

## 独立解释任务

任务目标：讲清链路自适应闭环（测量→CQI→MCS→反馈→修正）、CQI/PMI/RI 三件报告的内容与作用、CQI 报告的周期/非周期与宽带/子带类型，以及 outer loop（外环）如何用 ACK/NACK 校准 CQI 误差。

## 科学定义

### 链路自适应闭环

```
UE 测 CSI-RS SINR（T2.11）→ 折算 CQI（满足 BLER≤10% 的最大可支持 MCS）
→ PUCCH/PUSCH 上报
→ gNB 调度器选 MCS/资源
→ 传输 → UE 译码（BLER 目标验证）→ ACK/NACK
→ outer loop：连续 NACK 下调 SINR 折算偏置、连续 ACK 上调（校准 CQI 误差）
```

其中 CSI 上报与 HARQ-ACK 反馈均经 PUCCH（物理上行控制信道，Physical Uplink Control Channel）[[PUCCH_上行控制信道与UCI]]/PUSCH（物理上行共享信道，Physical Uplink Shared Channel）承载；gNB（5G 基站，gNodeB）的 MCS 选择与资源分配决策见 [[Scheduler_MAC调度器与资源分配]]。

### CQI/PMI/RI 三件报告

| 报告 | 内容 | 作用 |
|:---|:---|:---|
| CQI（信道质量指示，Channel Quality Indicator） | 4-bit 索引（0-15），每值对应一个调制阶数+码率组合 | 决定 MCS 选择 |
| PMI（预编码矩阵指示，Precoding Matrix Indicator） | 码本索引，指示期望的预编码矩阵 | 波束/层成形（与 [[Precoding_预编码]] 衔接） |
| RI（秩指示，Rank Indicator） | 建议的传输层数 | 决定 MIMO 层数与码率换算 |

三件合称 CSI；CQI 按 RI 假设折算（层数不同码率口径不同）。CQI 表定义在 TS 38.214 §5.2.2.1（4-bit 表与 5-bit 表）。

### CQI 报告类型

| 维度 | 类型 | 承载 |
|:---|:---|:---|
| 触发 | 周期（RRC（无线资源控制，Radio Resource Control）配置周期）/ 非周期（DCI（下行控制信息，Downlink Control Information）触发） | 周期走 PUCCH，非周期走 PUSCH（容量大） |
| 频域粒度 | 宽带（一个 CQI 覆盖全带宽）/ 子带（每子带一个 CQI） | 宽带省开销、子带支持频率选择性调度 |

### outer loop 的修正原理

CQI 是 UE 的「预测」——测量误差、信道变化、干扰波动都会让它偏乐观/悲观。outer loop 用真实传输结果（ACK/NACK）修正：NACK 说明 CQI 偏乐观（降低折算 SINR 偏置），连续 ACK 说明偏悲观（上调）——把实际 BLER（块错误率，Block Error Rate）拉回目标值（10%）。它是闭环的自校准层。

## 直观模型

链路自适应像「自助餐配菜」：顾客（UE）先报「我胃口怎么样」（CQI 报 SINR 折算），厨师（调度器）按胃口配菜量（MCS）；吃完反馈「咸淡」（ACK/NACK），厨师调盐（outer loop 修正）——下一次配菜更准。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| CQI 越高越好 | CQI 反映可支持的 MCS 上限，调度器还要结合资源/QoS（服务质量，Quality of Service）选实际 MCS |
| CQI 就是 SINR | CQI 是 SINR 按 BLER 目标折算后的索引——同样的 SINR 可对应不同 CQI（不同 BLER 目标） |
| PMI/RI 只影响下行 | 上行用 SRS（探测参考信号，Sounding Reference Signal）探测与 TPMI（传输预编码矩阵指示，Transmitted Precoding Matrix Indicator）指示（TDD（时分双工，Time Division Duplexing）互易性/码本） |
| 一次上报就够了 | CQI 会过时，周期/非周期上报持续跟踪信道变化 |

## 协议锚点

- CSI 报告配置与 CQI 表：TS 38.214（Rel-19 j30）§5.2，本地 `3GPP_Rel19/processed/TS_38.214_38214-j30`。
- PUCCH/PUSCH 承载 CSI：TS 38.213（Rel-19 j30）§9.2，本地 `TS_38.213_38213-j30`。
- CSI 配置参数：TS 38.331（Rel-19 j20）§6.3.2（CSI-ReportConfig），本地 `TS_38.331_38331-j20`。
- 测量侧衔接：T2.11（CSI/SINR，`docs/L1_基础/`）、[[CSI_SINR]]。

## 图谱关联

- [[概念图谱入口]]
- [[Scheduler_MAC调度器与资源分配]]
- [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]
- [[CSI_SINR]]
- [[PUCCH_上行控制信道与UCI]]
- 关系语义：链路自适应把「信道质量」变成「传输参数」——CSI 测量（T2.11）→ CQI/PMI/RI 上报（PUCCH/PUSCH）→ 调度器选 MCS（MCS 表）→ 传输；outer loop 用 HARQ（混合自动重传请求，Hybrid Automatic Repeat Request）反馈（ACK/NACK）校准，是物理层与 MAC 层耦合最紧的闭环。
