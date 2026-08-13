# M14 控制信道族深化讲义 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按全链路规划阶段 2：M14 控制信道族 5 篇完整讲义（T14.1-T14.5，每篇 500-800 行），控制面从概念笔记升级为完整讲义。

**Architecture:** 按拷问锁定版 `docs/superpowers/plans/PLAN-m14-control-plane.md` 执行。8 任务：M14.1-M14.5（5 篇讲义）+ M14.6（同步清单）+ M14.7（全量验证）+ M14.8（双推）。每篇讲义为创作型任务——brief 给出结构要求、内容大纲、验证要求，implementer 创作全文。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- **讲义模板**（.claude/rules/documentation.md §二）：frontmatter（type: algorithm + aliases + tags 含 l2 + source_spec）→ `# T14.x 中文标题` → 本节学习目标（叙事 intro + 6-8 条可检验 bullets，动词开头）→ 前置知识检查（表格 `| 前置项 | 本节需要达到的程度 |`）→ 内容章节（LaTeX \tag 编号公式、表格、生活类比、数值实例）→ 示范例题（完整解题过程）/ 引导练习（带提示）/ 独立习题（附参考答案）→ 小结（收束 + 指向下一篇）。
- **写作规范**：正文不得含代码中间运行结果；概念首现必须讲解（名称+定义+一句解释 + [[wikilink]] 概念笔记）；手算数值与 numpy 独立重算一致；每篇 ≥1 生活类比；英文术语首现「ABBR（中文，English Full Name）」（audit_term_first_use 全绿为硬验收）；带圈数字禁令；标题正式化。
- **每篇硬件要求**：500-800 行；≥1 教学图（复杂图手绘 SVG 入 L2 资产目录并过 `tools/audit_svg_layout.py` R1-R11 + cairosvg 预览；简单流程 Mermaid 过 `bash tools/audit_mermaid_syntax.sh`）；1 个内嵌 numpy 验证（先实跑断言通过再写入正文，输出与断言一致）。
- **概念笔记底座**：6 篇控制面概念笔记（PDCCH/DCI/PUCCH/PBCH/TBCC/PSS_SSS）为内容与 wikilink 底座——讲义与笔记双向链接。
- **前置讲义锚点**：T14.1 锚 T10（Polar 控制译码）/T9.0（descriptor）；T14.2 锚 T9.0/T2.5；T14.3 锚 T7.5/T9.8；T14.4 锚 T2.7/T2.8；T14.5 锚 T6（Turbo 对照）。
- 工具缺失（mmdc/cairosvg/KaTeX）显式声明验证缺口。
- 提交后 `git push origin master`（双推，阶段收尾统一执行）。

---

### Task M14.1: 讲义 T14.1 PDCCH 盲检

**Files:**
- Create: `3gpp/docs/L2_协议算法/T14.1_PDCCH_blind_decoding.md`
- Create（如用图）: `3gpp/docs/L2_协议算法/assets/T14.1_*.svg` 或 Mermaid 内嵌

**Interfaces:**
- Consumes: 概念笔记 `[[PDCCH_物理下行控制信道]]`、讲义 T10.6/T10.8（Polar 控制译码）、T9.0（descriptor）。
- Produces: 讲义全文（500-800 行），T14.2 的前置依赖。

**Step 1: 创作讲义**——结构要求：
- 学习目标：PDCCH 承载 DCI 的完整机制（CORESET 时频结构/REG/CCE 聚合/搜索空间/盲检流程/RNTI 机制/盲检复杂度）
- 内容章节建议：① 为什么需要盲检（无寻址信道的试错设计）② CORESET/REG/CCE 与聚合等级（含 38.211 §7.3.2 结构）③ 搜索空间与监测时机（CSS/USS、monitor occasion）④ 盲检流程与 RNTI 机制（含 38.213 §10）⑤ 盲检复杂度分析（候选数×RNTI×DCI 大小）⑥ 接收端实现视角（Polar 译码 + CRC/RNTI 校验 + T10.6 衔接）
- numpy 验证例：给定聚合等级候选数（1/2/4/8/16 的候选计数表），计算一个监测时机的总盲检候选数，与协议表核对
- 例题：聚合等级 8 的含义与 CCE 位置计算
- 图：≥1——建议手绘 SVG（盲检流程状态图或 CCE 聚合示意）
- 协议锚点：TS 38.213 §10、TS 38.211 §7.3.2、TS 38.321（RNTI）

