# 工作区规则与经验索引

本工作区（git 仓库根）的核心项目是 `3gpp/`（3GPP LTE/NR 译码教学知识库）。**开始任何 3gpp 相关工作前，必须读取以下文件**（它们是规则与经验的权威来源，随 git 双推永久保存）：

## 必须读取（按序）

1. **`docs/rules/用户全局规则.md`** — 用户全局规则的项目内随行副本（`~/.claude/CLAUDE.md` 全文镜像，全局文件更新后同步本副本）；用户级 SKILL 执行体随行副本见 `.claude/skills/`。
2. **`3gpp/CLAUDE.md`** — 项目硬性规则 17 条：SKILL 优先检查、DOXYGEN 注释红线、SVG 生成后强制视觉验证（R1-R11）、字体度量规则、Mermaid 引号节点与可渲染性验证、纠错固化元规则、批量替换作用域、重绘交付检查清单、序号写法（禁带圈数字）、合规基线、经验教训库指引、绘图政策（禁 Python 绘图）、写作计划先拷问（第 14 条）、Q&A 流水线（第 15 条）、编辑前同步远程（第 16 条）、记忆双份维护（第 17 条）。
3. **`3gpp/合规与遵从.md`** — 23 条 Hard Constraints（零基础保护、中文术语优先、3GPP 协议精读优先、LaTeX 渲染全检等）。
4. **`3gpp/项目规则与记忆索引.md`** — 规则文件优先级、写作规范、同步清单、编号约定、经验库登记（第七节）。
5. **`3gpp/docs/audits/lessons/lesson-*.md`** — 经验教训库（lesson-* 经验教训与记忆备份：SVG 审计盲区、字体度量、圈号、Mermaid、批量替换、双推、纠错固化、空心节点、绘图政策、写作先拷问、Q&A 流水线、协议族分布展示等）。遇到用户纠错或新问题**先查这里**。
6. **`3gpp/.claude/rules/documentation.md`** — DOXYGEN 细则、讲义文档规范、概念笔记模板、SVG 资产规范、术语同步。

## 关键行为约束（摘要，完整见 3gpp/CLAUDE.md）

- SVG 生成/修改后：`python3 tools/audit_svg_layout.py <file>` 必须 ALL_PASS（R1-R11）+ cairosvg 渲染。
- 用户每次指出错误：修复之外必须固化（工具规则 / CLAUDE.md / lessons/ 三选一或组合）→ 提交双推。
- 推送：`git push origin master` 自动双推 Gitee + GitHub（origin 配了双 pushurl；GitHub 走 ssh.github.com:443）。
- 编号/批量替换：限定作用域 + 存在性闭环验证。

## 维护

- 新增教训 → `3gpp/docs/audits/lessons/lesson-<主题>.md` → 更新 `项目规则与记忆索引.md` 第七节 → 提交并 `git push origin master`（双推）。
- 全局规则更新后 → 同步 `docs/rules/用户全局规则.md` 随行副本；用户级 SKILL 更新后 → 同步 `.claude/skills/`（详见 `.claude/CLAUDE.md`）。
