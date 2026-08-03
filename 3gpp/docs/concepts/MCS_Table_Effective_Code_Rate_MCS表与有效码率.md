---
type: definition
aliases:
  - MCS Table
  - MCS 表
  - Effective Code Rate
  - 有效码率
  - R_eff
  - ps_mcs_table
tags:
  - 3gpp
  - concepts
  - protocol
source_spec: "TS 38.214 §5.1.3; evaluation-link-simulator MCS 表"
---

# MCS Table & Effective Code Rate MCS表与有效码率

调制与编码方案表（MCS Table）把调度索引（MCS index）映射为调制阶数（modulation order，Qm）与目标码率（target code rate，R）——PS 场景还额外含整形强度（shaping parameter，ν）；而"有效码率"（effective code rate，R_eff）是实际 payload 折算出来的真实码率，与目标码率脱钩。

## 独立解释任务

任务目标：解释 4 张 MCS 表的结构差异（标准 qam64 表、标准 qam256 表、非标准 ps_mcs_table1、ps_mcs_table2）、PS 表为什么 SE≠Qm×R/1024、以及 R_eff 与目标码率脱钩的含义。

## 科学定义

- **标准表**：qam64 表（MCS 0-28，QPSK/16QAM/64QAM）、qam256 表（MCS 0-31，其中 28-31 保留）——仿真器内部解析为 3 列 [MCS, Qm, R×1024]；TS 38.214 表格本身为 4 列（含频谱效率），频谱效率（spectral efficiency，SE）= Qm×R/1024 严格成立
- **PS 表**：ps_mcs_table1/2（MCS 5-27，5 列含 ν_MB；1024QAM 仅出现在 MCS 24-27，Qm=10）
- **5 列结构**：[MCS, SE, Qm, R×1024, ν_MB]；SE = Qm×R/1024 只在标准表成立，PS 表不成立
- **PS 表 SE ≠ Qm·R/1024**：MCS 10 表值 2.5704 vs 按 (Qm, R) 折算的 4.5——整形压缩了信息速率，SE 列直接列出整形后实际可达值，不能再由 Qm 与 R 相乘得出
- **有效码率**：$R_{\text{eff}} = N_{\text{TBS}}/(N_{\text{RE}} \cdot Q_m)$——由 payload 折算的真实码率，与目标码率 R 脱钩；整形、DMRS/控制开销都会让 R_eff 偏离 R，所以 PS 与 Uniform 公平比较必须用 R_eff（TBS matching 后同码率比能量）

## 直观模型

"菜单 vs 实付"：MCS 表是菜单——上面标注的是标称码率（Qm×R）；R_eff 是结账时的实付——由实际点的 payload 折算出来。整形像是"点了 4.5 份、实际上桌只有 2.57 份"：菜单没变、实付变低了。因此比较两家餐厅（PS vs Uniform）谁更划算，必须按实付金额（R_eff）算，不能看菜单标注。

## 常见误解

| 误解 | 正确理解 |
|:---|:---|
| PS 表的 SE 就是 Qm×码率 | PS 表 SE 已扣除整形压缩，直接列出可达值（MCS10: 2.5704 vs 4.5） |
| 有效码率 = 目标码率 | R_eff 是 payloadTBS/(N_RE·Qm)，整形/开销都会让它偏离 R |
| 1024QAM 是标准 MCS 能力 | 1024QAM 只在 PS 表 MCS 24-27，标准表不含 |

## 协议锚点

- MCS/TBS：TS 38.214 Rel-19 §5.1.3。
- 本地锚点：`3GPP_Rel19/processed/TS_38.214_38214-j30/content.md`。
- 仿真器实现：`getMcsInfo.m`（4 表硬编码，5 列解析）、`resolveMcsInfo.m`（表选择 + nu 参数流）。

## 图谱关联

- [[概念图谱入口]]
- [[TB_传输块]]
- [[QAM1024_1024QAM]]
- [[Probabilistic_Shaping_概率整形]]
- [[MB_Distribution_MB分布]]
- 关系语义：MCS 表把 MCS 索引映射到 (Qm, 码率, ν)；PS 表多一列 ν_MB 使整形参数进入链路选择，R_eff 是跨 PS/Uniform 公平比较的统一口径。
