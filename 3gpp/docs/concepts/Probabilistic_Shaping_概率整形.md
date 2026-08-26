---
type: definition
aliases:
  - Probabilistic Shaping
  - PS
  - 概率整形
  - 整形增益
  - shaping gain
tags:
  - 3gpp
  - concepts
  - probability-shaping
source_spec: "非 3GPP 标准（6G 候选）; Qualcomm evaluation-link-simulator"
---

# Probabilistic Shaping 概率整形

概率整形（PS）是改变星座点**使用概率**的发射端技术：不改星座坐标，只让内圈（低能量）点多用、外圈（高能量）点少用，从而降低平均能量、获得整形增益（shaping gain）。

## 独立解释任务

任务目标：解释整形增益从哪来、代价是什么，以及它与标准链路的关系边界。

## 科学定义

- **整形增益（shaping gain）**：概率重分配省下的平均能量（dB）。理论上限 1.53 dB（二维，无限星座/无限长极限）；实测 AWGN 0.5-1.2 dB、TDL 衰落 0.2-0.6 dB
- **rate loss（速率损失）**：概率不均匀 → 每符号熵下降 → 信息率损失（$P(1)$=0.734 时熵 0.835 < 1 bit/符号）——**整形是用速率换能量**，最优 ν 需按目标码率折中
- **体系结构**：概率由 MB 分布定义；均匀 bit 到非均匀幅度的映射由 DM/ESS 完成；bit 位置由 SBPM 组织；统计由选择性加扰保护；接收端用 LLR prior 感知
- **四个接入点架构**：PS 只改 4 处——TB 构造（build_tb_for_ps）、加扰（ps_scramble）、解调前（preprocess_demod_input）、LDPC 解码后（deshape_tb）；NR spine（nrDLSCH/OFDM/检测器/nrDLSCHDecoder）全部复用——数据路径只认长度与统计约定，不认内容语义
- **PS 几何可行性条件**：numParityBits ≤ 2N_s(Qm/2−k)−L_cb 且 2Zc+2kN_s ≤ K−F−L_cb——整形区不能侵占 LDPC 打孔前缀（2Zc）与校验 bit 预算
- **非标准属性**：PS 全部环节是 6G 候选技术，不在 3GPP 标准中（Rel-19 全套 TS 语料无 shaping 内容）；只贴标准接口（QAM label、加扰、MCS/TBS）工作
- **公平对比前提**：增益报告必须做 TBS matching（同样 payload 比能量）+ 固定 MCS + 功率归一

## 直观模型

概率整形像"调整出行习惯"：平时出门远近路线各半（uniform），平均耗能高；改成"近路多走、远路少走"（shaped），平均耗能下降——但少看远路的风景（信息量下降，rate loss）。调整幅度（ν）要按"省多少油 vs 少看多少风景"折中。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PS 改变星座坐标 | 坐标由 TS 38.211 §5.1 固定，PS 只改使用概率 |
| ν 是 MCS 表/RRC 字段 | ν 是算法参数，标准表没有也不会有 |
| 整形增益 1.53 dB 是实际收益 | 是无限极限；实测 AWGN 0.5-1.2 dB、衰落更低 |
| 内圈点越多越好 | 概率越偏 rate loss 越大，有最优 ν |
| PS 是 3GPP Rel-19 特性 | Rel-19 全套 TS 无 shaping 内容，PS 是 6G 候选 |
| PS 要改标准编码链路 | 只改 4 个接入点，NR 编码/OFDM/检测器全复用——标准接口不动 |

## 协议锚点

- 接口锚：TS 38.211 Rel-19 §5.1（星座）、§7.3.1.1/2（加扰/调制映射）；TS 38.214 Rel-19 §5.1.3（MCS/TBS）。
- **PS 本身：非 3GPP 标准，无标准小节**。
- 仿真器实现：`+toolbox/+ProbShaping/`（ESS/SBPM/选择性加扰/功率缩放全套）。

## 图谱关联

- [[概念图谱入口]]
- [[Modulation_Constellations_调制星座]]
- [[LLR_对数似然比]]
- [[MB_Distribution_MB分布]]
- [[Distribution_Matching_分布匹配]]
- [[ESS_枚举球面整形]]
- [[SBPM_整形比特位置映射]]
- [[Selective_Scrambling_选择性加扰]]
- [[LLR_Prior_LLR先验]]
- [[T13.1_probabilistic_shaping_overview_shaping_gain]]
- [[T13.6_tbs_matching_system_cost_roi]]
- 关系语义：PS 是总纲，MB/DM/ESS/SBPM/选择性加扰/LLR prior 是它的组成部分；与 1024QAM 的幅度位结构天然契合。
