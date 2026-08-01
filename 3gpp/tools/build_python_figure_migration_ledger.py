#!/usr/bin/env python3
"""
@file build_python_figure_migration_ledger.py
@brief 构建 Python 图片到正文等价内容迁移总账，统一追踪每张 PNG 图片是否已有 Mermaid 等价图、
       Markdown 等价表或正文等价说明，防止讲义中只存像素信息而无结构化文本可检索。
@date 2026-07-22
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.audit_python_figure_body_equivalents import RETAINED_ASSET_RE, has_marker_near


OUT = Path("docs/audits/python_figure_to_body_content_migration.md")
DOC_ROOTS = [Path("docs/L1"), Path("docs/L2"), Path("docs/L3")]
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+\.png)\)")
SCRIPT_RE = re.compile(r"tools/figures/[\w./-]+\.py")
EVIDENCE_STATUS_TOKENS = ("evidence_only", "compatibility_retained", "not_current_body_reference", "not_applicable")


def equivalent_type(image: str, lesson_text: str) -> str:
    """
    @brief 根据图片文件名和讲义正文内容推断该图片应使用哪种等价表示形式，
           避免因信息丢失而无从判断是画流程图还是列表格。
    @param image 图片文件名，通过命名关键字判断类型倾向。
    @param lesson_text 图片所在讲义的全文，用于正文关键词二次兜底判断。
    @return 等价类型标签，三选一：Mermaid 等价图、Markdown 等价表、图片内容正文等价。
    """
    lower = image.lower()
    if any(token in lower for token in ["table", "sequence", "compare", "comparison", "requirements", "report"]):
        return "Markdown 等价表"
    if any(token in lower for token in ["flow", "architecture", "chain", "decoder", "rtl", "testbench", "synthesis", "timing", "map"]):
        return "Mermaid 等价图"
    if "table" in lesson_text.lower():
        return "Markdown 等价表"
    return "图片内容正文等价"


def existing_evidence_rows() -> list[tuple[str, str, str, str, str, str]]:
    """
    @brief 从已有总账文件中读取标记为"证据保留"（evidence_only/compatibility_retained 等）的行，
           避免增量构建时丢弃已审核通过的既有记录。
    @return 六元组列表：(Lesson, Image, Scripts, EquivalentType, Status, BodyLocation)，
           均来自总账 Markdown 表格的单元格文本。
    @note 仅解析以 | ` 开头的表格行，非表格行和格式不完整的行被静默跳过。
    """
    if not OUT.exists():
        return []
    rows: list[tuple[str, str, str, str, str, str]] = []
    for line in OUT.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        status = cells[4]
        if any(token in status for token in EVIDENCE_STATUS_TOKENS):
            rows.append(tuple(cells[:6]))  # type: ignore[arg-type]
    return rows


def main() -> int:
    """
    @brief 扫描所有讲义中的 PNG 图片引用，结合附近 40 行内是否存在等价标记，
           生成一张完整的图片到正文内容迁移总账表格。
    @return 0 表示生成成功（或干运行完毕）；非 0 表示内部逻辑异常（当前实现始终返回 0）。
    @note 扫描 docs/L1、docs/L2、docs/L3 下所有 .md 文件；
          既存证据行通过 existing_evidence_rows() 保留合并，防止重复审核。
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Build Python figure to body content migration ledger"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print ledger summary without writing output file",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=OUT,
        help=f"output ledger path (default: {OUT})",
    )
    args = parser.parse_args()

    rows = []
    for root in DOC_ROOTS:
        for md in sorted(root.glob("*.md")):
            text = md.read_text(encoding="utf-8")
            scripts = ", ".join(sorted(set(SCRIPT_RE.findall(text)))) or "-"
            lines = text.splitlines()
            for idx, line in enumerate(lines):
                matches = list(IMAGE_RE.finditer(line)) + list(RETAINED_ASSET_RE.finditer(line))
                for match in matches:
                    image = match.group(1)
                    status = "body_equivalent_only; asset_retained" if has_marker_near(lines, idx, 40) else "missing"
                    body_location = f"{md}:{idx + 1}" if status == "present" else "-"
                    if status != "missing":
                        body_location = f"{md}:{idx + 1}"
                    rows.append((md, image, scripts, equivalent_type(image, text), status, body_location))

    body_assets = {(str(md), image) for md, image, *_ in rows}
    for lesson, image, scripts, eq_type, status, body_location in existing_evidence_rows():
        lesson_value = lesson.strip("`")
        image_value = image.strip("`")
        if (lesson_value, image_value) not in body_assets:
            rows.append((Path(lesson_value), image_value, scripts.strip("`"), eq_type, status, body_location.strip("`")))

    missing = sum(1 for row in rows if row[4] == "missing")
    retained = sum(1 for row in rows if "asset_retained" in row[4])
    out = [
        "# Python Figure to Body Content Migration",
        "",
        "审查时间：2026-06-23",
        "",
        f"总计：{len(rows)} 个正文保留资产记录；`body_equivalent_only_asset_retained={retained}`，`missing={missing}`。",
        "",
        "状态规则：`body_equivalent_only; asset_retained` 表示正文不再嵌入 PNG，原图片文件保留为资产记录，且附近 40 行内已有 `Mermaid 等价图`、`Markdown 等价表` 或 `图片内容正文等价` 标记；`missing` 表示仍需补正文等价块。",
        "",
        "| Lesson | Image | Script | Equivalent type | Status | Body location |",
        "|:---|:---|:---|:---|:---|:---|",
    ]
    for md, image, scripts, eq_type, status, body_location in rows:
        out.append(f"| `{md}` | `{image}` | `{scripts}` | {eq_type} | {status} | `{body_location}` |")

    if args.dry_run:
        print(f"[DRY-RUN] Would write ledger to {args.output}: {len(rows)} rows, missing={missing}")
    else:
        args.output.write_text("\n".join(out) + "\n", encoding="utf-8")
        print(f"WROTE {args.output} rows={len(rows)} missing={missing}")
    return 0


# @brief 构建 Python 图片到正文等价内容迁移总账。
# @usage python tools/build_python_figure_migration_ledger.py [--dry-run] [--output PATH]
# @args --dry-run  仅打印摘要，不写入输出文件。
# @args --output   指定输出文件路径，默认 docs/audits/python_figure_to_body_content_migration.md。
# @exit_code 0 正常完成；非 0 表示内部异常。
if __name__ == "__main__":
    raise SystemExit(main())
