---
type: definition
aliases:
  - HARQ
  - Hybrid Automatic Repeat Request
  - 混合自动重传请求
  - HARQ process
tags:
  - 3gpp
  - concepts
  - harq
source_spec: "TS 36.213 Rel-19 HARQ anchors; TS 38.214 Rel-19 §5.1.7 and §6.1.5; TS 36.321/38.321 MAC HARQ anchors"
---

# HARQ 混合自动重传请求

HARQ 把前向纠错和自动重传结合起来。接收端在 CRC 失败后保留同一 HARQ process 的软信息，后续重传按 RV 和调度上下文补充新的接收证据。

## 独立解释任务

任务目标：解释 HARQ 如何把 CRC 结果、RV、soft buffer 和 ACK/NACK 组织成闭环。

## 科学定义

HARQ 是链路层/物理层协同的可靠性机制。接收端先用 FEC 译码尝试恢复 TB 或控制对象；若 CRC 失败，则通过反馈或调度流程进入重传。与普通 ARQ 不同，HARQ 可以保留失败传输的软信息，并在后续重传中继续利用这些证据。

## 直观模型

HARQ 不是“错了重做一遍”，更像“第一次证据不够，第二次补证据”。第一次译码失败留下的 LLR 仍可能方向正确，只是可靠度不足；重传带来的新 LLR 与旧 LLR 合并后，译码器看到的证据更完整。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| HARQ 是译码算法 | HARQ 是重传与合并流程，译码核心仍是 Turbo/LDPC/Polar 等。 |
| CRC fail 就丢掉所有软信息 | 同一 HARQ process 的失败软信息通常可以保留等待重传。 |
| RV 等于 HARQ process | RV 描述冗余选择，HARQ process 描述并行传输上下文。 |

## 协议锚点

- LTE：TS 36.213 Rel-19 HARQ/RV 相关过程，精确分册按具体上下行章节核验。
- NR：TS 38.214 Rel-19 §5.1.7 PDSCH CBG/HARQ 上下文。
- NR：TS 38.214 Rel-19 §6.1.5 PUSCH CBG/HARQ 上下文。
- MAC：TS 36.321/TS 38.321 Rel-19 HARQ entity 和 HARQ process 行为。

## 图谱关联

- [[Chase_Combining_Chase合并]]
- [[Incremental_Redundancy_增量冗余]]
- [[Circular_Buffer_循环缓存]]
- [[概念图谱入口]]
- [[CRC_循环冗余校验]]
- [[RV_冗余版本]]
- [[Soft_Buffer_软缓存]]
- [[LLR_对数似然比]]
- [[TB_传输块]]
- [[CBG_码块组]]
- [[T4.3_HARQ_soft_combining_basics]]
- [[T7.3_LTE_HARQ_soft_buffer_RV]]
- [[T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0]]
- [[T11.3_HARQ_soft_buffer_comparison]]
- [[HARQ_Process_HARQ进程管理]]
- [[Scheduler_MAC调度器与资源分配]]
- 关系语义：HARQ 使用 CRC 结果决定保留、释放或继续合并 soft buffer，RV 决定重传证据对应的编码位置。
