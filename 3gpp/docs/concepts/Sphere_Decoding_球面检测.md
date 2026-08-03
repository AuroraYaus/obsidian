---
type: definition
aliases:
  - Sphere Decoding
  - 球面检测
  - Sphere Detector
  - ML 检测
tags:
  - 3gpp
  - concepts
  - rx-chain
  - detection
source_spec: "接收机实现（非协议算法）; 通信检测理论"
---

# Sphere Decoding 球面检测

球面检测是 MIMO 接收的**最优检测**算法：搜索使 $\|\mathbf{y} - \mathbf{H}\mathbf{s}\|^2$ 最小的符号向量 s（最大似然，ML），用"半径剪枝"把搜索限制在球内，避免指数枚举。

## 独立解释任务

任务目标：解释 ML 检测为什么最优但昂贵，以及球面剪枝如何缓解指数爆炸。

## 科学定义

- **ML 目标**：$\hat{\mathbf{s}} = \arg\min_{\mathbf{s} \in \mathcal{S}^L} \|\mathbf{y} - \mathbf{H}\mathbf{s}\|^2$——找"最像"接收信号的符号组合；直接枚举 $O(2^{M\cdot L})$（4 层 256QAM = $2^{32}$）
- **球面约束**：只搜索 $\|\mathbf{y} - \mathbf{H}\mathbf{s}\|^2 \le r^2$ 的候选——球外组合剪掉
- **树搜索**：H 做 QR 分解 → 树形结构逐层枚举+剪枝：
  - Fincke-Pohst（FP）：固定半径深度优先
  - Schnorr-Euchner（SE）：按距离排序枚举（先近后远），剪枝更快
- **适用条件**：高 SNR 时球内候选少、搜索快；低 SNR 时球内候选爆炸（≈全枚举）——**只在高 SNR 实用**

## 直观模型

球面检测像"寻宝限范围"：宝藏（发送符号组合）可能藏在巨大的地图（所有候选）里，直接翻遍地图太慢（指数）。球面检测先划一个圈（半径 r），只在圈里找——圈小（高 SNR，候选都集中）就快；圈太大（低 SNR）和翻遍地图没区别。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 球面检测总是最优且快 | 性能最优，但复杂度随 SNR 恶化——低 SNR 时退化为全枚举 |
| 球面检测和信道估计有关 | 无关——它是检测算法，输入是 y 和 H（来自信道估计） |
| 球面检测是协议规定的 | 接收机实现自由选择，协议不管检测算法 |
| MMSE 和球面性能一样 | MMSE 线性近似次优，球面最优；工程常"MMSE 保底 + 球面增强" |

## 协议锚点

- 检测算法：接收机实现，非协议规定。
- 仿真器实现：`comm.SphereDecoder`（MATLAB，full=ML / radius 模式）、`+phy/+receiver/detect_pdsch_sphere.m`。

## 图谱关联

- [[概念图谱入口]]
- [[MMSE_均衡]]
- [[MIMO_多天线系统]]
- [[Soft_Demodulation_软解调]]
- [[T12.4_sphere_detection_detector_selection]]
- 关系语义：球面检测是 MMSE 的"最优替代"——同一输入（y、H），不同代价（复杂度 vs 性能）；检测器输出的软信息进入软解调/LLR。
