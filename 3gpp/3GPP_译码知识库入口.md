---
type: spec
aliases:
  - 3GPP LTE NR 译码链路
  - 3GPP 译码知识库
tags:
  - 3gpp
  - obsidian
  - index
source_spec: "Local vault index"
---

# 3gpp
3GPP LTE 和 NR 译码链路

## 入口

- [[Obsidian图谱标准化]]
- [[3gpp/3GPP_Rel19_资料入口总览]]
- [[3gpp/docs/concepts/概念图谱入口]]
- Rel-19 协议下载清单：`3gpp/3GPP_Rel19/Rel19_协议下载清单.md`
- [[3gpp/docs/3GPP_讲义入口]]
- [[3gpp/2026-06-19-lte-nr-decoding-learning-roadmap]]
- [[3gpp/sim/python/L0_crc_gf2/L0_CRC_GF2_仿真入口]]
- [[3gpp/CLAUDE]]
- [[3gpp/合规与遵从]]

## 项目规则与经验库（存储与索引）

- **规则**（每次会话自动加载）：`CLAUDE.md`（12 条硬性规则）、`合规与遵从.md`（23 条硬约束）、`.claude/rules/documentation.md`（DOXYGEN 与讲义规范）。
- **经验教训库**：`docs/audits/lessons/lesson-*.md`（10 条历史返工教训：SVG 审计盲区、字体度量、圈号禁令、Mermaid 引号节点、批量替换作用域、双推等）——随 git 双推永久保存，删除任何本地目录不影响。
- **可执行规则**：`tools/audit_svg_layout.py`（R1-R11 几何审计）、`tools/audit_circled_digits.py`、`tools/audit_mermaid_syntax.sh`。
- **索引**：`项目规则与记忆索引.md`（规则文件/经验库/同步清单/编号约定）。
