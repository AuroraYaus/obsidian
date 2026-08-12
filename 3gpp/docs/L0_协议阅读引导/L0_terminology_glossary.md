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

本章集中收纳 `docs/` 作者讲义中反复出现的术语、缩写和简要解释。其他讲义正文默认直接使用这些简称；只有当某一节正在讲解概念本身时，才在正文中补充上下文说明。条目合并自既有术语表与 `docs/concepts/3GPP全流程_缩写概念理论清单.md` 缩写清单；末尾「概念笔记索引」收录 `docs/concepts/` 全部概念笔记（104 篇），可经 wikilink 跳转阅读。

## 系统与协议

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| 3GPP | 第三代合作伙伴计划 | 3rd Generation Partnership Project；LTE/NR 协议规范来源。 |
| LTE | 长期演进 | Long Term Evolution；4G 蜂窝系统，本项目关注其 Turbo 数据译码链路。 |
| NR | 新空口 | New Radio；5G 空口系统，本项目关注其 LDPC 数据译码和 Polar 控制译码链路。 |
| 频谱 | 频谱 | Frequency Spectrum；电磁波按频率的连续范围，3GPP 划分 FR1/FR2 频段。→ [[Spectrum_and_Frequency_Point_频谱与频点]] |
| 频段 | 频段 | Frequency Band；3GPP 对频谱的划分块（NR n1-n104、LTE 1-105），如 n78 = 3300-3800 MHz。 |
| 频点 | 频点 | Frequency Point；频段内具体载波中心频率，用 ARFCN 整数编号表达。 |
| FR1 | 频率范围 1 | Frequency Range 1；450 MHz-6 GHz 中低频段。 |
| FR2 | 频率范围 2 | Frequency Range 2；24.25-52.6 GHz 毫米波频段。 |
| ARFCN | 绝对射频信道号 | Absolute Radio Frequency Channel Number；频点的整数编号：NR-ARFCN（TS 38.101-1 §5.4.2.1）/ E-UTRA ARFCN（TS 36.101 §5.7.3）。 |
| GSCN | 全球同步信道号 | Global Synchronization Channel Number；同步栅格上 SSB 参考位置编号（TS 38.101-1 §5.4.3.1）。 |
| 信道栅格 | 信道栅格 | Channel Raster；频点合法放置的离散位置集，步长 ΔF_Global（TS 38.104 §5.4.2）。 |
| 同步栅格 | 同步栅格 | Synchronization Raster；SSB 中心可放置的更稀疏位置集，用 GSCN 编号，UE 盲检搜索位置。 |
| MAC | 媒体接入控制层 | Medium Access Control；调度、HARQ process 和上层交付上下文来源。 |
| OSI | 开放式系统互联参考模型 | Open Systems Interconnection Reference Model；七层参考模型。3GPP 分层与之是功能类比而非同一体系。 |
| 协议栈 | 协议栈 | Protocol Stack；无线接口 L1/L2/L3 分层体系，层2 = MAC/RLC/PDCP（NR 加 SDAP）。→ [[Protocol_Stack_协议栈]] |
| PDCP | 分组数据汇聚协议 | Packet Data Convergence Protocol；层2 子层，负责加解密、头压缩与重排序。 |
| SDAP | 服务数据适配协议 | Service Data Adaptation Protocol；NR 层2 子层，QoS 流到无线承载映射。 |
| 数据链路层 | 数据链路层 | Data Link Layer；OSI 第二层，负责相邻节点成帧与差错控制；与 3GPP 层2 功能对应。 |
| PBCH | 物理广播信道 | Physical Broadcast Channel；承载 MIB，NR 用 Polar 编码、LTE 用 TBCC 编码。→ [[PBCH_MIB_广播信道]] |
| MIB | 主信息块 | Master Information Block；小区接入最少系统参数（SFN/公共子载波间隔/PDCCH-ConfigSIB1 等）。 |
| SIB | 系统信息块 | System Information Block；SIB1 由 MIB 指向，其余 SIB 由 SIB1 调度。 |
| TBCC | 咬尾卷积码 | Tail Biting Convolutional Code；LTE PDCCH/PBCH 信道编码，非递归无迭代。→ [[TBCC_咬尾卷积码]] |
| 调度器 | 调度器 | Scheduler；MAC 层每 slot 决策用户/资源/MCS 的单元。→ [[Scheduler_MAC调度器与资源分配]] |
| RBG | 资源块组 | Resource Block Group；频域分配最小粒度，位图分配单位。 |
| VRB | 虚拟资源块 | Virtual Resource Block；调度分配单位，经交织映射到 PRB。 |
| CQI | 信道质量指示 | Channel Quality Indicator；4-bit 索引映射 MCS/码率，BLER 目标约束。→ [[Link_Adaptation_链路自适应与CQI]] |
| PMI | 预编码矩阵指示 | Precoding Matrix Indicator；期望预编码矩阵的码本索引。 |
| RI | 秩指示 | Rank Indicator；建议的传输层数。 |
| NDI | 新数据指示 | New Data Indicator；同进程内翻转=新传、不翻转=重传。→ [[HARQ_Process_HARQ进程管理]] |
| SPS | 半静态调度 | Semi-Persistent Scheduling；周期资源免逐次 DCI 的调度机制。 |
| DFT-s-OFDM | 离散傅里叶变换扩展正交频分复用 | Discrete Fourier Transform Spread OFDM；NR 上行可选波形（低 PAPR）。→ [[DFT_sOFDM_上行波形]] |
| SC-FDMA | 单载波频分多址 | Single Carrier Frequency Division Multiple Access；LTE 上行波形，DFT-s-OFDM 前身。 |
| TPC | 发射功率控制命令 | Transmit Power Control Command；DCI 携带的闭环功控命令。→ [[Power_Control_上行功率控制]] |
| PHR | 功率余量报告 | Power Headroom Report；UE 上报功率余量，MAC 层。 |
| TA | 定时提前 | Timing Advance；UE 上行发射定时调整，RACH 建立。→ [[PRACH_随机接入]] |
| FDMA | 频分多址 | Frequency Division Multiple Access；按频率划分用户信道，1G AMPS 代表。→ [[Multiple_Access_多址接入]] |
| TDMA | 时分多址 | Time Division Multiple Access；按时隙划分用户，GSM = FDMA+TDMA。 |
| CDMA | 码分多址 | Code Division Multiple Access；按正交扩频码区分用户，3G WCDMA 代表。 |
| OFDMA | 正交频分多址 | Orthogonal Frequency Division Multiple Access；子载波分组（RB）分配用户，LTE/NR 多址方式。 |
| WCDMA | 宽带码分多址 | Wideband Code Division Multiple Access；3G 制式（TS 25 系列，本地无资料）。 |
| ASK | 幅度键控 | Amplitude Shift Keying；用载波幅度承载比特，OOK 是其特例。→ [[ASK_FSK_PSK_键控调制]] |
| FSK | 频移键控 | Frequency Shift Keying；用载波频率承载比特，GMSK（GSM）是其连续相位变体。 |
| PSK | 相移键控 | Phase Shift Keying；用载波相位承载比特，BPSK/QPSK 是其成员。 |
| DSSS | 直接序列扩频 | Direct Sequence Spread Spectrum；码片序列直接相乘的扩频方式。→ [[Spreading_扩频与解扩]] |
| 扩频 | 扩频 | Spread Spectrum；窄带信号扩展到宽频带传输的技术。 |
| 解扩 | 解扩 | De-spreading；接收端用同步码片序列把宽带信号恢复为窄带。 |
| UL-SCH | 上行共享信道 | Uplink Shared Channel；上行数据传输信道。 |
| DL-SCH | 下行共享信道 | Downlink Shared Channel；下行数据传输信道。 |
| UCI | 上行控制信息 | Uplink Control Information；NR Polar 或 small block coding 的常见控制负载来源。 |
| DCI | 下行控制信息 | Downlink Control Information；PDCCH 盲检、CRC/RNTI 和 Polar 译码相关。 |
| PDCCH | 物理下行控制信道 | Physical Downlink Control Channel；承载 DCI，是控制信息盲检与 Polar 译码的入口。 |
| PDSCH | 物理下行共享信道 | Physical Downlink Shared Channel；下行数据或 PCH 承载入口。 |
| PUSCH | 物理上行共享信道 | Physical Uplink Shared Channel；上行数据承载信道。 |
| PUCCH | 物理上行控制信道 | Physical Uplink Control Channel；承载 UCI 的上行控制信道。 |
| PRACH | 物理随机接入信道 | Physical Random Access Channel；承载随机接入前导的信道。 |
| RLC | 无线链路控制层 | Radio Link Control；无线链路控制层，有 TM/UM/AM 三模式。 |
| RNTI | 无线网络临时标识 | Radio Network Temporary Identifier；UE 在小区内用于寻址/加扰的临时身份。 |
| UE | 用户设备 | User Equipment；协议与链路仿真的收端主体。 |
| BWP | 带宽部分 | Bandwidth Part；UE 工作带宽的子集，是调度与 RF 配置的粒度。 |
| RRC | 无线资源控制 | Radio Resource Control；信令层，负责配置与连接管理。 |

