---
type: spec
aliases:
  - regression command plan
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/regression_command_plan.md"
---
# LTE/NR Decoding Regression Command Plan

审查时间：2026-06-21  
用途：记录当前文档、图片和后续真实工程回归命令。当前 L1/L2/L3 共 94 篇讲义已存在；真实 golden model、定点 C/C++、SystemVerilog RTL、coverage database、Design Compiler 综合和 STA 报告仍是后续工程阶段，不得把模板命令写成已运行证据。

## 文档审计命令

| 目的 | 命令 | 当前结果 |
|:---|:---|:---|
| 术语首现 | `python3 tools/audit_lesson_terms.py docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md` | `LESSON_TERM_AUDIT_OK` |
| 标题正式化 | `python3 tools/audit_markdown_headings.py docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md` | `MARKDOWN_HEADING_AUDIT_OK` |
| 深度与协议索引化风险 | `python3 tools/audit_lesson_depth.py --strict docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md` | `LESSON_DEPTH_AUDIT_OK` |
| 全量 LaTeX 渲染 | `python3 tools/audit_latex_render.py docs/L1/T*.md`；`python3 tools/audit_latex_render.py docs/L2/T*.md`；`python3 tools/audit_latex_render.py docs/L3/T*.md` | 分段全检通过：L1 `2036`、L2 `3444`、L3 `948`，合计 6428。 |
| 引用重建候选 | `python3 tools/audit_reference_rebuilds.py docs/L1/T*.md docs/L2/T*.md docs/L3/T*.md > docs/audits/reference_rebuild_candidates_full.txt` | 退出码 0，候选清单 1320 行；输出为候选清单，不是硬失败。 |
| 审计/台账标题 | `python3 tools/audit_markdown_headings.py docs/audits/*.md` | 本轮最终复跑输出 `MARKDOWN_HEADING_AUDIT_OK`。 |

## 图片回归命令

