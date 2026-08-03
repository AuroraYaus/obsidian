# 全链路缺口概念笔记实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 依据已批准 spec（`docs/superpowers/specs/2026-08-03-full-link-concept-notes-design.md`）完成 6 篇新概念笔记 + 3 篇增强 + 入口文件挂载，补齐 3GPP_FULL_LINK 复核出的概念层缺口。

**Architecture:** 全部为 Obsidian markdown 文档，无代码。每篇笔记独立成文件（`docs/concepts/`），六段式模板；增强类只补缺失内容（LLR_Quantization 例外：重建为六段式但保留全部现有内容）。执行顺序按主题分批：信道域 → 检测器域 → 协议/PS 域 → 增强 → 入口整合。每任务独立可验证（结构检查 + 死链检查 + 提交）。

**Tech Stack:** Obsidian markdown、LaTeX 公式（$...$ / $$...$$）、[[wikilink]] 双向链接、git。

## Global Constraints

- 六段式模板（每篇必须按序含）：`## 独立解释任务`（首行"任务目标：…"）→ `## 科学定义` → `## 直观模型` → `## 常见误解`（表格 `| 误解 | 正确理解 |`）→ `## 协议锚点` → `## 图谱关联`（末行"关系语义：…"）
- 命名与标题：文件名 `English_中文.md`；标题 `# English 中文`（空格分隔，不用全角括号）
- frontmatter：`type: definition` + `aliases` + `tags`（含 `3gpp`、`concepts`）+ `source_spec`
- 合规红线：Rule 10 英文术语首现"中文（English）"；Rule 16 标题口语化禁止；Rule 20 LaTeX 必须可渲染；Rule 8 零基础保护（直观模型用生活类比）
- 来源可溯：协议锚点引用 TS/TR 小节号 + 本地锚点 `3GPP_Rel19/processed/TS_38.211_38211-j30/content.md`；非标准项显式标注"非 3GPP 标准"
- 增强规则：Channel_Estimation、Probabilistic_Shaping 只追加不重构；LLR_Quantization 整篇重建（保留现有内容）
- 每篇 图谱关联 必须含 `[[概念图谱入口]]` + 上下游笔记
- 死链规则：全部 `[[链接]]` 必须能在仓库内找到对应文件

---

### Task 1: 信道域新笔记（Timing_Sync + Coherence_Bandwidth_Time）

**Files:**
- Create: `3gpp/docs/concepts/Timing_Sync_定时同步.md`
- Create: `3gpp/docs/concepts/Coherence_Bandwidth_Time_相干带宽与时间.md`

**Interfaces:**
- Produces: 两个新文件，供 Task 6 入口挂载引用（文件名即链接名，勿改名）

- [ ] **Step 1: 写 Timing_Sync_定时同步.md**

frontmatter：
```yaml
---
type: definition
aliases:
  - Timing Synchronization
  - 定时同步
  - 时间同步
  - PSS/SSS 检测
tags:
  - 3gpp
  - concepts
  - rx-chain
source_spec: "接收机实现（非协议算法）; evaluation-link-simulator"
---
```
正文结构（标题 `# Timing Sync 定时同步`）：
- **intro 段**：定时同步是 OFDM 接收的第一关——FFT 窗口必须对准符号边界，否则整帧解调错位；仿真器用理想定时，实际系统靠 PSS/SSS 或 CP 相关自己找。
- **独立解释任务**：任务目标：解释 OFDM 解调为什么需要先对齐符号边界、理想定时与实际定时的差距、以及定时误差如何进入估计误差预算。
- **科学定义**（bullets）：
  - 为什么需要：OFDM 解调要求 FFT 窗口对准符号边界；CP 提供一定容差（窗口落在 CP 内只有相位旋转）
  - 理想定时（仿真）：`nrPerfectTimingEstimate` 由 path_gains/path_filters 直接合成零误差定时——性能上界参考
  - 实际定时：PSS/SSS 相关峰检测（主/辅同步序列相关）或 CP 相关（CP 与符号尾部重复结构）；滑动窗相关器 O(Nfft×Ncp) MACs
  - 定时误差后果：FFT 窗口偏移 → 子载波间干扰 + 相位旋转 → 折算进信道估计误差（理想/实际定时差是估计误差来源之一）
