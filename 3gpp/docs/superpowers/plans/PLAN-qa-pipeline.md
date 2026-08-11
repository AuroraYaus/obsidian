# Plan: Q&A Pipeline 机制复制入库（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-11）_

## Goal

把 ic 项目（`~/AGENT/ic/CLAUDE.md` 第 9 条）的「问答与知识沉淀机制（Q&A Pipeline）」复制并适配到 3gpp 知识库规则：有问题先查询知识库 → 未命中补充知识库 + 更新查询次数 → 命中完善知识点 + 更新查询次数。

## Approach

1. `3gpp/CLAUDE.md` 新增第 15 条「问答与知识沉淀机制（Q&A Pipeline）」，适配 3gpp 术语：MOC → 入口文件（L0_术语入口/概念图谱入口）；概念笔记 frontmatter 新增 `queries` 字段约定（存量不回填）；9.0-9.6 全套（问题润色/检索/命中策略表/查询计数/易忘排名/输出标准/终端回答展示）。
2. `项目规则与记忆索引.md` 第一节规则文件表登记 + 第七节经验库登记 lesson-qa-pipeline。
3. auto-memory 写 `qa-pipeline-knowledge-base`（feedback 类型，跨会话生效）+ MEMORY.md 索引。
4. 提交双推。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 复制范围 | 仅 Q&A Pipeline（ic 第 9 条 9.0-9.6） | 用户澄清：不是构建规范（Wavedrom/RTL 铁律等），是查询-沉淀机制 |
| 落点 | 3gpp/CLAUDE.md 第 15 条 | 用户裁定；3gpp 是核心知识库子项目，规则权威文件 |
| 适配 | MOC→入口文件；queries 字段存量不回填 | 避免存量 71+ 笔记大规模返工；新内容/命中时引入 |
| ic 侧 | 不动 | 已有自己的版本 |

## Risks / open questions

- queries 字段引入后，审计工具（audit_lesson_terms 等）不检查该字段——后续可工具化（登记为后续任务）。
- 命中策略与既有「概念首现必须讲解」规则的关系：Q&A 写回的新概念笔记仍须遵守六段式模板与同步清单。

## Out of scope

- Wavedrom/RTL 铁律/元指令等其他 ic 规则（用户明确排除）。
- ic 项目文件修改。
- queries 字段审计工具化（后续任务）。
