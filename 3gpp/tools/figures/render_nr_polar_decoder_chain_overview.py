#!/usr/bin/env python3
"""Render the NR Polar receive-side decoding chain overview."""

from __future__ import annotations

import math
from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T10.1_NR_Polar_decoder_chain_overview.png"

PALETTE = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#596879",
    "line": "#CBD5E1",
    "blue": "#2457A6",
    "green": "#2D8F5D",
    "gold": "#B7791F",
    "purple": "#7457A6",
    "red": "#C64B59",
    "llr": "#EAF6FF",
    "rate": "#F2F7EA",
    "decode": "#FFF4D8",
    "crc": "#F6ECFF",
    "ctrl": "#FFEDEF",
    "panel": "#F8FAFD",
}



def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def center_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = box[0] + (box[2] - box[0] - w) / 2 - bbox[0]
    y = box[1] + (box[3] - box[1] - h) / 2 - bbox[1]
    draw.text((x, y), text, font=fnt, fill=fill)


def wrap_draw(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_chars: int,
    line_gap: int = 6,
) -> int:
    x, y = xy
    for paragraph in text.split("\n"):
        for line in textwrap.wrap(paragraph, width=max_chars, break_long_words=False):
            draw.text((x, y), line, font=fnt, fill=fill)
            y += fnt.size + line_gap
        y += line_gap
    return y


def node(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    fill: str,
    stripe: str,
) -> None:
    draw.rounded_rectangle(box, radius=12, fill=fill, outline=PALETTE["line"], width=2)
    draw.rounded_rectangle((box[0], box[1], box[2], box[1] + 12), radius=12, fill=stripe, outline=stripe)
    center_text(draw, (box[0] + 8, box[1] + 22, box[2] - 8, box[1] + 66), title, font(24, True), PALETTE["ink"])
    wrap_draw(draw, (box[0] + 18, box[1] + 84), body, font(24), PALETTE["muted"], 12, line_gap=5)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#61758A") -> None:
    sx, sy = start
    ex, ey = end
    length = math.hypot(ex - sx, ey - sy)
    if length == 0:
        return
    ux, uy = (ex - sx) / length, (ey - sy) / length
    px, py = -uy, ux
    head_len, head_w = 15, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line((sx, sy, *line_end), fill=color, width=4)
    pts = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=color)


def tag(draw: ImageDraw.ImageDraw, x: int, y: int, label: str, fill: str) -> int:
    fnt = font(24, True)
    w, h = text_size(draw, label, fnt)
    pad_x, pad_y = 24, 10
    box = (x, y, x + w + pad_x * 2, y + h + pad_y * 2)
    draw.rounded_rectangle(box, radius=9, fill=fill, outline=fill)
    center_text(draw, box, label, fnt, "#FFFFFF")
    return box[2] + 10