- **直观模型**："对表"：开会前先校准钟表。OFDM 符号像一列固定节拍的车厢，FFT 窗口是检票口——窗口对不准，检票人就会把车厢里的人错配到相邻车厢。
- **常见误解**（表格，至少 3 行）：
  - 定时同步是协议规定的步骤 → 协议只定义 PSS/SSS 位置与序列，检测算法是接收机自由度
  - 仿真里不需要定时同步 → 仿真假设 nrPerfectTimingEstimate 理想定时，实际系统必须自己找
  - 定时误差只影响幅度 → 会引入相位旋转与载波间泄漏（ICI），并进入估计误差预算
- **协议锚点**：
  - PSS/SSS：TS 38.211 Rel-19 §7.4.2（本地 `3GPP_Rel19/processed/TS_38.211_38211-j30/content.md`）
  - 仿真器实现：`receive_grid.m`（nrPerfectTimingEstimate）、PHY01 §1.5
- **图谱关联**：`[[概念图谱入口]]`、`[[Channel_Estimation_信道估计]]`、`[[TDL_信道模型]]`、`[[MMSE_均衡]]`、`[[Physical_Channels_物理信道]]`；关系语义：定时同步是 OFDM 解调的第一关，定时误差进入信道估计误差预算，是"理想假设 vs 实际实现"差距的一部分。

- [ ] **Step 2: 写 Coherence_Bandwidth_Time_相干带宽与时间.md**

frontmatter：
```yaml
---
type: definition
aliases:
  - Coherence Bandwidth
  - Coherence Time
  - 相干带宽
  - 相干时间
  - coherence
tags:
  - 3gpp
  - concepts
  - channel
source_spec: "TR 38.901; 接收机设计（非协议算法）"
---
```
正文结构（标题 `# Coherence Bandwidth & Time 相干带宽与时间`）：
- **intro 段**：衰落信道在多大范围内"看起来一样"由两个尺度决定——频率上的相干带宽、时间上的相干时间；它们是信道估计/均衡颗粒度设计的依据。
- **独立解释任务**：任务目标：解释相干带宽/时间是什么、数值怎么来，以及为什么 30 kHz 子载波和 0.5 ms 时隙在这两个尺度内是安全的（平坦/准静态假设）。
- **科学定义**（bullets，含公式）：
  - 相干带宽：B_c ≈ 1/(2πτ_rms)；TDL-C 300 ns → ≈530 kHz ≫ 30 kHz SCS → 每个子载波内信道平坦，频选性主要体现为 RE 间 SNR 散布
  - 相干时间：T_c ≈ 0.423/f_d；30 Hz 多普勒 → ≈14.1 ms ≫ 0.5 ms 时隙 → 时隙内准静态，块级处理合理
  - 速度换算：f_d = v·f_c/c；30 Hz @3.5 GHz = 9.3 km/h
  - 使用方式：相干带宽决定估计/均衡的 RE 颗粒度（每子载波一组 H 即可）；相干时间决定信道更新频率（每时隙一次即可）
- **直观模型**："地形起伏尺度"：一段路"看起来平"，是因为路面起伏的波长比车轮间距大得多。相干带宽就是信道在频率上的"起伏波长"——子载波间距远小于它，所以每个子载波视野内地面是平的。
- **常见误解**（表格，至少 3 行）：
  - 相干带宽内信道完全一样 → 是"近似平坦"（起伏可忽略），不是处处相等
  - 相干时间 = 信道保持不变的时长 → 是统计相关尺度；"准静态"是工程近似
  - 相干带宽与 SCS 无关 → numerology 设计要让 SCS ≪ B_c，否则每个 RE 都得单独估计
- **协议锚点**：
  - TDL 参数：TR 38.901 Table 7.7.2-1（TDL-A~E 时延谱、RMS 延迟扩展）
  - SCS/时隙：TS 38.211 Rel-19 §4.2（Numerologies）与 §4.3.2（Slots）（本地 `3GPP_Rel19/processed/TS_38.211_38211-j30/content.md`）
- **图谱关联**：`[[概念图谱入口]]`、`[[TDL_信道模型]]`、`[[Fading_Channel_衰落信道]]`、`[[Channel_Estimation_信道估计]]`、`[[Timing_Sync_定时同步]]`；关系语义：相干带宽/时间决定信道估计与均衡的颗粒度——相干带宽≫SCS 使每子载波估计可行，相干时间≫时隙使块级处理合理。

- [ ] **Step 3: 结构验证两篇**

Run（在仓库根目录）：
```bash
for f in "3gpp/docs/concepts/Timing_Sync_定时同步.md" "3gpp/docs/concepts/Coherence_Bandwidth_Time_相干带宽与时间.md"; do
  echo "=== $f ==="; grep -c "^## " "$f"; grep -n "^## " "$f" | awk '{print $2}'; done
```
Expected：每篇 6 个 `##` 节，顺序为 独立解释任务/科学定义/直观模型/常见误解/协议锚点/图谱关联。

