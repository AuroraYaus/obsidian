#!/usr/bin/env python3
"""Dynamically audit PIL figure scripts for text padding inside rounded boxes."""

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
DEFAULT_MIN_TAG_PAD_X = 8.0
DEFAULT_MIN_TAG_PAD_Y = 4.0


@dataclass(frozen=True)
class TextRecord:
    image: object
    text: str
    bbox: tuple[float, float, float, float]


@dataclass(frozen=True)
class RoundedBox:
    image: object
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


def normalize_box(xy: Any) -> tuple[float, float, float, float]:
    if len(xy) == 2 and isinstance(xy[0], (tuple, list)):
        x0, y0 = xy[0]
        x1, y1 = xy[1]
    else:
        x0, y0, x1, y1 = xy
    return float(x0), float(y0), float(x1), float(y1)


def contains(outer: tuple[float, float, float, float], inner: tuple[float, float, float, float]) -> bool:
    return outer[0] <= inner[0] and outer[1] <= inner[1] and outer[2] >= inner[2] and outer[3] >= inner[3]


def area(box: tuple[float, float, float, float]) -> float:
    return max(0.0, box[2] - box[0]) * max(0.0, box[3] - box[1])


def padding(
    outer: tuple[float, float, float, float],
    inner: tuple[float, float, float, float],
) -> tuple[float, float, float, float]:
    return inner[0] - outer[0], inner[1] - outer[1], outer[2] - inner[2], outer[3] - inner[3]


def is_tag_box(box: tuple[float, float, float, float]) -> bool:
    width = box[2] - box[0]
    height = box[3] - box[1]
    return height <= 64 and width <= 360


def audit_script(
    path: Path,
    *,
    include_containers: bool = False,
    min_tag_pad_x: float = DEFAULT_MIN_TAG_PAD_X,
    min_tag_pad_y: float = DEFAULT_MIN_TAG_PAD_Y,
) -> list[Finding]:
    text_records: list[TextRecord] = []
    rounded_boxes: list[RoundedBox] = []
    original_save = Image.Image.save
    original_text = ImageDraw.ImageDraw.text
    original_rounded_rectangle = ImageDraw.ImageDraw.rounded_rectangle

    def patched_save(self: Image.Image, fp: Any, *args: Any, **kwargs: Any) -> None:
        return None

    def patched_rounded_rectangle(self: ImageDraw.ImageDraw, xy: Any, *args: Any, **kwargs: Any) -> Any:
        try:
            box = normalize_box(xy)
            width = box[2] - box[0]
            height = box[3] - box[1]
            if width >= 40 and height >= 20:
                rounded_boxes.append(RoundedBox(getattr(self, "_image", None), box))
        except Exception:
            pass
        return original_rounded_rectangle(self, xy, *args, **kwargs)

    def patched_text(self: ImageDraw.ImageDraw, xy: Any, text: Any, *args: Any, **kwargs: Any) -> Any:
        font = kwargs.get("font")
        anchor = kwargs.get("anchor")
        rendered = str(text)
        if rendered.strip():
            try:
                bbox = self.textbbox(xy, rendered, font=font, anchor=anchor)
                text_records.append(
                    TextRecord(
                        getattr(self, "_image", None),
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
    ImageDraw.ImageDraw.rounded_rectangle = patched_rounded_rectangle
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
        ImageDraw.ImageDraw.rounded_rectangle = original_rounded_rectangle

    findings: list[Finding] = []
    for record in text_records:
        candidates = [
            box
            for box in rounded_boxes
            if box.image is record.image and contains(box.bbox, record.bbox)
        ]
        if not candidates:
            continue
        nearest = min(candidates, key=lambda box: area(box.bbox))
        if not include_containers and not is_tag_box(nearest.bbox):
            continue
        pads = padding(nearest.bbox, record.bbox)
        min_x, min_y = (min_tag_pad_x, min_tag_pad_y)
        if pads[0] < min_x or pads[2] < min_x or pads[1] < min_y or pads[3] < min_y:
            findings.append(
                Finding(
                    path,
                    1,
                    "text_box_padding",
                    (
                        f"required=({min_x:.0f}px horizontal, {min_y:.0f}px vertical) "
                        f"actual=({pads[0]:.1f}, {pads[1]:.1f}, {pads[2]:.1f}, {pads[3]:.1f}) "
                        f"text={record.text[:60]!r} text_bbox={record.bbox} box={nearest.bbox}"
                    ),
                )
            )
    return findings


def audit_scripts(
    paths: list[Path],
    *,
    include_containers: bool = False,
    min_tag_pad_x: float = DEFAULT_MIN_TAG_PAD_X,
    min_tag_pad_y: float = DEFAULT_MIN_TAG_PAD_Y,
) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_python_files(paths):
        findings.extend(
            audit_script(
                path,
                include_containers=include_containers,
                min_tag_pad_x=min_tag_pad_x,
                min_tag_pad_y=min_tag_pad_y,
            )
        )
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=DEFAULT_PATHS)
    parser.add_argument("--include-containers", action="store_true")
    parser.add_argument("--min-tag-pad-x", type=float, default=DEFAULT_MIN_TAG_PAD_X)
    parser.add_argument("--min-tag-pad-y", type=float, default=DEFAULT_MIN_TAG_PAD_Y)
    args = parser.parse_args(argv)

    findings = audit_scripts(
        args.paths,
        include_containers=args.include_containers,
        min_tag_pad_x=args.min_tag_pad_x,
        min_tag_pad_y=args.min_tag_pad_y,
    )
    for finding in findings:
        print(finding.format())
    if findings:
        print(f"FIGURE_TEXT_PADDING_DYNAMIC_AUDIT_FAIL findings={len(findings)}", file=sys.stderr)
        return 1
    print("FIGURE_TEXT_PADDING_DYNAMIC_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
