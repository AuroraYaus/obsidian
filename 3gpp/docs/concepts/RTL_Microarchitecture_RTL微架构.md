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

## 符号与记号约定
| 符号 | 含义与取值 | 协议锚点 |
|:---|:---|:---|
| $K$ | 一个码块的比特长度，即编码器输入的信息位数，LTE Turbo 最大取 6144，单位为 bit | TS 36.212 §5.1.2 |
| $W_{\alpha}$ | 前向路径度量在硬件中的存储位宽，取正整数、单位为 bit，由定点位宽策略选定 | 实现域 |
| $W_{\beta}$ | 后向路径度量在硬件中的存储位宽，取正整数、单位为 bit，由定点位宽策略选定 | 实现域 |
| $M_{\alpha}$ | 全块前向路径度量的存储量，由状态数 8、码块长度 $K$ 与位宽 $W_{\alpha}$ 相乘得到，取正整数、单位为 bit | 由 TS 36.212 §5.1.3.2.1 导出 |
| $M_{\beta}$ | 全块后向路径度量的存储量，由状态数 8、码块长度 $K$ 与位宽 $W_{\beta}$ 相乘得到，取正整数、单位为 bit | 由 TS 36.212 §5.1.3.2.1 导出 |
| $W_{\mathrm{ext}}$ | 外信息的存储位宽，取正整数、单位为 bit，由定点位宽策略选定 | 实现域 |
| $M_{\mathrm{ext}}$ | 外信息的存储量，按 ping-pong 双缓冲计算，取正整数、单位为 bit | 实现域 |
| $L_{\mathrm{sys},k}$ | 第 k 个比特的系统位信道观测值，取实数、无量纲（对数似然比），由解调器给出 | 非 3GPP 标准 |
| $L_{\mathrm{a},k}$ | 第 k 个比特的先验信息，取实数、无量纲，即上一轮迭代中另一组成译码器给出、作为本译码器输入的可靠度 | 非 3GPP 标准 |
| $L_{\mathrm{ext},k}$ | 第 k 个比特的外信息，即本次迭代中由另一组成译码器带来、尚未被本译码器先验包含的新证据，取实数、无量纲 | 非 3GPP 标准 |
| $L_{\mathrm{post},k}$ | 第 k 个比特的后验对数似然比，等于系统位观测、先验与本次外信息三项之和，取实数、无量纲 | 非 3GPP 标准 |
| $f_{\mathrm{clk}}$ | 译码器的工作时钟频率，取正实数、单位为 Hz | 实现域 |
| $C_{\mathrm{block}}$ | 完成一个码块完整译码所需的时钟周期数，含全部迭代，取正整数、单位为周期 | 实现域 |
| $T_{\mathrm{bps}}$ | 译码吞吐率，取正实数、单位为 bit/s，等于码块长度与时钟频率之积除以块周期数 | 实现域 |

运算符与记号惯例：外信息容量按 $M_{\mathrm{ext}}=2KW_{\mathrm{ext}}$ 表达，式中并列书写的 $K$ 与 $W_{\mathrm{ext}}$ 表示相乘，系数 2 来自 ping-pong 双缓冲而不是幂次；外信息的扣除关系写作 $L_{\mathrm{ext},k}=L_{\mathrm{post},k}-L_{\mathrm{sys},k}-L_{\mathrm{a},k}$，三者在同一对数域内相减；公式末尾的 `\tag{}` 只用于交叉引用，编号本身不参与任何运算；下标 k 表示第 k 个比特、下标 clk 表示时钟、下标 bps 表示比特每秒，三者都不表示乘法。

RTL（Register Transfer Level）微架构是译码器的硬件实现蓝图，用 Verilog/SystemVerilog 描述数据通路、控制状态机和存储结构。Turbo、LDPC、Polar 三类译码引擎各有独特的微架构挑战。一句话本质：**RTL 微架构是"浮点算法到物理芯片的桥梁"——不是公式的逐行翻译，而是把算法变量与硬件对象一一对应：路径度量是存储化、外信息是交换通道、FSM 是时序化、trace 是证据化**。

## 解释目标与范围

