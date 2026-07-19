---
type: spec
aliases:
  - global compliance review
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/global_compliance_review.md"
---
# Global Compliance Review

审查时间：2026-06-21  
审查范围：`docs/L1/T*.md`、`docs/L2/T*.md`、`docs/L3/T*.md`、`合规与遵从.md`、`2026-06-19-lte-nr-decoding-learning-roadmap.md`、`docs/audits/*.md`。最新交付状态见 `docs/audits/final_delivery_status.md`。

## 规则一致性

| 规则来源 | 状态 | 证据 |
|:---|:---|:---|
| `合规与遵从.md` | 已纳入审查。 | 包含零基础理论铺垫、3GPP 协议精读、缩写首现、标题正式化、引用内容重建、协议索引化防复发、LaTeX 全检、Prompt 最低线与适当拓展、连续执行和图片视觉审计要求。 |
| `2026-06-19-lte-nr-decoding-learning-roadmap.md` | 已纳入审查。 | 顶部规范强调弹性审计清单，不把固定讲义骨架机械套入每节。 |
| `docs/audits/lte_nr_decoding_remaining_work_register.md` | 已纳入审查。 | 记录模块 8-15、全项目图片规则加严、T15.6 最终证据报告和后续审计证据。 |

结论：三处规则没有方向性冲突。总纲提供硬性约束，路线图和剩余工作台账提供执行顺序、Prompt 覆盖和证据记录。

## 用户全局要求核对

| 要求 | 状态 | 证据或遗留动作 |
|:---|:---|:---|
| 重点是 LTE 和 NR 的译码部分。 | 通过 | 94 篇讲义围绕 LTE Turbo、NR LDPC、NR Polar 的理论、协议、接收端流程、定点、RTL/ASIC 和验证展开。 |
| 3GPP 相关知识点必须围绕协议精读。 | 通过，保留真实系统级条件项 | T6-T11 精读 TS 36.212/38.212，必要处回链 TS 36.213/36.321/38.214；T15.6 汇总具体 TS 包、章节、表/图/公式和本地路径。TS 38.214 MCS/TBS 具体表值仍为系统级 bit-exact 条件项。 |
| 零基础教学，先讲理论、解释和推导，不能只列协议索引。 | 通过 | `audit_lesson_depth.py --strict docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md` 输出 `LESSON_DEPTH_AUDIT_OK`。 |
| 固定“单节工程讲义骨架”不能机械套用，要因地制宜。 | 通过 | 当前讲义按基础课、协议课、工程课性质调整标题和顺序；审计以覆盖和证据为准。 |
| 缩写首次出现要解释，3GPP/LTE/NR 不要每次重复全称。 | 通过 | 本轮补齐 L1/L2 首现说明后，`audit_lesson_terms.py docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md` 输出 `LESSON_TERM_AUDIT_OK`。 |
| 标题不得口语化，全项目整改。 | 通过 | `audit_markdown_headings.py docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md` 输出 `MARKDOWN_HEADING_AUDIT_OK`。 |
| 每篇文章要足够细致，不能篇幅太薄。 | 通过 | 全项目严格深度审计通过；L3 T12-T15 按 prompt 全量覆盖并扩展对象模型、例子、伪代码、验证和证据边界。 |
| 引用协议/论文公式、表格、图不能只给链接，要复现或重建。 | 交付级分类完成，仍有条件项 | 关键协议表/图/公式已在 T3/T6-T11/T15 中复现或回链；引用重建候选脚本输出需人工分类，不等同失败。真实新增引用仍需随写随审。 |
| 难理解内容要配 Python 绘图，图要清晰、无遮挡、间距合理。 | 通过，持续控制 | 当前 `docs/audits/image_asset_inventory.md` 记录 68 张 PNG、58 个 Python 文件；`tools/audit_project_image_inventory.py` 覆盖资产目录、正文引用、资产清单和迁移台账一致性。用户指出过的 T6.3、T7.3、T7.5、T8.1-T8.4、T10.2、T10.7、T11.1、T11.2、T12.1、T14.4、T15.2 等图形问题已规则化。 |
| LaTeX 公式必须全检，不抽检。 | 通过 | LaTeX 分段全检通过：L1 `2036`、L2 `3444`、L3 `948`，合计 6428。 |
| Prompt 必须完全覆盖，并适当拓展。 | 通过 | `docs/audits/prompt_coverage_matrix.md` 覆盖 94 篇；当前无未纳入 T 类讲义。 |
| 新问题不得中断旧任务，默认并行处理。 | 已写入规则 | `合规与遵从.md`、路线图和剩余工作台账均记录该规则；当前按旧任务继续执行。 |
| 图片箭头、连线、字体、表格、说明框必须逐图审计。 | 通过，持续控制 | `docs/audits/image_review_detailed_checklist.md`、`docs/audits/python_figure_visual_geometry_checklist.md`、`tools/audit_figure_geometry.py`、`tools/audit_figure_readability.py` 和资产清单已固化。 |

