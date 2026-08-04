---
type: spec
aliases:
  - L2 overall review
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/L2_overall_review.md"
---
# L2 Overall Review

## 审查范围

本报告覆盖 `docs/L2_协议算法/T6.*.md` 到 `docs/L2_协议算法/T11.*.md`，共 41 篇讲义：

| 模块 | 范围 | 篇数 | 状态 |
|:---|:---|---:|:---|
| T6 | LTE Turbo 译码核心 | 8 | 已完成并纳入全量审计。 |
| T7 | LTE Turbo 速率恢复、HARQ、重组和边界案例 | 6 | 已完成并纳入全量审计。 |
| T8 | NR LDPC 译码核心 | 8 | 已完成并纳入全量审计。 |
| T9 | NR LDPC 速率恢复、HARQ、重组和边界案例 | 6 | 已完成并纳入全量审计。 |
| T10 | NR Polar 控制信息译码 | 8 | 已完成并纳入全量审计。 |
| T11 | LTE/NR 译码对比 | 5 | 已完成并纳入全量审计。 |

## 自动审计结果

| 审计项 | 命令 | 结果 |
|:---|:---|:---|
| 缩写首现与术语 | `python3 tools/audit_lesson_terms.py docs/L2_协议算法/T*.md` | `LESSON_TERM_AUDIT_OK` |
| 标题正式化 | `python3 tools/audit_markdown_headings.py docs/L2_协议算法/T*.md` | `MARKDOWN_HEADING_AUDIT_OK` |
| 深度与零基础讲解 | `python3 tools/audit_lesson_depth.py --strict docs/L2_协议算法/T*.md` | `LESSON_DEPTH_AUDIT_OK` |
| LaTeX 渲染 | `python3 tools/audit_latex_render.py docs/L2_协议算法/T*.md` | `LATEX_RENDER_AUDIT_OK formulas=3241` |
| 引用重建候选 | `python3 tools/audit_reference_rebuilds.py docs/L2_协议算法/T*.md` | `REFERENCE_REBUILD_AUDIT_CANDIDATES`，候选清单 544 行，已保存到 `docs/audits/reference_rebuild_candidates_L2.txt`。 |

说明：引用重建脚本输出候选项，不等同于自动失败。L2 中大量候选来自“已在正文复现的协议表/图/公式”“明确交由专题章节复现”“仅作为背景锚点”“正文已标注不展开或待核验关闭条件”。后续若做最终交付，应按候选清单继续分类，不把候选项直接视为协议错误。

## 图片审查

| 检查项 | 结果 |
|:---|:---|
| 图片脚本重生成 | `tools/figures/*.py` 共 32 个脚本全部运行成功。 |
| PNG 边界检查 | 仅确认 `docs/L1_基础/assets/*.png` 与 `docs/L2_协议算法/assets/*.png` 共 36 张 PNG 的 top/bottom/left/right 非白边界计数均为 0；该项不等于局部视觉审计通过。 |
| T11 新增图片 | T11.1-T11.5 五张图均重生成成功，边界检查通过；用户指出过的局部几何问题已修复并记录。 |
| 全局视觉规则 | 规则已写入总纲、roadmap 和台账；这是后续逐图审计依据，不是 36 张图永久通过证明。 |
| T6.3 底部说明框复修 | 用户指出 `T6.3_TS36.212_Figure_5.1.3-2_turbo_encoder_rebuild.png` 底部“接收端读图顺序”说明框纵向布局不协调。已修复脚本为 bbox-based 分区居中布局，重新生成图片，边界检查 `IMAGE_EDGE_CHECK (1800, 1280) {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}`。 |

图片边界检查不能替代人工视觉审查。此前 L2 图片审查对 T6.3 的记录需要收窄解释：脚本重生成和 PNG 边界检查通过，但底部说明框的局部视觉几何没有被充分检查，已按“局部视觉审计漏检”记录并修复。后续每张 Python 生成图必须逐图检查底部说明框、脚注、图例、caption、表格块、“读图顺序”“要点”“风险”“工程检测点”等局部面板，不能用边界检查或粗略目检替代。当前已重点目检过用户指出过的问题图，包括 T6.3、T10.2、T10.7、T11.1、T11.2、T11.3、T11.4 和 T11.5。阶段 10 已生成 `docs/audits/image_asset_inventory.md` 资产清单；该清单记录脚本、输出路径和历史风险，但后续图片修改仍必须重新逐图局部视觉审计。

## 逐篇状态表

