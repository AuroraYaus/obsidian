---
type: spec
aliases:
  - lte nr depth gap backlog
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/lte_nr_depth_gap_backlog.md"
---
# LTE/NR Decoding Depth Gap Backlog

用途：记录从 `/home/yys/ClaudeCode/ldpc` 和 `/home/yys/ClaudeCode/LDPC_Basics` 对照得到的深度缺口。后续扩写现有章节或新增少量专题章节时，以本台账为执行清单；完成一项必须勾选并在“完成记录”追加证据。

范围：当前项目 `docs/L1_基础`、`docs/L2_协议算法`、`docs/L3_工程实现` 共 94 篇讲义，以及必要的 `tools/figures`、`docs/audits`、路线图和全局规则。

原则：

- 扩写现有章节优先，新增章节只用于协议阅读地图、跨章节专题或现有章节无法承载的系统级内容。
- LTE Turbo、NR LDPC、NR Polar 都要检查同类质量缺口；不能只补 NR LDPC。
- Prompt 覆盖是最低线；本台账关注“没有、不够详细、不够深入、不够突出、不够直观、不够协议精读、不够工程闭环”的差距。
- 所有协议相关补写必须核验 Rel-19 本地资料，记录 TS 编号、包版本、章节、表/图/公式和本地路径。
- 参考项目中的 PPA、综合、门级仿真、定点性能和阈值结果不能直接写成当前项目真实证据；没有本项目日志、种子、脚本和输出时，只能写方法、模板或待证据项。

## 状态标记

| 标记 | 含义 |
|:---|:---|
| `[ ]` | 未开始。 |
| `[~]` | 进行中。 |
| `[x]` | 已完成并写入完成记录。 |
| `N/A` | 已评估但不适用，必须写明原因。 |

## 质量维度

- **缺失维度**：参考项目已讲，当前项目没有独立讲解或只在一句话中出现。
- **深度维度**：当前项目有标题或公式，但缺少术语来源、动机、理论铺垫、手算例子、推导链或失败案例。
- **突出维度**：当前项目讲了，但主线地位不清，读者不知道它为什么重要、在哪个协议链路被调用。
- **协议维度**：当前项目只写通用原理，未解释 3GPP 为什么这样规定、接收端如何据此反向处理。
- **图表维度**：循环缓存、矩阵、路径搜索、调度、缓存生命周期、性能曲线等难理解内容缺少 Python 图，或图不够直观。
- **工程维度**：缺少仿真、定点、RTL/ASIC、验证、证据边界、失败 dump 或 descriptor 字段。

## 执行级记录模板

后续每处理一个缺口，不允许只勾选“已补”。必须按下表追加一条执行记录，保证能追踪“为什么补、补到哪里、如何验收”。

| 字段 | 填写要求 |
|:---|:---|
| 缺口编号 | 使用本文件编号，例如 `B2-03`、`D4-05`。 |
| 缺口类型 | 从缺失、深度、突出、协议、图表、工程六类中选择，可多选。 |
| 参考来源 | 写清参考文件路径和章节标题；不能只写 `ldpc` 或 `LDPC_Basics`。 |
| 当前章节 | 写当前项目受影响文件路径，例如 `docs/L2_协议算法/T8.5_LDPC_sum_product_BP.md`。 |
| 现状问题 | 具体描述现有正文哪里薄，例如“只有 check node 公式，缺少边缘化来源”。 |
| 补写范围 | 写新增小节标题、表格、公式、图、伪代码或例子。 |
| 协议证据 | 写 TS 编号、Rel-19 包、本地路径、章节、表/图/公式；若是算法背景，写明非协议强制。 |
| 图表要求 | 写是否需要 Python 图、图名、脚本路径、图中必须出现的元素。 |
| 工程要求 | 写是否补浮点、定点、RTL/ASIC、验证、failure dump、descriptor 字段。 |
| 验收命令 | 写单篇或批量审计命令；涉及图时加几何和可读性审计。 |
| 完成证据 | 写审计输出、图片路径、脚本输出、人工复核结论。 |

## 缺口严重度定义

| 严重度 | 判定标准 | 处理顺序 |
|:---|:---|:---|
| Critical | 现有章节会误导读者、协议结论可能错误、图表遮挡导致无法读懂、公式无法渲染、把模板写成真实证据。 | 立即修复，修复后复跑单篇和相关模块审计。 |
| Important | 内容存在但明显不够深，缺少理论推导、协议前因后果、关键图、关键例子、工程验证或 prompt 关键拓展。 | 本轮深度增强优先处理。 |
| Normal | 内容可读但不突出，缺少横向对比、补充例子、术语表、常见错误或更清晰的图。 | 随模块扩写处理。 |
| Deferred | 属于真实工程阶段，例如真实 BLER、真实综合、真实 STA、真实功耗报告。 | 记录证据边界，不在文档阶段伪造结果。 |

## 处理批次

| 批次 | 目标 | 章节范围 | 完成定义 |
|:---|:---|:---|:---|
| P0 | 建立入口和协议地图 | A1-A3 | 新增或扩写协议阅读地图、TS 38.212 Chapter 5 地图、TS 38.214 MCS/TBS descriptor 专题。 |
| P1 | 修复共同理论底座 | B1-B4，L1 T1-T5 | 初学者能理解 GF(2)、概率、LLR、AWGN/QAM、性能曲线，再进入 LTE/NR 协议。 |
| P2 | 补齐 LTE Turbo 深度 | C1-C3，L2 T6-T7 | LTE Turbo 不再只是 NR 对照项，具备协议、算法、rate recovery、HARQ、边界案例完整链。 |
| P3 | 补齐 NR LDPC 深度 | D1-D5，L2 T8-T9 | LDPC 术语、BG 结构、BP 推导、rate matching、IR-HARQ、error floor 和工程映射完整。 |
| P4 | 补齐 NR Polar 深度 | E1-E3，L2 T10 | Polar 理论、协议角色、SC/SCL/CA-SCL、rate recovery 和 small block 边界完整。 |
| P5 | 补齐横向比较和工程闭环 | T11-T15，F1-F3，G | 三类译码器在仿真、定点、RTL/ASIC、验证、综合、STA、低功耗和最终证据上有可执行模板。 |

## 章节级补齐矩阵

### L1 共同基础章节

| 编号 | 当前章节 | 缺口类型 | 参考来源 | 具体补写动作 | 图表与验收 |
|:---|:---|:---|:---|:---|:---|
| B1-01 | `T1.1_GF2_binary_arithmetic_for_decoders.md` | 深度、突出 | `ldpc/docs/L1_理论基础/T1.1_GF2有限域运算.md` | 增加“为什么二进制信道编码需要 GF(2)”小节；补 GF(2) 与普通整数、模 2 算术、XOR 硬件门的关系；增加 3 个手算例子：奇偶校验、二进制加法、短多项式乘法。 | 不新增协议图；单篇术语、标题、深度、LaTeX 审计。 |
| B1-02 | `T1.3_GF2_vectors_matrices.md` | 缺失、深度 | `ldpc/docs/L1_理论基础/T1.2_编码线性代数.md` | 补生成矩阵 `G`、校验矩阵 `H`、行空间、零空间、系统形式、`GH^T=0`；增加一个小型线性分组码从消息到码字再到 syndrome 的完整例子。 | 建议 Python 图：`G/H/零空间/校验子关系图`；图中文字居中、箭头从矩阵对象边界出发。 |
| B2-01 | `T1.4_probability_bayes_soft_decoding.md` | 深度 | `ldpc/docs/L1_理论基础/T1.3_概率与LLR基础.md` | 补联合概率、条件独立、全概率、边缘化；用 2 比特联合表说明“对未知变量求和”；增加 MAP 和 ML 的区别。 | 增加 Markdown 表格和 Python 小图可选；LaTeX 全检。 |
| B2-02 | `T1.5_LLR_soft_decision.md` | 深度、工程 | `ldpc/docs/L1_理论基础/T1.3_概率与LLR基础.md` | 补概率到 LLR、LLR 到概率的互转；补独立观测下 LLR 可加的推导；增加两个接收机观测合并的数值例子；连接 HARQ soft combining。 | 必须补一张“概率比值到加法证据”的教学图或表。 |
| B4-01 | `T1.6_information_theory_minimum_for_decoding.md` | 深度、突出 | `ldpc/docs/L1_理论基础/T1.4_信息论与信道容量.md` | 补 BSC/BEC/BI-AWGN 的直觉；解释容量、码率、容量差距、瀑布区、错误平层；说明这些不是协议门槛，而是性能分析语言。 | 建议 Python 图：容量边界、瀑布区、错误平层三段曲线。 |
| B3-01 | `T2.9_AWGN_noise_scaling.md` | 深度、工程 | `ldpc/docs/L1_理论基础/T1.6_AWGN信道模型与噪声特性.md` | 补实基带和复基带噪声方差差异；补 `N0/2`、Eb/N0、Es/N0、码率、调制阶数换算；列四类 LLR scaling bug。 | 增加噪声缩放错误诊断表；可选 Python 曲线图。 |
| B3-02 | `T2.14_QAM_Max_Log_MAP_demapping.md` | 深度、协议 | `ldpc/docs/L1_理论基础/T1.5_数字调制BPSK_QPSK_QAM.md` | 补 QAM 星座能量归一化、Gray 映射、1024QAM 复杂度、bit-channel 可靠性；核验 TS 36.211/38.211 调制入口。 | 若引用 1024QAM，必须记录 Rel-19 本地路径；建议补星座和 bit-channel 图。 |
| B4-02 | `T4.5_decoder_performance_metrics.md` | 深度、图表 | `ldpc/docs/L2_算法实现/T5.8_错误平层与陷阱集.md` | 在 BER/BLER 指标外补曲线读法：waterfall、error-floor、iteration saturation、confidence interval；补高 SNR 统计成本。 | Python 性能曲线图必须标注教学示意，不得伪装真实仿真结果。 |
| B1-03 | `T5.2_memory_banking_buffering_basics.md` | 工程 | `ldpc/docs/L1_理论基础/T1.2_编码线性代数.md`、`ldpc/docs/L3_硬件实现/T11.2_存储器架构设计.md` | 补稀疏矩阵存储、edge-major/layer-major、bank conflict 与译码器数据结构关系；连接 LDPC layered、Turbo interleaver、Polar path memory。 | 建议补统一 memory layout 对比表。 |

