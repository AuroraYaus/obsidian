#!/usr/bin/env python3
"""
@file    audit_image_content_bounds.py
@brief   审计已渲染图像的内容边界，检测过量的底部空白边距。
         通过 Pillow 的 ImageChops.difference() 检测实际内容与背景色的
         差异区域，计算底部空白——过大的底部空白意味着渲染脚本的布局计算
         有误，导致图像在小尺寸截图或幻灯片嵌入时浪费大量空间。
@date    2026-07-22

Audit rendered image content bounds against excessive blank margins.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops


DEFAULT_PATHS = [Path("docs/L1_基础/assets"), Path("docs/L2_协议算法/assets"), Path("docs/L3_工程实现/assets")]
DEFAULT_MAX_BOTTOM_PIXELS = 160
DEFAULT_MAX_BOTTOM_RATIO = 0.10


@dataclass(frozen=True)
class Finding:
    """
    @brief   不可变的审计发现数据结构。
             封装发现的路径、行号（图像文件统一为 1）、规则名和详细消息。
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


def iter_image_files(paths: list[Path]) -> list[Path]:
    """
    @brief   从路径列表中收集所有 PNG 图像文件。
             遍历目录下的 .png 文件（也支持 .jpg/.jpeg），
             过滤掉非图像文件以专注于已渲染产物的审计。
    @param   paths  路径列表，可混合目录和文件。
    @return  去重排序后的图像文件路径列表。
    """
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
    """
    @brief   通过 Pillow 的像素差分检测图像的实际内容包围盒。
             以左上角像素 (0,0) 的颜色作为背景色，将整张图像与该背景色的
             纯色图像做差分——差分区域的包围盒即为内容边界。
    @param   path  图像文件路径。
    @return  内容包围盒 (x0, y0, x1, y1)，若图像完全空白则返回 None。
    @note    该方法假设背景是纯色且左上角像素代表背景色。
             对于渐变或有边框的图像可能不精确，但在本项目的教学图中，
             背景通常是统一的白色或浅色。
    """
    with Image.open(path) as img:
        rgb = img.convert("RGB")
        background = Image.new("RGB", rgb.size, rgb.getpixel((0, 0)))
        return ImageChops.difference(rgb, background).getbbox()


def audit_images(
    paths: list[Path],
    max_bottom_pixels: int = DEFAULT_MAX_BOTTOM_PIXELS,
    max_bottom_ratio: float = DEFAULT_MAX_BOTTOM_RATIO,
) -> list[Finding]:
    """
    @brief   对多个路径下的所有图像执行内容边界审计。
             检测每张图像的底部空白——同时检查绝对像素数和相对比例，
             两者都超标才报告，以避免对小尺寸图像的误报。
    @param   paths              待审计的路径列表。
    @param   max_bottom_pixels  允许的最大底部空白像素数，默认 160。
    @param   max_bottom_ratio   允许的最大底部空白比例，默认 0.10 (10%)。
    @return  底部空白过量的发现列表。
    @note    同时使用像素数和比例双重阈值——只有两者都超标才报告。
             例如：高分辨率图像可能有 >160px 空白但仍 <10% 比例。
    """
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
    """
    @brief   图像内容边界审计入口——检测已渲染 PNG 中的过量底部空白。
    @param   argv  命令行参数列表（sys.argv）。
    @usage   python audit_image_content_bounds.py [paths...]
             [--max-bottom-pixels N] [--max-bottom-ratio R]
    @args    paths               待审计的图像文件路径或目录，
                                 默认为 docs/L1_基础/assets docs/L2_协议算法/assets docs/L3_工程实现/assets。
             --max-bottom-pixels  允许的最大底部空白像素数，默认 160。
             --max-bottom-ratio   允许的最大底部空白比例（0.0-1.0），默认 0.10。
    @exit_code  0 = 无发现，1 = 存在底部空白过量的图像。
    @note    需要 Pillow 库已安装。空白检测基于左上角像素颜色作为背景色，
             适用于本项目纯色背景的教学图。
    """
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
