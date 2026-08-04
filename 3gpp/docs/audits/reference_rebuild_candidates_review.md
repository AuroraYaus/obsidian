---
type: spec
aliases:
  - reference rebuild candidates review
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/reference_rebuild_candidates_review.md"
---
# Reference Rebuild Candidate Review

审查时间：2026-06-20  
输入文件：`docs/audits/reference_rebuild_candidates_full.txt`  
生成命令：

```bash
python3 tools/audit_reference_rebuilds.py docs/L1/T*.md docs/L2_协议算法/T*.md > docs/audits/reference_rebuild_candidates_full.txt
```

结果说明：`audit_reference_rebuilds.py` 输出的是候选清单，不是失败清单。脚本会把正文中的公式、表格、协议图、论文引用和 `待核验` 边界都列出，后续必须人工分类。

## 统计摘要

| 类别 | 数量 | 解释 |
|:---|---:|:---|
| `formula_ref` | 504 | 包括教学公式、协议公式、公式边界说明和自测题中的公式。 |
| `table_or_figure` | 335 | 包括协议表/图、教学表、Mermaid 图、Python 图片资产和表格证据行。 |
| `paper_citation` | 75 | 包括背景论文、教材和经典算法引用。 |
| `unverified` | 105 | 明确含有 `待核验`、未核验、抽取不完整或边界声明的条目。 |
| 合计候选条目 | 1019 | `reference_rebuild_candidates_full.txt` 共 1020 行，其中第一行为脚本标题 `REFERENCE_REBUILD_AUDIT_CANDIDATES`，实际候选条目 1019 条。 |

候选最多的文件：

| 文件 | 候选行数 | 当前判断 |
|:---|---:|:---|
| `docs/L1/T1.2_GF2_polynomials_crc_remainders.md` | 53 | 多数为教学 CRC 公式和协议边界说明；T3.1 已承接 LTE CRC 多项式复现。 |
| `docs/L1/T3.3_LTE_Turbo_segmentation_rules.md` | 45 | 多数为 TS 36.212 Table 5.1.3-3 已复现图和分段公式；剩余为 Turbo 编码器图/尾比特边界。 |
| `docs/L1/T1.1_GF2_binary_arithmetic_for_decoders.md` | 42 | 多数为 GF(2) 教学公式，不是协议图表缺失。 |
| `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md` | 40 | TS 38.212 Table 5.3.2-1/2/3 已图片化复现；候选多来自表格证据和 QC 构造公式。 |
| `docs/L1/T3.4_NR_LDPC_segmentation_rules.md` | 38 | TS 38.212 Table 5.3.2-1/2/3 已图片化复现；分段公式受原始抽取限制，正文已说明人工重构和边界。 |
| `docs/L1/T3.1_LTE_NR_CRC_families.md` | 37 | LTE/NR CRC 多项式已复现；候选多来自多项式公式和协议证据表。 |
| `docs/L2_协议算法/T6.4_LTE_Turbo_internal_interleaver.md` | 34 | Table 5.1.3-3 输入 CSV/HTML、生成脚本、输出资产和使用位置已由正文、`image_asset_inventory.md`、`final_delivery_status.md` 共同闭合。 |
| `docs/L2_协议算法/T8.4_LDPC_Tanner_graph_message_passing.md` | 33 | 多数为 Tanner 图、syndrome 和 LDPC 教学/协议边界候选；正文已说明协议表图承接关系。 |
| `docs/L2_协议算法/T8.5_LDPC_sum_product_BP.md` | 25 | 多数为 BP/SPA 推导公式和 toy 计算公式；不等同为外部协议公式缺失。 |
| `docs/L2_协议算法/T11.5_decoder_selection_by_channel_type.md` | 23 | 多数为协议映射表和 selector 证据行；正文已作为信道/信息类型到译码器家族映射总结。 |

## 分类结论

### A. 已复现或已由专题章节承接

这些候选不作为当前缺陷，但后续维护时仍要保留证据链。

