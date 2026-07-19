#!/usr/bin/env python3
"""Audit project-wide PNG inventory consistency for L1/L2/L3 lessons."""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DOC_ROOTS = (Path("docs/L1"), Path("docs/L2"), Path("docs/L3"))
ASSET_ROOTS = (Path("docs/L1/assets"), Path("docs/L2/assets"), Path("docs/L3/assets"))
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
    return Path(posixpath.normpath(path.as_posix()))


def rel_to_root(path: Path, root: Path) -> Path:
    return normalized(path.resolve().relative_to(root.resolve()))


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for doc_root in DOC_ROOTS:
        base = root / doc_root
        if base.exists():
            files.extend(sorted(base.glob("T*.md")))
    return files


def resolve_image_ref(root: Path, lesson: Path, raw: str) -> Path:
    target = (lesson.parent / raw).resolve()
    return rel_to_root(target, root)


def collect_markdown_references(root: Path) -> list[ImageReference]:
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
    assets: set[Path] = set()
    for asset_root in ASSET_ROOTS:
        base = root / asset_root
        if base.exists():
            assets.update(rel_to_root(path, root) for path in sorted(base.glob("*.png")))
    return assets


def resolve_inventory_asset(text_path: str) -> Path | None:
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
    lesson_path = Path(lesson)
    if image.startswith("../"):
        return normalized((lesson_path.parent / image))
    if image.startswith("assets/"):
        return normalized(lesson_path.parent / image)
    if image.startswith("docs/"):
        return normalized(Path(image))
    return normalized(lesson_path.parent / image)


def parse_migration(root: Path) -> list[MigrationRow]:
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
