# TX 发送端镜像讲义 Implementation Plan（阶段 4）

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按全链路规划阶段 4（G2 深化）：发送端镜像 5 篇完整讲义（TX1-TX5，每篇 500-800 行），发送链路从概念笔记升级为完整讲义系列，与 T2.x 接收链路形成镜像对照。

**Architecture:** 依拷问锁定版 `docs/superpowers/specs/2026-08-11-full-link-knowledge-map.md` 阶段 4 执行（发送端镜像依赖 T2.x 接收端逆过程对照）。**编号方案：TX 系列（用户裁定，2026-08-13）**——L1 已用 T1-T5、L2 占 T6-T15、L3 占 T16-T21，全库连续编号无剩余空间；TX 与全库零碰撞、与 TX_Chain 概念笔记呼应。8 任务：TX1-TX5（5 篇讲义）+ TX6（同步清单）+ TX7（全量验证）+ TX8（双推）。子代理配额已尽——主会话直接创作 + 自审（用户已批准）。

## Global Constraints

- 所有命令在仓库根 `/home/yys/AGENT/obsidian` 下以 `cd 3gpp && …` 运行。
- **讲义模板**（.claude/rules/documentation.md §二）：frontmatter（type: algorithm + aliases + tags 含 l1 + source_spec）→ `# TXn 中文标题` → 本节学习目标（叙事 intro + 6-8 条可检验 bullets）→ 前置知识检查（表格）→ 内容章节（LaTeX \tag 公式、表格、生活类比、数值实例）→ 示范例题/引导练习/独立习题（附答案）→ 小结（指向下一篇）。
- **写作规范**：正文无中间过程叙述（含自纠错）；概念首现讲解 + wikilink 概念笔记；手算与 numpy 一致；每篇 ≥1 生活类比；英文术语首现「ABBR（中文，English Full Name）」（audit_term_first_use 全绿硬验收）；带圈数字禁令；标题正式化（禁"为什么/怎么"口语词）；wikilink 管道用普通 `|`（禁 `\|`）；习题插入按编号顺序（教训：T14.5/T15 系列五次插错）。
- **每篇硬件要求**：500-800 行；≥1 教学图（复杂图手绘 SVG 过 `tools/audit_svg_layout.py` R1-R11 + cairosvg；简单流程 Mermaid 过 `bash tools/audit_mermaid_syntax.sh`，节点带括号用引号节点）；1 个内嵌 numpy 验证（实跑断言通过后原样贴入输出，**禁止编造输出**）。
- **概念笔记底座**：发送链路组概念笔记（Modulation_Mapping/RE_Mapping/Layer_Mapping/Precoding/Gold_序列加扰/TX_Chain 等）为内容与 wikilink 底座——讲义与笔记双向链接。
- **镜像对照**：每篇明确与 T2.x 接收链路的逆过程对照（TX1↔T2.13/T2.14 软解调、TX2↔T2.x 解扰、TX3↔T12 检测、TX4↔T2.x 资源格提取）。
- **协议锚点**：TS 38.211 §5.1（调制）/§6.3.1.1（加扰）/§6.3.1.3（层映射）/§6.3.1.5（预编码）/§5.3（RE 映射）——数值对照本地 `3GPP_Rel19/processed/` 原文。
- 提交后 `git push origin master`（双推，阶段收尾统一执行）。

---

### Task TX1: 讲义 TX1 调制映射（发送端星座映射）

**Files:**
- Create: `3gpp/docs/L1_基础/TX1_modulation_mapping.md`
- Create（如用图）: `3gpp/docs/L1_基础/assets/TX1_*.svg` 或 Mermaid 内嵌

**Interfaces:**
- Consumes: `[[Modulation_Mapping_调制映射]]`、T2.13/T2.14（软解调——逆过程对照）。
- Produces: 讲义全文，TX5 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：调制映射的发送端视角（比特 → 星座符号）、NR 调制族（BPSK/QPSK/16QAM/64QAM/256QAM + π/2-BPSK）、星座图与 Gray 映射、与软解调（T2.13/T2.14）的逆过程对照
- 内容章节：(1) 调制在发送链的位置（TX_Chain 概念笔记衔接）(2) 星座与 Gray 映射（38.211 §5.1，公式化）(3) 各调制阶数对照（Qm 与每符号比特）(4) 功率归一化（星座能量归一）(5) 与软解调的镜像（发送映射 vs 接收 LLR）(6) π/2-BPSK 的相位连续化
- numpy 验证例：QPSK/16QAM 星座映射 + 能量归一化 + 与软解调 LLR 的往返验证
- 例题：16QAM 星座映射手算
- 图：≥1（QPSK 星座图或调制家族对照 Mermaid）
- 协议锚点：TS 38.211 §5.1、TS 38.214 §5.1.3（MCS 表衔接）

