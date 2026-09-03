---
name: docx-wmf-formula-extraction
description: 3gpp 协议 docx 内联公式为 MathType WMF 图片时（processed 抽取丢公式）的恢复方法：rId→word/media 映射 + LibreOffice SVG glyph 重组 + OCR 互证
metadata: 
  node_type: memory
  type: project
  originSessionId: 4d076c5a-1561-447c-ab15-aee0f2c8c404
  modified: 2026-08-17T14:08:17.258Z
---

3GPP docx 的公式以 MathType WMF 图片（`word/media/image*.wmf`）而非 OMML 嵌入，processed 抽取流水线可能整节丢公式（2026-08-17 在 TS 38.213 §11.2 发现，§11.2A 却完整）。恢复方法：(1) zipfile+ElementTree 解析 document.xml，段落内 0 个 oMath + N 个 pic/blip = 公式是图片；(2) 段落 `r:embed` 经 document.xml.rels 映射到 word/media 文件；(3) `libreoffice --headless --convert-to svg` 转 WMF，提取 tspan glyph 重组公式（Symbol 码位：f0e9=⌈ f0f9=⌉ f0eb=⌊ f0fb=⌋ f02d=− f02b=+ f0d7=× f06d=μ；tspan 文档序=视觉左→右序）；(4) ImageMagick 渲染 + tesseract 互证。

**Why:** 协议公式必须逐位核验才能入知识库正文（合规 Rule 精读优先），processed 丢失时不能凭记忆拼公式。

**How to apply:** 协议锚点表注明"公式原文为 WMF 图片，已从 specs/<版本>.docx 抽取核验"。权威副本在 [[lesson-docx-wmf-formula-extraction]]（3gpp/docs/audits/lessons/）。本次应用实例：[[Preemption_Indication_抢占指示]] 笔记的 38.213 §11.2 公式（N_INT/B_INT 记号、set0/set1 分组式）。
