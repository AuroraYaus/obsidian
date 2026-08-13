# T22 Modem 接收链子系统工程讲义 Implementation Plan（阶段 6 首轮）

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按全链路规划阶段 6（G11 首轮）：Modem 接收链子系统工程 4 篇完整讲义（T22.1-T22.4，L3），把 L1 T2.x 的接收算法升级为工程实现级——与译码器工程（T17-T20）并列。

**Architecture:** 依拷问锁定版 spec 阶段 6（"Modem 子系统仿真/RTL"）执行。**批次构成：4 篇一轮（按推荐决策执行，用户授权 2026-08-13）**——同步/信道估计、均衡器、软解调器、接收链集成预算。L3 编号：讲义文件 T22.x（T16-T21 已用，T22 空闲）；模块 M17（L3 规则 M17+，与 L2 M16 不冲突——跨层编号带层名）。7 任务：T22.1-T22.4 + 同步 + 全量验证 + 双推。子代理配额已尽——主会话直接创作 + 自审。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- **讲义模板**（.claude/rules/documentation.md §二）：frontmatter（type: algorithm + aliases + tags 含 l3 + source_spec）→ 学习目标（6-8 条 bullets）→ 前置知识检查（表格）→ 内容章节（LaTeX \tag 公式、表格、生活类比、数值实例）→ 示范例题/引导练习/独立习题（附答案）→ 小结（指向下一篇）。
- **例题数量上限**：示范例题、引导练习、独立习题**每类 ≤3、全篇 ≤9**。
- **行数**：≥500 为下限参考、内容充实即可；上限不限；深度不足合并（2026-08-13 用户裁定）。
- **写作规范**：正文无中间过程叙述；概念首现讲解 + wikilink；手算与 numpy 一致；每篇 ≥1 生活类比；英文术语首现「ABBR（中文，English Full Name）」（audit_term_first_use 全绿硬验收）；带圈数字禁令；标题正式化；wikilink 管道用普通 `|`；习题插入按编号顺序。
- **每篇硬件要求**：≥1 教学图（复杂图 SVG 过 audit_svg_layout R1-R11 + cairosvg；简单流程 Mermaid 过 audit_mermaid_syntax.sh）；1 个内嵌 numpy 验证（实跑断言通过后原样贴入）。
- **前置锚点**：T22.x 锚 L1 T2.x（算法）+ L3 T17/T19（工程惯例：golden model/定点/RTL 视角）。
- **协议锚点**：TS 38.211（参考信号/信道结构）——算法数值对照本地 `3GPP_Rel19/processed/`。
- 提交后 `git push origin master`（双推，阶段收尾统一执行）。

---

### Task T22.1: 讲义 T22.1 同步与信道估计工程

**Files:**
- Create: `3gpp/docs/L3_工程实现/T22.1_sync_channel_estimation_engineering.md`

**Interfaces:**
- Consumes: T2.7/T2.8（同步算法）、T2.11（信道估计）、T17.x（工程惯例）。
- Produces: 讲义全文，T22.4 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：同步跟踪环路与信道估计器的工程实现（环路结构、估计器架构、定点/资源视角）
- 内容章节：(1) 接收链中同步/估计的位置（T2.x 算法回顾）(2) 定时/频偏跟踪环路（环路滤波器、带宽 vs 噪声）(3) 信道估计器架构（LS/MMSE 的工程近似、插值器）(4) 定点与资源（乘加单元、存储）(5) 与 T17 golden model 惯例衔接
- numpy 验证例：跟踪环路仿真（定时误差收敛）或 LS/插值信道估计的定点误差分析
- 例题：环路带宽选择 / 估计器资源估算
- 图：≥1（跟踪环路 Mermaid）
- 协议锚点：TS 38.211（DM-RS 位置）

**Step 2/3**: 验证与提交。

---

### Task T22.2: 讲义 T22.2 均衡器工程

**Files:**
- Create: `3gpp/docs/L3_工程实现/T22.2_equalizer_engineering.md`

