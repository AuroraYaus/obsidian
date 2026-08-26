---
type: spec
aliases:
  - 裸 LaTeX 标记教训
  - bare math tokens
tags:
  - 3gpp
  - lessons
  - latex
  - audit
source_spec: "docs/audits/lessons/lesson-bare-latex-tokens.md"
---

# lesson-bare-latex-tokens：裸 LaTeX 标记（该围栏未围栏）

## 根因

2026-08-26 用户在 T2.0 图 1 说明中发现 `x(t)`、`X(k)`、`|X_k|=1` 未渲染——这些数学记号**没有加 `$` 围栏**，在 Obsidian/Web 中按普通文本显示。更深的问题：`tools/audit_latex_render.py` 只验证**围栏内**公式能否被 KaTeX 渲染，对"该围栏未围栏"的裸标记完全无感——审计工具盲区让存量问题长期积累（全库修复时发现约 150 处真实裸标记散布在 30+ 文件中，包括 T2.10 表格、T10.9 自测答案、T13.x PS 系列、T21.x 工程预算等）。

## 教训（How to apply）

1. **数学记号必须加 `$` 围栏**：函数记号（`x(t)`、`X(k)`、`r(n)`）、单字符下标记号（`X_k`、`H_k`、`f_c`）、绝对值（`|X_k|`）出现在讲义正文、表格单元格、例题、自测答案中时，一律 `$...$` 包裹。复合表达式（`max|x(n)|`、`|q_h|`）整体包裹，避免表达式分裂。
2. **协议参数名（多字母下划线命名）是例外**：`c_init`、`N_C`、`R_eff`、`n_SCID`、`P_CMAX` 是协议命名约定（行内代码风格），不属于裸标记检测范围——检测正则只匹配"单字符变量 + 单字符下标"（`[A-Za-z]_[a-z0-9]`），避免把参数名误报为数学记号。
3. **审计工具已升级**：`audit_latex_render.py` 新增 `check_bare_math()`，在全文层剔除代码围栏/`$$` 块公式/`$` 内联/反引号后，逐行检测三类裸标记。**关键实现教训**：块公式剔除必须用等量换行替换（保持行号），否则审计行号与原文错位导致修复脚本漏修（T2.8 误报教训）；修复脚本的 token 边界不能用 `\b`（token 以 `)` 结尾时 `\b` 永不匹配），改用 `(?![A-Za-z0-9_])`。
4. **清单/台账类文件豁免**：缩写概念理论清单、术语表的内容是参数名/缩写枚举，不属于讲义正文，裸标记规则不适用（`3GPP全流程_缩写概念理论清单` 已豁免）。
5. **修复脚本可复用**：`tools/fix_bare_math.py`（一次性迁移脚本）按审计报告逐行包裹，支持 `max|token|`/`|token|` 整体扩展，防嵌套包裹（`|q_h|` 先整体包、内部 `q_h` 不再重复包）。

## 关联

- 工具：`tools/audit_latex_render.py`（`check_bare_math`）、`tools/fix_bare_math.py`
- 规则：CLAUDE.md 第 11 条合规基线（Rule 20 LaTeX 渲染）+ 第 7 条纠错固化元规则
- 教训谱系：lesson-svg-audit-blind-spots（审计工具盲区同类问题——工具 PASS 不等于真实无错，必须补盲区后全库回归）
