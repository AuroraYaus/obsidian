#!/usr/bin/env python3
"""
@file    audit_figure_text_padding_dynamic.py
@brief   动态审计 PIL 教学图渲染脚本中圆角框内文本的 padding 是否充足。
         通过 monkey-patch PIL 的 rounded_rectangle() 和 text() 来截获
         所有圆角框和文本包围盒，检测文本是否过于贴近框边界——
         缺乏 padding 的教学图在投影和打印场景下会显得拥挤难读。
@date    2026-07-22

Dynamically audit PIL figure scripts for text padding inside rounded boxes.
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
DEFAULT_MIN_TAG_PAD_X = 8.0
DEFAULT_MIN_TAG_PAD_Y = 4.0


@dataclass(frozen=True)
class TextRecord:
    """
    @brief   不可变的文本绘制记录。
             记录每次 draw.text() 调用的文本内容、图像引用和包围盒。
    """
    image: object
    text: str
    bbox: tuple[float, float, float, float]


@dataclass(frozen=True)
class RoundedBox:
    """
    @brief   不可变的圆角矩形绘制记录。
             记录每次 rounded_rectangle() 调用的图像引用和包围盒。
    """
    image: object
    bbox: tuple[float, float, float, float]


@dataclass(frozen=True)
class Finding:
    """
    @brief   不可变的审计发现数据结构。
             路径、行号、规则名和详细消息组成一条完整的发现。
    """
    path: Path
    line: int
    rule: str
    message: str

    def format(self) -> str:
        """
        @brief   将发现格式化为 "path:line: rule: message" 标准输出。
                 统一格式化接口，确保所有发现以一致的格式输出。
        @return  格式化后的发现字符串。
        """
        return f"{self.path}:{self.line}: {self.rule}: {self.message}"


def iter_python_files(paths: list[Path]) -> list[Path]:
    """
    @brief   从路径列表中收集所有 render_*.py 文件。
             仅匹配 render_ 前缀——只有渲染脚本才需要动态执行审计。
    @param   paths  路径列表，可混合目录和文件。
    @return  去重排序后的渲染脚本路径列表。
    """
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
    """
    @brief   将 PIL 的 xy 参数统一规范化为 (x0, y0, x1, y1) 格式。
             PIL 接受 [(x0,y0), (x1,y1)] 或 (x0, y0, x1, y1) 两种格式——
             统一后简化后续的包含关系和 padding 计算。
    @param   xy  PIL 矩形参数，可以是二元列表或四元元组。
    @return  规范化的四浮点包围盒 (x0, y0, x1, y1)。
    """
    if len(xy) == 2 and isinstance(xy[0], (tuple, list)):
        x0, y0 = xy[0]
        x1, y1 = xy[1]
    else:
        x0, y0, x1, y1 = xy
    return float(x0), float(y0), float(x1), float(y1)


def contains(outer: tuple[float, float, float, float], inner: tuple[float, float, float, float]) -> bool:
    """
    @brief   检查 outer 包围盒是否完全包含 inner 包围盒。
             用于建立文本框与圆角框之间的包含关系——只有文本在框内才需要检查 padding。
    @param   outer  外部包围盒（圆角框）。
    @param   inner  内部包围盒（文本框）。
    @return  若 outer 完全包含 inner 则返回 True。
    """
    return outer[0] <= inner[0] and outer[1] <= inner[1] and outer[2] >= inner[2] and outer[3] >= inner[3]


def area(box: tuple[float, float, float, float]) -> float:
    """
    @brief   计算包围盒的面积。
             用于在多个包含同一文本的圆角框中找到最近的（面积最小的）那个。
    @param   box  包围盒 (x0, y0, x1, y1)。
    @return  面积值（宽*高，非负）。
    """
    return max(0.0, box[2] - box[0]) * max(0.0, box[3] - box[1])


def padding(
    outer: tuple[float, float, float, float],
    inner: tuple[float, float, float, float],
) -> tuple[float, float, float, float]:
    """
    @brief   计算文本相对于圆角框的四边 padding 值。
             返回 (left_pad, top_pad, right_pad, bottom_pad)——任何一方的
             padding 不足都意味着文字在视觉上过于贴近边框。
    @param   outer  外部包围盒（圆角框）。
    @param   inner  内部包围盒（文本框）。
    @return  四元组 (左间距, 上间距, 右间距, 下间距)，单位像素。
    """
    return inner[0] - outer[0], inner[1] - outer[1], outer[2] - inner[2], outer[3] - inner[3]


def is_tag_box(box: tuple[float, float, float, float]) -> bool:
    """
    @brief   判断圆角框是否为标签/徽章框（而非大型容器）。
             标签框通常较小（高度≤64px 且宽度≤360px），这些是需要 padding 检查的
             主要目标——大型容器框的 padding 容忍度更高，可能不需要检查。
    @param   box  包围盒 (x0, y0, x1, y1)。
    @return  若框尺寸在标签范围内则返回 True。
    """
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
    """
    @brief   动态执行单个渲染脚本并审计圆角框中文本的 padding 充足性。
             通过 monkey-patch PIL 的 rounded_rectangle() 和 text() 来截获
             所有圆角框和文本位置，然后建立包含关系并检查四边 padding。
    @param   path               渲染脚本的文件路径。
    @param   include_containers 若为 True，则也检查大型容器框的 padding。
                                默认为 False，仅检查标签/徽章框。
    @param   min_tag_pad_x      水平方向的最小要求 padding（像素），默认 8.0。
    @param   min_tag_pad_y      垂直方向的最小要求 padding（像素），默认 4.0。
    @return  padding 不足的发现列表。
    @note    使用 runpy.run_path() 执行脚本，Image.save() 被 patch 为 no-op，
             因此不会产生任何输出文件。
    @throws  不会向上抛异常——脚本执行失败会被捕获并转为 Finding 报告。
    """
    text_records: list[TextRecord] = []
    rounded_boxes: list[RoundedBox] = []
    original_save = Image.Image.save
    original_text = ImageDraw.ImageDraw.text
    original_rounded_rectangle = ImageDraw.ImageDraw.rounded_rectangle

    def patched_save(self: Image.Image, fp: Any, *args: Any, **kwargs: Any) -> None:
        """@brief   Monkey-patched Image.save() —— no-op 以阻止文件写入。
        @param   self   Image 实例。
        @param   fp     文件路径或文件对象（被忽略）。"""
        return None

    def patched_rounded_rectangle(self: ImageDraw.ImageDraw, xy: Any, *args: Any, **kwargs: Any) -> Any:
        """@brief   Monkey-patched ImageDraw.rounded_rectangle() —— 记录圆角框后调用原始实现。
        @param   self   ImageDraw 实例。
        @param   xy     矩形坐标参数。"""
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
        """@brief   Monkey-patched ImageDraw.text() —— 记录文本包围盒后调用原始实现。
        @param   self   ImageDraw 实例。
        @param   xy     文本绘制位置。
        @param   text   待绘制的文本内容。"""
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
    """
    @brief   对多个渲染脚本执行动态文本 padding 审计。
             遍历所有 render_*.py 脚本，逐个执行并收集 padding 发现。
    @param   paths               待审计的路径列表。
    @param   include_containers  是否也检查大型容器框的 padding。
    @param   min_tag_pad_x       水平方向的最小要求 padding（像素）。
    @param   min_tag_pad_y       垂直方向的最小要求 padding（像素）。
    @return  所有脚本的 padding 不足发现列表。
    """
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
    """
    @brief   动态文本 padding 审计入口——执行渲染脚本并检测圆角框中文本 padding。
    @param   argv  命令行参数列表（sys.argv）。
    @usage   python audit_figure_text_padding_dynamic.py [paths...] [--include-containers]
             [--min-tag-pad-x N] [--min-tag-pad-y N]
    @args    paths                待审计的渲染脚本路径或目录，默认为 tools/figures。
             --include-containers 同时检查大型容器框的 padding（默认仅检查标签框）。
             --min-tag-pad-x      水平方向最小要求 padding（像素），默认 8.0。
             --min-tag-pad-y      垂直方向最小要求 padding（像素），默认 4.0。
    @env     需要 PIL/Pillow；被审计的渲染脚本需在其自身环境可执行。
    @exit_code  0 = 无 padding 不足发现，1 = 存在 padding 不足。
    @note    本脚本会实际执行渲染脚本，但 Image.save() 被 patch 为 no-op，
             不会产生输出文件。
    """
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
