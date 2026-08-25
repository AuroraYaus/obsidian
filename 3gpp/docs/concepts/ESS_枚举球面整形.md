---
type: definition
aliases:
  - ESS
  - Enumerative Sphere Shaping
  - 枚举球面整形
  - 能量球约束
  - DP 计数表
tags:
  - 3gpp
  - concepts
  - probability-shaping
source_spec: "非 3GPP 标准（6G 候选）; Qualcomm evaluation-link-simulator"
queries: 1
---

# ESS 枚举球面整形

ESS（Enumerative Sphere Shaping）是概率整形采用的 DM 实现：在"总能量不超过上限"的能量球约束下，用 DP 计数表把均匀 bit（转成 rank）可逆地映射为非均匀幅度序列。

## 独立解释任务

任务目标：解释 ESS 如何在能量球约束下用 DP 计数表把均匀 bit 可逆映射为非均匀幅度序列，以及它相对 CCDM 的 rate loss 优势与硬件可实现性。

## 科学定义

能量球约束定义可用的幅度序列集合：总能量不超过上限 $E_{\max}$ 的序列都可以入选——

$$\mathcal{S}(n, E_{\max}) = \left\{ \mathbf{a} \in \mathcal{A}^n : \sum_{i=1}^n a_i^2 \le E_{\max} \right\}$$

集合大小决定每块能编码的 bit 数。与固定组成的 CCDM 相比，能量球约束的序列集合大得多——同样长度，可区分序列更多 → rate loss 更小；且 DP 表可定点化、硬件可实现——rate loss 与可实现性的综合最优，这就是选 ESS 而不选 CCDM 的原因。

实现要点：

- **整数能量**：幅度 {1,3,5,7} 映射到整数能量 $(a^2-1)/8 \to \{0,1,3,6\}$——DP 表需要整数索引。
- **DP 计数表**：$\text{count}(n,e) = \sum_a \text{count}(n-1, e-e(a))$——避免枚举所有序列；表大小 ~129×256，实测约 264 KB（mantissa/exponent 定点存储）。
- **编码（rank → 序列）**：逐符号沿 DP 表选路径（比较 rank 与候选分支计数、扣减）——O(n) 每块；**解码（序列 → rank）**：逆路径累加——O(1) 查表，解码比编码轻。
- **分块与残差**：标准 CB 可能很长，按 nMax 分块（如 300 → 128+128+44），残差块按偶数化规则处理——ESS block ≠ 标准 CB。
- **错误传播**：ESS 无纠错；幅度错一位 → rank 累加分支改变 → 恢复 bit 可能大面积错——所以 inverse ESS 必须在 LDPC/CRC 之后。

## 直观模型

ESS 像"按编号查目录"：DP 计数表是目录索引，均匀 bit 组成一个大编号（rank），编码时逐位按编号翻到对应分支选出幅度符号，解码时沿原路累加把序列翻回编号。能量球约束像"购书预算"——只收录总价不超预算的组合；预算内的组合比固定页数（CCDM）多得多，编号空间更大，浪费的编号（rate loss）更小。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| ESS 的"球"和 MIMO 球面检测的"球"是一回事 | ESS 的球是发射端幅度序列的能量约束（$\sum a_i^2 \le E_{\max}$）；MIMO sphere detector 的球是接收端检测的搜索空间——两个完全不同的东西 |
| ESS 有纠错能力 | ESS 无纠错，幅度错一位会导致恢复 bit 大面积错——inverse ESS 必须放在 LDPC/CRC 之后 |
| ESS 块就是标准 CB | 标准 CB 很长时按 nMax 分块（如 300 → 128+128+44），残差块按偶数化规则处理——ESS block ≠ 标准 CB |
| ESS 是 3GPP 标准流程 | ESS 是非 3GPP 标准（6G 候选），协议只提供 TB/CB 粒度接口锚点 |

## 协议锚点

- TB/CB 粒度：TS 38.212 §5.2.2（接口锚）。
- **ESS 本身：非 3GPP 标准，无标准小节**。
- 仿真器实现：`+ProbShaping/+ess/`（ess.m、encode/decode.m、generateEnergyTable.m、dec2binFloat.m）。

## 图谱关联

- [[概念图谱入口]]
- [[Distribution_Matching_分布匹配]]
- [[MB_Distribution_MB分布]]
- [[Probabilistic_Shaping_概率整形]]
- [[T13.3_ess_enumerative_sphere_shaping]]
- 关系语义：ESS 是 DM 的能量球实现（rate loss 更小）；MB 分布定义目标概率（ESS 的输入），DP 表是它的数学引擎，定点存储是它的工程形态。
