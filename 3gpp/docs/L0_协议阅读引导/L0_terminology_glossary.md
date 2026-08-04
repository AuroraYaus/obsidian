---
type: definition
aliases:
  - 译码讲义术语总表
  - 3GPP 译码术语总表
tags:
  - 3gpp
  - docs
  - l0
  - glossary
source_spec: "docs/L0_协议阅读引导/L0_terminology_glossary.md"
---
# 译码讲义术语总表

本章集中收纳 `docs/` 作者讲义中反复出现的术语、缩写和简要解释。其他讲义正文默认直接使用这些简称；只有当某一节正在讲解概念本身时，才在正文中补充上下文说明。

## 系统与协议缩写

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| 3GPP | 第三代合作伙伴计划 | 3rd Generation Partnership Project；LTE/NR 协议规范来源。 |
| LTE | 长期演进 | Long Term Evolution；4G 蜂窝系统，本项目关注其 Turbo 数据译码链路。 |
| NR | 新空口 | New Radio；5G 空口系统，本项目关注其 LDPC 数据译码和 Polar 控制译码链路。 |
| MAC | 媒体接入控制层 | Medium Access Control；调度、HARQ process 和上层交付上下文来源。 |
| UL-SCH | 上行共享信道 | Uplink Shared Channel；上行数据传输信道。 |
| DL-SCH | 下行共享信道 | Downlink Shared Channel；下行数据传输信道。 |
| UCI | 上行控制信息 | Uplink Control Information；NR Polar 或 small block coding 的常见控制负载来源。 |
| DCI | 下行控制信息 | Downlink Control Information；PDCCH 盲检、CRC/RNTI 和 Polar 译码相关。 |
| PDSCH | 物理下行共享信道 | Physical Downlink Shared Channel；下行数据或 PCH 承载入口。 |
| DM-RS | 解调参考信号 | Demodulation Reference Signal；接收端估计数据符号附近信道的参考信号。 |
| CSI-RS | 信道状态信息参考信号 | Channel State Information Reference Signal；用于信道状态测量、报告和相关接收过程。 |
| RSRP | 参考信号接收功率 | Reference Signal Received Power；描述参考信号功率强弱。 |
| SINR | 信干噪比 | Signal to Interference plus Noise Ratio；描述信号相对干扰和噪声的强弱。 |

## 译码对象与算法

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| LLR | 对数似然比 | Log-Likelihood Ratio；译码器输入软信息，通常用符号表示倾向、幅度表示可靠度。 |
| CRC | 循环冗余校验 | Cyclic Redundancy Check；用于错误检测，不负责纠错。 |
| HARQ | 混合自动重传请求 | Hybrid Automatic Repeat Request；通过重传和软合并提升可靠性。 |
| TB | 传输块 | Transport Block；信道编码/译码链路最终交付的整体数据对象。 |
| CB | 码块 | Code Block；TB 分段后由译码核心逐块处理的工作单元。 |
| CBG | 码块组 | Code Block Group；NR LDPC 中可作为部分重传粒度的一组 CB。 |
| LDPC | 低密度奇偶校验码 | Low-Density Parity-Check Code；NR 数据业务的主要信道编码家族。 |
| Turbo | Turbo 码 | Turbo Code；LTE 数据业务的主要信道编码家族。 |
| Polar | 极化码 | Polar Code；NR 控制信息译码的主要编码家族。 |
| BCJR | BCJR 算法 | Bahl、Cocke、Jelinek、Raviv 提出的后验概率译码算法；名称来自作者姓氏。 |
| MAP | 最大后验概率 | Maximum A Posteriori；基于观测后后验概率选择最可能路径或比特。 |
| SCL | 连续消除列表译码 | Successive Cancellation List；Polar 译码中保留多条候选路径的算法。 |
| CA-SCL | CRC 辅助 SCL | CRC-aided SCL；用 CRC 在 Polar SCL 候选路径中辅助最终选择。 |

## 调制、信道与性能

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| AWGN | 加性白高斯噪声 | Additive White Gaussian Noise；入门链路仿真的常用噪声模型。 |
| BPSK | 二进制相移键控 | Binary Phase Shift Keying；每个符号承载一个比特的调制方式。 |
| QPSK | 正交相移键控 | Quadrature Phase Shift Keying；每个复符号承载两个比特的调制方式。 |
| QAM | 正交幅度调制 | Quadrature Amplitude Modulation；用幅度和相位承载多比特信息的调制家族。 |
| MCS | 调制与编码方案 | Modulation and Coding Scheme；调度侧选择调制阶数和目标码率的索引。 |
| TBS | 传输块大小 | Transport Block Size；调度侧得到的 TB 比特规模。 |
| BLER | 块错误率 | Block Error Rate；多帧统计中块译码失败比例。 |
| BER | 比特错误率 | Bit Error Rate；按比特统计的错误比例。 |
| FER | 帧错误率 | Frame Error Rate；按帧统计的错误比例。 |
| SNR | 信噪比 | Signal-to-Noise Ratio；信号功率与噪声功率的比值。 |
| RV | 冗余版本 | Redundancy Version；速率匹配循环缓存中的不同起点或区域选择。 |
| PRB | 物理资源块 | Physical Resource Block；物理层资源分配的基本频域块。 |
| RE | 资源元素 | Resource Element；一个 OFDM 符号和一个子载波位置上的资源单元。 |

