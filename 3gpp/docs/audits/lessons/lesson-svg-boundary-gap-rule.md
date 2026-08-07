# svg-boundary-gap-rule

> SVG 规则：文本框边界与框外文字/其他文本框间距 ≥8px；任何形式重叠不允许

SVG 绘图规则（用户 2026-08-04 反馈）：**文本框边界必须与框外的文字或其他文本框边界保持适当距离（投影间距 ≥ 8px）**；**任何形式的重叠都不允许**（text-text、text 与异宿主 rect、rect 部分重叠；完全嵌套的容器 rect 除外）。

**Why:** 用户发现 T2.14 图 3 的"仿真验证：同时跑"文字与上方文本框边界仅约 2px，紧贴边界视觉质量差。已固化为 `tools/audit_svg_layout.py` 的 R6（边界间距 ≥8px，含 class="free" 框外文字）与 R7（rect 部分重叠禁止）规则，并更新 3gpp/CLAUDE.md 第 4 条 SVG 强制视觉验证步骤。

**How to apply:** 所有手绘/生成 SVG 必须通过 `python3 tools/audit_svg_layout.py <svg>` 的 R1-R7 全部检查；Y 坐标扫描之外必须做边界间距与重叠检查。存量 SVG（T2.x/T6-9/T14/T15 等约 60 个文件）曾用旧工具审计，R4 有大量疑似误报（text 结构差异），全库合规修复以逐文件违规分布为准。
