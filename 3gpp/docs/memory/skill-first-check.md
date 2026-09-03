---
name: skill-first-check
description: 每次响应前必须先检查是否有匹配的 SKILL 可调用
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 23cdd4bd-5a26-4437-bb71-dfcb1ff029f0
---

每次收到用户请求后，在生成任何其他回复或执行任何工具之前，必须先检查当前可用的 SKILL 列表，判断是否有匹配的 SKILL。如果匹配，必须用 Skill 工具调用它，不得跳过直接手写。

这是用户明确要求的防复发规则。之前多次违反（合规审核时跳过了 brainstorming/planning-with-files，code review 时手动模拟了整套流程）。规则已写入项目 CLAUDE.md 作为最高优先级规则。

**Why:** 用户发现我会忘记使用已安装的 SKILL，直接手动完成任务。这会浪费已安装 SKILL 提供的专业能力、结构化流程和一致性保证。

**How to apply:** 每次回复前先扫一遍可用 SKILL 列表（在 system-reminder 中），判断是否有匹配项。有疑问时宁可多调用，不可跳过。
