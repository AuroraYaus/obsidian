# Plan: 调度与 HARQ 进程概念笔记批次（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-12）_

## Goal

按全链路规划阶段 1 剩余批次（G3 调度与 HARQ 进程）：4 篇概念笔记（MAC 调度器与资源分配 / HARQ 进程管理 / 链路自适应与 CQI / 调度与授权），织入现有层，同步图谱/术语表，全量验证后双推。依赖已就绪：PDCCH/DCI/PUCCH（控制面批次 1）已建成。

## Approach

1. 4 篇概念笔记（六段式，术语配对三件套在计划内容中写全——控制面批次 15+ 处返工教训）：
   - `Scheduler_MAC调度器与资源分配`（调度器角色/RBG/VRB/资源分配类型/频域时域调度/LCP）
   - `HARQ_Process_HARQ进程管理`（进程状态机/进程数/NDI 翻转/k0-k2 时序/同步异步）
   - `Link_Adaptation_链路自适应与CQI`（CQI 闭环/PMI/RI/SINR→CQI 映射/BLER 目标）
   - `Scheduling_Grant_调度与授权`（DL assignment/UL grant 流程/动态 vs SPS/configured grant/MU-MIMO）
2. 创建顺序：Scheduler → Grant（引用 Scheduler）→ HARQ_Process/Link_Adaptation（独立）。
3. 同步清单：图谱入口挂载 4 篇（Scheduler/Grant→协议结构组、HARQ_Process→HARQ 与速率匹配组、Link_Adaptation→信道与接收链路组）；L0 术语总表登记 8 项（CQI/PMI/RI/NDI/RBG/VRB/SPS/调度器）；概念笔记索引 4 行（2 列格式）；计数 83→87。
4. 工具扩展：**TECH_TERMS 本次不扩**（NDI 39 篇/RI 26 篇讲义返工面大，与 PDCCH/PUCCH/PBCH 治理合并为阶段 2 前置任务——用户裁定模式）；术语表登记即可。
5. 全量审计 + 双推。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 批次内容 | G3 调度与 HARQ 进程 4 篇 | 用户裁定；PDCCH/DCI 下游依赖最顺 |
| 工具扩展 | 不扩 TECH_TERMS | NDI/RI 返工面大（39/26 篇），与 PDCCH/PUCCH 治理合并阶段 2 |
| 术语表 | 登记 8 项 | 首现即登记（同步清单第 6 条） |
| 分组 | Scheduler/Grant→协议结构；HARQ_Process→HARQ 组；Link_Adaptation→信道与接收链路 | 与概念图谱入口现有分组逻辑一致 |
| 命名 | Scheduler_MAC调度器与资源分配 等 4 篇 | English_中文 惯例 |

## Risks / open questions

- RBG 尺寸表（TS 38.214 §6.1.2.2）与 VRB 交织（§6.1.2.3）实施时核验本地章节号。
- k0/k1/k2 默认值（k0=0/k1=1/k2=0 起）以 TS 38.213/38.214 本地为准。
- 计数 83→87 以实施时实测为准。
- 阶段 2 前置任务登记：NDI/RI/CQI/PMI/RBG/VRB TECH_TERMS 全库治理（合并 PDCCH/PUCCH/PBCH）。

## Out of scope

- G2 发送端镜像与 G4 上行链路批次（后续批次）。
- TECH_TERMS 全库治理（阶段 2 前置）。
- 深化讲义（阶段 2）。
