#!/usr/bin/env python3
""" @file render_nr_polar_sc_decoding_tree.py
@brief 渲染 N=4 Polar SC（逐次抵消）译码树教学图，展示 f/g 函数、判决与 partial sum 回传的完整流程。
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
OUT_PATH = ROOT / "docs/L2/assets/T10.4_NR_Polar_SC_N4_tree.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#5B6778",
    "line": "#8EA0B8",
    "blue": "#2457A6",
    "blue_fill": "#EAF1FB",
    "green": "#237A57",
    "green_fill": "#E8F6EF",
    "orange": "#B7662D",
    "orange_fill": "#FFF2E6",
    "red": "#B83E4A",
    "red_fill": "#FCEBED",
    "gray_fill": "#F6F8FB",
}



def round_box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    fill: str,
    outline: str,
    width: int = 2,
    radius: int = 14,
) -> None:
    """ @brief 绘制统一风格的圆角矩形框，用于包裹译码树中的每个阶段节点。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @param fill 填充色 hex 字符串。
    @param outline 描边色 hex 字符串。
    @param width 描边宽度，默认 2px。
    @param radius 圆角半径，默认 14px。
    @return None
    """
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def center_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    lines: list[str],
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    gap: int = 6,
) -> None:
    """ @brief 将多行文本在指定矩形区域内水平和垂直居中绘制，用于节点内显示公式与译码结果。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @param lines 待绘制的文本行列表。
    @param fnt PIL 字体对象。
    @param fill 文本颜色 hex 字符串。
    @param gap 行间距，默认 6px。
    @return None
    """
    heights = []
    widths = []
    for line in lines:
        box = draw.textbbox((0, 0), line, font=fnt)
        widths.append(box[2] - box[0])
        heights.append(box[3] - box[1])
    total_h = sum(heights) + gap * (len(lines) - 1)
    y = xy[1] + (xy[3] - xy[1] - total_h) / 2
    for line, w, h in zip(lines, widths, heights):
        x = xy[0] + (xy[2] - xy[0] - w) / 2
        draw.text((x, y), line, font=fnt, fill=fill)
        y += h + gap


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    fill: str,
    width: int = 3,
) -> None:
    """ @brief 绘制带三角形箭头的直线段，表示译码树中的数据流向。
    @param draw PIL 绘图上下文。
    @param start 线段起点坐标 (x, y)。
    @param end 线段终点坐标 (x, y)，箭头指向此处。
    @param fill 线条与箭头填充色 hex 字符串。
    @param width 线宽，默认 3px。
    @return None
    @note 箭头头部长度 14px、宽度 8px，居中于线段末端。
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
    draw.line((x0, y0, *line_end), fill=fill, width=width)
    pts = [
        (x1, y1),
        (x1 - ux * head_len + px * head_w, y1 - uy * head_len + py * head_w),
        (x1 - ux * head_len - px * head_w, y1 - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=fill)


def segment_intersects_rect(
    p0: tuple[float, float],
    p1: tuple[float, float],
    rect: tuple[int, int, int, int],
    margin: int = 0,
) -> bool:
    """ @brief 判断线段是否与矩形区域相交，用于折线箭头布局时的碰撞检测。
    @param p0 线段起点 (x, y)。
    @param p1 线段终点 (x, y)。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @param margin 矩形外扩边距，默认 0。
    @return 相交返回 True，否则 False。
    @note 检测线段端点是否在矩形内、以及线段与矩形四条边的交点。
    """
    x0, y0, x1, y1 = rect
    x0 -= margin
    y0 -= margin
    x1 += margin
    y1 += margin
    ax, ay = p0
    bx, by = p1
    if (x0 < ax < x1 and y0 < ay < y1) or (x0 < bx < x1 and y0 < by < y1):
        return True
    if ax == bx:
        return x0 <= ax <= x1 and min(ay, by) <= y1 and max(ay, by) >= y0
    if ay == by:
        return y0 <= ay <= y1 and min(ax, bx) <= x1 and max(ax, bx) >= x0
    for x in (x0, x1):
        t = (x - ax) / (bx - ax)
        if 0 <= t <= 1:
            y = ay + t * (by - ay)
            if y0 <= y <= y1:
                return True
    for y in (y0, y1):
        t = (y - ay) / (by - ay)
        if 0 <= t <= 1:
            x = ax + t * (bx - ax)
            if x0 <= x <= x1:
                return True
    return False


def assert_no_unrelated_crossing(
    name: str,
    points: list[tuple[float, float]],
    forbidden: dict[str, tuple[int, int, int, int]],
) -> None:
    """ @brief 断言折线路径不穿过任何禁行矩形区域，确保箭头布局视觉上不重叠。
    @param name 箭头名称，用于错误消息标识。
    @param points 折线顶点列表 [(x, y), ...]。
    @param forbidden 禁行矩形字典 {名称: (x0, y0, x1, y1)}。
    @return None
    @throws AssertionError 当任意折线段穿过禁行矩形时抛出。
    """
    for p0, p1 in zip(points, points[1:]):
        for rect_name, rect in forbidden.items():
            if segment_intersects_rect(p0, p1, rect, margin=3):
                raise AssertionError(f"{name} segment {p0}->{p1} crosses {rect_name} {rect}")


def elbow_arrow(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[int, int]],
    fill: str,
    width: int = 3,
) -> None:
    """ @brief 绘制折线箭头（多段直线 + 末端三角箭头），用于绕开其他节点的反馈路径。
    @param draw PIL 绘图上下文。
    @param points 折线顶点列表 [(x, y), ...]，最后一段末端绘制箭头。
    @param fill 线条与箭头填充色 hex 字符串。
    @param width 线宽，默认 3px。
    @return None
    """
    x1, y1 = points[-1]
    x0, y0 = points[-2]
    length = math.hypot(x1 - x0, y1 - y0)
    if length == 0:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    px, py = -uy, ux
    head_len, head_w = 14, 8
    line_points = list(points[:-1]) + [(x1 - ux * head_len, y1 - uy * head_len)]
    for start, end in zip(line_points, line_points[1:]):
        draw.line((start, end), fill=fill, width=width)
    pts = [
        (x1, y1),
        (x1 - ux * head_len + px * head_w, y1 - uy * head_len + py * head_w),
        (x1 - ux * head_len - px * head_w, y1 - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=fill)


def main() -> None:
    """ @brief 渲染 T10.4 N=4 Polar SC 译码树教学图，保存为 PNG 到 docs/L2/assets/。
    @note 该图展示从通道 LLR 输入、f 函数进入左半树、frozen 位强制判决、g 函数进入右半树、
     information 位判决到 partial sum 回传的完整 SC 译码流程，附带 f/g 函数约定公式。
    @return None
    """
    img = Image.new("RGB", (2100, 1460), COL["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "T10.4 N=4 Polar SC 译码树：f/g、判决与 partial sum", font=font(34, True), fill=COL["ink"])
    center_text(
        draw,
        (70, 104, 1750, 158),
        [
            "LLR 输入 L=[-0.7, 2.1, -1.4, 1.8]；f 使用 min-sum 近似；",
            "frozen set={0,1}，information set={2,3}。",
        ],
        font(24),
        COL["muted"],
    )

    # Main flow boxes.
    boxes = {
        "input": (80, 220, 500, 370),
        "top_f": (650, 185, 1120, 345),
        "left_sc": (1280, 150, 1900, 360),
        "top_g": (650, 515, 1120, 680),
        "right_sc": (1280, 500, 1900, 745),
        "combine": (650, 890, 1900, 1075),
        "result": (650, 1195, 1900, 1375),
    }

    round_box(draw, boxes["input"], COL["gray_fill"], COL["line"])
    center_text(draw, boxes["input"], ["通道 LLR", "L0=-0.7  L1=2.1", "L2=-1.4  L3=1.8"], font(24, True), COL["ink"])

    round_box(draw, boxes["top_f"], COL["blue_fill"], COL["blue"])
    center_text(draw, boxes["top_f"], ["左半树输入", "a0=f(L0,L2)=+0.7", "a1=f(L1,L3)=+1.8"], font(24, True), COL["blue"])

    round_box(draw, boxes["left_sc"], COL["red_fill"], COL["red"])
    center_text(draw, boxes["left_sc"], ["先译 u0,u1", "u0 frozen -> 0", "u1 frozen -> 0", "βL=[u0⊕u1,u1]=[0,0]"], font(24, True), COL["red"], gap=8)

    round_box(draw, boxes["top_g"], COL["green_fill"], COL["green"])
    center_text(draw, boxes["top_g"], ["右半树输入", "b0=g(L0,L2,βL0)=-2.1", "b1=g(L1,L3,βL1)=+3.9"], font(24, True), COL["green"])

    round_box(draw, boxes["right_sc"], COL["orange_fill"], COL["orange"])
    center_text(draw, boxes["right_sc"], ["再译 u2,u3", "u2: f(b0,b1)=-2.1 -> 1", "u3: g(b0,b1,u2)=+6.0 -> 0", "βR=[u2⊕u3,u3]=[1,0]"], font(24, True), COL["orange"], gap=7)

    round_box(draw, boxes["combine"], COL["gray_fill"], COL["line"])
    center_text(
        draw,
        boxes["combine"],
        ["partial sum 回传与合成", "β=[βL⊕βR, βR]=[1,0,1,0]", "叶子判决 û=[0,0,1,0]，硬编码输出估计 x̂=[1,0,1,0]"],
        font(24, True),
        COL["ink"],
    )

    round_box(draw, boxes["result"], COL["blue_fill"], COL["blue"])
    center_text(
        draw,
        boxes["result"],
        ["读图顺序", "1 输入通道 LLR  2 f 进入左半树  3 frozen 强制判决", "4 g 进入右半树  5 information 判决  6 partial sum 回传"],
        font(24, True),
        COL["blue"],
    )

    arrow(draw, (500, 265), (650, 235), COL["line"])
    arrow(draw, (1120, 235), (1280, 225), COL["blue"])
    arrow(draw, (885, 315), (885, 485), COL["green"])
    partial_sum_feedback = [(1280, 225), (1210, 225), (1210, 568), (1120, 568)]
    assert_no_unrelated_crossing(
        "partial_sum_feedback",
        partial_sum_feedback,
        {"再译 u2,u3": boxes["right_sc"], "partial sum 回传与合成": boxes["combine"]},
    )
    elbow_arrow(draw, partial_sum_feedback, COL["green"])
    arrow(draw, (1120, 568), (1280, 592), COL["green"])
    arrow(draw, (1590, 715), (1590, 860), COL["orange"])
    arrow(draw, (1590, 1045), (1590, 1165), COL["line"])

    # Formula strip.
    strip = (80, 1195, 500, 1375)
    round_box(draw, strip, COL["orange_fill"], COL["orange"])
    center_text(
        draw,
        strip,
        ["函数约定", "f(a,b)≈sign(a)sign(b)min(|a|,|b|)", "g(a,b,s)=b+(1-2s)a"],
        font(24, True),
        COL["orange"],
        gap=5,
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
