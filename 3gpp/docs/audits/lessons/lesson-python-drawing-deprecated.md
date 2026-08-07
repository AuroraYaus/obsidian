---
name: lesson-python-drawing-deprecated
description: Python 绘图禁令与 SVG/PlantUML 分工；新增资产前台账查重（T3.3/T3.2 重复教训）
metadata:
  type: feedback
---

# Python 绘图禁令与 SVG/PlantUML 分工（2026-08-07）

**政策（用户确立）**：以后都不使用 Python 绘图。复杂图用手绘 SVG（默认），**只有特别大型的图**用 PlantUML；简单流程/结构图仍用 Mermaid。存量 Python 绘图工具（17 个）已归档 `tools/archive_python_drawing/`（不再使用，git 可恢复）；协议原文截图类 PNG 保留；讲义正文中的工具路径引用已同步改为 archive 路径（218 处）。

## 触发教训

用户发现 `T3.3` 与 `T3.2` 各有一张 **TS 36.212 Table 5.1.3-3 协议原文截图**（都来自 source.pdf 第 16 页，1320×1690 裁剪版 vs 2360×6060 高清版）——同源同表重复资产，T3.3 生成时未检查 T3.2 已嵌入该表。按用户指示删除 T3.3 副本、两篇（T3.3 + T6.4 引用）共用 T3.2 资产，台账同步更新。

**Why:** 绘图资产没有"新增前查重"环节——同类协议表/图在两篇讲义各自生成，既浪费又造成图谱/台账冗余。另：规则文件（合规 Rule 18/23）中的实现媒介措辞（PIL anchor、脚本画布）绑定 Python，政策变更后必须迁移为 SVG/PlantUML 等价写法（text-anchor/dominant-baseline、引擎自动布局），否则规则与新政策矛盾。

**How to apply:**
- 任何新图（SVG/PlantUML/协议截图）嵌入前，先查 `docs/audits/image_asset_inventory.md` 是否已有同源资产（同步清单第 5 条已固化）
- 复杂图 → 手绘 SVG（audit_svg_layout.py R1-R11）；特别大型图 → PlantUML（`bash tools/audit_plantuml_syntax.sh` 真实渲染验证）；禁止新写 Python 绘图脚本
- 协议表/图引用多篇讲义时，指定一篇为主资产，其余引用之（T3.3 案例）
- 相关：[[lesson-knowledge-base-sync-checklist]]（第五类图片资产变化）、CLAUDE.md 第 13 条、documentation.md §4.1
