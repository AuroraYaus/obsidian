---
type: spec
aliases:
  - image asset inventory
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/image_asset_inventory.md"
---
# Python Figure Asset Inventory

审查时间：2026-06-21  
范围：`docs/L1_基础/assets/*.png`、`docs/L2_协议算法/assets/*.png`、`docs/L3_工程实现/assets/*.png`、`tools/archive_python_drawing/figures/*.py`。  
结论：当前 `docs/L1_基础/L2/L3/assets` 共有 68 张 PNG，其中 L1 5 张、L2 40 张、L3 23 张；`tools/figures` 共有 58 个 Python 文件，其中 57 个 `render_*.py` 绘图脚本和 1 个共享 helper `figure_text_fit.py`。只读边界检查只能证明文件没有明显贴边裁切，不能证明视觉审计通过；本清单记录资产、脚本、来源和历史风险。2026-08-07 绘图政策变更：Python 绘图工具已归档 `tools/archive_python_drawing/`，视觉验证统一走 `tools/audit_svg_layout.py`（SVG）与 `tools/audit_plantuml_syntax.sh`（PlantUML 渲染）。

当前加严标准：表格正文、表头、首列、图例和说明框教学文字原则上不低于 24px，表格行高原则上不低于 56px；20-23px 只允许作为坐标轴刻度、码位小标签、环形缓存短索引等辅助标注，并必须有更大字号的说明区补偿。旧的 20px/48px 记录只作为历史快照，不再作为当前验收门槛。

最终审计记录：2026-06-21 全项目最终复跑，`python3 tools/archive_python_drawing/audit_figure_readability.py tools/figures` 输出 `FIGURE_READABILITY_AUDIT_OK`，`python3 tools/archive_python_drawing/audit_figure_geometry.py tools/figures` 输出 `FIGURE_GEOMETRY_AUDIT_OK`，`PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/archive_python_drawing/audit_figure_geometry.py tools/archive_python_drawing/audit_figure_readability.py tests/test_audit_figure_geometry.py tools/archive_python_drawing/figures/*.py` 无输出且退出码为 0，`python3 -m unittest tests/test_audit_figure_geometry.py` 输出 `Ran 13 tests OK`。新增 T0.1 协议地图图已纳入清单，单图几何/可读性审计通过；新增/更新 T8.3 BG regions/QC 接收端图已纳入清单，单脚本几何/可读性审计通过。历史图片规则和 T17.1/T19.4/T7.3/T9.3 等重点修复记录仍见下方各资产行。

2026-06-21 本轮补充审计：新增正文等价块审计和文本适配静态审计。`python3 tools/archive_python_drawing/audit_python_figure_body_equivalents.py` 输出 `PYTHON_FIGURE_BODY_EQUIVALENT_AUDIT_OK`，迁移台账后续已升级为区分 `present_quality_pass; body_referenced`、`evidence_only` 和 `not_current_body_reference` 的状态，不再只用 `present` 表示通过。`python3 tools/archive_python_drawing/audit_figure_text_fit_static.py tools/figures` 输出 `FIGURE_TEXT_FIT_STATIC_AUDIT_OK advisory=56`；本轮已消除静默删行阻断项，剩余 advisory 为固定行高或长标题/说明的保守提示，继续由几何/可读性审计和逐图人工目检兜底。

2026-06-21 T8 复查修正：用户反馈 T8 全部图片仍有问题后，重新人工联系表审查 T8.1-T8.8。修正包括：T8.3 BG1/BG2 协议长表正文改用 PDF 原表分片图，完整拼接图保留作证据；T8.8 数值走读改为 part1/part2 两张正文图，兼容合并图保留；T8.3 BG regions 图移除压住 HARQ 框的红色小字；T8.5 syndrome 说明下移避开数值表；T8.3/T8.4/T8.5/T8.6/T8.7 裁掉无效底部空白。T8 正文等价块已重写为具体 Mermaid/Markdown 内容并通过单组审计。全项目图片审核已新增为 `docs/superpowers/plans/2026-06-21-python-figure-body-equivalents.md` Task 8，后续必须补全 68 个实物 PNG、65 个唯一正文引用 PNG 和 3 个证据/兼容保留 PNG 的逐图目检闭环。

2026-06-22 全项目正文等价质量复查：`python3 tools/archive_python_drawing/audit_python_figure_body_equivalents.py` 已从 25 条低质量失败清零，输出 `PYTHON_FIGURE_BODY_EQUIVALENT_AUDIT_OK`。本轮补强了 L1/T3.3、T3.4，L2/T6.4、T7.5、T9.3-T9.6、T10.2、T10.3，L3/T17.1 的图片正文等价块；这些块不再使用“输入字段/地址转换/译码器消费/验证输出”模板，而改为具体协议表列义、图中对象、地址/CRC/soft-buffer/工程证据流。同期全项目脚本级审计 `audit_figure_text_fit_static.py`、`audit_figure_geometry.py`、`audit_figure_readability.py` 均输出 OK；逐图人工目检台账仍按 Task 8 作为更细粒度持续控制项。

2026-06-22 T8.4 返工记录：用户指出 `docs/L2_协议算法/assets/T8.4_LDPC_Tanner_syndrome_toy.png` 仍有文字覆盖和文本越框。复查确认旧图存在左侧矩阵标题压 `v0..v3` 列标、Tanner 标题贴近变量节点、右侧消息流第 4 条越出面板和 `syndrome` 断词问题。已修改 `tools/archive_python_drawing/figures/render_ldpc_tanner_syndrome.py`：矩阵和 Tanner 节点下移、右侧面板增高、混合中英文 wrap 尽量保留英文 token、脚本内新增标题/节点间距和面板底部留白断言，PNG 重生成后尺寸为 `(1600, 1180)`。同时把该脚本加入 `audit_figure_geometry.py --focus-only` 历史重点范围，防止后续全局审计漏掉固定布局风险。

