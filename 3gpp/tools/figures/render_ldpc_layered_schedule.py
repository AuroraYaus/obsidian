#!/usr/bin/env python3
"""Render LDPC flooding vs layered schedule overview."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T8.7_LDPC_layered_schedule_flow.png"

PALETTE = {
    "ink": "#17212F",
    "muted": "#5B6877",
    "line": "#C9D4DF",
    "bg": "#FFFFFF",
    "panel": "#F7F9FC",
    "blue": "#2457A6",
    "green": "#2D8F5D",
    "amber": "#C69220",
    "red": "#C64B59",
    "purple": "#7457A6",
}



def center_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill: str, width: int, gap: int = 6) -> int:
    x, y = xy
    for line in fit_wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#61758A") -> None:
    sx, sy = start
    ex, ey = end
    length = math.hypot(ex - sx, ey - sy)
    if length == 0:
        return
    ux, uy = (ex - sx) / length, (ey - sy) / length
    px, py = -uy, ux
    head_len, head_w = 14, 8
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line((sx, sy, *line_end), fill=color, width=3)
    points = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(points, fill=color)


def node(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, body: str, fill: str) -> None:
    draw.rounded_rectangle(box, radius=10, fill=fill, outline=PALETTE["line"], width=2)
    center_text(draw, (box[0] + 10, box[1] + 12, box[2] - 10, box[1] + 54), title, font(24, True), PALETTE["ink"])
    draw_wrapped(draw, (box[0] + 18, box[1] + 66), body, font(24), PALETTE["muted"], box[2] - box[0] - 36, gap=8)


def table(draw: ImageDraw.ImageDraw, x: int, y: int, headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 56) -> int:
    xx = x
    for header, width in zip(headers, widths):
        draw.rectangle((xx, y, xx + width, y + row_h), fill="#EAF3FF", outline=PALETTE["line"], width=2)
        center_text(draw, (xx + 6, y, xx + width - 6, y + row_h), header, font(24, True), PALETTE["ink"])
        xx += width
    y += row_h
    for row in rows:
        xx = x
        for value, width in zip(row, widths):
            draw.rectangle((xx, y, xx + width, y + row_h), fill="#FFFFFF", outline=PALETTE["line"], width=1)
            center_text(draw, (xx + 6, y, xx + width - 6, y + row_h), value, font(24), PALETTE["ink"])
            xx += width
        y += row_h
    return y


def draw_schedule_compare(draw: ImageDraw.ImageDraw) -> None:
    draw.text((80, 165), "Flooding 与 Layered 时序差异", font=font(34, True), fill=PALETTE["blue"])
    # Flooding row.
    y = 235
    boxes = [
        (80, y, 305, y + 140, "CN all rows", "先用旧变量消息计算所有校验节点。", "#F7F9FC"),
        (370, y, 595, y + 140, "VN all cols", "再统一更新所有变量节点。", "#F7F9FC"),
        (660, y, 885, y + 140, "Syndrome", "整轮结束后检查。", "#F7F9FC"),
    ]
    for b in boxes:
        node(draw, b[:4], b[4], b[5], b[6])
    arrow(draw, (305, y + 70), (370, y + 70))
    arrow(draw, (595, y + 70), (660, y + 70))
    draw_wrapped(
        draw,
        (80, y + 165),
        "Flooding：一轮内先算完全部 CN，再统一 VN；同一轮后面的行看不到前面行的新结果。",
        font(24),
        PALETTE["muted"],
        830,
    )
    # Layered row.
    y = 530
    boxes = [
        (80, y, 305, y + 140, "Layer 0", "更新行组 0，立即写回软值。", "#F0F7F4"),
        (370, y, 595, y + 140, "Layer 1", "读到前层的新软值。", "#F0F7F4"),
        (660, y, 885, y + 140, "Layer 2", "继续 RMW 更新。", "#F0F7F4"),
    ]
    for b in boxes:
        node(draw, b[:4], b[4], b[5], b[6])
    arrow(draw, (305, y + 70), (370, y + 70), PALETTE["green"])
    arrow(draw, (595, y + 70), (660, y + 70), PALETTE["green"])
    draw_wrapped(
        draw,
        (80, y + 165),
        "Layered：同一 iteration 内逐层更新，变量节点新值立即影响后续 layer，通常收敛更快。",
        font(24),
        PALETTE["muted"],
        830,
    )


def draw_layer_table(draw: ImageDraw.ImageDraw) -> None:
    draw.text((980, 165), "小 H 的 layer 更新顺序", font=font(34, True), fill=PALETTE["green"])
    rows = [
        ["0", "c0", "v0,v1,v3", "更新 L0,L1,L3"],
        ["1", "c1", "v1,v2,v4", "使用新 L1"],
        ["2", "c2", "v0,v2,v5", "使用新 L0/L2"],
    ]
    table(draw, 980, 225, ["layer", "row", "connected cols", "read-modify-write"], rows, [95, 95, 260, 300], row_h=56)
    draw_wrapped(
        draw,
        (980, 500),
        "真实 NR 中一个 layer 通常对应 BG 的一个 row group；该 row group 通过 shift value 连接若干 column group，每个有效连接扩展成 Zc 个 bit-level 更新。",
        font(24),
        PALETTE["muted"],
        800,
    )
    draw.rounded_rectangle((980, 650, 1830, 835), radius=14, fill=PALETTE["panel"], outline=PALETTE["line"], width=2)
    draw.text((1015, 680), "Zc 地址访问", font=font(30, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (1015, 730),
        "BG 边含 row group、column group 和 shift；地址为 base(column)+(local+shift) mod Zc。",
        font(24),
        PALETTE["muted"],
        780,
    )


def draw_flow_and_log(draw: ImageDraw.ImageDraw) -> None:
    panel = (80, 965, 1830, 1335)
    draw.rounded_rectangle(panel, radius=16, fill="#FFFDF6", outline="#E2CD7A", width=2)
    draw.text((120, 1000), "Layered decoder loop 与验证日志", font=font(34, True), fill=PALETTE["ink"])
    steps = [
        ("iteration loop", "iter < max_iter"),
        ("layer loop", "row group order"),
        ("CN update", "current layer"),
        ("VN update", "write soft value"),
        ("syndrome", "check schedule"),
    ]
    x = 120
    y = 1075
    prev = None
    for title, body in steps:
        box = (x, y, x + 250, y + 125)
        node(draw, box, title, body, "#FFFFFF")
        if prev:
            arrow(draw, (prev[2], y + 62), (box[0], y + 62), PALETTE["amber"])
        prev = box
        x += 330
    draw_wrapped(
        draw,
        (120, 1248),
        "最小验证日志：iteration、layer、syndrome_weight、updated_variable_count、bank_conflict_count、pipeline_stall_count。",
        font(24),
        PALETTE["red"],
        1680,
    )


def main() -> None:
    img = Image.new("RGB", (1920, 1400), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((80, 48), "LDPC Flooding 与 Layered 译码调度", font=font(46, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (80, 112),
        "Layered schedule 不是新的码结构，而是按 TS 38.212 的 BG row group / QC-LDPC 连接顺序组织消息更新。核心差异是同一 iteration 内是否立即使用刚更新的变量节点值。",
        font(24),
        PALETTE["muted"],
        1680,
    )
    draw_schedule_compare(draw)
    draw_layer_table(draw)
    draw_flow_and_log(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
