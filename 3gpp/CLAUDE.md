---
type: spec
aliases:
  - 3GPP 项目 CLAUDE 指南
  - 3GPP 执行规范
tags:
  - 3gpp
  - claude
  - policy
source_spec: "Local project instructions"
---

# 3GPP 项目 CLAUDE.md

## 硬性规则

### 1. SKILL 优先检查（最高优先级）

**每次收到用户请求后，第一步必须检查可用 SKILL 列表，判断是否有匹配的 SKILL。**

匹配即调用——在生成任何其他回复之前，先用 Skill 工具调用匹配的 SKILL。

常见匹配场景：
- 审查代码 → `code-review` 或 `superpowers:requesting-code-review`
- 修复/精简代码 → `simplify`
- 创建功能/修改行为 → `superpowers:brainstorming`
- 深度调研 → `deep-research`
- 编写计划 → `superpowers:writing-plans`
- 执行计划 → `superpowers:executing-plans`
- 调试 → `superpowers:systematic-debugging`
- TDD → `superpowers:test-driven-development`
- 处理 PDF → `document-skills:pdf`
- 处理 Word → `document-skills:docx`
- 任务规划 → `planning-with-files:planning-with-files`
- 创建新 SKILL → `example-skills:skill-creator`
- 配置修改 → `update-config`
- 完成开发分支 → `superpowers:finishing-a-development-branch`

违反此规则是本次会话中已确认的已知问题，必须杜绝。

### 2. 项目背景

本项目是 3GPP LTE/NR 译码链路的全栈教学工程，包含：
- `docs/` — 128 篇讲义（L1 基础 42 → L2 协议/算法 57 → L3 工程 29）
- `sim/` — Python 仿真（CRC/GF(2) 等）
- `tools/` — 审计/抽取/渲染工具链
- `3GPP_Rel19/` — 协议原始资料和结构化抽取

### 3. 强制 DOXYGEN 风格注释（知识库红线）

**本项目是教学知识库，代码可读性优先于功能正确性。** 所有 Python 脚本、Shell 脚本、配置文件中的函数/类/任务入口必须使用完整的 DOXYGEN 风格注释：
- 文件头：`@file` + `@brief` + `@date`
- 函数：`@brief` + `@param` + `@return` + `@note` + `@throws`（按需）
- 脚本入口：`@brief` + `@usage` + `@args` + `@env` + `@exit_code`

代码审查时注释质量与功能正确性同等权重。详见 `.claude/rules/documentation.md`（项目根级规则）。

### 4. SVG 图生成后强制视觉验证

**任何 SVG 图（含手写、Python 生成、Mermaid/PlantUML 渲染）生成后，必须先验证再嵌入文档，禁止直接提交。**

验证步骤：
1. **Y 坐标扫描**（必须）：提取所有 `<text>`、`<rect>`、`<line>` 的 y 坐标，逐层核对间距 ≥ 8 px
2. **全量几何审计**（必须，`tools/audit_svg_layout.py` R1-R9）：R1-R3 文字宿主/越界/宽度、R4 text-text 重叠、R5 箭头终点贴盒边、R6 框外文字与文本框边界间距 ≥ 8 px（重叠/接触同样报）、R7 rect 部分重叠、R8 free 文字与任意 rect 重叠（网格格、图例色块等）、R9 polygon 箭头三角侵入 rect/text（贴边豁免，面积阈值 15px²）
3. **PNG 预览**（推荐）：`cairosvg` 或 ImageMagick `convert` 转 PNG，肉眼确认无交叠
4. **旋转文字禁令**（必须）：禁止裸 `transform="rotate"`——审计工具无法解析旋转 bbox，会漏报真实遮盖；旋转轴标签必须用 tspan 逐字竖排
5. **宿主文字豁免规则**：文字完全位于某 rect 内（宿主关系）时，与相邻无缝小格（如 26x22 导频格）的间距由 R3 内边距管理，R6 不适用——不要在密集小格图里为凑 8px 把文字缩小到不可读
6. 确认通过后才能写入 `docs/L1_基础/assets/` 并在正文引用

