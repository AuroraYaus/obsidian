---
name: obsidian-graph-config-versioning
description: .obsidian/graph.json 承载图谱颜色分组/过滤规则/孤立节点开关，必须随仓库版本控制（2026-09-04 换机实测缺失教训）
metadata:
  type: project
---

graph.json 与 workspace.json 易失性不同：workspace.json 每次会话必改写（保持 .gitignore 忽略）；graph.json 仅在修改图谱设置时变化（2026-09-04 重新纳入版本控制）。图谱颜色分组（33 组 tag/path/type 查询）、过滤规则（`path:3gpp/docs -path:...lessons -path:...3GPP_Rel19`）、隐藏孤立节点开关全存于 graph.json——另一台机器 clone 后该文件缺失，图谱无颜色、无过滤、非知识库文件与孤立节点全显。

**Why:** 2026-08-14 仓库治理把 graph.json 与 workspace.json 一并移出版本控制，graph.json 被"连坐"误伤；2026-09-04 用户换机打开图谱才暴露。图谱配置是知识库的展示契约，属配置类（同 app.json/appearance.json/snippets），不属易失状态。

**How to apply:** UI 状态文件按"是否随正常使用自变"区分易失与否，不按"是否在 .obsidian/ 下"一刀切；换机/拷贝项目后验证图谱颜色与过滤是否生效（vault 根必须是仓库根）；相关 [[lesson-link-obsidian-hollow-nodes]]。