## 自动审计结果

| 审计项 | 命令 | 最新结果 |
|:---|:---|:---|
| 术语首现 | `python3 tools/audit_lesson_terms.py docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md` | `LESSON_TERM_AUDIT_OK` |
| 标题正式化 | `python3 tools/audit_markdown_headings.py docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md` | `MARKDOWN_HEADING_AUDIT_OK` |
| 深度/协议索引化风险 | `python3 tools/audit_lesson_depth.py --strict docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md` | `LESSON_DEPTH_AUDIT_OK` |
| LaTeX 全检 | `python3 tools/audit_latex_render.py docs/L1/T*.md`；`python3 tools/audit_latex_render.py docs/L2/T*.md`；`python3 tools/audit_latex_render.py docs/L3/T*.md` | L1 `LATEX_RENDER_AUDIT_OK formulas=2036`；L2 `LATEX_RENDER_AUDIT_OK formulas=3444`；L3 `LATEX_RENDER_AUDIT_OK formulas=948`；合计 6428。 |
| 图片几何/可读性 | `python3 tools/audit_figure_geometry.py tools/figures`；`python3 tools/audit_figure_readability.py tools/figures` | `FIGURE_GEOMETRY_AUDIT_OK`；`FIGURE_READABILITY_AUDIT_OK`。 |
| 引用重建候选 | `python3 tools/audit_reference_rebuilds.py docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md > docs/audits/reference_rebuild_candidates_full.txt` | 退出码 0，候选清单 1320 行；候选不是硬失败。 |

## 图片资产审查

| 范围 | 数量 | 当前状态 |
|:---|---:|:---|
| L1 PNG | 5 | 协议表格、基础复现资产和协议阅读地图图，纳入资产清单。 |
| L2 PNG | 40 | LTE Turbo、NR LDPC、NR Polar、对比章节图；包含 T8.3/T8.8 分片正文图和完整证据/兼容保留图。 |
| L3 PNG | 23 | Golden model、定点、RTL/ASIC、验证、综合和最终证据图，纳入资产清单。 |
| Python 文件 | 58 | 57 个 `render_*.py` 绘图脚本和 1 个共享 helper；已有几何/可读性/文本适配/项目级一致性审计覆盖。 |

局部视觉审计仍是持续控制项。任何新增、修改或重生成图片都必须分别记录字体与上下边框距离、相邻边框间距、箭头是否正常、连线起止位置是否合理，并确认表格单元格和文本框水平/垂直居中。

## 遗留风险

| 问题 | 影响 | 后续动作 |
|:---|:---|:---|
| TS 38.214 MCS/TBS 具体表值未按真实系统级向量完整复现 | 不影响当前译码讲义交付，但影响未来 conformance 级 bit-exact 调度向量。 | 后续按实际使用范围复现表格子集。 |
| 真实 BLER、定点、RTL、coverage、DC、STA、功耗证据未运行 | 不能把 T15.6 模板视为真实 sign-off。 | 真实工程阶段按 T15.6 schema 归档证据，签核状态从 `hold` 更新。 |
| 引用候选脚本误报和候选较多 | 若不分类，容易把候选误写成失败或通过。 | 保持人工分类报告和证据表，不用候选行数替代判断。 |

## 结论

当前 94 篇讲义符合全局文档合规要求：术语、标题、深度和 LaTeX 全检均通过；Prompt 覆盖矩阵无未纳入 T 类讲义；图片资产清单覆盖当前 68 张 PNG 和 58 个 Python 文件，并通过项目级一致性审计。真实工程签核保持 `hold`，这是证据边界，不是文档缺口。
