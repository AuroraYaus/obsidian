#!/usr/bin/env python3
"""
@file extract_3gpp_word.py
@brief 从 3GPP Word 文件（.docx/.doc）中批量抽取结构化内容（段落、标题、
       表格、公式、图片），产出自包含的 Markdown 文件和 manifest.json 索引。
       目的：将协议源文档从二进制封闭格式转为可检索、可版本管理、可被讲义引用的纯文本知识资产。
@date 2026-07-22
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.word_extract import export_document, parse_docx


def main() -> int:
    """
    @brief 脚本入口：扫描源目录中的 .docx/.doc 文件，逐个抽取结构化内容，
           生成 manifest.json 汇总索引和 extraction_report.md 可读报告。
    @return 0 表示所有文件抽取成功；1 表示至少一个文件处理失败。
    @note .doc 文件优先尝试 LibreOffice 转换为 .docx 后再解析，转换失败时记录错误并继续。
    """
    parser = argparse.ArgumentParser(description="Extract structured artifacts from 3GPP Word files.")
    parser.add_argument("--source", default="3GPP_Rel19/specs", help="Directory containing .docx/.doc files")
    parser.add_argument("--output", default="3GPP_Rel19/processed", help="Output directory")
    parser.add_argument("--clean", action="store_true", help="Remove output directory before processing")
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)
    if args.clean and output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    rows = []
    for path in sorted(_discover_sources(source)):
        rows.append(_process_source(path, output))

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_dir": str(source),
        "output_dir": str(output),
        "document_count": len(rows),
        "status_counts": _status_counts(rows),
        "documents": rows,
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    _write_report(manifest, output / "extraction_report.md")
    print(json.dumps(manifest["status_counts"], ensure_ascii=False, sort_keys=True))
    return 0 if not any(row["status"] == "failed" for row in rows) else 1


def _discover_sources(source: Path) -> list[Path]:
    """
    @brief 在源目录中收集所有 .docx 和 .doc 文件，
           作为后续批量抽取的输入列表。
    @param source 源目录路径。
    @return 文件路径列表（不含子目录递归，仅一级迭代）。
    """
    return [
        path
        for path in source.iterdir()
        if path.is_file() and path.suffix.lower() in {".docx", ".doc"}
    ]


def _process_source(path: Path, output: Path) -> dict:
    """
    @brief 处理单个源文件：.doc 先转 .docx，解析结构化内容，写出到 output 目录。
           异常时记录错误信息而不中断整个批量流程，保证一个文件失败不影响其余文件。
    @param path 源文件路径。
    @param output 输出目录。
    @return 包含状态、统计信息和错误描述的结果字典。
    @note .doc 转换产生的临时目录在 finally 块中确保清理。
    """
    base_row = {
        "source_name": path.name,
        "source_path": str(path),
        "spec": _spec_from_name(path.name),
        "status": "failed",
        "error": "",
        "converted_from": "",
        "output_dir": "",
        "paragraph_count": 0,
        "heading_candidate_count": 0,
        "table_count": 0,
        "equation_count": 0,
        "media_count": 0,
    }
    temp_dir: Path | None = None
    try:
        docx_path = path
        status = "processed"
        converted_from = ""
        if path.suffix.lower() == ".doc":
            temp_dir = output / ".conversion_tmp" / path.stem
            if temp_dir.exists():
                shutil.rmtree(temp_dir)
            temp_dir.mkdir(parents=True, exist_ok=True)
            docx_path = _convert_doc_to_docx(path, temp_dir)
            status = "converted"
            converted_from = str(path)
        doc = parse_docx(docx_path)
        metadata = export_document(doc, output)
        base_row.update(metadata)
        base_row.update(
            {
                "source_name": path.name,
                "source_path": str(path),
                "status": status,
                "error": "",
                "converted_from": converted_from,
            }
        )
        return base_row
    except Exception as exc:
        base_row["error"] = f"{type(exc).__name__}: {exc}"
        return base_row
    finally:
        if temp_dir is not None:
            shutil.rmtree(temp_dir, ignore_errors=True)


def _convert_doc_to_docx(path: Path, output_dir: Path) -> Path:
    """
    @brief 使用 LibreOffice 无头模式将旧版 .doc 文件转换为 .docx，
           为后续 python-docx 解析提供兼容输入格式。
    @param path 源 .doc 文件路径。
    @param output_dir 转换输出目录。
    @return 转换后的 .docx 文件路径。
    @throws RuntimeError 当 LibreOffice 未安装、转换失败或未产出 .docx 文件时抛出。
    @note 设置 180 秒超时防止大文档卡死；转换后检查输出文件存在性并处理可能的文件名不匹配。
    """
    converter = shutil.which("libreoffice") or shutil.which("soffice")
    if converter is None:
        raise RuntimeError("LibreOffice is not available for .doc conversion")
    result = subprocess.run(
        [
            converter,
            "--headless",
            "--convert-to",
            "docx",
            "--outdir",
            str(output_dir),
            str(path),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=180,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "LibreOffice conversion failed: "
            + (result.stderr.strip() or result.stdout.strip() or f"exit {result.returncode}")
        )
    converted = output_dir / f"{path.stem}.docx"
    if not converted.exists():
        matches = list(output_dir.glob("*.docx"))
        if len(matches) == 1:
            return matches[0]
        raise RuntimeError("LibreOffice did not produce a .docx file")
    return converted


def _spec_from_name(name: str) -> str:
    """
    @brief 从 3GPP 文件名中提取规范号（如 "38212-j30.docx" -> "TS 38.212"），
           用于 manifest 索引中的文档分类标识。
    @param name 文件名（不含路径）。
    @return "TS xx.xxx" 格式的规范号字符串，无法匹配时返回 "TS unknown"。
    @note 匹配模式为两位数字+三位数字后跟连字符（如 "38212-"）。
    """
    match = re.match(r"([0-9]{2})([0-9]{3})-", name)
    if not match:
        return "TS unknown"
    return f"TS {match.group(1)}.{match.group(2)}"


def _status_counts(rows: list[dict]) -> dict[str, int]:
    """
    @brief 按 status 字段聚合统计已处理文档的各类状态数量，
           用于 manifest 和报告中的概览信息。
    @param rows _process_source 产出的结果字典列表。
    @return {status: count} 映射字典。
    """
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    return counts


def _write_report(manifest: dict, path: Path) -> None:
    """
    @brief 将 manifest JSON 数据渲染为可读的 Markdown 抽取报告，
           包含生成时间、源/输出目录、状态统计和逐文档明细表。
    @param manifest 完整的 manifest 字典（含 documents 列表）。
    @param path 报告输出文件路径。
    """
    lines = [
        "# 3GPP Rel-19 Word Extraction Report",
        "",
        f"Generated at: `{manifest['generated_at']}`",
        f"Source directory: `{manifest['source_dir']}`",
        f"Output directory: `{manifest['output_dir']}`",
        f"Document count: `{manifest['document_count']}`",
        "",
        "## Status Counts",
        "",
    ]
    for status, count in sorted(manifest["status_counts"].items()):
        lines.append(f"- `{status}`: {count}")
    lines.extend(
        [
            "",
            "## Documents",
            "",
            "| Source | Status | Paragraphs | Headings | Tables | Equations | Media | Output/Error |",
            "|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in manifest["documents"]:
        output_or_error = row["output_dir"] or row["error"]
        lines.append(
            f"| `{row['source_name']}` | `{row['status']}` | {row['paragraph_count']} | "
            f"{row['heading_candidate_count']} | {row['table_count']} | "
            f"{row['equation_count']} | {row['media_count']} | `{output_or_error}` |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
