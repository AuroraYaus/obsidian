---
type: spec
aliases:
  - python figure to body TS_36.211_36211-j30_s06-s08_content migration
tags:
  - 3gpp
  - docs
  - audit
source_spec: "docs/audits/python_figure_to_body_TS_36.211_36211-j30_s06-s08_TS_36.213_36213-j30_cover_TS_38.300_38300-j20_TS_36.211_36211-j30_cover_TS_36.201_36201-j00_TS_36.322_36322-j00_TS_38.201_38201-j00_TS_36.213_36213-j30_s06-s07_TS_36.331_36331-j21_TS_38.202_38202-j00_TS_36.213_36213-j30_s14-xx_TS_38.306_38306-j20_TS_38.213_38213-j30_TS_36.213_36213-j30_sAnnexes_TS_38.214_38214-j30_TS_36.302_36302-j00_TS_36.306_36306-j20_TS_36.211_36211-j30_s09-sxx_TS_38.212_38212-j30_TS_38.321_38321-j20_TS_36.212_36212-j30_TS_38.322_38322-j20_TS_36.321_36321-j20_TS_38.211_38211-j30_TS_36.214_36214-j00_TS_38.331_38331-j20_TS_36.300_36300-j10_TS_36.213_36213-j30_s00-s05_TS_38.323_38323-j10_TS_36.213_36213-j30_s08-s09_TS_38.215_38215-j20_TS_36.213_36213-j30_s10-s13_TS_36.211_36211-j30_s00-s05_TS_36.323_36323-j00_content_migration.md"
---
# Python Figure to Body Content Migration

审查时间：2026-06-23

总计：69 个 Python 绘图资产记录；`body_text_represented_asset_retained=66`，`evidence_only_compatibility_retained=3`，`missing=0`。

## 2026-08-04 SVG 迁移更新

本台账 8 月前记录的是 PNG 时代状态。2026-08-04 全量 SVG 迁移后，57 张教学 PNG 已删除并由同名手绘 SVG 替代（详见 `image_asset_inventory.md` 2026-08-04 迁移记录），12 张协议证据表 PNG 保留。下表已按当前磁盘状态同步：已删除的 PNG 行移除，保留 12 张证据表资产行；SVG 资产由 `image_asset_inventory.md` 登记。
；`body_text_represented_asset_retained=66`，`evidence_only_compatibility_retained=3`，`missing=0`。

状态规则：`body_text_represented; asset_retained` 表示课程正文不再嵌入或链接 PNG，图中流程、节点、表格、字段和边界已经用 Mermaid、Markdown 表格和普通正文承接；PNG 文件只作为审计资产保留。`evidence_only; compatibility_retained; not_current_body_reference` 表示兼容或完整拼接图仅保留在资产目录和审计台账中，不作为当前正文入口。资产路径、脚本路径和生成证据只写在本台账与图片资产清单中，不写入课程主体。

| Lesson | Image | Script | Equivalent type | Status | Body location |
|:---|:---|:---|:---|:---|:---|
| `docs/L1_基础/T3.2_transport_code_block_filler_bits.md` | `assets/T3.2_TS36.212_Table_5.1.3-3_original_crop.png` | `pdftoppm`（source.pdf 裁剪） | PDF crop | evidence_only; compatibility_retained; not_current_body_reference | `docs/L1_基础/T3.2_transport_code_block_filler_bits.md:159` |

| `docs/L1_基础/T3.3_LTE_Turbo_segmentation_rules.md` | `assets/T3.2_TS36.212_Table_5.1.3-3_original_crop.png`（2026-08-07 去重共用；原 T3.3 独立副本已删） | `tools/figures/render_lte_turbo_interleaver_table.py` | Markdown table | body_text_represented; asset_retained | `docs/L1_基础/T3.3_LTE_Turbo_segmentation_rules.md:164` |
| `docs/L1_基础/T3.4_NR_LDPC_segmentation_rules.md` | `assets/T3.4_TS38.212_Table_5.3.2-2_BG1.png` | `tools/figures/render_nr_ldpc_bg_tables_from_pdf.py, tools/figures/render_nr_ldpc_tables.py` | Markdown table | body_text_represented; asset_retained | `docs/L1_基础/T3.4_NR_LDPC_segmentation_rules.md:282` |
| `docs/L1_基础/T3.4_NR_LDPC_segmentation_rules.md` | `assets/T3.4_TS38.212_Table_5.3.2-3_BG2.png` | `tools/figures/render_nr_ldpc_bg_tables_from_pdf.py, tools/figures/render_nr_ldpc_tables.py` | Markdown table | body_text_represented; asset_retained | `docs/L1_基础/T3.4_NR_LDPC_segmentation_rules.md:296` |
| `docs/L2_协议算法/T10.3_NR_Polar_reliability_sequence.md` | `assets/T10.3_TS38.212_Table_5.3.1.2-1_Polar_sequence.png` | `tools/figures/render_nr_polar_reliability_sequence.py` | Markdown table | body_text_represented; asset_retained | `docs/L2_协议算法/T10.3_NR_Polar_reliability_sequence.md:147` |
| `docs/L2_协议算法/T6.4_LTE_Turbo_internal_interleaver.md` | `../L1_基础/assets/T3.2_TS36.212_Table_5.1.3-3_original_crop.png`（2026-08-07 去重共用） | `-` | Markdown table | body_text_represented; asset_retained | `docs/L2_协议算法/T6.4_LTE_Turbo_internal_interleaver.md:377` |
| `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md` | `assets/T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table_part1.png` | `tools/figures/render_nr_ldpc_bg_tables_from_pdf.py, tools/figures/render_nr_ldpc_lifting_qc_matrix.py` | Markdown table | body_text_represented; asset_retained | `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md:123` |
| `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md` | `assets/T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table_part2.png` | `tools/figures/render_nr_ldpc_bg_tables_from_pdf.py, tools/figures/render_nr_ldpc_lifting_qc_matrix.py` | Markdown table | body_text_represented; asset_retained | `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md:125` |
| `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md` | `assets/T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table_part3.png` | `tools/figures/render_nr_ldpc_bg_tables_from_pdf.py, tools/figures/render_nr_ldpc_lifting_qc_matrix.py` | Markdown table | body_text_represented; asset_retained | `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md:127` |
| `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md` | `assets/T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table_part1.png` | `tools/figures/render_nr_ldpc_bg_tables_from_pdf.py, tools/figures/render_nr_ldpc_lifting_qc_matrix.py` | Markdown table | body_text_represented; asset_retained | `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md:145` |
| `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md` | `assets/T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table_part2.png` | `tools/figures/render_nr_ldpc_bg_tables_from_pdf.py, tools/figures/render_nr_ldpc_lifting_qc_matrix.py` | Markdown table | body_text_represented; asset_retained | `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md:147` |
| `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md` | `assets/T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table.png` | `tools/figures/render_nr_ldpc_bg_tables_from_pdf.py` | not_applicable | evidence_only; compatibility_retained; not_current_body_reference | `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md:134` |
| `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md` | `assets/T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table.png` | `tools/figures/render_nr_ldpc_bg_tables_from_pdf.py` | not_applicable | evidence_only; compatibility_retained; not_current_body_reference | `docs/L2_协议算法/T8.3_NR_LDPC_lifting_QC_matrix.md:154` |
