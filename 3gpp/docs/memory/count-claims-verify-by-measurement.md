---
name: count-claims-verify-by-measurement
description: 知识库自指数字（术语/概念计数）必须实测行数校准，不能信任前序 commit 声明——2026-08-24 发现 254+104 口径与实测 241+105 漂移
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d6889ae-b0a7-441e-b008-cb96371c1da1
  modified: 2026-08-24T07:58:26.188Z
---

2026-08-24 PCICP 四概念入库时发现：README 三语与 项目规则与记忆索引.md 口径线声称"术语 254 + 概念索引 104、概念笔记 107"，但实测术语总表缩写数据行 241、概念笔记索引行 105——声称与实测漂移（前序 commit 9683c7f2f 还宣称"数字口径核实三语一致"）。

**Why:** 计数声明没有按实际行数核对就写入 commit message；"核实"可能只对照了声明之间的互相一致（三语互查），没有对照文件实况。计数类审计缺少"声称 → 实测"的对照工具。

**How to apply:** 任何批次涉及术语/概念/讲义计数时，用 grep/awk 实测行数（排除表头与分隔行）后再更新所有声明点；口径线（`项目规则与记忆索引.md` 第六节）以实测为准。相关：[[knowledge-base-sync-checklist]]。
