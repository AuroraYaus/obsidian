# Plan: 控制面主线概念笔记批次 1（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-11）_

## Goal

按全链路规划（`specs/2026-08-11-full-link-knowledge-map.md`）阶段 0 + 阶段 1 控制面主线：结构修复 2 项 + 6 篇控制面概念笔记（TBCC/PSS_SSS/PBCH/PDCCH/DCI/PUCCH），织入现有层（概念笔记六段式），同步图谱/术语表，术语工具只扩 TBCC，全量验证后双推。

## Approach

1. 阶段 0：`Pilot_导频.md` 挂载概念图谱入口「信道与信号」组（孤儿节点修复）；T0.1 阅读地图补控制面/上行链路分支小节（~20 行）。
2. 阶段 1a 六篇概念笔记（六段式完整，依赖已就绪：T10 Polar 控制译码/T9.0 descriptor/T7.5 DL-UL 差异/T10.9 UCI 交织）：
   - `TBCC_咬尾卷积码`（LTE 控制编码第四块，Turbo 组）
   - `PSS_SSS_同步信号与小区搜索`（全链路起点）
   - `PBCH_MIB_广播信道`（小区搜索产出）
   - `PDCCH_物理下行控制信道`（最大空白：盲检核心）
   - `DCI_下行控制信息`（调度指令本体，descriptor 正面镜像）
   - `PUCCH_上行控制信道与UCI`（反馈链路闭环）
3. 同步清单：图谱入口挂载 6 篇 + 术语表登记 4 条（PBCH/MIB/SIB/TBCC）+ 概念笔记索引 6 行（2 列格式）+ 计数 77→83。
4. 工具扩展：TECH_TERMS 只扩 TBCC（T11.5 已配对，零返工）；**PDCCH/PUCCH/PBCH 全库配对治理（30+ 处）列为阶段 2 前置任务**（用户裁定）。
5. 全量审计 + 双推。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 范围 | 控制面主线 6 篇 | 全链路最大空白；依赖（T10/T9.0/T7.5/T10.9）已就绪 |
| 工具扩展 | 只扩 TBCC | 用户裁定：PDCCH/PUCCH/PBCH 扩展触发 30+ 处返工，留阶段 2 |
| 结构修复 | Pilot 挂载 + T0.1 补分支 | S2/S3（编号）已在规划文档登记，无需代码动作 |
| 批次内依赖 | TBCC→PDCCH/PBCH 被引用，先建 | wikilink 顺序：TBCC/PSS_SSS 先建，PBCH/PDCCH/DCI/PUCCH 后建 |
| 分组归属 | TBCC→Turbo 译码组；其余 5 篇→发送链路组 | 与概念图谱入口现有分组逻辑一致 |

## Risks / open questions

- PDCCH/PUCCH/PBCH 术语表条目已存在但讲义未配对——阶段 1a 的笔记内容自带完整配对，不影响；全库治理登记阶段 2。
- DCI/UCI 的 TECH_TERMS 已存在（L1/L2 讲义已有配对），6 篇笔记首现须自足配对。
- 计数 77→83 以实施时实测为准（含 Pilot 挂载不影响计数口径）。

## Out of scope

- 阶段 1 其余缺口（调度/上行/发送端镜像概念笔记）——后续批次。
- PDCCH/PUCCH/PBCH TECH_TERMS 全库治理——阶段 2 前置任务。
- 控制面深化讲义（阶段 2）——本批概念笔记铺开后另立计划。
