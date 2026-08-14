---
type: definition
aliases:
  - RTL Microarchitecture
  - RTL 微架构
  - Hardware Decoder Architecture
tags:
  - 3gpp
  - concepts
  - engineering
  - rtl
  - hardware
source_spec: "Hardware implementation; derived from TS 36.212/38.212 decoder requirements"
---

# RTL 微架构

RTL（Register Transfer Level）微架构是译码器的硬件实现蓝图，用 Verilog/SystemVerilog 描述数据通路、控制状态机和存储结构。Turbo、LDPC、Polar 三类译码引擎各有独特的微架构挑战。

## 核心子概念

- **Turbo RTL**：SISO 数据通路（γ/α/β 递归单元）+ 交织/解交织网络 + CRC 门控迭代控制器。滑动窗口技术减少 α/β 存储。
- **LDPC RTL**：QC-LDPC 地址生成（Zc 循环移位）+ 分层调度存储 Bank + CN/VN 消息传递流水线。Min-Sum 只需比较器和加法器。
- **Polar RTL**：CA-SCL 树遍历引擎 + Path Metric 排序器（关键瓶颈）+ 路径拷贝与修剪。L=8 需要并行 8 条路径。
- **统一译码子系统**：三类引擎共享 DMA 输入/输出、软缓存（SRAM）、配置寄存器和中断控制器。
- **软缓存架构**：SRAM Bank 分块 + HARQ 事务提交/失败恢复 + N_soft 容量管理。
- **寄存器表**：协议参数（BG, Zc, K, E, RV, I_max）→ 硬件任务描述符 → 状态机配置。

## 图谱关联

- [[概念图谱入口]]
- [[Turbo_码]]
- [[LDPC_低密度奇偶校验码]]
- [[Polar_码]]
- [[Soft_Buffer_软缓存]]
- [[T19.1_LTE_Turbo_RTL_microarchitecture]]
- [[T19.2_NR_LDPC_RTL_microarchitecture]]
- [[T19.3_NR_Polar_RTL_microarchitecture]]
- [[T19.4_unified_decoder_subsystem_architecture]]
- [[T19.5_soft_buffer_HARQ_memory_architecture]]
- [[T19.6_decoder_register_map_configuration_flow]]
- [[T21.4_slot_cycle_budget_parallelization]]
- 关系语义：RTL 微架构是浮点算法到物理芯片的桥梁，每个译码器的硬件结构直接反映其算法特性。
