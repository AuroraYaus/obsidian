#!/usr/bin/env python3
"""Dynamically audit PIL figure scripts for overlapping text bboxes.

The audit executes render scripts with Image.save patched to a no-op, records
PIL text bounding boxes per image, and reports text-to-text overlaps. This
catches layout bugs that static checks miss, such as wrapped text that fits
horizontally but exceeds its fixed vertical box.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import runpy
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw


DEFAULT_PATHS = [Path("tools/figures")]
DEFAULT_MIN_AREA = 80.0


@dataclass(frozen=True)
class TextRecord:
    image: object
    text: str
    bbox: tuple[float, float, float, float]


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.path}:{self.line}: {self.rule}: {self.message}"


def iter_python_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_dir():
            files.extend(sorted(path.glob("render_*.py")))
        elif path.suffix == ".py":
            files.append(path)
    return sorted(dict.fromkeys(files))


def overlap_area(
    a: tuple[float, float, float, float],
    b: tuple[float, float, float, float],
) -> tuple[float, tuple[float, float, float, float] | None]:
    x0 = max(a[0], b[0])
    y0 = max(a[1], b[1])
    x1 = min(a[2], b[2])
    y1 = min(a[3], b[3])
    if x1 <= x0 or y1 <= y0:
        return 0.0, None
    return (x1 - x0) * (y1 - y0), (x0, y0, x1, y1)


def is_meaningful_text(text: str) -> bool:
    return len(text.strip()) > 1


def audit_script(path: Path, min_area: float = DEFAULT_MIN_AREA) -> list[Finding]:
    records: list[TextRecord] = []
    original_save = Image.Image.save
    original_text = ImageDraw.ImageDraw.text

    def patched_save(self: Image.Image, fp: Any, *args: Any, **kwargs: Any) -> None:
        return None

    def patched_text(self: ImageDraw.ImageDraw, xy: Any, text: Any, *args: Any, **kwargs: Any) -> Any:
        font = kwargs.get("font")
        anchor = kwargs.get("anchor")
        rendered = str(text)
        if rendered.strip():
            try:
                bbox = self.textbbox(xy, rendered, font=font, anchor=anchor)
                image = getattr(self, "_image", None)
                records.append(
                    TextRecord(
                        image,
                        rendered,
                        (float(bbox[0]), float(bbox[1]), float(bbox[2]), float(bbox[3])),
                    )
                )
            except Exception:
                pass
        return original_text(self, xy, text, *args, **kwargs)

    old_argv = sys.argv[:]
    old_path = sys.path[:]
    Image.Image.save = patched_save
    ImageDraw.ImageDraw.text = patched_text
    sys.argv = [str(path)]
    try:
        project_root = Path.cwd().resolve()
        script_dir = path.resolve().parent
        sys.path[:0] = [str(project_root), str(script_dir)]
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            runpy.run_path(str(path), run_name="__main__")
    except SystemExit as exc:
        if exc.code not in (0, None):
            return [Finding(path, 1, "script_failed", f"SystemExit({exc.code})")]
    except Exception as exc:
        return [Finding(path, 1, "script_failed", f"{type(exc).__name__}: {exc}")]
    finally:
        sys.argv = old_argv
        sys.path = old_path
        Image.Image.save = original_save
        ImageDraw.ImageDraw.text = original_text

    by_image: dict[int, list[TextRecord]] = {}
    for record in records:
        by_image.setdefault(id(record.image), []).append(record)

    findings: list[Finding] = []
    for image_records in by_image.values():
        for idx, first in enumerate(image_records):
            for second in image_records[idx + 1 :]:
                if first.text == second.text and first.bbox == second.bbox:
                    continue
                if not (is_meaningful_text(first.text) and is_meaningful_text(second.text)):
                    continue
                area, intersection = overlap_area(first.bbox, second.bbox)
                if area < min_area:
                    continue
                findings.append(
                    Finding(
                        path,
                        1,
                        "text_bbox_overlap",
                        (
                            f"area={area:.1f} intersection={intersection}; "
                            f"{first.text[:60]!r} overlaps {second.text[:60]!r}"
                        ),
                    )
                )
    return findings


def audit_scripts(paths: list[Path], min_area: float = DEFAULT_MIN_AREA) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_python_files(paths):
        findings.extend(audit_script(path, min_area=min_area))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_PATHS)
    parser.add_argument("--min-area", type=float, default=DEFAULT_MIN_AREA)
    args = parser.parse_args(argv)

    findings = audit_scripts(args.paths, min_area=args.min_area)
    for finding in findings:
        print(finding.format())
    if findings:
        print(f"FIGURE_TEXT_OVERLAP_DYNAMIC_AUDIT_FAIL findings={len(findings)}", file=sys.stderr)
        return 1
    print("FIGURE_TEXT_OVERLAP_DYNAMIC_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