**Step 2/3**: 验证与提交（同 M14/M15：audit_term_first_use 全绿 + circled_digits + latex + headings + link_integrity + mermaid/svg + numpy 实跑；提交含资产）。

---

### Task TX2: 讲义 TX2 加扰与交织

**Files:**
- Create: `3gpp/docs/L1_基础/TX2_scrambling_interleaving.md`

**Interfaces:**
- Consumes: `[[Gold_序列加扰]]`、T3.x（CRC/分段前置）。
- Produces: 讲义全文，TX5 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：加扰的伪随机序列（Gold 序列）生成、加扰的作用（小区间干扰随机化）、交织的作用（抗突发错误）、与接收端解扰/解交织的镜像
- 内容章节：(1) 为什么加扰（干扰随机化）(2) Gold 序列生成（38.211 §5.2.1，c_init 初始化）(3) 加扰位置与流程（38.211 §6.3.1.1）(4) 交织器结构（块交织，与速率匹配交织的区别）(5) 接收端镜像（解扰 LLR 符号处理）
- numpy 验证例：Gold 序列生成（给定 c_init 与标准公式）+ 加扰/解扰往返 + 交织/解交织往返
- 例题：c_init 计算与序列首项验证
- 图：≥1（加扰/交织流程 Mermaid）
- 协议锚点：TS 38.211 §5.2.1/§6.3.1.1

**Step 2/3**: 验证与提交。

---

### Task TX3: 讲义 TX3 层映射与预编码

**Files:**
- Create: `3gpp/docs/L1_基础/TX3_layer_mapping_precoding.md`

**Interfaces:**
- Consumes: `[[Layer_Mapping_层映射]]`、`[[Precoding_预编码]]`、T12（接收检测——逆过程对照）。
- Produces: 讲义全文，TX5 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：层映射（码字 → 层）规则（38.211 §6.3.1.3）、预编码矩阵（38.211 §6.3.1.5）、发送端 y=Wx 模型、与 T12 接收检测的镜像（y=Hx 的逆）
- 内容章节：(1) 码字/层/端口三概念（T12 衔接）(2) 层映射规则（单/双码字表）(3) 预编码模型（y=Wx，DFT 矩阵/码本）(4) 发送端 vs 接收端模型（y=Hx 全链路）(5) DM-RS 端口与预编码关联
- numpy 验证例：层映射（2 码字 → 4 层）+ 预编码矩阵乘 + 与 T12 检测的端到端往返（预编码 → 信道 → MMSE 检测）
- 例题：4 层预编码矩阵手算
- 图：≥1（码字→层→端口 Mermaid）
- 协议锚点：TS 38.211 §6.3.1.3/§6.3.1.5

**Step 2/3**: 验证与提交。

---

### Task TX4: 讲义 TX4 RE 映射与资源格

**Files:**
- Create: `3gpp/docs/L1_基础/TX4_re_mapping_resource_grid.md`

**Interfaces:**
- Consumes: `[[RE_Mapping_资源元素映射]]`、T2.0/T2.1（资源格接收——逆过程对照）。
- Produces: 讲义全文，TX5 的前置。

**Step 1: 创作**——结构要求：
- 学习目标：RE 映射规则（38.211 §6.3.1.6/6.3.1.7）、VRB→PRB 映射、资源格生成（发送端视角）、与接收端资源格提取的镜像
- 内容章节：(1) RE 映射在发送链的位置 (2) 符号→RE 的映射顺序（先频后时等）(3) VRB→PRB（交织/非交织）(4) 发送端资源格与接收端提取的对照（T2.x）(5) DM-RS/PTRS 的 RE 占位
- numpy 验证例：RE 映射仿真（符号块 → 资源格 → 提取往返）+ VRB→PRB 映射表
- 例题：映射顺序手算（符号索引 → RE 索引）
- 图：≥1（资源格发送端 Mermaid 或表格）
- 协议锚点：TS 38.211 §6.3.1.6/§6.3.1.7、§7.4.1.1（DM-RS 位置）