| 文件 | Prompt 覆盖 | 拓展充分性 | 协议证据 | 图片/表格 | LaTeX | 自动审计 | 遗留问题 |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `T6.1_LTE_Turbo_decoder_chain_overview.md` | 覆盖 | 已扩展接收链路、descriptor 和验证 | TS 36.212 Turbo 链路 | 无图片 | 通过 | 通过 | 协议图复现由 T6.3/T11.1 承接。 |
| `T6.2_RSC_code_foundation.md` | 覆盖 | 已扩展 RSC 理论、状态和 trellis | TS 36.212 Turbo 背景 | 无图片 | 通过 | 通过 | LTE Figure 5.1.3-2 由 T6.3 复现。 |
| `T6.3_LTE_Turbo_encoder_trellis_termination.md` | 覆盖 | 已扩展编码器、尾比特、接收端后果 | TS 36.212 §5.1.3.2 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T6.4_LTE_Turbo_internal_interleaver.md` | 覆盖 | 已扩展 QPP、地址、硬件 ROM | TS 36.212 Table 5.1.3-3 | 有表图 | 通过 | 通过 | Table 5.1.3-3 资产证据链已在 `image_asset_inventory.md` 补齐输入 CSV/HTML、脚本、输出路径和使用位置。 |
| `T6.5_BCJR_MAP_decoding_intuition.md` | 覆盖 | 已扩展 BCJR 概率、直觉和例子 | Turbo 实现边界 | 无图片 | 通过 | 通过 | 无 Critical/Important。 |
| `T6.6_Log_MAP_Max_Log_MAP_Turbo.md` | 覆盖 | 已扩展 Log-MAP、Max-Log-MAP、定点 | Turbo 实现边界 | 无图片 | 通过 | 通过 | 无 Critical/Important。 |
| `T6.7_Turbo_iteration_extrinsic_stopping.md` | 覆盖 | 已扩展外信息、早停、迭代控制 | TS 36.212/Turbo CRC 边界 | 无图片 | 通过 | 通过 | 无 Critical/Important。 |
| `T6.8_LTE_Turbo_decoder_numeric_walkthrough.md` | 覆盖 | 已扩展数值走读和验证 | LTE Turbo 接收链路 | 无图片 | 通过 | 通过 | 无 Critical/Important。 |
| `T7.1_LTE_Turbo_de_rate_matching_overview.md` | 覆盖 | 已扩展 rate recovery 总览和 toy 例子 | TS 36.212 §5.1.4.1 | 无图片 | 通过 | 通过 | 子块细节由 T7.2 承接。 |
| `T7.2_LTE_subblock_deinterleaver_circular_buffer.md` | 覆盖 | 已扩展 Table 5.1.4-1 和 `<NULL>` | TS 36.212 Table 5.1.4-1 | 表格 | 通过 | 通过 | 无 Critical/Important。 |
| `T7.3_LTE_HARQ_soft_buffer_RV.md` | 覆盖 | 已扩展 RV ring buffer、LLR 合并和饱和 | TS 36.212/36.213/36.321 | 有图 | 通过 | 通过 | TS 36.213 调度细节只保留译码相关字段。 |
| `T7.4_LTE_code_block_reassembly_TB_CRC.md` | 覆盖 | 已扩展 CB/TB CRC 和重组 | TS 36.212 | 无图片 | 通过 | 通过 | 无 Critical/Important。 |
| `T7.5_LTE_DL_UL_decoding_differences.md` | 覆盖 | 已扩展 DL/UL 接收端差异 | TS 36.212/36.213/36.321 | 有图 | 通过 | 通过 | 用户指出旧图问题已修复并写入全局规则。 |
| `T7.6_LTE_Turbo_decoder_edge_cases.md` | 覆盖 | 已扩展小块、filler、RV、软缓存诊断 | TS 36.212 | 无图片 | 通过 | 通过 | 无 Critical/Important。 |
| `T8.1_NR_LDPC_decoder_chain_overview.md` | 覆盖 | 已扩展 NR LDPC 接收链路和 CBG | TS 38.212/38.214 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T8.2_NR_LDPC_base_graph_selection.md` | 覆盖 | 已扩展 BG 选择公式和证据文件 | TS 38.212 §6.2.2/§7.2.2 | 有图 | 通过 | 通过 | 公式证据文件已单列。 |
| `T8.3_NR_LDPC_lifting_QC_matrix.md` | 覆盖 | 已扩展 lifting、QC 矩阵和完整 BG 表 | TS 38.212 Table 5.3.2-1/2/3 | 三张图 | 通过 | 通过 | 无 Critical/Important。 |
| `T8.4_LDPC_Tanner_graph_message_passing.md` | 覆盖 | 已扩展 Tanner、syndrome、边消息 | TS 38.212 rate matching 边界 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T8.5_LDPC_sum_product_BP.md` | 覆盖 | 已扩展 BP/SPA 理论、公式和 toy | LDPC 接收实现边界 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T8.6_LDPC_MS_NMS_OMS.md` | 覆盖 | 已扩展 Min-Sum/NMS/OMS 和硬件取舍 | LDPC 实现边界 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T8.7_layered_LDPC_decoding_schedule.md` | 覆盖 | 已扩展 layered schedule、bank conflict | TS 38.212 BG/QC 背景 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T8.8_NR_LDPC_decoder_numeric_walkthrough.md` | 覆盖 | 已扩展完整数值走读 | LDPC toy + TS 边界 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T9.1_NR_LDPC_rate_recovery_overview.md` | 覆盖 | 已扩展 circular buffer、RV、soft combine | TS 38.212 §5.4.2 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T9.2_NR_LDPC_circular_buffer_states.md` | 覆盖 | 已扩展 unknown/shortened/repeated 状态 | TS 38.212 §5.4.2 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T9.3_NR_LDPC_HARQ_soft_buffer_RV_k0.md` | 覆盖 | 已扩展 RV、k0、CBG、soft buffer | TS 38.212/38.214 | 有图 | 通过 | 通过 | k0 表抽取限制已通过人工证据说明。 |
| `T9.4_NR_LDPC_bit_deinterleaving.md` | 覆盖 | 已扩展 bit deinterleaving 公式证据 | TS 38.212 §5.4.2.2 | 有图 | 通过 | 通过 | 公式证据文件已单列。 |
| `T9.5_NR_LDPC_reassembly_TB_CRC.md` | 覆盖 | 已扩展 CB/TB CRC、CBG partial retransmission | TS 38.212/38.214 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T9.6_NR_LDPC_decoder_edge_cases.md` | 覆盖 | 已扩展 BG/Zc/RV/CBG/CRC 诊断 | TS 38.212/38.214 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T10.1_NR_Polar_decoder_chain_overview.md` | 覆盖 | 已扩展 Polar 链路总览和 UCI/DCI 背景 | TS 38.212 Table 5.3-2 | 有图 | 通过 | 通过 | 公式细节由 T10.2-T10.7 承接。 |
| `T10.2_channel_polarization_frozen_bits.md` | 覆盖 | 已扩展极化、frozen/info、N=4 | TS 38.212 Polar 背景 | 有图 | 通过 | 通过 | 用户指出的圆框/文字/连线问题已修复。 |
| `T10.3_NR_Polar_reliability_sequence.md` | 覆盖 | 已完整复现可靠性序列 | TS 38.212 Table 5.3.1.2-1 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T10.4_Polar_SC_decoding.md` | 覆盖 | 已扩展 SC、f/g、partial sum | Polar 实现边界 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T10.5_Polar_SCL_decoding.md` | 覆盖 | 已扩展路径分裂、PM、sorter | Polar 实现边界 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T10.6_CRC_aided_SCL_control_reliability.md` | 覆盖 | 已扩展 CA-SCL、CRC/RNTI final selector | TS 38.212 UCI/DCI | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T10.7_NR_Polar_rate_recovery.md` | 覆盖 | 已扩展 Polar rate recovery 和 pattern | TS 38.212 Table 5.4.1.1-1 | 有图 | 通过 | 通过 | 用户指出底部留白问题已修复。 |
| `T10.8_NR_Polar_decoder_edge_cases.md` | 覆盖 | 已扩展无 CRC、小负载、mask、PM、RNTI | TS 38.212 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T11.1_Turbo_LDPC_Polar_algorithm_comparison.md` | 覆盖 | 已扩展算法、图模型、协议代际 | TS 36.212/38.212 表 | 有图 | 通过 | 通过 | 用户指出连线端点问题已修复。 |
| `T11.2_LTE_NR_rate_matching_comparison.md` | 覆盖 | 已扩展三类 rate recovery 对比 | TS 36.212/38.212 表 | 有图 | 通过 | 通过 | 用户指出表格字号/间距已修复。 |
| `T11.3_HARQ_soft_buffer_comparison.md` | 覆盖 | 已扩展 HARQ soft buffer、RV、CBG | TS 36.212/36.213/36.321/38.212/38.214/38.321 | 有图 | 通过 | 通过 | 图片文字居中规则已落实。 |
| `T11.4_decoder_hardware_tradeoff_comparison.md` | 覆盖 | 已扩展硬件架构、周期估算、矩阵 | TS 36.212/38.212 使用证据 | 有图 | 通过 | 通过 | 无 Critical/Important。 |
| `T11.5_decoder_selection_by_channel_type.md` | 覆盖 | 已扩展 selector、descriptor、边界案例 | TS 36.212/38.212 表 | 有图 | 通过 | 通过 | 无 Critical/Important。 |