| 目的 | 命令 | 说明 |
|:---|:---|:---|
| 统计当前资产 | `find docs/L1/assets docs/L2/assets docs/L3/assets -name '*.png' | wc -l`；`find tools/figures -maxdepth 1 -name '*.py' | wc -l` | 当前为 68 张 PNG、58 个 Python 文件；其中 57 个 `render_*.py` 绘图脚本和 1 个 helper。 |
| 重生成全部 Python 图片 | `for f in tools/figures/*.py; do python3 "$f"; done` | 会覆盖 PNG 资产；执行前确认没有需要保留的人工图片修改。 |
| Python 图形静态几何风险审计 | `python3 tools/audit_figure_geometry.py tools/figures` | 检查固定坐标箭头、曲线/Bezier、未标注多段路径、穿框风险、端点和局部间距规则。 |
| Python 图形可读性审计 | `python3 tools/audit_figure_readability.py tools/figures` | 检查表格字号、行高、小字例外和说明区补偿。 |
| Python 图形静态文本适配审计 | `python3 tools/audit_figure_text_fit_static.py tools/figures` | 检查静默截断、按字符换行、长句直接绘制和缺少布局保护的 wrapped 文本。 |
| Python 图形动态文字覆盖审计 | `python3 tools/audit_figure_text_overlap_dynamic.py tools/figures` | 实际执行 `render_*.py`，记录 PIL 文本 bbox，阻断文字 bbox 互相覆盖。 |
| Python 图形动态文本框内边距审计 | `python3 tools/audit_figure_text_padding_dynamic.py tools/figures` | 实际执行 `render_*.py`，检查紧凑圆角 tag/chip 内文字到边框的最小留白；大容器默认不作为阻断噪声，必要时加 `--include-containers`。 |
| Python 图片底部内容边界审计 | `python3 tools/audit_image_TS_36.211_36211-j30_s06-s08_TS_36.213_36213-j30_cover_TS_38.300_38300-j20_TS_36.211_36211-j30_cover_TS_36.201_36201-j00_TS_36.322_36322-j00_TS_38.201_38201-j00_TS_36.213_36213-j30_s06-s07_TS_36.331_36331-j21_TS_38.202_38202-j00_TS_36.213_36213-j30_s14-xx_TS_38.306_38306-j20_TS_38.213_38213-j30_TS_36.213_36213-j30_sAnnexes_TS_38.214_38214-j30_TS_36.302_36302-j00_TS_36.306_36306-j20_TS_36.211_36211-j30_s09-sxx_TS_38.212_38212-j30_TS_38.321_38321-j20_TS_36.212_36212-j30_TS_38.322_38322-j20_TS_36.321_36321-j20_TS_38.211_38211-j30_TS_36.214_36214-j00_TS_38.331_38331-j20_TS_36.300_36300-j10_TS_36.213_36213-j30_s00-s05_TS_38.323_38323-j10_TS_36.213_36213-j30_s08-s09_TS_38.215_38215-j20_TS_36.213_36213-j30_s10-s13_TS_36.211_36211-j30_s00-s05_TS_36.323_36323-j00_content_bounds.py docs/L1/assets docs/L2/assets docs/L3/assets` | 检查已生成 PNG 的实际内容 bbox，阻断图片内容下边界离画布下边界过远。 |
| Python 图形真实输出审计 | `python3 tools/audit_python_figure_outputs.py tools/figures --timeout 60` | 逐个运行 `render_*.py`，确认脚本退出码、PNG 产物存在、PIL 可打开、尺寸合理、非空且内容不贴外边界；补足纯静态审计无法发现的“脚本成功但无有效输出”。 |
| Mermaid 语法与渲染审计 | `python3 tools/audit_mermaid_diagrams.py docs 2026-06-19-lte-nr-decoding-learning-roadmap.md`；快速静态版用 `--no-render` | 按本地 Mermaid skill 检查 ordered-list 节点文本、subgraph 命名、display-name 引用、样式声明，并用 `mmdc` + no-sandbox Puppeteer 配置实渲染。 |
| Python 图片正文等价审计 | `python3 tools/audit_python_figure_body_equivalents.py docs/L1 docs/L2 docs/L3` | 检查正文保留资产记录附近是否存在 Mermaid/Markdown 等价块，并阻断正文 `![...](...png)` 图片嵌入。 |
| Python 图片逐元素正文覆盖审计 | `python3 tools/audit_python_figure_element_coverage.py`；缺口摘要用 `python3 tools/audit_python_figure_element_coverage.py --summary` | 强制检查 Python 绘图脚本中的可见文字、节点标签、表格字段、流程说明和图例是否进入对应讲义正文。当前作为整改阻断项使用，只有全部讲义补齐后才能记录为全项目通过。 |
| 项目级图片一致性审计 | `python3 tools/audit_project_image_inventory.py` | 检查 `docs/L1/L2/L3/assets`、正文保留资产记录、`image_asset_inventory.md` 和 `python_figure_to_body_TS_36.211_36211-j30_s06-s08_TS_36.213_36213-j30_cover_TS_38.300_38300-j20_TS_36.211_36211-j30_cover_TS_36.201_36201-j00_TS_36.322_36322-j00_TS_38.201_38201-j00_TS_36.213_36213-j30_s06-s07_TS_36.331_36331-j21_TS_38.202_38202-j00_TS_36.213_36213-j30_s14-xx_TS_38.306_38306-j20_TS_38.213_38213-j30_TS_36.213_36213-j30_sAnnexes_TS_38.214_38214-j30_TS_36.302_36302-j00_TS_36.306_36306-j20_TS_36.211_36211-j30_s09-sxx_TS_38.212_38212-j30_TS_38.321_38321-j20_TS_36.212_36212-j30_TS_38.322_38322-j20_TS_36.321_36321-j20_TS_38.211_38211-j30_TS_36.214_36214-j00_TS_38.331_38331-j20_TS_36.300_36300-j10_TS_36.213_36213-j30_s00-s05_TS_38.323_38323-j10_TS_36.213_36213-j30_s08-s09_TS_38.215_38215-j20_TS_36.213_36213-j30_s10-s13_TS_36.211_36211-j30_s00-s05_TS_36.323_36323-j00_content_migration.md` 是否一致；不替代原尺寸逐图目检。 |
| 脚本语法检查 | `PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile tools/audit_figure_geometry.py tools/audit_figure_readability.py tools/audit_mermaid_diagrams.py tools/audit_python_figure_outputs.py tests/test_audit_figure_geometry.py tests/test_diagram_audit_tools.py tools/figures/*.py` | 确认审计器、测试和绘图脚本语法可用。 |
| 几何审计单元测试 | `python3 -m unittest tests/test_audit_figure_geometry.py` | 当前测试覆盖箭头头部向量、线身截断、法向量翼点、普通箭头两点直线和避让 helper。 |
| 新图形审计单元测试 | `python3 -m unittest tests/test_diagram_audit_tools.py` | 覆盖 Mermaid skill 规则、mmdc 入口前置静态检查、Python 脚本成功但无 PNG 输出、真实 PNG 产物验证。 |
| 局部视觉审计 | 人工逐图检查 `docs/audits/image_asset_inventory.md` 和 `docs/audits/python_figure_visual_geometry_checklist.md` | 重点检查字体上下边距、相邻边框间距、箭头形态、连线起止位置、表格居中、底部说明框和缩放后观感。 |