## 工程实现与验证

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| RTL | 寄存器传输级 | Register Transfer Level；用寄存器、组合逻辑、状态机和接口描述硬件的层级。 |
| ASIC | 专用集成电路 | Application-Specific Integrated Circuit；RTL 综合、布局布线后面向芯片实现的形态。 |
| SRAM | 静态随机存取存储器 | Static Random-Access Memory；常用于 LLR、消息、soft buffer 和 trace 存储。 |
| DUT | 待测设计 | Device Under Test；被 testbench 驱动、观测和判定的 RTL 模块。 |
| DMA | 直接存储器访问 | Direct Memory Access；硬件按地址搬移输入 LLR、输出比特和 trace 的数据通路。 |
| SVA | SystemVerilog 断言 | SystemVerilog Assertion；用时钟化属性检查接口不变量。 |
| UVM | 通用验证方法学 | Universal Verification Methodology；SystemVerilog 验证框架。 |
| STA | 静态时序分析 | Static Timing Analysis；用时钟、延迟和约束计算路径是否满足时序。 |
| SDC | Synopsys 设计约束 | Synopsys Design Constraints；描述时钟、输入输出延迟、false path、multicycle path 等约束。 |
| PPA | 功耗、性能、面积 | Power, Performance, Area；硬件实现常用综合权衡指标。 |

## 基础概念

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| 向量 | vector | 一排或一列数字；本项目里常是一串 `0/1` 比特或 LLR。 |
| 矩阵 | matrix | 按行和列排成的数字表。 |
| 奇偶校验矩阵 | parity-check matrix | 用来检查比特串是否满足若干奇偶规则的矩阵。 |
| 校验子 | syndrome | 校验结果；全零表示校验规则通过，非零表示至少有规则没通过。 |
| 概率 | probability | 描述事件发生可能性的数值。 |
| 条件概率 | conditional probability | 在某个条件已经发生时另一个事件发生的概率。 |
| 先验概率 | prior probability | 看到观测证据之前的概率判断。 |
| 似然 | likelihood | 给定假设时看到当前观测的支持程度。 |
| 后验概率 | posterior probability | 看到观测证据之后更新得到的概率判断。 |
| 证据 | evidence | 支撑协议结论或工程结论的本地文件、表格、公式、日志或测试输出。 |
| 贝叶斯公式 | Bayes' rule | 把先验、似然和后验联系起来的概率公式。 |
| 硬判决 | hard decision | 只输出 `0` 或 `1`，不保留可靠度。 |
| 软判决 | soft decision | 不只输出倾向，还保留可靠度。 |
| 似然比 | likelihood ratio | 两个假设的似然或概率相除后得到的支持度比较。 |
| 裁剪 | clipping | 把太大的数限制在最大范围内。 |
| 饱和 | saturation | 计算结果超过表示范围时停在边界值。 |
| 熵 | entropy | 描述不确定性的量。 |
| 互信息 | mutual information | 描述观测和原始信息之间共享信息量的量。 |
| 信道容量 | channel capacity | 给定信道条件下理论可可靠传输的最高信息率。 |
| 码率 | code rate | 信息比特数与编码后比特数的比例。 |
| 编码增益 | coding gain | 使用纠错编码后达到同等误码表现所节省的信噪比。 |
| 高斯随机变量 | Gaussian random variable | 服从高斯分布的随机变量。 |
| 噪声方差 | noise variance | 噪声离散程度的平方量纲指标。 |
| 噪声标准差 | noise standard deviation | 噪声方差的平方根。 |
| 每比特能量与噪声谱密度比 | $E_b/N_0$ | 按每个信息比特能量归一化的信噪比指标。 |
| 每符号能量与噪声谱密度比 | $E_s/N_0$ | 按每个调制符号能量归一化的信噪比指标。 |
| 调制阶数 | $Q_m$ | 每个调制符号承载的比特数。 |
| 星座图 | constellation diagram | 调制符号在复平面上的点集。 |
| 同相分量 | in-phase component, I | 复数信号的 I 分量。 |
| 正交分量 | quadrature component, Q | 复数信号的 Q 分量。 |
| Gray 映射 | Gray mapping | 相邻星座点只差一个比特的映射方式。 |
| 软解调 | soft demapping | 把接收符号转换成逐比特软信息的过程。 |
| 逐比特 LLR | bit-wise LLR | 每个编码比特对应一个 LLR。 |
