# Plan: MAC 层映射/载波聚合/BWP/射频前端概念笔记批次（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-12）_

## Goal

按选项 3 批 B（协议层 + 前端）：4 篇概念笔记（MAC 层映射 / 载波聚合 / BWP / 射频前端），织入现有层，同步图谱/术语表，全量验证后双推。完成后选项 3 全量收官（规划 G8-G10 缺口闭合）。

## Approach

1. 4 篇概念笔记（六段式，术语配对三件套在计划内容中写全——五批次 60+ 处返工教训）：
   - `MAC_Layer_Mapping_MAC层映射`（逻辑→传输→物理信道三层映射、MAC PDU 复用/LCP）
   - `Carrier_Aggregation_载波聚合`（多 CC 聚合、PCell/SCell、跨载波调度、每载波 HARQ）
   - `BWP_带宽部分`（激活带宽内子带、省电/能力适配、初始/默认 BWP、与 T2.3 讲义衔接）
   - `RF_Frontend_射频前端`（AGC/ADC/IQ 不平衡/相位噪声、损伤到 LLR 退化——非协议强制，标注教材背景 + T2.17 锚点）
2. 创建顺序：H1-H4（独立）→ 无收尾篇（四篇平级，各自链接既有体系）。
3. 同步清单：图谱入口挂载 4 篇（MAC_Layer_Mapping/CA/BWP→协议结构组、RF_Frontend→信道与信号组）；L0 术语总表按现状登记（CC/SCell/PCell/CA/BWP/AGC/ADC 等缺项）；概念笔记索引 4 行；计数 100→104。
4. 工具扩展：不扩 TECH_TERMS（同模式，合并阶段 2 治理）。
5. 全量审计 + 双推。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 批次内容 | 批 B 4 篇 | 用户裁定；选项 3 收官 |
| 工具扩展 | 不扩 TECH_TERMS | 同前批模式 |
| 分组 | MAC/CA/BWP→协议结构；RF_Frontend→信道与信号 | 与概念图谱入口分组逻辑一致 |
| RF 定位 | 非协议强制，标注教材背景 | Rule 2 边界声明（射频实现非 3GPP 规范） |

## Risks / open questions

- CA 载波数（NR 最多 16 CC）/跨载波调度（CIF 3-bit）实施时核验本地 TS 38.300 §5.2。
- BWP 配置（初始/默认/激活 BWP、switch 时延）实施时核验 TS 38.213 §12。
- 术语表登记项按实施时现状（BWP 在 T2.3 讲义已详讲、概念笔记登记补缺）。
- 计数 100→104 以实施时实测为准。

## Out of scope

- TECH_TERMS 全库治理（选项 2）。
- 阶段 2 深化讲义（选项 1）。
- **选项 3 收官登记**：本批次完成后规划 G8-G10 缺口闭合，选项 3 全量完成，下一项为选项 2（结构治理）。
