#!/usr/bin/env python3
"""@file audit_project_image_inventory.py
@brief 审计项目级 PNG 图片资产的一致性——确保 Markdown 引用、磁盘文件、
       资产清单（inventory ledger）和迁移台账（migration ledger）四者同步。
@date 2026-07-22

本工具回答四个问题：
1. 讲义中引用的 PNG 是否真的存在于 assets/ 目录？
2. 磁盘上的 PNG 是否在资产清单中有备案行？
3. 磁盘上的 PNG 是否在迁移台账中有分类状态？
4. 迁移台账中的条目是否对应真实存在的资产？

缺失行、未分类状态、孤儿引用均视为审计失败，因为知识库资产需要可追溯。
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DOC_ROOTS = (Path("docs/L1_基础"), Path("docs/L2_协议算法"), Path("docs/L3_工程实现"))
ASSET_ROOTS = (Path("docs/L1_基础/assets"), Path("docs/L2_协议算法/assets"), Path("docs/L3_工程实现/assets"))
INVENTORY_PATH = Path("docs/audits/image_asset_inventory.md")
MIGRATION_PATH = Path("docs/audits/python_figure_to_body_content_migration.md")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+\.png)\)")
RETAINED_ASSET_RE = re.compile(r"原图片资产：`([^`]+\.png)`")
ASSET_PATH_RE = re.compile(r"`((?:\.\./)?(?:docs/)?L[123]/assets/[^`]+\.png|assets/[^`]+\.png)`")
CLASSIFIED_STATUS_TOKENS = (
    "present_quality_pass",
    "body_referenced",
    "body_text_represented",
    "asset_retained",
    "evidence_only",
    "compatibility_retained",
    "not_current_body_reference",
    "not_applicable",
)


@dataclass(frozen=True)
class ImageReference:
    lesson: Path
    line: int
    raw: str
    resolved: Path


@dataclass(frozen=True)
class MigrationRow:
    lesson: str
    image: str
    status: str
    resolved: Path


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.path}:{self.line}: {self.rule}: {self.message}"


def normalized(path: Path) -> Path:
    """@brief  将路径规范化为 POSIX 风格的相对表示，消除 `.` 和 `..`。
    @param  path  任意 Path 对象。
    @return       规范化后的 Path。"""
    return Path(posixpath.normpath(path.as_posix()))


def rel_to_root(path: Path, root: Path) -> Path:
    """@brief  将绝对路径转换为相对于项目根目录的规范化路径。
    @param  path  绝对路径。
    @param  root  项目根目录的绝对路径。
    @return       相对于 root 的规范化路径。"""
    return normalized(path.resolve().relative_to(root.resolve()))


def iter_markdown_files(root: Path) -> list[Path]:
    """@brief  收集 L1/L2/L3 目录下所有以 T 开头的讲义 Markdown 文件。
    @param  root  项目根目录。
    @return       按字典序排列的讲义文件路径列表。"""
    files: list[Path] = []
    for doc_root in DOC_ROOTS:
        base = root / doc_root
        if base.exists():
            files.extend(sorted(base.glob("T*.md")))
    return files


def resolve_image_ref(root: Path, lesson: Path, raw: str) -> Path:
    """@brief  将讲义中的图片引用文本解析为相对于项目根目录的规范路径。
    @param  root    项目根目录。
    @param  lesson  讲义文件相对于 root 的路径。
    @param  raw     图片引用中 `()` 内的原始路径字符串。
    @return         解析后相对于 root 的规范化路径。"""
    target = (lesson.parent / raw).resolve()
    return rel_to_root(target, root)


def collect_markdown_references(root: Path) -> list[ImageReference]:
    """@brief  从所有讲义中收集对 PNG 图片的引用（包括标准 Markdown 图片语法
             和迁移台账中的"原图片资产"标记）。
    @param  root  项目根目录。
    @return       按文件排序的图片引用列表，每条记录含行号和解析后的路径。
    @note   同时扫描 `![]()` 语法和 `原图片资产：` 文本标记，确保覆盖所有引用源。"""
    refs: list[ImageReference] = []
    for lesson in iter_markdown_files(root):
        for idx, line in enumerate(lesson.read_text(encoding="utf-8").splitlines(), start=1):
            for match in IMAGE_RE.finditer(line):
                raw = match.group(1)
                refs.append(
                    ImageReference(
                        lesson=rel_to_root(lesson, root),
                        line=idx,
                        raw=raw,
                        resolved=resolve_image_ref(root, lesson, raw),
                    )
                )
            for match in RETAINED_ASSET_RE.finditer(line):
                raw = match.group(1)
                refs.append(
                    ImageReference(
                        lesson=rel_to_root(lesson, root),
                        line=idx,
                        raw=raw,
                        resolved=resolve_image_ref(root, lesson, raw),
                    )
                )
    return refs


def collect_assets(root: Path) -> set[Path]:
    """@brief  收集 L1/L2/L3 的 assets/ 目录下所有物理存在的 PNG 文件。
    @param  root  项目根目录。
    @return       规范化路径集合，每个元素相对于 root。"""
    assets: set[Path] = set()
    for asset_root in ASSET_ROOTS:
        base = root / asset_root
        if base.exists():
            assets.update(rel_to_root(path, root) for path in sorted(base.glob("*.png")))
    return assets


def resolve_inventory_asset(text_path: str) -> Path | None:
    """@brief  将资产清单中反引号包裹的路径文本解析为规范化 Path。
    @param  text_path  清单中提取的原始路径字符串。
    @return            规范化的 Path；`assets/` 裸路径（无 L* 前缀）返回 None。
    @note   只接受 `docs/L*/assets/*.png` 或 `L*/assets/*.png` 格式。"""
    if text_path.startswith("../"):
        text_path = text_path[3:]
    if text_path.startswith("assets/"):
        return None
    if text_path.startswith("docs/"):
        return normalized(Path(text_path))
    if text_path.startswith("L"):
        return normalized(Path("docs") / text_path)
    return None


def parse_inventory(root: Path) -> set[Path]:
    """@brief  解析资产清单文件，提取所有已备案的 PNG 资产路径。
    @param  root  项目根目录。
    @return       清单中出现的规范化 PNG 资产路径集合。"""
    path = root / INVENTORY_PATH
    if not path.exists():
        return set()
    assets: set[Path] = set()
    for match in ASSET_PATH_RE.finditer(path.read_text(encoding="utf-8")):
        asset = resolve_inventory_asset(match.group(1))
        if asset is not None:
            assets.add(asset)
    return assets


def resolve_migration_asset(lesson: str, image: str) -> Path:
    """@brief  将迁移台账行中的讲义路径和图片路径组合解析为规范化资产路径。
    @param  lesson  迁移行中的讲义文件名（如 `T1.1-something.md`）。
    @param  image   迁移行中的图片路径字符串。
    @return         相对于项目根的规范化资产路径。"""
    lesson_path = Path(lesson)
    if image.startswith("../"):
        return normalized((lesson_path.parent / image))
    if image.startswith("assets/"):
        return normalized(lesson_path.parent / image)
    if image.startswith("docs/"):
        return normalized(Path(image))
    return normalized(lesson_path.parent / image)


def parse_migration(root: Path) -> list[MigrationRow]:
    """@brief  解析 Python 图片到正文内容迁移台账，提取所有已记录的行。
    @param  root  项目根目录。
    @return       解析后的迁移行列表，每行含讲义、图片、状态和解析路径。
    @note   只解析表格式行（以 `| ` 开头），按迁移台账的列结构提取字段。"""
    path = root / MIGRATION_PATH
    if not path.exists():
        return []
    rows: list[MigrationRow] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        lesson = cells[0].strip("`")
        image = cells[1].strip("`")
        status = cells[4]
        if not lesson.endswith(".md") or not image.endswith(".png"):
            continue
        rows.append(MigrationRow(lesson, image, status.strip(), resolve_migration_asset(lesson, image)))
    return rows


def audit_project(root: Path = Path(".")) -> list[Finding]:
    """@brief  执行完整的项目级图片资产一致性审计——
             交叉校验 Markdown 引用、磁盘文件、资产清单和迁移台账四源数据。
    @param  root  项目根目录（默认当前目录）。
    @return       所有不一致 Findings 的列表；空列表表示四源数据完全一致。
    @note   五项检查：缺失文件、缺失清单行、缺失迁移行、资产无清单备案、资产无分类状态、
             迁移台账中的孤儿资产、有资产但无分类状态。"""
    root = root.resolve()
    refs = collect_markdown_references(root)
    assets = collect_assets(root)
    inventory_assets = parse_inventory(root)
    migration_rows = parse_migration(root)
    migration_assets = {row.resolved for row in migration_rows}
    body_refs = {ref.resolved for ref in refs}
    classified_assets = {
        row.resolved
        for row in migration_rows
        if any(token in row.status for token in CLASSIFIED_STATUS_TOKENS)
    }

    findings: list[Finding] = []
    for ref in refs:
        if ref.resolved not in assets:
            findings.append(
                Finding(ref.lesson, ref.line, "missing_asset_file", f"{ref.raw} resolves to missing {ref.resolved}")
            )
        if ref.resolved not in inventory_assets:
            findings.append(
                Finding(ref.lesson, ref.line, "missing_inventory_row", f"{ref.resolved} is referenced but absent from {INVENTORY_PATH}")
            )
        if ref.resolved not in migration_assets:
            findings.append(
                Finding(ref.lesson, ref.line, "missing_migration_row", f"{ref.resolved} is referenced but absent from {MIGRATION_PATH}")
            )

    for asset in sorted(assets):
        if asset not in inventory_assets:
            findings.append(
                Finding(INVENTORY_PATH, 1, "asset_not_in_inventory", f"{asset} exists under docs/L*/assets but has no inventory row")
            )
        if asset not in classified_assets:
            findings.append(
                Finding(
                    MIGRATION_PATH,
                    1,
                    "unclassified_unreferenced_asset",
                    f"{asset} exists under docs/L*/assets but has no classified migration status",
                )
            )

    for row in migration_rows:
        if row.resolved not in body_refs and row.resolved not in assets:
            findings.append(
                Finding(MIGRATION_PATH, 1, "migration_asset_missing", f"{row.resolved} is listed in migration ledger but no asset exists")
            )
        if row.resolved in assets and row.resolved not in classified_assets:
            findings.append(
                Finding(
                    MIGRATION_PATH,
                    1,
                    "migration_status_ambiguous",
                    f"{row.resolved} is listed in migration ledger but status does not classify body/evidence retention",
                )
            )

    return findings


def main(argv: list[str] | None = None) -> int:
    """@brief    脚本入口：审计项目级 PNG 资产一致性。
    @param    argv  命令行参数列表（sys.argv）。
    @usage    python audit_project_image_inventory.py [--root <dir>]
    @args     --root  项目根目录路径（默认当前目录）。
    @exit_code        0 = 四源数据一致；1 = 发现不一致问题。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args(argv)

    findings = audit_project(args.root)
    for finding in findings:
        print(finding.format())
    if findings:
        print(f"PROJECT_IMAGE_INVENTORY_AUDIT_FAIL findings={len(findings)}", file=sys.stderr)
        return 1
    print("PROJECT_IMAGE_INVENTORY_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
