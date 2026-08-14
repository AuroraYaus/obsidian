---
type: definition
aliases:
  - Layered Decoding
  - 分层译码
  - Flooding
  - Row-Layered
tags:
  - 3gpp
  - concepts
  - ldpc
  - algorithm
  - schedule
source_spec: "Algorithmic; hardware implementation of LDPC decoding"
---

# LDPC 分层译码调度

## 独立解释任务

任务目标：解释 LDPC 译码器中校验节点（Check Node, CN）与变量节点（Variable Node, VN）消息按什么顺序更新、何时写回，说明分层调度（Layered Schedule）为什么通常比泛洪调度（Flooding Schedule）收敛更快。在 LTE/NR 译码链路中的位置：NR LDPC 译码器迭代核心的消息更新时序安排——同一个 $H$、同一套最小和（Min-Sum）节点单元，仅写回顺序不同，收敛速度与存储压力就不同。

## 科学定义

泛洪调度把一轮迭代分成两个阶段：先用上一轮全部 VN 消息计算全部 CN 消息，再统一更新全部 VN 后验值。它需要两套消息存储，读写相位分开，但同一轮内新消息不能立即被利用。分层调度把 $H$ 的行按 layer 分组，逐层执行"CN 更新 → 立即读改写（Read-Modify-Write, RMW）该层涉及的 VN 后验值 → 进入下一层"：后一层立即看到前一层刚更新的 VN 值，同一轮迭代内新证据即刻传播。

工程上每个 layer 通常对应基图的一个行组（row group）：BG1 的 layer 索引为 0 到 45，BG2 为 0 到 41，组内 $Z_c$ 个 bit-level 行可并行处理。收敛收益来自信息传播路径变短，工程上常以约一半的迭代次数达到与泛洪相同的纠错性能。

## 直观模型

把译码比作批改成绩：泛洪是全部老师同时批改、再统一公布，公布前谁都不知道别人的最新结果；分层则是逐科批改、逐科公布，下一科老师批改时已经看到前面科目的最新成绩。若两个 CN 共享一个 VN，分层调度下第二个 CN 计算时该 VN 已经吸收第一个 CN 的新证据，一次迭代就完成两次信息交换；泛洪要等到下一轮才能利用。代价是分层引入顺序依赖：后一层必须等待前一层写回（读后写冒险，Read-After-Write Hazard），并行度受限；多行同时访问同一列组时还会出现存储体冲突（Bank Conflict），需要流水调度或地址映射化解。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 分层调度改变校验关系 | 只改变消息更新时间；$H$、CN/VN 更新公式与收敛结果不变。 |
| layered 是 3GPP 强制算法 | TS 38.212 只定义基图与 $H$；调度方式是接收机实现策略（非 3GPP 标准）。 |
| 泛洪一无是处 | 泛洪阶段边界清晰、无读写冒险，适合参考模型与教学验证。 |
| 一个 layer 等于一行 | layer 通常对应基图一个行组，组内含 $Z_c$ 行，可并行更新。 |
| 分层无条件更快 | 需要处理 RMW 冒险、bank conflict 与流水停顿，收益依赖硬件调度质量。 |

## 协议锚点

- 协议锚点：TS 38.212 Rel-19 `38212-j30` §5.3.2（定义基图、提升与完整 $H$）：`3GPP_Rel19/processed/TS_38.212_38212-j30/content.md` 行 948-989。
- 调度方式本身非 3GPP 标准：TS 38.212 不规定译码器消息更新顺序，flooding/layered 均为接收端实现选择。

## 图谱关联

- [[QC_LDPC_准循环LDPC]]
- [[Sum_Product_Algorithm_和积算法]]
- [[Min_Sum_Algorithm_最小和算法]]
- [[Iterative_Decoding_迭代译码]]
- [[T8.7_layered_LDPC_decoding_schedule]]
- [[T8.6_LDPC_MS_NMS_OMS]]
- [[T19.2_NR_LDPC_RTL_microarchitecture]]
- [[概念图谱入口]]
- 关系语义：分层调度是 LDPC 硬件关键优化。
