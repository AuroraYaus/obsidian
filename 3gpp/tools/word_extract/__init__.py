"""
@file __init__.py
@brief word_extract 包 — 3GPP Word 文档结构化抽取
@date 2025

提供 DOCX 解析引擎，用于从 3GPP 协议 Word 文档（.docx）中提取：
- 段落文本（含样式、标题识别）
- 表格（OMML/WordprocessingML，含合并单元格）
- 数学公式（OMML Math）
- 内嵌媒体（图片等）

核心流程：parse_docx() 解析 → export_document() 导出为结构化目录。

@see docx_parser.py — 解析器实现
@see exporter.py — 导出器实现
"""

from .docx_parser import parse_docx
from .exporter import export_document

__all__ = ["parse_docx", "export_document"]