- [ ] **Step 4: 死链检查两篇**

Run（仓库根目录）：
```bash
for f in "3gpp/docs/concepts/Timing_Sync_定时同步.md" "3gpp/docs/concepts/Coherence_Bandwidth_Time_相干带宽与时间.md"; do
  grep -oE "\[\[[^]]+\]\]" "$f" | sed 's/\[\[//;s/\]\]//' | while read -r link; do
    base="${link%%|*}"; base="${base%%#*}";
    if [ -z "$(find 3gpp -name "${base}.md" 2>/dev/null | head -1)" ] && [ -z "$(find 3gpp -name "${base}.md" 2>/dev/null)" ]; then echo "DEAD LINK in $f: $base"; fi
  done; done
```
Expected：无 DEAD LINK 输出（T0.1/T4.x 等讲义链接须存在于 docs 树）。

- [ ] **Step 5: Commit**

```bash
git add 3gpp/docs/concepts/Timing_Sync_定时同步.md 3gpp/docs/concepts/Coherence_Bandwidth_Time_相干带宽与时间.md
git commit -m "docs(concepts): 新增定时同步与相干带宽/时间概念笔记"
```

---

### Task 2: 检测器域新笔记（Detector_Comparison + Diversity_Combining）

**Files:**
- Create: `3gpp/docs/concepts/Detector_Comparison_检测器对比.md`
- Create: `3gpp/docs/concepts/Diversity_Combining_分集与合并.md`

**Interfaces:**
- Produces: 两个新文件，供 Task 6 入口挂载引用（文件名即链接名，勿改名）

- [ ] **Step 1: 写 Detector_Comparison_检测器对比.md**

frontmatter：
```yaml
---
type: definition
aliases:
  - Detector Comparison
  - 检测器对比
  - 均衡器对比
  - ZF/MMSE/Sphere
tags:
  - 3gpp
  - concepts
  - rx-chain
  - detection
source_spec: "接收机实现（非协议算法）; MIMO01 §5-6"
---
```
正文结构（标题 `# Detector Comparison 检测器对比`）：
- **intro 段**：每 RE 的 MIMO 模型 y=Hx+n 下，接收机用检测器把符号 x 估计出来；MF/ZF/MMSE/Sphere 四族是精度与代价的不同折中。
- **独立解释任务**：任务目标：解释四种检测器的公式、复杂度与性能损失，以及为什么 MMSE 是默认、Sphere 只在特定场景（高 SNR）用。
- **科学定义**（bullets，含公式）：
  - MF：ŝ = Hᴴy（只匹配信道、忽略干扰；σ²→∞ 极限）
  - ZF：ŝ = (HᴴH)⁻¹Hᴴy（完全消干扰、放大噪声；σ²→0 极限）
  - MMSE：ŝ = Hᴴ(HHᴴ+σ²I)⁻¹y（正则化折中；相对 ZF 1-3 dB；4×4 ~100 MACs/tone、~95K gates、~20 cycles/tone）
  - Sphere：半径约束 ML 搜索（‖y−Hs‖²≤r²、QR 树搜索 + FP/SE 剪枝）；0 dB 损失；~100-1000 MACs/tone、~150K gates、50-500 cycles/tone；低 SNR 球内格点数 ∝(r²/σ²)^Nlayers 爆炸 → 退化为穷举
  - 性能排序 MF ≤ ZF ≤ MMSE ≤ ML（Sphere）；复杂度排序相反
- **直观模型**："四种听法"：MF=只听最强声源；ZF=把其他声源完全消掉（杂音被放大）；MMSE=在消除与放噪之间找平衡；Sphere=把每一种可能组合都核对一遍（最准、最贵、最慢）。
- **常见误解**（表格，至少 3 行）：
  - Sphere 一定比 MMSE 好 → 性能 0 dB 损失，但低 SNR 复杂度爆炸、延迟随机，只适合高 SNR 场景
  - MMSE 是协议规定的算法 → 检测器是接收机自由度，协议只定义传输假设
  - ZF 消除干扰没有代价 → 消干扰必然放大噪声（σ²/|h|² 量级），深衰落处最严重
- **协议锚点**：
  - 接收机自由度（TS 38.214 只定义传输假设，不规定检测器）
  - 仿真器实现：`new_pdsch_decode.m`（demapper 分支 mmse/sphere）、`nrEqualizeMMSE`、`comm.SphereDecoder`（MIMO01 §5-6、analysis 03 §3）
