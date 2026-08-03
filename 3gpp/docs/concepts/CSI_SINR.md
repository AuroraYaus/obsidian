---
type: definition
aliases:
  - CSI
  - SINR
  - Channel State Information
  - 信道状态信息
  - 信号与干扰加噪声比
tags:
  - 3gpp
  - concepts
  - rx-chain
  - csi
source_spec: "TS 38.215 Rel-19（测量定义）; 接收机实现"
---

# CSI 与 SINR

CSI（信道状态信息）是接收端对信道质量的度量，SINR（信干噪比）是其中核心标量：$\text{SINR} = P_{\text{signal}}/(P_{\text{interference}} + P_{\text{noise}})$。

## 独立解释任务

任务目标：解释 CSI 为什么能"翻译"信道质量、以及它如何影响译码器输入 LLR。

## 科学定义

- **SNR vs SINR**：SNR 只含噪声；SINR 还含干扰（小区间、层间残留）——MIMO 场景必须用 SINR
- **post-eq SINR**：均衡/检测后的每符号等效 SINR；MMSE 后与 csi 相关（csi = 1 + SINR 在归一化中出现）
- **CSI 加权**：$\text{LLR}_{\text{out}} = \text{LLR}_{\text{in}} \times \text{CSI}$——信道好的符号 LLR 放大、差的收缩，再裁剪到 ±31
- **测量指标**（TS 38.215）：RSRP（接收功率）、RSRQ（功率/总功率）、SINR（信/干+噪）——三个指标的区别是"功率 vs 质量 vs 信干噪"
- **CSI 的用途**：除了解调加权，还用于 CQI 上报（链路自适应选 MCS）

## 直观模型

CSI 像"老师的批改笔"：信道质量好（SINR 高）的符号，老师把分数（LLR）放大（更可信）；信道差的符号，分数收缩（不可信）。加权后的分数才交给下一关（LDPC 译码）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| SNR 和 SINR 可以混用 | 无干扰场景近似相同；有干扰（小区间/层间）时必须用 SINR |
| CSI 加权是协议规定的 | 接收机实现，协议只定义测量指标（TS 38.215） |
| RSRP 高 = 信道好 | RSRP 只反映功率，不反映干扰——RSRQ/SINR 才是质量 |
| CSI 只用于解调 | CSI 还驱动 CQI 上报（MCS 选择），是链路自适应的依据 |

## 协议锚点

- 测量定义：TS 38.215 Rel-19。
- 本地锚点：`3GPP_Rel19/processed/TS_38.215_38215-j20/content.md`。
- CSI 加权：接收机实现（`+phy/+receiver/apply_csi_weighting.m`）。

## 图谱关联

- [[概念图谱入口]]
- [[MMSE_均衡]]
- [[Channel_Estimation_信道估计]]
- [[LLR_对数似然比]]
- 关系语义：信道估计 → post-eq SINR（CSI）→ LLR 加权 → 裁剪——CSI 是"信道质量 → 软信息可靠度"的翻译器。