**Step 2/3**: 验证与提交。

---

### Task TX5: 讲义 TX5 发送端处理链总览

**Files:**
- Create: `3gpp/docs/L1_基础/TX5_tx_chain_overview.md`

**Interfaces:**
- Consumes: `[[TX_Chain_发送端处理链总览]]`、TX1-TX4、T2.x（接收链总览镜像）。
- Produces: 讲义全文（阶段 4 收官）。

**Step 1: 创作**——结构要求：
- 学习目标：发送端处理链全景（CRC → 分段 → 编码 → 速率匹配 → 加扰 → 调制 → 层映射 → 预编码 → RE 映射 → 波形生成），与接收链（T2.x）逐环节镜像对照
- 内容章节：(1) 发送链全景图（Mermaid 大图）(2) 逐环节对照表（发送 vs 接收镜像）(3) 编解码对称性（T3-T10 收束）(4) 物理信道谱系（PDSCH/PUSCH/PDCCH/PUCCH/PBCH 的发送差异）(5) 发送端实现视角（硬件流水线）
- numpy 验证例：发送链端到端仿真（比特 → 全链 → 接收全链 → 译码恢复）
- 例题：发送链某环节的输入输出走查
- 图：≥2（全景图 + 对照表）
- 协议锚点：TS 38.211 综合

**Step 2/3**: 验证与提交。

---

### Task TX6: 同步清单

**Files:**
- Modify: `3gpp/docs/L1_基础/L1_基础入口.md`（新增 TX 模块章节：5 篇讲义登记）
- Modify: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`（如有新术语登记）
- Modify: `3gpp/docs/audits/image_asset_inventory.md`（如有 SVG 资产登记）
- Modify: `3gpp/项目规则与记忆索引.md` 第五节（TX 编号登记 + L1 新系列说明）

**Step 1**: L1 入口新增 `## TX 发送端镜像（阶段 4）` 模块；概念笔记回链核对（发送链路组补 TX 讲义链接）；编号规则登记。

**Step 2**: 提交。

---

### Task TX7: 全量验证

**Files:** 无新增；FAIL 修复。

**Step 1**: 全量审计（8 项）：
```bash
cd 3gpp && python3 tools/audit_term_first_use.py docs/L1_基础 docs/L2_协议算法 docs/L3_工程实现 && python3 tools/audit_circled_digits.py && python3 tools/audit_lesson_terms.py docs && python3 tools/audit_markdown_headings.py docs && python3 tools/audit_latex_render.py --syntax-only docs && python3 tools/audit_link_integrity.py && bash tools/audit_mermaid_syntax.sh docs && bash tools/audit_plantuml_syntax.sh docs 2>/dev/null || true
```
**Step 2**: 修复 FAIL 复跑。**Step 3**: 提交。

---

### Task TX8: 双推 + 阶段 4 收官登记

**Step 1**: 工作区干净确认。**Step 2**: `git push origin master` 双远端确认。**Step 3**: 阶段 4 收官声明（TX 系列 5 篇完成；下一步阶段 5：调度/HARQ、参考信号、波束、CA/BWP、MAC 映射、射频前端）。

---

## 自审记录

- 规格覆盖：阶段 4（G2 深化）定义落地——调制映射/RE 映射/加扰交织/物理信道谱系 5 篇，与 spec 的"4-5 篇"一致（取 5 篇，含发送链总览）。
- 编号方案：TX 系列（用户裁定）——与全库 T1-T21 零碰撞，与 TX_Chain 概念笔记呼应；TX6 任务登记规则索引第五节。
- 镜像对照：每篇锚定 T2.x 接收链路逆过程（TX1↔软解调、TX2↔解扰、TX3↔检测、TX4↔资源格提取、TX5↔接收链总览）——"发送端镜像"的核心是双向对照。
- 概念笔记底座：发送链路组 6 篇概念笔记已就绪（Modulation/RE/Layer/Precoding/Gold/TX_Chain），双向链接。
- 教训前置：`\|` 转义管道禁用、习题顺序插入校验、numpy 输出实跑后原样贴入、无自纠错叙述（T14/T15 系列全部教训）。
- 验收闭环：audit_term_first_use 全绿硬验收 + 8 项全量审计 + 本地 Rel-19 原文数值核验。
