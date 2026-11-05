---
type: definition
aliases:
  - Rate Matching
  - Rate Recovery
  - 速率匹配
  - 解速率匹配
  - de-rate matching
tags:
  - 3gpp
  - concepts
  - rate-matching
source_spec: "TS 36.212 Rel-19 §5.1.4; TS 38.212 Rel-19 §5.4.1 and §5.4.2"
queries: 1
---

# Rate Matching 速率匹配

速率匹配把编码后比特适配到本次可发送资源；接收端的 rate recovery 则把收到的 LLR 放回编码器母码或 circular buffer 坐标。它是 HARQ/RV 和译码核心之间的地址桥。

## 独立解释任务

任务目标：解释速率匹配如何连接无线资源数量、RV 和译码器输入坐标。

## 科学定义

编码器输出的母码长度通常不等于本次无线资源承载的 bit 数。速率匹配通过 puncturing、repetition、shortening、interleaving 和 bit selection 等操作选择实际发送序列。接收端执行 rate recovery，把空口顺序 LLR 恢复到译码器需要的母码位置。

## 直观模型

速率匹配像从一本完整教材里按本次课时挑页打印。RV 告诉你从哪里开始挑，资源数量告诉你挑多少页。接收端拿到打印页后，要按页码放回原书，而不是按收到顺序直接阅读。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| rate recovery 只是补零 | 它是带地址和 mask 的反向映射。 |
| RV 只影响 HARQ | RV 直接影响 rate recovery 地址。 |
| punctured、filler、unknown 都一样 | 三者 LLR 语义不同，必须用 mask 区分。 |

## 协议锚点

- LTE：TS 36.212 Rel-19 §5.1.4 Turbo rate matching。
- NR Polar：TS 38.212 Rel-19 §5.4.1。
- NR LDPC：TS 38.212 Rel-19 §5.4.2。

## 速率匹配在协议族中的分布（五层职责）

速率匹配横跨五层规范，每层回答不同问题——理解协议间联系的关键是"分层职责"：

| 协议层 | 回答的问题 | 代表 TS（本地 Rel-19 资料） |
|:---|:---|:---|
| 信道编码 | **算法本体**：母码按 RV 起点截出每 CB 的 E 比特（比特选择） | TS 36.212 §5.1.4（Turbo）/TS 38.212 §5.4.1（Polar）/§5.4.2（LDPC） |
| 物理层过程 | **可用资源总数 G 从哪来**（MCS/PRB 数 → TBS → G → 每 CB 输出 E） | TS 38.214 §5.1.3（NR PDSCH TBS）/TS 36.213 §7.1.7（LTE TBS） |
| 物理层控制 | **MCS/RV/资源分配由谁指示** | TS 38.212 §7.3（DCI 字段） |
| RRC 信令 | **哪些 RE 不能用**（rateMatchPattern 打孔/避让） | TS 38.331（RateMatchPattern IE） |
| MAC | **调度决策与 HARQ 信息**（TB 大小、重传 RV 选择） | TS 38.321 §5.3.2.2 |

**联系链**：MAC 决定 TB 大小与调度 → 213/214 定出总资源 G 与 TBS → 212 把母码按 RV 起点截出每 CB 的 E 比特 → 331 挖掉 rateMatchPattern 覆盖的 RE → 接收端 rate recovery 把 LLR 放回母码坐标（本笔记职责）。

## 图谱关联

- [[Circular_Buffer_循环缓存]]
- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[RV_冗余版本]]
- [[Soft_Buffer_软缓存]]
- [[LDPC_低密度奇偶校验码]]
- [[Turbo_码]]
- [[Polar_码]]
- [[T7.1_LTE_Turbo_de_rate_matching_overview]]
- [[T9.1_NR_LDPC_rate_recovery_overview]]
- [[T10.7_NR_Polar_rate_recovery]]
- 关系语义：rate matching/recovery 决定 LLR 从空口顺序到译码核心坐标的映射。
