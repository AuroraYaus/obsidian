# Plan: M14 控制信道族深化讲义批次（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-13）_

## Goal

按全链路规划阶段 2（选项 1 深化讲义）：M14 控制信道族 5 篇完整讲义（T14.1-T14.5），把控制面概念笔记（6 篇已就绪）升级为 500-800 行完整讲义，完成控制面从概念到讲义的知识闭环。

## Approach

1. 5 篇讲义（每篇 500-800 行，遵循讲义模板：学习目标/前置检查/内容章节/示范例题/引导练习/独立习题/小结 + ≥1 教学图 + 内嵌 numpy 验证实跑 + 协议锚点）：
   - `T14.1_PDCCH_blind_decoding.md`（PDCCH 盲检：CORESET/REG/CCE/聚合等级/搜索空间/RNTI/盲检流程/复杂度）
   - `T14.2_DCI_format_detailed.md`（DCI 格式精读：0_x/1_x/2_x 全字段、descriptor 映射、T9.0 衔接）
   - `T14.3_PUCCH_UCI_formats.md`（PUCCH format 0-4、UCI 编码、HARQ-ACK 时序 k1、承载选择）
   - `T14.4_PBCH_cell_search_system_info.md`（小区搜索流程、PBCH 编码、MIB/SIB1/SIB 层级）
   - `T14.5_TBCC_decoding.md`（咬尾 Viterbi/BCJR 译码、数值走读、与 Turbo 对照）
2. 每篇讲义：概念笔记为内容底座（wikilink 双向）、前置依赖讲义锚定（T10 Polar 控制译码/T9.0 descriptor/T7.5）、≥1 教学图（复杂图手绘 SVG 经 audit_svg_layout R1-R11、简单流程 Mermaid）。
3. 同步：L2 入口 M14 模块登记、编号 T14.x（已确认空闲）、图片资产台账（如有 SVG）、概念笔记回链。
4. 全量审计（8 项含 audit_term_first_use）+ 双推。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 深化系列 | 控制信道族（规划阶段 2） | 用户裁定；最大空白从概念升级讲义 |
| 批次规模 | 5 篇一轮 | 用户裁定；符合规划阶段 2 完整定义 |
| 编号 | T14.x（M14 模块） | 项目规则 L2 用 M14+；T14 已确认空闲 |
| 讲义底座 | 概念笔记 6 篇（已就绪） | 内容与 wikilink 双底座 |
| 教学图 | 每篇 ≥1（SVG/Mermaid 按绘图政策） | 讲义规范 §2.3 |

## Risks / open questions

- 讲义 500-800 行/篇——5 篇为大型创作工程（一轮 SDD，每篇一子任务 + 逐篇审查）。
- 教学图数量：每篇 ≥1——SVG 需过 audit_svg_layout R1-R11（重绘检查四查）。
- numpy 验证：每篇 1 个内嵌验证实跑（如 PDCCH 盲检候选数计算、TBCC 咬尾 Viterbi 小例）——实跑通过后写入正文。
- 前置依赖：T14.1 依赖 T10（Polar 控制译码）、T14.2 依赖 T9.0、T14.4 依赖 T2.7/T2.8（同步）——讲义内明确前置知识检查。

## Out of scope

- 上行链路（阶段 3）与发送端镜像（阶段 4）讲义——后续批次。
- 概念笔记层（已收官 104 篇）。
- 术语治理（已收官，audit_term_first_use 全绿）。