图片交付门槛采用多层证据：静态几何审计通过、可读性审计通过、静态文本适配审计通过、动态文字覆盖审计通过、动态文本框内边距审计通过、PNG 内容边界审计通过、Python 真实输出审计通过、Mermaid 静态/渲染审计通过、逐图局部视觉记录齐全。旧的静态几何/可读性审计不能单独证明图片和 Mermaid 图合格；只记录“无裁切、无遮挡、无箭头压字”不足以关闭图片审计项。

## L3 Golden Model 回归草案

| 方向 | 建议命令形态 | 最小输入 | 最小输出 |
|:---|:---|:---|:---|
| LTE Turbo 浮点模型 | `python3 -m lte_nr_decoding.lte_turbo.run_vector --config vectors/lte_turbo/*.yaml` | TB bits、CRC、CB segmentation、interleaver、rate matching、RV、LLR。 | CB/TB CRC、decoded bits、iteration count、soft buffer dump。 |
| NR LDPC 浮点模型 | `python3 -m lte_nr_decoding.nr_ldpc.run_vector --config vectors/nr_ldpc/*.yaml` | BG、`Zc`、lifting table、rate recovery、RV/`k0`、CBG mask、LLR。 | syndrome、CB/TB CRC、CBG state、iteration count、soft buffer dump。 |
| NR Polar 浮点模型 | `python3 -m lte_nr_decoding.nr_polar.run_vector --config vectors/nr_polar/*.yaml` | UCI/DCI payload、CRC/RNTI、reliability sequence、frozen mask、rate recovery、list size、LLR。 | selected path、CRC/RNTI pass、payload、PM diagnostics。 |
| 定点 bit-exact | `python3 -m lte_nr_decoding.fixed.run_bitexact --suite vectors/fixed/*.yaml` | 浮点参考、定点配置、饱和和舍入策略。 | bit-exact diff、clip/saturation counters、first mismatch。 |
| RTL 对比 | `make sim VECTOR=<name>` 或 `pytest tests/rtl_bitexact` | C/Python reference vector、RTL dump、descriptor。 | scoreboard pass/fail、waveform anchor、error code。 |

这些命令是后续工程入口模板。当前仓库没有对应可执行包、真实向量目录或 RTL simulator 配置时，不能写成已运行。

## 可执行 Python 片段汇总策略

当前讲义内存在教学 Python 片段和固定输出行。统一回归前，应把片段整理为三类：

| 类型 | 示例 | 处理方式 |
|:---|:---|:---|
| 教学 toy 片段 | GF(2)、CRC-4、LLR、toy LDPC/Polar。 | 保留在讲义中，后续抽取为 `tests/tutorial_vectors`。 |
| 协议表驱动检查 | Turbo interleaver、LDPC lifting、Polar reliability sequence。 | 进入 `tests/protocol_tables`，要求输入 CSV/HTML SHA-256 可追踪。 |
| 边界负测试 | LLR 符号反转、RV mismatch、filler/unknown 混淆、CRC/RNTI 错。 | 进入 `tests/negative_cases`，要求最小 dump 包可复现。 |

## 最终签核回归草案

| 证据类别 | 后续真实命令或产物 | 签核前必须存在 |
|:---|:---|:---|
| 浮点 BLER | `decoder_golden.bler --suite ...` 或等价脚本 | 曲线 CSV、随机种子、confidence interval、失败样本索引。 |
| 定点损失 | `decoder_fixed.compare --float-ref ...` | 定点配置、loss table、clip/saturation 统计。 |
| RTL regression | simulator regression 命令 | scoreboard summary、waveform anchor、failure bundle。 |
| Coverage | simulator coverage merge/report | functional/code/assertion coverage DB 和 waiver。 |
| DC synthesis | `dc_shell -f scripts/syn/decoder_top.tcl` | mapped netlist、timing/area/power reports、约束文件。 |
| Timing closure | STA 或 DC timing report | worst paths、slack、修复记录、post-fix regression 证据。 |

真实签核状态只由上述证据闭环决定。当前文档交付完成不等于真实工程 sign-off 完成。