- **图谱关联**：`[[概念图谱入口]]`、`[[MMSE_均衡]]`、`[[Sphere_Decoding_球面检测]]`、`[[CSI_SINR]]`、`[[Diversity_Combining_分集与合并]]`、`[[MIMO_多天线系统]]`；关系语义：检测器把每 RE 矩阵模型变成符号估计，输出（+CSI 加权）喂给软解调；MMSE 是线性默认、Sphere 是 ML 参考。

- [ ] **Step 2: 写 Diversity_Combining_分集与合并.md**

frontmatter：
```yaml
---
type: definition
aliases:
  - Diversity Combining
  - 分集
  - 分集合并
  - MRC
  - Maximum Ratio Combining
  - 最大比合并
  - 分集阶数
tags:
  - 3gpp
  - concepts
  - rx-chain
  - diversity
source_spec: "接收机实现（非协议算法）; MIMO01 §3"
---
```
正文结构（标题 `# Diversity Combining 分集与合并`）：
- **intro 段**：多天线接收的收益来自分集——多份独立衰落的拷贝合在一起，深衰落的概率被指数压低；MRC 是最优线性合并。
- **独立解释任务**：任务目标：解释分集阶数是什么、MRC 如何合并多份拷贝、"32 天线 ≈ +15 dB" 怎么来的，以及 MMSE 与 MRC 的关系。
- **科学定义**（bullets，含公式）：
  - 分集阶数：独立衰落支路数 N；N 支路下 P(‖h‖²<ε) ~ ε^N/N!——深衰落概率指数下降
  - MRC：ŝ = hᴴy/‖h‖²，SNR_out = ‖h‖²/σ² ~ χ²₂ₙ（n 支路）；共轭匹配自动对齐相位
  - 数值实例：32 支路 → χ²₆₄、分集阶数 32、0-6 dB SNR 下 256QAM 可行、≈ +15 dB 阵列增益（test_simo 场景）
  - MMSE 单层 = 正则化 MRC：分母 ‖h‖²+σ²，深衰落避免除零
- **直观模型**："多份拷贝投票"：同一句话让 32 个人分别听，每个人听到不同的噪音；把 32 份记录加权平均，独立错误互相抵消——单份可能全错，32 份全错需要 32 个独立坏运气，概率指数变小。
- **常见误解**（表格，至少 3 行）：
  - 分集 = 波束赋形 → 分集抗衰落（非相干合并独立拷贝），波束赋形定向增强（相干合并）——目的与合并方式都不同
  - MRC 需要估计相位再补偿 → 共轭匹配 hᴴy 自动完成相位对齐
  - 天线越多吞吐线性增长 → 阵列增益对数增长；分集收益体现在深衰落概率指数下降，主要在低 SNR/深衰落区
- **协议锚点**：
  - 接收机自由度；仿真器实现：`test_simo.m`（1×32 MRC 域）、`nrEqualizeMMSE`（MIMO01 §3.2-3.3）
- **图谱关联**：`[[概念图谱入口]]`、`[[MIMO_多天线系统]]`、`[[MMSE_均衡]]`、`[[Detector_Comparison_检测器对比]]`、`[[Fading_Channel_衰落信道]]`；关系语义：分集是 MIMO 接收的第一重收益（抗衰落），MRC 是合并工具，MMSE 是它的正则化推广。

- [ ] **Step 3: 结构验证两篇**

Run（同 Task 1 Step 3 的命令，文件替换为这两篇）：Expected：每篇 6 个 `##` 节且顺序正确。

- [ ] **Step 4: 死链检查两篇**

Run（同 Task 1 Step 4 的命令，文件替换为这两篇）：Expected：无 DEAD LINK 输出。

- [ ] **Step 5: Commit**

```bash
git add 3gpp/docs/concepts/Detector_Comparison_检测器对比.md 3gpp/docs/concepts/Diversity_Combining_分集与合并.md
git commit -m "docs(concepts): 新增检测器对比与分集合并概念笔记"
```

---

### Task 3: 协议/PS 域新笔记（MCS_Table + Geometric_Shaping）

**Files:**
- Create: `3gpp/docs/concepts/MCS_Table_Effective_Code_Rate_MCS表与有效码率.md`
- Create: `3gpp/docs/concepts/Geometric_Shaping_几何整形.md`

**Interfaces:**
- Produces: 两个新文件，供 Task 6 入口挂载引用（文件名即链接名，勿改名）