## 逐主题一致性结论

| 主题 | 结论 | 证据位置 |
|:---|:---|:---|
| LLR 定义 | L2 统一把 LLR 作为软信息，按不同 core 区分 channel/extrinsic/message/path metric；未知 LLR、重复累加和饱和在 T7/T9/T10/T11 中保持一致。 | T6.6、T7.3、T9.1、T10.7、T11.2。 |
| CRC 定义 | TB CRC、CB CRC、UCI/DCI CRC、Polar CA-SCL 选择、syndrome 与 CRC 边界已区分。 | T7.4、T8.4、T9.5、T10.6、T11.5。 |
| filler/`<NULL>`/puncturing/shortening/repetition | LTE Turbo、NR LDPC、NR Polar 三类空洞语义已分别讲解，T11.2 明确不可混用。 | T7.2、T9.2、T10.7、T11.2。 |
| RV 和 soft buffer | LTE RV 与 NR RV 都以循环缓存窗口/起点理解，但 NR 增加 BG/Zc/CBG/limited-buffer 语义。 | T7.3、T9.3、T11.3。 |
| Turbo/LDPC/Polar 协议证据 | 三类译码器均有 TS 36.212/38.212 本地路径、表格和接收端流程证据。 | T6/T8/T10/T11.1/T11.5。 |
| descriptor 字段 | `tb_id`、`cb_id`、`cbg_id`、`harq_id`、`rvidx`、`E`、`Ncb`、`K`、`Zc`、`BG` 等字段在 T9/T11 中统一使用。 | T9.3、T11.3、T11.5。 |
| Python 片段 | 多数数值讲义提供 Python toy 输出；全量图片脚本可重生成。 | 各讲义执行记录；本报告图片审查。 |
| 工业用例数量 | 未发现超出每节最多 2 个工业用例的明显问题。 | 全量深度审计和人工阅读。 |