本节目标：解释寄存器传输级（Register Transfer Level, RTL）微架构的层次化设计方法——数据通路、控制状态机（Finite State Machine, FSM）与存储结构如何把译码算法映射为可综合、可验证的硬件，并说明统一译码子系统中共享资源与引擎私有状态的边界。在 LTE/NR 译码链路中，RTL 微架构位于浮点/定点模型之后：它把协议 descriptor 与算法中间量落实到时钟、存储、地址生成与状态控制上，是浮点算法到物理芯片的桥梁。

## 前置概念

寄存器传输级（Register Transfer Level, RTL）。用「时钟沿之间数据从哪些寄存器经哪些组合逻辑搬到哪些寄存器」来描述硬件的一层抽象，对应的描述语言是可综合的 Verilog 或 SystemVerilog。它低于算法模型、高于门级网表：算法里一次赋值在这里变成一次跨时钟的存储与搬运，算法里一次循环在这里变成一段占用若干拍的时序。

有限状态机（Finite State Machine, FSM）。用有限个状态和状态之间的迁移条件描述控制流程的结构。译码器的取数、迭代、输出各阶段由 FSM 编排，迁移条件来自计数器、握手信号与错误标志；把控制流程写成显式状态机，是为了让每个状态的时序边界可被逐拍核对。

路径度量与软输入软输出译码。Turbo 译码沿网格递推前向与后向路径度量，再由两者与分支度量合成每个比特的对数似然比。路径度量是逐状态、逐拍存在的二维数组，它的位宽与存储布局决定硬件成本，也决定定点舍入误差能否被逐拍复现，见 [[Turbo_码]]。

存储层次与静态随机存取存储器（Static Random-Access Memory, SRAM）。译码器的面积与时序主要由存储决定：路径度量、外信息、输入软值与 trace 缓冲各自有独立的读写节拍与端口需求。把哪一份数据放在片上 SRAM、哪一份放在共享软缓存，决定了 bank 划分与端口冲突的规模，也决定了流水线能否满速，见 [[Soft_Buffer_软缓存]]。

比特精确回归（Bit-exact Regression）。以整数运算逐位一致为判据，比较 C/C++ 参考模型与 RTL 在同一激励下的中间结果与输出。定点化引入的舍入、饱和、归一化策略一旦不同，trace 会在第一个检查点分叉；因此归一化策略必须写进位精确约定，而不是留给实现者自由选择，见 [[Bit_Exact_Regression_比特精确回归]]、[[Fixed_Point_Numbers_定点数]]。

## 起源与演进

(1) **起点：从模型到芯片。** 浮点/定点模型验证完算法——物理芯片需要把算法变量映射为时钟、存储、地址生成与状态控制。

(2) **映射纪律。** alpha/beta 是路径度量的存储化、外信息是交换通道、FSM 是流程的时序化、trace 是工程后果的证据化。

(3) **四层结构。** 寄存器/控制层（common config）→ 数据搬运层（DMA/软缓存读改写）→ 引擎层（Turbo/LDPC/Polar 私有状态）→ 证据层（trace FIFO）。

(4) **存储与周期预算。** 全块 alpha/beta = $8K(W_{\alpha}+W_{\beta})$、外信息 ping-pong = $2KW_{\mathrm{ext}}$、吞吐 ≈ $K f_{\mathrm{clk}}/C_{\mathrm{block}}$——$K=6144$ 例：alpha/beta 约 144 KiB、6 次迭代最坏约 184 μs @ 400 MHz。

(5) **边界。** 共享资源只管理数据所有权、不存算法私有状态；归一化策略必须写进 bit-exact policy——否则 trace 第一轮就分叉；bank 数/窗口大小是实现设计、非协议强制。

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

## 关键要点

1. RTL ≠ 公式翻译——存储/带宽/时序/控制/证据的系统安排。
2. 四层结构：控制/搬运/引擎/证据——共享资源不存算法私有状态。
3. 存储公式：alpha/beta = 8K(Wα+Wβ)、外信息 2KW_ext。
4. 吞吐 ≈ K·f_clk/C_block——不达标就并行 trellis/窗口流水。
5. 归一化策略必须进 bit-exact policy——否则第一轮 trace 分叉。
6. bank 数/窗口/早停是实现设计，非 3GPP 强制。

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
