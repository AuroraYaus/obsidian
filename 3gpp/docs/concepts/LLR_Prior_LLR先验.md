---
type: definition
aliases:
  - LLR Prior
  - LLR 先验
  - 非均匀先验
  - amplitude bit 偏置
tags:
  - 3gpp
  - concepts
  - probability-shaping
source_spec: "非 3GPP 标准（6G 候选）; MAP 检测理论"
---

# LLR Prior LLR先验

LLR prior 是 PS 接收端的感知环节：软解调时把符号的非均匀先验概率加入距离度量——内圈点更"可信"。

## 独立解释任务

任务目标：解释为什么整形后"均匀先验"的软解调会系统性偏差，以及 prior 如何进入 LLR 度量、接收端如何低成本实现。

## 科学定义

标准 soft demapper 假设所有星座点等先验（uniform prior），其 LLR 只由距离决定；整形后这个假设不成立，必须修正为带先验的 MAP 度量：

$$\text{LLR}_b \propto \log \frac{\sum_{s \in \mathcal{S}_b^1} P(s) \cdot e^{-\|y-s\|^2/2\sigma^2}}{\sum_{s \in \mathcal{S}_b^0} P(s) \cdot e^{-\|y-s\|^2/2\sigma^2}}$$

其中 $P(s)$ 是非均匀先验（来自 MB 分布）。

- **为什么需要 LLR prior**：接收端若不感知整形（把 shaped 星座当 uniform 解），LLR 会系统性偏差——外圈点概率被高估，LDPC 输入不可靠，增益丢失甚至误码率变差。接收端感知整形是兑现整形增益的必要条件，不是可选项。
- **prior 偏置**：非均匀先验使"同一距离"的内圈候选更可信——LLR 被偏置向低能量符号。
- **amplitude bit 偏置**：整形只作用于幅度——幅度位的 LLR 受 prior 影响最大，sign 位近似不变。
- **LUT 实现**：prior 偏置项可预计算成查找表（PS 解调 LUT，1024QAM 时 1024×10 bit 量级）——避免在线算指数。
- **与 CSI 加权的关系**：LLR prior（符号概率）+ CSI 加权（信道质量）是两个独立乘子，叠加后统一裁剪（±31）。
- **3GPP 立场**：标准不规定唯一 demapper——接收端用什么解调算法是自己的事，prior 是接收端自由度。

## 直观模型

LLR prior 像"给候选名单加底分"：标准解调把同一距离的所有星座点一视同仁；整形后内圈点天生更可能被发送，prior 相当于给内圈候选加了一个"先验底分"（偏置向低能量符号）。不知道这个底分，LLR 就会高估外圈点，相当于裁判带着错误偏向打分——所以接收端必须知道发射端用了什么分布。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| prior 是协议规定的算法 | 标准不规定唯一 demapper——用什么解调算法是接收机自己的事，prior 是接收端自由度 |
| 发射端整形、接收端照旧解调也能拿到增益 | 不感知整形会导致 LLR 系统性偏差（外圈点被高估），增益丢失甚至误码率变差——感知是兑现增益的必要条件 |
| prior 对所有 bit 影响相同 | 整形只作用于幅度——幅度位 LLR 受影响最大，sign 位近似不变 |
| prior 与 CSI 加权二选一 | 两者是两个独立乘子（符号概率 × 信道质量），叠加后统一裁剪（±31） |

## 协议锚点

- 星座/软解调接口：TS 38.211 §5.1（接口锚）。
- **LLR prior：非 3GPP 标准，无标准小节**（标准不规定 demapper）。
- 仿真器实现：`+demod/get_ps_demodulation_lut.m`（prior LUT）、`preprocess_demod_input.m`（PS-MIMO 先验正则）。

## 图谱关联

- [[概念图谱入口]]
- [[LLR_对数似然比]]
- [[Probabilistic_Shaping_概率整形]]
- [[MB_Distribution_MB分布]]
- [[Soft_Demodulation_软解调]]
- 关系语义：MB 分布定义先验（TX 的目标概率 = RX 的先验），LLR prior 是接收端对它的感知；与 CSI 加权共同决定 LLR 可靠度，是 PS 增益兑现的最后一环。