- [ ] **Step 1: 写 MCS_Table_Effective_Code_Rate_MCS表与有效码率.md**

frontmatter：
```yaml
---
type: definition
aliases:
  - MCS Table
  - MCS 表
  - Effective Code Rate
  - 有效码率
  - R_eff
  - ps_mcs_table
tags:
  - 3gpp
  - concepts
  - protocol
source_spec: "TS 38.214 §5.1.3; evaluation-link-simulator MCS 表"
---
```
正文结构（标题 `# MCS Table & Effective Code Rate MCS表与有效码率`）：
- **intro 段**：MCS 表把调度索引映射为调制阶数、目标码率（PS 场景还含整形强度 ν）；"有效码率"是实际 payload 折算出来的真实码率，与目标码率脱钩。
- **独立解释任务**：任务目标：解释 4 张 MCS 表的结构差异、PS 表为什么 SE≠Qm×R/1024、以及 R_eff 与目标码率脱钩的含义。
- **科学定义**（bullets）：
  - 标准表：qam64（MCS 0-28）、qam256（MCS 0-31，28-31 保留）
  - PS 表：ps_mcs_table1/2（MCS 5-27，5 列含 ν_MB；1024QAM 仅 MCS 24-27，Qm=10）
  - 5 列结构：[MCS, SE, Qm, R×1024, ν_MB]；SE = Qm×R/1024 仅在标准表成立
  - PS 表 SE ≠ Qm·R/1024：MCS10 表值 2.5704 vs Qm×R=4.5——整形压缩信息速率，SE 直接列实际可达值
  - 有效码率：R_eff = payloadTBS/(N_RE·Qm)，与目标码率 R 脱钩；PS 公平比较用 R_eff（TBS matching 后同码率比能量）
- **直观模型**："菜单 vs 实付"：MCS 表是菜单（标称码率 Qm×R），R_eff 是结账时的实付（payload 折算）。整形像"点 4.5 份实际上桌 2.57 份"——菜单没变，实付低了，所以公平比较必须按实付（R_eff）来。
- **常见误解**（表格，至少 3 行）：
  - PS 表的 SE 就是 Qm×码率 → PS 表 SE 已扣除整形压缩，直接列出可达值（MCS10: 2.5704 vs 4.5）
  - 有效码率 = 目标码率 → R_eff 是 payload/(N_RE·Qm)，整形/开销都会让它偏离 R
  - 1024QAM 是标准 MCS 能力 → 1024QAM 只在 PS 表 MCS 24-27，标准表不含
- **协议锚点**：
  - MCS/TBS：TS 38.214 Rel-19 §5.1.3（本地 `3GPP_Rel19/processed/TS_38.214_38214-j30/content.md`）
  - 仿真器实现：`getMcsInfo.m`（4 表硬编码，5 列解析）、`resolveMcsInfo.m`（表选择+nu 参数流）
- **图谱关联**：`[[概念图谱入口]]`、`[[TB_传输块]]`、`[[QAM1024_1024QAM]]`、`[[Probabilistic_Shaping_概率整形]]`、`[[MB_Distribution_MB分布]]`；关系语义：MCS 表把 MCS 索引映射到 (Qm, 码率, ν)；PS 表多一列 ν_MB 使整形参数进入链路选择，R_eff 是跨 PS/Uniform 公平比较的统一口径。

- [ ] **Step 2: 写 Geometric_Shaping_几何整形.md**

frontmatter：
```yaml
---
type: definition
aliases:
  - Geometric Shaping
  - GS
  - 几何整形
tags:
  - 3gpp
  - concepts
  - probability-shaping
source_spec: "非 3GPP 标准（6G 候选）; PS01 §1.2"
---
```
正文结构（标题 `# Geometric Shaping 几何整形`）：
- **intro 段**：逼近高斯输入分布的路线有两条——改使用概率（PS）或改星座坐标（GS）；GS 路线因标准兼容性差，在 3GPP 语境下是 PS 的对照而非替代。
- **独立解释任务**：任务目标：解释 GS 与 PS 的本质区别、GS 难进标准的原因、以及 DVB-S2X 走 PS 路线的启示。
- **科学定义**（bullets）：
  - GS：改变星座点坐标位置（几何形状，如圆 QAM）；使用概率保持均匀
  - PS：保持坐标不变（TS 38.211 §5.1 固定），只改使用概率；可叠加 NR QAM 链路
  - 标准兼容性：GS 需 TX/RX 协商新星座表 + 改解调参考 → 标准流程（TS 38.211 §5.1 星座定义）改动大；PS 只贴标准接口工作
  - 商用先例：DVB-S2X 采用 CCDM+MB（PS 路线）而非 GS
  - 实证状态：3GPP Rel-19 全套语料无 PS/GS 内容（均为 6G 候选）
