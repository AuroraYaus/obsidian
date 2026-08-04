# T2 系列整体重编号报告（按接收链路因果链）

- **日期**：2026-08-04
- **主提交**：`8d79b9f38` refactor(lectures): T2 系列按接收链路因果链整体重编号（T2.0-T2.19）+ 资产与全库引用同步（96 files changed, +1295/-1749）
- **范围**：`3gpp/`（讲义、资产、全库引用、审计/工具/计划文档中的 T2.x 引用）

## 1. 新旧编号对照（映射表确认）

| 旧 | 新 | 讲义主题 | 旧 | 新 | 讲义主题 |
|:--:|:--:|:--|:--:|:--:|:--|
| 2.0 | 2.0 | OFDM 系统全景（不变） | 2.12 | 2.7 | OFDM 定时同步 |
| 2.1 | 2.1 | 子载波间隔基础（不变） | 2.13 | 2.8 | OFDM CFO/SFO 频率同步 |
| 2.2 | 2.2 | NR 时域层级（不变） | 2.7 | 2.9 | AWGN 噪声缩放 |
| 2.3 | 2.3 | NR 频域资源网格（不变） | 2.14 | 2.10 | OFDM 信道估计（DMRS） |
| 2.5 | 2.4 | LTE 帧结构（时频） | 2.15 | 2.11 | OFDM 均衡与 CSI/SINR |
| 2.4 | 2.5 | MCS 调制阶数与目标码率 | 2.16 | 2.12 | MIMO-OFDM 层检测 |
| 2.6 | 2.6 | 资源网格到译码器 LLR（不变） | 2.8 | 2.13 | BPSK/QPSK 软解调 |
| — | — | — | 2.9 | 2.14 | QAM Max-Log-MAP 解映射 |
| — | — | — | 2.10 | 2.15 | 衰落信道 LLR 可靠度 |
| — | — | — | 2.11 | 2.16 | LLR 裁剪/缩放/量化 |
| — | — | — | 2.19 | 2.17 | OFDM 失真到 LLR |
| — | — | — | 2.17 | 2.18 | OFDM PAPR 与功放 |
| — | — | — | 2.18 | 2.19 | OFDM 加窗与滤波 |

接收链路因果链：帧结构(4) → MCS(5) → 资源网格→LLR 地图(6) → 定时(7) → 频偏(8) → 噪声(9) → 信道估计(10) → 均衡(11) → MIMO(12) → 软解调(13/14) → LLR 可靠度(15/16) → 失真汇总(17) → 发射端 PAPR(18) → 加窗(19)。

## 2. 重命名清单

### 讲义（15 个，git mv，两阶段临时名规避 2.4↔2.5、2.8↔2.13、2.17→2.18→2.19、2.7→2.9→2.14→2.10→2.15→2.11→2.16→2.12→2.7 环）

```
T2.12_OFDM_timing_synchronization.md        → T2.7_OFDM_timing_synchronization.md
T2.13_OFDM_CFO_SFO_frequency_synchronization.md → T2.8_OFDM_CFO_SFO_frequency_synchronization.md
T2.7_AWGN_noise_scaling.md                  → T2.9_AWGN_noise_scaling.md
T2.14_OFDM_channel_estimation_DMRS.md       → T2.10_OFDM_channel_estimation_DMRS.md
T2.15_OFDM_equalization_CSI_SINR.md         → T2.11_OFDM_equalization_CSI_SINR.md
T2.16_MIMO_OFDM_layer_detection.md          → T2.12_MIMO_OFDM_layer_detection.md
T2.8_BPSK_QPSK_soft_demapping.md            → T2.13_BPSK_QPSK_soft_demapping.md
T2.9_QAM_Max_Log_MAP_demapping.md           → T2.14_QAM_Max_Log_MAP_demapping.md
T2.10_fading_channel_LLR_reliability.md     → T2.15_fading_channel_LLR_reliability.md
T2.11_LLR_clipping_scaling_quantization.md  → T2.16_LLR_clipping_scaling_quantization.md
T2.19_OFDM_impairments_to_LLR.md            → T2.17_OFDM_impairments_to_LLR.md
T2.17_OFDM_PAPR_power_amplifier.md          → T2.18_OFDM_PAPR_power_amplifier.md
T2.18_OFDM_windowing_filtering.md           → T2.19_OFDM_windowing_filtering.md
T2.5_LTE_frame_structure_time_frequency.md  → T2.4_LTE_frame_structure_time_frequency.md
T2.4_MCS_modulation_order_target_code_rate.md → T2.5_MCS_modulation_order_target_code_rate.md
```

### 资产（27 个 SVG，仅改编号前缀，英文部分不变）

T2.12_*（3 个）→ T2.7_*；T2.13_*（3）→ T2.8_*；T2.14_*（3）→ T2.10_*；T2.15_*（3）→ T2.11_*；T2.16_*（3）→ T2.12_*；T2.17_*（3）→ T2.18_*；T2.18_*（3）→ T2.19_*；T2.19_*（3）→ T2.17_*；T2.4_mcs_staircase.svg → T2.5_mcs_staircase.svg；T2.5_*（2）→ T2.4_*。
T2.1/T2.2/T2.3/T2.6 资产与 4 个 .mmd（T2.1/T2.3）不变。总数 46 个 SVG 不变。