**Interfaces:**
- Consumes: T2.11/T12.3（均衡算法）、T18（定点惯例）。
- Produces: 讲义全文，T22.4 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：MMSE/ZF 均衡器的工程实现（矩阵求逆硬件、近似、定点）
- 内容章节：(1) 均衡算法回顾（T12.3）(2) MMSE 的工程实现（Cholesky/迭代求逆）(3) 均衡器架构（流水线、资源）(4) 定点分析（矩阵条件数 vs 精度）(5) 与译码器衔接（输出 LLR 接口）
- numpy 验证例：MMSE 均衡的定点误差分析（浮点 vs 定点 SNR 损失）
- 例题：矩阵求逆复杂度 / 定点位宽选择
- 图：≥1（均衡器流水线 Mermaid）
- 协议锚点：TS 38.214（DM-RS 辅助估计）

**Step 2/3**: 验证与提交。

---

### Task T22.3: 讲义 T22.3 软解调器工程

**Files:**
- Create: `3gpp/docs/L3_工程实现/T22.3_soft_demapper_engineering.md`

**Interfaces:**
- Consumes: T2.13/T2.14（软解调算法）、T18（定点惯例）。
- Produces: 讲义全文，T22.4 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：LLR 计算的工程实现（Max-Log-MAP 近似、查找表、定点）
- 内容章节：(1) 软解调算法回顾（T2.13/T2.14）(2) Max-Log-MAP 的工程简化（分段线性/查找表）(3) LLR 量化与裁剪（T2.16 衔接）(4) 硬件架构（并行 LLR 单元）(5) 与译码器 LLR 接口（T17/T19 衔接）
- numpy 验证例：Max-Log-MAP 近似 vs 精确 LLR 的误差分析 + 量化损失
- 例题：LLR 位宽选择 / 查找表大小
- 图：≥1（软解调流水线 Mermaid）
- 协议锚点：TS 38.211 §5.1（星座）

**Step 2/3**: 验证与提交。

---

### Task T22.4: 讲义 T22.4 接收链集成与预算

**Files:**
- Create: `3gpp/docs/L3_工程实现/T22.4_rx_chain_integration_budget.md`

**Interfaces:**
- Consumes: T22.1-T22.3、T21（预算惯例）、T19.4（译码器子系统）。
- Produces: 讲义全文（阶段 6 首轮收官）。

**Step 1: 创作**——结构要求：
- 学习目标：接收链端到端集成（同步→估计→均衡→软解调→译码）与资源/功耗预算
- 内容章节：(1) 接收链子系统全景（T2.x 算法 → T22 工程）(2) 数据流与接口（各子系统间 LLR/信道矩阵传递）(3) 资源预算（乘法器/存储/功耗分摊）(4) 端到端定点误差预算（各环节误差分配）(5) 与译码器子系统（T19.4）集成
- numpy 验证例：端到端定点仿真（全链定点误差 vs 浮点 BER 对比）
- 例题：误差预算分配 / 资源分摊
- 图：≥1（接收链集成全景 Mermaid）
- 协议锚点：TS 38.211 综合

**Step 2/3**: 验证与提交。

---

### Task T22.5: 同步清单

**Files:**
- Modify: `3gpp/docs/L3_工程实现/L3_工程实现入口.md`（新增 M17 模块：4 篇登记）
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（如有新术语）
- Modify: `3gpp/项目规则与记忆索引.md` 第五节（L3 M17/T22 编号登记）

**Step 1**: L3 入口新增模块；编号规则登记。**Step 2**: 提交。

---

### Task T22.6: 全量验证

8 项审计全库运行，修复 FAIL，提交。

---

### Task T22.7: 双推 + 阶段 6 首轮收官登记

工作区干净确认；`git push origin master` 双远端；阶段 6 首轮收官声明（接收链子系统 4 篇；阶段 6 后续：后端/DFT/功耗深化、软硬件协同）。

---

## 自审记录

- 规格覆盖：阶段 6（G11 首轮）——Modem 接收链子系统工程 4 篇（同步/估计、均衡、软解调、集成预算），与 spec"Modem 子系统仿真/RTL"一致。
- 编号：L3 T22.x（T16-T21 已用）+ 模块 M17（L3 M17+ 规则）。
- 前置：L1 T2.x 算法 + L3 T17-T20 工程惯例（golden model/定点/RTL）——工程系列的自然延续。
- 教训前置：习题 ≤3/类、行数内容充实、`\|` 禁、numpy 实跑后贴入、无自纠错。
- 验收闭环：audit_term_first_use 全绿 + 8 项全量审计 + 本地 Rel-19 数值核验。