## 译码对象与算法

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| LLR | 对数似然比 | Log-Likelihood Ratio；译码器输入软信息，通常用符号表示倾向、幅度表示可靠度。→ [[LLR_对数似然比]] |
| CRC | 循环冗余校验 | Cyclic Redundancy Check；用于错误检测，不负责纠错。→ [[CRC_循环冗余校验]] |
| HARQ | 混合自动重传请求 | Hybrid Automatic Repeat Request；通过重传和软合并提升可靠性。→ [[HARQ_混合自动重传请求]] |
| TB | 传输块 | Transport Block；信道编码/译码链路最终交付的整体数据对象。→ [[TB_传输块]] |
| CB | 码块 | Code Block；TB 分段后由译码核心逐块处理的工作单元。→ [[CB_码块]] |
| CBG | 码块组 | Code Block Group；NR LDPC 中可作为部分重传粒度的一组 CB。→ [[CBG_码块组]] |
| LDPC | 低密度奇偶校验码 | Low-Density Parity-Check Code；NR 数据业务的主要信道编码家族。→ [[LDPC_低密度奇偶校验码]] |
| Turbo | Turbo 码 | Turbo Code；LTE 数据业务的主要信道编码家族。→ [[Turbo_码]] |
| Polar | 极化码 | Polar Code；NR 控制信息译码的主要编码家族。→ [[Polar_码]] |
| BCJR | BCJR 算法 | Bahl、Cocke、Jelinek、Raviv 提出的后验概率译码算法；名称来自作者姓氏。→ [[BCJR_Algorithm_BCJR算法]] |
| MAP | 最大后验概率 | Maximum A Posteriori；基于观测后后验概率选择最可能路径或比特。 |
| SCL | 连续消除列表译码 | Successive Cancellation List；Polar 译码中保留多条候选路径的算法。→ [[SCL_Decoding_SCL译码]] |
| CA-SCL | CRC 辅助 SCL | CRC-aided SCL；用 CRC 在 Polar SCL 候选路径中辅助最终选择。→ [[CA_SCL_CRC辅助SCL]] |
| k0 | 速率匹配起点 | Rate matching starting position；由 RV 决定的循环缓存起始位置，是 rate recovery 的坐标语义。→ [[Rate_Matching_速率匹配]] |
| 迭代译码 | iterative decoding | 多个软输入软输出译码器反复交换外信息、逐步提升比特置信度的译码范式。→ [[Iterative_Decoding_迭代译码]] |

