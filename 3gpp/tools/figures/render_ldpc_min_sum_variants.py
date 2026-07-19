#!/usr/bin/env python3
"""Render LDPC Min-Sum/NMS/OMS check-node comparison."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T8.6_LDPC_MS_NMS_OMS_compare.png"

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


def table(draw: ImageDraw.ImageDraw, x: int, y: int, headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 56) -> int:
    row_h = max(row_h, 56)
    xx = x
    for header, width in zip(headers, widths):
        draw.rectangle((xx, y, xx + width, y + row_h), fill="#EAF3FF", outline=PALETTE["line"], width=2)
        center_text(draw, (xx + 4, y, xx + width - 4, y + row_h), header, font(24, True), PALETTE["ink"])
        xx += width
    y += row_h
    for row in rows:
        xx = x
        for value, width in zip(row, widths):
            draw.rectangle((xx, y, xx + width, y + row_h), fill="#FFFFFF", outline=PALETTE["line"], width=1)
            center_text(draw, (xx + 4, y, xx + width - 4, y + row_h), value, font(24), PALETTE["ink"])
            xx += width
        y += row_h
    return y


def draw_check_node(draw: ImageDraw.ImageDraw) -> None:
    draw.text((70, 160), "Check-node 输入", font=font(30, True), fill=PALETTE["blue"])
    cx, cy = 330, 395
    inputs = [
        ("q0=+2.4", 105, 250),
        ("q1=-0.9", 105, 525),
        ("q2=+1.6", 555, 250),
        ("q3=-3.1", 555, 525),
    ]
    # Draw edges first so they never cover node labels.
    for _, x, y in inputs:
        draw.line((x, y, cx, cy), fill="#9FB0C3", width=3)
    draw.rounded_rectangle((cx - 52, cy - 36, cx + 52, cy + 36), radius=10, fill="#EAF8F1", outline=PALETTE["green"], width=3)
    center_text(draw, (cx - 52, cy - 36, cx + 52, cy + 36), "CN", font(24, True), PALETTE["ink"])
    for label, x, y in inputs:
        draw.ellipse((x - 50, y - 50, x + 50, y + 50), fill="#EAF3FF", outline=PALETTE["blue"], width=3)
        center_text(draw, (x - 50, y - 22, x + 50, y + 22), label, font(24, True), PALETTE["ink"])
    draw_wrapped(
        draw,
        (70, 610),
        "给某条边输出时，只看其他输入：符号取其他输入符号乘积，幅度取其他输入绝对值的最小值。",
        font(24),
        PALETTE["muted"],
        560,
    )


def draw_min1_min2(draw: ImageDraw.ImageDraw) -> None:
    panel = (710, 160, 1530, 385)
    draw.rounded_rectangle(panel, radius=16, fill=PALETTE["panel"], outline=PALETTE["line"], width=2)
    draw.text((740, 190), "min1/min2 机制", font=font(30, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (740, 240),
        "输入绝对值为 [2.4, 0.9, 1.6, 3.1]。min1=0.9 来自 q1，min2=1.6 来自 q2。输出给 q1 时不能用 q1 自己的 min1，因此改用 min2；其他输出使用 min1。",
        font(24),
        PALETTE["muted"],
        730,
    )


def draw_compare_table(draw: ImageDraw.ImageDraw) -> None:
    draw.text((710, 410), "同一组输入下的三种输出", font=font(30, True), fill=PALETTE["green"])
    rows = [
        ["to q0", "+", "0.9", "+0.900", "+0.675", "+0.500"],
        ["to q1", "-", "1.6", "-1.600", "-1.200", "-1.200"],
        ["to q2", "+", "0.9", "+0.900", "+0.675", "+0.500"],
        ["to q3", "-", "0.9", "-0.900", "-0.675", "-0.500"],
    ]
    table(draw, 710, 455, ["输出边", "符号", "幅度", "MS", "NMS α=.75", "OMS β=.4"], rows, [100, 80, 90, 110, 140, 140], row_h=56)


def draw_resource_panel(draw: ImageDraw.ImageDraw) -> None:
    panel = (70, 750, 1530, 1060)
    draw.rounded_rectangle(panel, radius=16, fill="#FFFDF6", outline="#E2CD7A", width=2)
    draw.text((105, 780), "工程取舍", font=font(30, True), fill=PALETTE["ink"])
    items = [
        ("SPA", "tanh/atanh 精确但昂贵，需要 LUT 或函数近似。"),
        ("Min-Sum", "只需符号异或和 min1/min2，复杂度低但偏乐观。"),
        ("NMS", "乘 α<1 降低过度自信，性能通常优于纯 MS。"),
        ("OMS", "减 β 后截零，弱消息压为 0；β 过大会损失信息。"),
    ]
    x = 105
    for title, body in items:
        draw.rounded_rectangle((x, 845, x + 320, 990), radius=10, fill="#FFFFFF", outline=PALETTE["line"], width=2)
        draw.text((x + 18, 862), title, font=font(24, True), fill=PALETTE["blue"])
        draw_wrapped(draw, (x + 18, 902), body, font(24), PALETTE["muted"], 284, gap=8)
        x += 350


def main() -> None:
    img = Image.new("RGB", (1600, 1120), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "LDPC Min-Sum、NMS 与 OMS 校验节点更新", font=font(40, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (70, 102),
        "教学输入 q=[+2.4,-0.9,+1.6,-3.1]。图中展示 check-node 输出给每条边时如何排除自身输入，并比较 Min-Sum、Normalized Min-Sum 和 Offset Min-Sum。",
        font(24),
        PALETTE["muted"],
        1420,
    )
    draw_check_node(draw)
    draw_min1_min2(draw)
    draw_compare_table(draw)
    draw_resource_panel(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
