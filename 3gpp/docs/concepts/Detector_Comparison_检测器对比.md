---
type: definition
aliases:
  - Detector Comparison
  - 检测器对比
  - 均衡器对比
  - ZF/MMSE/Sphere
tags:
  - 3gpp
  - concepts
  - rx-chain
  - detection
source_spec: "接收机实现（非协议算法）; MIMO01 §5-6"
---

# Detector Comparison 检测器对比

在 MIMO 接收中，每个资源单元（RE，Resource Element）的接收信号可写成矩阵模型 $y = Hx + n$：$y$ 是接收符号向量，$H$ 是信道矩阵，$x$ 是发射符号向量，$n$ 是噪声。接收机用检测器（Detector）从 $y$ 中估计出符号 $\hat{x}$。匹配滤波（Matched Filter，MF）、迫零（Zero Forcing，ZF）、最小均方误差（Minimum Mean Square Error，MMSE）与球面检测（Sphere Decoding，Sphere）四族检测器，是精度与实现代价之间的不同折中；在接收机语境下"检测器"与"均衡器"常指同一概念（对应别名"均衡器对比"）。

## 独立解释任务

任务目标：解释四种检测器的公式、复杂度与性能损失，以及为什么 MMSE 是默认选择、Sphere 只在特定场景（高 SNR）使用。

## 科学定义

- **MF（匹配滤波）**：$\hat{s} = H^H y$——只匹配信道、完全忽略干扰；是 $\sigma^2 \to \infty$ 的极限（噪声主导时最合理）
- **ZF（迫零）**：$\hat{s} = (H^H H)^{-1} H^H y$——完全消除干扰、但放大噪声；是 $\sigma^2 \to 0$ 的极限（噪声可忽略时最合理）
- **MMSE（最小均方误差）**：$\hat{s} = H^H (H H^H + \sigma^2 I)^{-1} y$——用噪声功率做正则化的折中；相对 ZF 有 1-3 dB 增益；4×4 时约 100 MACs/tone、约 95K gates、约 20 cycles/tone
- **Sphere（球面检测）**：半径约束的 ML 搜索——在 $\|y - Hs\|^2 \le r^2$ 的球内找最优符号组合（QR 分解建树 + FP/SE 剪枝）；性能 0 dB 损失（等价于 ML 最优）；约 100-1000 MACs/tone、约 150K gates、50-500 cycles/tone；低 SNR 时球内格点数 $\propto (r^2/\sigma^2)^{N_{\text{layers}}}$ 爆炸 → 退化为穷举
- **性能排序**：MF ≤ ZF ≤ MMSE ≤ ML（Sphere）；**复杂度排序相反**——检测器的全部设计空间就是在这两个方向上取舍

## 直观模型

"四种听法"：嘈杂房间里有一句想听的话（目标信号），还有几个别人在说话（干扰）。MF 是只听最强声源——耳朵只对准目标，干扰照单全收；ZF 是试图把其他声源完全消掉——干扰消得干净，但杂音（噪声）也被一并放大；MMSE 是在"消除干扰"与"放大噪声"之间找平衡——噪声大时少消一点，噪声小时多消一点；Sphere 则是把每一种可能的说法组合都核对一遍——最准、最贵、也最慢。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| Sphere 一定比 MMSE 好 | 性能上 Sphere 0 dB 损失，但低 SNR 下复杂度爆炸、延迟随机，只适合高 SNR 场景 |
| MMSE 是协议规定的算法 | 检测器是接收机自由度——协议只定义传输假设，不规定接收端怎么检测 |
| ZF 消除干扰没有代价 | 消干扰必然放大噪声（$\sigma^2/\|h\|^2$ 量级），深衰落处最严重 |

## 协议锚点

- 接收机自由度：TS 38.214 只定义传输假设（传输方案、层数、预编码），不规定检测器。
- 仿真器实现：`new_pdsch_decode.m`（demapper 分支 mmse/sphere）、`nrEqualizeMMSE`、`comm.SphereDecoder`（MIMO01 §5-6、analysis 03 §3）。

## 图谱关联

- [[概念图谱入口]]
- [[MMSE_均衡]]
- [[Sphere_Decoding_球面检测]]
- [[CSI_SINR]]
- [[Diversity_Combining_分集与合并]]
- [[MIMO_多天线系统]]
- 关系语义：检测器把每 RE 的矩阵模型变成符号估计，输出（+ CSI 加权）喂给软解调；MMSE 是线性默认、Sphere 是 ML 参考。
