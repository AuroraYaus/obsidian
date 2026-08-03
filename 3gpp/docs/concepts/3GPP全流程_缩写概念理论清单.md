---
type: definition
aliases:
  - 3GPP 全流程缩写概念理论清单
  - evaluation-link-simulator 知识索引
tags:
  - 3gpp
  - docs
  - concept-index
source_spec: "3GPP_6G_PS（evaluation-link-simulator-main）"
---
# 3GPP 链路仿真器（evaluation-link-simulator）全流程：项目内没有的缩写、概念、理论清单

> 已剔除知识库已覆盖条目（对照 100 课 + 46 概念笔记）。
> 来源：`3GPP_6G_PS/`（现目录名 `3GPP_PS/`）（evaluation-link-simulator-main 代码 + reproduction_output/analysis 8 份分析 + deep_dive 5 份深挖）
> 日期：2026-08-02；2026-08-03 依据 3GPP_FULL_LINK 全量源材料交叉复核补齐（缩写 +9、概念 +27、理论 +18）

## 一、缩写清单（A-Z）

### 通信/物理层
| 缩写 | 全称 | 一句话 |
|---|---|---|
| CSI | Channel State Information | 信道状态信息 |
| DCI | Downlink Control Information | 下行控制信息 |
| DL-SCH | Downlink Shared Channel | 下行共享传输信道 |
| DMRS | Demodulation Reference Signal | 解调参考信号 |
| Gold | Gold Sequence | Gold 序列（加扰） |
| MAC | Medium Access Control | 媒体接入控制层 |
| MIMO | Multiple-Input Multiple-Output | 多输入多输出 |
| MMSE | Minimum Mean Square Error | 最小均方误差（均衡） |
| MRC | Maximum Ratio Combining | 最大比合并 |
| OCC | Orthogonal Cover Code | 正交覆盖码（DMRS 端口复用） |
| PDCCH | Physical Downlink Control Channel | 物理下行控制信道 |
| PDSCH | Physical Downlink Shared Channel | 物理下行共享信道 |
| PRACH | Physical Random Access Channel | 物理随机接入信道 |
| PSS | Primary Synchronization Signal | 主同步信号（定时/小区搜索） |
| PUCCH | Physical Uplink Control Channel | 物理上行控制信道 |
| PUSCH | Physical Uplink Shared Channel | 物理上行共享信道 |
| RLC | Radio Link Control | 无线链路控制层 |
| RNTI | Radio Network Temporary Identifier | 无线网络临时标识 |
| SIMO | Single-Input Multiple-Output | 单入多出 |
| SINR | Signal to Interference plus Noise Ratio | 信干噪比 |
| SISO | Single-Input Single-Output | 单入单出 |
| SSS | Secondary Synchronization Signal | 辅同步信号（定时/小区搜索） |
| TDL | Tapped Delay Line | 抽头延迟线信道模型 |
| UE | User Equipment | 用户设备 |

### 概率整形（PS）体系
| 缩写 | 全称 | 一句话 |
|---|---|---|
| PS | Probabilistic Shaping | 概率整形 |
| PAS | Probabilistic Amplitude Shaping | 概率幅度整形（amplitude/sign 分工） |
| DM | Distribution Matcher | 分布匹配器（均匀 bit→非均匀幅度） |
| ESS | Enumerative Sphere Shaping | 枚举球面整形（DM 的一种实现） |
| MB | Maxwell-Boltzmann | 麦克斯韦-玻尔兹曼分布（目标概率） |
| SBPM | Shaped Bit Position Mapping | 整形比特位置映射 |
| GS | Geometric Shaping | 几何整形（改星座点位置，非 PS） |
| R_eff | Effective Code Rate | 有效码率（PS 公平比较口径） |
| LUT | Look-Up Table | 查找表 |
| RRC | Radio Resource Control | 无线资源控制（信令层） |