## 调制、信道与性能

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| AWGN | 加性白高斯噪声 | Additive White Gaussian Noise；入门链路仿真的常用噪声模型。→ [[AWGN_信道模型]] |
| BPSK | 二进制相移键控 | Binary Phase Shift Keying；每个符号承载一个比特的调制方式。 |
| QPSK | 正交相移键控 | Quadrature Phase Shift Keying；每个复符号承载两个比特的调制方式。 |
| QAM | 正交幅度调制 | Quadrature Amplitude Modulation；用幅度和相位承载多比特信息的调制家族。 |
| 1024QAM | 1024 阶正交幅度调制 | 32×32 星座、每符号 10 bit 的最后一档调制，对 SNR/EVM/PA 线性度要求苛刻。→ [[QAM1024_1024QAM]] |
| Qm | 调制阶数 | Modulation order；每个调制符号承载的比特数。 |
| PTRS | 相位跟踪参考信号 | Phase Tracking Reference Signal；补偿相位噪声 CPE，随数据同传。→ [[PTRS_相位跟踪参考信号]] |
| TRS | 跟踪参考信号 | Tracking Reference Signal；时频跟踪用，CSI-RS 的 trs-Info 子集。→ [[TRS_跟踪参考信号]] |
| CRS | 小区特定参考信号 | Cell-specific Reference Signal；LTE 专属广播式下行参考信号。→ [[CRS_小区特定参考信号]] |
| BFR | 波束失败恢复 | Beam Failure Recovery；波束失效检测与恢复过程。→ [[Beam_Management_波束管理]] |
| CA | 载波聚合 | Carrier Aggregation；多 CC 聚合提升带宽。→ [[Carrier_Aggregation_载波聚合]] |
| CC | 分量载波 | Component Carrier；CA 中被聚合的单个载波。 |
| PCell | 主小区 | Primary Cell；CA 中承载连接与移动性的主载波小区。 |
| SCell | 辅小区 | Secondary Cell；CA 中纯数据承载的辅载波小区。 |
| LCID | 逻辑信道标识 | Logical Channel Identity；MAC PDU 子头中标识逻辑信道的字段。→ [[MAC_Layer_Mapping_MAC层映射]] |
| AGC | 自动增益控制 | Automatic Gain Control；射频前端增益调节，防 ADC 饱和。→ [[RF_Frontend_射频前端]] |
| MCS | 调制与编码方案 | Modulation and Coding Scheme；调度侧选择调制阶数和目标码率的索引。→ [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]] |
| TBS | 传输块大小 | Transport Block Size；调度侧得到的 TB 比特规模。 |
| SNR | 信噪比 | Signal-to-Noise Ratio；信号功率与噪声功率的比值。 |
| SINR | 信干噪比 | Signal to Interference plus Noise Ratio；描述信号相对干扰和噪声的强弱。→ [[CSI_SINR]] |
| BLER | 块错误率 | Block Error Rate；多帧统计中块译码失败比例。 |
| BER | 比特错误率 | Bit Error Rate；按比特统计的错误比例。 |
| FER | 帧错误率 | Frame Error Rate；按帧统计的错误比例。 |
| RV | 冗余版本 | Redundancy Version；速率匹配循环缓存中的不同起点或区域选择。→ [[RV_冗余版本]] |
| PRB | 物理资源块 | Physical Resource Block；物理层资源分配的基本频域块。 |
| RE | 资源元素 | Resource Element；一个 OFDM 符号和一个子载波位置上的资源单元。 |
| TDL | 抽头延迟线信道模型 | Tapped Delay Line；3GPP 定义的多径衰落信道模型，TDL-A~E 剖面可选。→ [[TDL_信道模型]] |
| PSS | 主同步信号 | Primary Synchronization Signal；用于定时/小区搜索的同步信号。 |
| SSS | 辅同步信号 | Secondary Synchronization Signal；用于定时/小区搜索的同步信号。 |
| OFDM | 正交频分复用 | Orthogonal Frequency Division Multiplexing；多载波调制，子载波正交重叠。→ [[DFT_sOFDM_上行波形]] |
| CP | 循环前缀 | Cyclic Prefix；OFDM 符号前部冗余，消除 ISI/ICI。 |
| FFT | 快速傅里叶变换 | Fast Fourier Transform；OFDM 接收端时频变换。 |
| IFFT | 逆快速傅里叶变换 | Inverse Fast Fourier Transform；OFDM 发送端频时变换。 |
| SSB | 同步信号块 | Synchronization Signal Block；PSS+SSS+PBCH 一体。→ [[PSS_SSS_同步信号与小区搜索]] |
| SRS | 探测参考信号 | Sounding Reference Signal；上行信道探测。→ [[SRS_探测参考信号]] |
| CORESET | 控制资源集 | Control Resource Set；PDCCH 可占用的时频资源块。→ [[PDCCH_物理下行控制信道]] |
| CCE | 控制信道单元 | Control Channel Element；PDCCH 分配最小单位（6 REG）。 |
| REG | 资源元素组 | Resource Element Group；1 PRB × 1 符号。 |
| OCC | 正交覆盖码 | Orthogonal Cover Code；DMRS 端口复用的正交码。 |
| 相干带宽 | coherence bandwidth | 衰落信道在频率上"看起来一样"的尺度，决定信道估计/均衡的颗粒度。→ [[Coherence_Bandwidth_Time_相干带宽与时间]] |
| 定时同步 | timing synchronization | OFDM 接收第一关：FFT 窗口必须对准符号边界，实际靠 PSS/SSS 或 CP 相关实现。→ [[Timing_Sync_定时同步]] |
| 衰落 | fading | 多径导致的信号幅度/相位随机波动；瑞利衰落是 NLOS 的默认模型。→ [[Fading_Channel_衰落信道]] |

