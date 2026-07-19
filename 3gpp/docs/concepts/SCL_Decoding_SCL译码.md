---
type: definition
aliases:
  - SCL
  - Successive Cancellation List
  - 列表译码
  - Path Metric
tags:
  - 3gpp
  - concepts
  - polar
  - algorithm
  - scl
source_spec: "Algorithmic; TS 38.212 Polar decoder context"
---

# SCL 列表译码

SCL 保留 L 条候选路径并行搜索，每信息位分裂+修剪。

- **路径分裂**：每信息位分裂为 0/1 两条→2L 临时路径。
- **PM**：累积负对数似然，越小越好。
- **修剪**：排序→保留 PM 最小的 L 条。
- **L=8** 标准，L=1→SC（简单但差），L=16/32→更优但复杂度线性增长。

## 图谱关联

- [[Channel_Polarization_信道极化]]
- [[CA_SCL_CRC辅助SCL]]
- [[T10.5_Polar_SCL_decoding]]
- [[T10.6_CRC_aided_SCL_control_reliability]]
- 关系语义：SCL 是 Polar 译码核心算法。
