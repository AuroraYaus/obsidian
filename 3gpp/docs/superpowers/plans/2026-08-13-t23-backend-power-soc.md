# T23 后端物理实现与软硬件协同讲义 Implementation Plan（阶段 6 后续）

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按全链路规划阶段 6 后续（G11 后端/DFT/功耗/软硬件协同）：T23 系列 3 篇完整讲义（T23.1-T23.3，L3），把译码器 RTL（T17-T20）与接收链工程（T22）升级到后端实现层。

**Architecture:** 依 spec 阶段 6（"后端物理实现/DFT/功耗深化/软硬件协同"）执行。**批次构成：3 篇一轮（按推荐决策执行）**——综合与后端、功耗深化、软硬件协同。L3 编号：T23.x（T22 已用，T23 空闲）。6 任务：T23.1-T23.3 + 同步 + 全量验证 + 双推。子代理配额已尽——主会话直接创作 + 自审。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- **讲义模板**：frontmatter（type: algorithm + aliases + tags 含 l3 + source_spec）→ 学习目标（6-8 条 bullets）→ 前置知识检查 → 内容章节（\tag 公式、表格、生活类比、数值实例）→ 示范例题/引导练习/独立习题（附答案）→ 小结。
- **例题数量上限**：每类 ≤3、全篇 ≤9。
- **行数**：≥500 为参考、内容充实即可、上限不限、深度不足合并。
- **写作规范**：正文无中间过程叙述；概念首现讲解 + wikilink；手算与 numpy 一致；每篇 ≥1 生活类比；英文术语首现「ABBR（中文，English Full Name）」；带圈数字禁令；标题正式化；wikilink 管道用 `|`；习题按编号顺序。
- **每篇硬件要求**：≥1 教学图（SVG 过 audit_svg_layout R1-R11 + cairosvg 或 Mermaid 过 audit_mermaid_syntax.sh）；1 个内嵌 numpy 验证（实跑后原样贴入）。
- **前置锚点**：T23.x 锚 T17-T20（RTL/验证）、T22（接收链工程）、T21（预算）。
- 提交后 `git push origin master`（双推，阶段收尾统一执行）。

---

### Task T23.1: 讲义 T23.1 综合与后端物理实现

**Files:**
- Create: `3gpp/docs/L3_工程实现/T23.1_synthesis_backend_physical.md`

**Interfaces:**
- Consumes: T19.x（RTL 微架构）、T20.x（验证）。
- Produces: 讲义全文，T23.3 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：RTL → 综合 → 布局布线的后端流程（时序/面积/功耗约束、DFT 插入）
- 内容章节：(1) 后端流程全景（综合/布局布线/时序收敛）(2) 综合（RTL → 门级网表、时序约束）(3) DFT 插入（扫描链/ATPG，可测性设计）(4) 布局布线与时序收敛（关键路径）(5) 物理验证（DRC/LVS）
- numpy 验证例：关键路径时延统计（组合逻辑链时延分布）或扫描链插入的覆盖率计算
- 例题：时序约束 / DFT 覆盖率
- 图：≥1（后端流程 Mermaid）
- 协议锚点：工程方法（非 3GPP 协议）

**Step 2/3**: 验证与提交。

---

### Task T23.2: 讲义 T23.2 功耗深化

**Files:**
- Create: `3gpp/docs/L3_工程实现/T23.2_power_deep_dive.md`

**Interfaces:**
- Consumes: T19.5（HARQ 存储）、T22.4（资源预算）、T21（预算惯例）。
- Produces: 讲义全文，T23.3 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：译码器与接收链的功耗构成（动态/静态）、低功耗技术（时钟门控/DVFS/电压域）
- 内容章节：(1) 功耗构成（动态 P=αCV²f、静态泄漏）(2) 译码器的功耗热点（迭代/存储访问）(3) 低功耗技术（时钟门控/操作数隔离/DVFS）(4) 存储功耗（软缓存/寄存器堆）(5) 功耗预算与降耗策略（T22.4 衔接）
- numpy 验证例：功耗模型计算（动态功耗 vs 频率/电压）或时钟门控的功耗节省
- 例题：功耗计算 / 门控收益
- 图：≥1（功耗构成 Mermaid 或表格）
- 协议锚点：工程方法

**Step 2/3**: 验证与提交。

---

### Task T23.3: 讲义 T23.3 软硬件协同

**Files:**
- Create: `3gpp/docs/L3_工程实现/T23.3_sw_hw_co_design.md`

**Interfaces:**
- Consumes: T19.6（寄存器配置）、T22.1-T22.4（接收链）、T23.1/T23.2。
- Produces: 讲义全文（阶段 6 收官）。

**Step 1: 创作**——结构要求：
- 学习目标：接收链/译码器的软硬件划分（固件调度、硬件加速器、寄存器接口）
- 内容章节：(1) 软硬件划分原则（控制面软、数据面硬）(2) 固件架构（调度/配置/中断）(3) 硬件加速器接口（DMA/寄存器/中断）(4) 接收链任务调度（同步→估计→均衡→译码的流水调度）(5) 软硬件协同调试（T20 验证衔接）
- numpy 验证例：任务调度仿真（流水线利用率）或软硬划分的时延对比
- 例题：划分决策 / 调度时延
- 图：≥1（软硬件架构 Mermaid）
- 协议锚点：TS 38.213（时序链，k1 等）

**Step 2/3**: 验证与提交。

---

### Task T23.4: 同步清单

**Files:**
- Modify: `3gpp/docs/L3_工程实现/L3_工程实现入口.md`（M17 模块扩展：T23 三篇登记）
- Modify: `3gpp/项目规则与记忆索引.md` 第五节（T23 编号登记）

**Step 1**: 入口与编号登记。**Step 2**: 提交。

---

### Task T23.5: 全量验证

8 项审计全库运行，修复 FAIL，提交。

---

### Task T23.6: 双推 + 阶段 6 收官登记

工作区干净确认；`git push origin master` 双远端；阶段 6 收官声明（T22+T23 七篇完成；全链路规划阶段 0-6 全部收官）。

---

## 自审记录

- 规格覆盖：阶段 6 后续（G11 后端/DFT/功耗/软硬件协同）——综合后端、功耗、软硬件协同 3 篇，与 spec 一致。
- 编号：L3 T23.x（空闲核对）。
- 前置：T17-T20（RTL/验证）、T22（接收链）、T21（预算）——工程系列的自然延续。
- 教训前置：习题 ≤3/类、行数内容充实、`\|` 禁、numpy 实跑后贴入、无自纠错。
- 验收闭环：audit_term_first_use 全绿 + 8 项全量审计。
