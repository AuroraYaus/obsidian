# Plan: 通信基础三件套知识点入库（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-11）_

## Goal

补齐知识库缺失的通信基础三件套（详细分析）：多址接入（FDMA/TDMA/CDMA/OFDMA）、键控调制（ASK/FSK/PSK）、扩频与解扩（DSSS）。三篇独立概念笔记（六段式，图+公式全配），同步图谱入口与术语总表，术语审计工具八项全扩，全量验证后双推。

## Approach

1. 新建 3 篇概念笔记（各 200-400 行详细分析）：
   - `docs/concepts/Multiple_Access_多址接入.md`（FDMA/TDMA/CDMA/OFDMA：资源划分示意 Mermaid 图 + 对比表 + 演进史 + LTE/NR 选 OFDMA 的原因 + OFDMA 正交性公式）
   - `docs/concepts/ASK_FSK_PSK_键控调制.md`（分类树 Mermaid + 三键控信号表达式 LaTeX + 波形/解调/误码对比表 + 到 BPSK/QPSK/QAM 的演进衔接）
   - `docs/concepts/Spreading_扩频与解扩.md`（扩频-解扩流程 Mermaid + 扩频增益公式 + DSSS 原理 + 与 CDMA 关系 + 4G 弃用 CDMA 的原因）
2. 同步清单：概念图谱入口「信道与信号」挂载 3 篇；L0 术语总表登记 11 项（OFDMA/CDMA/TDMA/FDMA/WCDMA/ASK/FSK/PSK/DSSS/扩频/解扩）；概念笔记索引「### 协议、信道与信号」分区 3 行（2 列格式）。
3. 工具扩展：`tools/audit_lesson_terms.py` TECH_TERMS 追加 9 项（OFDMA/CDMA/TDMA/FDMA/WCDMA/ASK/FSK/PSK/DSSS）——自查零返工（独立裸用均 0 处；正则负向断言不会误匹配 BPSK/mask 等子串）。
4. 全量审计 + 双推。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 组织方式 | 3 篇独立概念笔记 | 用户裁定；扩频与 CDMA 虽紧密但用户单独列出，独立成篇互链 |
| 图表公式 | 图+公式全配 | 用户裁定；详细分析需要直观承载（资源划分/分类树/流程 + 信号表达式/处理增益） |
| 工具扩展 | 九项全扩 | 用户裁定；自查零返工（PSK 21 篇含 PSK 均为 BPSK/QPSK 子串，正则安全） |
| 落点 | 概念笔记（无讲义补节） | 用户未选"讲义补节"选项；L1 编号排满不新建讲义 |
| 双链 | 调制↔调制星座/T2.13/T2.14；多址↔频谱频点/T2.0；扩频↔多址接入 | 既有笔记/讲义 wikilink 闭环 |

## Risks / open questions

- WCDMA 的协议锚点：TS 25.213 属 3G 制式，本地 3GPP_Rel19 无 TS 25 系列——笔记中标注"本地无 TS 25 资料，锚点仅指标准"（合规 Rule 2 边界声明）。
- GMSK（GSM）非 3GPP LTE/NR 内容——标注为非本项目主线制式的背景知识。
- 概念笔记索引引言「71 篇」计数已过期（现 73 篇）——本计划 Task B4 与协议栈 Task 5 一并修正为实际数。

## Out of scope

- 讲义补节（T2.0 补 OFDMA 等）——用户未选。
- 新独立讲义 T 系列（编号排满）。
- FHSS（跳频扩频）仅作对比提及，不独立成篇。
- ic 项目规则复制（已完成，见 PLAN-qa-pipeline）。
