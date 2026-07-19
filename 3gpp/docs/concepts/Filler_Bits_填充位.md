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

当 TB+CRC 不能刚好平分时，插入填充位使所有码块大小相等。

## 关键机制

- **填充位值**：<NULL>，编码侧插入到码块数据之前。
- **译码器处理**：填充位位置 LLR=0（等概率），不计入判决。
- **K+ 和 K-**：大码块 C₊ 个，小码块 C₋ 个。

## 图谱关联

- [[TB_传输块]]
- [[CB_码块]]
- [[Segmentation_码块分段]]
- [[T3.2_transport_code_block_filler_bits]]
- 关系语义：填充位是协议分段流程的必要环节。
