---
name: svg-render-cjk-font
description: SVG 的 PNG 目检必须用 rsvg-convert；ImageMagick 内置 MSVG 渲染器不渲染中文字形，会产生「无重叠但无文字」的假通过
metadata:
  type: feedback
---

2026-11-10 制作概念笔记配图时实测：`magick`/`convert` 渲染含中文的 SVG 时中文字形全部静默丢失，布局与色块正常，因此只看"有无重叠"会误判通过。

**根因**：`convert -list format` 显示 SVG 由 `MSVG`（ImageMagick 自研渲染器）处理，不做 fontconfig 回退；系统虽有 94 个中文字体也不使用。

**How to apply**：
1. 渲染固定用 `rsvg-convert -w W -h H -o x.png x.svg`（需 `librsvg2-bin`）。
2. 目检第一步是确认中文可见；中文全空即渲染器问题，换渲染器而不是改图。
3. `tools/audit_svg_layout.py` 用 Noto Sans CJK 度量，与 rsvg-convert 一致、与 MSVG 不一致。
4. SVG 内写 `font-family="Noto Sans CJK SC, DejaVu Sans, sans-serif"`。