- **直观模型**："改走法 vs 改路"：PS 是改变出行习惯（近路多走远路少走，路网不变）；GS 是重新修路（改地图）。修路要所有司机（TX/RX）换新地图，改习惯只需约定各路的走法频率。
- **常见误解**（表格，至少 3 行）：
  - GS 和 PS 是同类技术 → 一个改坐标一个改概率，硬件与标准影响完全不同
  - GS 一定比 PS 好 → 无标准支撑、协商成本高；PS 已获得大部分整形增益且兼容现有链路
  - 星座是发射端自由决定的 → TS 38.211 §5.1 固定星座与 label，改动即标准变更
- **协议锚点**：
  - **GS 本身：非 3GPP 标准，无标准小节**
  - 对照：TS 38.211 Rel-19 §5.1（固定星座定义，本地 `3GPP_Rel19/processed/TS_38.211_38211-j30/content.md`）
- **图谱关联**：`[[概念图谱入口]]`、`[[Probabilistic_Shaping_概率整形]]`、`[[MB_Distribution_MB分布]]`、`[[Modulation_Constellations_调制星座]]`；关系语义：GS 是 PS 的对照路线——同一目标（逼近高斯输入）的两种实现，PS 以标准兼容性胜出；DVB-S2X 提供了商用实证。

- [ ] **Step 3: 结构验证两篇**

Run（同 Task 1 Step 3，文件替换为这两篇）：Expected：每篇 6 个 `##` 节且顺序正确。

- [ ] **Step 4: 死链检查两篇**

Run（同 Task 1 Step 4，文件替换为这两篇）：Expected：无 DEAD LINK 输出。

- [ ] **Step 5: Commit**

```bash
git add "3gpp/docs/concepts/MCS_Table_Effective_Code_Rate_MCS表与有效码率.md" "3gpp/docs/concepts/Geometric_Shaping_几何整形.md"
git commit -m "docs(concepts): 新增 MCS 表与有效码率、几何整形概念笔记"
```

---

### Task 4: 增强 Channel_Estimation + Probabilistic_Shaping（只补不重构）

**Files:**
- Modify: `3gpp/docs/concepts/Channel_Estimation_信道估计.md`（科学定义追加 3 bullets、常见误解追加 1 行）
- Modify: `3gpp/docs/concepts/Probabilistic_Shaping_概率整形.md`（科学定义追加 2 bullets、常见误解追加 1 行）

**Interfaces:**
- Consumes: 两个既有文件（六段式已合规，不改结构、不动存量文字）

- [ ] **Step 1: Channel_Estimation 科学定义追加 3 bullets**

在"**估计误差的代价**"bullet 之后追加：
```markdown
- **维纳滤波估计**：Ĥ = R_HH(R_HH+σ²I)⁻¹Ĥ_LS——利用信道统计先验加权；低 SNR 显著优于 LS、高 SNR 与 LS 趋同；代价 O(N_DMRS³) 矩阵求逆
- **估计误差三途径**：均衡输出偏置（Ĥ·W≠I）、CSI 失真（过度自信/保守）、噪声方差失配——256QAM 下 d_min≈0.16，硬判决偏移超 d_min/2≈0.08 即翻转
- **DMRS 走预编码 → H_eff 直接估计**：DMRS 在层域插入后与数据同乘预编码矩阵 P，DMRS-based 估计直接给出层域等效信道 H_eff，接收端无需知道 P
```

- [ ] **Step 2: Channel_Estimation 常见误解追加 1 行**

表格末尾追加：
```markdown
| 完美估计与实际估计的差距可以忽略 | 深衰落处估计误差最大；256QAM 偏移超 0.08 硬判决即翻转——误差预算必须显式管理 |
```

- [ ] **Step 3: Probabilistic_Shaping 科学定义追加 2 bullets**

在"**非标准属性**"bullet 之前追加：
```markdown
- **四个接入点架构**：PS 只改 4 处——TB 构造（build_tb_for_ps）、加扰（ps_scramble）、解调前（preprocess_demod_input）、LDPC 解码后（deshape_tb）；NR spine（nrDLSCH/OFDM/检测器/nrDLSCHDecoder）全部复用——数据路径只认长度与统计约定，不认内容语义
- **PS 几何可行性条件**：numParityBits ≤ 2N_s(Qm/2−k)−L_cb 且 2Zc+2kN_s ≤ K−F−L_cb——整形区不能侵占 LDPC 打孔前缀（2Zc）与校验 bit 预算
```