**Step 2: 验证**：`cd 3gpp && python3 tools/audit_term_first_use.py docs/L2_协议算法/T14.1_PDCCH_blind_decoding.md`（全绿）+ audit_circled_digits + audit_latex_render --syntax-only + audit_markdown_headings + audit_link_integrity + mermaid/svg 按图类型 + numpy 验证实跑。

**Step 3: 提交**（含资产）。

---

### Task M14.2: 讲义 T14.2 DCI 格式精读

**Files:**
- Create: `3gpp/docs/L2_协议算法/T14.2_DCI_format_detailed.md`

**Interfaces:**
- Consumes: `[[DCI_下行控制信息]]`、T9.0、T2.5（MCS/TBS）。
- Produces: 讲义全文，T14.3 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：DCI 格式体系（0_0/0_1/1_0/1_1/2_0-2_3）与核心字段语义、DCI→descriptor 映射、DCI 大小与盲检的关系
- 内容章节：① DCI 格式概览（38.212 §7.3）② 1_1 下行调度字段逐项（频域/时域/MCS/HARQ/NDI/RV/TPC/DAI 等）③ 0_1 上行调度字段差异 ④ 回退格式 0_0/1_0 ⑤ 2_x 组公共格式 ⑥ DCI→descriptor 完整映射（T9.0 深化）
- numpy 验证例：从 MCS 索引+RB 数计算 TBS（T9.0 公式复核）或 DCI 字段位宽求和
- 例题：解析一个 1_1 DCI 的字段到 descriptor
- 图：≥1（DCI 字段结构图或映射流程）
- 协议锚点：TS 38.212 §7.3、TS 38.214 §5.1

**Step 2/3**: 验证与提交（同 M14.1）。

---

### Task M14.3: 讲义 T14.3 PUCCH 与 UCI

**Files:**
- Create: `3gpp/docs/L2_协议算法/T14.3_PUCCH_UCI_formats.md`

**Interfaces:**
- Consumes: `[[PUCCH_上行控制信道与UCI]]`、T7.5（DL/UL 差异）、T9.8（CBG）、T10.9（UCI 交织）。
- Produces: 讲义全文，T14.4 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：UCI 三兄弟（HARQ-ACK/SR/CSI）、PUCCH format 0-4 划分逻辑、UCI 承载选择（PUCCH vs PUSCH）、HARQ-ACK 时序（k1）
- 内容章节：① UCI 内容与优先级 ② format 0-4 结构（38.213 §9，短/长/容量）③ 序列选择与 DMRS 辅助 ④ UCI 复用与 PUSCH 承载（T10.9 衔接）⑤ k1 时序链 ⑥ 资源分配（PUCCH resource set + indicator）
- numpy 验证例：format 容量计算（符号数×RB×调制）或 k1 时序链 slot 计算
- 例题：给定 HARQ-ACK 负载选 format
- 图：≥1（format 0-4 对照或 k1 时序图）
- 协议锚点：TS 38.213 §9、TS 38.212 §6.3

**Step 2/3**: 验证与提交。

---

### Task M14.4: 讲义 T14.4 小区搜索与系统信息（PBCH）

**Files:**
- Create: `3gpp/docs/L2_协议算法/T14.4_PBCH_cell_search_system_info.md`

**Interfaces:**
- Consumes: `[[PBCH_MIB_广播信道]]`、`[[PSS_SSS_同步信号与小区搜索]]`、T2.7/T2.8（同步）、T10（Polar 控制译码）、TBCC 笔记。
- Produces: 讲义全文，T14.5 的前置（LTE 侧）。

**Step 1: 创作**——结构要求：
- 学习目标：小区搜索全流程（同步栅格→PSS/SSS→小区 ID→PBCH→MIB→SIB1）、PBCH 编码（NR Polar/LTE TBCC）、MIB/SIB 层级
- 内容章节：① 小区搜索流程总览（GSCN→SSB→PBCH 链路）② PSS/SSS 与小区 ID ③ PBCH 结构与编码（38.212 §7.1 Polar；LTE 36.212 TBCC）④ MIB 字段精读（38.331 §6.2.2）⑤ SIB1 与系统信息层级（pdcch-ConfigSIB1→SIB1→其他 SIB）⑥ 接收端流程（T2.7/T2.8 同步衔接）
- numpy 验证例：小区 ID 推导（PSS/SSS 索引组合）或 PBCH 载荷→Polar 编码长度计算
- 例题：GSCN→频点→SSB 位置推算
- 图：≥1（小区搜索流程 SVG 或 SSB 结构图）
- 协议锚点：TS 38.211 §7.4、TS 38.212 §7.1、TS 38.331 §6.2.2、TS 36.212 §5.1.3.1