def main() -> None:
    img = Image.new("RGB", (2200, 1520), PALETTE["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "NR Polar 控制信息接收侧译码链路总览", font=font(36, True), fill=PALETTE["ink"])
    wrap_draw(
        draw,
        (70, 96),
        "读图顺序从左到右：解调器给出控制信道 LLR；接收端恢复 Polar 码字位置；SC/SCL 生成候选路径；CRC 辅助选择最终控制比特。UCI 与 DCI 共用 Polar 主链路，但 CRC、RNTI 和上下文字段不同。",
        font(24),
        PALETTE["muted"],
        78,
        line_gap=5,
    )

    boxes = []
    x, y, w, h, gap = 70, 210, 290, 230, 44
    nodes = [
        ("Demapper LLR", "PUCCH/PUSCH/PDCCH 解调后软信息", PALETTE["llr"], PALETTE["blue"]),
        ("Rate recovery", "反速率匹配、反交织、恢复 N 位码字 LLR", PALETTE["rate"], PALETTE["green"]),
        ("Polar decoder", "SC 或 SCL 树遍历；使用 frozen mask", PALETTE["decode"], PALETTE["gold"]),
        ("Path list", "多条候选路径、PM、partial sums", "#FFF7E8", PALETTE["gold"]),
        ("CRC aided select", "CRC 过滤路径；DCI 还涉及 RNTI", PALETTE["crc"], PALETTE["purple"]),
        ("Control bits", "输出 UCI 或 DCI payload 与状态", PALETTE["ctrl"], PALETTE["red"]),
    ]
    for item in nodes:
        box = (x, y, x + w, y + h)
        node(draw, box, *item)
        boxes.append(box)
        x += w + gap
    for left, right in zip(boxes, boxes[1:]):
        arrow(draw, (left[2], (left[1] + left[3]) // 2), (right[0], (right[1] + right[3]) // 2))

    band = (70, 500, 2130, 840)
    draw.rounded_rectangle(band, radius=16, fill=PALETTE["panel"], outline=PALETTE["line"], width=2)
    draw.text((100, 540), "UCI 与 DCI 的共同主链路和差异字段", font=font(28, True), fill=PALETTE["ink"])
    rows = [
        ("UCI on PUCCH", "TS 38.212 §6.3.1", "可能使用 6/11 bit CRC；E 来自 PUCCH 资源与 UCI 类型"),
        ("UCI on PUSCH", "TS 38.212 §6.3.2", "复用到 PUSCH；仍按 UCI Polar 链路编码与速率匹配"),
        ("DCI on PDCCH", "TS 38.212 §7.3", "24 bit CRC，CRC parity bits 与对应 RNTI 相关"),
        ("General Polar", "TS 38.212 §5.2.1/§5.3.1/§5.4.1", "分段/CRC、Polar 编码、速率匹配的通用规则"),
    ]
    yrow = 615
    for label, anchor, note in rows:
        draw.text((105, yrow), label, font=font(24, True), fill=PALETTE["blue"])
        draw.text((470, yrow), anchor, font=font(24), fill=PALETTE["ink"])
        wrap_draw(draw, (940, yrow - 2), note, font(24), PALETTE["muted"], 38, line_gap=4)
        yrow += 58

    example = (70, 900, 1070, 1380)
    draw.rounded_rectangle(example, radius=16, fill="#FFFDF6", outline="#E4D18A", width=2)
    draw.text((100, 945), "小型控制块流程例子", font=font(28, True), fill=PALETTE["ink"])
    wrap_draw(
        draw,
        (100, 1000),
        "假设一个教学 DCI 候选经过速率恢复得到 N=8 个 LLR。SCL 保留 L=2 条路径，最终不是简单选择 PM 最优路径，而是先检查路径 CRC/RNTI 边界，再在通过者中选 PM 最优。",
        font(24),
        PALETTE["muted"],
        42,
    )
    x = 105
    ytag = 1180
    for label, color in [
        ("N=8 LLR", PALETTE["blue"]),
        ("frozen mask", PALETTE["green"]),
        ("L=2 paths", PALETTE["gold"]),
        ("CRC check", PALETTE["purple"]),
        ("payload", PALETTE["red"]),
    ]:
        x = tag(draw, x, ytag, label, color)
        if x > 800:
            x = 105
            ytag += 64

    desc = (1130, 900, 2130, 1380)
    draw.rounded_rectangle(desc, radius=16, fill="#F7FBFF", outline="#B9D2EA", width=2)
    draw.text((1160, 945), "最小 Polar decoder descriptor", font=font(28, True), fill=PALETTE["ink"])
    wrap_draw(
        draw,
        (1160, 1000),
        "这些字段共同决定接收端反操作和路径选择。缺少任一字段，错误常表现为 CRC fail、盲检误通过或路径列表全部淘汰。",
        font(24),
        PALETTE["muted"],
        42,
    )
    x = 1165
    ytag = 1165
    for label, color in [
        ("A/K/E/N", PALETTE["blue"]),
        ("CRC len", PALETTE["purple"]),
        ("IB/IL flag", PALETTE["green"]),
        ("RNTI", PALETTE["red"]),
        ("L", PALETTE["gold"]),
        ("UCI/DCI", "#728399"),
        ("info set", PALETTE["green"]),
        ("frozen set", PALETTE["blue"]),
    ]:
        x = tag(draw, x, ytag, label, color)
        if x > 1935:
            x = 1165
            ytag += 64

    wrap_draw(
        draw,
        (70, 1440),
        "工程检查点：LLR 顺序、E/N/K、interleaver flag、frozen mask、path metric 方向、CRC/RNTI 边界、最终 selector。",
        font(24, True),
        PALETTE["red"],
        70,
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