### LTE Turbo 章节

| 编号 | 当前章节 | 缺口类型 | 参考来源 | 具体补写动作 | 图表与验收 |
|:---|:---|:---|:---|:---|:---|
| C1-01 | `T6.1_LTE_Turbo_decoder_chain_overview.md` | 突出、协议 | `ldpc/docs/L1_理论基础/T0.1_LTE_NR译码学习路线与3GPP协议导读.md` | 增加 LTE Turbo 在 TS 36.212 中的发射侧位置和接收侧逆流程；说明 Turbo 在 LTE 数据链路中的历史角色；列 DL-SCH/UL-SCH/PCH 边界。 | 补一张 LTE Turbo 接收链图，覆盖 demapper、de-rate matching、Turbo、CB/TB CRC。 |
| C1-02 | `T11.1_Turbo_LDPC_Polar_algorithm_comparison.md` | 突出 | `LDPC_Basics/LDPC.md`、`ldpc/docs/L1_理论基础/T3.1_LDPC码发明与历史.md` | 增加“NR 为什么没有继续用 LTE Turbo 作为数据信道主码”的详细段落；维度包括吞吐、并行度、QC 矩阵、IR-HARQ、错误平层、功耗。 | 横向比较图要避免把 Turbo 写成过时无价值。 |
| C2-01 | `T6.2_RSC_code_foundation.md` | 深度 | `ldpc/docs/L1_理论基础/T3.2_Tanner图与因子图.md` | 补 RSC 编码器从卷积码到递归系统结构的动机；解释 systematic/parity/feedback/feedforward；增加 trellis 状态例子。 | 可补状态转移图；协议证据回链 TS 36.212 Turbo 编码结构。 |
| C2-02 | `T6.5_BCJR_MAP_decoding_intuition.md` | 深度 | `ldpc/docs/L1_理论基础/T1.3_概率与LLR基础.md` | 补路径概率、边缘化、前向 alpha、后向 beta、分支 gamma 的逐步来源；用小 trellis 手算一拍。 | 建议 Python 图：trellis 上 alpha/beta/gamma 的方向和含义。 |
| C2-03 | `T6.6_Log_MAP_Max_Log_MAP_Turbo.md` | 深度、工程 | `ldpc/docs/L2_算法实现/T5.3_BP算法对数域推导.md` | 补 log-domain 转换、Jacobian logarithm、max-star、Max-Log 近似误差、定点修正查表策略。 | 增加公式前后的符号解释；LaTeX 全检。 |
| C2-04 | `T6.7_Turbo_iteration_extrinsic_stopping.md` | 深度、工程 | `ldpc/docs/L2_算法实现/T9.4_早停策略比较.md` | 补外信息非回声原则、相关性积累、振荡、CRC early stop 风险、iteration cap 与功耗关系。 | 可补迭代轨迹示意图。 |
| C3-01 | `T7.1_LTE_Turbo_de_rate_matching_overview.md` | 协议、深度 | `LDPC_Basics/RateMatching_Detailed.md` | 补 LTE rate matching 与 NR rate matching 的共同抽象：母码、实际发送长度、puncturing、repetition、LLR 初始化；再落回 TS 36.212 Turbo 细节。 | 增加 LTE de-rate matching 接收侧逆流程表。 |
| C3-02 | `T7.2_LTE_subblock_deinterleaver_circular_buffer.md` | 图表、协议 | `LDPC_Basics/RateMatching_Detailed.md` | 补 sub-block interleaver 的动机和接收端 deinterleaver；说明 circular buffer 读写顺序、NULL、punctured、repeated 的状态差异。 | 必须有循环缓存图，标明 NULL、unknown、known、repeated。 |
| C3-03 | `T7.3_LTE_HARQ_soft_buffer_RV.md` | 深度、图表 | `LDPC_Basics/RateMatching_Detailed.md` | 在现有 ring buffer 基础上补 Chase Combining 与 Incremental Redundancy 的概率证据差异；补定点饱和和 same-bit LLR accumulation。 | 图中四个 RV 位置必须清晰，读图顺序和工程检测点保持间距。 |
| C3-04 | `T7.6_LTE_Turbo_decoder_edge_cases.md` | 工程、突出 | `ldpc/docs/L2_算法实现/T5.8_错误平层与陷阱集.md` | 增加高 SNR 仍失败、error floor、RV mismatch、NULL 与 punctured 混淆、LLR sign 反转、K+/K- 顺序错误的定位流程。 | 增加 failure bundle 字段表。 |

### NR LDPC 章节

