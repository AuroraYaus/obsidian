---
type: spec
aliases:
  - 3GPP 项目 CLAUDE 指南
  - 3GPP 执行规范
tags:
  - 3gpp
  - claude
  - policy
source_spec: "Local project instructions"
---

# 3GPP 项目 CLAUDE.md

## 硬性规则

### 1. SKILL 优先检查（最高优先级）

**每次收到用户请求后，第一步必须检查可用 SKILL 列表，判断是否有匹配的 SKILL。**

匹配即调用——在生成任何其他回复之前，先用 Skill 工具调用匹配的 SKILL。

常见匹配场景：
- 审查代码 → `code-review` 或 `superpowers:requesting-code-review`
- 修复/精简代码 → `simplify`
- 创建功能/修改行为 → `superpowers:brainstorming`
- 深度调研 → `deep-research`
- 编写计划 → `superpowers:writing-plans`
- 执行计划 → `superpowers:executing-plans`
- 调试 → `superpowers:systematic-debugging`
- TDD → `superpowers:test-driven-development`
- 处理 PDF → `document-skills:pdf`
- 处理 Word → `document-skills:docx`
- 任务规划 → `planning-with-files:planning-with-files`
- 创建新 SKILL → `example-skills:skill-creator`
- 配置修改 → `update-config`
- 完成开发分支 → `superpowers:finishing-a-development-branch`

违反此规则是本次会话中已确认的已知问题，必须杜绝。

### 2. 项目背景

本项目是 3GPP LTE/NR 译码链路的全栈教学工程，包含：
- `docs/` — 94 篇讲义（L1 基础 → L2 协议/算法 → L3 工程）
- `sim/` — Python 仿真（CRC/GF(2) 等）
- `tools/` — 审计/抽取/渲染工具链
- `3GPP_Rel19/` — 协议原始资料和结构化抽取

### 3. 强制 DOXYGEN 风格注释（知识库红线）

**本项目是教学知识库，代码可读性优先于功能正确性。** 所有 Python 脚本、Shell 脚本、配置文件中的函数/类/任务入口必须使用完整的 DOXYGEN 风格注释：
- 文件头：`@file` + `@brief` + `@date`
- 函数：`@brief` + `@param` + `@return` + `@note` + `@throws`（按需）
- 脚本入口：`@brief` + `@usage` + `@args` + `@env` + `@exit_code`

代码审查时注释质量与功能正确性同等权重。详见 `.claude/rules/documentation.md`（项目根级规则）。

### 4. SVG 图生成后强制视觉验证

**任何 SVG 图（含手写、Python 生成、Mermaid/PlantUML 渲染）生成后，必须先验证再嵌入文档，禁止直接提交。**

验证步骤：
1. **Y 坐标扫描**（必须）：提取所有 `<text>`、`<rect>`、`<line>` 的 y 坐标，逐层核对间距 ≥ 8 px
2. **边界间距检查**（必须，可用 `tools/audit_svg_layout.py` 的 R6 规则）：文本框边界与**框外文字**（含 class="free" 的框外标注）及其他文本框边界保持适当距离（投影间距 ≥ 8 px）——文字不能紧贴其他文本框的边
3. **PNG 预览**（推荐）：`cairosvg` 或 ImageMagick `convert` 转 PNG，肉眼确认无交叠
4. 确认通过后才能写入 `docs/L1_基础/assets/` 并在正文引用

**教训来源**：
- 2026-07-23 生成的 circular buffer 交错图因未做坐标扫描，箭头说明文字、分隔标签、目标格子挤在 4 px 范围内，用户立即发现文字交叠。详见 `memory/svg-render-verify-before-commit.md`。
- 2026-08-04 T2.14 图 3 的"仿真验证：同时跑"文字与上方文本框边界仅约 2 px——框外文字必须与文本框边界留出 ≥ 8 px 间距，已固化为审计工具 R6 规则。

### 5. 合规基线

所有讲义和代码必须遵守 `合规与遵从.md` 中的 22 条 Hard Constraints。关键规则：
- 标题口语化禁止（Rule 16）
- 英文术语不能裸奔，首现必须"中文（English）"（Rule 10）
- 3GPP/LTE/NR 不机械重复全称（Rule 15）
- LaTeX 公式必须可渲染（Rule 20）
- 零基础保护（Rule 8）
