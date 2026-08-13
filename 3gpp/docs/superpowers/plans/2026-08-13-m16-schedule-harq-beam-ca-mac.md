# M16 调度/HARQ/波束/CA/MAC 讲义 Implementation Plan（阶段 5）

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按全链路规划阶段 5（G3+G7+G8+G9 讲义级）：M16 系列 4 篇完整讲义（M16.1-M16.4，每篇内容充实即可——≥500 为下限参考、上限不限、深度不足合并），调度/HARQ/波束/CA/MAC 从概念笔记升级为完整讲义。

**Architecture:** 依拷问锁定版 `docs/superpowers/specs/2026-08-11-full-link-knowledge-map.md` 阶段 5 执行（G3/G7/G8/G9 落 L2 M14+）。**批次构成：4 篇讲义一轮（用户裁定，2026-08-13）**——G6 参考信号与 G10 射频的概念笔记已齐（核对确认），本批仅讲义。8 任务：M16.1-M16.4（4 篇讲义）+ M16.5（同步清单）+ M16.6（全量验证）+ M16.7（双推）。子代理配额已尽——主会话直接创作 + 自审（用户已批准）。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- **讲义模板**（.claude/rules/documentation.md §二）：frontmatter（type: algorithm + aliases + tags 含 l2 + source_spec）→ 本节学习目标（6-8 条可检验 bullets）→ 前置知识检查（表格）→ 内容章节（LaTeX \tag 公式、表格、生活类比、数值实例）→ 示范例题/引导练习/独立习题（附答案）→ 小结（指向下一篇）。
- **例题数量上限（用户确立，强制）**：示范例题、引导练习、独立习题**每类 ≤3、全篇 ≤9**——禁止用习题凑行数。
- **行数**：≥500 为下限参考、内容充实即可；上限不限（内容与主题允许可远超 500）；话题深度不足时**合并**而非注水（2026-08-13 用户裁定）。
- **写作规范**：正文无中间过程叙述；概念首现讲解 + wikilink 概念笔记；手算与 numpy 一致；每篇 ≥1 生活类比；英文术语首现「ABBR（中文，English Full Name）」（audit_term_first_use 全绿硬验收）；带圈数字禁令；标题正式化（禁"为什么/怎么"口语词）；wikilink 管道用普通 `|`；习题插入按编号顺序。
- **每篇硬件要求**：≥1 教学图（复杂图手绘 SVG 过 audit_svg_layout R1-R11 + cairosvg；简单流程 Mermaid 过 audit_mermaid_syntax.sh，节点带括号用引号节点）；1 个内嵌 numpy 验证（实跑断言通过后原样贴入输出，禁止编造）。
- **概念笔记底座**：11 篇相关概念笔记（Scheduler/HARQ_Process/Beam_Management/Carrier_Aggregation/BWP/MAC_Layer_Mapping 等）已齐——讲义与笔记双向链接。
- **前置讲义锚点**：M16.1 锚 T14.2（DCI 字段）/T15.3（SRS 频选）/T15.4（PHR 调度联动）；M16.2 锚 T14.4（SSB 波束）/T15.3（SRS 波束）；M16.3 锚 T14.1（跨载波调度）/T14.2（载波指示字段）；M16.4 锚 T9.0（descriptor）/T14.2（DCI 到 MAC 的衔接）。
- **协议锚点**：TS 38.214 §5.1.2（RBG/资源分配）、§5.1.3（MCS/TBS）；TS 38.321 §5.3（HARQ 进程）、§6.1（MAC PDU）；TS 38.213 §5.2（波束管理）；TS 38.331（CA/BWP 配置）——数值对照本地 `3GPP_Rel19/processed/` 原文。
- 提交后 `git push origin master`（双推，阶段收尾统一执行）。

---

### Task M16.1: 讲义 M16.1 调度与 HARQ 进程

**Files:**
- Create: `3gpp/docs/L2_协议算法/M16.1_scheduler_HARQ_process.md`
- Create（如用图）: `3gpp/docs/L2_协议算法/assets/M16.1_*.svg` 或 Mermaid 内嵌