## MIMO 与接收链路

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| MIMO | 多输入多输出 | Multiple-Input Multiple-Output；收发多天线的传输形态，基带模型 y=HPx+n。→ [[MIMO_多天线系统]] |
| SIMO | 单入多出 | Single-Input Multiple-Output；单发多收，是分集接收的形态。 |
| SISO | 单入单出 | Single-Input Single-Output；单发单收的基准形态。 |
| CSI | 信道状态信息 | Channel State Information；接收端对信道质量的度量，SINR 是其中的核心标量。→ [[CSI_SINR]] |
| MMSE | 最小均方误差 | Minimum Mean Square Error；均衡器设计准则，W=Hᴴ(HHᴴ+σ²I)⁻¹。→ [[MMSE_均衡]] |
| ZF | 迫零均衡 | Zero Forcing；σ²→0 时 MMSE 的退化极限，消除干扰但放大噪声。→ [[MMSE_均衡]] |
| MF | 匹配滤波 | Matched Filter；σ²→∞ 时 MMSE 的退化极限。 |
| MRC | 最大比合并 | Maximum Ratio Combining；SIMO 最优线性合并，SNR 随分集分支数提升。→ [[Diversity_Combining_分集与合并]] |
| ML | 最大似然 | Maximum Likelihood（检测）；球面检测的搜索目标度量。→ [[Sphere_Decoding_球面检测]] |
| 球面检测 | sphere decoding | 用半径剪枝把搜索限制在球内的 ML 检测树搜索，避免指数枚举；FP/SE 是两种枚举策略。→ [[Sphere_Decoding_球面检测]] |
| 均衡 | equalization | 抵消信道影响、恢复发送符号的接收处理；MMSE/ZF/MF 是典型准则。→ [[MMSE_均衡]] |
| 信道估计 | channel estimation | 利用参考信号（DMRS）估计信道矩阵 H；LS 与维纳滤波是两种实现。→ [[Channel_Estimation_信道估计]] |
| Wiener | 维纳滤波 | Wiener Filter Estimation；MMSE 准则的信道估计，低 SNR 下显著优于 LS。→ [[Channel_Estimation_信道估计]] |
| 分集 | diversity | 多份独立衰落的拷贝合并，把深衰落概率指数压低；MRC 是最优线性合并方式。→ [[Diversity_Combining_分集与合并]] |
| H_eff | 等效信道矩阵 | Effective Channel Matrix；层映射与预编码后的等效信道，DMRS 估计直接给出，接收端无需知道预编码矩阵 P。 |
| Rhh | 信道相关矩阵 | HᴴH correlation matrix；PS 正则化的 Gram 矩阵，是 Cholesky 分解的输入。 |
| 导频 | pilot / 参考信号 | 收发双方都已知的参考符号（NR 中称参考信号 Reference Signal），接收端用它估计信道；DMRS/CSI-RS/PTRS/SRS 是其具体类型。→ [[Pilot_导频]] |
| DMRS | 解调参考信号 | Demodulation Reference Signal；接收端估计数据符号附近信道的参考信号（与数据同走预编码）。→ [[DMRS_解调参考信号]] |
| CSI-RS | 信道状态信息参考信号 | Channel State Information Reference Signal；用于信道状态测量、报告和相关接收过程。 |
| RSRP | 参考信号接收功率 | Reference Signal Received Power；描述参考信号功率强弱。 |

## 概率整形（PS）

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| PS | 概率整形 | Probabilistic Shaping；改星座点使用概率、不改坐标，降低平均能量获得整形增益。→ [[Probabilistic_Shaping_概率整形]] |
| PAS | 概率幅度整形 | Probabilistic Amplitude Shaping；amplitude/sign 分工：只整形幅度、符号保持均匀。→ [[PAS_概率幅度整形]] |
| DM | 分布匹配器 | Distribution Matcher；把均匀 bit 可逆映射为非均匀幅度的映射引擎。→ [[Distribution_Matching_分布匹配]] |
| ESS | 枚举球面整形 | Enumerative Sphere Shaping；DM 的一种实现：能量球约束 + DP 计数表。→ [[ESS_枚举球面整形]] |
| MB | 麦克斯韦-玻尔兹曼分布 | Maxwell-Boltzmann；P(a)∝e^(−νa²) 的目标概率分布，ν=0 退化为均匀。→ [[MB_Distribution_MB分布]] |
| SBPM | 整形比特位置映射 | Shaped Bit Position Mapping；把 shaped bits 放到 QAM label 幅度位上的置换（4^k 块组织）。→ [[SBPM_整形比特位置映射]] |
| GS | 几何整形 | Geometric Shaping；改星座点位置（非 PS），因标准兼容性差是 PS 的对照路线。→ [[Geometric_Shaping_几何整形]] |
| R_eff | 有效码率 | Effective Code Rate；=payloadTBS/(N_RE·Qm)，PS 公平比较口径，与目标码率 R 脱钩。→ [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]] |
| ν | 整形强度参数 | Shaping strength；MB 分布中控制概率/能量/熵的参数（ν=0 为均匀分布）。→ [[MB_Distribution_MB分布]] |
| rate loss | 速率损失 | 有限块长下整形引入的信息速率损失（熵损失、payload 与 chain TBS 之差）。 |
| 整形增益 | shaping gain | PS 相对均匀星座的 SNR 增益；1.53 dB 上限，AWGN 实测 0.5-1.2 dB。→ [[Probabilistic_Shaping_概率整形]] |
| LLR 先验 | LLR prior | PS 接收端在软解调中把符号的非均匀先验注入距离度量（内圈点更"可信"）。→ [[LLR_Prior_LLR先验]] |
| 选择性加扰 | selective scrambling | 只对非整形 bit 做标准 Gold 加扰、对 shaped bits 不加扰，保住 ESS 建立的整形统计；RX 侧以 LLR sign flip 对称还原。→ [[Selective_Scrambling_选择性加扰]] |