- [ ] **Step 4: Probabilistic_Shaping 常见误解追加 1 行**

表格末尾追加：
```markdown
| PS 要改标准编码链路 | 只改 4 个接入点，NR 编码/OFDM/检测器全复用——标准接口不动 |
```

- [ ] **Step 5: 验证（追加内容在位、六段式未破坏）**

Run（仓库根目录）：
```bash
grep -c "维纳滤波\|估计误差三途径\|H_eff" "3gpp/docs/concepts/Channel_Estimation_信道估计.md"
grep -c "四个接入点\|几何可行性" "3gpp/docs/concepts/Probabilistic_Shaping_概率整形.md"
```
Expected：Channel_Estimation ≥3（维纳滤波/误差三途径/H_eff 各 1+）、Probabilistic_Shaping ≥2（四接入点/可行性条件各 1）——新增内容全部在位。

- [ ] **Step 6: Commit**

```bash
git add "3gpp/docs/concepts/Channel_Estimation_信道估计.md" "3gpp/docs/concepts/Probabilistic_Shaping_概率整形.md"
git commit -m "docs(concepts): 增强信道估计（维纳滤波/误差三途径/H_eff）与概率整形（四接入点/可行性条件）"
```

---

### Task 5: 重建 LLR_Quantization（六段式）

**Files:**
- Rewrite: `3gpp/docs/concepts/LLR_Quantization_LLR量化.md`

**Interfaces:**
- Consumes: 现有内容（均匀/非均匀量化、裁剪阈值 C、位宽-收益 0.1-0.2 dB）必须全部保留
- Produces: 六段式重建文件

- [ ] **Step 1: 整篇重写**

frontmatter 沿用现有（type: definition、aliases、tags、source_spec 不变）。正文结构（标题 `# LLR 量化与裁剪` 保留）：
- **intro 段**：浮点 LLR 进入定点译码器前须经裁剪与量化；裁剪防溢出（灾难性错误），量化损失精度（可接受误差）。
- **独立解释任务**：任务目标：解释裁剪与量化的分工、裁剪阈值 C 怎么选、以及为什么 ±31（6-bit）是工程拐点。
- **科学定义**（bullets，含公式）：
  - 均匀量化：Δ 固定，LLR_q = round(clip(LLR, ±C)/Δ)·Δ
  - 非均匀量化：小 |LLR| 细量化、大 |LLR| 粗量化（保留小 LLR 的方向与精度）
  - 裁剪阈值 C：|LLR|>C → 截断；C 太小丢可信度、太大浪费位宽；位宽增 1 bit → ~0.1-0.2 dB BLER 改善
  - LLR 动态范围：1024QAM 下 max|y−x|²≈11.2（(2×31/√682)²≈5.6 × I/Q 两维）；SNR=30 dB → σ²=0.001 → LLR_max≈11200，无裁剪需 14-bit
  - 裁剪-损失权衡表：±7（4-bit）<0.1 dB、±15（5-bit）<0.05 dB、±31（6-bit）<0.02 dB、±63 <0.01 dB——±31 已到收益拐点
  - **±31 吸收机制**：MMSE 归一化除法放大（csi→0 时 0/0、∞）被 ±31 裁剪兜底，BLER 损失 <0.02 dB；定点溢出回绕才是"灾难性错误"
- **直观模型**："温度计的刻度上限"：LLR 是可信度刻度，裁剪是温度计的量程上限——超量程都记为上限，丢掉的是极端值细节，保住的是方向和极性；宁可牺牲极端读数，也不能让指针撞坏（溢出回绕）。
- **常见误解**（表格，至少 3 行）：
  - 裁剪阈值越大越好 → 位宽成本随阈值线性涨，收益 <0.02 dB 封顶——±31 是工程拐点
  - 量化误差和裁剪误差是同一回事 → 裁剪防溢出（错误分级：灾难性），量化只损失精度（可预测）
  - 定点溢出回绕可以接受 → 回绕是灾难性错误（方向翻转），裁剪是第一道闸门
- **协议锚点**：
  - 译码器输入接口：TS 36.212/38.212 译码器要求（本地讲义 `T18.1_fixed_point_decoder_requirements`）
  - 仿真器口径：LLR 恒裁剪 ±31（6-bit signed）、48-bit SRAM word 装 8 个 LLR（PHY01 §12）
