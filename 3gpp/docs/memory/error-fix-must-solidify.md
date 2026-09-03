---
name: error-fix-must-solidify
description: 元规则——用户每次指出错误，修复之外必须固化为全局/项目经验教训与规则记忆，不能只修不固化
metadata:
  type: feedback
---

2026-08-05 用户明确要求："我每次指出你的错误你都要固化为全局或者项目的经验教训和规则记忆。"

**Why**：本项目经历了多次"修复后复发"——带圈数字替换 509 处仍反复出现（只替换未固化规则）、T2.10 遮盖三次漏检（工具盲区未登记）、T11.1 连续四次视觉问题（审查流程依赖工具 PASS 无目检闭环）。一次性修复不是治理，规则/工具/记忆固化才是。

**How to apply（每次纠错的固定流程）**：
1. 定位根因（工具盲区/流程缺失/规则缺失，而非表面现象）
2. 修复当前问题
3. **固化**（三选一或组合）：
   - 工具规则：audit_svg_layout.py / audit_circled_digits.py / audit_mermaid_syntax.sh 等新增检查项
   - 项目规则：CLAUDE.md 增补条款（含教训来源）
   - 项目记忆：memory/ 下新增或更新经验文件 + MEMORY.md 索引
4. 全库同类扫描（修一类问题必须扫整类，不只已发现的那一个）
5. 验证闭环（修复 → 全量验证 → 才宣告完成）

**检查清单**：每次用户指出错误后，回复中必须包含"已固化"部分（指向规则/记忆/工具的具体条目）；发现遗漏固化要主动补齐。

相关：[[svg-audit-blind-spots]]、[[circled-digits-forbidden]]、[[mermaid-parse-error-lessons]]