| 编号 | 当前章节 | 缺口类型 | 参考来源 | 具体补写动作 | 图表与验收 |
|:---|:---|:---|:---|:---|:---|
| D1-01 | `T8.1_NR_LDPC_decoder_chain_overview.md` | 突出、协议 | `LDPC_Basics/LDPC.md` | 增加 TS 38.212 的核心定位、LDPC 在 NR 中的数据链路角色；明确 UL-SCH/DL-SCH/PCH 适用，DCI/BCH/UCI 不适用。 | 补“NR LDPC 适用/不适用信道”表。 |
| D1-02 | `T8.1_NR_LDPC_decoder_chain_overview.md` | 深度 | `LDPC_Basics/LDPC.md` | 增加通用 LDPC 与 NR LDPC 术语对照：base graph、lifting size、iLS、shift value、mother code、filler、first 2Zc puncturing。 | 表格必须解释每列含义，不只列术语。 |
| D1-03 | `T8.2_NR_LDPC_base_graph_selection.md` | 协议、深度 | `LDPC_Basics/LDPC.md` | 补 BG1/BG2 选择规则的因果：块长、码率、短块保护、硬件复杂度；解释 `A`、`B`、`R`、`Kcb`、`Kb` 的生命周期。 | 协议证据必须核验 TS 38.212 §5.2.2 和 §7.2.2 回链。 |
| D2-01 | `T8.3_NR_LDPC_lifting_QC_matrix.md` | 缺失、图表 | `LDPC_Basics/LDPC.md` | 新增 BG 五子矩阵 A/B/C/D/E 的结构角色；解释核心 parity、扩展 parity、双对角/近似双对角和 Raptor-like 结构。 | 必须生成 Python 图：BG 子矩阵区域、非零位置、QC lifting、decoder memory 视角。 |
| D2-02 | `T8.3_NR_LDPC_lifting_QC_matrix.md` | 深度、协议 | `LDPC_Basics/LDPC.md` | 补 `V_ij` 查表、`P_ij = V_ij mod Zc`、循环移位单位阵和全零子矩阵的逐步例子。 | 小矩阵例子必须能手算；图要标明 `Zc` 和 shift。 |
| D3-01 | `T8.4_LDPC_Tanner_graph_message_passing.md` | 深度 | `ldpc/docs/L1_理论基础/T3.2_Tanner图与因子图.md` | 补 variable node、check node、edge、cycle、girth、短环、消息相关性；说明短环为什么影响 BP。 | 增加 Tanner 图和短环高亮图。 |
| D3-02 | `T8.5_LDPC_sum_product_BP.md` | 深度 | `ldpc/docs/L2_算法实现/T5.2_BP算法概率域推导.md` | 从因子分解和边缘化推导 probability-domain BP；再转到 LLR-domain BP；每个公式前说明回答的问题。 | 增加一个 3 VN/2 CN 小图手算一轮消息。 |
| D3-03 | `T8.6_LDPC_MS_NMS_OMS.md` | 深度、工程 | `ldpc/docs/L2_算法实现/T5.4_最小和与改进变体.md` | 补 MS 为什么高估可靠度、NMS alpha、OMS beta、定点饱和、trapping set 与 error floor 风险。 | 补参数扫描模板，不写真实最优 alpha/beta。 |
| D3-04 | `T8.7_layered_LDPC_decoding_schedule.md` | 深度、工程 | `ldpc/docs/L2_算法实现/T5.5_调度策略洪泛与分层.md` | 补 flooding、layered、shuffled 的对比；说明 layered 为什么收敛快、为什么需要 read-modify-write、为什么容易有 bank conflict。 | 增加调度时序图或 layer-major memory 图。 |
| D4-01 | `T8.5_LDPC_sum_product_BP.md` | 缺失 | `ldpc/docs/L2_算法实现/T5.7_密度进化与译码阈值.md` | 增加 DE 作为 LDPC 收敛分析方法的入门段；用 BEC 简化递推说明阈值概念。 | 明确 DE/EXIT 不是 3GPP 协议结果。 |
| D4-02 | `T17.3_NR_LDPC_float_sim_plan.md` | 工程 | `ldpc/docs/L2_算法实现/T9.1_密度进化与EXIT图仿真.md` | 增加 DE/EXIT 仿真模板、输入参数、输出文件、随机种子或确定性网格、证据标签。 | 无真实日志时标为模板。 |
| D4-03 | `T20.2_protocol_vector_corner_case_suite.md` | 工程、缺失 | `ldpc/docs/L2_算法实现/T9.2_错误平层仿真与陷阱集搜索.md` | 补高 SNR failure dump、错误比特子图、trapping set 搜索、directed vector 生成方法。 | 增加 failure bundle schema。 |
| D5-01 | `T9.1_NR_LDPC_rate_recovery_overview.md` | 深度、协议 | `LDPC_Basics/RateMatching_Detailed.md` | 补 rate matching 的三种基本操作：puncturing、shortening、repetition；明确接收端 LLR 初始化规则。 | 增加操作到 LLR 状态映射表。 |
| D5-02 | `T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0.md` | 深度、协议 | `LDPC_Basics/RateMatching.md` | 补 `Ncb`、LBRM、`k0` 表、RV 起点和循环缓存地址空间；强调 `Ncb` 变小时 RV 覆盖区域变化。 | 必须有 NR LDPC circular buffer/RV 图。 |
| D5-03 | `T9.4_NR_LDPC_bit_deinterleaving.md` | 突出、深度 | `LDPC_Basics/RateMatching_Detailed.md` | 补 bit interleaving 与 Qm、调制 bit-channel 不均衡的关系；说明接收端 deinterleaving 错误如何污染 LLR。 | 与 T2.3 回链，必要时增加高阶 QAM bit reliability 图。 |

### NR Polar 章节

| 编号 | 当前章节 | 缺口类型 | 参考来源 | 具体补写动作 | 图表与验收 |
|:---|:---|:---|:---|:---|:---|
| E1-01 | `T10.1_NR_Polar_decoder_chain_overview.md` | 突出、协议 | `LDPC_Basics/TS38212_Rel19_Chapter5.md` | 补 Polar 在 NR 控制信道中的角色；明确 PBCH/PDCCH/UCI/PUCCH/PUSCH UCI 与 LDPC 数据链路边界。 | 增加 NR Polar 适用/不适用信道表。 |
| E1-02 | `T10.2_channel_polarization_frozen_bits.md` | 深度、图表 | `ldpc/docs/L1_理论基础/T1.3_概率与LLR基础.md` | 从 `N=2` 到 `N=4` 解释好信道/坏信道；补冻结位为什么固定、信息位为什么选可靠位置。 | 重新审查或新增极化树图，圆框大小和文字居中必须合格。 |
| E1-03 | `T10.3_NR_Polar_reliability_sequence.md` | 协议、深度 | `LDPC_Basics/TS38212_Rel19_Chapter5.md` | 补可靠性序列协议来源、信息集合、冻结集合、CRC 位插入位置；说明协议固定序列与工程实现表的关系。 | 复现必要协议子集或明确边界。 |
| E2-01 | `T10.4_Polar_SC_decoding.md` | 深度 | `ldpc/docs/L1_理论基础/T1.3_概率与LLR基础.md` | 补 SC 递归的概率意义、`f` 函数和 `g` 函数来源、partial sum 更新。 | 增加 `N=4` 手算树图。 |
| E2-02 | `T10.5_Polar_SCL_decoding.md` | 深度、工程 | `ldpc/docs/L1_理论基础/T1.3_概率与LLR基础.md` | 补 list path、path metric、split、prune、tie-breaking；解释复杂度随 list size 增长。 | 图中候选路径文字不得贴边，普通文字不全加粗。 |
| E2-03 | `T10.6_CRC_aided_SCL_control_reliability.md` | 协议、深度 | `LDPC_Basics/TS38212_Rel19_Chapter5.md` | 补 CRC-aided final selection 的协议语义；解释 CRC 通过但 path metric 较差、CRC 全失败时的选择边界。 | 增加候选选择表和失败场景。 |
| E3-01 | `T10.7_NR_Polar_rate_recovery.md` | 深度、协议 | `LDPC_Basics/TS38212_Rel19_Chapter5.md` | 补 Polar rate matching 的 puncturing、shortening、repetition 与 LLR 初始化规则；和 LDPC 的差异。 | 现有图底部边距、说明框和流程箭头必须复检。 |
| E3-02 | `T10.8_NR_Polar_decoder_edge_cases.md` | 协议、工程 | `LDPC_Basics/TS38212_Rel19_Chapter5.md` | 补 small block lengths 与 Polar coding 分支边界；列 coding scheme、CRC length、RNTI、rate recovery type 错误案例。 | 增加 edge-case decision tree。 |

### 横向比较和工程章节

| 编号 | 当前章节 | 缺口类型 | 参考来源 | 具体补写动作 | 图表与验收 |
|:---|:---|:---|:---|:---|:---|
| H1-01 | `T11.1_Turbo_LDPC_Polar_algorithm_comparison.md` | 深度、图表 | `LDPC_Basics/LDPC.md`、`ldpc/docs/L2_算法实现/T5.8_错误平层与陷阱集.md` | 加强三类码的历史、协议角色、图结构、译码算法、并行度、错误平层、硬件瓶颈对比。 | 现有比较图连线端点必须复检；表格字体不小于规则阈值。 |
| H1-02 | `T11.2_LTE_NR_rate_matching_comparison.md` | 深度、协议 | `LDPC_Basics/RateMatching_Detailed.md` | 补 LTE sub-block interleaver、NR LDPC `k0/Zc/Ncb`、Polar bit selection、LBRM、bit-channel interleaving 的对照。 | 表格与上方框图间距要足够；文本居中。 |
| H1-03 | `T11.3_HARQ_soft_buffer_comparison.md` | 深度、工程 | `LDPC_Basics/RateMatching_Detailed.md` | 补 Chase vs IR-HARQ、same-bit LLR accumulation、soft buffer key、CBG 部分重传、定点饱和。 | 必须同时覆盖 LTE 和 NR。 |
| F1-01 | `T17.2/T17.3/T17.4` | 工程 | `ldpc/docs/L2_算法实现/T9.5_仿真阶段总结报告.md` | 三类译码器都补实验矩阵、seed、输出字段、失败 dump、曲线报告、无真实结果边界。 | 运行单篇深度和 LaTeX 审计。 |
| F1-02 | `T18.1-T18.6` | 工程 | `ldpc/docs/L2_算法实现/T7.3_定点仿真与量化分析.md` | 补位宽扫描模板、clip/scale/saturation 统计、BLER 损失预算、bit-exact mismatch 定位。 | 不写真实最优位宽；所有建议标为候选。 |
| F2-01 | `T19.1-T19.5` | 工程、图表 | `ldpc/docs/L3_硬件实现/T11.1_ASIC架构概述与选择.md`、`T11.3_分层NMS译码器微架构.md` | LTE Turbo、NR LDPC、NR Polar 都补硬件瓶颈：SISO、CNU/VNU、sorter、soft buffer、banking、DMA。 | 微架构图必须逐图复检箭头和文本框。 |
| F2-02 | `T20.4_DC_synthesis_flow_decoders.md` | 工程、深度 | `ldpc/docs/L3_硬件实现/T19.2_Design_Compiler综合指南.md` | 补 DC Tcl 逐命令解释、库设置、analyze/elaborate/link、compile、report、网表/SDF/SDC 输出。 | 明确当前环境没有真实 DC 运行。 |
| F2-03 | `T20.5_timing_closure_decoder_critical_paths.md` | 工程、深度 | `ldpc/docs/L3_硬件实现/T19.5_静态时序分析STA.md` | 补 setup/hold、多角、OCV/AOCV/POCV、report 字段、cell 级关键路径模板。 | 不声称真实 STA 收敛。 |
| F2-04 | `T14/T15` 或新增专题 | 缺失、工程 | `ldpc/docs/L3_硬件实现/T19.4_低功耗设计技术.md` | 新增或扩写低功耗专题：clock gating、operand isolation、SRAM sleep、Multi-Vt、DVFS、早停功耗收益。 | 明确协议不规定低功耗实现，只约束任务时序和功能语义。 |
| F3-01 | `T20.1/T20.3/T20.6` | 缺失、工程 | `ldpc/docs/L3_硬件实现/T19.6_门级仿真与形式验证.md` | 补 gate-level simulation、SDF、glitch、X propagation、Formality、RTL-to-netlist 等价验证。 | 新增脚本模板必须标为模板。 |
| F3-02 | `T20.6_final_decoder_verification_evidence_report.md` | 突出、工程 | `ldpc/docs/L3_硬件实现/T19.7_项目总结设计报告.md` | 区分最终设计报告和最终证据报告；补摘要、设计动机、算法选择、架构、定点、验证、综合、标准符合性、后续优化结构。 | 保持真实 sign-off 状态为 hold，直到有真实证据。 |