| 主题 | 已有闭环 | 证据 |
|:---|:---|:---|
| LTE CRC 多项式 | 已在 T3.1 复现 LTE CRC24A、CRC24B、CRC16、CRC8。 | `docs/L1/T3.1_LTE_NR_CRC_families.md`。 |
| LTE Turbo 分段合法块长表 | 已在 T3.3 用 Python 图片化复现 TS 36.212 Table 5.1.3-3。 | `docs/L1/assets/T3.3_TS36.212_Table_5.1.3-3.png`；`tools/figures/render_lte_turbo_interleaver_table.py`。 |
| NR LDPC lifting set 与基图移位表 | 已在 T3.4 用 Python 图片化复现 TS 38.212 Table 5.3.2-1/2/3。 | `docs/L1/assets/T3.4_TS38.212_Table_5.3.2-*.png`；`tools/figures/render_nr_ldpc_tables.py`。 |
| LTE sub-block interleaver 32 列置换 | T7.2 正文复现 Table 5.1.4-1 序列，并记录 `table_0010.csv/html`。 | `docs/L2_协议算法/T7.2_LTE_subblock_deinterleaver_circular_buffer.md`。 |
| LTE HARQ soft buffer `Ncb/NIR/E/k0` 主线 | T7.3 已重建 DL-SCH/PCH 主线公式并记录 Word media 证据。 | `docs/L2_协议算法/T7.3_LTE_HARQ_soft_buffer_RV.md`。 |
| TS 36.213/36.321 LTE HARQ/MAC 边界锚点 | 已在 T7.3/T7.5/T7.6 补入 TS 36.213 §8.3、§8.6、§8.6.1 和 TS 36.321 §4.3.2、§4.4、§5.3.2.1、§5.3.2.2、§5.4.2.1 的本地路径与行号证据。 | `docs/L2_协议算法/T7.3_LTE_HARQ_soft_buffer_RV.md`；`docs/L2_协议算法/T7.5_LTE_DL_UL_decoding_differences.md`；`docs/L2_协议算法/T7.6_LTE_Turbo_decoder_edge_cases.md`。 |
| TS 36.212 Figure 5.1.3-2 Turbo 编码器结构图 | 已用 Python 图片化重建，解释两个 8 状态组成编码器、内部交织器、三路母码流和 trellis termination 虚线路径；T6 系列引用已指向该资产。 | `tools/figures/render_lte_turbo_encoder_structure.py`；`docs/L2_协议算法/assets/T6.3_TS36.212_Figure_5.1.3-2_turbo_encoder_rebuild.png`；`docs/L2_协议算法/T6.3_LTE_Turbo_encoder_trellis_termination.md`。 |
| TS 38.212 NR CRC 多项式 | 已在 T3.1 复现 CRC24A、CRC24B、CRC24C、CRC16、CRC11、CRC6，并记录 TS 38.212 `source.docx` 中 Equation.3 OLE/media 证据链。 | `docs/L1/T3.1_LTE_NR_CRC_families.md`；`3GPP_Rel19/processed/TS_38.212_38212-j30/media/image7.wmf`、`image9.wmf`、`image10.wmf`、`image11.wmf`、`image13.wmf`、`image15.wmf`。 |

### B. 合理边界，不应强行补成协议结论

这些候选属于基础课或教学模型，正文已经说明不把教学公式写成 3GPP 规范。

| 范围 | 代表文件 | 处理原则 |
|:---|:---|:---|
| GF(2)、概率、LLR、信息论教学公式 | T1.1、T1.4、T1.5、T1.6 | 保留为教学推导；不需要协议表/图复现。 |
| BPSK/QPSK/QAM 教学映射 | T2.1-T2.3 | 当前用于软解调理论；真实协议调制表在调制专题或后续链路仿真中核验。 |
| toy Turbo-like / toy LDPC 数值例子 | T6.8 等 | 必须醒目标注非 conformance vector；不应伪装成协议测试向量。 |
| 论文/教材背景引用 | 多篇基础课和算法课 | 若未引用具体公式、表格、图，只作为背景阅读，正文说明即可。 |

### C. 需要后续关闭的协议证据项

这些不是立即阻塞模块 8-11 写作，但进入 bit-exact 模型或最终交付前必须关闭。

| 优先级 | 主题 | 当前状态 | 关闭动作 |
|:---|:---|:---|:---|
| Important | TS 38.214 MCS/TBS 具体表值 | L2 T9/T11 仅使用调度字段来源与 RV/CBG/CBGTI/CBGFI 语义，不使用 MCS/TBS 表具体数值。 | L3 或系统级向量阶段如实际查表，应按使用范围复现表格子集。 |
| Minor | TS 36.211/38.211 调制星座表 | T2 基础课只用教学映射。 | 真实链路仿真或 demapper 专题中复现 BPSK/QPSK/QAM 表格和 bit labeling。 |
| Closed | T6.4 Table 5.1.3-3 资产证据链 | T3.3 已复现长表，T6.4 使用地址公式。 | `docs/L2_协议算法/T6.4_LTE_Turbo_internal_interleaver.md` 已列 `table_0009.csv/html` 和输出图；`docs/audits/image_asset_inventory.md` 已列脚本 `render_lte_turbo_interleaver_table.py`、输入证据、输出图片和 T3.3/T6.4 使用位置。 |

## 后续动作

1. 阶段 4 当前仅保留 TS 38.214 MCS/TBS 具体表值为 L3/system bit-exact 条件项，不处理 B 类教学公式。
2. 模块 8 写作时，若引用 TS 38.212 Table 5.3.2-1/2/3，可复用 T3.4 的图片资产，但必须重新解释本节用到的列、行、`Zc`、set index 和 shift value。
3. 模块 9/11 已关闭 L2 所需 RV/CBG/CBGTI/CBGFI 语义；若后续 L3 使用 MCS/TBS 表具体数值，必须按本节实际使用范围复现协议表或明确关闭条件。
4. 阶段 10 最终交付已生成 `docs/audits/final_delivery_status.md`，其中“未关闭待核验清单”承接本报告 C 类和 `reference_rebuild_candidates_full.txt` 的 `unverified` 行。
