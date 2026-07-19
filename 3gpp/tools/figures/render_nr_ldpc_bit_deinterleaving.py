#!/usr/bin/env python3
"""Render NR LDPC bit deinterleaving and LLR placement flow for T9.4."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T9.4_NR_LDPC_bit_deinterleaving.png"

PALETTE = {
    "ink": "#17212F",
    "muted": "#5B6877",
    "line": "#C9D4DF",
    "bg": "#FFFFFF",
    "blue": "#2457A6",
    "blue_l": "#EAF3FF",
    "green": "#2D8F5D",
    "green_l": "#EAF8EF",
    "amber": "#B9841A",
    "amber_l": "#FFF5DD",
    "red": "#B94A55",
    "red_l": "#FFECEF",
    "purple": "#6E55A4",
    "purple_l": "#F1EDFF",
}



def center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def wrap_lines(draw: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    return fit_wrap_text(draw, text, fnt, width)


def wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, width: int, fill: str, gap: int = 5) -> int:
    x, y = xy
    for line in wrap_lines(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#61758A", width: int = 3) -> None:
    sx, sy = start
    ex, ey = end
    length = math.hypot(ex - sx, ey - sy)
    if length == 0:
        return
    ux, uy = (ex - sx) / length, (ey - sy) / length
    px, py = -uy, ux
    head_len, head_w = 14, 8
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line((sx, sy, *line_end), fill=color, width=width)
    draw.polygon(
        [
            (ex, ey),
            (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
            (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def draw_flow(draw: ImageDraw.ImageDraw) -> None:
    y = 174
    boxes = [
        ("demapper LLR", "按调制符号输出：每符号 Qm 个 LLR", PALETTE["blue_l"], PALETTE["blue"]),
        ("deinterleaver", "按 TS 38.212 §5.4.2.2 反向置换", PALETTE["purple_l"], PALETTE["purple"]),
        ("rate recovery", "恢复 e 序列后按 RV/k0 写回缓存", PALETTE["green_l"], PALETTE["green"]),
        ("LDPC input", "得到按母码位置排列的 CB LLR", PALETTE["amber_l"], PALETTE["amber"]),
    ]
    x = 70
    prev = None
    for title, body, fill, edge in boxes:
        box = (x, y, x + 340, y + 136)
        draw.rounded_rectangle(box, radius=14, fill=fill, outline=edge, width=2)
        center(draw, (box[0], box[1] + 14, box[2], box[1] + 54), title, font(24, True), PALETTE["ink"])
        wrapped(draw, (x + 24, y + 66), body, font(24), 292, PALETTE["muted"], gap=4)
        if prev:
            arrow(draw, (prev[2], y + 68), (box[0], y + 68))
        prev = box
        x += 385


def draw_matrix(draw: ImageDraw.ImageDraw, x0: int, y0: int, qm: int, symbols: int, title: str) -> None:
    draw.text((x0, y0 - 44), title, font=font(24, True), fill=PALETTE["ink"])
    cell_w, cell_h = 112, 64
    header_h = 60
    draw.text((x0, y0), "demapper order f", font=font(24, True), fill=PALETTE["blue"])
    for s in range(symbols):
        for b in range(qm):
            idx = s * qm + b
            box = (x0 + b * cell_w, y0 + header_h + s * cell_h, x0 + (b + 1) * cell_w, y0 + header_h + (s + 1) * cell_h)
            draw.rectangle(box, fill=PALETTE["blue_l"], outline=PALETTE["line"], width=1)
            center(draw, box, f"f{idx}", font(24, True), PALETTE["ink"])
    for b in range(qm):
        center(draw, (x0 + b * cell_w, y0 + 32, x0 + (b + 1) * cell_w, y0 + 58), f"bit{b}", font(24), PALETTE["muted"])
    for s in range(symbols):
        draw.text((x0 - 72, y0 + header_h + 12 + s * cell_h), f"sym{s}", font=font(24), fill=PALETTE["muted"])

    mid_x = x0 + qm * cell_w + 100
    arrow_y = y0 + header_h + symbols * cell_h // 2
    arrow(draw, (x0 + qm * cell_w + 18, arrow_y), (mid_x - 30, arrow_y))
    label_box = (mid_x - 112, arrow_y - 42, mid_x - 8, arrow_y - 10)
    draw.rounded_rectangle(label_box, radius=6, fill=PALETTE["bg"], outline=PALETTE["line"], width=1)
    center(draw, label_box, "inverse", font(24, True), PALETTE["purple"])

    right_x = mid_x
    draw.text((right_x, y0), "rate-recovery input e", font=font(24, True), fill=PALETTE["green"])
    for i in range(symbols * qm):
        bit = i // symbols
        sym = i % symbols
        fidx = sym * qm + bit
        x = right_x + (i % (qm * 2)) * cell_w
        y = y0 + header_h + (i // (qm * 2)) * cell_h
        draw.rectangle((x, y, x + cell_w, y + cell_h), fill=PALETTE["green_l"], outline=PALETTE["line"], width=1)
        center(draw, (x, y, x + cell_w, y + 32), f"e{i}", font(24, True), PALETTE["ink"])
        center(draw, (x, y + 32, x + cell_w, y + cell_h), f"=f{fidx}", font(24), PALETTE["muted"])


def draw_checks(draw: ImageDraw.ImageDraw) -> None:
    panel = (70, 1060, 1530, 1306)
    draw.rounded_rectangle(panel, radius=14, fill="#FFFDF7", outline="#DDBB60", width=2)
    draw.text((100, 1056), "工程检测点", font=font(26, True), fill=PALETTE["amber"])
    rows = [
        ("Qm 来源", ["TS 38.214 MCS 决定 Qm；", "descriptor 不能写死。"]),
        ("bit order", ["固定 LLR pattern 检查：", "e[bS+s] = f[b+sQm]"]),
        ("buffer", ["写 demapper order，", "读 rate-recovery order。"]),
        ("bank conflict", ["Qm=4/6/8 时同拍", "多读写可能撞 bank。"]),
        ("failure", ["高 SNR 仍 CRC fail，", "先查 Qm/order/codeword。"]),
    ]
    x = 100
    for title, lines in rows:
        draw.rounded_rectangle((x, 1146, x + 270, 1266), radius=9, fill="#FFFFFF", outline=PALETTE["line"], width=1)
        center(draw, (x + 10, 1156, x + 260, 1190), title, font(24, True), PALETTE["ink"])
        y = 1194
        for line in lines:
            draw.text((x + 18, y), line, font=font(24), fill=PALETTE["muted"])
            y += 29
        x += 280


def main() -> None:
    img = Image.new("RGB", (1980, 1400), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 40), "NR LDPC Bit Deinterleaving 与 LLR 放置", font=font(40, True), fill=PALETTE["ink"])
    wrapped(
        draw,
        (70, 102),
        "TS 38.212 §5.4.2.2 的 bit interleaver 按 Qm 把 rate-matching 输出 e 重排成调制映射输入 f。接收端从 demapper 得到符号顺序 LLR 后，必须反向恢复 e 顺序，再交给 RV/k0 地址生成器。",
        font(24),
        1550,
        PALETTE["muted"],
    )
    draw_flow(draw)
    draw_matrix(draw, 95, 416, 2, 4, "QPSK: Qm=2，每个 symbol 两个 LLR")
    draw_matrix(draw, 95, 762, 4, 3, "16QAM: Qm=4，每个 symbol 四个 LLR")
    draw_checks(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
