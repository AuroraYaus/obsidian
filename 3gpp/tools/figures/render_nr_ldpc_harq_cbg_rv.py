#!/usr/bin/env python3
"""Render NR LDPC HARQ soft-buffer, RV, and CBG partial retransmission diagram."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T9.3_NR_LDPC_HARQ_CBG_RV.png"

PALETTE = {
    "ink": "#17212F",
    "muted": "#586575",
    "line": "#C8D2DD",
    "bg": "#FFFFFF",
    "blue": "#2463A6",
    "blue_l": "#EAF3FF",
    "green": "#277D54",
    "green_l": "#EAF7EF",
    "amber": "#B9841A",
    "amber_l": "#FFF5DD",
    "red": "#B94A55",
    "red_l": "#FFECEF",
    "purple": "#6E55A4",
    "purple_l": "#F1EDFF",
    "gray": "#F3F6F9",
}



def text_center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt,
    width: int,
    fill: str,
    gap: int = 5,
) -> int:
    x, y = xy
    lines = fit_wrap_text(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#61758A") -> None:
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    ux, uy = dx / dist, dy / dist
    length = 13
    wing = 7
    line_end = (end[0] - ux * length, end[1] - uy * length)
    draw.line((start[0], start[1], *line_end), fill=color, width=3)
    px, py = -uy, ux
    p1 = (end[0] - ux * length + px * wing, end[1] - uy * length + py * wing)
    p2 = (end[0] - ux * length - px * wing, end[1] - uy * length - py * wing)
    draw.polygon([end, p1, p2], fill=color)


def draw_hierarchy(draw: ImageDraw.ImageDraw) -> None:
    draw.text((70, 205), "TB / CBG / CB 层级与本次重传 mask", font=font(28, True), fill=PALETTE["blue"])
    tb = (70, 260, 1830, 340)
    draw.rounded_rectangle(tb, radius=12, fill=PALETTE["blue_l"], outline=PALETTE["blue"], width=2)
    text_center(draw, tb, "TB0: harq_id=5, tb_id=0, NDI=old data, RV=2, CBGTI=[0,1], CBGFI=1", font(24, True), PALETTE["ink"])

    groups = [
        ("CBG0", "CB0, CB1", "mask bit=0: 本次不重传，soft buffer 保持", PALETTE["gray"], PALETTE["muted"]),
        ("CBG1", "CB2, CB3", "mask bit=1: 本次重传，按 RV2/k0 写回", PALETTE["green_l"], PALETTE["green"]),
    ]
    for idx, (name, cbs, note, fill, edge) in enumerate(groups):
        x0 = 100 + idx * 850
        box = (x0, 390, x0 + 760, 560)
        draw.rounded_rectangle(box, radius=14, fill=fill, outline=edge, width=2)
        draw.text((x0 + 26, 410), name, font=font(24, True), fill=edge)
        draw.text((x0 + 26, 438), cbs, font=font(24, True), fill=PALETTE["ink"])
        wrapped(draw, (x0 + 26, 480), note, font(24), 700, PALETTE["muted"], gap=5)
        arrow(draw, (tb[0] + 480 + idx * 800, tb[3]), (x0 + 380, box[1]), edge)
        for j, cb in enumerate(cbs.split(", ")):
            cb_box = (x0 + 95 + j * 320, 600, x0 + 335 + j * 320, 668)
            draw.rounded_rectangle(cb_box, radius=8, fill="#FFFFFF", outline=edge, width=2)
            text_center(draw, cb_box, cb, font(24, True), PALETTE["ink"])
            arrow(draw, (x0 + 325, box[3]), (cb_box[0] + 100, cb_box[1]), edge)


def draw_ring(draw: ImageDraw.ImageDraw, cx: int, cy: int, title: str, retransmit: bool) -> None:
    draw.text((cx - 240, cy - 210), title, font=font(24, True), fill=PALETTE["ink"])
    radius = 112
    labels = [str(i) for i in range(12)]
    rv0 = {0, 1, 2, 3}
    rv2 = {3, 4, 5, 6}
    repeat = {3}
    for i in range(12):
        angle = -math.pi / 2 + i * 2 * math.pi / 12
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        if i in rv2 and retransmit:
            fill = PALETTE["green_l"] if i not in repeat else PALETTE["amber_l"]
            edge = PALETTE["green"] if i not in repeat else PALETTE["amber"]
        elif i in rv0:
            fill = PALETTE["blue_l"]
            edge = PALETTE["blue"]
        else:
            fill = "#FFFFFF"
            edge = PALETTE["line"]
        cell = (int(x - 32), int(y - 28), int(x + 32), int(y + 28))
        draw.rounded_rectangle(cell, radius=8, fill=fill, outline=edge, width=2)
        text_center(draw, cell, labels[i], font(24, True), PALETTE["ink"])

    draw.ellipse((cx - 82, cy - 82, cx + 82, cy + 82), outline=PALETTE["line"], width=2)
    text_center(draw, (cx - 90, cy - 48, cx + 90, cy - 8), "circular", font(24, True), PALETTE["muted"])
    text_center(draw, (cx - 90, cy - 4, cx + 90, cy + 36), "buffer", font(24, True), PALETTE["muted"])
    draw.arc((cx - 140, cy - 140, cx + 140, cy + 140), start=90, end=210, fill=PALETTE["blue"], width=5)
    draw.arc((cx - 140, cy - 140, cx + 140, cy + 140), start=270, end=390, fill=PALETTE["green"] if retransmit else PALETTE["line"], width=5)
    draw.text((cx - 235, cy + 170), "RV0 history: addr 0-3", font=font(24), fill=PALETTE["blue"])
    if retransmit:
        draw.text((cx - 235, cy + 205), "RV2 now: addr 3-6, addr3 repeats", font=font(24), fill=PALETTE["green"])
    else:
        draw.text((cx - 235, cy + 205), "本次无新 LLR，保持 RV0 结果", font=font(24), fill=PALETTE["muted"])


def draw_buffers(draw: ImageDraw.ImageDraw) -> None:
    draw.text((70, 735), "RV 起点、部分重传与 soft buffer 动作", font=font(28, True), fill=PALETTE["green"])
    draw_ring(draw, 340, 1015, "CB0 / CBG0: 未被 CBGTI 调度", retransmit=False)
    draw_ring(draw, 850, 1015, "CB2 / CBG1: RV2 部分重传", retransmit=True)

    panel = (1160, 785, 1830, 1385)
    draw.rounded_rectangle(panel, radius=14, fill="#FFFDF7", outline="#DFC16A", width=2)
    draw.text((1190, 820), "接收端写回规则", font=font(28, True), fill=PALETTE["amber"])
    rows = [
        ("CBG0 mask=0", "不消费本组 LLR；缓存不变"),
        ("CBG1 mask=1", "CBGFI=1；CB2/CB3 合并"),
        ("new coverage", "addr 4/5/6 首次写入"),
        ("repeat", "addr 3 饱和累加"),
        ("key", "harq/tb/cbg/cb/addr 定位"),
    ]
    y = 880
    for title, body in rows:
        draw.rounded_rectangle((1190, y, 1800, y + 76), radius=8, fill="#FFFFFF", outline=PALETTE["line"], width=1)
        draw.text((1210, y + 20), title, font=font(24, True), fill=PALETTE["ink"])
        draw.text((1420, y + 20), body, font=font(24), fill=PALETTE["muted"])
        y += 88


def draw_footer(draw: ImageDraw.ImageDraw) -> None:
    panel = (70, 1395, 1830, 1710)
    draw.rounded_rectangle(panel, radius=14, fill=PALETTE["purple_l"], outline=PALETTE["purple"], width=2)
    draw.text((100, 1435), "最小调试 dump 与风险检查", font=font(28, True), fill=PALETTE["purple"])
    checks = [
        ("CBGTI/CBGFI", "mask 顺序正确；刷新/合并语义正确"),
        ("RV / k0", "rvidx、BG、Ncb、E 和地址窗口一致"),
        ("CB status", "CB CRC、CBG 状态、未重传 CBG 保持"),
        ("TB CRC", "TB 失败保留缓存，成功释放上下文"),
        ("saturation", "记录 old/new/sat_sum 和饱和次数"),
    ]
    x = 100
    for title, body in checks:
        draw.rounded_rectangle((x, 1500, x + 315, 1668), radius=9, fill="#FFFFFF", outline=PALETTE["line"], width=1)
        text_center(draw, (x + 12, 1512, x + 303, 1550), title, font(24, True), PALETTE["ink"])
        wrapped(draw, (x + 22, 1580), body, font(24), 272, PALETTE["muted"], gap=5)
        x += 340


def main() -> None:
    img = Image.new("RGB", (1900, 1780), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 40), "NR LDPC HARQ Soft Buffer、RV 与 CBG 部分重传", font=font(36, True), fill=PALETTE["ink"])
    wrapped(
        draw,
        (70, 100),
        "目标：把 NR LDPC 的 RV/k0 地址选择、HARQ soft buffer 合并、CBG partial retransmission 放在同一张图里。重点是：CBGTI 只选择哪些 CBG 本次出现；CBGFI 决定重传 CBG 是否能与旧实例合并；RV 决定这些 CBG 内部 CB 的 circular-buffer 起点；soft buffer 负责按地址保持、写入、累加和饱和。",
        font(24),
        1450,
        PALETTE["muted"],
        gap=5,
    )
    draw_hierarchy(draw)
    draw_buffers(draw)
    draw_footer(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
