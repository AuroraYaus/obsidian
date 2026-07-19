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

### 3. 合规基线

所有讲义和代码必须遵守 `合规与遵从.md` 中的 22 条 Hard Constraints。关键规则：
- 标题口语化禁止（Rule 16）
- 英文术语不能裸奔，首现必须"中文（English）"（Rule 10）
- 3GPP/LTE/NR 不机械重复全称（Rule 15）
- LaTeX 公式必须可渲染（Rule 20）
- 零基础保护（Rule 8）