## 工程与硬件

| 术语 | 中文/常用名 | 说明 |
|:---|:---|:---|
| RTL | 寄存器传输级 | Register Transfer Level；用寄存器、组合逻辑、状态机和接口描述硬件的层级。→ [[RTL_Microarchitecture_RTL微架构]] |
| ASIC | 专用集成电路 | Application-Specific Integrated Circuit；RTL 综合、布局布线后面向芯片实现的形态。 |
| SRAM | 静态随机存取存储器 | Static Random-Access Memory；常用于 LLR、消息、soft buffer 和 trace 存储。 |
| DUT | 待测设计 | Device Under Test；被 testbench 驱动、观测和判定的 RTL 模块。 |
| DMA | 直接存储器访问 | Direct Memory Access；硬件按地址搬移输入 LLR、输出比特和 trace 的数据通路。 |
| SVA | SystemVerilog 断言 | SystemVerilog Assertion；用时钟化属性检查接口不变量。 |
| UVM | 通用验证方法学 | Universal Verification Methodology；SystemVerilog 验证框架。 |
| STA | 静态时序分析 | Static Timing Analysis；用时钟、延迟和约束计算路径是否满足时序。 |
| SDC | Synopsys 设计约束 | Synopsys Design Constraints；描述时钟、输入输出延迟、false path、multicycle path 等约束。 |
| PPA | 功耗、性能、面积 | Power, Performance, Area；硬件实现常用综合权衡指标。 |
| 位宽 | bit width | 定点实现中每级信号的数据位宽；全链路 TX 14 级/RX 18 级逐级追踪。→ [[Fixed_Point_Numbers_定点数]] |
| Qm.n | 定点 Q 格式 | 定点数表示法：m 位整数 + n 位小数（另含符号位），决定动态范围与精度。→ [[Fixed_Point_Numbers_定点数]] |
| ADC | 模数转换器 | Analog-to-Digital Converter；接收链路前端把模拟信号数字化。 |
| DAC | 数模转换器 | Digital-to-Analog Converter；发射链路把数字信号转模拟。 |
| PAPR | 峰均功率比 | Peak-to-Average Power Ratio；信号峰值与平均功率之比，影响 PA 回退。 |
| EVM | 误差矢量幅度 | Error Vector Magnitude；发射信号相对理想星座点的误差度量。 |
| PA | 功率放大器 | Power Amplifier；发射链路末端放大，PAPR 与线性度决定其回退量。 |
| Cholesky | 乔列斯基分解 | Cholesky Decomposition；正定矩阵的三角分解，用于 PS 正则化 Rhh 的预处理。 |
| QR | QR 分解 | QR Decomposition；球面检测树搜索的信道预处理手段。 |
| LUT | 查找表 | Look-Up Table；查表实现函数（如 PS 解调、ESS 能量表）。 |
| CORDIC | 坐标旋转数字计算 | Coordinate Rotation Digital Computer；用移位+加法迭代计算三角函数/幅相。 |
| LFSR | 线性反馈移位寄存器 | Linear Feedback Shift Register；Gold 序列等伪随机序列的生成硬件。→ [[Gold_序列加扰]] |
| Gold 序列 | Gold 序列 | Gold Sequence；两个 m 序列逐位异或的加扰序列，周期 2³¹−1，初态由 c_init 决定。→ [[Gold_序列加扰]] |
| FP | Fincke-Pohst 策略 | Fincke-Pohst；球面枚举策略，按星座顺序区间搜索。→ [[Sphere_Decoding_球面检测]] |
| SE | Schnorr-Euchner 策略 | Schnorr-Euchner；球面枚举策略，按部分距离排序搜索。→ [[Sphere_Decoding_球面检测]] |
| MACs | 乘累加操作 | Multiply-Accumulate；硬件复杂度（面积/周期）的常用度量。 |
| ROM | 只读存储器 | Read-Only Memory；存常量表（如星座、CRC 表）。 |
| O(n) | 复杂度记号 | Big-O notation；算法复杂度随规模 n 的增长阶。 |
| Nrx/Ntx | 收/发天线数 | Receiver/Transmitter antenna count；决定信道矩阵维度与处理复杂度。 |
| Nfft | FFT 点数 | FFT size；OFDM 处理的变换规模。 |
| Nlayers | 层数 | Number of layers；空间复用维度，决定每符号承载的数据流数。 |
| Nre | 资源元素数 | Number of resource elements；吞吐/复杂度计算的 RE 规模。 |
| DFT | 离散傅里叶变换 | Discrete Fourier Transform；预编码矩阵之一（也用于 OFDM 调制）。 |
| Hadamard | 阿达玛矩阵 | Hadamard Matrix；±1 正交的预编码矩阵之一。 |
| 周期预算 | cycle budget | 时隙内各处理阶段可用的时钟周期数（如 61,440 @122.88 MHz）。 |

