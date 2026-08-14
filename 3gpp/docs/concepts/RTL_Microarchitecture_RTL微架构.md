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

## 独立解释任务

任务目标：解释寄存器传输级（Register Transfer Level, RTL）微架构的层次化设计方法——数据通路、控制状态机（Finite State Machine, FSM）与存储结构如何把译码算法映射为可综合、可验证的硬件，并说明统一译码子系统中共享资源与引擎私有状态的边界。在 LTE/NR 译码链路中，RTL 微架构位于浮点/定点模型之后：它把协议 descriptor 与算法中间量落实到时钟、存储、地址生成与状态控制上，是浮点算法到物理芯片的桥梁。

## 科学定义

RTL 微架构不是公式的逐行翻译，而是把算法变量与硬件对象一一对应：alpha/beta 是路径度量的存储化，外信息是推导结果的交换通道，FSM 是接收端流程的时序化，trace 是工程后果的证据化。统一译码子系统采用四层结构：(1) 寄存器/控制层负责 common config 与 family extension；(2) 数据搬运层负责输入输出直接存储器访问（Direct Memory Access, DMA）与软缓存读改写；(3) 引擎层保留 Turbo/LDPC/Polar 私有状态；(4) 证据层负责 trace FIFO 与 failure bundle。Turbo SISO 数据通路中外信息必须扣除信道与先验：

$$
L_{\mathrm{ext},k}=L_{\mathrm{post},k}-L_{\mathrm{sys},k}-L_{\mathrm{a},k}
\tag{1}
$$

漏掉 $L_{\mathrm{a},k}$ 会把上一轮证据再听一遍，表现为饱和计数高、偶发 CRC 提前通过。存储估算方面，码块长度 $K$、状态数 8、度量位宽 $W_{\alpha},W_{\beta}$ 时全块 alpha/beta 存储为：

$$
M_{\alpha}+M_{\beta}=8K(W_{\alpha}+W_{\beta})
\tag{2}
$$

外信息采用 ping-pong 双 bank（一个 bank 读、一个 bank 写），系数 2 来自双缓冲：

$$
M_{\mathrm{ext}}=2KW_{\mathrm{ext}}
\tag{3}
$$

吞吐由时钟频率与块周期预算决定：

$$
T_{\mathrm{bps}}\approx \frac{K f_{\mathrm{clk}}}{C_{\mathrm{block}}}
\tag{4}
$$

其中 $C_{\mathrm{block}}$ 是一次完整译码的周期数。共享资源（DMA、软缓存、trace FIFO）只管理数据所有权与流控，不保存算法私有状态，否则破坏每个引擎的独立验证。

## 直观模型

以 $K=6144$ 的 LTE Turbo 码块做存储与周期预算。取 $W_{\alpha}=W_{\beta}=12$ bit、$W_{\mathrm{ext}}=8$ bit、输入 LLR 三路各 6 bit：(1) 全块 alpha/beta 存储 $8\times6144\times24=1{,}179{,}648$ bit，约 144 KiB；(2) 外信息 ping-pong $2\times6144\times8=98{,}304$ bit；(3) 三路输入 LLR $3\times6144\times6=110{,}592$ bit。周期上，单步 SISO 每拍处理一个 trellis step，一个半迭代约 6144 拍，一次完整迭代含 SISO A 与 SISO B 约 12,288 拍；最多 6 次迭代最坏约 73,728 拍，在 400 MHz 时钟下块时延约 $73{,}728/(400\times10^6)=184.32$ 微秒。若不满足吞吐目标，就要并行 trellis step、窗口流水或双 SISO 并行，代价是 SRAM 端口、bank conflict 与验证复杂度上升——这是微架构取舍，不是协议结论。滑动窗口可显著压缩 alpha/beta 存储，但必须把归一化策略（如每列减最大度量）写进 bit-exact policy，否则 C/C++ 与 RTL 在 trace 第一轮就分叉。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| RTL 就是把公式翻译成 Verilog | 微架构是对存储、带宽、时序、控制与调试证据的系统安排。 |
| bank 数、窗口大小、早停是 3GPP 强制要求 | 3GPP 规定编码结构与参数，硬件组织（SRAM bank、寄存器地址、IRQ 位）是实现设计。 |
| 共享资源可以保存算法私有状态 | 共享 DMA/软缓存只管理数据所有权；extrinsic RAM、path memory 等必须归引擎私有。 |
| 归一化策略不影响 bit-exact 对比 | 减最大值与减固定值会让 trace 在第一个 checkpoint 就分叉。 |
| 复位时必须全清大 SRAM | 大 SRAM 全清代价高，清 valid mask 与 descriptor valid 更关键。 |

## 协议锚点

- LTE Turbo 编码结构与 trellis 来源：TS 36.212 Rel-19 `36212-j30` §5.1.3.2.1、§5.1.3.2.2、§5.1.3.2.3/Table 5.1.3-3，本地 `3GPP_Rel19/processed/TS_36.212_36212-j30/content.md`、`tables/table_0009.csv/html`。
- LTE 速率匹配与 RV 边界：TS 36.212 Rel-19 `36212-j30` §5.1.4.1、§5.1.4.1.2，本地 `content.md` 对应章节。
- 统一子系统上下文证据：TS 36.213/36.321/36.331 与 TS 38.212/38.214/38.321/38.331 本地路径（TS 36.213 精确分册字段标注待核验）。
- 标注：RTL 微架构本身是实现设计，非 3GPP 强制——协议不规定 SRAM bank 数、寄存器地址、DMA burst 大小或中断位定义，只提供任务上下文。
- 本地讲义锚点：`docs/L3_工程实现/T19.1_LTE_Turbo_RTL_microarchitecture.md`、`docs/L3_工程实现/T19.4_unified_decoder_subsystem_architecture.md`。

## 图谱关联

- [[概念图谱入口]]
- [[Turbo_码]]
- [[LDPC_低密度奇偶校验码]]
- [[Polar_码]]
- [[Soft_Buffer_软缓存]]
- [[Fixed_Point_Numbers_定点数]]
- [[Bit_Exact_Regression_比特精确回归]]
- [[HARQ_Process_HARQ进程管理]]
- [[T19.1_LTE_Turbo_RTL_microarchitecture]]
- [[T19.2_NR_LDPC_RTL_microarchitecture]]
- [[T19.3_NR_Polar_RTL_microarchitecture]]
- [[T19.4_unified_decoder_subsystem_architecture]]
- [[T19.5_soft_buffer_HARQ_memory_architecture]]
- [[T19.6_decoder_register_map_configuration_flow]]
- [[T21.4_slot_cycle_budget_parallelization]]
- 关系语义：RTL 微架构是浮点算法到物理芯片的桥梁，每个译码器的硬件结构直接反映其算法特性。
