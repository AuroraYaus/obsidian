---
name: claude-settings-json-do-not-modify
description: 用户明确 ~/.claude/settings.json 不得被修改；deepseek harness key 更换只允许动 settings_deepseek.json 与 ~/.bashrc
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f36ee99a-746f-43c6-88ee-1c9dc1730f0a
  modified: 2026-08-17T13:32:58.272Z
---

2026-08-17 更换 deepseek harness api-key 时，我同时替换了 `~/.claude/settings.json`、`~/.claude/settings_deepseek.json`、`~/.bashrc` 三处 key。用户纠正：**`~/.claude/settings.json` 这个文件不要改**，已还原其原值 sk-704250…。

**Why:** settings.json 是用户的总配置文件（插件/hook/权限/env 全套），其中 `ANTHROPIC_AUTH_TOKEN` 的值用户有意保持原样；deepseek harness 的专属配置在 `~/.claude/settings_deepseek.json`（配合 --settings 启动）与 `~/.bashrc` 的 `DEEPSEEK_API_KEY` 两处，key 轮换只应落在专属文件上。

**How to apply:** 涉及 key/环境变量的更换任务，动手前先识别各文件归属：只改该 harness 的专属配置文件；`~/.claude/settings.json` 除非用户明确要求，否则一律不动。
