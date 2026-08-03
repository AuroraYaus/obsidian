---
type: definition
aliases:
  - DMRS
  - Demodulation Reference Signal
  - 解调参考信号
  - DMRS 端口
tags:
  - 3gpp
  - concepts
  - phy
  - reference-signal
source_spec: "TS 38.211 Rel-19 §7.4.1.1"
---

# DMRS 解调参考信号

DMRS（解调参考信号）是 PDSCH 链路上的"已知信号"：收发双方都知道的参考符号，接收端用它估计信道，才能解调数据。

## 独立解释任务

任务目标：解释 DMRS 为什么是解调的前提，以及它的配置如何权衡精度与开销。

## 科学定义

- **位置固定**：DMRS 在资源网格的特定位置（位置由 RRC/DCI 配置，收发一致），数据 RE 绕开它
- **type1/type2**：两种配置，决定每 PRB 参考 RE 数与端口数——type1 每符号 12 RE（两符号开销约 14%），type2 密度更高、端口更多
- **端口与层一一对应**：每层一个 DMRS 端口——4 层需要 4 端口，接收端按端口分别估计各层信道
- **预编码透明**：DMRS 也经过预编码，接收端估计的是层域信道 H·P——不需要知道 P
- **开销权衡**：DMRS 越多估计越准，数据 RE 越少——"参考信号 vs 数据容量"

## 直观模型

DMRS 像地图上的"已知地标"：地图（接收端）知道地标的确切位置和样子，收到信号后对比地标被"扭曲"了多少，就能推断整个地形（信道）怎么扭曲的。地标越多，地形推断越准，但地标占的地方不能放货（数据）。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| DMRS 越多越好 | 更多 DMRS = 更准估计但更少数据容量——必须权衡 |
| DMRS 只在仿真里有 | 实际系统全靠 DMRS 估计信道（完美估计只存在于仿真） |
| 接收端需要知道预编码矩阵 | DMRS 携带等效信道 H·P，预编码对接收端透明 |
| DMRS 端口数 = 天线数 | 端口与层对应，层数 ≤ 秩 ≤ 天线数 |

## 协议锚点

- DMRS：TS 38.211 Rel-19 §7.4.1.1。
- 本地锚点：`3GPP_Rel19/processed/TS_38.211_38211-j30/content.md`。
- 仿真器实现：`nrPDSCHDMRS`/`nrPDSCHDMRSIndices`（MATLAB 5G Toolbox）、`build_link_objects.m`。

## 图谱关联

- [[概念图谱入口]]
- [[Channel_Estimation_信道估计]]
- [[Layer_Mapping_层映射]]
- [[Precoding_预编码]]
- 关系语义：DMRS 是信道估计的输入（已知信号 → H），H 是所有接收处理（均衡/检测）的地基；端口与层一一对应衔接层映射。