## A. 新增少量总览/专题章节

### A1. 协议阅读地图与问题提纲

参考来源：

- `/home/yys/ClaudeCode/LDPC_Basics/LDPC_README.md`
- `/home/yys/ClaudeCode/LDPC_Basics/TS38212_Rel19_Chapter5.md`
- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T0.1_LTE_NR译码学习路线与3GPP协议导读.md`

任务：

- [x] 新增或扩写 LTE/NR 译码协议阅读地图，覆盖 TS 36.211/36.212/36.213/36.321/36.331 与 TS 38.211/38.212/38.213/38.214/38.321/38.331 的译码边界。
- [x] 增加问题提纲：CRC、TB/CB、filler、Turbo、LDPC、Polar、rate matching、HARQ、MCS/TBS、soft buffer、descriptor、验证证据分别应问什么、查哪里。
- [x] 明确 LTE Turbo、NR LDPC、NR Polar 三条主线的学习路径，避免读者把 NR LDPC 材料误认为全项目唯一重点。
- [x] 补一张 Python 或 Mermaid 总览图，展示协议源、接收端对象、译码器输入输出和审计证据之间的关系。

验收：

- [x] 新增章节或审计文档中能从任一问题定位到现有章节或待补章节。
- [x] LTE 与 NR 双侧协议路径均覆盖。
- [x] 术语、标题、深度、LaTeX 审计通过。

### A2. TS 38.212 Chapter 5 接收侧地图

参考来源：

- `/home/yys/ClaudeCode/LDPC_Basics/TS38212_Rel19_Chapter5.md`

任务：

- [x] 集中讲解 TS 38.212 Chapter 5：CRC、code block segmentation、channel coding、rate matching、code block concatenation。
- [x] 把发射侧协议步骤逐项翻译为接收侧逆流程。
- [x] 覆盖 Polar、LDPC 和 small block lengths，不只讲 LDPC。
- [x] 补协议证据表和本地路径。

验收：

- [x] T3.1/T3.4/T3.5/T8/T9/T10/T11 能回链到本地图。
- [x] small block lengths 有明确边界，不能误套 CA-SCL 或 LDPC。

### A3. TS 38.214 MCS/TBS 到译码 descriptor

参考来源：

- `/home/yys/ClaudeCode/LDPC_Basics/NR_TBS_CB_Calculation.md`
- `/home/yys/ClaudeCode/ldpc/NR_TBS_CB_Calculation.md`
- `/home/yys/ClaudeCode/ldpc/docs/审计/LDPC正式审计.md`

任务：

- [x] 新增或扩写系统级专题，讲 MCS、Qm、目标码率、PRB、RE、层数、TBS 如何影响译码器输入规模。
- [x] 复现 TS 38.214 TBS 计算链路的本节必要子集。
- [x] 用 Rel-19 最大 TB/CB 数例子说明 decoder throughput、soft buffer 和回归向量压力。
- [x] 核验 1024QAM 表号和 MCS 行，不能复制旧材料中可疑的 Table 5.1.3.1-3/MCS27 说法。

验收：

- [x] TS 38.214 表号、MCS 行和本地路径已核验。
- [x] 输出 descriptor 字段表，说明哪些字段进入 Turbo/LDPC/Polar，哪些只是系统调度元数据。

## B. 共同理论基础补齐

### B1. GF(2)、线性代数和校验矩阵深度

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T1.1_GF2有限域运算.md`
- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T1.2_编码线性代数.md`

影响章节：

- `docs/L1_基础/T1.1_GF2_binary_arithmetic_for_decoders.md`
- `docs/L1_基础/T1.3_GF2_vectors_matrices.md`
- `docs/L2_协议算法/T8.4_LDPC_Tanner_graph_message_passing.md`

任务：

- [x] T1.1 补“为什么信道编码要用 GF(2)”和多例题，但避免过早讲 LTE/LDPC。
- [x] T1.3 补生成矩阵 G、校验矩阵 H、行空间、零空间、系统形式和 `GH^T=0` 的直觉。
- [x] T1.3 补一个小型线性分组码或汉明码例子，用来承接 LDPC/Turbo/Polar 前的矩阵语言。
- [x] T8.4 补稀疏矩阵存储、edge list/CSR/CSC 与硬件访存关系。

验收：

- [x] 初学者能从 GF(2) 加法一路理解 `Hc^T=0`。
- [x] LTE/NR 协议段只作为后续桥接，不压过基础理论。

### B2. 概率、边缘化、MAP/ML 与 LLR 累加

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T1.3_概率与LLR基础.md`

影响章节：

- `docs/L1_基础/T1.4_probability_bayes_soft_decoding.md`
- `docs/L1_基础/T1.5_LLR_soft_decision.md`
- `docs/L2_协议算法/T6.5_BCJR_MAP_decoding_intuition.md`
- `docs/L2_协议算法/T8.5_LDPC_sum_product_BP.md`
- `docs/L2_协议算法/T10.4_Polar_SC_decoding.md`

任务：

- [x] T1.4 补联合概率、条件独立、边缘化和 MAP/ML 的入门解释。
- [x] T1.5 补 LLR 与概率互转、LLR 加法规则的完整推导、多观测合并例子。
- [x] T6.5/T8.5/T10.4 回链这些概率概念，避免直接写公式。

验收：

- [x] BCJR、BP、SC/SCL 中的“对未知变量求和/取最大/比较路径”有共同概率底座。

### B3. AWGN、调制、QAM 和 bit-channel 可靠性

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T1.5_数字调制BPSK_QPSK_QAM.md`
- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T1.6_AWGN信道模型与噪声特性.md`
- `/home/yys/ClaudeCode/LDPC_Basics/RateMatching_Detailed.md`

影响章节：

- `docs/L1_基础/T2.9_AWGN_noise_scaling.md`
- `docs/L1_基础/T2.13_BPSK_QPSK_soft_demapping.md`
- `docs/L1_基础/T2.14_QAM_Max_Log_MAP_demapping.md`
- `docs/L2_协议算法/T9.4_NR_LDPC_bit_deinterleaving.md`
- `docs/L2_协议算法/T11.2_LTE_NR_rate_matching_comparison.md`

任务：

- [x] T2.1 补实基带/复基带噪声方差、`N0/2`、常见 LLR scaling bug。
- [x] T2.3 补星座能量归一化、高阶 QAM 复杂度、Gray 映射和 1024QAM 边界。
- [x] T9.4/T11.2 补高阶调制 bit-channel 不均衡为什么需要 bit interleaving。

验收：

