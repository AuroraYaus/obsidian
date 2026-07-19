---
type: definition
aliases:
  - CA-SCL
  - CRC-Aided SCL
  - CRC辅助SCL
  - Path Selection
tags:
  - 3gpp
  - concepts
  - polar
  - algorithm
  - ca-scl
  - crc
source_spec: "Algorithmic; TS 38.212 Polar decoder context"
---

# CA-SCL CRC辅助SCL

CA-SCL 是 NR Polar 的实际译码方案：信息位前附加 CRC，SCL 后用 CRC 选最优路径。

- **编码**：K 信息位 + CRC11/6 → 极化编码。
- **译码后**：L 条候选→去 CRC 校验→选通过且 PM 最小的路径。
- **性能**：L=8 时 CA-SCL 接近 ML（<0.2dB）。
- **CRC11**：K≥20；**CRC6**：K<20。

## 图谱关联

- [[SCL_Decoding_SCL译码]]
- [[CRC_循环冗余校验]]
- [[Polar_码]]
- [[T10.6_CRC_aided_SCL_control_reliability]]
- 关系语义：CA-SCL 是 NR Polar 标准译码方案。