### 算法/数学/硬件
| 缩写 | 全称 | 一句话 |
|---|---|---|
| Cholesky | Cholesky Decomposition | 乔列斯基分解（正定矩阵） |
| DFT | Discrete Fourier Transform | 离散傅里叶变换（预编码） |
| FP | Fincke-Pohst | 球面枚举策略（按星座顺序区间） |
| Hadamard | Hadamard Matrix | 阿达玛矩阵（预编码） |
| LFSR | Linear Feedback Shift Register | 线性反馈移位寄存器 |
| LUT | Look-Up Table | 查找表 |
| MACs | Multiply-Accumulate | 乘累加操作 |
| MF | Matched Filter | 匹配滤波 |
| ML | Maximum Likelihood | 最大似然（检测） |
| MAP | Maximum A Posteriori | 最大后验 |
| QR | QR Decomposition | QR 分解 |
| Rhh | HᴴH correlation matrix | 信道相关矩阵（PS 正则化 Gram） |
| SE | Schnorr-Euchner | 球面枚举策略（按部分距离排序） |
| SRAM | Static RAM | 静态随机存取存储器 |
| Wiener | Wiener Filter Estimation | 维纳滤波信道估计（MMSE 估计） |
| ZF | Zero Forcing | 迫零均衡（MMSE 的 σ²→0 极限） |
| ADC | Analog-to-Digital Converter | 模数转换器 |
| DAC | Digital-to-Analog Converter | 数模转换器 |
| PAPR | Peak-to-Average Power Ratio | 峰均功率比 |
| EVM | Error Vector Magnitude | 误差矢量幅度 |
| PA | Power Amplifier | 功率放大器 |
| CORDIC | Coordinate Rotation Digital Computer | 坐标旋转数字计算 |
| ROM | Read-Only Memory | 只读存储器 |
| O(n) | Big-O notation | 复杂度记号 |
| Nrx/Ntx | Receiver/Transmitter antennas | 收/发天线数 |
| Nfft | FFT size | FFT 点数 |
| Nlayers | Number of layers | 层数 |
| Nre | Number of resource elements | 资源元素数 |
| Qm | Modulation order | 调制阶数 |
| ν (nu) | Shaping strength | 整形强度参数 |
| k0 | Rate matching starting position | 速率匹配起点 |

## 二、概念清单（按链路分类）

### A. 发送链路
- Gold 序列加扰（双 31-bit LFSR、c_init）
- PDSCH 加扰 c_init 结构（n_RNTI·2¹⁵+q·2¹⁴+n_ID；PDSCH 不含时隙/符号号，区别于 DMRS/PDCCH 的通用结构）
- Gold 序列硬件化（2×31-bit LFSR；A³² 状态跳跃 32 路并行，62-bit 状态，串行 324K cycles → 并行 10,140）
- 层映射与预编码（DFT/Hadamard/Identity）
- 单码字 ≤4 层协议约束（TS 38.211 §7.3.1.3；5-8 层双码字，仿真器只有单 nrDLSCH）
- DMRS 与数据同走预编码（层域插入后同乘 P；DMRS-based 估计直接给 H_eff，接收端无需知道 P）
- RE 映射与 DMRS 插入
- PS TB 构造（四段结构：punctured/unshaped_before/shaped/unshaped_after）
- PS 功率归一（√psPowerScaling）

### B. 信道
- TDL-A~E 信道模型（delay spread/Doppler/coherence）
- 相干带宽/相干时间（B_c≈1/(2πτ_rms)≈530 kHz ≫ 30 kHz SCS——每子载波内平坦；T_c≈0.423/f_d≈14.1 ms ≫ 0.5 ms 时隙——准静态）
- 信道估计（完美估计 vs DMRS 实际估计）
- AWGN 噪声模型（σ=1/√(2·Nrx·Nfft·SNR) 三因子口径；实测 n_var 误差 <0.05%）
- 信道播种与可复现性（TDL Seed=rngSeed+17、每 SNR 点 reset(channel)）

### C. 接收链路
- OFDM 解调（信号+噪声各一次 FFT）
- 定时同步（仿真：nrPerfectTimingEstimate；实际：PSS/SSS 或 CP 相关滑动窗 O(Nfft×Ncp) MACs）
- 信道估计实现（LS：Ĥ=Y_DMRS/X_DMRS，噪声放大 1/|X|²；维纳滤波：Ĥ=R(R+σ²I)⁻¹Ĥ_LS，低 SNR 显著优于 LS，O(N³)）
- 估计误差三途径（均衡输出偏置、CSI 失真、噪声方差失配；256QAM d_min≈0.16，偏移超 0.08 硬判决翻转）
- MMSE 均衡（W=Hᴴ(HHᴴ+σ²I)⁻¹、归一化危险点）
- 球面检测（ML/Fincke-Pohst/Schnorr-Euchner）
- 三检测器对比（MMSE SISO 1 MAC/tone ~1K gates；MMSE 4×4 ~100 MACs ~95K gates，损失 1-3 dB；Sphere ~100-1000 MACs ~150K gates，0 dB 损失，仅高 SNR 可用）
- PS 接收：LLR prior、选择性解扰、inverse ESS