- [x] 从 Qm 到 LLR 顺序、bit interleaving 和 decoder 输入可靠性有连续解释。

### B4. 性能曲线、瀑布区、错误平层和容量差距

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T1.4_信息论与信道容量.md`
- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T5.8_错误平层与陷阱集.md`

影响章节：

- `docs/L1_基础/T1.6_information_theory_minimum_for_decoding.md`
- `docs/L1_基础/T4.5_decoder_performance_metrics.md`
- `docs/L3_工程实现/T17.5_BER_BLER_curve_reporting.md`
- `docs/L2_协议算法/T11.1_Turbo_LDPC_Polar_algorithm_comparison.md`

任务：

- [x] T1.6/T4.5 补容量、编码增益、瀑布区、错误平层区的直观曲线。
- [x] T17.5 补如何在 BLER/BER 曲线报告中标注 waterfall/error-floor 风险。
- [x] T11.1 比较 Turbo、LDPC、Polar 时加入错误平层和收敛行为差异。

验收：

- [x] 性能指标不只定义 BER/BLER，还能解释曲线形状和失败机制。

## C. LTE Turbo 主线补齐

### C1. LTE Turbo 历史、协议角色和 NR 取代原因

参考来源：

- `/home/yys/ClaudeCode/LDPC_Basics/LDPC.md`
- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T3.1_LDPC码发明与历史.md`

影响章节：

- `docs/L2_协议算法/T6.1_LTE_Turbo_decoder_chain_overview.md`
- `docs/L2_协议算法/T11.1_Turbo_LDPC_Polar_algorithm_comparison.md`

任务：

- [x] T6.1 补 Turbo 在 LTE 数据业务中的协议角色和历史位置。
- [x] T11.1 补 NR 为什么用 LDPC 承接 LTE Turbo 的数据业务位置：吞吐、并行、QC、IR-HARQ、错误平层、功耗。
- [x] 避免把“LDPC 取代 Turbo”写成绝对优劣，强调协议场景和硬件时代背景。

验收：

- [x] 读者能理解 LTE Turbo 仍是 LTE 译码主线，不是被 NR LDPC 材料覆盖掉。

### C2. BCJR/Log-MAP 理论推导加厚

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T1.3_概率与LLR基础.md`
- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T3.2_Tanner图与因子图.md`

影响章节：

- `docs/L2_协议算法/T6.5_BCJR_MAP_decoding_intuition.md`
- `docs/L2_协议算法/T6.6_Log_MAP_Max_Log_MAP_Turbo.md`
- `docs/L2_协议算法/T6.7_Turbo_iteration_extrinsic_stopping.md`

任务：

- [x] T6.5 补从路径概率、边缘化、MAP 到 alpha/beta/gamma 的逐步推导。
- [x] T6.6 补 log-domain、max-star、修正项和 Max-Log 误差来源。
- [x] T6.7 补外信息交换、相关性、振荡、早停和错误平层风险。

验收：

- [x] 不再直接从公式跳到算法；每个度量都有概率来源。

### C3. LTE rate matching、HARQ 和边界案例突出化

参考来源：

- `/home/yys/ClaudeCode/LDPC_Basics/RateMatching_Detailed.md`

影响章节：

- `docs/L2_协议算法/T7.1_LTE_Turbo_de_rate_matching_overview.md`
- `docs/L2_协议算法/T7.2_LTE_subblock_deinterleaver_circular_buffer.md`
- `docs/L2_协议算法/T7.3_LTE_HARQ_soft_buffer_RV.md`
- `docs/L2_协议算法/T7.6_LTE_Turbo_decoder_edge_cases.md`
- `docs/L2_协议算法/T11.2_LTE_NR_rate_matching_comparison.md`

任务：

- [x] T7.1/T7.2 补 LTE sub-block interleaver、circular buffer、puncturing/repetition 与 LLR 初始化的概念解释。
- [x] T7.3 保持 RV ring buffer 图，进一步补 Chase vs IR-HARQ 与 LLR 累加/饱和的理论动机。
- [x] T7.6 补错误平层、高 SNR 失败、RV mismatch 和 `<NULL>`/punctured 混淆的定位流程。
- [x] T11.2 重新强调 LTE 与 NR rate matching 的结构差异。

验收：

- [x] LTE 不只是 NR rate matching 的对照项，具备完整接收侧 rate recovery 教学闭环。

## D. NR LDPC 主线补齐

### D1. 通用 LDPC 与 NR LDPC 术语对照

参考来源：

- `/home/yys/ClaudeCode/LDPC_Basics/LDPC.md`
- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T3.3_LDPC码构造方法与分类.md`

影响章节：

- `docs/L2_协议算法/T8.1_NR_LDPC_decoder_chain_overview.md`
- `docs/L2_协议算法/T8.2_NR_LDPC_base_graph_selection.md`
- `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md`

任务：

- [x] T8.1 补“通用 LDPC 术语 vs NR LDPC 协议术语”对照表。
- [x] T8.1 明确 LDPC 在 NR 中服务 UL-SCH/DL-SCH/PCH 等数据链路，排除 DCI/BCH/UCI 等控制链路。
- [x] T8.2/T8.3 补 BG、Zc、iLS、shift value、mother code、filler、first `2Zc` puncturing 的术语关系。

验收：

- [x] 读者能分清算法概念、协议字段和工程 descriptor 字段。

### D2. BG 五子矩阵、Raptor-like 结构和校验位结构

参考来源：

- `/home/yys/ClaudeCode/LDPC_Basics/LDPC.md`

影响章节：

- `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md`
- `docs/L3_工程实现/T19.2_NR_LDPC_RTL_microarchitecture.md`

任务：

- [x] T8.3 补 BG1/BG2 五子矩阵 A/B/C/D/E 的结构角色。
- [x] 解释核心 parity、扩展 parity、双对角/近似双对角结构和 Raptor-like 扩展的意义。
- [x] 说明这些结构为什么影响编码端、接收端 H 构造、IR-HARQ、layered schedule 和 memory layout。
- [x] 新增 Python 图，展示 BG 子矩阵区域、QC lifting 和接收端使用位置。

验收：

- [x] 五子矩阵不只是名词，要能读图理解“每一块为什么存在”。

### D3. BP、Min-Sum、Layered 的理论与收敛分析

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T5.1_消息传递算法概述.md`
- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T5.2_BP算法概率域推导.md`
- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T5.3_BP算法对数域推导.md`
- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T5.4_最小和与改进变体.md`
- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T5.5_调度策略洪泛与分层.md`

影响章节：

- `docs/L2_协议算法/T8.4_LDPC_Tanner_graph_message_passing.md`
- `docs/L2_协议算法/T8.5_LDPC_sum_product_BP.md`
- `docs/L2_协议算法/T8.6_LDPC_MS_NMS_OMS.md`
- `docs/L2_协议算法/T8.7_layered_LDPC_decoding_schedule.md`

任务：

- [x] T8.4 补 cycle、girth、短环导致消息相关性。
- [x] T8.5 补概率域 BP、边缘化、因子图消息的逐步推导。
- [x] T8.5 补 LLR 域 check node 和 variable node 更新的来源。
- [x] T8.6 补 MS/NMS/OMS 近似误差、alpha/beta 参数、陷阱集和 error floor 风险。
- [x] T8.7 补 flooding/layered/shuffled 对比、收敛速度和存储冲突。

验收：

- [x] LDPC 算法不再是公式列表，而是从概率推导到硬件调度的连续链。

### D4. 密度进化、EXIT、错误平层和陷阱集

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T5.7_密度进化与译码阈值.md`
- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T5.8_错误平层与陷阱集.md`
- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T9.1_密度进化与EXIT图仿真.md`
- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T9.2_错误平层仿真与陷阱集搜索.md`

影响章节：

- `docs/L2_协议算法/T8.5_LDPC_sum_product_BP.md`
- `docs/L2_协议算法/T8.7_layered_LDPC_decoding_schedule.md`
- `docs/L2_协议算法/T8.8_NR_LDPC_decoder_numeric_walkthrough.md`
- `docs/L3_工程实现/T17.3_NR_LDPC_float_sim_plan.md`
- `docs/L3_工程实现/T20.2_protocol_vector_corner_case_suite.md`

任务：

- [x] 增加 DE/EXIT 作为分析方法的教学，不写成 3GPP 协议结果。
- [x] 补 BEC 简化 DE 递推例子，说明 threshold 和收敛含义。
- [x] 补 trapping set/absorbing set 定义和高 SNR 失败机制。
- [x] T20.2 补高 SNR failure dump、错误子图分析和 directed vector 构造。

验收：

- [x] 明确 3GPP 定义 BG/shift 表，不定义 DE/EXIT 阈值；没有本项目仿真日志时不能声称性能结论。

### D5. NR LDPC rate matching、LBRM 与 IR-HARQ

参考来源：

- `/home/yys/ClaudeCode/LDPC_Basics/RateMatching.md`
- `/home/yys/ClaudeCode/LDPC_Basics/RateMatching_Detailed.md`

影响章节：

- `docs/L2_协议算法/T9.1_NR_LDPC_rate_recovery_overview.md`
- `docs/L2_协议算法/T9.2_NR_LDPC_circular_buffer_states.md`
- `docs/L2_协议算法/T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0.md`
- `docs/L2_协议算法/T9.4_NR_LDPC_bit_deinterleaving.md`
- `docs/L2_协议算法/T11.2_LTE_NR_rate_matching_comparison.md`
- `docs/L3_工程实现/T19.5_soft_buffer_HARQ_memory_architecture.md`

任务：

- [x] T9.1 补 mother code、puncturing、shortening、repetition 的理论解释。
- [x] T9.1/T9.3 补 LBRM 的缓存封顶含义和 `Ncb` 对 RV 地址空间的影响。
- [x] T9.3 补 IR-HARQ vs Chase Combining 的概率证据差异。
- [x] T9.4 补 bit interleaving 与高阶调制 bit-channel 不均衡。
- [x] 增加完整 Python RM/de-RM roundtrip 小工具或片段。

验收：

- [x] 读者能从 `E_r/N_cb/k0/Qm` 推到接收端 LLR 初始化、合并和饱和。

## E. NR Polar 主线补齐

### E1. Polar 理论深度与协议角色

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T0.1_LTE_NR译码学习路线与3GPP协议导读.md`
- `/home/yys/ClaudeCode/LDPC_Basics/TS38212_Rel19_Chapter5.md`