2026-06-22 最新规则全量脚本审核：按用户要求重新审核 `tools/archive_python_drawing/figures/*.py`。先运行 `python3 tools/archive_python_drawing/audit_figure_text_fit_static.py tools/figures`、`python3 tools/archive_python_drawing/audit_figure_geometry.py tools/figures`、`python3 tools/archive_python_drawing/audit_figure_geometry.py --focus-only tools/figures`、`python3 tools/archive_python_drawing/audit_figure_readability.py tools/figures`，四项均输出 OK；再逐个执行 58 个 Python 文件以触发脚本内部 bbox、间距、底部留白和穿框断言，结果 `FIGURE_SCRIPT_RUNS total=58 failures=0`，其中 `figure_text_fit.py` 是 helper 自检，57 个 `render_*.py` 是绘图脚本。执行过程中曾暴露共享 helper 在直接执行 `python tools/archive_python_drawing/figures/render_*.py` 时 `ModuleNotFoundError: No module named 'tools'`，已新增直接执行回归测试并为相关脚本加本地导入回退。脚本重生成后复跑同四项审计仍全部 OK，并复跑 `python3 tools/archive_python_drawing/audit_python_figure_body_equivalents.py docs/L1_基础 docs/L2_协议算法 docs/L3_工程实现` 输出 `PYTHON_FIGURE_BODY_EQUIVALENT_AUDIT_OK`。该记录是脚本级和自动规则级闭环；逐 PNG 原尺寸人工目检仍按 Task 8 单独推进。

2026-06-22 项目级图片一致性审计：新增 `tools/audit_project_image_inventory.py`，用于补足旧审计没有覆盖的“资产目录全量、Markdown 正文引用、资产清单、迁移台账”一致性层。初次运行暴露 7 张正文正在引用的 T8.3/T8.8 分片图未登记，以及 3 张完整拼接/兼容图未标明 evidence/compatibility 状态；本轮已补登记并把迁移台账状态升级为 `present_quality_pass; body_referenced` 或 `evidence_only; compatibility_retained; not_current_body_reference`。该审计只验证项目级台账一致性，不证明 PNG 原尺寸人工目检完成。

2026-06-23 正文图片链接迁移：按“图片不链接，但不删除原图片文件”要求，`docs/L1_基础`、`docs/L2_协议算法`、`docs/L3_工程实现` 中 66 处 Markdown PNG 图片嵌入已改为 `原图片资产：` 文本记录；正文内容由相邻 Mermaid、Markdown 表格和文字补充承接。迁移台账现为 69 行，其中 66 个 `body_equivalent_only; asset_retained` 正文保留资产记录和 3 个 `evidence_only; compatibility_retained; not_current_body_reference` 完整拼接/兼容保留资产。`python3 tools/archive_python_drawing/audit_python_figure_body_equivalents.py docs/L1_基础 docs/L2_协议算法 docs/L3_工程实现`、`python3 tools/audit_project_image_inventory.py` 均输出 OK；PNG 文件继续保留在 assets 目录，不作为正文图片链接展示。

新增静态审计入口：`python3 tools/archive_python_drawing/audit_figure_geometry.py --focus-only tools/figures`。该脚本用于暴露历史重点图脚本中的固定坐标箭头、左上角表格文字、固定 y 底部说明框、缺少间距断言等风险；它不能替代人工目检，也不能证明图片美观。初次运行曾暴露 T10.7、T11.1 和 T10.2 的脚本级风险；已修复为居中 helper、真实边界连线和局部间距/底部留白断言驱动，当前重点图范围输出 `FIGURE_GEOMETRY_AUDIT_OK`。后续脚本修改仍需继续运行该命令并逐图目检。

## 2026-08-04 全量 SVG 迁移记录

- 用户要求"PNG 图都美化并作相同处理"：57 张 PIL 脚本渲染的教学图全部迁移为**手绘 SVG**（布局与配色依据各讲义正文语义重新设计，不参考任何已有图片内容；几何审计 + cairosvg 渲染验证通过，语义与数据与原脚本一致）。原 57 个 `render_*.py` 脚本与 PNG 已删除（git 可恢复）。
- **12 张协议证据表图保留 PNG 不动**（PDF/CSV 来源的协议原表，符合"必须从 source.pdf 裁剪"红线）：L1 `T3.2_*_original_crop`、`T3.3_*`、`T3.4_*_BG1/BG2`；L2 `T8.3_*_shift_table*`（7 张）、`T10.3_*_Polar_sequence`。
- 新审计工具：`tools/audit_svg_layout.py`（五规则几何审计）投入使用；`tools/archive_python_drawing/audit_figure_geometry.py` 的 HISTORICAL_FOCUS 已移除全部已删脚本。
- 历史命名差异修正：讲义正文引用（T17.x/T18.x/T19.x/T20.x 章节引用 T12.x-T15.x 资产）原为死链，已全部改为真实 SVG 路径；本清单 L3 表的历史行因沿用旧命名未批量改写，以实际 `docs/L3_工程实现/assets/` 目录为准。
- 上方各资产行的 Script/Status 列已按迁移状态批量更新；历史审计段落保持原样。

