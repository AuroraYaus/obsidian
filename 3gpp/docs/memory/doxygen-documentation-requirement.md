---
name: doxygen-documentation-requirement
description: 所有代码必须使用 DOXYGEN 风格注释 — 知识库项目强制规范
metadata: 
  node_type: memory
  type: project
  originSessionId: 17b3a171-8663-4b2b-99ff-28a451ae67b7
---

本项目（AGENT/obsidian）是面向新手的 Digital IC 知识库。所有代码（脚本、函数、类、任务）**必须**使用完整的 DOXYGEN 风格注释，包括 `@brief`、`@param`、`@return`、`@note`、`@warning`、`@see` 等标签。脚本入口还需要 `@usage`、`@args`、`@env`、`@exit_code`。

**Why:** 知识库的第一优先级是教学可读性，代码无解释对新手极其不友好。DOXYGEN 是业界标准文档格式，新手在工程中必然遇到。

**How to apply:**
- 写任何代码前先写 DOXYGEN 注释头
- 每个文件必须有 `@file` 头
- 每个函数/方法必须有 `@brief` + `@param` + `@return`
- 代码审查时注释质量与功能正确性同等权重
- 详见 `.claude/rules/documentation.md` 和 `CLAUDE.md`
