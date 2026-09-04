# Lesson: 2026-08-14 全库审核的三类治理缺口

## 教训一：命名约定即工具契约

**根因链**：`audit_lesson_depth.py` 把"讲义 = T*.md"写死在代码注释里（本项目的讲义命名约定）；L2 M16 系列（2026-08-13 批次）为避开 L3 的 T16-T21 声明区间，使用了全库唯一的 `M16.x` 文件名。结果该系列 4 篇讲义**数周内完全逃逸讲义深度审计**——同样的体量在别的系列会被标 very short/weak theory，M16 却零发现。反向盲区同时存在：`Turbo_码`、`TB_传输块`、`TDL_信道模型` 等 T 开头的概念笔记被 `T*.md` glob 误收为讲义，产生假 TRIAGE。

**How to apply**：
1. 新增讲义系列必须沿用 T*.md 文件名（T6-T16/T17-T23/TX 区间），模块号（M 系列）只存在于正文与入口标题，禁止出现在文件名。
2. 审计工具的发现模式（glob/正则/豁免目录）是治理契约的一部分——改命名或改目录结构时，先查所有工具的发现逻辑是否同步。
3. 工具发现逻辑必须排除非讲义目录（concepts/audits/superpowers/L0），与术语审计豁免区 h/i/j 对齐。

## 教训二：规则文件自指数字需要定义口径并随批次同步

**根因链**：同一指标在多个权威文件中并存多个版本——讲义数 128（CLAUDE.md §2 旧口径）/155（README，把入口 spec 文件计入）/153（实际）；概念笔记 104/106；术语 155+71 vs 实际 254+104；Hard Constraints 22/23；SVG 审计 R1-R7/R1-R11；lessons 10/16/19/21。根因是"什么算讲义"从未定义口径，且 Rule 23 等新增规则后计数器没有全链更新。

**How to apply**：
1. 每个自指数字必须先定口径（讲义 = T/TX 编号正文文件；概念笔记 = `English_中文.md` 六段式；术语 = L0 总表数据行）。
2. 数字变更必须一次改全：三份 README + 3gpp/CLAUDE.md §2/§12 + 工作区 CLAUDE.md + 项目规则与记忆索引（同步清单第 9 条已把口径固化进去）。
3. 本次审核还发现 frontmatter `type` 字段存在大面积误标（67 篇讲义标 definition/spec）——分类治理另立议题，口径暂时不依赖 type 字段。

## 教训三：易失状态与派生数据不入库

**根因链**：`.obsidian/workspace.json`、`graph.json` 是 Obsidian 的 UI 状态文件，每次打开 vault 都会改写——入库导致每次会话必 dirty、每次批量提交都携带无意义噪音。`3GPP_Rel19/processed/` 2.6GB 派生数据入库使主仓克隆成本 3GB（知识库本体仅 16MB）。

**How to apply**：
1. UI 状态文件一律 `git rm --cached` + .gitignore（配置类 app.json/core-plugins.json/snippets 保留）。
2. 大体量派生/原始数据拆独立数据仓，主仓 README 写明可选复原方式（clone 到原相对路径即恢复所有引用）；首次全量推 Gitee、GitHub 走 Import 中转（本仓 2.6GB/81359 文件 2026-08-14 实测可行）。
3. 主仓历史保留不 filter-repo——双端 force push 风险大于收益。

## 补记：数据仓复原 clone 必须带目标路径（2026-09-03）

拆仓后的复原 clone 若漏掉目标路径参数（只复制数据仓 URL），目录会落在仓库根 `3GPP_Rel19/`——协议锚点类引用全部失效，且约 8 万文件成为主仓未跟踪目录（根 `.gitignore` 只匹配 `3gpp/3GPP_Rel19/`，`git add .` 即误入库）。**How to apply**：README「协议证据数据」章节已扩充为配置步骤 + 落点警告（clone 必须带目标路径、放错位置的双后果、克隆后结构验证 + git status 干净）；复原或指导复原时直接照抄 README 命令，不得只发 URL。

## 补记：graph.json 被 workspace.json 连坐误伤（2026-09-04）

教训三将 `graph.json` 与 `workspace.json` 一并移出版本控制，但两者易失性不同：workspace.json 每次会话必改写；graph.json 仅在修改图谱设置时变化。图谱颜色分组（33 组 tag/path/type 查询）、过滤规则（`path:3gpp/docs -path:...lessons -path:...3GPP_Rel19`）、隐藏孤立节点开关全部存于 graph.json——另一台机器 clone 后该文件缺失，图谱无颜色、无过滤、非知识库文件与孤立节点全显（2026-09-04 换机实测）。**How to apply**：UI 状态文件按"是否随正常使用自变"区分易失与否，不按"是否位于 .obsidian/ 下"一刀切——workspace.json 保持忽略，graph.json 重新纳入版本控制（改图谱设置产生的 diff 值得提交）；警惕其它"看似易失实为配置"的文件被连坐。

## 补记：归档移动后引用必须同类同步

Python 绘图工具归档至 `tools/archive_python_drawing/` 时，多级相对根 `parents[2]` 少算一层（4 个 render 脚本同类）、测试文件 3 类 import 路径未更新（tools.figures / tools.audit_* → archive 前缀）——测试套件 33 个失败全是 `ModuleNotFoundError`。**How to apply**：目录归档/移动后，除 md 引用外，必须扫描 py 脚本内 `parents[N]`/`__file__` 相对根与测试 import，跑一遍测试套件闭环（2026-08-14 修复后 59/59 通过）。
