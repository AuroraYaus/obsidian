---
name: svg-css-class-font-metric-lessons
description: SVG 审计工具不解析 CSS class 字体的漏检教训——T10.9 标题按 12px 低估度量超边 42px 未被发现；固化 CSS 解析 + 8% 字体回退安全系数
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 30cc3013-8452-437a-8c46-a0e217366592
  modified: 2026-08-04T15:08:06.348Z
---

2026-08-04 用户发现 T10.9_interleaving_error_scatter.svg 右面板标题"三角交织后：..."超出面板右缘 33px，而审计工具输出 ALL_PASS。

**根因（2 层）**：
1. **工具不解析 `<style>` 的 CSS class 规则**：该标题 `class="label"` 的 `font-size: 14px` 定义在 `<style>` 中，元素上没有 font-size 属性。工具只读元素属性/继承，按默认 12px 度量——14px 文字被低估 17%（实测 Noto Bold 420px 宽 vs 工具按 12px 算 249px），右缘 942 被算成 771 → 判定"在面板内"→ PASS。**所有用 class 样式的图（.title/.label/.small/.mono）都被系统性低估度量**。
2. **字体回退差异**：工具按 Noto Sans CJK 度量；Obsidian 渲染可能 fallback 到更宽字体（DejaVu Bold 实测 410px），真实渲染比工具度量更宽。

**How to apply（固化规则）**：
1. **工具必须解析 CSS class**：audit_svg_layout.py 已升级——解析 `<style>` 的 `.class { font-size; font-weight }` 规则，text 的 class 匹配样式表（属性/继承 > CSS > 默认 12px）
2. **字体回退安全系数**：text_metrics 宽度 +8%（fallback 字体通常更宽）；宿主内边距判定随之收紧
3. **文字排版规则**：长文字（序列、数组、说明句）避免单行排满宿主——预留 ≥10px 右缘余量；工具升级后 40 个存量 FAIL（全部目录）暴露并已批量修复（2026-08-04）
4. **验证链**：SVG 修改 → audit_svg_layout.py ALL_PASS → cairosvg 渲染 → （可用时）肉眼目检

**工具状态**：audit_svg_layout.py 现支持 CSS class 解析（含 px 单位）、+8% 宽度安全系数；R1-R9 规则见文件头。

相关：[[svg-audit-blind-spots]]（同类"工具盲区未识别就采信 PASS"教训）
