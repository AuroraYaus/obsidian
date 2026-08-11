# Plan: 协议栈与 OSI 知识点入库（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-11）_

## Goal

把「3GPP 层2 vs OSI 数据链路层 + OSI 各层典型协议」知识点写入 3gpp 知识库：新建 `Protocol_Stack_协议栈` 概念笔记（六段式）、T0.1 补节「3GPP 分层与 OSI 模型」（含 Mermaid 图 + 整合表）、同步图谱入口与 L0 术语总表、术语审计工具扩展并连带修复存量 RLC 首现，全量验证后双推。

## Approach

1. 新建 `docs/concepts/Protocol_Stack_协议栈.md`（六段式，含 OSI 七层协议表 + TCP/IP 四层 + Mermaid 分层图 + 常见误解 4 行）。
2. T0.1「协议分册如何分工」后插补节 `## 3GPP 分层与 OSI 模型`（~70 行：三层定义 + Mermaid 图 + 整合对照表 + TCP/IP 一句 + 结论 + wikilink）。
3. 同步清单：概念图谱入口「协议结构」挂载 1 行；L0 术语总表「系统与协议」节新增 5 行（OSI/协议栈/PDCP/SDAP/数据链路层）+「概念笔记索引」→「### 协议、信道与信号」分区 2 列格式追加 1 行。
4. 工具扩展：`tools/audit_lesson_terms.py` TECH_TERMS 增 OSI/PDCP/SDAP/RLC 四项；连带修复 T2.14:115、T9.6:376 的 RLC 首现配对。
5. 全量审计（headings/terms/latex --syntax-only/circled/link integrity/mermaid 真实渲染），修复 FAIL，双推提交。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 术语工具扩展 | **扩展 TECH_TERMS + 连带修复 T2.14/T9.6** | 用户裁定：工具化根治符合项目精神；PDCP/SDAP 无讲义触发属空转但无害，RLC 修复仅 2 处文本 |
| MAC 中文名 | 统一为**媒体接入控制层** | 全库既有标准（术语表 + 6 篇讲义），计划中"介质访问控制"为笔误 |
| 概念笔记索引 | 2 列格式，入「### 协议、信道与信号」分区 | 实测索引区为 2 列 `| [ [笔记]] | 一句话 |`，非计划初稿的 3 列 |
| LTE/NR 双侧 | 图注注明"图示为 NR，LTE 无 SDAP" | Mermaid 图按 NR 画（含 SDAP），LTE 用户面无 SDAP，避免误导 |
| 译码主线桥接 | 补节开头加一句"译码器工作在 L1 与 MAC 交付边界" | T0.1 是译码阅读地图，分层知识须与主线挂钩 |
| README 三份 | 不动 | 本次不改知识库结构/系列/规则，仅新增内容 |

## Risks / open questions

- `audit_lesson_terms.py` 对表格内文本的首现配对行为以实际运行结果为准（T9.6 的 RLC 位于表格行内）；若工具不扫表格，修复仍保留（Rule 10 合规）。
- TECH_TERMS 扩表后若发现未预料的存量 FAIL（如 OSI 在讲义中已有裸用——预查 docs/ 无 OSI，低风险），按 Task 4 修复流程处理。
- mmdc/KaTeX 工具缺失须显式声明验证缺口，不得默认通过。

## Out of scope

- 不新建 MAC/RLC/PDCP/SDAP 单层概念笔记（协议栈总览已覆盖，YAGNI）。
- 不新增 SVG/图片资产文件（Mermaid 代码块 2 处同源，无台账负担）。
- 不改 L2 系列讲义正文（仅 T2.14/T9.6 的 RLC 配对修复）。
- 不重排 T0.1 现有章节，仅插补节。
