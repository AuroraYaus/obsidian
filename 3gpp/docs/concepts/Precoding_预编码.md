---
type: definition
aliases:
  - Precoding
  - 预编码
  - 预编码矩阵
  - 天线端口映射
tags:
  - 3gpp
  - concepts
  - tx-chain
  - mimo
source_spec: "TS 38.211 Rel-19 §7.3.1.4; TS 38.214 Rel-19 §5.1"
---

# Precoding 预编码

预编码是 MIMO 发射链路的步骤：把层（layer）上的 QAM 符号通过矩阵 P 映射到天线端口，每 RE 的操作为 $\mathbf{y} = \mathbf{P} \cdot \mathbf{x}$（x 是层符号 Nlayers×1，P 是 Nports×Nlayers，y 是端口符号）。

## 独立解释任务

任务目标：解释预编码与层映射的分工，以及为什么接收端不需要知道预编码矩阵。

## 科学定义

预编码是层域到天线域的线性映射：

$$\mathbf{y}_{\text{port}} = \mathbf{P} \cdot \mathbf{x}_{\text{layer}}$$

- **三种开环预编码器**：
  - DFT：$P_{mn} = e^{j2\pi mn/N_{tx}}$——列正交，均匀铺开波束
  - Hadamard：±1 矩阵（归一化 1/√N）——实现最简单
  - Identity：$[I; 0]$——层数 ≤ 天线数时的直接映射
- **功率归一化**：矩阵做 Frobenius 归一化（‖P‖_F = 1），保证总发射功率与层数无关
- **DMRS 透明性**：DMRS 也经过预编码，接收端估计的是层域信道 H·P——因此**不需要知道 P**（预编码对接收端透明）

## 直观模型

预编码像"分线器"：层是几条逻辑数据流（传送带），预编码矩阵决定每条传送带上的货物怎么分到各根天线（出口）。分线方式（矩阵）可以有很多种，但出口（天线）收到的总量由功率归一化保证不超标。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| 预编码 = 层映射 | 层映射做数据分发（符号→层），预编码做天线加权（层→端口），两步两个矩阵 |
| 接收端必须知道 P 才能解调 | DMRS 携带了等效信道 H·P，接收端直接估计它，P 对接收端透明 |
| 预编码矩阵随便选 | 矩阵选择影响波束/干扰特性，DFT/Hadamard 各有适用场景 |
| 层数等于天线数 | 层数 ≤ 秩 ≤ min(Ntx, Nrx)，天线多但秩低时层数上不去 |

## 协议锚点

- 预编码/端口：TS 38.211 Rel-19 §7.3.1.4。
- 层映射：TS 38.211 Rel-19 §7.3.1.3。
- 层数/码本：TS 38.214 Rel-19 §5.1。
- 本地锚点：`3GPP_Rel19/processed/TS_38.211_38211-j30/content.md`。
- 仿真器实现：`+phy/+mimo/build_dft_precoder.m`、`build_hadamard_precoder.m`、`build_identity_precoder.m`、`precode_resource_grid.m`。

## 图谱关联

- [[概念图谱入口]]
- [[MIMO_多天线系统]]
- [[Layer_Mapping_层映射]]
- [[TX3_layer_mapping_precoding|TX3 层映射与预编码讲义]]
- [[DMRS_解调参考信号]]
- 关系语义：预编码是 MIMO 基带模型 y=HPx+n 中的 P；层映射（数据分发）→ 预编码（天线加权）→ RE 映射是 MIMO 发射链的三连步。
