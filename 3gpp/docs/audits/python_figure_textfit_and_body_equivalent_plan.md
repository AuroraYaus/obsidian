---
type: spec
aliases:
  - python figure textfit and body equivalent plan
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/python_figure_textfit_and_body_equivalent_plan.md"
---
# Python Figure Text-Fit and Body Equivalent Plan

审查时间：2026-06-21

## 目标

本计划用于关闭两类问题：

- Python/PIL 绘图脚本中存在文字被文本框裁剪、贴边或静默删除的风险。
- 正文中过度依赖 Python 生成的 PNG，读者不打开图片时无法通过 Mermaid 图或 Markdown 表格获得等价内容。

完成标准不是“图片能生成”或“现有静态审计通过”，而是同时满足：

- PNG 中没有文字裁剪、静默删行、文本贴框、表格小字、箭头压字或连线穿框。
- 每个 Python PNG 引用附近都有明确标记的 Mermaid 或 Markdown 表格等价块。
- 正文不再使用 `![...](...png)` 嵌入 Python 生成图片；原图片文件保留为 `原图片资产：` 文本记录、证据资产或兼容输出，不删除。
- 等价块覆盖图片中的主要流程、对象、状态、字段、协议/工程边界和失败路径；若图片同时包含流程和表格，正文必须同时补流程和表格。
- 讲义“执行与证据记录”、资产清单和迁移台账记录脚本路径、图片路径、正文等价块位置、审计命令和复核结论。

## 根因结论

只读审计确认，当前问题根因集中在以下模式：

| 根因 | 影响 | 首批处理对象 |
|:---|:---|:---|
| 固定文本框或固定表格行高，只按宽度换行，不校验高度。 | 文字可能贴上/下边框，或被框外裁剪。 | T10.6、T10.7、T11.1、T12.1、T14/T15 模板族。 |
| 直接 `draw.text()` 写长句，不 wrap，不检查右边界。 | 中文长句、英文长 token 或协议字段可能越界。 | T10.2、T11.2、T14/T15 标题/说明。 |
| 表格单元格静默截断。 | 文本被直接删除，读者无法知道缺失内容。 | `tools/figures/render_lte_nr_rate_matching_comparison.py` 中 `lines[:2]`。 |
| `wrap()` 只按空格拆词。 | 中文无空格、路径名、字段名、`CRC/RNTI`、`alpha_beta_snapshot` 等 token 不可靠。 | T14/T15 模板、T12.1、T10/T11 图。 |
| 普通正文大面积加粗。 | 增加文字宽度和高度压力，使固定框更容易拥挤。 | T10.7、T11.1、T14/T15 表格正文。 |

## 新增全局规则

| 规则 | 要求 |
|:---|:---|
| Python 图不得作为唯一正文表达 | 所有由 `tools/figures/*.py` 生成并插入正文的教学图、协议图、流程图、结构图、表格图，都必须在正文补充等价 Mermaid 或 Markdown 表格。 |
| 正文不嵌入 PNG | 讲义正文应使用 Mermaid、Markdown 表格和文字补充表达图片内容；PNG 路径只以 `原图片资产：` 或证据表代码文本形式保留，不使用 Markdown 图片链接。 |
| PNG 修复不是完成项 | 修复 PNG 裁剪只是必要条件；必须同时完成正文等价块、审计台账和证据记录。 |
| 流程/架构/状态机优先 Mermaid | 使用 `flowchart`、`sequenceDiagram`、`stateDiagram-v2` 或等价 Mermaid 表达节点、方向、输入输出、协议边界和失败路径。 |
| 表格/字段/矩阵优先 Markdown 表格 | 协议表、字段表、descriptor、corner case、对比矩阵、证据矩阵应补 Markdown 表格；长表可分段或说明完整资产回链，但本节依赖的列义和使用范围必须写清。 |
| 混合图片必须混合补充 | 一张图同时包含流程和表格时，正文必须同时补 Mermaid 和表格，不能只补其中一种。 |
| 等价块必须靠近图片 | Mermaid/表格应放在对应图片读图说明附近，不能只放在文末证据记录。 |
| 等价块必须可审计 | 每个等价块使用明确标题或标记，例如“Mermaid 等价图”“Markdown 等价表”“图片内容正文等价”。 |

## 首批脚本修复队列