## 基础概念（数学与信息论）

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
| 星座图 | constellation diagram | 调制符号在复平面上的点集。 |
| 同相分量 | in-phase component, I | 复数信号的 I 分量。 |
| 正交分量 | quadrature component, Q | 复数信号的 Q 分量。 |
| Gray 映射 | Gray mapping | 相邻星座点只差一个比特的映射方式。 |
| 软解调 | soft demapping | 把接收符号转换成逐比特软信息的过程。→ [[Soft_Demodulation_软解调]] |
| 逐比特 LLR | bit-wise LLR | 每个编码比特对应一个 LLR。 |

## 概念笔记索引

> `docs/concepts/` 全部概念笔记（104 篇），按主题分组；每条一句话取自笔记首段。

### 协议、信道与信号

| 笔记 | 一句话 |
|:---|:---|
| [[Physical_Channels_物理信道]] | 空口上不同内容的通道分工：数据（PDSCH/PUSCH）、控制（PDCCH/PUCCH）、接入（PRACH）各走各的通道，接收端按通道类型用不同流程解调。 |
| [[Layer_Mapping_层映射]] | 把一个码字的 QAM 符号分发到一个或多个空间层的步骤；层数就是空间复用的维度，层不是天线。 |
| [[Precoding_预编码]] | 把层上的 QAM 符号通过矩阵 P 映射到天线端口的发射链路步骤，接收端不需要知道预编码矩阵。 |
| [[DMRS_解调参考信号]] | 收发双方都已知的参考符号，接收端用它估计信道，才能解调数据。 |
| [[Pilot_导频]] | 收发双方都已知的参考符号（NR 中称参考信号）；从序列生成、资源映射到接收端提取、估计、插值、使用的完整链路。 |

| [[Gold_序列加扰]] | 用两个 m 序列逐位异或生成的伪随机序列对编码 bit 流做 XOR，把数据"白化"。 |
| [[HARQ_混合自动重传请求]] | 把前向纠错和自动重传结合，CRC 失败后保留同一 process 的软信息，按 RV 和调度上下文补充接收证据。 |
| [[RV_冗余版本]] | 描述一次传输选取哪一部分编码冗余，是 HARQ soft combining 的"地址语义"。 |
| [[CBG_码块组]] | 把多个 CB 组合成部分重传粒度，把 HARQ 从整 TB 重传细化到一组 CB。 |
| [[CB_码块]] | TB 分段后交给译码核心逐块处理的工作单元，是译码核心的最小主要工作单元。 |
| [[TB_传输块]] | 物理层信道编码链路最终要交付或拒绝的整体数据对象，也是 HARQ 成败判断的主对象。 |
| [[Segmentation_码块分段]] | 把一个 TB 拆成若干 CB，使每个译码核心处理的块长满足协议和编码器约束。 |
| [[Filler_Bits_填充位]] | 当 TB+CRC 不能刚好平分时插入的 <NULL> 位，使所有码块大小相等。 |
| [[Rate_Matching_速率匹配]] | 把编码后比特适配到本次可发送资源；接收端 rate recovery 把 LLR 放回 circular buffer 坐标。 |
| [[Circular_Buffer_循环缓存]] | 速率匹配的核心数据结构：编码比特按系统位→校验位写入环形缓存，RV 定义起始位置 k₀。 |
| [[Soft_Buffer_软缓存]] | 保存译码前的软信息（LLR 坐标化证据）而非硬判决 bit，供 HARQ 重传之间累积。 |
| [[Incremental_Redundancy_增量冗余]] | 每次重传用不同 RV 发送不同校验位，等效于降低码率，同时获得能量与编码增益。 |
| [[Chase_Combining_Chase合并]] | 最简单的 HARQ 软合并：重传使用相同 RV，接收端 LLR 直接逐比特相加。 |
| [[Early_Stopping_早停控制]] | 用 syndrome、CRC 或路径条件提前结束无意义译码迭代，在性能、时延、功耗间折中。 |
| [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]] | MCS 表把调度索引映射为调制阶数与目标码率（PS 表还含 ν），R_eff 是实际 payload 折算的真实码率。 |
| [[CSI_SINR]] | CSI 是接收端对信道质量的度量，SINR 是其中核心标量，影响译码器输入 LLR。 |
| [[QAM1024_1024QAM]] | 32×32 星座、每符号 10 bit 的"最后一档"调制，给接收与 RF 带来 SNR/EVM/PA 线性度挑战。 |
| [[Protocol_Stack_协议栈]] | 3GPP L1/L2/L3 分层与 OSI 七层模型对照。 |
| [[Spectrum_and_Frequency_Point_频谱与频点]] | 频谱→频段→频点→ARFCN→栅格定位链。 |
| [[Multiple_Access_多址接入]] | FDMA/TDMA/CDMA/OFDMA 四种多址方式详细对比。 |
| [[ASK_FSK_PSK_键控调制]] | ASK/FSK/PSK 键控调制家族与到 QAM 的演进。 |
| [[Spreading_扩频与解扩]] | DSSS 扩频-解扩机制、处理增益与 CDMA 关系。 |
| [[TBCC_咬尾卷积码]] | LTE 控制信道编码（PDCCH/PBCH），咬尾网格零码率损失。 |
| [[PSS_SSS_同步信号与小区搜索]] | 小区搜索流程：同步栅格→PSS/SSS→小区 ID→SSB。 |
| [[PBCH_MIB_广播信道]] | MIB 字段与 PBCH 编码（NR Polar / LTE TBCC）。 |
| [[PDCCH_物理下行控制信道]] | CORESET/CCE/聚合等级/搜索空间与盲检机制。 |
| [[DCI_下行控制信息]] | DCI 格式体系与字段语义，调度指令本体。 |
| [[PUCCH_上行控制信道与UCI]] | UCI 三兄弟与 PUCCH format 0-4。 |
| [[Scheduler_MAC调度器与资源分配]] | MAC 调度器决策与 RBG/VRB/Type 0-1 资源分配。 |
| [[Scheduling_Grant_调度与授权]] | 动态授权与 SPS/configured grant 机制。 |
| [[HARQ_Process_HARQ进程管理]] | HARQ 进程状态机、NDI 翻转与 k0/k1/k2 时序。 |
| [[Link_Adaptation_链路自适应与CQI]] | CQI/PMI/RI 反馈闭环与 outer loop 校准。 |
| [[DFT_sOFDM_上行波形]] | NR 上行 DFT-s-OFDM 波形原理与低 PAPR 优势。 |
| [[Power_Control_上行功率控制]] | 开环/闭环功控、TPC 与 PHR。 |
| [[PRACH_随机接入]] | 前导、四步/两步随机接入过程。 |
| [[SRS_探测参考信号]] | 上行探测、comb 结构与 TDD 互易性。 |
| [[UL_DL_Differences_上下行差异]] | 上下行七维度全景对照。 |
| [[Modulation_Mapping_调制映射]] | TS 38.211 §5.1 星座表与归一化因子。 |
| [[RE_Mapping_资源元素映射]] | 符号到网格的填充规则与参考信号避让。 |
| [[TX_Chain_发送端处理链总览]] | 发送端 11 环处理链全景（阶段 1 收官）。 |
| [[CSI_RS_信道状态信息参考信号]] | 下行测量参考信号（CSI 测量/波束/跟踪三用途）。 |
| [[PTRS_相位跟踪参考信号]] | 相位噪声 CPE 补偿，随数据同传。 |
| [[TRS_跟踪参考信号]] | CSI-RS 的 trs-Info 子集，时频跟踪。 |
| [[CRS_小区特定参考信号]] | LTE 专属广播式参考信号（解调/测量/同步）。 |
| [[Beam_Management_波束管理]] | 波束测量/报告/指示/BFR 四步闭环。 |
| [[MAC_Layer_Mapping_MAC层映射]] | 逻辑→传输→物理三层信道映射与 MAC PDU 复用。 |
| [[Carrier_Aggregation_载波聚合]] | 多 CC 聚合、PCell/SCell 分工与跨载波调度。 |
| [[BWP_带宽部分]] | 载波内激活工作子带（适配/省电/切换）。 |
| [[RF_Frontend_射频前端]] | LNA/AGC/ADC/IQ/相位噪声，非协议强制。 |

