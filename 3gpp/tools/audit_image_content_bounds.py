#!/usr/bin/env python3
"""Audit rendered image content bounds against excessive blank margins."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops


DEFAULT_PATHS = [Path("docs/L1/assets"), Path("docs/L2/assets"), Path("docs/L3/assets")]
DEFAULT_MAX_BOTTOM_PIXELS = 160
DEFAULT_MAX_BOTTOM_RATIO = 0.10


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.path}:{self.line}: {self.rule}: {self.message}"


def iter_image_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_dir():
            files.extend(sorted(path.glob("*.png")))
        elif path.suffix.lower() in {".png", ".jpg", ".jpeg"}:
            files.append(path)
    return sorted(dict.fromkeys(files))


def content_bbox(path: Path) -> tuple[int, int, int, int] | None:
    with Image.open(path) as img:
        rgb = img.convert("RGB")
        background = Image.new("RGB", rgb.size, rgb.getpixel((0, 0)))
        return ImageChops.difference(rgb, background).getbbox()


def audit_images(
    paths: list[Path],
    max_bottom_pixels: int = DEFAULT_MAX_BOTTOM_PIXELS,
    max_bottom_ratio: float = DEFAULT_MAX_BOTTOM_RATIO,
) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_image_files(paths):
        try:
            with Image.open(path) as img:
                width, height = img.size
            bbox = content_bbox(path)
        except Exception as exc:
            findings.append(Finding(path, 1, "invalid_image", str(exc)))
            continue
        if not bbox:
            findings.append(Finding(path, 1, "blank_image", "image has no non-background content"))
            continue
        bottom_blank = height - bbox[3]
        bottom_ratio = bottom_blank / height
        if bottom_blank > max_bottom_pixels and bottom_ratio > max_bottom_ratio:
            findings.append(
                Finding(
                    path,
                    1,
                    "excessive_bottom_blank",
                    (
                        f"bottom_blank={bottom_blank}px ratio={bottom_ratio:.2%} "
                        f"size={width}x{height} content_bbox={bbox}"
                    ),
                )
            )
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_PATHS)
    parser.add_argument("--max-bottom-pixels", type=int, default=DEFAULT_MAX_BOTTOM_PIXELS)
    parser.add_argument("--max-bottom-ratio", type=float, default=DEFAULT_MAX_BOTTOM_RATIO)
    args = parser.parse_args(argv)

    findings = audit_images(
        args.paths,
        max_bottom_pixels=args.max_bottom_pixels,
        max_bottom_ratio=args.max_bottom_ratio,
    )
    for finding in findings:
        print(finding.format())
    if findings:
        print(f"IMAGE_CONTENT_BOUNDS_AUDIT_FAIL findings={len(findings)}", file=sys.stderr)
        return 1
    print("IMAGE_CONTENT_BOUNDS_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
