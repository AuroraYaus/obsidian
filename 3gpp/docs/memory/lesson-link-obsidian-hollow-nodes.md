---
name: lesson-link-obsidian-hollow-nodes
description: "图谱空心节点根因——Obsidian 索引代码块/行内代码内无转义 [[..]]，审计工具三盲区假 PASS"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c0d8be5d-dad6-4d07-b569-2b0b7ec75c82
  modified: 2026-08-07T06:30:51.821Z
---

Obsidian 的 metadataCache 会把**代码块/行内代码内**的无转义 `[[...]]` 也索引为链接（阅读视图不渲染但图谱出幽灵节点）。2026-08-07 空心节点根因：T8.5 讲义 Python 嵌套推导式 `[[i for i, ... if row[j]]...]]`、计划文件省略号字样 `[[T2.1_AWGN...]]`、入口文件正文死链 `[[3gpp/Obsidian图谱标准化-执行结果]]`。

**Why:** 全库正文 wikilink 审计通过（M2 修复）仍有空心节点——工具三盲区：Markdown 正则漏 `\(`、路径形式未按 vault 根（.obsidian 所在目录）解析、不扫代码块；诊断脚本 `(!!?)` 正则前缀 bug 还造成假 0 死链（验证输出必须抽查样本行）。

**How to apply:** 代码/展示中需要字面 `[[` 一律插空格 `[ [`（100% 规避，转义 `\[[` 依赖解析器行为不确定）；跑升级版 `python3 tools/audit_link_integrity.py`（vault 根探测 + aliases + 代码块扫描 + 3GPP_Rel19 默认排除）。项目权威副本：[[3gpp 项目规则]] `docs/audits/lessons/lesson-link-obsidian-hollow-nodes.md`。关联 [[link-format-completeness]]、[[batch-rename-scope-scope-limit]]。
