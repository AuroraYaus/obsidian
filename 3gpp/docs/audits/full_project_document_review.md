---
type: spec
aliases:
  - full project document review
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/full_project_document_review.md"
---
# Full Project Document Review

审查时间：2026-06-21  
审查范围：已存在的 `docs/L1/T*.md`、`docs/L2_协议算法/T*.md`、`docs/L3/T*.md`，共 94 篇讲义。最新总表见 `docs/audits/final_delivery_status.md`。  
审查原则：Prompt 是最低覆盖线，正文必须适当拓展；3GPP 相关知识点必须围绕协议精读；零基础讲义必须先解释概念、理论和直觉，再进入公式；LaTeX 必须全检，不抽检；图片必须逐图检查局部视觉几何。

## 审查对象

| 层级 | 文件数 | 范围 | 状态 |
|:---|---:|:---|:---|
| L1 | 28 | T0.1-T5.5 | 已纳入审查。 |
| L2 | 43 | T6.1-T11.5，含 T8.0/T9.0 专题 | 已纳入审查；历史 L2 总体状态由 `docs/audits/L2_overall_review.md` 承接。 |
| L3 | 23 | T17.1-T20.6 | 已纳入审查；内容为 golden model、定点、RTL/ASIC 架构、验证、综合、时序和最终证据报告讲义。 |

## 自动审计基线

| 审计项 | 命令 | 结果 | 说明 |
|:---|:---|:---|:---|
| 术语首现 | `python3 tools/audit_lesson_terms.py docs/L1/T*.md docs/L2_协议算法/T*.md docs/L3/T*.md` | `LESSON_TERM_AUDIT_OK` | 本轮补齐 L1/L2 多篇 3GPP/LTE/NR 标题后首现说明，避免标题被脚本忽略后正文首现失败。 |
| 标题正式化 | `python3 tools/audit_markdown_headings.py docs/L1/T*.md docs/L2_协议算法/T*.md docs/L3/T*.md` | `MARKDOWN_HEADING_AUDIT_OK` | 标题正式化审计通过。 |
| 深度/协议索引风险 | `python3 tools/audit_lesson_depth.py --strict docs/L1/T*.md docs/L2_协议算法/T*.md docs/L3/T*.md` | `LESSON_DEPTH_AUDIT_OK` | 全项目已通过深度审计。 |
| LaTeX 全检 | `python3 tools/audit_latex_render.py docs/L1/T*.md`；`python3 tools/audit_latex_render.py docs/L2_协议算法/T*.md`；`python3 tools/audit_latex_render.py docs/L3/T*.md` | L1 `LATEX_RENDER_AUDIT_OK formulas=2036`；L2 `LATEX_RENDER_AUDIT_OK formulas=3444`；L3 `LATEX_RENDER_AUDIT_OK formulas=948`；合计 6428。 | 全项目 94 篇讲义公式分段全检通过。 |
| 图片几何/可读性 | `python3 tools/audit_figure_geometry.py tools/figures`；`python3 tools/audit_figure_readability.py tools/figures` | `FIGURE_GEOMETRY_AUDIT_OK`；`FIGURE_READABILITY_AUDIT_OK` | 本轮最终收尾已复跑。 |
| 引用重建候选 | `python3 tools/audit_reference_rebuilds.py docs/L1/T*.md docs/L2_协议算法/T*.md docs/L3/T*.md > docs/audits/reference_rebuild_candidates_full.txt` | 退出码 0，候选清单 1320 行 | 该脚本输出候选清单，不是硬失败；需要人工分类为已复现、项目内回链、自写公式、真实工具未运行边界或待核验项。 |

## 总体结论

当前 94 篇讲义具备统一的教学和审计结构：学习目标、前置知识检查、理论解释、协议依据或边界、接收端/工程位置、公式或算法推导、伪代码或 Python 片段、验证方法、自测题与参考答案、执行与证据记录、协议证据表或协议边界、参考文献基本齐全。L1 侧重零基础理论和协议阅读入口，L2 侧重 LTE Turbo、NR LDPC、NR Polar 协议精读和接收端流程，L3 侧重 golden model、定点、RTL/ASIC 和验证证据框架。

