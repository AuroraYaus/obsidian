---
type: definition
aliases:
  - Bit-Exact
  - 比特精确
  - Regression
  - 回归测试
tags:
  - 3gpp
  - concepts
  - implementation
  - verification
  - bit-exact
source_spec: "Engineering methodology; decoder verification"
---

# Bit-Exact 回归验证

Bit-Exact 回归验证要求同一输入在所有实现层级（Python ↔ C/C++ ↔ RTL（寄存器传输级，Register Transfer Level））产生逐比特一致的输出。

## 独立解释任务

任务目标：解释分层比对框架中各层级的误差容限为何不同，以及 bit-exact 与功能正确之间的区别。

## 科学定义

设 $V$ 为协议向量集合，$A, B$ 为两个实现层级，bit-exact 定义为对每条向量输出比特串完全相等：

$$A \overset{\text{bit-exact}}{=} B \quad\Longleftrightarrow\quad \forall v \in V:\; A(v) = B(v)$$

分层框架的三级误差容限依次收紧：

- **Golden Reference**：Python 浮点实现，作为正确性基准，无量化误差。
- **定点比对**：C/C++ 定点模型 vs Golden，量化误差在容许范围内。
- **RTL 比对**：RTL vs 定点模型，必须 bit-exact，容差为零。
- **回归套件**：覆盖正常/边界/异常/重传 case。

## 直观模型

同一笔账由手算、Excel、银行流水三方对账：分毫不差才算平账，差一分钱都说明某处进位或舍入不一致。数值例子：某译码器对同一码块输入 16 bit LLR 向量，Golden 浮点与定点模型各自给出判决比特串，若第 17 位由 0 变 1，回归即失败——差异点直接指向溢出、舍入或状态机错误，而不是笼统的"结果不对"。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| bit-exact 要求所有层级与浮点 Golden 完全一致 | 浮点 Golden 是正确性基准；定点与 RTL 只需互相 bit-exact，与 Golden 的差距在量化容限内。 |
| 只比对最终 CRC 就足够 | 中途 checkpoint（各译码器内部状态）也要比对，才能定位首个发散点。 |
| bit-exact 等于功能正确 | 两个实现可能一致地错；bit-exact 保证一致性，正确性靠 Golden 基准与协议向量保证。 |
| 一条向量通过即宣告回归通过 | 正常/边界/异常/重传向量都要覆盖，单条通过不构成回归证据。 |

## 协议锚点

- 协议向量来源：TS 36.212 Rel-19 `36212-j30`（LTE Turbo 语义）、TS 38.212 Rel-19 `38212-j30`（NR Polar/LDPC 语义）。
- 本地锚点：`3GPP_Rel19/processed/TS_36.212_36212-j30`；`3GPP_Rel19/processed/TS_38.212_38212-j30`。
- 协议边界：TS 不规定回归框架、文件命名、CI 命令或 RTL 端口；协议只规定每串逻辑比特和校验语义应是什么。bit-exact 验证属工程方法论，非 3GPP 标准。

## 图谱关联

- [[Golden_Model_黄金模型]]
- [[Fixed_Point_Numbers_定点数]]
- [[RTL_Microarchitecture_RTL微架构]]
- [[概念图谱入口]]
- [[T5.5_decoder_hardware_verification_mindset]]
- [[T18.6_bit_exact_regression_harness]]
- [[T20.1_decoder_testbench_architecture]]
- [[T21.6_throughput_and_full_link_roi]]
- 关系语义：Bit-Exact 是验收标准——所有层级必须一致。
