# 记忆索引备份（MEMORY.md）

> auto-memory 索引的云端备份副本。

- [IC vault session 2026-07-22](session-2026-07-22-ic-vault-creation.md) — Built independent digital IC Obsidian vault ~/AGENT/ic/, 45 files, 6 domains, recovered from regex corruption
- [Doxygen documentation requirement](doxygen-documentation-requirement.md) — 所有代码必须使用完整 DOXYGEN 风格注释，知识库面向新手，教学可读性优先
- [讲义正文无中间运行结果](lecture-writing-no-intermediate-results.md) — 讲义正文不得含代码中间运行结果/调试输出/过程叙述，书面严谨
- [概念首现必须讲解](lecture-first-occurrence-explain.md) — 讲义中概念首次出现必须给出介绍讲解，不能只靠概念笔记/wikilink
- [SVG 边界间距规则](svg-boundary-gap-rule.md) — 文本框边界与框外文字/其他文本框间距 ≥8px；任何形式重叠不允许
- [知识库同步清单](knowledge-base-sync-checklist.md) — 术语/入口/编号/资产/路径/台账八类同步场景，新增内容必须逐项检查（权威清单在 3gpp/项目规则与记忆索引.md 第六节）
- [SVG 审计盲区教训](svg-audit-blind-spots.md) — T2.10 图 1 三次遮盖漏检根因链：工具盲区/针对性验证/语义心算/误报干扰；固化 R8/R9 全元素穷举与修复闭环规则
- [Mermaid parse error 漏检教训](mermaid-parse-error-lessons.md) — T2.0 括号问题漏检 4 层原因；固化引号节点规则、全库同类扫描、验证手段先行
- [SVG CSS class 字体度量漏检](svg-css-class-font-metric-lessons.md) — 工具不解析 `<style>` class 样式导致 14px 文字按 12px 低估、超边 42px 漏检；固化 CSS 解析 + 8% 安全系数
- [带圈数字禁令](circled-digits-forbidden.md) — 圈号序号两次替换 509 处仍反复出现；固化 audit_circled_digits.py 检查 + (1)(2)(3)/1. 2. 3. 写法
- [SVG 注释书面语](formal-writing-svg-notes.md) — 注释/标注禁止"画…出的"类口语表达，用"补充表格之外的拓扑结构"式书面语
- [纠错必固化元规则](error-fix-must-solidify.md) — 用户每次指出错误，修复外必须固化为工具规则/CLAUDE.md/项目记忆三选一或组合
- [批量替换作用域限定](batch-rename-scope-scope-limit.md) — 批量重命名必须按目录限定 + 存在性闭环验证（2026-08-05 误伤 L2 引用 11 文件）
- [重绘交付检查清单](svg-redraw-check-centering-density.md) — 图模型居中/面板边距/布局密度/文字余量四查（T11.1 四次返工教训）
- [双推 Gitee+GitHub](dual-push-gitee-github.md) — push origin 已配双 pushurl；大仓库首同步走 GitHub Import，增量走 ssh.github.com:443
