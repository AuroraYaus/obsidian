---
name: dsh-web-cordis-webserver-typo
description: "dsh web 崩溃 \"cannot get property webserver without inject\" 的根因（ctx.webserver 大小写笔误）+ Cordis inject 语义 + 本地补丁位置与 npm 更新覆盖风险"
metadata: 
  node_type: memory
  type: project
  originSessionId: f0a30206-3f8f-45dc-bde9-910d36670ce0
  modified: 2026-08-26T17:02:51.897Z
---

# dsh web 崩溃：ctx.webserver 大小写笔误（2026-08-26）

**症状**：`dsh web` 启动即崩——`dsh: plugin tree failed to load: failed to apply loader entry web-runtime (@deepseek-ai/dsh-web-app): cannot get property "webserver" without inject`。

**根因**：2026-08-26 23:47 给 `~/.npm-global/lib/node_modules/@deepseek-ai/dsh/node_modules/@deepseek-ai/dsh-web-app/lib/index.js` 的 `apply()` 加"计费价格同步"端点补丁时，把 Cordis 服务属性写成小写 `ctx.webserver`；该服务真实属性名是 `ctx.webServer`（camelCase，与文件第 30 行 `inject = ["webServer"]` 及全文件其余用法一致），Cordis 对未声明属性直接抛 "cannot get property X without inject"。修复即一行大小写改正，全库扫描确认无同类笔误。

**Cordis inject 语义（避免再误诊）**：插件自身的 `inject` 声明始终生效；bundle 入口层的 `inject`（如 web-runtime 的 `[webStartup]`）只为该入口 `config` 的 `!!js` 表达式求解服务（`ctx.webStartup.host` 等），不是插件 `apply()` 依赖的来源。因此**不需要**在 `cordis.patch.yml` 里给 web-runtime 重注入 `[webServer, webStartup]`——当晚 23:56 那个注入补丁属误诊，实测空补丁 + 笔误修复即可正常启动（root 与 /api/deepseek-pricing 均 HTTP 200），已还原为 `[]`。

**位置与风险**：
- Profile 用户补丁层：`~/.dsh/profiles/web/cordis.patch.yml`（bundle 列表在 `package.json` 的 `dsh.profile.bundles`；`cordis.yml` 是根文件、勿编辑）。
- 本地功能补丁直接改在 npm-global 的 node_modules 包内，`npm update`/重装 dsh 会覆盖，需留意丢失。
- 计费端点：`GET /api/deepseek-pricing`（服务端 6h 缓存 + 定时刷新；前端 `dsh-client-ui-conversation/lib/client.js` 有内置回退价格表，失败降级）。

**坑**：Claude Code Bash 工具里 `pkill -f "dsh web"` 会匹配到自己的 `bash -c` 命令行导致自杀（exit 144）；杀 dsh 进程用精确 PID（`pgrep -af "bin/dsh"` 取 PID 后 kill）。

**2026-08-27 回退记录**：用户要求"替换为官方源码版本"（官方 master b150a55 已含 webServer 正确写法、但不含定价补丁），已克隆源码并 pnpm 构建到一半时被用户叫停并全量回退——源码 checkout、备份 diff、pnpm 及 1.4G store 全部删除，npm 全局安装的两处本地补丁（webServer 笔误修复 + 定价同步）**仍原样保留**。后续会话不得未经用户明确要求再次尝试源码替换；本地补丁备份曾存于 `~/.dsh/backup/`（已被删除，如再需备份可重新 `npm pack` 对应包 diff 提取）。

**2026-08-27 深夜替换完成**：用户删除自己的 `~/deepseek-harness`（setup.sh 安装包）后明确要求重做。最终状态：官方源码 checkout 在 `~/deepseek-harness`（master b150a55）；全局 dsh 已卸载 npm 版、`npm link` 指向 checkout 构建物（`~/.npm-global/lib/node_modules/@deepseek-ai/dsh -> ../../../../deepseek-harness/apps/cli`）；官方构建物无 `ctx.webserver`（0 处），`dsh web --no-open` 实测 HTTP 200 无崩溃，`/api/deepseek-pricing` 404（定价补丁按"都回退"弃用）。**更新方式**：`cd ~/deepseek-harness && git pull && pnpm install && pnpm run build`（pnpm@11.7.0 已全局安装）。注意：不可 `npm i -g <checkout>/apps/cli` 方式装（npm 会按 registry 装其依赖，拉到带笔误的发布版 web-app）；必须 npm link 使依赖从 checkout node_modules 解析。

## 2026-09-03 Windows 机器（D:/ClaudeCode/obsidian 工作机）dsh 配置记录

- 本机 dsh = **npm 全局安装版 0.1.0-rc.6**（`%APPDATA%\npm\node_modules\@deepseek-ai\dsh`），无源码 checkout（Linux 机的官方源码流程未在本机复现）。
- API key 落点：`~/.dsh/.credentials.yaml`（DSH_HOME 默认 `~/.dsh`），格式 `DEEPSEEK_API_KEY: sk-...`——插件 `dsh-llm-deepseek` 默认读 env 名 `DEEPSEEK_API_KEY`（`DEFAULT_API_KEY_ENV`），官方端点 `PUBLIC_BASE_URL = https://api.deepseek.com`。
- 凭据解析顺序（dsh-credentials-local）：继承的进程环境变量 > `$DSH_HOME/.credentials.yaml`（provider 管理、watch 热发布）> 调用 cwd 的 `.env` > `$DSH_HOME/.env`。
- 验证：key 用 `curl /models` 实测有效（deepseek-v4-flash / deepseek-v4-pro / deepseek-v4-flash-vision-exp）；`dsh web --port 8123` 启动 root HTTP 200。
- 本机杀 dsh：`netstat -ano | grep :<port>` 取 PID → `taskkill //PID <pid> //F`（pkill -f "dsh web" 自杀坑同前）。

## 相关

- [[claude-settings-json-do-not-modify]]（deepseek harness 环境约束）