## 问题清单

| 严重度 | 问题 | 影响 | 处理建议 |
|:---|:---|:---|:---|
| Critical | 无。 | 无阻塞交付问题。 | 无。 |
| Important | TS 38.214 MCS/TBS 具体表值仍是 L3/system bit-exact 条件项。 | L2 T9/T11 只使用调度字段来源、RV/CBG/CBGTI/CBGFI 语义，不从 MCS/TBS 表中读取具体规范数值。 | L3 或系统级向量阶段若实际查表，按使用范围重建相关表格子集。 |
| Resolved | T6.3 底部说明框局部视觉审计漏检。 | 像素边界检查为 0 仍可能存在说明框内部文字偏位、底部留白不足或标题/正文布局失衡。 | 已修复 T6.3 图片脚本并重新生成；后续图片审计必须逐图检查底部说明框、脚注、图例、caption、表格块和“读图顺序/要点/风险/工程检测点”等面板。 |
| Resolved | T6.4 Table 5.1.3-3 资产证据链总表缺项。 | 不影响正文学习，但影响资产审计闭环。 | `image_asset_inventory.md` 已列 `table_0009.csv/html`、`render_lte_turbo_interleaver_table.py`、输出图片和 T3.3/T6.4 使用位置。 |
| Resolved | T9/T10/T11 模块级审核经理状态未闭合。 | 自动审计通过不等于独立复核完成。 | 阶段 9 L2 总体审核经理复核覆盖 T6-T11 共 41 篇，当前 Critical=0；T9/T10/T11 用户指出的图形问题已修复并纳入规则。 |
| Minor | 早期 T6/T7/T8 部分章节的 Prompt 覆盖表标题不完全统一。 | 内容存在，不影响审计；形式一致性略弱。 | 可在最终风格统一时批量改标题，不作为当前阻塞。 |

## 修复优先级

1. 先修协议错误或证据错误。目前未发现 L2 Critical 协议错误。
2. 再修 Prompt 漏项。目前 L2 Prompt 覆盖矩阵已覆盖已完成讲义，未发现 T6-T11 重要漏项。
3. 再修 LaTeX/图片问题。目前 LaTeX 全量通过，PNG 边界全量通过；PNG 边界全量通过不代表 36 张图逐图局部视觉审计永久通过。用户指出过的图片问题已修复并纳入全局规则，后续修改图片时继续逐图复检。
4. 最后修风格和资产总表。阶段 10 已生成图片资产清单、最终状态总表和回归命令草案；引用重建候选已按交付级类别归档，保留 L3 条件项。

## 结论

L2 T6-T11 共 41 篇讲义已完成当前轮总体审查。自动审计硬门槛全部通过：术语、标题、深度和 LaTeX 均为 OK。图片脚本全部可重生成，L1/L2 PNG 边界检查通过；图片局部视觉审计作为全项目持续控制保留，不计入 L2 内容级 Important。当前无 Critical 问题；已关闭 T6.4 资产证据链和 T9/T10/T11 复核状态问题。剩余 L2 内容级 Important 仅为 L3/system bit-exact 阶段需要按实际使用复现 TS 38.214 MCS/TBS 表具体数值。