- **图谱关联**：`[[概念图谱入口]]`、`[[LLR_对数似然比]]`、`[[Fixed_Point_Numbers_定点数]]`、`[[Soft_Demodulation_软解调]]`、`[[Detector_Comparison_检测器对比]]`；**必须保留现有 图谱关联 条目** `[[T2.11_LLR_clipping_scaling_quantization]]`、`[[T18.1_fixed_point_decoder_requirements]]`；关系语义：LLR 量化是软解调到译码器的格式转换；裁剪阈值决定动态范围预算，±31 同时吸收 MMSE 归一化放大。

- [ ] **Step 2: 结构验证**

Run：`grep -n "^## " "3gpp/docs/concepts/LLR_Quantization_LLR量化.md"`
Expected：6 个 `##` 节，顺序正确（独立解释任务/科学定义/直观模型/常见误解/协议锚点/图谱关联）。

- [ ] **Step 3: 存量内容保留检查**

Run：`grep -c "非均匀量化\|裁剪阈值 C\|0.1-0.2"`
Expected：≥3（原有点/线内容全部保留）。

- [ ] **Step 4: Commit**

```bash
git add "3gpp/docs/concepts/LLR_Quantization_LLR量化.md"
git commit -m "docs(concepts): 重建 LLR 量化笔记为六段式并补充裁剪权衡表"
```

---

### Task 6: 入口文件挂载 + 全量校验

**Files:**
- Modify: `3gpp/docs/concepts/概念图谱入口.md`

**Interfaces:**
- Consumes: Task 1-5 全部 6 个新文件名（链接名=文件名）

- [ ] **Step 1: 协议结构章节追加 1 行**

在 `- [[Segmentation_码块分段]]` 后追加：
```markdown
- [[MCS_Table_Effective_Code_Rate_MCS表与有效码率]]
```

- [ ] **Step 2: 信道与接收链路章节追加 4 行**

在 `- [[QAM1024_1024QAM]]` 后追加：
```markdown
- [[Timing_Sync_定时同步]]
- [[Coherence_Bandwidth_Time_相干带宽与时间]]
- [[Detector_Comparison_检测器对比]]
- [[Diversity_Combining_分集与合并]]
```

- [ ] **Step 3: 概率整形章节追加 1 行**

在 `- [[LLR_Prior_LLR先验]]` 后追加：
```markdown
- [[Geometric_Shaping_几何整形]]
```

- [ ] **Step 4: 全量死链校验（concepts 目录全部文件）**

Run（仓库根目录）：
```bash
cd 3gpp/docs/concepts && for f in *.md; do
  grep -oE "\[\[[^]]+\]\]" "$f" | sed 's/\[\[//;s/\]\]//' | while read -r link; do
    base="${link%%|*}"; base="${base%%#*}";
    if ! ls "${base}.md" >/dev/null 2>&1 && ! find /home/yys/AGENT/obsidian/3gpp/docs -name "${base}.md" 2>/dev/null | grep -q .; then
      echo "DEAD LINK in $f: $base";
    fi
  done
done; echo "scan done"
```
Expected：仅输出 `scan done`（无 DEAD LINK）。

- [ ] **Step 5: 全量六段式校验（concepts 目录全部文件，旧式格式文件除外）**

Run：`grep -L "^## 独立解释任务" *.md` 输出应只含 3GPP全流程_缩写概念理论清单.md 与旧式格式存量（若输出含新 6 篇或重建的 LLR_Quantization 则为失败）。

- [ ] **Step 6: Commit**

```bash
git add "3gpp/docs/concepts/概念图谱入口.md"
git commit -m "docs(concepts): 概念图谱入口挂载 6 篇全链路新笔记"
```

---

## Self-Review（编写者自查）

1. **Spec 覆盖**：spec 的 6 新（Timing_Sync/Coherence/Detector/Diversity/MCS_Table/Geometric_Shaping）→ Task 1-3；3 增强（Channel_Estimation/LLR_Quantization/Probabilistic_Shaping）→ Task 4-5；入口三处挂载 → Task 6；验收 1-5 条 → 各任务 Step 3/4/5 验证 + Task 6 Step 4/5 ✓
2. **占位符扫描**：无 TBD/TODO；每篇笔记的章节内容均给出具体要点与公式 ✓
3. **类型一致性**：文件名（链接名）在 Task 1-3 创建与 Task 6 挂载完全一致；LLR_Quantization 文件名不变；frontmatter 字段名统一 ✓
