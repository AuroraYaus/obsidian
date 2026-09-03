# 项目级规则（obsidian 工作区）

本文件为 obsidian 工作区（3gpp/、ic/ 等子项目）的项目级规则。全局规则见 `~/.claude/CLAUDE.md`（项目内随行副本：`docs/rules/用户全局规则.md`），3gpp 子项目的专属硬性规则见 `3gpp/CLAUDE.md`。

## 写作计划与决策问题先拷问（2026-08-11 用户确立，全局规则在本工作区的重申）

任何写作计划、设计方案或需要用户决策的问题，动手前必须先拷问用户（grill-me 风格：一次一个问题、附推荐答案、能自查先自查），收敛并写入 PLAN.md 后再执行。豁免：纯信息性问答、已获用户批准的执行步骤（无新决策点）、单一机械性修改。完整条款见 `~/.claude/CLAUDE.md`；3gpp 子项目另见 `3gpp/CLAUDE.md` 第 14 条与经验库 `3gpp/docs/audits/lessons/lesson-grill-before-planning.md`。

## 全局规则与 SKILL 随行维护（2026-09-03 用户确立）

工作区文件夹拷贝到任何位置后，生效规则与记忆不失效：

1. **全局规则随行副本**：`docs/rules/用户全局规则.md` 为 `~/.claude/CLAUDE.md` 全文镜像——全局文件为权威（跨 6 个项目生效），每次修改全局文件后同步本副本（方向：全局 → 项目，与记忆的"项目 → 镜像"相反）。
2. **SKILL 执行体随行**：`.claude/skills/` 为用户级 `~/.claude/skills/` 的全量拷贝，用户级 SKILL 新增/更新后同步拷贝。
3. **记忆随行**：详见 `3gpp/CLAUDE.md` 第 17 条（`docs/memory/` 项目内权威 → `~/.claude/projects/*/memory/` 会话加载镜像）。
