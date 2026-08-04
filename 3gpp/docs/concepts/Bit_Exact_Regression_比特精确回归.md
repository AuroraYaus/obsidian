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

同一输入在所有实现层级（Python↔C/C++↔RTL）产生逐比特一致输出。

- **Golden Reference**：Python 浮点→正确性基准。
- **定点比对**：C/C++ vs Golden→量化误差在容许范围。
- **RTL 比对**：RTL vs 定点→必须 bit-exact。
- **回归套件**：覆盖正常/边界/异常/重传 case。

## 图谱关联

- [[Golden_Model_黄金模型]]
- [[Fixed_Point_Numbers_定点数]]
- [[RTL_Microarchitecture_RTL微架构]]
- [[T5.5_decoder_hardware_verification_mindset]]
- [[T18.6_bit_exact_regression_harness]]
- [[T20.1_decoder_testbench_architecture]]
- [[T21.6_throughput_and_full_link_roi]]
- 关系语义：Bit-Exact 是验收标准——所有层级必须一致。
