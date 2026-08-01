#!/usr/bin/env python3
""" @file render_nr_polar_scl_path_pruning.py
@brief 渲染 N=4, L=2 Polar SCL 路径分裂、PM 排序与剪枝教学图，展示列表译码的候选管理机制。
@date 2025
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T10.5_NR_Polar_SCL_N4_L2_paths.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#5B6778",
    "line": "#91A1B7",
    "blue": "#2457A6",
    "blue_fill": "#EAF1FB",
    "green": "#237A57",
    "green_fill": "#E8F6EF",
    "red": "#B83E4A",
    "red_fill": "#FCEBED",
    "orange": "#B7662D",
    "orange_fill": "#FFF2E6",
    "gray_fill": "#F7F9FC",
}



def box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    lines: list[str],
    fill: str,
    outline: str,
) -> None:
    """ @brief 绘制带标题和正文列表的圆角矩形卡片，用于表示 SCL 译码路径的每个阶段。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @param title 卡片标题文本。
    @param lines 正文行列表。
    @param fill 填充色 hex 字符串。
    @param outline 标题与描边色 hex 字符串。
    @return None
    """
    draw.rounded_rectangle(xy, radius=14, fill=fill, outline=outline, width=2)
    draw.text((xy[0] + 22, xy[1] + 16), title, font=font(24, True), fill=outline)
    heights = [draw.textbbox((0, 0), line, font=font(24))[3] - draw.textbbox((0, 0), line, font=font(24))[1] for line in lines]
    gap = 10
    total = sum(heights) + gap * max(len(lines) - 1, 0)
    y = xy[1] + 72 + (xy[3] - xy[1] - 98 - total) / 2
    for line, height in zip(lines, heights):
        draw.text((xy[0] + 26, y), line, font=font(24), fill=COL["ink"])
        y += height + gap


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], fill: str) -> None:
    """ @brief 绘制带三角形箭头的直线段，表示 SCL 路径在阶段间的流向。
    @param draw PIL 绘图上下文。
    @param start 线段起点坐标 (x, y)。
    @param end 线段终点坐标 (x, y)。
    @param fill 线条与箭头填充色 hex 字符串。
    @return None
    """
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length == 0:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    px, py = -uy, ux
    head_len, head_w = 14, 8
    line_end = (x1 - ux * head_len, y1 - uy * head_len)
    draw.line((x0, y0, *line_end), fill=fill, width=3)
    pts = [
        (x1, y1),
        (x1 - ux * head_len + px * head_w, y1 - uy * head_len + py * head_w),
        (x1 - ux * head_len - px * head_w, y1 - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=fill)


def center_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], text: str, fnt: ImageFont.ImageFont, fill: str) -> None:
    """ @brief 在矩形区域内居中绘制单行文本，用于表格单元格中的路径信息展示。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @param text 待绘制的文本字符串。
    @param fnt PIL 字体对象。
    @param fill 文本颜色 hex 字符串。
    @return None
    """
    draw.text(((xy[0] + xy[2]) / 2, (xy[1] + xy[3]) / 2), text, font=fnt, fill=fill, anchor="mm")


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.ImageFont, fill: str, width: int, gap: int = 6) -> None:
    """ @brief 在给定宽度内自动换行绘制文本，用于工程检测点的说明段落。
    @param draw PIL 绘图上下文。
    @param xy 起始坐标 (x, y)。
    @param text 待绘制的文本字符串。
    @param fnt PIL 字体对象。
    @param fill 文本颜色 hex 字符串。
    @param width 最大行宽（px）。
    @param gap 行间距，默认 6px。
    @return None
    """
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += draw.textbbox((0, 0), line, font=fnt)[3] + gap


def main() -> None:
    """ @brief 渲染 T10.5 N=4, L=2 Polar SCL 路径分裂与剪枝教学图，保存为 PNG 到 docs/L2/assets/。
    @note 该图展示从空列表初始、frozen 位强制置 0、information 位分裂 0/1、
     按 PM 排序保留前 L=2 条路径的完整流程，附带路径表和工程检测点提醒。
    @return None
    """
    img = Image.new("RGB", (2000, 1340), COL["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "T10.5 N=4, L=2 Polar SCL 路径分裂、排序与剪枝", font=font(34, True), fill=COL["ink"])
    draw_wrapped(
        draw,
        (70, 88),
        "约定 path metric 越小越好；frozen 位不分裂，information 位分裂 0/1，超过 L 条后按 PM 排序保留前 L 条。",
        font(24),
        COL["muted"],
        1700,
    )

    x = [80, 445, 810, 1175, 1540]
    y_top = 190
    w = 300
    h = 260

    box(draw, (x[0], y_top, x[0] + w, y_top + h), "初始", ["path: []", "PM=0.00", "active=1"], COL["gray_fill"], COL["line"])
    box(draw, (x[1], y_top, x[1] + w, y_top + h), "u0 frozen", ["force 0", "path: [0]", "PM=0.00", "no split"], COL["red_fill"], COL["red"])
    box(draw, (x[2], y_top, x[2] + w, y_top + h), "u1 frozen", ["force 0", "path: [0,0]", "PM=0.00", "no split"], COL["red_fill"], COL["red"])

    box(
        draw,
        (x[3], y_top, x[3] + w, y_top + h),
        "u2 information",
        ["split to 0/1", "u2=0: PM=2.2", "u2=1: PM=0.0", "keep both"],
        COL["green_fill"],
        COL["green"],
    )

    box(
        draw,
        (x[4], y_top, x[4] + w, y_top + h),
        "u3 information",
        ["split each path", "4 candidates", "sort by PM", "keep best L=2"],
        COL["green_fill"],
        COL["green"],
    )

    for i in range(4):
        arrow(draw, (x[i] + w, y_top + 130), (x[i + 1], y_top + 130), COL["line"])

    # Candidate table.
    table_x = 150
    table_y = 570
    col_w = [170, 250, 170, 170, 170, 240]
    row_h = 62  # TEXT_FIT_OK: candidate table uses short PM/path labels centered at 24px.
    headers = ["step", "candidate path", "u2 PM", "u3 PM", "total PM", "status"]
    rows = [
        ["after u2", "[0,0,0]", "+2.2", "-", "2.2", "kept"],
        ["after u2", "[0,0,1]", "+0.0", "-", "0.0", "kept"],
        ["after u3", "[0,0,0,0]", "2.2", "+0.0", "2.2", "pruned"],
        ["after u3", "[0,0,0,1]", "2.2", "+1.1", "3.3", "pruned"],
        ["after u3", "[0,0,1,0]", "0.0", "+0.0", "0.0", "kept #1"],
        ["after u3", "[0,0,1,1]", "0.0", "+6.0", "6.0", "kept #2"],
    ]

    draw.text((table_x, table_y - 52), "路径表：每次分裂后必须复制 bits、PM、LLR state 和 partial sums", font=font(24, True), fill=COL["ink"])
    cx = table_x
    for htxt, cw in zip(headers, col_w):
        cell_box = (cx, table_y, cx + cw, table_y + row_h)
        draw.rectangle(cell_box, fill=COL["blue_fill"], outline=COL["line"])
        center_text(draw, cell_box, htxt, font(24, True), COL["blue"])
        cx += cw

    for r, row in enumerate(rows):
        cy = table_y + row_h * (r + 1)
        fill = COL["green_fill"] if "kept" in row[-1] else COL["red_fill"]
        cx = table_x
        for cell, cw in zip(row, col_w):
            cell_box = (cx, cy, cx + cw, cy + row_h)
            draw.rectangle(cell_box, fill=fill, outline=COL["line"])
            is_key = cell in {"kept", "pruned", "kept #1", "kept #2"}
            center_text(draw, cell_box, cell, font(24, is_key), COL["ink"])
            cx += cw

    note = (150, 1065, 1850, 1240)
    draw.rounded_rectangle(note, radius=14, fill=COL["orange_fill"], outline=COL["orange"], width=2)
    draw.text((note[0] + 22, note[1] + 18), "工程检测点", font=font(26, True), fill=COL["orange"])
    draw_wrapped(
        draw,
        (note[0] + 22, note[1] + 58),
        "排序器只比较 PM 不足够：剪枝时必须同步复制路径 bit、LLR memory 指针、partial sum memory 和 CRC 状态。",
        font(24),
        COL["ink"],
        note[2] - note[0] - 44,
    )
    draw.text(
        (note[0] + 22, note[1] + 94),
        "若只复制 bit 而漏复制 partial sum，下一次 g 函数会使用错误历史，PM 看似合理但候选路径不可复现。",
        font=font(24),
        fill=COL["ink"],
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
