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
