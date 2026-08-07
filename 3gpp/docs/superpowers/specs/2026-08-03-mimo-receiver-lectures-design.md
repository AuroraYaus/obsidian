# 2026-08-03 MIMO 接收机与检测器讲义系列设计

## 背景

概念层缺口已补齐（6 新 + 3 增强，spec `2026-08-03-full-link-concept-notes-design.md`，已实施完成）。本计划把 MIMO 接收侧的 A 级理论缺口（MMSE 推导、ZF/MF 极限、MRC 分集阶数、LS/维纳滤波估计、球面检测）落为 L2 讲义系列，素材底座为概念笔记（Detector_Comparison、Diversity_Combining、Channel_Estimation、MMSE_均衡、Sphere_Decoding、CSI_SINR、MIMO_多天线系统）+ `3GPP全流程_缩写概念理论清单.md` 理论清单 + 外部语料（`3GPP_FULL_LINK/reproduction_output/deep_dive/` MIMO01/PHY01/PS02）。

## 范围

**5 篇 L2 讲义**（L2 新增模块 M12，编号 T12.1-T12.5，T12 系列编号空闲）。每篇 **500-800 行**（内容广深度要求：学习目标 bullets、多视角展开——数学推导/协议锚点/工程代价/生活类比、数值实例与表格、1 个内嵌 numpy 验证代码块、**至少 1 个 SVG 图**）。定时同步/相干带宽时间不做独立篇目（L1 T2.x + 概念笔记已覆盖），在 T12.1 衔接说明。

### 篇目与内容锚点

