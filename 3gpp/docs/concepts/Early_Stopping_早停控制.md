---
type: definition
aliases:
  - Early Stopping
  - 早停控制
  - CRC gated stopping
  - syndrome stopping
tags:
  - 3gpp
  - concepts
  - early-stopping
source_spec: "Algorithmic receiver control; CRC anchors in TS 36.212/38.212"
---

# Early Stopping 早停控制

早停控制是在译码迭代或路径搜索过程中用 syndrome、CRC 或路径选择条件提前结束无意义计算。它是实现策略，但必须尊重协议定义的 CRC 和输出验收边界。

## 独立解释任务

任务目标：解释早停如何在性能、时延、功耗和误通过风险之间折中。

## 科学定义

早停是接收端实现策略。迭代译码器每轮会得到新的候选 bit 或可靠度状态；如果 syndrome、CRC、路径度量或其他门控条件已经满足设计要求，就可以提前终止后续计算。协议通常规定验收对象和 CRC 边界，不规定厂商内部第几轮必须停。

## 直观模型

早停像考试提前交卷。题目已经全部核对无误时，继续检查收益很小；但如果检查标准不严，可能把错误答案提前交出去。因此早停要把节省功耗和避免误通过一起考虑。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| syndrome pass 等于 TB pass | syndrome 是编码约束，TB 交付还要看 CRC 和重组边界。 |
| 早停是 3GPP 固定公式 | 早停策略多为实现设计。 |
| 越早停越好 | 早停要控制误停、CRC latency 和 pipeline flush 风险。 |

## 协议锚点

- CRC 验收边界：TS 36.212 Rel-19 §5.1.1；TS 38.212 Rel-19 §5.1。
- LDPC syndrome 语义来自奇偶校验矩阵和 Tanner 图算法，不是单独的 3GPP 停止公式。
- Polar CA-SCL 的 CRC 辅助选择与 TS 38.212 控制信息 CRC 章节相关。

## 图谱关联

- [[概念图谱入口]]
- [[CRC_循环冗余校验]]
- [[LDPC_低密度奇偶校验码]]
- [[Turbo_码]]
- [[Polar_码]]
- [[T4.4_early_stopping_crc_gated_control]]
- [[T10.6_CRC_aided_SCL_control_reliability]]
- 关系语义：早停控制依赖 CRC/syndrome/path metric 等检查，影响迭代次数、功耗、延迟和误通过风险。
