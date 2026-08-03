---
type: definition
aliases:
  - Distribution Matcher
  - DM
  - 分布匹配器
  - rate loss
  - 速率损失
tags:
  - 3gpp
  - concepts
  - probability-shaping
source_spec: "非 3GPP 标准（6G 候选）; 信息论"
---

# Distribution Matching 分布匹配

分布匹配（DM）是概率整形的**映射引擎**：把均匀的 0/1 bit 流可逆地映射成符合目标分布（MB 分布）的幅度序列——"均匀 bit → 非均匀幅度"，且接收端能精确还原。

## 独立解释任务

任务目标：解释均匀输入怎么变成非均匀输出（且可逆），以及 rate loss 从哪来。

## 科学定义

- **输入输出**：均匀 bit（信息）→ 非均匀幅度序列 a1…an（符合 MB 分布）；inverse DM 精确逆
- **rate**：$R_{\text{DM}} = \text{输入 bit 数}/\text{输出符号数}$（bit/符号）
- **rate loss**：$H - R_{\text{DM}} \ge 0$——理想每符号可承载熵 H，实际映射器速率小于 H，差值即 rate loss（有限长度的必然代价）
- **可逆性**：每个 bit 串对应唯一幅度序列（一对一），接收端逆查表恢复——数据不丢的前提
- **两种实现流派**：CCDM（固定组成，集合=组合数，rate loss 偏大）；ESS（能量球约束，集合更大，rate loss 更小）
- **inverse DM 的位置**：在 LDPC/CRC 之后——DM 无纠错，幅度错一个符号可能导致恢复 bit 大面积错

## 直观模型

DM 像"洗牌机带标记"：一副等概率的牌（均匀 bit）洗成"红桃占 73%"的牌（非均匀幅度），每副洗法对应一个编号（bit 串）——接收端看到牌型能反查编号（可逆）。洗法越精细（长序列），编号利用率越高（rate loss 小），但洗牌机越复杂（表越大）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| DM 是一种信道编码 | DM 是可逆映射（无纠错），LDPC 才是纠错码 |
| rate loss 可以为零 | 有限长度下 rate loss > 0，只有无限长才趋近熵 |
| inverse DM 可以在 LDPC 之前 | DM 无纠错，CRC 通过前输出不可信（错误传播） |
| 查表法 DM 很实用 | 序列数指数爆炸，必须用 DP 表/ESS（T17.3） |

## 协议锚点

- TB/CB 粒度（DM 输出落点）：TS 38.212 Rel-19 §5.2.2（接口锚）。
- **DM 本身：非 3GPP 标准，无标准小节**。
- 仿真器实现：`+ess/encode.m`、`decode.m`（ESS 即 DM 的一种实现）。

## 图谱关联

- [[概念图谱入口]]
- [[Probabilistic_Shaping_概率整形]]
- [[MB_Distribution_MB分布]]
- [[ESS_枚举球面整形]]
- [[T13.3_ess_enumerative_sphere_shaping]]
- 关系语义：DM 是"均匀 → 非均匀"的通用概念；ESS 是它的具体实现（能量球约束）；rate loss 是整形收益的必然代价，公平对比必须 TBS matching。
