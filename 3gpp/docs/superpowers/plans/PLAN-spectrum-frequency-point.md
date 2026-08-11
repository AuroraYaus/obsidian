# Plan: 频谱与频点知识点入库（grill-me 拷问锁定版）
_Locked via grill — by Claude + AuroraYaus（2026-08-11）_

## Goal

把「频谱和频点」（含频段划分、ARFCN、信道栅格/同步栅格、接收端频点定位流程）写入 3gpp 知识库：新建概念笔记（六段式）+ T2.3 充实前置补节（Mermaid 坐标链图 + ARFCN 公式）+ 同步图谱入口与 L0 术语总表 + 术语审计工具扩展（ARFCN/GSCN）+ 全量验证后双推。内容为「核心答案（频谱 vs 频点区别）+ 深入讲解（公式/栅格/流程）」有机结合。

## Approach

1. 新建 `docs/concepts/Spectrum_and_Frequency_Point_频谱与频点.md`（六段式：频谱→频段→频点→ARFCN→信道栅格/同步栅格→接收端流程；FR1/FR2 频段表 + ARFCN 公式（NR/LTE 双版本）+ 栅格对照 + 常见误解 4 行）。
2. T2.3「前置知识检查」后插入充实补节（~40 行）：频谱→频段→频点→ARFCN 坐标链 + Mermaid 图（频谱→频段→信道栅格→同步栅格→SSB→ARFCN 对齐）+ ARFCN 公式 + wikilink。
3. 同步清单：概念图谱入口「信道与信号」挂载 1 行；L0 术语总表「系统与协议」节新增 9 项（频点/频谱/ARFCN/GSCN/信道栅格/同步栅格/频段/FR1/FR2）+「概念笔记索引」→「### 协议、信道与信号」分区追加 1 行（2 列格式）。
4. 工具扩展：`tools/audit_lesson_terms.py` TECH_TERMS 增 ARFCN/GSCN 两项（ARFCN 在 T2.3 已配对零返工；GSCN 连带修复 T2.8:418 首现配对）；**FR1/FR2 不扩**（9+5 篇讲义裸用，扩展需全量返工，登记术语总表并列为后续任务）。
5. 全量审计（headings/terms/latex --syntax-only/circled/link integrity/mermaid 真实渲染），修复 FAIL，双推提交。

## Key decisions & tradeoffs

| 决策 | 结论 | 理由 |
|:---|:---|:---|
| 落点 | 概念笔记 + T2.3 充实补节 | 与协议栈模式一致；ARFCN/栅格正是 T2.3 资源网格坐标系的来源；T2.x 编号已排满不新建讲义 |
| 补节深度 | 充实（~40 行） | 用户延续协议栈任务的选择；坐标链是 RE/PRB 主线的前置 |
| 图表 | 图+公式全配 | 补节 1 张 Mermaid 坐标链图 + ARFCN 公式（LaTeX 块级）；概念笔记含公式与对照表 |
| 工具扩展 | 只扩 ARFCN+GSCN | 用户裁定：FR1/FR2 扩展触发 14 篇讲义全量首现检查，范围膨胀一倍；登记总表 + 留作后续 |
| 概念笔记命名 | `Spectrum_and_Frequency_Point_频谱与频点.md` | English_中文 惯例；尊重用户主题词 |
| 插入位置 | T2.3「前置知识检查」（33 行）与「RE」（41 行）之间 | 坐标链先于资源网格主线 |

## Risks / open questions

- TS 38.101-1 §5.4.2.1（NR-ARFCN 表）精确本地行号实施时核验（T2.8 已核验 §5.4.3.1 在 `s00-0504` 卷 1141 行，§5.4.2.1 大概率同卷）。
- audit_lesson_terms 对表格内文本首现行为以实际运行为准（T2.8:418 在正文，低风险）。
- mmdc/KaTeX 工具缺失须显式声明验证缺口。
- 执行顺序：本计划在协议栈 SDD 流（Task 2 审查 + Task 3-6）完成后执行，两流不混跑。

## Out of scope

- FR1/FR2 加入 TECH_TERMS（后续任务）。
- 不新建独立讲义 T2.x（编号排满，重排成本高）。
- 不改 T2.8 正文（仅 GSCN 首现配对一行修复）。
- 概念笔记不放 Mermaid 图（图在 T2.3 补节；概念笔记用表格+公式）。
