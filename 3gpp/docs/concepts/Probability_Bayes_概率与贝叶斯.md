---
type: definition
aliases:
  - Probability
  - Bayes Theorem
  - 条件概率
  - 贝叶斯定理
  - MAP
tags:
  - 3gpp
  - concepts
  - math
  - probability
  - bayes
source_spec: "Algorithmic receiver concept"
---

# 概率与贝叶斯推断

概率论为噪声信道下的译码提供数学基础。贝叶斯定理将先验信念与观测证据结合，产出后验概率——所有软输入软输出（SISO）译码器的推理核心。

## 核心概念

- **条件概率 P(A|B)**：已知 B 发生时 A 的概率。译码中：P(x|y) 已知接收信号求发送比特的概率。
- **贝叶斯定理**：P(x|y) = P(y|x)·P(x) / P(y)。似然来自信道模型，先验来自外信息。
- **MAP 准则**：选后验概率最大的 x，即 argmax_x P(x|y)——最优符号判决准则。

## 图谱关联

- [[GF2_伽罗瓦域]]
- [[LLR_对数似然比]]
- [[Iterative_Decoding_迭代译码]]
- [[T1.4_probability_bayes_soft_decoding]]
- 关系语义：贝叶斯推断是 LLR 定义和 BCJR 算法的概率基础。
