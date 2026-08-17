---
name: lesson-docx-wmf-formula-extraction
description: 协议 docx 内联公式为 WMF 图片（MathType）时的抽取核验方法——processed 抽取丢失公式时从 specs/*.docx 的 word/media 恢复
metadata:
  type: feedback
---

# docx WMF 公式抽取核验（processed 抽取丢失内联公式的恢复手段）

**根因**：2026-08-17 写 Preemption_Indication 概念笔记时发现，本地 `3GPP_Rel19/processed/TS_38.213_38213-j30/` 的 §11.2（Interrupted transmission indication）正文中全部内联公式为空（"includes  PRBs"、"first  symbol groups"），而相邻 §11.2A 公式完整——抽取流水线对不同章节的处理不一致，公式丢失后正文语义残缺。核对 `specs/38213-j30.docx` 原文确认：3GPP docx 的公式以 MathType WMF 图片（`word/media/image*.wmf`）而非 OMML（`<m:oMath>`）嵌入，§11.2 的公式全部是 WMF 图片，抽取流水线未对其 OCR，导致空位。

**How to apply**：
1. 判断公式形态：用 zipfile + ElementTree 解析 `word/document.xml`，统计目标段落内 `oMath` 出现次数与 `pic/blip` 图片引用数——0 个 oMath + N 个图片 = 公式是图片。
2. 定位图片：从段落的 `r:embed`（officeDocument/2006/relationships 命名空间）经 `word/_rels/document.xml.rels` 映射到 `word/media/image*.wmf`。
3. 恢复公式文本：`libreoffice --headless --convert-to svg` 把 WMF 转 SVG（保留 MathType 文本 glyph），提取 `<tspan>` 序列；Symbol 字体码位需映射（f0e9=⌈、f0f9=⌉、f0eb=⌊、f0fb=⌋、f02d=−、f02b=+、f0d7=×、f06d=μ）。tspan 文档序即视觉左→右序（本案例已验证），可逐段重组公式。
4. 交叉验证：ImageMagick 高 DPI 渲染 + tesseract OCR 作为第二通道，与 SVG glyph 重组结果互证。
5. 写回证据：概念笔记「协议锚点」表注明"公式原文为 WMF 图片，已从 `specs/<版本>.docx` 抽取核验"，保证证据链可溯源。

**固化**：本 lesson 登记 `项目规则与记忆索引.md` 第七节；核验结果已写入 `docs/concepts/Preemption_Indication_抢占指示.md` 协议锚点表。本方法为一次性技术手段（非工具规则），不入 audit_* 工具；后续遇到 processed 抽取公式丢失时按本方法恢复，不再从记忆拼公式。