| 篇目（文件名） | 核心内容锚点 | 内嵌 Python 验证示例 | 素材来源 |
|---|---|---|---|
| `T12.1_mimo_receiver_chain_overview.md` MIMO 接收链路总览 | 每 RE 模型 y=H·P·x+n（H∈C^{Nrx×Ntx}、x∈C^{Nlayers}、n~CN(0,σ²I)）；层域等效信道 H_eff=H·P；发射功率归一化 E‖Px‖²=‖P‖_F²E_s、‖P‖_F=1 时天线域总功率恒等；单码字 ≤4 层（TS 38.211 §7.3.1.3）；transpose vs ctranspose 约定；接收机 RE 网格→LLR 向量流程；译码器对 RE 网格不可见（衔接 T2.6） | 预编码器构造（DFT/Hadamard/Identity）+ Frobenius 归一化后天线域功率守恒数值验证 | MIMO01 §1-2；概念笔记 MIMO_多天线系统、Detector_Comparison；L1 T2.6 |
| `T12.2_diversity_combining_mrc.md` 分集与合并 | MRC 推导 ŝ=hᴴy/‖h‖²；SNR_out=‖h‖²/σ²~χ²₂ₙ；分集阶数 N：P(‖h‖²<ε)~ε^N/N!；32 支路→χ²₆₄、≈+15 dB（10log₁₀32）、0-6 dB 下 256QAM 可行；SIMO 1×N（test_simo 场景）；MMSE 单层=正则化 MRC（分母 ‖h‖²+σ² 避免深衰落除零）；分集 vs 波束赋形区别 | 蒙特卡洛：N=1/2/4/32 分支 MRC 深衰落概率（P(‖h‖²<ε)）随 ε 曲线 vs 理论 ε^N/N! | MIMO01 §3；概念笔记 Diversity_Combining；L1 T2.15 |
| `T12.3_linear_detectors_mf_zf_mmse.md` 线性检测器 MF/ZF/MMSE | MF ŝ=Hᴴy（σ²→∞ 极限）；ZF ŝ=(HᴴH)⁻¹Hᴴy（σ²→0 极限、消干扰放大噪声）；MMSE ŝ=Hᴴ(HHᴴ+σ²I)⁻¹y（正则化折中；相对 ZF 1-3 dB）；MMSE 推导（最小化 J(W)=E‖Wy−x‖²、Woodbury）；后验 MSE=σ²(HᴴH+σ²I)⁻¹；csi≥1 恒成立；无偏化归一化（effective_csi=max(csi−n_var,0)、mmse_gain、β=(csi−1)/csi）；0/0 与 ∞ 放大机理（csi→0）；±31 裁剪吸收（BLER 损失 <0.02 dB）；定点除法保护（csi_safe） | 固定随机 H：MF/ZF/MMSE 输出 SINR 对比 + csi≥1 恒成立数值验证 | MIMO01 §5；PHY01 §7；概念笔记 MMSE_均衡、Detector_Comparison；清单理论行（MMSE 推导/ZF/MF 两极限） |
| `T12.4_sphere_detection_detector_selection.md` 球面检测与检测器选择 | ML 复杂度 2^(Qm·Nlayers)（256QAM×4=2³² 不可穷举）；半径约束 ‖y−H_eff·s‖²≤r²；QR 树搜索（‖Qᴴy−Rs‖² 上三角分层累加、深度优先、剪枝）；FP（区间枚举、收缩慢）vs SE（部分距离排序、快 2-3 倍）；白化（y/√n_var、H/√n_var）与 LLR 符号约定；低 SNR 球内格点爆炸退化为穷举；三检测器对比（MMSE 4×4 ~100 MACs/tone ~95K gates 1-3 dB 损失；Sphere ~100-1000 MACs ~150K gates 0 dB、50-500 cycles/tone、仅高 SNR） | 2×2 QPSK 穷举 ML vs 半径剪枝枚举结果一致性验证（小规模随机实例） | MIMO01 §6；analysis 03 §3；概念笔记 Sphere_Decoding、Detector_Comparison；清单理论行（球面检测） |
| `T12.5_channel_estimation_llr_reliability.md` 信道估计与 LLR 可靠度 | 完美估计（nrPerfectChannelEstimate、上界参考）vs DMRS 实际估计；LS Ĥ_LS=Y_DMRS/X_DMRS（噪声放大 1/\|X\|²）；维纳滤波 Ĥ=R_HH(R_HH+σ²I)⁻¹Ĥ_LS（低 SNR 显著优、高 SNR 趋同、O(N_DMRS³)）；估计误差三途径（均衡输出偏置/CSI 失真/噪声方差失配；256QAM d_min≈0.16、偏移 0.08 翻转）；DMRS 走预编码→DMRS-based 估计直接给 H_eff；CSI 加权 LLR_out=LLR×csi（逐 RE 可靠度）；±31 裁剪与误差预算 | 1×1 信道：LS vs 维纳滤波估计 MSE 随 SNR（-5~20 dB）对比曲线 | MIMO01 §4/§7；概念笔记 Channel_Estimation、CSI_SINR；L1 T2.16 |

### 系列内衔接

- T12.1 为地图篇（衔接 L1 T2.6/T2.15 + MIMO_多天线系统概念笔记）；T12.2-12.5 承接 T12.1
- 每篇 `## 本节学习目标` 末尾给出系列内"下一篇承接"说明（仿 T8.1 风格）
- 篇目间互引：T12.3 引用 T12.2（MMSE=正则化 MRC）；T12.4 引用 T12.3（MMSE 基线）；T12.5 引用 T12.3（无偏化/CSI）

## 格式规范