**Interfaces:**
- Consumes: `[[Scheduler_MAC调度器与资源分配]]`、`[[HARQ_Process_HARQ进程管理]]`、T14.2（DCI 字段）、T15.3（SRS 频选）。
- Produces: 讲义全文，M16.4 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：MAC 调度器的工作原理（资源分配 RBG/VRB、MCS 选择、频选/功控联动）、HARQ 进程状态机（NDI/k0/k1/k2、进程数与软合并）
- 内容章节：(1) 调度器在协议栈的位置（MAC 层，descriptor 的消费者）(2) 资源分配（RBG/VRB，38.214 §5.1.2）(3) MCS 选择链（SRS 测量 → SINR → MCS 表）(4) HARQ 进程状态机（38.321 §5.3：NDI 翻转/进程数/软合并）(5) 调度与功控联动（PHR → 调度空间）(6) 接收端视角（descriptor 重建 → 译码）
- numpy 验证例：HARQ 进程状态机仿真（N 进程轮转、NDI 翻转判定新传/重传、软合并增益）
- 例题：RBG 分配计算 / HARQ 进程时序
- 图：≥1（调度-译码-反馈闭环 Mermaid 或 HARQ 进程时序）
- 协议锚点：TS 38.214 §5.1.2/§5.1.3、TS 38.321 §5.3

**Step 2/3**: 验证与提交（同 TX：audit_term_first_use 全绿 + circled_digits + latex + headings + link_integrity + mermaid/svg + numpy 实跑；提交含资产）。

---

### Task M16.2: 讲义 M16.2 波束管理

**Files:**
- Create: `3gpp/docs/L2_协议算法/M16.2_beam_management.md`

**Interfaces:**
- Consumes: `[[Beam_Management_波束管理]]`、`[[Beam_Coherence_波束相干理论]]`、T14.4（SSB 波束）、T15.3（SRS 波束）。
- Produces: 讲义全文，M16 系列衔接。

**Step 1: 创作**——结构要求：
- 学习目标：波束管理流程（初始波束获取 → 波束细化 → 波束切换/失败恢复）、SSB/CSI-RS 波束测量与 L1-RSRP、TCI 状态与 QCL（准共址，Quasi-Co-Location）、BFR
- 内容章节：(1) 波束管理的三个阶段（P1/P2/P3）(2) SSB 波束扫射与测量（T14.4 衔接）(3) CSI-RS 波束细化（38.213 §5.2）(4) TCI/QCL（TypeD 空间参数，38.214 §6.1.1）(5) 波束失败恢复（BFR 流程）(6) 与波束相干理论衔接（角度域）
- numpy 验证例：波束扫描仿真（ULA 方向图扫描，选最大 RSRP 波束）
- 例题：TCI 状态配置 / BFR 时序
- 图：≥1（P1/P2/P3 流程 Mermaid）
- 协议锚点：TS 38.213 §5.2、TS 38.214 §6.1.1

**Step 2/3**: 验证与提交。

---

### Task M16.3: 讲义 M16.3 载波聚合与 BWP

**Files:**
- Create: `3gpp/docs/L2_协议算法/M16.3_CA_BWP.md`

**Interfaces:**
- Consumes: `[[Carrier_Aggregation_载波聚合]]`、`[[BWP_带宽部分]]`、T14.1（跨载波调度）、T14.2（载波指示/BWP 指示字段）。
- Produces: 讲义全文，M16 系列衔接。

**Step 1: 创作**——结构要求：
- 学习目标：载波聚合（CC/SCell/跨载波调度/多载波 HARQ）、BWP 机制（BWP 切换/休眠/带宽适配）
- 内容章节：(1) CA 的动机与结构（PCell/SCell、CC 数）(2) 跨载波调度（CIF 字段，T14.2 衔接）(3) 多载波 HARQ（每 CC 独立进程）(4) BWP 概念与切换（38.331 BWP-Config）(5) BWP 休眠与省电（DRX 衔接）(6) 接收端视角（每 BWP 的调度解释）
- numpy 验证例：多 CC 的 HARQ 时序仿真（每 CC 独立 k1）+ BWP 切换对带宽/功率的影响计算
- 例题：CIF 跨载波调度解析 / BWP 切换计算
- 图：≥1（CA 结构 Mermaid 或 BWP 切换时序）
- 协议锚点：TS 38.213 §12（多载波）、TS 38.331 BWP-Config/CA 配置