**教训来源**：
- 2026-07-23 生成的 circular buffer 交错图因未做坐标扫描，箭头说明文字、分隔标签、目标格子挤在 4 px 范围内，用户立即发现文字交叠。详见 `memory/svg-render-verify-before-commit.md`。
- 2026-08-04 T2.10 图 3 的"仿真验证：同时跑"文字与上方文本框边界仅约 2 px——框外文字必须与文本框边界留出 ≥ 8 px 间距，已固化为审计工具 R6 规则。
- 2026-08-04 T2.10 图 1 三次遮盖漏检（旋转轴标签压 k 行标签、'Δl=9' 压网格底行、'组内 Δk=2' 压图例色块、Δk 箭头三角压网格）——根因：审计工具盲区（rotate/polygon/free 豁免/重叠漏报）未被识别就采信 PASS；临时检查只做针对性验证未全量穷举；语义心算网格尺寸（12 子载波误当列数 → 右缘算成 400 实为 420）。已固化为工具 R8/R9 + 全元素穷举 + 几何事实优先规则，详见 `memory/svg-audit-blind-spots.md`。

### 5. SVG 字体度量规则

**审计工具的字体度量必须匹配实际渲染。**

1. **CSS class 样式必须被审计**：SVG 用 `<style>` 定义 `.title/.label/.small/.mono` 等 class 字号时，`tools/audit_svg_layout.py` 必须解析 CSS 规则（属性/继承 > CSS class > 默认 12px）——禁止按默认 12px 度量 class 文字。教训来源：2026-08-04 T10.9 图标题 `class="label"`(14px) 被按 12px 低估 17%，实际超出面板 42px 而审计 PASS。
2. **字体回退安全系数**：审计宽度 +8%（Obsidian 渲染可能 fallback 到更宽字体，如 DejaVu）；长文字（序列、数组、说明句）单行不得排满宿主，右缘预留 ≥10px 余量。
3. **工具升级后全库回归**：审计工具任何度量/规则变更后，必须对全部 assets 目录重跑并修复新增 FAIL（2026-08-04 升级后暴露 40 个存量 FAIL 已批量修复）。

### 6. Mermaid 语法强制规则

**任何 Mermaid 块必须可渲染（Obsidian/Mermaid 版本差异大，特殊字符写法必须取所有版本的安全子集）。**

1. **引号节点规则**（必须）：节点文本含 `[` `]` `(` `)` `{` `}` 等特殊字符时，一律用引号节点 `id["text"]`；**无引号节点 `id[text]` 内禁止任何括号**（Obsidian 的 Mermaid 对无引号节点内的圆括号/方括号都会解析失败）。教训来源：2026-08-04 T2.0 `X[k]`→`X(k)`→引号化 两次返工。
2. **语法修复全库同类扫描**（必须）：修复一类 Mermaid 语法错误后，扫描整类特殊字符（不只已发现的字符），并检查相邻系列文档的存量块。
3. **可渲染性验证**（必须，新增/修改 Mermaid 块后）：`bash tools/audit_mermaid_syntax.sh`（mmdc 真实渲染全库 Mermaid 块）。本工具依赖 puppeteer Chromium，缺失时先 `npx puppeteer browsers install chrome-headless-shell`；**工具不可用必须显式声明为验证缺口，不得默认通过**。
4. **Mermaid 与 SVG 的关系**：复杂图示优先手绘 SVG（`tools/audit_svg_layout.py` R1-R9 验证）；Mermaid 仅用于简单流程/结构图。

### 7. 纠错固化规则（元规则）

