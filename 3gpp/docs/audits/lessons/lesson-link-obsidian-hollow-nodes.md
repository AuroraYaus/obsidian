---
name: lesson-link-obsidian-hollow-nodes
description: 图谱空心节点根因——Obsidian 索引代码块内 [ [..]] 与审计工具三盲区假通过
metadata:
  type: feedback
---

# 图谱空心节点（幽灵节点）三连盲区

**现象（2026-08-07）**：Obsidian 关系图谱出现空心节点（未解析链接的虚线圆点）。全库正文 wikilink 全部可解析（M2 修复已生效），空心节点另有来源。

## 根因链

1. **Obsidian metadataCache 索引代码块/行内代码内的无转义 `[ [...]]`**（与阅读视图不同，链接提取不排除代码块；unresolvedLinks → 图谱幽灵节点，`stat.ctime===0` 哨兵）。活例：
   - `docs/L2_协议算法/T8.5_LDPC_sum_product_BP.md` 讲义正文 Python 嵌套列表推导式 `cols = [ [i for i, row in enumerate(H) if row[j]] for j ...]`——`[ [` 后紧跟 `]]` 的形态被 Obsidian 解析成 wikilink，目标名是一段 Python 代码。
   - 计划/报告文件的省略号字样 `[ [T2.1_AWGN...]]`、`[ [概念笔记]]`、`[ [...]]`、`[ [T12.x_...]]`——历史文件"刻意还原"的展示文本，目标不存在。
2. **正文路径形式死链**：`3GPP_译码知识库入口.md` 的 `[ [3gpp/Obsidian图谱标准化-执行结果]]`（引用的目标文件从未存在/已改名，入口文件引用未同步）。
3. **根目录空文件掩盖死链**：子代理把 memory 教训文件误写进 vault 根（`wikilink.md`、`链接.md` 等 0 字节 untracked 文件），使 `[ [wikilink]]`、`[ [链接]]` 恰好可解析；删除空文件后这些字样立即变死链（lesson-lecture-first-occurrence-explain 第 5 行即此类）。

## 工具侧三盲区（假 PASS 根因）

- **Markdown 链接正则漏 `\(`**：`\]` 直接接 `([^)]*\.md)` 会把 `(3GPP_Rel19/x.md` 整段当目标 → `3GPP_Rel19_资料入口总览.md` 误报。
- **路径形式 wikilink 按文件目录解析**，而 Obsidian 按 **vault 根**（`.obsidian` 所在目录）解析 → 入口文件的 `[ [3gpp/docs/...]]` 系列 8 条全误报。
- **不扫代码块内 `[ [`** → T8.5 类死链漏报。
- 诊断脚本自身正则 `(!!?)` 前缀实际要求**至少一个 `!`**，普通 `[ [` 全不匹配 → 假 0 死链。**验证输出必须抽查样本行，不能只看结论行**（本会话假 PASS 一次）。
- **`[ [` 展示字样自身也会变死链**：本 lesson 初版用无转义 `[ [` 写展示示例，工具立即抓出 16 条——写文档时展示链接写法一律插空格。

## 修复

- 规避 Obsidian 索引的统一写法：**`[ [` 插空格**（`[ [x]]` → `[ [x]]`），Python 语义不变、字符层面不构成 `[ [`，100% 可靠（转义 `\[[` 依赖解析器行为，不确定）。共 13 处 + 1 处正文改链 `[ [Obsidian图谱标准化]]`。
- 转义 `\[[`（grep 示例）Obsidian 不索引，无需处理。

## How to apply

- **写/改任何 md（含代码块）后跑** `python3 tools/audit_link_integrity.py`：升级版已含代码块内无转义 `[ [` 扫描（转义排除）、vault 根自动探测（向上找 `.obsidian`）、frontmatter 别名解析、Markdown 链接修正、`3GPP_Rel19` 默认排除（`--include-rel19` 可开）。
- 代码里需要字面 `[ [` 的展示/示例：一律插空格 `[ [`。
- 删除空文件前先查同名 `[ [` 引用，避免把可解析变死链（本会话先修链接后删文件，仍漏 lesson 存量 1 处——工具闭环补抓）。
- 与 [[lesson-batch-rename-scope-scope-limit]]（改名后验证引用）、[[lesson-knowledge-base-sync-checklist]]（第八类 Obsidian 状态同步）联动。
