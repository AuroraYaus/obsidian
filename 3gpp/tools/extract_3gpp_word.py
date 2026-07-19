#!/usr/bin/env python3
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
    return [
        path
        for path in source.iterdir()
        if path.is_file() and path.suffix.lower() in {".docx", ".doc"}
    ]


def _process_source(path: Path, output: Path) -> dict:
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
    match = re.match(r"([0-9]{2})([0-9]{3})-", name)
    if not match:
        return "TS unknown"
    return f"TS {match.group(1)}.{match.group(2)}"


def _status_counts(rows: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    return counts


def _write_report(manifest: dict, path: Path) -> None:
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