**用户每次指出错误，修复之外必须固化为规则与记忆——三选一或组合：审计工具检查项 / CLAUDE.md 条款 / 项目记忆文件。** 只修不固化视为未完成（教训：带圈数字替换 509 处仍复发、T11.1 连续四次视觉返工）。

修复流程固定五步：定位根因 → 修复 → 固化 → 全库同类扫描 → 验证闭环。

### 8. 批量替换作用域规则

**批量重命名/正则替换必须限定作用域，并以"引用→资产存在性"闭环验证。** 全库替换前先确认编号在各目录的唯一性（2026-08-05 误伤 L2 引用 11 文件：T12.x 在 L2/L3 都是合法编号）。替换后必须跑图片引用存在性检查（零缺失才算完成）。

### 9. 重绘交付检查清单

**重绘/新绘 SVG 交付前四查**：① 图模型节点组水平中心 = 宿主面板中心；② 节点距面板边 ≥ 8px（R10）；③ 布局密度（面板内容纵向填满，无大段空白）；④ 文字右缘余量 ≥ 10px、两行行距 ≥ 16px。工具盲区未覆盖的维度（居中、密度）必须手工坐标核算，不能只依赖工具 PASS（T11.1 四次返工教训）。

### 10. 序号写法规则

**禁止使用带圈数字序号（U+2460-U+2473 等全部变体）——全库 md/svg/py 通用。**

1. **序号统一写法**：行内枚举用 `(1)(2)(3)`，列表/步骤用 `1. 2. 3.`（Markdown 有序列表）。带圈数字是 Unicode 字符，字体支持不统一、无法表达有序列表语义。
2. **审计命令**：`python3 tools/audit_circled_digits.py`（默认扫 docs/tools/sim；发现即 FAIL）。新增/修改任何文档、SVG、代码后运行；全库回归在阶段验收时运行。
3. **教训来源**：2026-08-04 用户两次要求消除圈号——第一次替换 323 处后未固化规则，子代理写新内容又引入 186 处。一次性替换不是治理，检查规则才是。

### 12. 经验教训库（项目永久存储）

**每次会话开始即知**：本项目经验教训的权威副本在 `docs/audits/lessons/lesson-*.md`（10 条，随 git 双推保存，与 `~/.claude/projects/*/memory/` 的 auto-memory 同步维护，**以项目副本为准**）。

1. **使用时机**：遇到用户纠错、新问题、或规则未覆盖的场景，**先查经验库**（grep `docs/audits/lessons/` 关键字）是否已有同类教训——避免重复踩坑（每一条 lesson 都对应一次真实返工）。
2. **维护流程**（配合第 7 条纠错固化元规则）：新教训 → 写入 `docs/audits/lessons/lesson-<主题>.md`（含根因 + How to apply）→ 更新 `项目规则与记忆索引.md` 第七节登记表 → `git push origin master`（自动双推 Gitee+GitHub）。
3. **规则的可执行形态**：CLAUDE.md 各条、`合规与遵从.md`、`tools/audit_*.py`（审计工具即规则）均为经验的落地；经验库记录的是"为什么"。
4. **本地-云端双写机制**：`~/.claude/projects/<项目>/memory/` 是 auto-memory 工作层（会话自动加载，保留不动）；新经验**双写**——本地 memory + 项目仓库 `docs/audits/lessons/`（或 ic/docs/lessons、workspace-memory），映射关系见 `docs/audits/lessons/同步映射表-本地与云端.md`。删除本地 projects 目录不影响云端。

### 11. 合规基线

所有讲义和代码必须遵守 `合规与遵从.md` 中的 23 条 Hard Constraints（含 Rule 23 SVG T2.1 基准）。关键规则：
- 标题口语化禁止（Rule 16）
- 英文术语不能裸奔，首现必须"中文（English）"（Rule 10）
- 3GPP/LTE/NR 不机械重复全称（Rule 15）
- LaTeX 公式必须可渲染（Rule 20）
- 零基础保护（Rule 8）