全项目当前没有 Critical 或 Important 级文档缺口。必须保留的边界是：L3 的综合、时序、覆盖率、RTL regression、BLER campaign 和最终 sign-off 是讲义和模板，不是真实工程已通过证据；T20.6 已把最终签核状态明确为 `hold`。

## 问题清单

### Critical

无。

### Important

| 问题 | 状态 | 处理 |
|:---|:---|:---|
| 真实 BLER/定点/RTL/coverage/DC/STA 证据未生成 | 非文档缺口，是工程证据边界。 | T20.6 已明确 `hold`，不得宣称真实签核完成。 |
| TS 38.214 MCS/TBS 具体表值未形成系统级 bit-exact 表驱动闭环 | 当前未用于真实 conformance 向量。 | 进入系统级向量阶段后按实际查表范围复现。 |

### Minor

| 问题 | 状态 | 后续控制 |
|:---|:---|:---|
| L1/L2 多篇标题包含 LTE/NR/3GPP，但正文首现缺少脚本要求的固定全称字符串。 | 本轮已在标题后补“本节缩写说明”，术语审计通过。 | 后续新增讲义继续按每篇首现展开。 |
| 引用重建候选脚本输出较多候选。 | 保持人工分类，不把候选行数等同于失败数。 | 修改引用、公式、表格、图片时同步更新证据表。 |
| 图片局部视觉问题历史上多次复发。 | 已写入全局规则、资产清单和静态审计脚本。 | 任一图片新增或重生成后逐图复查。 |

## 逐层状态

| 层级 | Prompt 覆盖 | 拓展充分性 | 协议证据 | 图表/公式 | 自动审计状态 | 状态 |
|:---|:---|:---|:---|:---|:---|:---|
| L1 T1-T5 | 已纳入矩阵 | 以零基础理论、直觉和手算为主 | 基础课明确协议入口和边界 | LaTeX 通过；关键协议表在 T3 复现 | 术语/标题/深度/LaTeX 通过 | 通过 |
| L2 T6-T7 | 已纳入矩阵 | LTE Turbo 译码、rate recovery、HARQ 和边界案例已扩展 | TS 36.212/36.213/36.321 相关锚点已记录，未核验项明确边界 | T6.3/T7.3 等图片已修复并审计 | 术语/标题/深度/LaTeX 通过 | 通过 |
| L2 T8-T9 | 已纳入矩阵 | NR LDPC BG、lifting、BP/MS、rate recovery、CBG/HARQ 已扩展 | TS 38.212/38.214 相关锚点已记录 | BG/lifting、rate recovery、CBG/RV 图表已生成 | 术语/标题/深度/LaTeX 通过 | 通过 |
| L2 T10-T11 | 已纳入矩阵 | NR Polar 与三类译码器对比已扩展 | TS 38.212 Polar 序列和 rate recovery 表已复现或回链 | Polar reliability sequence、rate recovery、对比图已生成 | 术语/标题/深度/LaTeX 通过 | 通过 |
| L3 T12-T13 | 已纳入矩阵 | Python golden model、浮点仿真、定点模型、bit-exact harness 已扩展 | 通过上游 T7/T9/T10 和 Rel-19 路径回链 | 相关工程流程图已生成 | 术语/标题/深度/LaTeX 通过 | 通过 |
| L3 T14-T15 | 已纳入矩阵 | RTL/ASIC、寄存器、soft buffer、testbench、coverage、DC、时序、最终报告已扩展 | 具体 TS 包名、章节、表/图/公式和本地路径在 T20.6 汇总 | T14/T15 架构和证据图已生成 | 术语/标题/深度/LaTeX 通过 | 通过，真实工程签核为 `hold` |

## 后续队列

1. active audit/status 文件已同步到当前范围：94 篇讲义、68 张 PNG、58 个 Python 文件和 6428 条已通过渲染的 LaTeX 公式；图片项目级一致性审计已覆盖资产目录、正文引用、资产清单和迁移台账。
2. 真实工程阶段按 T20.6 schema 补齐 BLER、定点、RTL、coverage、DC、STA 和功耗证据后，再更新最终 sign-off 状态。