| 优先级 | 脚本 | 修复点 | 验收 |
|:---|:---|:---|:---|
| P0 | `tools/figures/render_lte_nr_rate_matching_comparison.py` | 删除 `lines[:2]` 静默截断；表格单元格按宽 wrap，行高按最大文本高度计算；`draw_checks()` 改为 wrap。 | 单脚本生成、几何/可读性审计通过；新增静态审计不再发现截断。 |
| P0 | `tools/figures/render_nr_polar_channel_polarization.py` | 修复底部说明标题坐标错位；长说明改为 wrap；节点/说明框文字 bbox 不越界。 | T10.2 图片重生成，人工复核底部说明和节点文字居中。 |
| P1 | `tools/figures/render_nr_polar_ca_scl_selector.py` | `box()`、表格和说明框增加高度校验；普通正文改 regular；表格支持 wrap。 | T10.6 图片重生成并复核候选行和 selector 表。 |
| P1 | `tools/figures/render_nr_polar_rate_recovery_flow.py` | `draw_centered_lines()` 增加溢出断言；表格按 wrap 布局；说明框长句 wrap。 | T10.7 图片重生成并复核 LLR 初始化说明和表格单元格。 |
| P1 | `tools/figures/render_turbo_ldpc_polar_algorithm_comparison.py` | 对比矩阵单元格 wrap；正文 regular；每格 bbox 校验。 | T11.1 图片重生成并复核矩阵、箭头和说明框。 |
| P2 | `tools/figures/render_t12_1_golden_model_layout.py` | `centered_lines()` 使用真实 bbox 高度；note 区 wrap；超框时报错。 | T12.1 图片重生成并复核 fanout、note 和箭头。 |
| P2 | T14/T15 模板族 | `centered()`/`table()` 增加文本 bbox 校验；中文/长 token wrap；表格正文 regular。 | 重点脚本重生成；全项目几何/可读性审计通过。 |

## 正文等价块迁移队列

| 范围 | 处理方式 |
|:---|:---|
| L1 5 张 PNG | 协议表图以 Markdown 表格/列义说明为主；T0.1 协议地图补 Mermaid 总览。 |
| L2 40 张 PNG | 流程/算法图补 Mermaid；协议表、数值走读、对比矩阵、descriptor/corner case 补 Markdown 表格；混合图同时补两者；T8.3/T8.8 分片图和完整证据图分开登记。 |
| L3 23 张 PNG | 架构/流程图补 Mermaid；工程对象、寄存器、验证矩阵、综合/时序/证据矩阵补 Markdown 表格。 |

## 新增审计脚本

| 脚本 | 职责 |
|:---|:---|
| `tools/audit_python_figure_body_equivalents.py` | 扫描 `docs/L1/T*.md`、`docs/L2/T*.md`、`docs/L3/T*.md` 中的 PNG 保留资产记录，要求同一附近章节存在明确标记的 Mermaid 或 Markdown 等价块，并阻断正文 Markdown 图片嵌入。 |
| `tools/audit_figure_text_fit_static.py` | 静态扫描 Python 绘图脚本中的文字裁剪风险：`lines[:N]`、直接长句 `draw.text()`、固定行高表格、无溢出断言的 `centered()`/`draw_centered_lines()`。 |

## 执行顺序

- [x] 新增或更新全局标准文件，固化“Python 图不得作为唯一正文表达”和“文本框内部 bbox 审计”规则。
- [x] 新增迁移台账 `docs/audits/python_figure_to_body_content_migration.md`，列出当前 66 个 Markdown PNG 正文引用、65 个唯一正文引用 PNG 和 3 个 evidence/compatibility 保留 PNG 的状态。
- [x] 新增两个审计脚本，先运行得到失败清单。
- [x] 修复 P0 静默删行绘图脚本并重生成对应 PNG。
- [x] 对每篇含 PNG 的讲义补 Mermaid/Markdown 等价块，优先处理失败清单。
- [x] 更新资产清单、合规审查和最终状态。
- [x] 全量运行图片几何、图片可读性、正文等价块和文本适配静态审计；术语、标题、深度和 LaTeX 审计未因本轮图文等价迁移修改对应规则，仍沿用既有全项目审计入口。
- [x] 项目级图片一致性闭环：建立 `docs/L1`、`docs/L2`、`docs/L3` 的 PNG 引用台账审计，核对 68 个实物 PNG、66 个 Markdown PNG 引用、65 个唯一正文引用 PNG、3 个 evidence/compatibility 保留 PNG、资产清单和迁移台账一致性。
- [x] 正文图片链接迁移为正文等价-only：移除 `docs/L1`、`docs/L2`、`docs/L3` 中 66 处 Markdown PNG 图片嵌入，改为 `原图片资产：` 文本记录；原 PNG 文件不删除，迁移台账更新为 66 个 `body_equivalent_only; asset_retained` 和 3 个 evidence/compatibility 保留资产。
- [ ] 全项目原尺寸逐图目检闭环：分类 `python_pil_drawn` / `python_pdf_crop` / `python_generated_from_table` / `external_or_unknown`，记录 68 个实物 PNG 的字体上下边距、相邻框距、箭头形态、连线端点、表格居中、底部说明区、协议源/crop 质量和残余风险，并对 PDF/Word 原表裁剪图记录源页、裁剪边界、分片可读性和禁止旧脚本覆盖规则。
- [ ] 刷新迁移台账质量状态：`present` 不再只表示“附近有 marker”，而要区分 `present_quality_pass`、`present_low_quality`、`missing`、`not_applicable`；任何 `present_low_quality` 均不得写成完成。