## 2026-08-05 资产编号统一记录

- 讲义重编号后（L3 讲义为 T17-T21 系列），资产编号与讲义编号不一致（资产 T12.x-T15.x 对应讲义 T17.x-T20.x）。已按讲义编号统一重命名 23 个资产（T12.1→T17.1 … T15.6→T20.6），全库 35 个 md 引用与全部 SVG @file 头同步更新，旧编号引用零残留（历史计划文档除外）。
- 文档内图片序号（图 N）按出现顺序全库重排，5 个乱序文件已修复。

## 清单字段

| 字段 | 含义 |
|:---|:---|
| Asset | 图片文件路径。 |
| Script | 生成脚本。 |
| Source/Evidence | 输入数据、协议来源或教学来源。 |
| Used By | 正文使用位置。 |
| Status | 当前资产状态。 |
| Visual Risk | 历史反馈或后续重点检查点。 |
后续刷新本清单时，应新增两列：`Global Rule Tags` 和 `Audit Method`。`Global Rule Tags` 用于标记 `center`、`font-size`、`arrow-boundary`、`bottom-margin`、`local-spacing` 等必须检查的规则；`Audit Method` 用于记录边界检查、静态几何审计和逐图局部视觉清单的证据。当前表仍沿用既有字段，避免在并行整改期间机械改写每一行状态。

## L1 Assets