**Step 2/3**: 验证与提交。

---

### Task M16.4: 讲义 M16.4 MAC 层映射

**Files:**
- Create: `3gpp/docs/L2_协议算法/M16.4_MAC_layer_mapping.md`

**Interfaces:**
- Consumes: `[[MAC_Layer_Mapping_MAC层映射]]`、T9.0（descriptor）、T14.2（DCI 到 MAC 衔接）。
- Produces: 讲义全文（阶段 5 收官）。

**Step 1: 创作**——结构要求：
- 学习目标：逻辑信道 → 传输信道 → 物理信道映射、MAC PDU 结构与复用、调度与 HARQ 在 MAC 层的落地
- 内容章节：(1) 信道映射全景（逻辑/传输/物理三层）(2) MAC PDU 结构（38.321 §6.1：MAC header/subheader/LCE）(3) 复用与优先级（逻辑信道优先级）(4) 调度在 MAC 的落地（descriptor → 传输）(5) 接收端 MAC 解析（PDU 拆解）
- numpy 验证例：MAC PDU 组装/解析仿真（header+payload 位操作往返）
- 例题：MAC subheader 解析
- 图：≥1（三层信道映射 Mermaid）
- 协议锚点：TS 38.321 §6.1/§5.3、TS 38.300 §6.4

**Step 2/3**: 验证与提交。

---

### Task M16.5: 同步清单

**Files:**
- Modify: `3gpp/docs/L2_协议算法/L2_协议算法入口.md`（新增 M16 模块章节：4 篇讲义登记）
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（如有新术语登记）
- Modify: `3gpp/docs/audits/image_asset_inventory.md`（如有 SVG 资产登记）

**Step 1**: L2 入口新增 `## M16 调度与系统体系（阶段 5）` 模块；概念笔记回链核对（Scheduler/HARQ_Process/Beam_Management/Carrier_Aggregation/BWP/MAC_Layer_Mapping 补 M16 讲义链接）。

**Step 2**: 提交。

---

### Task M16.6: 全量验证

**Files:** 无新增；FAIL 修复。

**Step 1**: 全量审计（8 项）：
```bash
cd 3gpp && python3 tools/audit_term_first_use.py docs/L1_基础 docs/L2_协议算法 docs/L3_工程实现 && python3 tools/audit_circled_digits.py && python3 tools/audit_lesson_terms.py docs && python3 tools/audit_markdown_headings.py docs && python3 tools/audit_latex_render.py --syntax-only docs && python3 tools/audit_link_integrity.py && bash tools/audit_mermaid_syntax.sh docs && bash tools/audit_plantuml_syntax.sh docs 2>/dev/null || true
```
**Step 2**: 修复 FAIL 复跑。**Step 3**: 提交。

---

### Task M16.7: 双推 + 阶段 5 收官登记

**Step 1**: 工作区干净确认。**Step 2**: `git push origin master` 双远端确认。**Step 3**: 阶段 5 收官声明（M16 系列 4 篇完成；下一步阶段 6 远期：Modem 子系统仿真/RTL）。

---

## 自审记录

- 规格覆盖：阶段 5（G3+G7+G8+G9 讲义级）定义落地——调度/HARQ、波束、CA/BWP、MAC 映射 4 篇，与用户裁定"4 篇讲义一轮"一致；G6 参考信号与 G10 射频概念笔记已齐（核对确认，本批不涉及）。
- 编号：L2 M16（M16+ 规则；M16 空闲核对）。
- 概念笔记底座 11 篇已就绪，双向链接。
- 教训前置：习题 ≤3/类、行数内容充实即可（≥500 参考）、`\|` 转义管道禁用、习题顺序插入校验、numpy 输出实跑后原样贴入、无自纠错叙述。
- 验收闭环：audit_term_first_use 全绿硬验收 + 8 项全量审计 + 本地 Rel-19 原文数值核验。