**Step 2/3**: 验证与提交。

---

### Task M14.5: 讲义 T14.5 TBCC 译码

**Files:**
- Create: `3gpp/docs/L2_协议算法/T14.5_TBCC_decoding.md`

**Interfaces:**
- Consumes: `[[TBCC_咬尾卷积码]]`、T6（Turbo/BCJR 对照）、T1（GF2/概率基础）。
- Produces: 讲义全文（LTE 控制编码译码闭环）。

**Step 1: 创作**——结构要求：
- 学习目标：TBCC 咬尾机制、咬尾 Viterbi（硬判决）与 BCJR（软判决）译码、LTE 控制信道译码流程
- 内容章节：① TBCC 编码回顾（36.212 §5.1.3.1：K=7、g0/g1/g2、咬尾初始化）② 咬尾 Viterbi（环形网格、wrap-around 扫描）③ 咬尾 BCJR（环形前向后向）④ LTE PDCCH/PBCH 译码链路（速率匹配逆、RNTI 解扰衔接）⑤ 数值走读（小例子：K=3 或 K=7 短码）
- numpy 验证例：咬尾 Viterbi 小例实跑（给定接收序列求最大似然路径）或 BCJR LLR 计算
- 例题：咬尾初始化状态计算
- 图：≥1（咬尾网格图 SVG 或译码流程图）
- 协议锚点：TS 36.212 §5.1.3.1、TS 36.211 §6.8

**Step 2/3**: 验证与提交。

---

### Task M14.6: 同步清单

**Files:**
- Modify: `3gpp/docs/L2_协议算法/L2_协议算法入口.md`（新增 M14 模块章节：5 篇讲义登记）
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（如有新术语——核对：讲义引入的协议字段名不强制登记，新缩写需登记）
- Modify: `3gpp/docs/audits/image_asset_inventory.md`（如有 SVG 资产登记）

**Step 1**: L2 入口新增 `## M14 控制信道族（阶段 2）` 模块（5 篇列表 + 一句话定位）；概念笔记回链核对（6 篇控制面笔记图谱关联已含讲义链接——核对补全）。

**Step 2**: 提交。

---

### Task M14.7: 全量验证

**Files:** 无新增；FAIL 修复。

**Step 1**: 全量审计（8 项）：
```bash
cd 3gpp && python3 tools/audit_term_first_use.py docs/L1_基础 docs/L2_协议算法 docs/L3_工程实现 && python3 tools/audit_circled_digits.py && python3 tools/audit_lesson_terms.py docs && python3 tools/audit_markdown_headings.py docs && python3 tools/audit_latex_render.py --syntax-only docs && python3 tools/audit_link_integrity.py && bash tools/audit_mermaid_syntax.sh docs && bash tools/audit_plantuml_syntax.sh docs 2>/dev/null || true
```
**Step 2**: 修复 FAIL 复跑。**Step 3**: 提交。

---

### Task M14.8: 双推 + 阶段 2 收官登记

**Step 1**: 工作区干净确认。**Step 2**: `git push origin master` 双远端确认。**Step 3**: 阶段 2 收官声明（M14 控制信道族 5 篇完成；下一步阶段 3 上行链路）。

---

## 自审记录（writing-plans 内置 + grill-me 拷问合并）

- 规格覆盖：拷问决策 2 项全部落地——深化系列（控制信道族）→ M14.1-M14.5；批次规模（5 篇一轮）→ 8 任务结构。
- 讲义为创作型任务：brief 定义结构与验收（模板/规范/图/公式/numpy/锚点），全文由 implementer 创作——每篇 brief 需含本计划的「结构要求」节全部要点。
- 前置依赖链：M14.1→M14.2→M14.3→M14.4→M14.5（每篇锚定前置讲义与概念笔记）。
- 验收闭环：audit_term_first_use 全绿（治理工具现在作为讲义写作的自动验收——治理成果反哺写作流程）。
