---
type: definition
aliases:
  - SBPM
  - Shaped Bit Position Mapping
  - 整形比特位置映射
  - 4^k 块置换
tags:
  - 3gpp
  - concepts
  - probability-shaping
source_spec: "非 3GPP 标准（6G 候选）; Qualcomm evaluation-link-simulator"
---

# SBPM 整形比特位置映射

SBPM（Shaped Bit Position Mapping）是把 shaped bits 放到 QAM label 幅度位上的置换：ESS 输出的整形 bit 必须落在真正控制星座幅度的 bit 位置，整形才有效。一句话本质：**SBPM 是"排座次的分拣员"——QAM label 是一列有固定职责的座位：sign 位是队长位（必须正负平衡、不允许整形）、幅度位是队员位（概率可调）；ESS 输出的 shaped bits 必须坐到队员位，TX 领位、RX 按同一张座位图还原**。

## 独立解释任务

任务目标：解释为什么 shaped bits 必须落在 QAM label 的幅度位上，以及 SBPM 的 4^k 块组织、TX/RX 对称操作和与标准交织的区别。

## 起源与演进

(1) **起点：shaped bits 必须坐对位置。** QAM label 每维 1 个 sign 位 + 若干 amplitude 位——只有幅度位控制概率；放错位置整形失效。

(2) **4^k 块组织。** 块大小 $4^k$ 对应 $2k$ 个 shaped bit/符号（16QAM 的 k=1、1024QAM 的 k=4）——1024QAM 的 4 个幅度位是最大舞台。

(3) **TX/RX 对称。** TX deinterleave（重排到幅度位）、RX interleave（逆过程）——两端座位图必须一模一样，否则 bit 顺序错乱。

(4) **与标准交织的区别。** 标准交织是 TS 38.212 §5.4.2.2 的 LDPC bit interleaving（标准步骤）；SBPM 是非标准扩展、叠加其后——对象、位置、目的完全不同。

(5) **与选择性加扰配合。** SBPM 决定"哪些行是 shaped 行"，选择性加扰据此只对非 shaped 行 XOR——同一 bit 组织的两面。

## 科学定义

QAM label 有结构——每维 1 个 sign bit（控制正负）+ 若干 amplitude bit（控制幅度）。如果 shaped bits 被放到 sign 位，它们就失去了"控制概率"的意义（sign 必须均匀）。SBPM 就是"把整形 bit 送到该去的位置"的置换器：

- **block = 4^k**：SBPM 按块组织——块大小 $4^k$ 对应 $2k$ 个 shaped bit/符号（k = 每维幅度 bit 数，16QAM 的 k=1、1024QAM 的 k=4）。
- **TX/RX 对称**：TX 做 deinterleave（把 shaped bits 从 ESS 输出重排到幅度位），RX 做 interleave（逆过程）——两端必须严格一致，否则 bit 顺序错乱。
- **与标准交织的区别**：TS 38.212 §5.4.2.2 的 LDPC bit interleaving 是标准步骤（LDPC 编码后的行/列交织）；SBPM 是非标准扩展（把 shaped bits 放幅度位）——两者对象、位置、目的完全不同，SBPM 叠加在标准交织之后。
- **与选择性加扰配合**：SBPM 决定"哪些行是 shaped 行"，选择性加扰据此只对非 shaped 行做 XOR——两者是同一 bit 组织的两面。

## 直观模型

QAM label 像一列有固定职责的座位：sign 位是"队长位"（必须正负平衡、不允许整形），幅度位是"队员位"（概率可以调整）。ESS 输出的 shaped bits 是必须坐到队员位上的队员，SBPM 是排座次的分拣员——TX 把队员领到正确座位（deinterleave），RX 按同一张座位图把队列还原（interleave）；两端的座位图必须一模一样，否则队形全乱。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| SBPM 就是标准交织 | 标准交织是 TS 38.212 §5.4.2.2 的 LDPC bit interleaving；SBPM 是非标准扩展，叠加在标准交织之后——对象、位置、目的完全不同 |
| shaped bits 放在哪个 bit 位置都一样 | 只有幅度位才控制概率——放到 sign 位整形就失效 |
| SBPM 只影响发送端 | TX/RX 严格对称：TX deinterleave、RX interleave，两端必须一致，否则 bit 顺序错乱 |

## 协议锚点

- 对照：TS 38.212 §5.4.2.2（标准 bit interleaving）、TS 38.211 §7.3.1.2（调制映射）。
- **SBPM 本身：非 3GPP 标准，无标准小节**。
- 仿真器实现：`+mapping/sbpm_interleave.m`、`sbpm_deinterleave.m`。

## 关键要点

1. shaped bits 必须落在幅度位——放到 sign 位整形失效。
2. block = 4^k：对应 2k 个 shaped bit/符号（1024QAM k=4）。
3. TX/RX 严格对称：deinterleave/interleave 两端一致。
4. SBPM ≠ 标准交织——叠加在标准交织之后的非标准扩展。
5. SBPM 与选择性加扰是同一 bit 组织的两面。
6. 1024QAM 的 4 个幅度位是 SBPM 的最大舞台。

## 图谱关联

- [[概念图谱入口]]
- [[Probabilistic_Shaping_概率整形]]
- [[ESS_枚举球面整形]]
- [[Selective_Scrambling_选择性加扰]]
- [[Interleaver_交织器]]
- [[QAM1024_1024QAM]]
- [[T13.4_ps_embedding_four_access_points_bit_organization]]
- 关系语义：SBPM 是"位置语义"的落实者——shaped bits 放对位置整形才有效（1024QAM 的 4 个幅度位是最大舞台）；它与标准交织、选择性加扰共同构成 PS 的 bit 组织层。
