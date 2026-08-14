---
type: definition
aliases:
  - SIMD
  - Memory Layout
  - Cache-Friendly
  - SoA
tags:
  - 3gpp
  - concepts
  - implementation
  - simd
  - optimization
source_spec: "Engineering methodology; C/C++ implementation"
---

# SIMD 与内存布局

## 独立解释任务

任务目标：解释译码器 C/C++ 实现中单指令多数据（Single Instruction, Multiple Data, SIMD）与内存布局（Memory Layout）的基本概念——向量宽度、缓存行、AoS/SoA 与对齐如何决定定点译码模型的实际吞吐。

SIMD 与内存布局属于译码器工程实现层（C 模型、RTL 映射之前），作用于 LLR、外信息、LDPC 消息与 Polar 路径度量等对象的存储组织。

## 科学定义

SIMD 用一条指令对多个数据 lane 同时运算：SSE 128 bit、AVX2 256 bit、AVX-512 512 bit；16 bit lane 下分别可装 8/16/32 个 LLR。缓存行（cache line）是缓存与内存交换的最小块，常见 64 byte，一条 cache line 可装 32 个 int16 LLR。AoS（结构数组，Array of Structures）把同一位置的多个字段放一起（llr/extrinsic/hard_bit 相邻），调试直观；SoA（数组结构，Structure of Arrays）把同类字段拆成连续数组，hot loop 只搬运需要的字段，SIMD 与硬件预取友好。对齐：`alignas(64)` 使数组起点落在 cache line 边界，避免跨行读写与伪共享（false sharing）。这些均为实现选择，非 3GPP 规定。

## 直观模型

手算：64 byte cache line 除以 2 byte（int16）等于 32 个 LLR/行。若 LDPC layer 连续读取 `posterior[z]`，每条 cache line 服务 32 次访问；若改成 `posterior[z*64]`，相邻访问间隔 128 byte，跨过两条 cache line 却只用其中一小部分——stride 越大 cache 利用率越差。类比：仓库按"同类货物连续摆放"（SoA）时取货一趟能装满一车；按"AoS 混放"则每取一件都要多跑一趟。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| SIMD lane 多就一定快 | lane 数据无效（padding）、访问不连续、分支不一致时，向量宽度反而暴露内存瓶颈。 |
| AoS 总比 SoA 好 | 调试时 AoS 直观；译码 hot loop 只取单字段时 SoA 的 cache 利用率更高。 |
| SIMD 与内存布局是 3GPP 规定 | 协议固定逻辑比特顺序与译码结果，布局是接收机实现选择。 |
| int8 总优于 int16 | int8 吞吐翻倍但精度有损失，int16 是精度/吞吐平衡点，需按定点模型取舍。 |
| 对齐只是性能优化细节 | 不对齐会跨 cache line、引发 false sharing，甚至破坏 bit-exact 回放稳定性。 |

## 协议锚点

非 3GPP 标准：SIMD 指令集、cache line、AoS/SoA、对齐与预取均为工程实现方法论——TS 36.212/TS 38.212 只决定接收端要恢复的逻辑序列。实现中协议相关字段（`tb_id/cb_id/rv_idx/K/E/Ncb`、`base_graph/Zc/layer/cbg/rv/k0`、`A/K/E/N/info_set/frozen_set/rnti_context`）必须保留，并与实现布局字段（`alignment_bytes/simd_width_bits/lane_count/stride/padding`）分列，不得混写。讲义：`docs/L3_工程实现/T18.5_SIMD_memory_layout_decoders.md`。

## 图谱关联

- [[Fixed_Point_Numbers_定点数]]
- [[RTL_Microarchitecture_RTL微架构]]
- [[Golden_Model_黄金模型]]
- [[Bit_Exact_Regression_比特精确回归]]
- [[LLR_Quantization_LLR量化]]
- [[概念图谱入口]]
- [[T18.5_SIMD_memory_layout_decoders]]
- [[T21.5_storage_and_area_estimation]]
- 关系语义：SIMD 优化与内存布局决定定点模型的实际吞吐，是从 bit-exact 基线到高性能实现的桥梁。