| Asset | Script | Source/Evidence | Used By | Status | Visual Risk |
|:---|:---|:---|:---|:---|:---|
| `docs/L1_基础/assets/T0.1_LTE_NR_decoder_protocol_reading_map.png` | 已删除（2026-08-04，SVG 迁移） | LTE/NR 译码协议阅读地图教学图；TS 36.211/36.212/36.213/36.321/36.331 与 TS 38.211/38.212/38.213/38.214/38.321/38.331 的译码边界。 | 2026-08-04 已迁移为手绘 SVG `T0.1_LTE_NR_decoder_protocol_reading_map.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 2026-06-21 新增；单图几何/可读性审计通过，全项目几何/可读性审计通过。 | 作为总览图，后续新增协议路径时需保持协议源、接收端对象、译码器输入输出和审计证据四类区块的间距、文本居中和箭头端点。 |
| `docs/L1_基础/assets/T3.2_TS36.212_Table_5.1.3-3_original_crop.png` | 协议证据保留（source.pdf 裁剪，`pdftoppm` 提取） | TS 36.212 Table 5.1.3-3 原文截图，Turbo 内部交织器参数表。 | T3.2 | 2026-08-04 SVG 迁移后保留的 12 张协议证据表图之一。 | 协议原表裁剪，不得替换为手绘重绘。 |
| `docs/L1_基础/assets/T3.3_TS36.212_Table_5.1.3-3.png` | `tools/archive_python_drawing/figures/render_lte_turbo_interleaver_table.py` | TS 36.212 `tables/table_0009.csv/html`；Table 5.1.3-3。 | T3.3, T6.4 | 已删除（2026-08-07 与 T3.2 重复，用户指示共用 `T3.2_..._original_crop.png`，git 可恢复）。 | 原 2x2 分面长表，表头/首列/正文 24px+/56px+。 |
| `docs/L1_基础/assets/T3.4_TS38.212_Table_5.3.2-1_lifting_sets.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_tables.py` | TS 38.212 `tables/table_0013.csv/html`；Table 5.3.2-1。 | T3.4 | 边界检查通过。 | 长表缩放阅读字号。 |
| `docs/L1_基础/assets/T3.4_TS38.212_Table_5.3.2-2_BG1.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_bg_tables_from_pdf.py` | TS 38.212 `source.pdf` 第 21-23 页；`tables/table_0014.csv/html` 用于结构化核验；Table 5.3.2-2。 | T3.4 | 2026-06-21 已替换为 Word/PDF 原表裁剪拼接图，尺寸 `(1560, 4554)`。 | 不再使用 Python 手绘长表；后续若重生成，必须从 `source.pdf` 裁剪，不能用旧 CSV 重绘脚本覆盖。 |
| `docs/L1_基础/assets/T3.4_TS38.212_Table_5.3.2-3_BG2.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_bg_tables_from_pdf.py` | TS 38.212 `source.pdf` 第 23-24 页；`tables/table_0015.csv/html` 用于结构化核验；Table 5.3.2-3。 | T3.4 | 2026-06-21 已替换为 Word/PDF 原表裁剪拼接图，尺寸 `(1560, 2941)`。 | 不再使用 Python 手绘长表；后续若重生成，必须从 `source.pdf` 裁剪，不能用旧 CSV 重绘脚本覆盖。 |

## L2 Assets

| Asset | Script | Source/Evidence | Used By | Status | Visual Risk |
|:---|:---|:---|:---|:---|:---|
| `docs/L2_协议算法/assets/T6.3_TS36.212_Figure_5.1.3-2_turbo_encoder_rebuild.png` | 已删除（2026-08-04，SVG 迁移） | TS 36.212 Figure 5.1.3-2；`media/image79.wmf`；Word relationship `rId87`。 | 2026-08-04 已迁移为手绘 SVG `T6.3_TS36.212_Figure_5.1.3-2_turbo_encoder_rebuild.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；底部说明区、终止路径和关键 token 已放大并通过几何/可读性审计，当前尺寸 `(2040, 1650)`。2026-06-20 已修复箭头线身画到三角尖端的旧实现，重生成并通过全项目审计。 | 曾发生底部说明框局部视觉审计漏检；现已按 24px+ 主体文字和 bbox-based 居中说明区处理，继续重点关注底部留白。目检箭头头部方向与线段方向一致，线身在头部前停止。 |
| `docs/L2_协议算法/assets/T7.3_LTE_HARQ_RV_windows.png` | 已删除（2026-08-04，SVG 迁移） | LTE HARQ/RV circular-buffer 教学重建；TS 36.212 §5.1.4.1.2。 | 2026-08-04 已迁移为手绘 SVG `T7.3_LTE_HARQ_RV_windows.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；`2220x2760` 可读性整改已完成，`FIGURE_GEOMETRY_AUDIT_OK`、`FIGURE_READABILITY_AUDIT_OK`。2026-06-20 已修复 `draw_arrow()` 线身画到箭头尖端的问题；本轮进一步把箭头翼点改为同一回退点的法向量展开，重生成并复检。2026-06-21 复核脚本中环形地址索引为 24px。 | 必须保持 4 个 RV 在 ring buffer 上的位置、soft combining、两行 LLR/地址 chips 和底部说明框间距；目检斜向说明箭头和垂直箭头的头部方向、线身截断和翼点对称均与实际线段一致。 |
| `docs/L2_协议算法/assets/T7.5_LTE_DL_UL_decoder_context.png` | 已删除（2026-08-04，SVG 迁移） | LTE DL/UL decoder context 教学图。 | 2026-08-04 已迁移为手绘 SVG `T7.5_LTE_DL_UL_decoder_context.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；两侧面板、负例区和说明条已放大并通过几何/可读性审计，当前尺寸 `(1920, 1600)`。2026-06-20 已把固定向下三角箭头 helper 改为 start/end 向量箭头并重生成，单图几何/可读性审计通过。 | 历史上修复过箭头/文本框重叠；已按 24px+ 重新布局说明框、soft buffer key 和底部负例区。目检垂直箭头头部由实际线段向量生成，线身在头部前停止。 |
| `docs/L2_协议算法/assets/T8.1_NR_LDPC_decoder_chain_overview.png` | 已删除（2026-08-04，SVG 迁移） | NR LDPC 接收链路教学图。 | 2026-08-04 已迁移为手绘 SVG `T8.1_NR_LDPC_decoder_chain_overview.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；已重生成。 | 节点、协议锚点和 descriptor 区块已加宽；仍保留长链路图中极少量英文术语小字号。 |
| `docs/L2_协议算法/assets/T8.2_NR_LDPC_base_graph_selection_flow.png` | 已删除（2026-08-04，SVG 迁移） | TS 38.212 BG 选择公式教学图。 | 2026-08-04 已迁移为手绘 SVG `T8.2_NR_LDPC_base_graph_selection_flow.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；已重生成。 | 已增大画布、分支卡片和表格行高；BG 选择表中的“默认/输出”少量短索引属于有意保留的例外。 |
| `docs/L2_协议算法/assets/T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_bg_tables_from_pdf.py` | TS 38.212 `source.pdf` 第 21-23 页；`tables/table_0014.csv/html` 用于结构化核验。 | T8.3 | 完整拼接证据图保留，尺寸 `(1560, 4554)`；正文改引用 `_part1/_part2/_part3` 三张分片图。 | 长表不得作为正文唯一单图展示；后续若重生成，必须从 `source.pdf` 裁剪并保持分片图，不能用旧 CSV 手绘覆盖。 |
| `docs/L2_协议算法/assets/T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table_part1.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_bg_tables_from_pdf.py` | TS 38.212 `source.pdf` 第 21 页；`tables/table_0014.csv/html` 用于结构化核验。 | T8.3 | 正文主用分片图，当前纳入项目级图片一致性审计。 | PDF/Word 原表裁剪分片；必须保持源页、裁剪边界和分片可读性，不得由旧 CSV/PIL 手绘长表替换。 |
| `docs/L2_协议算法/assets/T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table_part2.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_bg_tables_from_pdf.py` | TS 38.212 `source.pdf` 第 22 页；`tables/table_0014.csv/html` 用于结构化核验。 | T8.3 | 正文主用分片图，当前纳入项目级图片一致性审计。 | PDF/Word 原表裁剪分片；必须保持源页、裁剪边界和分片可读性，不得由旧 CSV/PIL 手绘长表替换。 |
| `docs/L2_协议算法/assets/T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table_part3.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_bg_tables_from_pdf.py` | TS 38.212 `source.pdf` 第 23 页；`tables/table_0014.csv/html` 用于结构化核验。 | T8.3 | 正文主用分片图，当前纳入项目级图片一致性审计。 | PDF/Word 原表裁剪分片；必须保持源页、裁剪边界和分片可读性，不得由旧 CSV/PIL 手绘长表替换。 |
| `docs/L2_协议算法/assets/T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_bg_tables_from_pdf.py` | TS 38.212 `source.pdf` 第 23-24 页；`tables/table_0015.csv/html` 用于结构化核验。 | T8.3 | 完整拼接证据图保留，尺寸 `(1560, 2941)`；正文改引用 `_part1/_part2` 两张分片图。 | 长表不得作为正文唯一单图展示；后续若重生成，必须从 `source.pdf` 裁剪并保持分片图，不能用旧 CSV 手绘覆盖。 |
| `docs/L2_协议算法/assets/T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table_part1.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_bg_tables_from_pdf.py` | TS 38.212 `source.pdf` 第 23 页；`tables/table_0015.csv/html` 用于结构化核验。 | T8.3 | 正文主用分片图，当前纳入项目级图片一致性审计。 | PDF/Word 原表裁剪分片；必须保持源页、裁剪边界和分片可读性，不得由旧 CSV/PIL 手绘长表替换。 |
| `docs/L2_协议算法/assets/T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table_part2.png` | `tools/archive_python_drawing/figures/render_nr_ldpc_bg_tables_from_pdf.py` | TS 38.212 `source.pdf` 第 24 页；`tables/table_0015.csv/html` 用于结构化核验。 | T8.3 | 正文主用分片图，当前纳入项目级图片一致性审计。 | PDF/Word 原表裁剪分片；必须保持源页、裁剪边界和分片可读性，不得由旧 CSV/PIL 手绘长表替换。 |
| `docs/L2_协议算法/assets/T8.3_NR_LDPC_BG_regions_QC_receiver.png` | 已删除（2026-08-04，SVG 迁移） | NR LDPC BG 五子矩阵、QC lifting 和接收端 memory 视角教学图。 | 2026-08-04 已迁移为手绘 SVG `T8.3_NR_LDPC_BG_regions_QC_receiver.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 2026-06-21 T8 复查后重生成，当前尺寸 `(2200, 1080)`。 | 已移除右下角压住 HARQ view 的红色小字；必须保持 A/B/C/D/E、QC lifting、receiver pipeline 三栏清晰。 |
| `docs/L2_协议算法/assets/T8.3_NR_LDPC_toy_QC_expansion.png` | 已删除（2026-08-04，SVG 迁移） | Toy QC-LDPC expansion 教学图。 | 2026-08-04 已迁移为手绘 SVG `T8.3_NR_LDPC_toy_QC_expansion.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 2026-06-21 T8 复查后重生成，当前尺寸 `(1640, 800)`。 | 已裁掉底部空白；继续保持 `B -> P^0/P^1/P^2/zero -> H` 的 toy 展开语义，正文等价块不得混入 receiver pipeline。 |
| `docs/L2_协议算法/assets/T8.4_LDPC_Tanner_syndrome_toy.png` | 已删除（2026-08-04，SVG 迁移） | Toy Tanner/syndrome 教学图。 | 2026-08-04 已迁移为手绘 SVG `T8.4_LDPC_Tanner_syndrome_toy.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 2026-06-22 返工重生成，当前尺寸 `(1600, 1180)`；单脚本几何/可读性/文本适配静态审计通过，并纳入 `--focus-only` 历史重点范围。 | 已修复矩阵标题压列标、Tanner 标题贴节点、右侧消息流越框和英文断词；脚本内有标题/节点间距与面板底部留白断言。继续重点复查矩阵、Tanner 边、syndrome panel 和右侧消息流入口。 |
| `docs/L2_协议算法/assets/T8.5_LDPC_BP_SPA_one_round.png` | 已删除（2026-08-04，SVG 迁移） | Toy BP/SPA one-round 教学图。 | 2026-08-04 已迁移为手绘 SVG `T8.5_LDPC_BP_SPA_one_round.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 2026-06-21 T8 复查后重生成，当前尺寸 `(1600, 1120)`。 | 已把红色 syndrome 说明下移避开数值表；公式、三张数值表和底部工程检测点需保持 24px+ 可读。 |
| `docs/L2_协议算法/assets/T8.6_LDPC_MS_NMS_OMS_compare.png` | 已删除（2026-08-04，SVG 迁移） | Min-Sum/NMS/OMS comparison 教学图。 | 2026-08-04 已迁移为手绘 SVG `T8.6_LDPC_MS_NMS_OMS_compare.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 2026-06-21 T8 复查后重生成，当前尺寸 `(1600, 1120)`。 | 已裁掉底部空白；对比表列标题仍需在正文等价表完整承接。 |
| `docs/L2_协议算法/assets/T8.7_LDPC_layered_schedule_flow.png` | 已删除（2026-08-04，SVG 迁移） | Flooding/layered schedule 教学图。 | 2026-08-04 已迁移为手绘 SVG `T8.7_LDPC_layered_schedule_flow.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 2026-06-21 T8 复查后重生成，当前尺寸 `(1920, 1400)`。 | 已裁掉底部空白；右侧 layer 表、Zc 地址公式和底部验证日志必须由正文等价块承接。 |
| `docs/L2_协议算法/assets/T8.8_LDPC_numeric_walkthrough.png` | 已删除（2026-08-04，SVG 迁移） | Toy LDPC numeric walkthrough 教学图。 | 2026-08-04 已迁移为手绘 SVG `T8.8_LDPC_numeric_walkthrough.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 兼容合并图保留，当前尺寸 `(2000, 2220)`；正文改引用 `T8.8_LDPC_numeric_walkthrough_part1.png` `(2000, 900)` 和 `part2.png` `(2000, 1320)`。 | 单张高图不再作为正文主图；part1 承接 H/初始/CN messages，part2 承接 posterior/early stop/debug fields。 |
| `docs/L2_协议算法/assets/T8.8_LDPC_numeric_walkthrough_part1.png` | 已删除（2026-08-04，SVG 迁移） | Toy LDPC numeric walkthrough 第一分片。 | 2026-08-04 已迁移为手绘 SVG `T8.8_LDPC_numeric_walkthrough_part1.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 正文主用分片图，当前纳入项目级图片一致性审计。 | 承接 H 矩阵、初始 LLR/hard decision、initial syndrome 和 CN message 表；必须与 part2 共同复核，不能只看单张图。 |
| `docs/L2_协议算法/assets/T8.8_LDPC_numeric_walkthrough_part2.png` | 已删除（2026-08-04，SVG 迁移） | Toy LDPC numeric walkthrough 第二分片。 | 2026-08-04 已迁移为手绘 SVG `T8.8_LDPC_numeric_walkthrough_part2.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 正文主用分片图，当前纳入项目级图片一致性审计。 | 承接 posterior LLR、updated hard decision、early stop 和 debug fields；必须与 part1 共同复核，兼容合并图只作证据保留。 |
| `docs/L2_协议算法/assets/T9.1_NR_LDPC_rate_recovery_overview.png` | 已删除（2026-08-04，SVG 迁移） | NR LDPC rate recovery 教学图。 | 2026-08-04 已迁移为手绘 SVG `T9.1_NR_LDPC_rate_recovery_overview.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；已重生成。 | 说明框与 descriptor 表已重新留白；仍保留少量短索引和 `Qm` / `Ncb` 这类协议缩写。 |
| `docs/L2_协议算法/assets/T9.2_NR_LDPC_circular_buffer_states.png` | 已删除（2026-08-04，SVG 迁移） | Circular buffer 状态教学图。 | 2026-08-04 已迁移为手绘 SVG `T9.2_NR_LDPC_circular_buffer_states.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；已重生成。 | legend、错误对照表和底部结论间距已扩大；纯位置索引 `pos 0..11` 属于例外。 |
| `docs/L2_协议算法/assets/T9.3_NR_LDPC_HARQ_CBG_RV.png` | 已删除（2026-08-04，SVG 迁移） | NR LDPC HARQ/CBG/RV 教学图。 | 2026-08-04 已迁移为手绘 SVG `T9.3_NR_LDPC_HARQ_CBG_RV.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；2026-06-20 已修复箭头线身画到尖端后叠三角头的问题；本轮进一步把箭头翼点改为同一回退点的法向量展开，重生成并通过全项目几何/可读性审计。 | 历史上修复过 RV2 地址/重复说明；后续检查 CBG 保持/合并语义。目检 TB->CBG、CBG->CB 箭头头部方向、线身截断和翼点对称均与实际线段一致。 |
| `docs/L2_协议算法/assets/T9.4_NR_LDPC_bit_deinterleaving.png` | 已删除（2026-08-04，SVG 迁移） | TS 38.212 bit interleaving 教学图。 | 2026-08-04 已迁移为手绘 SVG `T9.4_NR_LDPC_bit_deinterleaving.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；已重生成。 | `Qm`、`f_i/e_i` 与 bit 索引属协议短标识，保留小字号但不再硬拆 token。 |
| `docs/L2_协议算法/assets/T9.5_NR_LDPC_reassembly_TB_CRC.png` | 已删除（2026-08-04，SVG 迁移） | NR LDPC CB/TB CRC 教学图。 | 2026-08-04 已迁移为手绘 SVG `T9.5_NR_LDPC_reassembly_TB_CRC.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过。 | 重组流程和 CRC 边界框间距。 |
| `docs/L2_协议算法/assets/T9.6_NR_LDPC_edge_case_diagnosis.png` | 已删除（2026-08-04，SVG 迁移） | NR LDPC edge-case diagnosis 教学图。 | 2026-08-04 已迁移为手绘 SVG `T9.6_NR_LDPC_edge_case_diagnosis.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；已重生成。 | 多故障卡片字号和最小 dump 包间距已增大；少量协议字段缩写保持原样。 |
| `docs/L2_协议算法/assets/T10.1_NR_Polar_decoder_chain_overview.png` | 已删除（2026-08-04，SVG 迁移） | NR Polar receiver chain 教学图。 | 2026-08-04 已迁移为手绘 SVG `T10.1_NR_Polar_decoder_chain_overview.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；2026-06-20 已按可读性规则重生成，单脚本几何/可读性审计均通过。 | 已放大节点正文、标签 chips 和底部工程检查点；目检链路节点、CRC/RNTI selector 间距和说明框留白通过。 |
| `docs/L2_协议算法/assets/T10.2_NR_Polar_N4_transform_frozen_mask.png` | 已删除（2026-08-04，SVG 迁移） | N=4 Polar transform 教学图。 | 2026-08-04 已迁移为手绘 SVG `T10.2_NR_Polar_N4_transform_frozen_mask.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；已修复节点和连线。 | 曾发生节点过小、文字不居中、连线端点不贴边问题；后续重点检查节点 bbox 和箭头端点。 |
| `docs/L2_协议算法/assets/T10.3_TS38.212_Table_5.3.1.2-1_Polar_sequence.png` | `tools/archive_python_drawing/figures/render_nr_polar_reliability_sequence.py` | TS 38.212 `tables/table_0012.csv/html`；Table 5.3.1.2-1。 | T10.3 | 边界检查通过；2026-06-20 已重生成，单脚本几何/可读性审计通过，当前尺寸 `(2060, 7640)`。 | 完整 1024 项长图保留码位短索引例外：`rank/Q(rank)` 作为短索引展示；标题、表头、脚注和 56px+ 行高已放大，目检可接受。 |
| `docs/L2_协议算法/assets/T10.4_NR_Polar_SC_N4_tree.png` | 已删除（2026-08-04，SVG 迁移） | N=4 Polar SC tree 教学图。 | 2026-08-04 已迁移为手绘 SVG `T10.4_NR_Polar_SC_N4_tree.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；2026-06-20 二次加严后重生成，当前尺寸 `(2100, 1460)`。本轮修复 `elbow_arrow()` 最后一段线身画到箭头尖端的问题，并追加 partial-sum 回传路径 segment-rectangle 相交断言。 | 树节点、partial sum、箭头间距和底部函数约定均已按 24px+ 主体文字复查。后续全局穿框审计发现旧绿色回传斜段穿过 `再译 u2,u3` 框，已改为左侧短折线路径并用 `assert_no_unrelated_crossing()` 检查不穿 `再译 u2,u3` 和合成框；该线属于 SC partial-sum 回传/避让路径例外，不作为普通流程直线。 |
| `docs/L2_协议算法/assets/T10.5_NR_Polar_SCL_N4_L2_paths.png` | 已删除（2026-08-04，SVG 迁移） | N=4/L=2 SCL path pruning 教学图。 | 2026-08-04 已迁移为手绘 SVG `T10.5_NR_Polar_SCL_N4_L2_paths.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；2026-06-20 已重生成，单脚本几何/可读性审计通过。 | 路径表已抬升到 24px+/62px 行高，单元格居中；目检路径复制/剪枝箭头和底部说明框留白通过。 |
| `docs/L2_协议算法/assets/T10.6_NR_Polar_CA_SCL_final_selector.png` | 已删除（2026-08-04，SVG 迁移） | CA-SCL final selector 教学图。 | 2026-08-04 已迁移为手绘 SVG `T10.6_NR_Polar_CA_SCL_final_selector.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；2026-06-20 已重生成，单脚本几何/可读性审计通过。 | 多路径 CRC/RNTI checker、selector 表和底部说明框已放大并居中；目检路径度量说明和说明框底部留白通过。 |
| `docs/L2_协议算法/assets/T10.7_NR_Polar_rate_recovery_flow.png` | 已删除（2026-08-04，SVG 迁移） | TS 38.212 Table 5.4.1.1-1；Polar rate recovery 教学图。 | 2026-08-04 已迁移为手绘 SVG `T10.7_NR_Polar_rate_recovery_flow.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；2026-06-20 已再次重生成，单脚本几何/可读性审计通过。 | 已放大流程节点、缓存卡片、LLR 初始化规则和下方对比表；目检底部说明框、表格间距和箭头端点贴边通过。 |
| `docs/L2_协议算法/assets/T10.8_NR_Polar_edge_case_diagnosis.png` | 已删除（2026-08-04，SVG 迁移） | NR Polar edge-case diagnosis 教学图。 | 2026-08-04 已迁移为手绘 SVG `T10.8_NR_Polar_edge_case_diagnosis.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；2026-06-20 已重生成，单脚本几何/可读性审计通过。 | 故障卡片、最小 dump 包和底部工程定位原则已放大并增高；目检局部间距、说明框留白和缩放可读性通过。 |
| `docs/L2_协议算法/assets/T11.1_Turbo_LDPC_Polar_algorithm_comparison.png` | 已删除（2026-08-04，SVG 迁移） | Turbo/LDPC/Polar algorithm comparison 教学图。 | 2026-08-04 已迁移为手绘 SVG `T11.1_Turbo_LDPC_Polar_algorithm_comparison.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；2026-06-20 已按可读性规则重生成，单脚本几何/可读性审计通过。 | 连线端点仍按真实边界；比较矩阵已抬升到 24px+/78px 行高，面板长说明改为居中多行，目检连线/表格/说明框通过。 |

## L3 Assets

| Asset | Script | Source/Evidence | Used By | Status | Visual Risk |
|:---|:---|:---|:---|:---|:---|
| `docs/L3_工程实现/assets/T17.1_golden_model_project_layout.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | Golden Model 工程流转图（正文 §总体工程流转图）。 | T17.1 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 主链 5 节点 + artifact fanout + 四输出 + scoreboard；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T17.2_LTE_Turbo_float_sim_flow.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | LTE Turbo 浮点仿真链路（正文 §浮点仿真总览图）。 | T17.2 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 发送链 4 节点 + AWGN + Decoder + 三路输出；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T17.3_NR_LDPC_float_sim_flow.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | NR LDPC 浮点仿真链路（正文 §浮点仿真总览图）。 | T17.3 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 发送链 5 节点 + Decoder Variants + 两路输出；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T17.4_NR_Polar_float_sim_flow.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | NR Polar 浮点仿真链路（正文 §浮点仿真总览图）。 | T17.4 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 发送链 5 节点 + Decoder Sweep + 两路输出；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T17.5_BER_BLER_curve_reporting.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | BER/BLER 曲线报告总览（正文 §曲线报告总览图）。 | T17.5 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | CSV 链 + 曲线面板 + 诊断链；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T18.1_fixed_point_decoder_requirements.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | 定点位宽需求总览（正文 §位宽需求总览图）。 | T18.1 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 主链 4 节点 + 五类需求块 + 检查位置条；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T18.2_LTE_Turbo_fixed_point_model.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | Turbo 定点数据通路（正文 §定点数据通路图）。 | T18.2 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 主链 5 + 五层比较点 + 选项条；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T18.3_NR_LDPC_fixed_point_model.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | LDPC 定点数据通路（正文 §定点数据通路图）。 | T18.3 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 主链 5 + 五层比较点 + 选项条；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T18.4_NR_Polar_fixed_point_model.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | Polar 定点数据通路（正文 §定点数据通路图）。 | T18.4 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 主链 6 + 六层比较点 + 状态条；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T18.5_SIMD_memory_layout_decoders.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | SIMD 与缓存布局（正文 §内存布局的性能机制）。 | T18.5 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | cache line 条 + SIMD lane 条 + 好/坏布局对比；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T18.6_bit_exact_regression_harness.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | Bit-Exact 回归流水线（正文 §回归流水线总图）。 | T18.6 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 四层实现 + Compare Core + 规则行 + CI/Failure；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T19.1_LTE_Turbo_RTL_microarchitecture.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | Turbo RTL 微架构（正文 §微架构总图）。 | T19.1 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 主链 5 + 存储对象带 + 迭代 FSM；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T19.2_NR_LDPC_RTL_microarchitecture.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | LDPC RTL 微架构（正文 §微架构总图）。 | T19.2 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 主链 6 + Banked Memory 主干 + Layered FSM；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T19.3_NR_Polar_RTL_microarchitecture.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | Polar RTL 微架构（正文 §微架构总图）。 | T19.3 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 主链 6 + 存储带 4 + 2L→L 瓶颈；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T19.4_unified_decoder_subsystem_architecture.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | 统一子系统微架构（正文 §微架构总图）。 | T19.4 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | Config 条 + Dispatcher + 三引擎/DMA + 软缓存；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T19.5_soft_buffer_HARQ_memory_architecture.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | 软缓存内存架构（正文 §架构总图）。 | T19.5 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | LTE/NR context + Manager + Journal/Saturation/SRAM；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T19.6_decoder_register_map_configuration_flow.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | 寄存器映射配置流（正文 §寄存器表总览图）。 | T19.6 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 四来源 + CTRL/STATUS + 配置状态机；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T20.1_decoder_testbench_architecture.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | Testbench 总体架构（正文 §Testbench 总体架构）。 | T20.1 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 六段链 + Assertions + Failure Bundle；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T20.2_protocol_vector_corner_case_suite.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | 协议向量套件架构（正文 §套件总体架构）。 | T20.2 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | Evidence/Manifest + 三条 Lane + Policy；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T20.3_coverage_regression_strategy.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | 覆盖率与回归策略（正文 §覆盖率与回归总图）。 | T20.3 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 五段链 + Coverage DB + Sign-off；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T20.4_DC_synthesis_flow_decoders.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | DC 综合流程（正文 §综合流程总图）。 | T20.4 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 五段链 + 工具边界 + 报告解读；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T20.5_timing_closure_critical_paths.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | 时序收敛（正文 §时序收敛总图）。 | T20.5 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 五段链 + 路径分类 + 多角视图；文字 12-15px，节点间距 ≥8px。 |
| `docs/L3_工程实现/assets/T20.6_final_decoder_evidence_report.svg` | 手绘 SVG（2026-08-07 按正文重绘，无生成脚本） | 最终证据报告（正文 §最终证据报告总图）。 | T20.6 | 2026-08-07 重绘：audit_svg_layout.py R1-R11 全过 + cairosvg 渲染验证。 | 五级证据链 + 摘要汇总；文字 12-15px，节点间距 ≥8px。 |
| `docs/L2_协议算法/assets/T11.2_LTE_NR_rate_matching_comparison.png` | 已删除（2026-08-04，SVG 迁移） | LTE/NR rate matching comparison 教学图；TS 36.212/38.212 表格子集。 | 2026-08-04 已迁移为手绘 SVG `T11.2_LTE_NR_rate_matching_comparison.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；已修复遮挡、字号和间距。 | 曾发生循环缓存遮挡、表格字号偏小、表格离上方框图过近。 |
| `docs/L2_协议算法/assets/T11.3_HARQ_soft_buffer_comparison.png` | 已删除（2026-08-04，SVG 迁移） | LTE/NR HARQ soft buffer comparison 教学图。 | 2026-08-04 已迁移为手绘 SVG `T11.3_HARQ_soft_buffer_comparison.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；已统一文本居中。 | 文本框和表格单元格居中、RV/CBG 语义。 |
| `docs/L2_协议算法/assets/T11.4_decoder_hardware_tradeoff_comparison.png` | 已删除（2026-08-04，SVG 迁移） | Decoder hardware tradeoff comparison 教学图。 | 2026-08-04 已迁移为手绘 SVG `T11.4_decoder_hardware_tradeoff_comparison.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过。 | 表格字号、箭头端点和工程决策矩阵局部间距。 |
| `docs/L2_协议算法/assets/T11.5_decoder_selection_by_channel_type.png` | 已删除（2026-08-04，SVG 迁移） | Decoder selector by channel type 教学图。 | 2026-08-04 已迁移为手绘 SVG `T11.5_decoder_selection_by_channel_type.svg`；几何审计与 cairosvg 渲染验证通过，语义与数据不变 | 边界检查通过；2026-06-20 已重生成并通过单脚本几何/可读性审计。 | 表格/节点/说明框文字水平和垂直居中。后续穿框复核发现旧 `RAT = NR -> UCI/DCI` 分支斜线穿 `NR data` 兄弟节点，已调换 NR control/data 分支上下位置，使控制分支和 Polar 输出同层、数据分支和 LDPC 输出同层，分支线不再穿框。 |

## 持续控制项

当前边界检查可以判定为通过，但“全项目 Python 图片字号与局部几何审计”不能一次性关闭。原因是历史上多次出现边界检查为 0 但局部几何不合格的情况，且 `合规与遵从.md` 已把逐图局部视觉审计写成持续性规则。后续任何图片脚本修改、图片重生成或正文插图新增，都必须重新执行逐图局部视觉审计并更新本清单。
