"""Utilities for extracting structured artifacts from 3GPP Word documents."""

from .docx_parser import parse_docx
from .exporter import export_document

__all__ = ["parse_docx", "export_document"]