### D. 概率整形体系（重点专题）
- 整形增益（shaping gap、1.53 dB 上限、实测 AWGN 0.5-1.2 dB）
- 整形增益 ROI（AWGN MCS10 0.8-1.2 / MCS20 0.5-0.8 dB；TDL-A 0.3-0.6 / 0.2-0.4 dB；1 dB @3.5 GHz ≈ 20-25% 覆盖半径）
- 概率整形 vs 几何整形（PS 改使用概率不改星座几何，可叠加 NR QAM 链路；GS 改星座点位置、需协商新星座表）
- 四个接入点架构（PS 只改 TB 构造、加扰、解调前、LDPC 解码后 4 处；NR spine 全部复用——"只改四处"成立因各级只认长度/统计约定）
- rate loss（熵损失、payload vs chain TBS）
- PS 几何可行性条件（numParityBits ≤ 2N_s(Qm/2−k)−L_cb；2Zc+2kN_s ≤ K−F−L_cb）
- MB 分布（ν 控制概率/能量/熵）
- ESS 编解码（能量球约束、DP 表、增量窗口、rank 路径）
- 编解码非对称性（编码 O(n) 增量窗口严格串行 ~20K gates；解码 O(1) 查表 ~10K gates；与 LDPC 快编慢解互补）
- ESS 工程：整数能量 (s²−1)/8、mantissa/exponent 定点表、分块残差、错误传播
- 能量表生命周期（per-config 生成一次 33K DP 步；行索引单调、列波动，无法按行预取；TBS 匹配每次二分重跑）
- SBPM（4^k 块置换、TX/RX 反置换）
- 选择性加扰/解扰（shaped mask、row routing、LLR sign flip）
- PS 解调 LUT（先验偏置）
- 有效码率 R_eff = payloadTBS/(N_RE·Qm)（与目标码率 R 脱钩）
- TBS 匹配（nu 二分搜索）
- PS-MIMO 预处理（ν 正则项、Rhh、Cholesky、白化匹配滤波）

### E. PHY 支撑
- 1024QAM（32×32 星座、SNR/EVM/PA 线性度）
- 4 张 MCS 表结构（qam64 0-28 / qam256 0-31（28-31 保留）/ ps_mcs_table1/2 5-27；5 列 [MCS, SE, Qm, R×1024, ν_MB]）
- PS 表有效频谱效率（SE ≠ Qm·R/1024：MCS10 表 2.5704 vs 计算 4.5——整形压缩信息速率）
- CSI/SINR（post-eq SINR、CSI weighting）
- 吞吐计算（NRE×Qm×R×层×slots/s）
- 实测吞吐（MCS10 4.94 / MCS15 8.96 / MCS20 12.29 Mbps；256QAM 4 层 ~480；MCS27 ~570 Mbps；273PRB 外推 2.5/5.0/3.0 Gbps）
- 链路仿真方法（固定 MCS BLER/吞吐、SNR 扫描、seed 管理）

### F. 协议栈背景
- MAC（逻辑信道/DL-SCH/HARQ/LCID）
- RLC 三模式（TM/UM/AM）
- PDCP（加密/完整性）
- SDAP/QoS（QoS flow/DRB）
- 上下行物理信道边界（PDSCH/PUSCH/PUCCH/PDCCH/PRACH）
- BWP、K0/K1 时序

### G. 工程代价
- 全链路位宽追踪（TX 14 级/RX 18 级、Rhh 24-bit 最大）
- 位宽决策树（QAM 16 + PS 3 + 4 层 2 + TDL 2 + Cholesky real 4 = 23→24-bit I/Q；LLR 恒 ±31）
- 无缩放 IFFT 28-bit 上界（max|x(n)| ≤ N_sc·|X|_max = 1024×；缓解=蝶形分级缩放）
- LLR 裁剪-损失权衡（±7 4-bit <0.1 dB、±15 5-bit <0.05、±31 6-bit <0.02、±63 <0.01 dB；±31 吸收 MMSE 归一化放大）
- ESS 能量表 SRAM（264KB）
- ESS 编码器硬件化（O(n) 路径选择）
- MIMO/Cholesky 硬件预算（per-RE、slot budget）
- 时隙 cycle 预算（61,440 @122.88 MHz；273PRB 122,880 @245.76 MHz）
- 各阶段 cycle 需求（LDPC ~5.1M 专用引擎（81×超预算）；Rhh+Cholesky ~486,720 ≥8 路；MMSE ~162,240 ≥4 路；FFT ~20,480 4 引擎；ESS 编码 ~30,000 / 解码 ~1,500）
- 存储子系统占比（MIMO 矩阵族 26% + 信道估计 20% + PS 16% = 62%；LDPC 仅 8%——完整 Modem 存储大头在每 RE 矩阵与信道状态）
- 面积/功耗估算（7nm 52PRB：~7.4M gates、~6.1 MB、~4.0 mm²（SRAM 40%/逻辑 60%）、~167 mW；273PRB 外推 ~19 mm²）
- PS 硬件开销（ESS 编/解码 20K/10K gates、能量表 ~5K、TBS 匹配 ~10K、Cholesky 预处理 ~90K、PS 总计 ~155K gates ~36 mW；相对 NR 基线 +55% gates +45% SRAM +28% 功耗）
- PS 全系统代价（gates/SRAM/power/PA backoff）