- **模板**：沿用 L2 讲义模板（范本 `docs/L2_协议算法/T8.1_NR_LDPC_decoder_chain_overview.md`）：
  - frontmatter：`type: algorithm`、`aliases`（含 `T12.x <English title>`）、`tags`（`3gpp`、`docs`、`l2`、`lesson`）、`source_spec`
  - `# T12.x 中文标题`
  - `## 本节学习目标`：叙事 intro 段 + "学完本节后，应能做到：" bullets（6-8 条，动词开头、可检验）+ 系列内衔接段
  - `## 前置知识检查`：表格 `| 前置项 | 本节需要达到的程度 |`（引用 L1/L2 既有讲义与概念笔记）
  - 内容章节：公式 LaTeX（编号 `\tag{n}`）、表格、生活类比、数值实例
  - **SVG 图（每篇至少 1 个，硬性要求）**：放理解关键处（接收链路流程图、检测器对比框图、星座/决策区域示意、估计流程框图、数值曲线等），存 `docs/L2_协议算法/assets/`（命名 `T12.x_<英文主题>.svg`，与存量 `T10.x_*.png` 惯例一致）；**生成后强制按 CLAUDE.md 第 4 条视觉验证**：(1) Y 坐标扫描（提取全部 `<text>`/`<rect>`/`<line>` y 坐标，逐层核对间距 ≥ 8 px）(2) PNG 预览（cairosvg 或 ImageMagick convert 转 PNG 肉眼确认无交叠）——验证通过才允许写入资产目录并在正文引用；mermaid 图可作辅助，不能替代 SVG
  - `## 小结`：收束本节 + 指向下一篇
  - 与既有讲义/概念笔记的 `[[wikilink]]` 衔接
- **内嵌 Python**：每篇 1 个 numpy 代码块（10-30 行，`python` 代码围栏，教学注释风格；DOXYGEN 完整头仅适用于 `sim/` 正式脚本，内嵌块不强制，若日后抽为正式脚本再补）
- **合规**：Rule 10（英文术语首现"中文（English）"）、Rule 16（标题口语化禁止）、Rule 20（LaTeX 可渲染）、Rule 8（零基础保护——每篇至少 1 个生活类比）；SVG 图生成后强制视觉验证（Y 坐标扫描）
- **来源可溯**：协议锚点引用 TS/TR 小节号（TS 38.211 §5.1/§7.3.1.3/§7.4.1.1、TS 38.214 §5.1.3）+ 本地 `3GPP_Rel19/processed/` 锚点；仿真器/深挖语料引用标注"外部语料"

## 入口与集成

- `docs/L2_协议算法/L2_协议算法入口.md` 新增 `## M12 MIMO 接收机与检测器` 章节（在 M11 之后），挂 5 篇链接，与既有条目格式一致
- `概念图谱入口.md` 不改动（概念笔记已在图谱）
- 相关概念笔记补充指向讲义的图谱关联（可选，随讲义实施一并做）：Detector_Comparison/Diversity_Combining/Channel_Estimation/MMSE_均衡/Sphere_Decoding/CSI_SINR 各加 `[ [T12.x_...]]` 链接

## 验收标准

1. 5 篇按模板完成（学习目标 bullets 可检验、前置知识检查表格、内容章节、小结），每篇 500-800 行、内容有广度和深度（多视角 + 数值实例 + 表格）
2. **每篇 ≥1 个 SVG 图，且全部通过视觉验证**（Y 坐标扫描间距 ≥8 px + PNG 预览无交叠，验证证据记录在实施报告）
3. 每篇内嵌 Python 代码块实际运行，输出记录在实施报告，数值与讲义断言一致（功率守恒/分集概率/检测器 SINR 对比/剪枝一致性/MSE 曲线）
4. 无死链（全部 wikilink 可解析）
5. T12.1-12.5 编号唯一（不与现有编号冲突）
6. L2 入口 M12 章节更新完成
7. 合规红线抽查通过（Rule 10/16/20/8）
8. git 提交

## 不在范围（后续计划）

- 概率整形算法系列（L2 M13/T13.x）：ν̃ 归一化、完整平方 MAP 度量、衰落增益机制、功率节省公式、ESS 算法细节
- L3 工程讲义系列（T21.x）：周期预算、存储/面积估算、LLR 裁剪权衡深化
- `sim/python` 正式仿真包（内嵌代码已满足教学验证）