### 译码算法

| 笔记 | 一句话 |
|:---|:---|
| [[LDPC_低密度奇偶校验码]] | NR 数据业务的主要编码家族，用稀疏校验矩阵在 Tanner 图上迭代更新 LLR。 |
| [[QC_LDPC_准循环LDPC]] | NR LDPC 的实现形式：基图元素→Zc×Zc 循环移位子矩阵，硬件友好。 |
| [[Base_Graph_基图]] | NR LDPC 码的模板矩阵；BG1 用于大 TB 高吞吐，BG2 用于小 TB 低延迟。 |
| [[Layered_LDPC_Schedule_分层LDPC调度]] | 逐行更新 CN/VN、后一层立即可用前一层结果，收敛速度约 2× Flooding。 |
| [[Sum_Product_Algorithm_和积算法]] | LDPC 译码标准算法，在 Tanner 图 VN 和 CN 之间迭代传递 LLR 消息。 |
| [[Min_Sum_Algorithm_最小和算法]] | SPA 的硬件友好简化：CN 更新用 min 替代 tanh/atanh，高估可靠度 1-3 dB。 |
| [[Turbo_码]] | LTE 数据业务的主要编码家族，两个组成译码器通过交织器交换外信息实现迭代增益。 |
| [[RSC_Code_递归系统卷积码]] | Turbo 码的组成编码器，含反馈回路；LTE 用两个 8-state RSC 编码器并行级联。 |
| [[QPP_Interleaver_QPP交织器]] | LTE Turbo 内部交织器 Π(i)=(f₁·i+f₂·i²) mod K，无冲突特性支持并行译码。 |
| [[Polar_码]] | NR 控制信息的主要编码家族，用 SC/SCL/CA-SCL 译码保护控制比特。 |
| [[Channel_Polarization_信道极化]] | N=2ⁿ 独立信道经 G₂⊗ⁿ 变换后，部分趋于完美（容量→1）、部分趋于完全噪声（容量→0）。 |
| [[SCL_Decoding_SCL译码]] | 保留 L 条候选路径并行搜索，每个信息位分裂为 0/1 两条再修剪。 |
| [[CA_SCL_CRC辅助SCL]] | NR Polar 的实际译码方案：信息位前附加 CRC，SCL 后用 CRC 选最优路径。 |
| [[BCJR_Algorithm_BCJR算法]] | 最优逐比特 MAP 译码算法，在网格图上运行前向 α 和后向 β 递归。 |
| [[Iterative_Decoding_迭代译码]] | 多个软输入软输出译码器反复交换外信息（extrinsic），逐步提升比特置信度。 |
| [[LLR_对数似然比]] | 用有符号数表达比特倾向与可靠度；本库约定正 LLR 更像 0。 |
| [[LLR_Quantization_LLR量化]] | 浮点 LLR 经裁剪与量化映射到有限定点网格；±31（6-bit）是工程拐点。 |
| [[CRC_循环冗余校验]] | 错误检测机制：按生成多项式附加校验余数，余数通过表示"未检测到错误"，不负责纠错。 |
| [[CRC_Polynomials_CRC生成多项式]] | 3GPP 定义了 7 种长度 6-24 bit 的 CRC 生成多项式，用于不同 TB/CB/控制信息场景。 |
| [[Soft_Demodulation_软解调]] | 把接收符号 y 映射为每个编码比特的 LLR、保留软信息；硬判决丢失可信度，BLER 损失 2-3 dB。 |

