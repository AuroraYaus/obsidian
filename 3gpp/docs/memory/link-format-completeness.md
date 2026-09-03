---
name: link-format-completeness
description: 链接死链检查必须覆盖全部格式（wikilink/Markdown 链接/相对路径）——空心节点教训：修 wikilink 漏 Markdown 链接，第三次"针对性盲区"复发
metadata:
  type: feedback
---

2026-08-07 用户报告 Obsidian 图谱空心节点（skill-first-check）——根因链：
1. 迁移 auto-memory 时目标文件加 lesson- 前缀，但索引备份内的 Markdown 相对链接 `[text](skill-first-check.md)` 原样复制未同步 → 链接目标不存在
2. 迁移脚本只处理内容主体，未处理文件内相对链接（把"备份文件"当低风险类别——但 Obsidian 所有 .md 都是图谱节点）
3. M2 修复时只扫 `[[wikilink]]` 格式，漏了 `[text](file.md)` Markdown 链接格式

**这是项目第三次"针对性扫描盲区"复发**（T2.10 遮盖→只查 text-text；T2.0 Mermaid→只修方括号；本次→只修 wikilink）。共同根因：扫描模式只覆盖已发现格式，未枚举整类变体。记录教训不够，必须工具化。

**How to apply（固化规则）**：
1. **链接死链检查必须全格式**：wikilink `[[...]]` + Markdown 链接 `[...](file)` + 相对路径引用，三种格式一次扫全——写进审计工具（新增 check，纳入交付门禁）
2. **文件改名/迁移后必须验证"文件内引用可解析性"**：任何批量改名（含加前缀）后，对目标目录内全部 .md 跑链接存在性检查——不只查正文引用，也查索引/备份文件内部链接
3. **备份/归档文件不豁免可导航性**：Obsidian 图谱不区分文件类别，所有 .md 的链接都必须可解析
4. **修复时枚举格式变体**：修一类链接问题前，先列出该问题所有可能格式（wikilink/Markdown/HTML 链接/相对路径），不能只处理已发现的那个

相关：[[svg-audit-blind-spots]]（针对性盲区同构教训）、[[batch-rename-scope-scope-limit]]（改名后引用验证）
