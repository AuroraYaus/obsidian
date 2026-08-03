---
type: definition
aliases:
  - Geometric Shaping
  - GS
  - 几何整形
tags:
  - 3gpp
  - concepts
  - probability-shaping
source_spec: "非 3GPP 标准（6G 候选）; PS01 §1.2"
---

# Geometric Shaping 几何整形

逼近高斯输入分布（Gaussian input distribution）的路线有两条——改使用概率（概率整形，Probabilistic Shaping，PS）或改星座坐标（几何整形，Geometric Shaping，GS）；GS 路线因标准兼容性差，在 3GPP 语境下是 PS 的对照路线而非替代方案。

## 独立解释任务

任务目标：解释 GS 与 PS 的本质区别（改坐标 vs 改概率）、GS 难进标准的原因（星座定义是标准流程的一部分）、以及 DVB-S2X 走 PS 路线的启示。

## 科学定义

- **GS（几何整形）**：改变星座点坐标位置——几何形状变化（如圆 QAM，circular QAM），使用概率保持均匀
- **PS（概率整形）**：保持坐标不变（TS 38.211 §5.1 固定），只改使用概率；可直接叠加在 NR QAM 链路上
- **标准兼容性**：GS 需 TX/RX 双方协商新星座表 + 修改解调参考——触及标准流程（TS 38.211 §5.1 星座定义）的大改动；PS 只贴标准接口工作（QAM label、加扰、MCS/TBS 均不变）
- **商用先例**：DVB-S2X 采用 CCDM（恒定成分分布匹配，Constant Composition Distribution Matcher）+ MB 分布（Maxwell-Boltzmann）——走的是 PS 路线而非 GS
- **实证状态**：3GPP Rel-19 全套语料无 PS/GS 内容——两者均为 6G 候选技术

## 直观模型

"改走法 vs 改路"：PS 是改变出行习惯——近路多走、远路少走，路网（星座坐标）不变；GS 是重新修路——改地图（星座形状）。修路要所有司机（TX/RX）都换新地图（协商新星座表 + 改解调参考），而改习惯只需约定各条路的走法频率（使用概率）。换地图的成本远高于改习惯，所以先落地的是 PS。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| GS 和 PS 是同类技术 | 一个改坐标、一个改概率——硬件与标准影响完全不同 |
| GS 一定比 PS 好 | 无标准支撑、协商成本高；PS 已获得大部分整形增益且兼容现有链路 |
| 星座是发射端自由决定的 | TS 38.211 §5.1 固定星座与 label——改动即标准变更 |

## 协议锚点

- **GS 本身：非 3GPP 标准，无标准小节**。
- 对照：TS 38.211 Rel-19 §5.1（固定星座定义）。
- 本地锚点：`3GPP_Rel19/processed/TS_38.211_38211-j30/content.md`。

## 图谱关联

- [[概念图谱入口]]
- [[Probabilistic_Shaping_概率整形]]
- [[MB_Distribution_MB分布]]
- [[Modulation_Constellations_调制星座]]
- 关系语义：GS 是 PS 的对照路线——同一目标（逼近高斯输入）的两种实现，PS 以标准兼容性胜出；DVB-S2X 提供了商用实证。