### 信道、调制与性能

| 笔记 | 一句话 |
|:---|:---|
| [[AWGN_信道模型]] | 最基本的通信信道 y=x+n（n 为高斯噪声），LTE/NR 译码器 BER/BLER 性能基准的定义场景。 |
| [[TDL_信道模型]] | 3GPP 定义的多径衰落信道模型：若干不同时延的抽头叠加，TDL-A~E 剖面可选。 |
| [[Fading_Channel_衰落信道]] | 实际无线信道的多径衰落；瑞利衰落是 NLOS 默认模型，LLR 可信度随瞬时信道质量波动。 |
| [[Coherence_Bandwidth_Time_相干带宽与时间]] | 衰落信道在频率/时间上"看起来一样"的两个尺度，是信道估计与均衡颗粒度设计的依据。 |
| [[Timing_Sync_定时同步]] | OFDM 接收的第一关：FFT 窗口必须对准符号边界；仿真用理想定时，实际靠 PSS/SSS 或 CP 相关。 |
| [[Modulation_Constellations_调制星座]] | 比特组到复基带符号的映射；LTE/NR 用格雷映射使相邻星座点仅差 1 bit。 |

### MIMO 与接收

| 笔记 | 一句话 |
|:---|:---|
| [[MIMO_多天线系统]] | 收发两端都用多根天线的传输方式，基带模型 y=HPx+n，能提升容量。 |
| [[MMSE_均衡]] | 用线性滤波器 W=Hᴴ(HHᴴ+σ²I)⁻¹ 最小化均方误差，在消除干扰与不放大噪声之间折中。 |
| [[Sphere_Decoding_球面检测]] | ML 最优检测算法，用"半径剪枝"把搜索限制在球内，避免指数枚举。 |
| [[Detector_Comparison_检测器对比]] | MF/ZF/MMSE/Sphere 四族检测器是精度与实现代价之间的不同折中。 |
| [[Channel_Estimation_信道估计]] | 接收链路第一步：用已知参考信号（DMRS）估计信道矩阵 H，为均衡/检测提供输入。 |
| [[Diversity_Combining_分集与合并]] | 多份独立衰落的拷贝合并压低深衰落概率；MRC 是最优线性合并方式。 |

### 概率整形

| 笔记 | 一句话 |
|:---|:---|
| [[Probabilistic_Shaping_概率整形]] | 只改星座点使用概率（内圈多用、外圈少用）不改坐标，降低平均能量获得整形增益。 |
| [[PAS_概率幅度整形]] | PS 与 FEC 结合的框架：符号拆成"幅度"（可整形）与"符号"（保持均匀），只对幅度整形。 |
| [[Distribution_Matching_分布匹配]] | 概率整形的映射引擎：把均匀 0/1 bit 可逆映射为符合 MB 分布的幅度序列。 |
| [[ESS_枚举球面整形]] | DM 的一种实现：能量球约束下用 DP 计数表把 rank 可逆映射为非均匀幅度序列。 |
| [[MB_Distribution_MB分布]] | 概率整形使用的目标符号概率分布 P(a)∝e^(−νa²)，ν=0 退化为均匀分布。 |
| [[SBPM_整形比特位置映射]] | 把 shaped bits 放到 QAM label 幅度位上的置换（4^k 块组织），TX/RX 对称操作。 |
| [[Geometric_Shaping_几何整形]] | 改星座点坐标的整形路线，因标准兼容性差，是 PS 的对照路线而非替代方案。 |
| [[LLR_Prior_LLR先验]] | PS 接收端在软解调时把符号的非均匀先验加入距离度量，内圈点更"可信"。 |
| [[Selective_Scrambling_选择性加扰]] | 只对非整形 bit 做标准 Gold 加扰、对 shaped bits 不加扰，保住 ESS 建立的非均匀统计。 |

### 工程与硬件

| 笔记 | 一句话 |
|:---|:---|
| [[Fixed_Point_Numbers_定点数]] | 用固定位宽整数表示实数，Qm.n 格式决定动态范围和精度，是硬件实现基础。 |
| [[Bit_Exact_Regression_比特精确回归]] | 同一输入在所有实现层级（Python↔C/C++↔RTL）产生逐比特一致输出。 |
| [[Golden_Model_黄金模型]] | 用 Python 实现的浮点精度译码参考模型，作为定点化、RTL 与 bit-exact 回归的"黄金标准"。 |
| [[RTL_Microarchitecture_RTL微架构]] | 用 Verilog/SystemVerilog 描述译码器数据通路、控制状态机和存储结构的硬件蓝图。 |
| [[SIMD_Memory_Layout_SIMD内存布局]] | 一条指令同时处理多数据；译码器 CN/VN 并行更新天然适合 SIMD。 |

### 数学与信息论

| 笔记 | 一句话 |
|:---|:---|
| [[GF2_伽罗瓦域]] | 只含 {0,1} 的有限域：加法为 XOR、乘法为 AND，是 CRC/LDPC/Polar 运算的基础。 |
| [[GF2_Polynomials_GF2多项式]] | 系数在 GF(2) 上的多项式，二进制串与多项式系数一一对应，是 CRC 与 LDPC 校验矩阵的代数基础。 |
| [[Information_Theory_信息论基础]] | 熵度量不确定性，信道容量给出可靠通信最大速率，香农限是任何译码器无法超越的 Eb/N0 下界。 |
| [[Probability_Bayes_概率与贝叶斯]] | 贝叶斯定理把先验信念与观测证据结合产出后验概率，是 SISO 译码器的推理核心。 |