影响章节：

- `docs/L1_基础/T3.5_NR_Polar_segmentation_crc.md`
- `docs/L2_协议算法/T10.1_NR_Polar_decoder_chain_overview.md`
- `docs/L2_协议算法/T10.2_channel_polarization_frozen_bits.md`
- `docs/L2_协议算法/T10.3_NR_Polar_reliability_sequence.md`

任务：

- [x] T10.1 补 Polar 在 NR 控制信道中的协议角色，明确和 LDPC 数据链路的边界。
- [x] T10.2 补更厚的 channel polarization 理论，从 `N=2` 到 `N=4`，解释好信道/坏信道。
- [x] T10.3 补可靠性序列的协议来源、信息位/冻结位/CRC 位关系。
- [x] 补图，避免只用公式描述极化树和冻结 mask。

验收：

- [x] NR Polar 不再显得比 LDPC 粗略；控制信道链路讲清上下游。

### E2. SC/SCL/CA-SCL 推导和路径度量

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L1_理论基础/T1.3_概率与LLR基础.md`

影响章节：

- `docs/L2_协议算法/T10.4_Polar_SC_decoding.md`
- `docs/L2_协议算法/T10.5_Polar_SCL_decoding.md`
- `docs/L2_协议算法/T10.6_CRC_aided_SCL_control_reliability.md`
- `docs/L3_工程实现/T18.4_NR_Polar_fixed_point_model_plan.md`
- `docs/L3_工程实现/T19.3_NR_Polar_RTL_microarchitecture.md`

任务：

- [x] T10.4 补 SC 的递归概率意义、`f/g` 函数推导和 partial sum。
- [x] T10.5 补 SCL list path、path metric 更新、排序剪枝。
- [x] T10.6 补 CRC-aided final selection 的概率与协议语义。
- [x] T18.4/T19.3 补 path metric 饱和、排序器、lazy copy 和 RTL 瓶颈。

验收：

- [x] Polar 译码从理论到 CA-SCL 工程实现有连续推导。

### E3. Polar rate recovery、small block 与边界案例

参考来源：

- `/home/yys/ClaudeCode/LDPC_Basics/TS38212_Rel19_Chapter5.md`

影响章节：

- `docs/L2_协议算法/T10.7_NR_Polar_rate_recovery.md`
- `docs/L2_协议算法/T10.8_NR_Polar_decoder_edge_cases.md`
- `docs/L2_协议算法/T11.2_LTE_NR_rate_matching_comparison.md`

任务：

- [x] T10.7 补 Polar puncturing/shortening/repetition 与 LLR 初始化规则。
- [x] T10.8 补 small block lengths 分支与 Polar coding 分支的协议边界。
- [x] T11.2 补 Polar rate matching 与 LTE Turbo、NR LDPC 的差异。

验收：

- [x] small block 不被误写成 Polar CA-SCL 普通分支。

## F. L3 工程与 sign-off 方法补齐

### F1. 定点、仿真和 bit-exact 证据加厚

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T7.3_定点仿真与量化分析.md`
- `/home/yys/ClaudeCode/ldpc/docs/L2_算法实现/T9.5_仿真阶段总结报告.md`

影响章节：

- `docs/L3_工程实现/T17.2_LTE_Turbo_float_sim_plan.md`
- `docs/L3_工程实现/T17.3_NR_LDPC_float_sim_plan.md`
- `docs/L3_工程实现/T17.4_NR_Polar_float_sim_plan.md`
- `docs/L3_工程实现/T18.1_fixed_point_decoder_requirements.md`
- `docs/L3_工程实现/T18.2_LTE_Turbo_fixed_point_model_plan.md`
- `docs/L3_工程实现/T18.3_NR_LDPC_fixed_point_model_plan.md`
- `docs/L3_工程实现/T18.4_NR_Polar_fixed_point_model_plan.md`
- `docs/L3_工程实现/T18.6_bit_exact_regression_harness.md`

任务：

- [x] 增加 LTE/NR 三类译码器的实验矩阵、输出字段、随机种子、失败 dump 和验收阈值。
- [x] 补定点位宽扫描、clip/scale/saturation 统计、BLER 损失预算格式。
- [x] 明确没有真实仿真结果时只写模板，不写推荐最优位宽。

验收：

- [x] 每个工程结果都有“真实证据/模板/待生成”标签。