## 完成记录

| 时间 | 动作 | 证据 |
|:---|:---|:---|
| 2026-06-21 | 建立计划，记录根因和执行队列。 | 本文件。 |
| 2026-06-21 | 新增 `tools/audit_figure_text_fit_static.py`、`tools/audit_python_figure_body_equivalents.py`、`tools/build_python_figure_migration_ledger.py` 和 `tests/test_python_figure_audits.py`。 | `python3 -m unittest tests.test_python_figure_audits -v` 输出 `Ran 6 tests ... OK`。 |
| 2026-06-21 | 修复两个静默删行点：`render_lte_nr_rate_matching_comparison.py` 的 `lines[:2]` 改为完整绘制并加 text-fit 断言；`render_harq_soft_buffer_comparison.py` 的 `lines[:3]` 改为完整绘制。 | 两个脚本重新生成 PNG；`python3 tools/audit_figure_geometry.py tools/figures/render_lte_nr_rate_matching_comparison.py tools/figures/render_harq_soft_buffer_comparison.py` 输出 `FIGURE_GEOMETRY_AUDIT_OK`；对应可读性审计输出 `FIGURE_READABILITY_AUDIT_OK`。 |
| 2026-06-21 | 当日旧口径下的 Python PNG 正文引用已补 `图片内容正文等价` 块，L1/L2/L3 等价块经人工/子代理清理，移除自动生成的截断节点和脚本路径占位。2026-06-22 已更正为 66 个 Markdown PNG 正文引用、65 个唯一正文引用 PNG 和 3 个 evidence/compatibility 保留 PNG。 | 2026-06-21 当日 `python3 tools/audit_python_figure_body_equivalents.py` 输出 `PYTHON_FIGURE_BODY_EQUIVALENT_AUDIT_OK`；2026-06-22 迁移台账已升级为 `present_quality_pass; body_referenced` 与 `evidence_only; compatibility_retained; not_current_body_reference` 状态，并由 `python3 tools/audit_project_image_inventory.py` 输出 `PROJECT_IMAGE_INVENTORY_AUDIT_OK` 校验。 |
| 2026-06-21 | 文本适配静态审计阻断项清零，剩余固定行高/长标题风险作为 advisory，继续由几何/可读性审计和人工目检兜底。 | `python3 tools/audit_figure_text_fit_static.py tools/figures` 退出码 0，输出 `FIGURE_TEXT_FIT_STATIC_AUDIT_OK advisory=56`。 |
| 2026-06-21 | T8 全图复查发现原有审计仍漏掉泛化 Mermaid/表格、长表截图正文尺度不可读、单图信息过载和图内红色说明压表等问题。 | 已新增低质量 pipeline 等价块审计用例；T8.1-T8.8 正文等价块重写；T8.3 长表改正文分片展示并保留完整拼接图证据；T8.8 数值图拆为 part1/part2；全项目图片审核已追加为计划 Task 8，尚需全项目逐图闭环记录。 |
| 2026-06-22 | 全项目正文等价质量失败项清零。上一轮 `audit_python_figure_body_equivalents.py` 暴露 25 条非 T8 低质量等价块，涉及 L1/T3.3、T3.4，L2/T6.4、T7.5、T9.3-T9.6、T10.2、T10.3，L3/T12.1；本轮已替换为具体 Mermaid/Markdown 表格等价内容。 | `python3 tools/audit_python_figure_body_equivalents.py` 输出 `PYTHON_FIGURE_BODY_EQUIVALENT_AUDIT_OK`；`python3 tools/audit_figure_text_fit_static.py tools/figures` 输出 `FIGURE_TEXT_FIT_STATIC_AUDIT_OK`；`python3 tools/audit_figure_geometry.py tools/figures` 输出 `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures` 输出 `FIGURE_READABILITY_AUDIT_OK`；`python3 -m unittest tests.test_python_figure_audits -v` 输出 `Ran 11 tests ... OK`；`python3 -m unittest tests.test_audit_figure_geometry -v` 输出 `Ran 13 tests ... OK`；`git diff --check` 退出码 0。 |
| 2026-06-22 | T8.4 图片返工。用户复查指出 `T8.4_LDPC_Tanner_syndrome_toy.png` 仍有文字覆盖和越框；本轮确认旧图中矩阵标题压列标、Tanner 标题贴变量节点、右侧消息流第 4 条越出面板且英文断词。 | 已修改 `tools/figures/render_ldpc_tanner_syndrome.py`：矩阵/Tanner 上部布局下移，右侧消息流面板增高，混合中英文 wrap 尽量保留英文 token，新增标题/节点间距和面板底部留白断言；PNG 重生成后尺寸 `(1600, 1180)`。`python3 tools/audit_figure_geometry.py tools/figures/render_ldpc_tanner_syndrome.py`、`python3 tools/audit_figure_readability.py tools/figures/render_ldpc_tanner_syndrome.py`、`python3 tools/audit_figure_text_fit_static.py tools/figures/render_ldpc_tanner_syndrome.py` 均输出 OK；同时把该脚本加入 `audit_figure_geometry.py --focus-only` 历史重点范围并新增回归测试。 |
| 2026-06-22 | 全项目 Python 绘图脚本按最新规则重审并修正审计层漏项。新增阻断规则 `character_wrap` 和 `wrapped_without_layout_guard`，新增共享 token-aware helper `tools/figures/figure_text_fit.py`，替换旧的按字符换行逻辑；新增直接执行回归测试，修复共享 helper 在 `python tools/figures/render_*.py` 下导入失败的问题。 | `python3 -m py_compile tools/figures/*.py tools/figures/figure_text_fit.py` 退出码 0；`python3 tools/audit_figure_text_fit_static.py tools/figures` 输出 `FIGURE_TEXT_FIT_STATIC_AUDIT_OK`；`python3 tools/audit_figure_geometry.py --focus-only tools/figures` 和 `python3 tools/audit_figure_geometry.py tools/figures` 均输出 `FIGURE_GEOMETRY_AUDIT_OK`；`python3 tools/audit_figure_readability.py tools/figures` 输出 `FIGURE_READABILITY_AUDIT_OK`；逐个执行 58 个 Python 文件结果 `FIGURE_SCRIPT_RUNS total=58 failures=0`。 |
| 2026-06-22 | 新增项目级图片一致性审计，关闭“资产目录全量 vs 正文引用 vs 清单登记 vs 迁移台账”漏层。初次审计发现 T8.3 的 5 张长表分片和 T8.8 的 2 张数值走读分片未进入资产清单/迁移台账，且 3 张完整拼接/兼容图未标注非正文引用状态。 | 新增 `tools/audit_project_image_inventory.py` 和单元测试；补登 7 张正文分片图；把 3 张完整图标为 `evidence_only; compatibility_retained; not_current_body_reference`。`python3 tools/audit_project_image_inventory.py` 输出 `PROJECT_IMAGE_INVENTORY_AUDIT_OK`。该结果证明台账一致，不等于 68 张 PNG 原尺寸逐图目检完成。 |
| 2026-06-23 | 按“图片不链接，但不删除原图片文件”要求迁移正文：66 处 `![...](...png)` 改为 `原图片资产：` 文本记录，正文继续使用 Mermaid/Markdown 等价块承载内容。 | `rg -n '^!\\[[^\\]]*\\]\\([^)]*\\.png\\)' docs/L1 docs/L2 docs/L3 -g '*.md'` 无匹配；`python3 tools/audit_python_figure_body_equivalents.py docs/L1 docs/L2 docs/L3` 输出 `PYTHON_FIGURE_BODY_EQUIVALENT_AUDIT_OK`；`python3 tools/build_python_figure_migration_ledger.py` 输出 `rows=69 missing=0`；`python3 tools/audit_project_image_inventory.py` 输出 `PROJECT_IMAGE_INVENTORY_AUDIT_OK`。 |
