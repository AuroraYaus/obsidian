# Plan: 参考信号与波束管理概念笔记批次（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-12）_

## Goal

按选项 3 批 A（物理层：参考信号谱系 + 波束管理）：5 篇概念笔记（CSI-RS / PTRS / TRS / CRS / 波束管理），织入现有层，同步图谱/术语表，全量验证后双推。完成后选项 3 剩余批 B（协议层：MAC 映射/CA/射频前端）。

## Approach

1. 5 篇概念笔记（六段式，术语配对三件套在计划内容中写全——四批次 50+ 处返工教训）：
   - `CSI_RS_信道状态信息参考信号`（下行测量 RS：CSI 测量/波束管理/跟踪三用途、时频结构、与 Link_Adaptation 衔接）
   - `PTRS_相位跟踪参考信号`（相位噪声补偿、与 SCS/调制阶数的关系）
   - `TRS_跟踪参考信号`（时频跟踪、CSI-RS 子集配置（trs-Info））
   - `CRS_小区特定参考信号`（LTE 专属：小区级 RS、解调/测量、与 NR DMRS 的制式差异——标注非 NR）
   - `Beam_Management_波束管理`（SSB/CSI-RS 波束测量、波束报告、BFR（波束失败恢复）、与 TDD 互易性衔接）
2. 创建顺序：G1-G4（独立）→ G5（Beam_Management 收尾引用全部或部分）。
3. 同步清单：图谱入口挂载 5 篇（发送链路组或信道与信号组——CSI_RS/PTRS/TRS/CRS→「信道与信号」组（DMRS 所在？DMRS 在发送链路组——参考信号体系按组逻辑定，实施时按现状）；Beam_Management→发送链路组）；L0 术语总表登记 4 项（PTRS/TRS/CRS/BFR——CSI-RS 已有）；概念笔记索引 5 行；计数 95→100。
4. 工具扩展：不扩 TECH_TERMS（CSI-RS 8 篇返工面，合并阶段 2 治理）。
5. 全量审计 + 双推。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 批次内容 | 批 A 5 篇（参考信号 4 + 波束 1） | 用户裁定两批方案 |
| 工具扩展 | 不扩 TECH_TERMS | CSI-RS 返工面 8 篇，合并治理 |
| 创建顺序 | G1-G4 → G5 | G5 收尾引用 |
| CRS 定位 | LTE 专属，标注制式差异 | Rule 2 边界声明（本地有 TS 36.211） |

## Risks / open questions

- CSI-RS/PTRS/TRS 时频结构（CSI-RS 端口数/密度、PTRS 与 SCS 关系表、TRS=CSI-RS 子集）实施时核验本地 TS 38.211 §7.4.1。
- CRS 锚点 TS 36.211 §6.10（本地 `TS_36.211_*` 存在）。
- 计数 95→100 以实施时实测为准。

## Out of scope

- 批 B（MAC 层映射/CA/BWP/射频前端）——后续批次。
- TECH_TERMS 全库治理（选项 2）。
- 阶段 2 深化讲义（选项 1）。
