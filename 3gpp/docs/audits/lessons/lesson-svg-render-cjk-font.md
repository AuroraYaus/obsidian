# svg-render-cjk-font

> SVG 的 PNG 目检必须用 rsvg-convert；ImageMagick 内置 MSVG 渲染器不渲染中文字形，会让"目检通过"变成假信号

2026-11-10 制作首批概念笔记配图时实测：`magick`（ImageMagick 3.x 的 `convert`）渲染含中文的 SVG 时，**所有中文字形静默丢失**，只剩拉丁字母与数字；布局、网格、色块完全正常，因此单看"有没有重叠"会得出通过结论，而实际在 Obsidian 里是另一副样子。

## 根因

`convert -list format` 显示 SVG 由 `MSVG`（ImageMagick 自己的 SVG 内部渲染器）处理，而非 librsvg。MSVG 不做 fontconfig 字体回退，`font-family="Noto Sans CJK SC, …"` 里的中文直接缺字形输出空。系统装有 94 个中文字体（Noto Sans CJK 等），但 MSVG 不会去用。

## How to apply

1. **渲染命令固定为** `rsvg-convert -w <宽> -h <高> -o <png> <svg>`（依赖 `librsvg2-bin`，本机 2026-11-10 已安装）。
2. **目检判据加一条**：先确认图上中文可见，再判断重叠与对齐。中文全空即为渲染器问题，不是 SVG 问题，换渲染器重来，不要改图。
3. **审计工具与渲染器分离**：`tools/audit_svg_layout.py` 用 Noto Sans CJK 字体度量，与 rsvg-convert 的 pango 渲染一致；与 MSVG 不一致，故 MSVG 的产物不能作为验证依据。
4. SVG 里写明 `font-family="Noto Sans CJK SC, DejaVu Sans, sans-serif"`，让度量和渲染取同一字体栈首项。

## 影响面

任何以"PNG 预览确认无交叠"为验收步骤的 SVG 工作（CLAUDE.md 第 4 条第三步）都适用。此前若有图用 `convert` 出过预览，其目检结论需要复核一遍——尤其图内只有少量中文时，缺失不易察觉。

相关：[[lesson-svg-render-verify-before-commit]]（生成后强制视觉验证）、[[lesson-svg-audit-blind-spots]]（工具盲区系列）
