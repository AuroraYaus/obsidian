#!/usr/bin/env python3
"""
@file    audit_figure_text_overlap_dynamic.py
@brief   动态审计 PIL 教学图渲染脚本中的文本 bbox 重叠。
         通过 monkey-patch PIL 的 draw.text() 和 Image.save() 来截获所有
         文本包围盒，然后逐对检测重叠——捕捉静态检查遗漏的布局 bug，
         如水平适配但垂直超出固定容器的换行文本。
@date    2026-07-22

Dynamically audit PIL figure scripts for overlapping text bboxes.

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
    """
    @brief   不可变的文本绘制记录。
             记录每次 draw.text() 调用时的文本内容、图像实例和包围盒，
             用于后续逐对重叠检测。
    """
    image: object
    text: str
    bbox: tuple[float, float, float, float]


@dataclass(frozen=True)
class Finding:
    """
    @brief   不可变的审计发现数据结构。
             使用 frozen dataclass 确保发现的完整性——发现一旦创建不可修改。
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
             仅匹配 render_ 前缀的脚本——因为只有渲染脚本才需要动态执行审计。
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


def overlap_area(
    a: tuple[float, float, float, float],
    b: tuple[float, float, float, float],
) -> tuple[float, tuple[float, float, float, float] | None]:
    """
    @brief   计算两个包围盒的重叠面积和相交矩形。
             这是重叠检测的核心几何运算——判断两个文本标签是否在视觉上重叠。
    @param   a  第一个包围盒 (x0, y0, x1, y1)。
    @param   b  第二个包围盒 (x0, y0, x1, y1)。
    @return  (重叠面积, 相交矩形或 None) 二元组。不相交时面积为 0.0。
    """
    x0 = max(a[0], b[0])
    y0 = max(a[1], b[1])
    x1 = min(a[2], b[2])
    y1 = min(a[3], b[3])
    if x1 <= x0 or y1 <= y0:
        return 0.0, None
    return (x1 - x0) * (y1 - y0), (x0, y0, x1, y1)


def is_meaningful_text(text: str) -> bool:
    """
    @brief   判断文本是否有足够的语义内容值得参与重叠检测。
             过滤掉单字符和空白文本——这些通常是装饰元素或坐标标注，
             重叠也可接受，不需要报告。
    @param   text  文本内容。
    @return  若文本长度 >1（去除空白后）则返回 True。
    """
    return len(text.strip()) > 1


def audit_script(path: Path, min_area: float = DEFAULT_MIN_AREA) -> list[Finding]:
    """
    @brief   动态执行单个渲染脚本并审计所有文本 bbox 重叠。
             通过 monkey-patch PIL.Image.save（阻止文件写入）和
             PIL.ImageDraw.text（记录 bbox）来截获所有文本绘制操作，
             然后按图像分组进行逐对重叠检测。
    @param   path      渲染脚本的文件路径。
    @param   min_area  报告的最小重叠面积阈值（像素^2），默认为 80.0。
                       低于此阈值的微小重叠（如字体衬线接触）会被忽略。
    @return  重叠发现列表。
    @note    使用 runpy.run_path() 执行脚本，stdout/stderr 被重定向到
             StringIO 以避免审计过程中的噪音输出。
    @throws  不会向上抛异常——脚本执行失败（SystemExit/Exception）会被捕获
             并转为 Finding 报告。
    """
    records: list[TextRecord] = []
    original_save = Image.Image.save
    original_text = ImageDraw.ImageDraw.text

    def patched_save(self: Image.Image, fp: Any, *args: Any, **kwargs: Any) -> None:
        """@brief   Monkey-patched Image.save() —— no-op 以阻止文件写入。
        @param   self   Image 实例。
        @param   fp     文件路径或文件对象（被忽略）。"""
        return None

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
    """
    @brief   对多个渲染脚本执行动态文本重叠审计。
             遍历所有 render_*.py 脚本，逐个执行并收集重叠发现。
    @param   paths     待审计的路径列表。
    @param   min_area  报告的最小重叠面积阈值（像素^2）。
    @return  所有脚本的重叠发现列表。
    """
    findings: list[Finding] = []
    for path in iter_python_files(paths):
        findings.extend(audit_script(path, min_area=min_area))
    return findings


def main(argv: list[str] | None = None) -> int:
    """
    @brief   动态文本重叠审计入口——执行渲染脚本并检测文本 bbox 重叠。
    @param   argv  命令行参数列表（sys.argv）。
    @usage   python audit_figure_text_overlap_dynamic.py [paths...] [--min-area N]
    @args    paths       待审计的渲染脚本路径或目录，默认为 tools/figures。
             --min-area  报告的最小重叠面积（像素^2），默认 80.0。
                         低于此阈值的微小接触（如字体衬线）不会被报告。
    @env     需要 PIL/Pillow；被审计的渲染脚本需在其自身环境可执行。
    @exit_code  0 = 无重叠发现，1 = 存在文本 bbox 重叠。
    @note    本脚本会实际执行渲染脚本（通过 runpy），但所有 Image.save()
             调用被 monkey-patch 为 no-op，不会产生任何输出文件。
    """
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