## 3. 替换统计

- 全库两步占位替换（`T2.N → T2xN_PH → T2.M`，避免循环映射冲突）：**96 个文件、1131 处命中**（.md/.py/.json/.txt/.js/.svg）。
- 注意：任务给定脚本的映射 dict 用 float key（2.12）而查找用 `M[int(...)]`，首跑抛 `KeyError: 1`；改为 int key 后成功。首跑未写入任何文件，无污染。
- SVG 内容（`@file`/`@note` 头注释与文本标签）同步替换；已确认无 path `d=` 数据中的误匹配（`T2.` 不存在于任何路径数据中）。
- 入口文件 `docs/L1_基础/L1_基础入口.md` M2 列表按新编号升序重排（T2.0→T2.19，20 项）。
- `tools/audit_reference_rebuilds.py` 生成的 `docs/audits/reference_rebuild_candidates_full.txt` 用工具重新生成（866 行，路径全部为当前编号）。
- 手工语义修正（机械替换破坏的区间端点/旧旧编号残留）：
  - T2.0：7 处区间端点（`T2.1–T2.17`→`T2.1–T2.19`、`T2.7–T2.17`→`T2.7–T2.19` 等，原区间 `T2.12–T2.19` 的终点 2.19 被错误映射为 2.17）。
  - T2.1×2、T2.6×4、T2.16×2：区间折叠为精确列表（如 `T2.9–T2.16`→`T2.9、T2.13–T2.16`、`T2.4`→`T2.5`（Q_m=MCS））。
  - 根目录学习路线 `2026-06-19-lte-nr-decoding-learning-roadmap.md`：M2 五张卡片与 4 处前置引用从旧旧编号映射到新编号（T2.1/2/3/4/5 → T2.9/13/14/15/16）。
  - `docs/audits/reference_rebuild_candidates_review.md`：`T2.1-T2.3`→`T2.13-T2.14`。

## 4. 验证输出

- 讲义文件数：`ls docs/L1_基础/T2.*.md | wc -l` = **20**；资产 `T2.*.svg` = **46**。
- 死链检查：全库 wikilink 全部可解析；仅剩的 `[[T2.1_AWGN...]]` 字样位于**刻意还原的历史计划文件**（见 concerns），非真实链接。
- 图片引用：45 个唯一 `![](...assets/T2.x_*.svg)` 嵌入全部解析到实际文件。
- 旧编号残留扫描（旧文件名组合模式，如 T2.12_OFDM_timing、T2.4_MCS_mod、T2.7_AWGN_noise）：全库干净。
- frontmatter 抽查（aliases + source_spec 同步正确）：

```yaml
# docs/L1_基础/T2.9_AWGN_noise_scaling.md
aliases:
  - T2.9 AWGN noise scaling
source_spec: "docs/L1_基础/T2.9_AWGN_noise_scaling.md"

# docs/L1_基础/T2.17_OFDM_impairments_to_LLR.md
aliases:
  - T2.17 OFDM impairments to LLR
source_spec: "docs/L1_基础/T2.17_OFDM_impairments_to_LLR.md"

# docs/L1_基础/T2.5_MCS_modulation_order_target_code_rate.md
aliases:
  - T2.5 MCS modulation order target code rate
source_spec: "docs/L1_基础/T2.5_MCS_modulation_order_target_code_rate.md"
```

- git 检出 42 个重命名（15 讲义 + 27 资产），相似度 89-100%。

## 5. Concerns（刻意还原的历史文档与已知残留）

1. **历史计划/规格文档被机械替换污染后已还原到 HEAD**（它们描述的是已被取代的编号方案，替换会让其内部示例失去意义）：
   - `docs/superpowers/plans/2026-07-27-lte-nr-phy-t2-implementation.md`
   - `docs/superpowers/specs/2026-07-27-lte-nr-phy-t2-design.md`
   - `docs/superpowers/plans/2026-06-19-l1-remaining-lessons.md`
   - `docs/superpowers/plans/2026-06-19-lte-nr-decoding-roadmap.md`
   - `docs/superpowers/specs/2026-06-19-lte-nr-decoding-roadmap-design.md`
   - `tools/ppt/build_t2_t3_visual.js`、`tools/ppt/build_t2_t3_overview.js`（旧 PPT 构建脚本，内嵌旧旧编号）
   - 这些文件仍含旧编号，属历史记录，验证扫描已排除。
2. **根目录学习路线**的 M2 模块仍为"5 个任务"结构（2026-06-19 遗留，只列软解调核心 5 讲），未扩展为入口文件的 20 讲；卡片编号已与新方案一致，结构未动（超出重编号范围）。
3. `.obsidian/graph.json`、`.obsidian/workspace.json` 含旧路径（Obsidian 应用状态，仓库根、超出 `3gpp/` 范围），未改动未提交；Obsidian 刷新后可自愈或需手动更新。
4. `docs/audits/` 中个别旧旧编号散文引用（如 prompt_coverage_matrix 中"T2.1 噪声方差"）在替换前即已失效，属审计文档的历史残留，未逐一语义改写（本次仅修 review 文件一处明显的 BPSK/QPSK/QAM 引用）。
