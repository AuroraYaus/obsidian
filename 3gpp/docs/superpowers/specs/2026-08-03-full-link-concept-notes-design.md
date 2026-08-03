# 2026-08-03 全链路缺口概念笔记设计

## 背景

`3GPP全流程_缩写概念理论清单.md` 已依据 `3GPP_FULL_LINK/`（evaluation-link-simulator 代码 + reproduction_output 8 份分析 + 5 份 deep_dive）交叉复核补齐（2026-08-03，缩写 +9、概念 +27、理论 +18）。

本计划把清单中"概念层"缺口落为知识库概念笔记（`docs/concepts/`），为后续 L1/L2/L3 讲义创作打底。

## 范围

**6 篇新笔记 + 3 篇增强**，全部沿用项目概念笔记约定（六段式模板、`English_中文` 命名、frontmatter type/aliases/tags/source_spec）。

### 新笔记（6 篇）

| 笔记 | 核心定义锚点 | 直观模型方向 | 协议锚点 | 来源 |
|---|---|---|---|---|
| `Timing_Sync_定时同步` | 仿真 nrPerfectTimingEstimate（理想）vs 实际 PSS/SSS 或 CP 相关滑动窗 O(Nfft×Ncp)；定时误差折算进估计误差 | "对表" | TS 38.211 §7.4.2（PSS/SSS） | PHY01 §1.5、analysis 02 §2.2 |
| `Coherence_Bandwidth_Time_相干带宽与时间` | B_c≈1/(2πτ_rms)≈530 kHz ≫ 30 kHz SCS（子载波内平坦）；T_c≈0.423/f_d≈14.1 ms ≫ 0.5 ms 时隙（准静态）；30 Hz @3.5 GHz=9.3 km/h | "地形起伏尺度" | TR 38.901（TDL 参数） | PHY01 §5.2 |
| `Detector_Comparison_检测器对比` | ZF/MF/MMSE/Sphere：公式、复杂度（MMSE 4×4 ~100 MACs/tone vs Sphere ~100-1000）、性能损失（MMSE 1-3 dB vs Sphere 0 dB）、面积（~95K vs ~150K gates）、适用域（Sphere 仅高 SNR） | "四种听法" | 接收机自由度（非协议规定） | MIMO01 §5-6、analysis 03 §3 |
| `Diversity_Combining_分集与合并` | MRC 分集阶数（‖h‖²/σ²~χ²₆₄、P~ε³²/32!、32 天线 ≈+15 dB）；MMSE 单层 = 正则化 MRC（深衰落避免除零）；SIMO 1×N | "多份拷贝投票" | 接收机自由度 | MIMO01 §3.2-3.3 |
| `MCS_Table_Effective_Code_Rate_MCS表与有效码率` | 4 张 MCS 表（qam64 0-28 / qam256 0-31（28-31 保留）/ ps_mcs_table1/2 5-27）；5 列结构 [MCS,SE,Qm,R×1024,ν_MB]；PS 表 SE ≠ Qm·R/1024（整形压缩信息速率）；R_eff=payloadTBS/(N_RE·Qm) | "菜单 vs 实付" | TS 38.214 §5.1.3 | SIM01 §4、PHY01 §6 |
| `Geometric_Shaping_几何整形` | PS vs GS 对照：改使用概率 vs 改星座点位置；GS 需协商新星座表（标准流程难兼容）；DVB-S2X 商用先例（CCDM+MB）；Rel-19 无实证 | "改走法 vs 改路" | 非 3GPP 标准 | PS01 §1.2/§1.4 |

### 增强（3 篇，只补缺失内容，不重构存量）

| 笔记 | 补充内容 |
|---|---|
| `Channel_Estimation_信道估计` | 科学定义补：维纳滤波公式 Ĥ=R_HH(R_HH+σ²I)⁻¹Ĥ_LS（低 SNR 显著优、O(N³)）；估计误差三途径（均衡偏置/CSI 失真/噪声方差失配，256QAM 偏移 0.08 翻转）；DMRS 走预编码→DMRS-based 估计直接给 H_eff |
| `LLR_Quantization_LLR量化` | 整篇重建为六段式（现为旧式要点格式）；保留现有均匀/非均匀量化/裁剪/位宽内容；补 LLR 动态范围（1024QAM max\|y−x\|²≈11.2、SNR 30 dB → LLR_max≈11200 需 14-bit）；裁剪-损失表（±7 4-bit <0.1 / ±15 5-bit <0.05 / ±31 6-bit <0.02 / ±63 <0.01 dB）；±31 吸收 MMSE 归一化放大 |
| `Probabilistic_Shaping_概率整形` | 科学定义补：四个接入点架构（TB 构造/加扰/解调前/LDPC 解码后，NR spine 全复用）；PS 几何可行性条件（numParityBits ≤ 2N_s(Qm/2−k)−L_cb；2Zc+2kN_s ≤ K−F−L_cb） |

## 入口文件与图谱整合

`概念图谱入口.md` 挂载：
- 信道与接收链路 +4：[[Timing_Sync_定时同步]]、[[Coherence_Bandwidth_Time_相干带宽与时间]]、[[Detector_Comparison_检测器对比]]、[[Diversity_Combining_分集与合并]]
- 协议结构 +1：[[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]
- 概率整形 +1：[[Geometric_Shaping_几何整形]]

每篇笔记 图谱关联 含 [[概念图谱入口]] + 上下游笔记（双向可追溯）。

## 规范与合规

- 模板：独立解释任务 → 科学定义 → 直观模型 → 常见误解 → 协议锚点 → 图谱关联
- 命名：`English_中文`（标题 `# English 中文`）
- 合规红线：Rule 10（英文术语首现"中文（English）"）、Rule 16（标题口语化禁止）、Rule 20（LaTeX 可渲染）、Rule 8（零基础保护——直观模型用生活类比）
- 来源可溯：协议锚点引用 TS 小节号 + 本地 `3GPP_Rel19/processed/` 锚点；非标准项显式标注"非 3GPP 标准"

## 验收标准

1. 9 篇全部按六段式模板完成（LLR_Quantization 重建后六段式完整）
2. 无死链：写后 grep 校验全部 [[链接]] 有对应文件
3. 入口文件三处章节更新完成
4. 风格抽查与存量笔记一致（对照 Channel_Estimation / LDPC 模板）
5. git 提交

## 不在范围（后续计划）

- L1/L2 讲义（MIMO 接收机与检测器系列、概率整形算法系列）——A 级理论项（ν̃ 归一化、完整平方 MAP 度量、衰落增益机制、功率节省公式等）
- L3 工程讲义（周期预算/面积/裁剪权衡）
