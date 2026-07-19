#!/usr/bin/env python3
"""Render NR Polar rate recovery reverse flow and toy circular buffer."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T10.7_NR_Polar_rate_recovery_flow.png"

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



def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    lines: list[str],
    size: int,
    fill: str,
    bold: bool = True,
    gap: int = 6,
) -> None:
    fnt = font(size, bold)
    heights = [draw.textbbox((0, 0), line, font=fnt)[3] - draw.textbbox((0, 0), line, font=fnt)[1] for line in lines]
    total = sum(heights) + gap * (len(lines) - 1)
    y = (xy[1] + xy[3] - total) / 2
    cx = (xy[0] + xy[2]) / 2
    for line, h in zip(lines, heights):
        draw.text((cx, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + gap


def center(xy: tuple[int, int, int, int]) -> tuple[float, float]:
    return ((xy[0] + xy[2]) / 2, (xy[1] + xy[3]) / 2)


def boundary_point(xy: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    cx, cy = center(xy)
    dx = toward[0] - cx
    dy = toward[1] - cy
    if abs(dx) < 1e-6 and abs(dy) < 1e-6:
        return cx, cy
    half_w = max((xy[2] - xy[0]) / 2, 1)
    half_h = max((xy[3] - xy[1]) / 2, 1)
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return cx + dx / scale, cy + dy / scale


def box(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, lines: list[str], fill: str, outline: str) -> tuple[int, int, int, int]:
    draw.rounded_rectangle(xy, radius=14, fill=fill, outline=outline, width=2)
    draw_centered_lines(draw, (xy[0] + 10, xy[1] + 12, xy[2] - 10, xy[1] + 58), [title], 24, outline, True)
    draw_centered_lines(draw, (xy[0] + 16, xy[1] + 68, xy[2] - 16, xy[3] - 16), lines, 24, COL["ink"], True, 8)
    return xy


def arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], fill: str) -> None:
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux = (x1 - x0) / length
    uy = (y1 - y0) / length
    head_len = 13
    head_w = 8
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    draw.line((start, line_end), fill=fill, width=3)
    angle = math.atan2(y1 - y0, x1 - x0)
    back_x = x1 - head_len * math.cos(angle)
    back_y = y1 - head_len * math.sin(angle)
    perp_x = head_w * math.sin(angle)
    perp_y = -head_w * math.cos(angle)
    pts = [(x1, y1), (back_x + perp_x, back_y + perp_y), (back_x - perp_x, back_y - perp_y)]
    draw.polygon(pts, fill=fill)


def connect_arrow(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], fill: str) -> None:
    arrow(draw, boundary_point(src, center(dst)), boundary_point(dst, center(src)), fill)


def main() -> None:
    img = Image.new("RGB", (2080, 1530), COL["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "T10.7 NR Polar 速率恢复：接收端反操作与 LLR 放回", font=font(34, True), fill=COL["ink"])
    draw_centered_lines(
        draw,
        (70, 100, 1950, 158),
        [
            "发送端：sub-block interleaving -> bit collection/selection -> optional coded-bit interleaving",
            "接收端按相反方向恢复 LLR。",
        ],
        24,
        COL["muted"],
        False,
        4,
    )

    top_y = 200
    xs = [80, 455, 830, 1205, 1580]
    w = 300
    h = 240
    flow_boxes = [
        box(draw, (xs[0], top_y, xs[0] + w, top_y + h), "demapper LLR", ["rx_llr[0:E-1]", "Qm bit order", "soft values"], COL["gray_fill"], COL["line"]),
        box(draw, (xs[1], top_y, xs[1] + w, top_y + h), "coded-bit deinterleave", ["if enabled", "undo bit interleaving", "recover e-order"], COL["blue_fill"], COL["blue"]),
        box(draw, (xs[2], top_y, xs[2] + w, top_y + h), "bit selection reverse", ["place into buffer", "punctured=unknown", "shortened=known zero", "repeated=accumulate"], COL["green_fill"], COL["green"]),
        box(draw, (xs[3], top_y, xs[3] + w, top_y + h), "sub-block deinterleave", ["undo 32-block pattern", "table 5.4.1.1-1", "restore codeword order"], COL["blue_fill"], COL["blue"]),
        box(draw, (xs[4], top_y, xs[4] + w, top_y + h), "Polar decoder input", ["L[0:N-1]", "SC/SCL/CA-SCL", "frozen mask"], COL["green_fill"], COL["green"]),
    ]
    for left, right in zip(flow_boxes, flow_boxes[1:]):
        connect_arrow(draw, left, right, COL["line"])

    # Toy circular buffer.
    draw.text((120, 465), "小型循环缓存例子：N=8, E=10，位置 0/1 punctured，位置 6/7 repeated，位置 3 shortened", font=font(24, True), fill=COL["ink"])
    cell_x = 120
    cell_y = 530
    cell_w = 205
    cell_h = 128
    labels = [
        ("0", "punctured", "LLR=0"),
        ("1", "punctured", "LLR=0"),
        ("2", "received", "+1.2"),
        ("3", "shortened", "+31"),
        ("4", "received", "-0.7"),
        ("5", "received", "+2.0"),
        ("6", "repeated", "-1.0 + -0.5"),
        ("7", "repeated", "+0.6 + +0.8"),
    ]
    for i, (idx, role, val) in enumerate(labels):
        x = cell_x + i * cell_w
        fill = COL["red_fill"] if role == "punctured" else COL["orange_fill"] if role == "shortened" else COL["green_fill"] if role == "repeated" else COL["blue_fill"]
        outline = COL["red"] if role == "punctured" else COL["orange"] if role == "shortened" else COL["green"] if role == "repeated" else COL["blue"]
        cell_box = (x, cell_y, x + cell_w - 14, cell_y + cell_h)
        draw.rounded_rectangle(cell_box, radius=12, fill=fill, outline=outline, width=2)
        draw_centered_lines(draw, cell_box, [f"pos {idx}", role, val], 24, COL["ink"], True, 5)

    note = (120, 790, 1910, 1060)
    draw.rounded_rectangle(note, radius=14, fill=COL["orange_fill"], outline=COL["orange"], width=2)
    draw_centered_lines(draw, (note[0] + 20, note[1] + 16, note[0] + 390, note[1] + 58), ["LLR 初始化规则"], 26, COL["orange"], True)
    lines = [
        "punctured / not transmitted: unknown -> neutral LLR 0",
        "shortened / known zero: strong positive LLR, saturated to implementation max",
        "repetition: same mother-code position receives multiple LLRs -> accumulate with saturation",
        "sub-block deinterleaving changes positions, not LLR sign convention",
    ]
    y = note[1] + 70
    for line in lines:
        draw.text((note[0] + 24, y), line, font=font(24, True), fill=COL["ink"])
        y += 44

    # Comparison strip.
    table_x = 120
    table_y = 1175
    col_w = [260, 440, 440, 440]
    row_h = 64  # TEXT_FIT_OK: cells use centered 24px text and short controlled labels.
    headers = ["对象", "NR Polar", "NR LDPC", "LTE Turbo"]
    rows = [
        ["母码对象", "Polar codeword N", "LDPC circular buffer Ncb", "Turbo circular buffer Kw"],
        ["interleaving", "sub-block + optional coded-bit", "bit interleaving by Qm", "sub-block + bit collection"],
        ["重复处理", "LLR accumulate", "LLR accumulate", "HARQ soft combine"],
    ]
    cx = table_x
    for htxt, cw in zip(headers, col_w):
        cell_box = (cx, table_y, cx + cw, table_y + row_h)
        draw.rectangle(cell_box, fill=COL["blue_fill"], outline=COL["line"])
        draw_centered_lines(draw, cell_box, [htxt], 24, COL["blue"], True)
        cx += cw
    for r, row in enumerate(rows):
        cy = table_y + row_h * (r + 1)
        cx = table_x
        for cell, cw in zip(row, col_w):
            cell_box = (cx, cy, cx + cw, cy + row_h)
            draw.rectangle(cell_box, fill=COL["gray_fill"], outline=COL["line"])
            draw_centered_lines(draw, cell_box, [cell], 24, COL["ink"], True)
            cx += cw

    flow_to_table_gap = table_y - note[3]
    bottom_margin = 1620 - (table_y + row_h * (len(rows) + 1))
    assert flow_to_table_gap >= 90
    assert bottom_margin >= 120

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
