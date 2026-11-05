---
type: definition
aliases:
  - Selective Scrambling
  - 选择性加扰
  - shaped mask
  - row routing
  - LLR sign flip
tags:
  - 3gpp
  - concepts
  - probability-shaping
source_spec: "非 3GPP 标准（6G 候选）; Qualcomm evaluation-link-simulator"
---

# Selective Scrambling 选择性加扰

选择性加扰是 PS 的 bit 保护环节：只对非整形 bit（sign/unshaped）做标准 Gold 加扰，对 shaped bits 不加扰——保住 ESS 建立的非均匀统计。一句话本质：**选择性加扰是"洗牌时别动已经排好的那一叠"——标准加扰整副牌洗乱会毁掉 ESS 排出的概率分布；只洗非整形那一叠，shaped 牌原样保留，RX 侧给对应位置贴"翻面标记"（LLR 乘 ±1）即可**。

## 独立解释任务

任务目标：解释为什么标准全比特加扰会破坏整形统计，以及"只加扰非 shaped 行"的保护机制与 RX 侧 LLR sign flip 的软域对称操作。

## 起源与演进

(1) **起点：标准加扰与整形的冲突。** 标准加扰是全比特 XOR——shaped bits 被 XOR 后统计立即均匀化，整形白做。

(2) **解法：shaped mask。** 用掩码标记"哪些行是 shaped 行"，只对非 shaped 行做 XOR——保住 ESS 建立的非均匀统计。

(3) **配套操作。** row routing 把 shaped 行移到指定位置（与 SBPM 配合）；TX 只 XOR 非 shaped 行（标准 Gold 序列只作用于部分 bit）。

(4) **RX 的软域对称。** LLR sign flip：只对对应行的 LLR 乘 ±1——与发射端 XOR 对称、无需硬判决。

(5) **边界。** 标准 Gold 加扰（TS 38.211 §7.3.1.1）照常执行，选择性加扰是叠加其上的扩展层——不替代、不改写标准步骤。

## 科学定义

标准加扰是全比特 XOR——shaped bits 被 XOR 后统计立即打散（均匀化），整形白做。选择性加扰的解法：用 shaped mask 标记"哪些行是 shaped 行"，只对非 shaped 行做 XOR：

- **shaped mask**：标识 shaped 行位置的掩码（如 rows 3:(2+2k) 为保护行）——TX/RX 共用，是选择性加扰的地图。
- **row routing（行路由）**：把 Qm 行矩阵中 shaped 行移到指定位置、非 shaped 行保持——与 SBPM 配合的 bit 组织操作。
- **TX 操作**：只对非 shaped 行 XOR Gold 序列（标准序列，但只作用于部分 bit）。
- **RX 操作（LLR sign flip）**：只对对应行的 LLR 乘 ±1（软值符号翻转）——与发射端的 XOR 对称，无需硬判决。
- **与标准加扰的关系**：标准 Gold 加扰（TS 38.211 §7.3.1.1）照常执行其职责；选择性加扰是叠加其上的扩展层——不替代、不改写标准步骤。

## 直观模型

选择性加扰像"洗牌时别动已经排好的那一叠"：标准加扰把整副牌洗乱，会毁掉 ESS 精心排出的概率分布；选择性加扰只洗非整形那一叠，shaped 牌原样保留，洗完再合回一付牌。RX 侧不需要把牌重新洗回来，只需给对应位置的牌贴"翻面标记"（LLR 乘 ±1），信息完全等价。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 选择性加扰替代标准加扰 | 标准 Gold 加扰（TS 38.211 §7.3.1.1）照常执行；选择性加扰是叠加其上的扩展层——不替代、不改写 |
| 加扰和整形互斥 | 加扰负责统计均匀化、整形负责非均匀化——选择性加扰按行分工，各司其职 |
| RX 解扰必须硬判决恢复 bit | RX 在软域做 LLR sign flip（乘 ±1）即可——与发射端 XOR 对称，无需硬判决 |

## 协议锚点

- 标准加扰：TS 38.211 §7.3.1.1（本地 `TS_38.211_38211-j30/content.md`）。
- **选择性加扰：非 3GPP 标准，无标准小节**。
- 仿真器实现：`+mapping/ps_scramble.m`（TX）、`ps_descramble.m`（RX，inverse_route_rows）。

## 关键要点

1. 全比特加扰会打散整形统计——选择性加扰只 XOR 非 shaped 行。
2. shaped mask 是"哪些行受保护"的地图——TX/RX 共用。
3. RX 做 LLR sign flip（乘 ±1）——软域对称、无需硬判决。
4. row routing 与 SBPM 配合完成 bit 组织。
5. 标准加扰照常执行——选择性加扰是叠加层不替代。
6. 加扰管均匀化、整形管非均匀化——按行分工各司其职。

## 图谱关联

- [[概念图谱入口]]
- [[Gold_序列加扰]]
- [[SBPM_整形比特位置映射]]
- [[Probabilistic_Shaping_概率整形]]
- [[T13.4_ps_embedding_four_access_points_bit_organization]]
- 关系语义：Gold 加扰是标准基底，选择性加扰是 PS 的扩展保护层；它与 SBPM 共享同一 bit 组织（哪行 shaped、哪行加扰），是"整形统计不被搅匀"的第二道防线。
