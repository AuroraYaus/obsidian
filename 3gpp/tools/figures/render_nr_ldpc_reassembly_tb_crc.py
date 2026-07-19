#!/usr/bin/env python3
"""Render NR LDPC code-block reassembly and TB CRC flow for T9.5."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T9.5_NR_LDPC_reassembly_TB_CRC.png"

COLORS = {
    "ink": "#17212F",
    "muted": "#5A6675",
    "line": "#C7D1DC",
    "bg": "#FFFFFF",
    "blue": "#2457A6",
    "blue_l": "#EAF3FF",
    "green": "#278760",
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
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    x = box[0] + ((box[2] - box[0]) - width) / 2 - bbox[0]
    y = box[1] + ((box[3] - box[1]) - height) / 2 - bbox[1]
    draw.text((x, y), text, font=fnt, fill=fill)


def wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, width: int, fill: str, gap: int = 4) -> int:
    x, y = xy
    for line in fit_wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#66788A") -> None:
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
    draw.polygon(
        [
            (ex, ey),
            (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
            (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def card(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, body: str, fill: str, edge: str) -> None:
    draw.rounded_rectangle(box, radius=10, fill=fill, outline=edge, width=2)
    center(draw, (box[0] + 10, box[1] + 18, box[2] - 10, box[1] + 58), title, font(24, True), COLORS["ink"])
    wrapped(draw, (box[0] + 22, box[1] + 78), body, font(24), box[2] - box[0] - 44, COLORS["muted"], gap=6)


def draw_top_flow(draw: ImageDraw.ImageDraw) -> None:
    y = 170
    boxes = [
        ("LDPC decoder", "输出比特、校验子、迭代状态", COLORS["blue_l"], COLORS["blue"]),
        ("CB CRC gate", "逐块 CRC；无 CB CRC 标记 skip", COLORS["purple_l"], COLORS["purple"]),
        ("strip local fields", "去填充和 CB CRC，保留 TB 候选", COLORS["green_l"], COLORS["green"]),
        ("TB CRC gate", "检查 TB CRC，决定交付与反馈", COLORS["amber_l"], COLORS["amber"]),
    ]
    x = 70
    prev = None
    for title, body, fill, edge in boxes:
        box = (x, y, x + 390, y + 185)
        card(draw, box, title, body, fill, edge)
        if prev:
            arrow(draw, (prev[2], y + 65), (box[0], y + 65))
        prev = box
        x += 450


def draw_cb_bars(draw: ImageDraw.ImageDraw) -> None:
    draw.text((70, 430), "两个 CB 的重组边界：先清理每个 CB，再按 r 顺序拼接", font=font(28, True), fill=COLORS["ink"])
    x0, y0 = 115, 510
    segs = [
        ("filler", 90, COLORS["red_l"], COLORS["red"]),
        ("payload0", 230, COLORS["blue_l"], COLORS["blue"]),
        ("CB CRC0", 110, COLORS["purple_l"], COLORS["purple"]),
    ]
    segs2 = [
        ("payload1", 290, COLORS["blue_l"], COLORS["blue"]),
        ("CB CRC1", 110, COLORS["purple_l"], COLORS["purple"]),
    ]
    for idx, seg_list in enumerate([segs, segs2]):
        x = x0
        y = y0 + idx * 95
        draw.text((x - 70, y + 16), f"CB{idx}", font=font(24, True), fill=COLORS["ink"])
        for label, width, fill, edge in seg_list:
            box = (x, y, x + width, y + 56)
            draw.rectangle(box, fill=fill, outline=edge, width=2)
            center(draw, box, label, font(24, True), COLORS["ink"])
            x += width
    draw.text((x0, y0 + 195), "CB CRC pass 后仅保留 payload；输出按 r 顺序拼接。", font=font(24), fill=COLORS["muted"])

    arrow(draw, (620, y0 + 150), (735, y0 + 150), COLORS["green"])
    label_box = (552, y0 + 112, 728, y0 + 164)
    draw.rounded_rectangle(label_box, radius=5, fill=COLORS["bg"], outline=COLORS["line"], width=1)
    center(draw, label_box, "concat by r", font(24, True), COLORS["green"])

    tx = 760
    ty = y0 + 85
    out = [
        ("payload0", 250, COLORS["green_l"], COLORS["green"]),
        ("payload1", 310, COLORS["green_l"], COLORS["green"]),
        ("TB CRC", 120, COLORS["amber_l"], COLORS["amber"]),
    ]
    x = tx
    for label, width, fill, edge in out:
        box = (x, ty, x + width, ty + 64)
        draw.rectangle(box, fill=fill, outline=edge, width=2)
        center(draw, box, label, font(24, True), COLORS["ink"])
        x += width
    draw.text((tx, ty + 88), "TB CRC 覆盖整个 TB candidate；拼接顺序只按 CB 编号。", font=font(24), fill=COLORS["muted"])


def draw_cbg_panel(draw: ImageDraw.ImageDraw) -> None:
    panel = (70, 785, 1830, 1085)
    draw.rounded_rectangle(panel, radius=14, fill="#FFFDF7", outline="#DDBB60", width=2)
    draw.text((100, 820), "CBG 部分重传与重组状态", font=font(28, True), fill=COLORS["amber"])
    rows = [
        ("CBG0 mask=0", "未传输：保持历史结果", COLORS["blue_l"], COLORS["blue"]),
        ("CBG1 mask=1", "新 LLR：译码并刷新", COLORS["green_l"], COLORS["green"]),
        ("reassembly", "同一 HARQ/TB 的最新 CB 结果", COLORS["purple_l"], COLORS["purple"]),
        ("feedback", "fail->NACK；pass->释放上下文", COLORS["red_l"], COLORS["red"]),
    ]
    x = 100
    for title, body, fill, edge in rows:
        box = (x, 890, x + 410, 1038)
        draw.rounded_rectangle(box, radius=9, fill=fill, outline=edge, width=2)
        center(draw, (x + 14, 904, x + 396, 938), title, font(24, True), COLORS["ink"])
        center(draw, (x + 22, 960, x + 388, 1018), body, font(24), COLORS["muted"])
        x += 430


def draw_checks(draw: ImageDraw.ImageDraw) -> None:
    draw.text((70, 1155), "验证观察点", font=font(28, True), fill=COLORS["ink"])
    rows = [
        ("cb_crc_present", "无 CB CRC 时标记 skip"),
        ("strip ranges", "去除范围可 dump"),
        ("concat_order", "按 r 顺序拼接"),
        ("tb_crc_input", "payload 与 TB CRC 边界"),
        ("harq_feedback", "区分 CB/TB/CBG held"),
    ]
    x = 100
    for title, body in rows:
        box = (x, 1215, x + 330, 1375)
        draw.rounded_rectangle(box, radius=9, fill="#FFFFFF", outline=COLORS["line"], width=1)
        center(draw, (x + 12, 1230, x + 318, 1268), title, font(24, True), COLORS["ink"])
        wrapped(draw, (x + 22, 1295), body, font(24), 286, COLORS["muted"], gap=5)
        x += 350


def main() -> None:
    img = Image.new("RGB", (1900, 1460), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 40), "NR LDPC Code Block Reassembly 与 TB CRC", font=font(38, True), fill=COLORS["ink"])
    wrapped(
        draw,
        (70, 100),
        "接收端在 LDPC 译码之后，先按每个 CB 的协议边界去除 filler 和可选 CB CRC，再按 CB 编号顺序拼接成 TB candidate，最后由 TB CRC 决定交付和 HARQ 状态。",
        font(24),
        1450,
        COLORS["muted"],
    )
    draw_top_flow(draw)
    draw_cb_bars(draw)
    draw_cbg_panel(draw)
    draw_checks(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
