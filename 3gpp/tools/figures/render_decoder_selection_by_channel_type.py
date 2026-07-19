#!/usr/bin/env python3
"""Render LTE/NR decoder selection by channel and information type."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T11.5_decoder_selection_by_channel_type.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#152033",
    "muted": "#5C6978",
    "line": "#AAB7C8",
    "lte": "#B65B2E",
    "lte_l": "#FFF0E6",
    "nr": "#236B5A",
    "nr_l": "#E8F6EF",
    "ctrl": "#2457A6",
    "ctrl_l": "#EAF1FB",
    "warn": "#B9841A",
    "warn_l": "#FFF6DD",
    "panel": "#F6F8FB",
    "desc": "#6E55A4",
    "desc_l": "#F1EDFF",
}



def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    cur = ""
    for ch in text:
        if ch == "\n":
            if cur:
                tokens.append(cur)
                cur = ""
            tokens.append("\n")
        elif ch.isascii() and (ch.isalnum() or ch in "/_-+.[]=()"):
            cur += ch
        else:
            if cur:
                tokens.append(cur)
                cur = ""
            tokens.append(" " if ch.isspace() else ch)
    if cur:
        tokens.append(cur)
    return tokens


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    cur = ""
    for tok in tokenize(text):
        if tok == "\n":
            if cur.strip():
                lines.append(cur.strip())
            cur = ""
            continue
        nxt = cur + tok
        if draw.textlength(nxt, font=fnt) <= width or not cur.strip():
            cur = nxt
        else:
            lines.append(cur.strip())
            cur = tok
    if cur.strip():
        lines.append(cur.strip())
    return lines


def text_box_height(draw: ImageDraw.ImageDraw, lines: list[str], fnt: ImageFont.FreeTypeFont, gap: int) -> int:
    heights = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=fnt)
        heights.append(bbox[3] - bbox[1])
    return sum(heights) + gap * max(len(lines) - 1, 0)


def draw_centered(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str | list[str],
    size: int,
    color: str = COL["ink"],
    bold: bool = True,
    gap: int = 7,
    pad: int = 24,
) -> None:
    fnt = font(size, bold)
    raw = text if isinstance(text, list) else [text]
    lines: list[str] = []
    for item in raw:
        lines.extend(wrap(draw, item, fnt, max(box[2] - box[0] - 2 * pad, 80)))
    total = text_box_height(draw, lines, fnt, gap)
    x = (box[0] + box[2]) / 2
    y = (box[1] + box[3] - total) / 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=fnt)
        h = bbox[3] - bbox[1]
        draw.text((x, y + h / 2), line, font=fnt, fill=color, anchor="mm")
        y += h + gap


def center(box: tuple[int, int, int, int]) -> tuple[float, float]:
    return ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2)


def boundary_point(box: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    cx, cy = center(box)
    dx, dy = toward[0] - cx, toward[1] - cy
    if abs(dx) < 1e-6 and abs(dy) < 1e-6:
        return cx, cy
    half_w = max((box[2] - box[0]) / 2, 1)
    half_h = max((box[3] - box[1]) / 2, 1)
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return cx + dx / scale, cy + dy / scale


def arrow(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str) -> None:
    x0, y0 = boundary_point(src, center(dst))
    x1, y1 = boundary_point(dst, center(src))
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    head_len, head_w = 18, 10
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    draw.line(((x0, y0), line_end), fill=color, width=4)
    angle = math.atan2(y1 - y0, x1 - x0)
    bx = x1 - head_len * math.cos(angle)
    by = y1 - head_len * math.sin(angle)
    px = head_w * math.sin(angle)
    py = -head_w * math.cos(angle)
    draw.polygon([(x1, y1), (bx + px, by + py), (bx - px, by - py)], fill=color)


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str, radius: int = 18, width: int = 2) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def node(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str | list[str],
    fill: str,
    outline: str,
    size: int = 24,
) -> tuple[int, int, int, int]:
    rounded(draw, box, fill, outline, 18, 2)
    draw_centered(draw, box, text, size=size, bold=False)
    return box


def draw_mapping_table(draw: ImageDraw.ImageDraw, x: int, y: int) -> int:
    draw.text((x, y), "协议映射速查表", font=font(34, True), fill=COL["ink"])
    y += 58
    cols = [190, 330, 250, 320, 600]
    rows = [
        ["制式", "信道 / 信息类型", "译码器家族", "协议锚点", "接收端判定要点"],
        ["LTE", "DL-SCH / UL-SCH", "Turbo", "TS 36.212 §5.1.3, §5.2.2.3", "数据 TB/CB 主线；HARQ soft buffer 与 Turbo rate recovery 后进入 Turbo core"],
        ["LTE", "DCI / UCI 等控制", "TBCC / Block / Repetition", "TS 36.212 Table 5.1.3-2", "不是 NR Polar；不要用 Polar 解释 LTE 控制译码"],
        ["NR", "DL-SCH / UL-SCH / PCH", "LDPC", "TS 38.212 Table 5.3-1, §6.2.4", "数据 TB/CB 主线；BG、Zc、CBG、HARQ context 决定 LDPC descriptor"],
        ["NR", "DCI", "Polar", "TS 38.212 Table 5.3-2, §7.3.3", "PDCCH 盲检；CRC/RNTI 背景与 CA-SCL final selector 绑定"],
        ["NR", "UCI", "Polar / small-block", "TS 38.212 §6.3.1, §6.3.2", "PUCCH/PUSCH 皆可能承载 UCI；小负载可能走 small-block，不等于 LDPC"],
    ]
    row_h = [70, 108, 108, 124, 108, 124]
    for r, row in enumerate(rows):
        x0 = x
        fill = COL["panel"] if r == 0 else "#FFFFFF"
        for c, cell in enumerate(row):
            box = (x0, y, x0 + cols[c], y + row_h[r])
            draw.rectangle(box, fill=fill, outline=COL["line"], width=2)
            size = 24
            draw_centered(draw, box, cell, size=size, bold=(r == 0), gap=5, pad=14)
            x0 += cols[c]
        y += row_h[r]
    return y


def draw_decision_flow(draw: ImageDraw.ImageDraw, y: int) -> int:
    draw.text((90, y), "接收端 descriptor 选择逻辑", font=font(34, True), fill=COL["ink"])
    y += 62
    boxes = {
        "desc": node(draw, (90, y + 75, 395, y + 205), ["descriptor", "rat, channel_type", "payload_type"], COL["desc_l"], COL["desc"], 24),
        "lte": node(draw, (465, y, 770, y + 105), "RAT = LTE", COL["lte_l"], COL["lte"], 24),
        "nr": node(draw, (465, y + 170, 770, y + 275), "RAT = NR", COL["nr_l"], COL["nr"], 24),
        "lte_data": node(draw, (850, y, 1185, y + 112), "TrCH = DL-SCH / UL-SCH", "#FFFFFF", COL["lte"], 24),
        "lte_ctrl": node(draw, (850, y + 128, 1185, y + 240), "control info", "#FFFFFF", COL["lte"], 24),
        "nr_ctrl": node(draw, (850, y + 300, 1185, y + 412), "UCI / DCI", "#FFFFFF", COL["ctrl"], 24),
        "nr_data": node(draw, (850, y + 425, 1185, y + 545), "TrCH = DL-SCH / UL-SCH", "#FFFFFF", COL["nr"], 24),
        "turbo": node(draw, (1265, y, 1690, y + 112), ["decoder_type = Turbo", "crc_type = TB/CB CRC"], COL["lte_l"], COL["lte"], 24),
        "tbcc": node(draw, (1265, y + 128, 1690, y + 240), ["decoder_type = TBCC / block", "LTE control context"], COL["warn_l"], COL["warn"], 24),
        "polar": node(draw, (1265, y + 300, 1690, y + 412), ["decoder_type = Polar / small-block", "control_context required"], COL["ctrl_l"], COL["ctrl"], 24),
        "ldpc": node(draw, (1265, y + 425, 1690, y + 545), ["decoder_type = LDPC", "harq_context required"], COL["nr_l"], COL["nr"], 24),
    }
    for src, dst, color in [
        ("desc", "lte", COL["lte"]),
        ("desc", "nr", COL["nr"]),
        ("lte", "lte_data", COL["lte"]),
        ("lte", "lte_ctrl", COL["lte"]),
        ("nr", "nr_data", COL["nr"]),
        ("nr", "nr_ctrl", COL["ctrl"]),
        ("lte_data", "turbo", COL["lte"]),
        ("lte_ctrl", "tbcc", COL["warn"]),
        ("nr_data", "ldpc", COL["nr"]),
        ("nr_ctrl", "polar", COL["ctrl"]),
    ]:
        arrow(draw, boxes[src], boxes[dst], color)
    return y + 570


def draw_edge_cases(draw: ImageDraw.ImageDraw, y: int) -> int:
    draw.text((90, y), "边界情况与工程检测点", font=font(34, True), fill=COL["ink"])
    y += 58
    items = [
        ("小 payload", "NR UCI 可能 small-block；不要因为是控制信息就无条件进入 Polar SCL。", COL["warn"], COL["warn_l"]),
        ("UCI on PUSCH", "PUSCH 可同时有 UL-SCH 和 UCI；UL-SCH 数据仍进 LDPC，UCI 按控制分支处理。", COL["ctrl"], COL["ctrl_l"]),
        ("DCI CRC/RNTI", "DCI 不只是 payload CRC；CRC parity 与 RNTI 背景绑定，影响盲检和 final selector。", COL["ctrl"], COL["ctrl_l"]),
        ("NR CBG", "CBG 改变 LDPC HARQ 软缓存粒度；数据主线仍是 LDPC。", COL["nr"], COL["nr_l"]),
    ]
    w, h, gap = 395, 145, 34
    for i, (title, body, color, fill) in enumerate(items):
        x = 90 + i * (w + gap)
        box = (x, y, x + w, y + h)
        rounded(draw, box, fill, color, 18, 2)
        draw_centered(draw, (x + 18, y + 14, x + w - 18, y + 54), title, 24, color, True, 5, 8)
        draw_centered(draw, (x + 18, y + 58, x + w - 18, y + h - 14), body, 24, COL["ink"], False, 5, 8)
    return y + h


def edge_check(img: Image.Image) -> dict[str, int]:
    pix = img.load()
    w, h = img.size

    def nonwhite(points: list[tuple[int, int]]) -> int:
        count = 0
        for x, y in points:
            if pix[x, y] != (255, 255, 255):
                count += 1
        return count

    return {
        "top": nonwhite([(x, 0) for x in range(w)]),
        "bottom": nonwhite([(x, h - 1) for x in range(w)]),
        "left": nonwhite([(0, y) for y in range(h)]),
        "right": nonwhite([(w - 1, y) for y in range(h)]),
    }


def main() -> None:
    img = Image.new("RGB", (1900, 2200), COL["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 54), "T11.5 按信道和信息类型选择译码器", font=font(44, True), fill=COL["ink"])
    draw.text(
        (72, 112),
        "协议先决定编码对象，接收端 descriptor 再选择 Turbo、LDPC、Polar 或 LTE 控制类译码器。",
        font=font(24, False),
        fill=COL["muted"],
    )
    y = draw_mapping_table(draw, 90, 175) + 70
    y = draw_decision_flow(draw, y) + 70
    y = draw_edge_cases(draw, y)
    note = (
        "读图顺序：先看协议速查表，再看 descriptor 分支。"
        "工程检测点：每个任务必须同时记录 rat、channel_type、payload_type、decoder_type、crc_type、harq_context 和 control_context。"
    )
    note_box = (90, y + 70, 1810, y + 185)
    rounded(draw, note_box, "#FFFFFF", COL["line"], 18, 2)
    draw_centered(draw, note_box, note, 24, COL["ink"], False, 7, 30)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")
    print(f"IMAGE_EDGE_CHECK {img.size} {edge_check(img)}")


if __name__ == "__main__":
    main()
