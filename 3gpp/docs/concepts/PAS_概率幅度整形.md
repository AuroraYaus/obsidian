---
type: definition
aliases:
  - PAS
  - Probabilistic Amplitude Shaping
  - 概率幅度整形
  - amplitude/sign 分离
tags:
  - 3gpp
  - concepts
  - probability-shaping
source_spec: "非 3GPP 标准（6G 候选）; Qualcomm evaluation-link-simulator"
---

# PAS 概率幅度整形

PAS（Probabilistic Amplitude Shaping）是概率整形与 FEC 结合的**框架**：把符号拆成"幅度"（决定能量，可整形）和"符号"（决定正负，保持均匀），只对幅度做概率整形：$s = a \cdot \sigma$（a ∈ {1,3,5,…}，σ ∈ {±1}）。

## 独立解释任务

任务目标：解释整形怎么和 FEC 共存而不被"搅匀"，以及 amplitude/sign 分工的依据。

## 科学定义

- **分工表**：
  | 成分 | 概率特性 | 来源 |
  |---|---|---|
  | amplitude bits | 非均匀（整形目标） | DM/ESS 输出 |
  | parity bits | 近似均匀 | FEC 编码 → sign 位 |
  | unshaped bits | 均匀 | 原始数据 → 加扰保护 |
- **parity-as-sign**：FEC 的 parity 是信息位的线性组合，天然近似均匀——放 sign 位既不破坏均匀性，又完成纠错。整形与纠错互不干扰
- **systematic FEC**：系统码保留原始信息位（承载整形后的幅度信息），parity 独立输出——PAS 能工作的前提
- **为什么 sign 不能整形**：符号 ±1 必须保持各半（星座对称），否则破坏星座对称性、且与 parity 均匀性冲突

## 直观模型

PAS 像"分工打包"：货物（信息）分两路——一路走"慢速整形通道"（幅度，控制能量），一路走"快速均匀通道"（符号，放校验冗余）。两条通道各干各的互不干扰：整形的不会被搅匀（FEC 冗余放另一路），纠错也正常完成（parity 均匀分布）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PAS 和 ESS 是同一个东西 | PAS 是框架（amplitude/sign 分工），ESS 是 DM 的一种实现——ESS ⊂ DM ⊂ PAS |
| 符号位也可以整形 | sign 必须保持均匀（±1 各半），否则星座不对称、与 parity 冲突 |
| parity 放哪都行 | parity 近似均匀，放 sign 最合适；放 amplitude 会干扰整形统计 |
| 整形后不用管加扰 | 全比特加扰会打散整形统计——需要选择性加扰（见 Selective_Scrambling） |

## 协议锚点

- 接口锚：TS 38.211 Rel-19 §5.1（星座）、§7.3.1.1/2（加扰/调制映射）；TS 38.212 Rel-19 §5.3.2（FEC）。
- **PAS 本身：非 3GPP 标准，无标准小节**。
- 仿真器实现：`+tbgen/build_tb_for_ps.m`、`+mapping/sbpm_deinterleave.m`、`+mapping/ps_scramble.m`。

## 图谱关联

- [[概念图谱入口]]
- [[Probabilistic_Shaping_概率整形]]
- [[Distribution_Matching_分布匹配]]
- [[ESS_枚举球面整形]]
- [[SBPM_整形比特位置映射]]
- 关系语义：PAS 是整形体系的骨架（amplitude/sign 分工），ESS 是其幅度映射器，SBPM 是 bit 组装器——三者协作构成整形收发链路的组织方式。
