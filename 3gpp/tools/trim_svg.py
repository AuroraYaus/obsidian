#!/usr/bin/env python3
"""
@file trim_svg.py
@brief 裁剪 LibreOffice 导出的公式 SVG 到内容边界。
       LibreOffice 把 .wmf 公式导出为 SVG 时保留 A4 页面坐标（内容常位于
       负坐标区），Obsidian 渲染时显示为空白页 + 边角小公式。本脚本解析
       SVG 中 path/text 元素的坐标（考虑 scale transform），计算内容
       包围盒，重设 viewBox 为内容区域。
@date 2026-08-01
@usage python3 trim_svg.py [--dir media_svg] [--padding 60]
@args --dir       待裁剪的 SVG 目录（默认 media_svg）。
@args --padding   内容边距（SVG 用户单位，默认 60）。
@exit_code 0 = 全部成功；1 = 至少一个文件解析失败。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

COORD_RE = re.compile(r"[-+]?\d+\.?\d*(?:[eE][-+]?\d+)?")


def extract_coords(svg_text: str) -> list[float]:
    """
    @brief 从 SVG 中提取 path d 与 text 的坐标（未缩放坐标）。
    @param svg_text  SVG 文本。
    @return          坐标对列表（x0, y0, x1, y1, ...）。
    @note path d 中的每个数字按 (x, y) 成对收集；text 的 x/y 属性
           单独收集；忽略其他属性（stroke-width 等）。
    """
    coords: list[float] = []
    for m in re.finditer(r'd="([^"]+)"', svg_text):
        nums = [float(n) for n in COORD_RE.findall(m.group(1))]
        # path 坐标按序成对；奇数个时丢弃最后一个
        coords.extend(nums[: len(nums) - len(nums) % 2])
    for m in re.finditer(r'<text\b[^>]*\bx="([-0-9.eE+]+)"[^>]*\by="([-0-9.eE+]+)"', svg_text):
        coords.extend([float(m.group(1)), float(m.group(2))])
    for m in re.finditer(r'<text\b[^>]*\by="([-0-9.eE+]+)"[^>]*\bx="([-0-9.eE+]+)"', svg_text):
        coords.extend([float(m.group(2)), float(m.group(1))])
    return coords


def find_scale(svg_text: str) -> float:
    """
    @brief 提取 SVG 中内容的全局缩放因子。
    @param svg_text  SVG 文本。
    @return          缩放因子（默认 1.0）。
    @note LibreOffice 导出 wmf 时使用 scale(s, -s) 翻转 Y 轴，此处取
           第一个 transform 中的正缩放值。
    """
    m = re.search(r'transform="scale\(\s*([-0-9.eE+]+)\s*,\s*[-0-9.eE+]+', svg_text)
    if m:
        return abs(float(m.group(1)))
    return 1.0


def trim_svg(svg_text: str, padding: float = 60.0) -> str:
    """
    @brief 将 SVG 的 viewBox 裁剪到内容边界。
    @param svg_text  SVG 文本。
    @param padding   内容边距（用户单位）。
    @return          裁剪后的 SVG 文本。
    @note 保留全部元素，仅重设 svg 根元素的 viewBox/width/height；
           内容为空时返回原样。
    """
    coords = extract_coords(svg_text)
    if len(coords) < 4:
        return svg_text
    xs = coords[0::2]
    ys = coords[1::2]
    # 注意：viewBox 使用 wmf 原始坐标（子元素 transform="scale(s,-s)"
    # 已在渲染时处理缩放与 Y 翻转），因此这里直接取原始坐标 bbox，
    # 不乘 scale。
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(ys), max(ys)
    w = (x1 - x0) + 2 * padding
    h = (y1 - y0) + 2 * padding
    if w <= 0 or h <= 0:
        return svg_text
    vx, vy = x0 - padding, y0 - padding
    # 重设根 svg 的 viewBox 与尺寸
    svg_text = re.sub(
        r'viewBox="[^"]*"',
        f'viewBox="{vx:.1f} {vy:.1f} {w:.1f} {h:.1f}"',
        svg_text,
        count=1,
    )
    svg_text = re.sub(
        r'width="[^"]*"',
        f'width="{w / 100:.1f}mm"',
        svg_text,
        count=1,
    )
    svg_text = re.sub(
        r'height="[^"]*"',
        f'height="{h / 100:.1f}mm"',
        svg_text,
        count=1,
    )
    return svg_text


def main() -> int:
    """
    @brief 脚本入口：批量裁剪目录下的 SVG。
    @usage python3 trim_svg.py --dir media_svg --padding 60
    @args --dir       待裁剪 SVG 目录（默认 media_svg）。
    @args --padding   内容边距（默认 60）。
    @exit_code 0 = 全部成功；1 = 至少一个文件处理失败。
    """
    parser = argparse.ArgumentParser(description="Trim LibreOffice formula SVGs to content bounds")
    parser.add_argument("--dir", default="media_svg", help="Directory containing SVGs to trim")
    parser.add_argument("--padding", type=float, default=60.0, help="Content padding in user units")
    args = parser.parse_args()

    svg_dir = Path(args.dir)
    if not svg_dir.is_dir():
        print(f"目录不存在: {svg_dir}", file=sys.stderr)
        return 1
    ok = failed = 0
    for svg in sorted(svg_dir.glob("*.svg")):
        try:
            text = svg.read_text(encoding="utf-8")
            trimmed = trim_svg(text, args.padding)
            if trimmed != text:
                svg.write_text(trimmed, encoding="utf-8")
            ok += 1
        except Exception as exc:  # pragma: no cover - 单文件失败不影响其余
            print(f"{svg.name}: {exc}", file=sys.stderr)
            failed += 1
    print(f"裁剪完成: {ok} 成功, {failed} 失败")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