### F2. RTL/ASIC、DC、STA、PPA 和低功耗补齐

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L3_硬件实现/T19.2_Design_Compiler综合指南.md`
- `/home/yys/ClaudeCode/ldpc/docs/L3_硬件实现/T19.3_综合结果与PPA优化.md`
- `/home/yys/ClaudeCode/ldpc/docs/L3_硬件实现/T19.4_低功耗设计技术.md`
- `/home/yys/ClaudeCode/ldpc/docs/L3_硬件实现/T19.5_静态时序分析STA.md`

影响章节：

- `docs/L3_工程实现/T19.1_LTE_Turbo_RTL_microarchitecture.md`
- `docs/L3_工程实现/T19.2_NR_LDPC_RTL_microarchitecture.md`
- `docs/L3_工程实现/T19.3_NR_Polar_RTL_microarchitecture.md`
- `docs/L3_工程实现/T19.4_unified_decoder_subsystem_architecture.md`
- `docs/L3_工程实现/T19.5_soft_buffer_HARQ_memory_architecture.md`
- `docs/L3_工程实现/T20.4_DC_synthesis_flow_decoders.md`
- `docs/L3_工程实现/T20.5_timing_closure_decoder_critical_paths.md`

任务：

- [x] T20.4 补 DC Tcl 逐命令解释、库、analyze/elaborate/link、compile、报告生成。
- [x] T20.5 补 setup/hold、多角、OCV/AOCV/POCV、timing report 字段和 cell 级路径模板。
- [x] 新增或扩写 PPA 优化矩阵：CNU、sorter、SISO、memory、barrel shifter、banking、clock gating。
- [x] 新增或扩写低功耗设计：clock gating、operand isolation、SRAM sleep、Multi-Vt、DVFS、早停功耗。
- [x] 明确所有 PPA/功耗都是方法或模板，非真实签核。

验收：

- [x] 不把真实工具未运行的内容写成“通过”。
- [x] LTE Turbo、NR LDPC、NR Polar 都有对应硬件瓶颈，而不是只讲 LDPC。

### F3. 门级仿真、Formality 和最终设计报告

参考来源：

- `/home/yys/ClaudeCode/ldpc/docs/L3_硬件实现/T19.6_门级仿真与形式验证.md`
- `/home/yys/ClaudeCode/ldpc/docs/L3_硬件实现/T19.7_项目总结设计报告.md`

影响章节：

- `docs/L3_工程实现/T20.1_decoder_testbench_architecture.md`
- `docs/L3_工程实现/T20.3_coverage_regression_strategy.md`
- `docs/L3_工程实现/T20.4_DC_synthesis_flow_decoders.md`
- `docs/L3_工程实现/T20.6_final_decoder_verification_evidence_report.md`

任务：

- [x] 补 gate-level simulation、SDF back-annotation、glitch、X propagation、timing check 的教学模板。
- [x] 补 Formality/等价验证的流程、脚本骨架和失败分类。
- [x] T20.6 补最终设计报告和最终证据报告的区别。

验收：

- [x] 最终交付不只像审计表，也能作为设计报告骨架；但 sign-off 状态仍需真实证据。

## G. 全项目图表和审计补齐

任务：

- [x] 对新增或扩写后所有难理解主题补 Python 图：协议地图、TBS/CB 压力、BG 五子矩阵、DE/EXIT 曲线、trapping set、IR-HARQ ring/circular buffer、Polar tree/list pruning、PPA/STA 路径。
- [x] 所有图运行几何和可读性审计，并逐图目检四项：字体与上下边框距离、相邻边框间距、箭头是否正常、连线起止位置是否合理。
- [x] 更新 `docs/audits/image_asset_inventory.md`。
- [x] 更新 `docs/audits/prompt_coverage_matrix.md`、`docs/audits/full_project_document_review.md`、`docs/audits/global_compliance_review.md`。

验收命令：

```bash
python3 tools/audit_lesson_terms.py docs/L1_基础/T*.md docs/L2_协议算法/T*.md docs/L3_工程实现/T*.md
python3 tools/audit_markdown_headings.py docs/L1_基础/T*.md docs/L2_协议算法/T*.md docs/L3_工程实现/T*.md
python3 tools/audit_lesson_depth.py --strict docs/L1_基础/T*.md docs/L2_协议算法/T*.md docs/L3_工程实现/T*.md
python3 tools/audit_latex_render.py docs/L1_基础/T*.md docs/L2_协议算法/T*.md docs/L3_工程实现/T*.md
python3 tools/audit_figure_geometry.py tools/figures
python3 tools/audit_figure_readability.py tools/figures
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/audit_figure_geometry.py tools/audit_figure_readability.py tests/test_audit_figure_geometry.py tools/figures/*.py
python3 -m unittest tests/test_audit_figure_geometry.py
```

## 完成记录

| 日期 | 项目 | 证据 |
|:---|:---|:---|
| 2026-06-21 | 建立 LTE/NR 深度缺口专项台账 | 新增 `docs/audits/lte_nr_depth_gap_backlog.md`；依据 `/home/yys/ClaudeCode/ldpc` 与 `/home/yys/ClaudeCode/LDPC_Basics` 的对比，将缺失、深度不足、突出不足、协议精读不足、图表不足和工程闭环不足拆为 A-G 七类任务；同步在 `合规与遵从.md` 增加 LTE/NR 双侧深度补齐规则。 |
| 2026-06-21 | D1-D5 NR LDPC 主线补齐 | 修改 `docs/L2_协议算法/T8.1_NR_LDPC_decoder_chain_overview.md`、`docs/L2_协议算法/T8.2_NR_LDPC_base_graph_selection.md`、`docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md`、`docs/L2_协议算法/T8.4_LDPC_Tanner_graph_message_passing.md`、`docs/L2_协议算法/T8.5_LDPC_sum_product_BP.md`、`docs/L2_协议算法/T8.6_LDPC_MS_NMS_OMS.md`、`docs/L2_协议算法/T8.7_layered_LDPC_decoding_schedule.md`、`docs/L2_协议算法/T9.1_NR_LDPC_rate_recovery_overview.md`、`docs/L2_协议算法/T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0.md`、`docs/L2_协议算法/T9.4_NR_LDPC_bit_deinterleaving.md`、`docs/L3_工程实现/T20.2_protocol_vector_corner_case_suite.md`；新增/更新 `tools/figures/render_nr_ldpc_lifting_qc_matrix.py` 输出 `docs/L2_协议算法/assets/T8.3_NR_LDPC_BG_regions_QC_receiver.png`。覆盖 D1 术语和数据/控制链路边界，D2 BG 五区和 Raptor-like/QC 图，D3 BP/MS/layered 理论链，D4 DE/EXIT/BEC 和高 SNR failure dump，D5 mother code/LBRM/IR-HARQ/bit-channel/RM-deRM toy。D2/D4/D5 原影响章节中 `docs/L3_工程实现/T19.2_NR_LDPC_RTL_microarchitecture.md`、`docs/L2_协议算法/T8.8_NR_LDPC_decoder_numeric_walkthrough.md`、`docs/L3_工程实现/T17.3_NR_LDPC_float_sim_plan.md`、`docs/L2_协议算法/T9.2_NR_LDPC_circular_buffer_states.md`、`docs/L2_协议算法/T11.2_LTE_NR_rate_matching_comparison.md`、`docs/L3_工程实现/T19.5_soft_buffer_HARQ_memory_architecture.md` 不在本轮用户负责文件范围内，未修改；本轮只在允许文件中补协议/算法/工程边界和 T20.2 failure schema。图片审计：`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`；最终文档审计输出见本轮执行日志。 |
| 2026-06-21 | B 批次共同理论基础补齐 | 完成 B1-B4 中本批负责文件：`T1.1` 补信道编码需要 GF(2) 的二元约束动机；`T1.3` 补 G/H、行空间/零空间、系统形式、`GH^T=0` 与小型线性分组码闭环；`T1.4`/`T1.5` 补联合概率、条件独立、边缘化、MAP/ML、LLR 概率互转、LLR 加法和多观测合并；`T2.1`/`T2.3` 补实/复 AWGN 方差、`N0/2`、LLR scaling 诊断、QAM 能量归一化、Gray 映射、1024QAM 边界和 bit-channel 可靠性；`T1.6`/`T4.5`/`T17.5`/`T11.1` 补容量差距、编码增益、瀑布区、错误平层、统计成本和失败机制；`T6.5`/`T8.5`/`T10.4` 加概率底座回链。未修改未授权的 `T8.4`、`T9.4`、`T11.2`，因此其专属细项仍留给对应负责人。 |
| 2026-06-21 | F1 L3 仿真/定点工程模板补齐 | 核对并保留 `docs/L3_工程实现/T17.2_LTE_Turbo_float_sim_plan.md`、`T17.3_NR_LDPC_float_sim_plan.md`、`T17.4_NR_Polar_float_sim_plan.md` 的实验矩阵、输出字段、分层 seed、失败 dump/replay 和验收阈值；核对 `T18.1-T18.4` 的位宽扫描、clip/scale/saturation 统计、BLER 损失预算和 bit-exact mismatch 模板；所有章节均明确当前无真实 campaign 或最优位宽，只能作为模板/待生成证据。文档审计输出：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=587`。 |
| 2026-06-21 | F2 DC/STA/PPA/低功耗方法补齐 | 扩写 `docs/L3_工程实现/T20.4_DC_synthesis_flow_decoders.md`：新增 DC Tcl 逐命令解释、report/write 输出边界、PPA 优化矩阵覆盖 CNU、sorter、SISO、memory、barrel shifter、banking、clock gating，并补 clock gating、operand isolation、SRAM sleep、Multi-Vt、DVFS、早停功耗模板；扩写 `docs/L3_工程实现/T20.5_timing_closure_decoder_critical_paths.md`：新增 setup/hold、多角、OCV/AOCV/POCV、timing report 字段和 cell 级路径模板。明确当前无真实 DC/STA/PPA/功耗签核。 |
| 2026-06-21 | F3 gate-level/Formality/最终报告边界补齐 | 扩写 `docs/L3_工程实现/T20.6_final_decoder_verification_evidence_report.md`：新增最终设计报告与最终证据报告区分、gate-level simulation、SDF back-annotation、glitch、X propagation、timing check、Formality/等价验证流程、脚本骨架和失败分类；sign-off 状态继续保持 `hold`，直到真实 BLER、定点、RTL、coverage、DC/STA、gate/formal 证据生成。 |
| 2026-06-21 | G 点名图片风险复核与库存更新 | 重生成 `docs/L3_工程实现/assets/T17.1_golden_model_project_layout.png`、`T17.2_LTE_Turbo_float_sim_flow.png`、`T17.3_NR_LDPC_float_sim_flow.png`、`T17.4_NR_Polar_float_sim_flow.png`、`T17.5_BER_BLER_curve_reporting.png`、`T18.1_fixed_point_decoder_requirements.png`、`T18.2_LTE_Turbo_fixed_point_model.png`、`T18.3_NR_LDPC_fixed_point_model.png`、`T18.4_NR_Polar_fixed_point_model.png`、`T18.5_SIMD_memory_layout_decoders.png`、`T18.6_bit_exact_regression_harness.png`、`T19.4_unified_decoder_subsystem_architecture.png`，以及 `docs/L2_协议算法/assets/T10.4_NR_Polar_SC_N4_tree.png`、`T11.3_HARQ_soft_buffer_comparison.png`、`T11.5_decoder_selection_by_channel_type.png`、`T7.3_LTE_HARQ_RV_windows.png`；更新 `docs/audits/image_asset_inventory.md`，修正 T17.5 axis font 与 LTE HARQ ring index 均已为 24px。图形审计输出：相关脚本 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`；`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile ...` 对相关脚本无输出且退出码 0。 |
| 2026-06-21 | C1-C3 LTE Turbo 主线补齐 | 修改 `docs/L2_协议算法/T6.1_LTE_Turbo_decoder_chain_overview.md`、`docs/L2_协议算法/T6.5_BCJR_MAP_decoding_intuition.md`、`docs/L2_协议算法/T6.6_Log_MAP_Max_Log_MAP_Turbo.md`、`docs/L2_协议算法/T6.7_Turbo_iteration_extrinsic_stopping.md`、`docs/L2_协议算法/T7.1_LTE_Turbo_de_rate_matching_overview.md`、`docs/L2_协议算法/T7.2_LTE_subblock_deinterleaver_circular_buffer.md`、`docs/L2_协议算法/T7.3_LTE_HARQ_soft_buffer_RV.md`、`docs/L2_协议算法/T7.6_LTE_Turbo_decoder_edge_cases.md`、`docs/L2_协议算法/T11.1_Turbo_LDPC_Polar_algorithm_comparison.md`、`docs/L2_协议算法/T11.2_LTE_NR_rate_matching_comparison.md`；覆盖 C1 历史/协议角色/NR 取代原因、C2 BCJR/Log-MAP/外信息理论链、C3 LTE rate recovery/HARQ/边界案例。协议证据使用本地 TS 36.212 `3GPP_Rel19/processed/TS_36.212_36212-j30`、TS 38.212 `3GPP_Rel19/processed/TS_38.212_38212-j30` 及既有 TS 36.213/36.321 HARQ/MAC 锚点；完成后按用户指定运行术语、标题、深度和 LaTeX 审计。 |
| 2026-06-21 | E1-E3 NR Polar 主线补齐 | 覆盖 `docs/L2_协议算法/T10.1_NR_Polar_decoder_chain_overview.md`、`docs/L2_协议算法/T10.2_channel_polarization_frozen_bits.md`、`docs/L2_协议算法/T10.3_NR_Polar_reliability_sequence.md`、`docs/L2_协议算法/T10.4_Polar_SC_decoding.md`、`docs/L2_协议算法/T10.5_Polar_SCL_decoding.md`、`docs/L2_协议算法/T10.6_CRC_aided_SCL_control_reliability.md`、`docs/L2_协议算法/T10.7_NR_Polar_rate_recovery.md`、`docs/L2_协议算法/T10.8_NR_Polar_decoder_edge_cases.md`、`docs/L2_协议算法/T11.2_LTE_NR_rate_matching_comparison.md`、`docs/L3_工程实现/T18.4_NR_Polar_fixed_point_model_plan.md`、`docs/L3_工程实现/T19.3_NR_Polar_RTL_microarchitecture.md`。补齐控制信道角色与 LDPC 数据链路边界、`N=2` 到 `N=4` 极化解释、可靠性序列与 CRC/information/frozen 关系、SC/SCL/CA-SCL 推导、Polar rate recovery、small block 边界、PM 饱和、sorter、lazy copy 和 RTL 瓶颈；本轮重新运行术语、标题、深度和 LaTeX 审计。 |
| 2026-06-21 | A1-A3 协议地图和系统级 descriptor 入口补齐 | 新增 `docs/L1_基础/T0.1_LTE_NR_decoder_protocol_reading_map.md`、`docs/L2_协议算法/T8.0_TS38212_chapter5_decoder_side_map.md`、`docs/L2_协议算法/T9.0_TS38214_MCS_TBS_decoder_descriptor.md`；新增图片 `docs/L1_基础/assets/T0.1_LTE_NR_decoder_protocol_reading_map.png` 和脚本 `tools/figures/render_t0_1_lte_nr_decoder_protocol_map.py`。覆盖 LTE/NR 双侧协议阅读地图、CRC/TB/CB/filler/Turbo/LDPC/Polar/rate matching/HARQ/MCS/TBS/soft buffer/descriptor/验证证据问题提纲、TS 38.212 Chapter 5 接收侧逆流程、small block 边界、TS 38.214 MCS/TBS 到 decoder descriptor、1024QAM Table 5.1.3.1-4 核验和 descriptor 字段分类。审计输出：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=81`；图片审计输出：`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`。 |
| 2026-06-21 | B/D 交界遗留项补齐 | 扩写 `docs/L2_协议算法/T8.4_LDPC_Tanner_graph_message_passing.md`，新增稀疏矩阵存储、edge list、CSR、CSC、QC-LDPC `Zc` 局部地址和 bank conflict 关系；扩写 `docs/L2_协议算法/T11.2_LTE_NR_rate_matching_comparison.md`，补高阶 QAM bit-channel 不均衡与 NR LDPC `Qm` bit deinterleaving 的横向对比，并回链 `docs/L2_协议算法/T9.4_NR_LDPC_bit_deinterleaving.md`。同步修正 T8.4 公式编号顺序。审计输出：`LESSON_TERM_AUDIT_OK`、`MARKDOWN_HEADING_AUDIT_OK`、`LESSON_DEPTH_AUDIT_OK`、`LATEX_RENDER_AUDIT_OK formulas=400`。 |
| 2026-06-21 | Depth backlog 全部任务关闭 | A-G 批次全部完成并回写。当前实物计数：`find docs/L1_基础 docs/L2_协议算法 docs/L3_工程实现 -maxdepth 1 -name 'T*.md' | wc -l` -> `94`，其中 L1 `28`、L2 `43`、L3 `23`；`find docs/L1_基础/assets docs/L2_协议算法/assets docs/L3_工程实现/assets -name '*.png' | wc -l` -> `61`；`find tools/figures -maxdepth 1 -name '*.py' | wc -l` -> `56`。G 项中难理解主题已有 Python 图或正文内图表承接：协议地图 `T0.1`，BG/QC 图 `T8.3`，IR-HARQ/RV/circular buffer `T7.3/T9.3`，Polar tree/list pruning `T10.2/T10.4/T10.5`，PPA/STA 路径 `T20.4/T20.5`，DE/EXIT/trapping set 在 `T8.5/T17.3/T20.2` 以方法/模板和 failure schema 承接，未伪造真实仿真结果。全项目审计：术语 `LESSON_TERM_AUDIT_OK`，标题 `MARKDOWN_HEADING_AUDIT_OK`，深度 `LESSON_DEPTH_AUDIT_OK`，LaTeX 分段全检通过：L1 `2036`、L2 `3444`、L3 `948`，合计 `6428`；图片几何/可读性 `FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`；脚本 py_compile 退出码 0；`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 13 tests OK`；引用重建候选刷新为 `1320` 行，候选不是硬失败。 |
| 2026-06-21 | 继续收尾：覆盖矩阵和图片资产清单一致性复核 | 复核 `docs/audits/prompt_coverage_matrix.md` 覆盖当前 94 个 `docs/L1_基础/L2/L3/T*.md` 文件：`comm -23` 无缺失；反向多出的 21 项均为矩阵摘要中的通配符模式，不是具体讲义。当日图片清单仍采用后续已更正的旧计数口径；再次运行图片审计和脚本测试：`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`，py_compile 退出码 0，`python3 -m unittest tests/test_audit_figure_geometry.py` -> `Ran 13 tests OK`。 |
| 2026-06-22 | 图片资产计数和一致性审计口径更正 | 后续 T8.3/T8.8 分片正文图暴露 2026-06-21 的 61/56 口径已过时。当前实物为 68 张 PNG、58 个 Python 文件（57 个 `render_*.py` 绘图脚本和 1 个 helper），正文 PNG 引用为 66 个、唯一正文引用 PNG 为 65 个，另有 3 个完整拼接/兼容图作为 evidence/compatibility 保留。新增 `tools/audit_project_image_inventory.py` 后输出 `PROJECT_IMAGE_INVENTORY_AUDIT_OK`，用于防止资产目录、正文引用、资产清单和迁移台账再次脱节；该审计不替代 68 张 PNG 原尺寸逐图目检。 |
