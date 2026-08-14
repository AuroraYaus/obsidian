---
type: definition
aliases:
  - Filler Bits
  - 填充位
  - <NULL>
  - K+
  - K-
tags:
  - 3gpp
  - concepts
  - protocol
  - filler
source_spec: "TS 36.212 §5.1.2; TS 38.212 §5.2"
---

# 填充位

## 独立解释任务

任务目标：解释 LTE/NR 码块分段（Code Block Segmentation）中填充位（Filler Bits）的插入位置、取值语义与接收端处理方式，说明协议为什么需要填充位、填充位为什么不能当作普通业务比特交付。

填充位位于发送端处理链中传输块（Transport Block, TB）附加 CRC 之后、信道编码之前，是 TB 分段成码块（Code Block, CB）环节的产物，对应接收端译码完成后、TB 重组之前必须剥离的对象。

## 科学定义

填充位是码块分段时为把每个码块长度补齐到合法编码输入长度集合而插入的占位比特。LTE 的核心分段公式（TS 36.212 §5.1.2）：

$$C = \left\lceil \frac{B}{Z-L} \right\rceil, \qquad B' = B + C\cdot L$$

- $B$：分段入口输入长度（已含 TB CRC）；$Z=6144$ 为最大码块长度；$L=24$ 为每个码块附加的 CRC 长度（仅 $C>1$ 时）。
- $C$：码块数；$B'$：分段后的总比特数。
- $K_+$：从 TS 36.212 Table 5.1.3-3 选出的上侧合法码块长度（满足 $C\cdot K_+\ge B'$ 的最小表值）；$K_-$：低一档合法长度；$C_+$、$C_-$：使用两种长度的码块数。
- 填充位总数 $F = C_+K_+ + C_-K_- - B'$，全部插入第一个码块的开头。
- 特例：$B<40$ 时即使 $C=1$ 也要在码块开头加填充位——因为 40 是 Table 5.1.3-3 的最小合法 $K$。
- 取值语义：编码器输入处填充位设为 `<NULL>`；CRC 计算时按 0 参与；接收端译码后剥离，不交付上层。

## 直观模型

设 $B=6145$（刚超过 $Z=6144$），$L=24$：$C=\lceil 6145/(6144-24)\rceil=2$，$B'=6145+48=6193$。查 Table 5.1.3-3：满足 $2K\ge 6193$ 的最小合法 $K_+=3136$，$K_-=3072$；$C_-=\lfloor(2\times 3136-6193)/(3136-3072)\rfloor=1$，$C_+=1$；$F=3136+3072-6193=15$。于是第一个码块开头插入 15 个 `<NULL>`，两个码块长度分别为 3136 与 3072。类比：把货物装入固定规格的集装箱，装不满的空位用泡沫垫占住，收货方开箱时把泡沫扔掉。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 填充位就是普通 0 比特 | 协议语义是 `<NULL>`；CRC 计算按 0 参与，但译码输出必须剥离、不得交付上层。 |
| 只有大 TB 分段才有填充位 | $B<40$ 的小块即使不分段也要加填充位，因为 40 是 Table 5.1.3-3 最小合法 $K$。 |
| 填充位计入信息比特 | $F$ 不计入 $B$、$B'$，也不改变 Turbo 编码长度 $D=K_r+4$ 的公式形式。 |
| 填充位随机分散在码块中 | 全部插入第一个码块的开头，位置由协议固定。 |
| 译码器对填充位位置做硬判决 | 接收端把填充位位置的 LLR 置 0（等概率），不参与判决。 |

## 协议锚点

- TS 36.212 §5.1.2 Code block segmentation and code block CRC attachment：$Z=6144$、$L=24$、$K_+/K_-$ 选择与 filler 位置。本地：`3GPP_Rel19/processed/TS_36.212_36212-j30/content.md` 行 609-645。
- TS 36.212 §5.1.3 与 Table 5.1.3-3：合法 $K$ 与 Turbo 内部交织参数 $f_1/f_2$。本地：`3GPP_Rel19/processed/TS_36.212_36212-j30/tables/table_0009.csv/html`。
- NR：TS 38.212 §5.2.1（Polar 分段）与 §5.2.2（LDPC 分段）的填充位环节，完整公式由 [[T3.4_NR_LDPC_segmentation_rules|T3.4]]、[[T3.5_NR_Polar_segmentation_crc|T3.5]] 承接。
- 讲义：`docs/L1_基础/T3.2_transport_code_block_filler_bits.md`；完整尺寸推导见 `docs/L1_基础/T3.3_LTE_Turbo_segmentation_rules.md`。

## 图谱关联

- [[TB_传输块]]
- [[CB_码块]]
- [[Segmentation_码块分段]]
- [[CRC_循环冗余校验]]
- [[Turbo_码]]
- [[Rate_Matching_速率匹配]]
- [[概念图谱入口]]
- [[T3.2_transport_code_block_filler_bits]]
- [[T3.3_LTE_Turbo_segmentation_rules]]
- 关系语义：填充位是协议分段流程的必要环节，衔接 TB 与码块编码输入，接收端在 TB 重组前必须剥离。
