---
type: definition
aliases:
  - LLR Quantization
  - LLR量化
  - Clipping
  - Scaling
tags:
  - 3gpp
  - concepts
  - implementation
  - llr
  - quantization
source_spec: "Engineering methodology; decoder input signal conditioning"
---

# LLR 量化与裁剪

浮点 LLR 进入定点译码器前须经裁剪和量化。

- **均匀量化**：Δ 固定，LLR_q = round(clip(LLR, ±C)/Δ)·Δ。
- **非均匀量化**：小 |LLR| 细量化，大 |LLR| 粗量化。
- **裁剪阈值 C**：|LLR|>C→截断。C 太小丢可信度，太大浪费位宽。
- **位宽增 1bit→~0.1-0.2dB BLER 改善**。

## 图谱关联

- [[LLR_对数似然比]]
- [[Fixed_Point_Numbers_定点数]]
- [[T2.11_LLR_clipping_scaling_quantization]]
- [[T13.1_fixed_point_decoder_requirements]]
- 关系语义：LLR 量化是软解调到译码器的格式转换。
