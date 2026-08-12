# Plan: 上行链路概念笔记批次（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-12）_

## Goal

按全链路规划阶段 1 剩余批次（G4 上行链路）：5 篇概念笔记（DFT-s-OFDM / 上行功率控制 / PRACH / SRS / 上下行差异），织入现有层，同步图谱/术语表，全量验证后双推。依赖已就绪：控制面（PDCCH/DCI/PUCCH）、调度（Scheduler/Grant/HARQ_Process/Link_Adaptation）批次已建成。

## Approach

1. 5 篇概念笔记（六段式，术语配对三件套在计划内容中写全——连续两批次 30+ 处返工教训）：
   - `DFT_sOFDM_上行波形`（SC-FDMA/DFT-s-OFDM 原理、PAPR 优势、与 OFDMA 对比）
   - `Power_Control_上行功率控制`（开环/闭环、TPC、PHR、功控公式）
   - `PRACH_随机接入`（前导/四步 RACH/两步 RACH/时频资源）
   - `SRS_探测参考信号`（上行探测/波束/TDD 互易性）
   - `UL_DL_Differences_上下行差异`（NR 上下行处理链全景，T7.5 先例对照，收尾篇）
2. 创建顺序：E1-E4（独立可并行）→ E5（引用全部四篇，最后建）。
3. 同步清单：图谱入口挂载 5 篇（PRACH/SRS/DFT-s-OFDM→发送链路组、Power_Control/UL_DL_Differences→协议结构组）；L0 术语总表登记 5 项（SRS/PHR/TA/SC-FDMA/TPC——PRACH 已有）；概念笔记索引 5 行（2 列格式）；计数 87→92。
4. 工具扩展：**TECH_TERMS 本次不扩**（TA 15 篇讲义返工面大，与 PDCCH/PUCCH/PBCH/NDI/RI 等治理合并阶段 2 前置任务）。
5. 全量审计 + 双推。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 批次内容 | G4 全量 5 篇 | 用户裁定；一次铺完上行链路 |
| 工具扩展 | 不扩 TECH_TERMS | TA 返工面 15 篇，合并阶段 2 治理 |
| 术语表 | 登记 5 项 | 首现即登记（PRACH 已有） |
| 创建顺序 | E1-E4 → E5 | E5 收尾篇引用批内全部四篇 |
| 分组 | PRACH/SRS/DFT-s-OFDM→发送链路；Power_Control/UL_DL_Differences→协议结构 | 与概念图谱入口分组逻辑一致 |

## Risks / open questions

- PRACH 前导序列长度（LTE 839/ZC、NR 139 长前导）与四步/两步 RACH 流程实施时核验本地 TS 38.211 §6.3.3/38.213 §8。
- 功控公式（P = P0 + α·PL + ΔTF + f）参数以 TS 38.213 §7 本地为准。
- 计数 87→92 以实施时实测为准。
- 阶段 2 前置任务登记更新：TA/SRS/PHR/SC-FDMA/TPC 并入 TECH_TERMS 全库治理清单。

## Out of scope

- G2 发送端镜像批次（后续）。
- TECH_TERMS 全库治理（阶段 2 前置）。
- 上行深化讲义（阶段 2-3）。