## 三、理论清单（数学/信息论）

| 理论 | 内容 | 出处 |
|---|---|---|
| 香农容量与高斯输入最优 | 平均功率受限时高斯输入达到容量；均匀星座的 gap | PS01 §1 |
| 整形增益上限 1.53 dB | πe/6 球体积推导（无限星座/高 SNR 极限） | PS01 §7 |
| 1.53 dB 的三个折扣因素 | 有限星座、有限块长、有限 SNR；组成约束损失 ~(1/2n)log₂n；可达速率 R_PS(ν)=H_ν−(1/n)log₂(能量受限组成数/2^{H_νn}) | PS01 §1.3、§2.6 |
| 概率整形 vs 几何整形 | PS 只改使用概率不改星座几何（可叠加 NR QAM）；GS 改星座点位置需协商新表；3GPP Rel-19 语料无 PS 实证，商用先例 DVB-S2X（CCDM+MB） | PS01 §1.2、§1.4 |
| Maxwell-Boltzmann 分布推导 | 拉格朗日乘子法：给定功率熵最大 / 给定熵功率最小 | PS01 §2 |
| MB 对偶性与单调性 | 同族分布同时是"给定功率熵最大"与"给定熵功率最小"的解；dH/dν=−ν·Var_ν(A²)≤0，熵-功率权衡曲线由 ν 参数化 | PS01 §2.6 |
| 枚举球面整形（ESS） | 算术编码式枚举：组成空间/能量壳/增量窗口/rank 路径 | PS01 §3 |
| DP 计数表递推 | count(n,e) 递推、边界条件、表维度 | PS01 §5 |
| CCDM vs ESS | 固定组成 vs 能量球约束的 rate/复杂度对比 | PS01 §3/§5 |
| 有限块长速率损失实测 | 16QAM k=1：n=128→0.0307、116→0.0423、104→0.0469 bit/符号；256QAM：0.0279–0.0424；三来源：条件化+floor+量化截断 | PS01 §6.4 |
| 功率节省公式 | ΔP_shaping(R)=10log₁₀(E_uniform/E_MB(ν(R)))，ν(R) 由 H_ν=2R−1 确定；16QAM 2.04 / 64QAM 0.84 / 256QAM 1.71 / 1024QAM 0.59 dB | PS01 §7.1 |
| 衰落信道整形增益变小三机制 | ①高 SNR 才显著、深衰落权重高；②信道随机化 I(X;hX+N)=E_h[·]；③ν̃ 正则化补偿不完美 | PS01 §7.3 |
| ν̃ 归一化整形速率 | ν̃=ν·(2/3)(2^Qm−1)=ν·E_s，E_s=2(2^Qm−1)/3；实测 3.86–5.73 与 Gram 矩阵同量级，不可忽略 | PS02 §5.1 |
| 完整平方 MAP 度量 | M(x)=‖y−Gx‖²+ν̃σ²‖x‖²；R_hh=GᴴG+ν̃σ²I，H_eq=chol(R_hh)，Y_eq=H_eq·R_hh⁻¹Gᴴy；SISO β 模式、SIMO MRC 模式为其 1×1/1×N 特例 | PS02 §5.2-5.4 |
| MMSE 均衡推导 | Wirtinger 求导、csi≥1 恒成立、归一化=ZF 化 | MIMO01 §5 |
| ZF/MF 两极限 | σ²→0 退化为 ZF（消干扰放大噪声）；σ²→∞ 退化为匹配滤波；MMSE 相对 ZF 1-3 dB 增益 | MIMO01 §5.1 |
| MRC 分集阶数 | SNR_out=‖h‖²/σ²～χ²₆₄（32 分支）；P(‖h‖²<ε)~ε³²/32!；32 天线 ≈ +15 dB，0-6 dB 下 256QAM 可行 | MIMO01 §3.2-3.3 |
| LS 与维纳滤波信道估计 | Ĥ_LS=Y_DMRS/X_DMRS（噪声放大 1/|X|²）；Ĥ_MMSE=R_HH(R_HH+σ²I)⁻¹Ĥ_LS（低 SNR 显著优、O(N³)）；估计误差三途径 | MIMO01 §4.2-4.3 |
| Cholesky 分解 | 正定矩阵三角分解、PS 正则化 Rhh=HᴴH+ν̃σ²I | MIMO01 §5、PS02 §6 |
| Tikhonov 正则化 | MAP 先验 → ν̃σ²I 正则项（ν 与 MB 分布的联系） | MIMO01 §5 |
| 球面检测 | ML 枚举、QR 树搜索、FP/SE 剪枝 | MIMO01 §6 |
| 白化匹配滤波 | 有色噪声白化、等效信道构造 | MIMO01 §6 |
| Gold 序列理论 | 双 m 序列、互相关界（t(31)=65537≈−90dB） | PHY01 §2 |
| AWGN 噪声三因子口径 | σ=1/√(2·N_rx·N_fft·SNR_lin)：Nfft 时/频功率密度换算、Nrx 每天线独立噪声、×2 I/Q 两路；N₀=1/SNR 恒等、实测误差 <0.05% | PHY01 §4 |
| 相干带宽/相干时间 | B_c≈1/(2πτ_rms)≈530 kHz；T_c≈0.423/f_d≈14.1 ms；30 Hz @3.5 GHz = 9.3 km/h | PHY01 §5.2 |
| MCS 表 5 列结构与 PS SE 口径 | [MCS, SE, Qm, R×1024, ν_MB]；PS 表 SE ≠ Qm·R/1024（整形压缩信息速率） | SIM01 §4.1 |
| 有效码率新定义 | R_eff=payloadTBS/(N_RE·Qm)，与目标码率 R 脱钩；PS 公平比较口径 | PS02 §8.1 |
| 位宽追踪方法 | 逐级位宽表、最坏位宽推导链 | PHY01 §7 |
| LLR 裁剪-损失权衡 | 动态范围（1024QAM max|y−x|²≈11.2、SNR 30dB → LLR_max≈11200 需 14-bit）；裁剪表 ±7~±63 损失 <0.1 dB；±31 吸收 MMSE 归一化放大 | PHY01 §12、MIMO01 §5.4 |
| 定点量化漂移 | dec2binFloat 截断（非四舍五入）误差 <2^(−(M−1))=0.39%；|A|=8 ν=0.0054 时 n≥64 指数漂移（367 vs 368，0.3%） | PS01 §5.3 |
| 链路仿真统计 | BLER 置信度、公共随机数、TBS matching 公平性 | SIM01 §1/§2 |
| BLER 零错误上界 3/N | N=200 → 分辨率 0.5%、零错误点 95% 上界 3/N=1.5e-2；公共随机数使点间误差相关，不可当独立样本 | SIM01 §2.8 |
| 功率缩放数学 | E_new=4E+1 递推、7-14× 实测 | PS02 §7 |
| MAP 检测与 LLR prior | 非均匀先验进入距离度量 | PS02 §6 |
| 周期/存储/面积预算三件套 | slot budget 61,440 cycles；存储占比 MIMO 26%+CE 20%+PS 16%=62%（LDPC 仅 8%）；7nm 52PRB ~4.0 mm²、7.4M gates、~167 mW | PHY01 §8-10、06 §3-4 |

## 四、注记

- 清单覆盖：代码（49 个 .m 文件）+ 分析文档（00-07）+ 深挖文档（PS01/PS02/MIMO01/PHY01/SIM01）
- 2026-08-03 复核补齐：依据 3GPP_FULL_LINK 全量源材料（8 分析 + 5 深挖 + 49 代码文件）三方交叉提取，补齐缩写 +9、概念 +27、理论 +18
- 勘误：MCS12 的 ν=0.0918（analysis 04 原标注 MCS15 有误，见 PS02 §2.7）
- 缩写"AGROW/INIT/RUN/CONFIG"等为代码内部标识符，未列入
- 理论清单以深挖文档的数学推导为准（均有公式与数值验证）
- 方法学可迁移（SIM01 §9.2 十条）：固定 MCS 扫 SNR 协议、公共随机数、payload 口径、实测噪声自检列、静态热循环分离、校验即文档、往返恒等第一道闸门、BLER 置信度补强、配置对象整体回传
