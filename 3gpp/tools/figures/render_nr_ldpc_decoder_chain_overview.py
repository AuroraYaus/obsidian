#!/usr/bin/env python3
"""Render the NR LDPC receive-side decoding chain overview."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T8.1_NR_LDPC_decoder_chain_overview.png"

PALETTE = {
    "ink": "#17212F",
    "muted": "#596879",
    "line": "#C9D4DF",
    "bg": "#FFFFFF",
    "llr": "#EAF6FF",
    "recover": "#F2F7EA",
    "core": "#FFF4D8",
    "crc": "#F6ECFF",
    "harq": "#FFEDEF",
    "accent": "#2457A6",
    "green": "#2D8F5D",
    "purple": "#7457A6",
    "red": "#C64B59",
}



def center_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    x = box[0] + ((box[2] - box[0]) - width) / 2 - bbox[0]
    y = box[1] + ((box[3] - box[1]) - height) / 2 - bbox[1]
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill: str, max_width: int, line_gap: int = 6) -> int:
    x, y = xy
    for line in fit_wrap_text(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def draw_node(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, body: str, fill: str, stripe: str) -> None:
    draw.rounded_rectangle(box, radius=14, fill=fill, outline=PALETTE["line"], width=2)
    draw.rounded_rectangle((box[0], box[1], box[2], box[1] + 14), radius=14, fill=stripe, outline=stripe)
    center_text(draw, (box[0] + 10, box[1] + 26, box[2] - 10, box[1] + 62), title, font(24, True), PALETTE["ink"])
    draw_wrapped(draw, (box[0] + 18, box[1] + 76), body, font(24), PALETTE["muted"], box[2] - box[0] - 36, line_gap=5)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#61758A") -> None:
    sx, sy = start
    ex, ey = end
    length = math.hypot(ex - sx, ey - sy)
    if length == 0:
        return
    ux, uy = (ex - sx) / length, (ey - sy) / length
    px, py = -uy, ux
    head_len, head_w = 16, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line((sx, sy, *line_end), fill=color, width=4)
    points = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(points, fill=color)


def tag(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fill: str) -> int:
    fnt = font(24, True)
    bbox = draw.textbbox((0, 0), text, font=fnt)
    width = bbox[2] - bbox[0] + 44
    height = bbox[3] - bbox[1] + 20
    draw.rounded_rectangle((x, y, x + width, y + height), radius=9, fill=fill, outline=fill)
    center_text(draw, (x, y, x + width, y + height), text, fnt, "#FFFFFF")
    return x + width + 10


def draw_two_cb_example(draw: ImageDraw.ImageDraw) -> None:
    top = 870
    box = (70, top, 1770, top + 248)
    draw.rounded_rectangle(box, radius=16, fill="#F8FAFD", outline=PALETTE["line"], width=2)
    draw.text((100, top + 32), "两个码块的接收侧路径示例", font=font(28, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (100, top + 78),
        "TB 先被分成 CB0 和 CB1；接收端分别做速率恢复、LDPC 译码和 CB CRC。两个 CB 都通过后，才按 r=0,1 的顺序拼接并检查 TB CRC。",
        font(24),
        PALETTE["muted"],
        1120,
    )
    x0 = 110
    y0 = top + 162
    x = tag(draw, x0, y0, "CB0 pass", PALETTE["green"])
    x = tag(draw, x, y0, "CB1 pass", PALETTE["green"])
    x = tag(draw, x + 20, y0, "concat r order", PALETTE["accent"])
    x = tag(draw, x + 20, y0, "TB CRC", PALETTE["purple"])
    tag(draw, x + 20, y0, "ACK/NACK", PALETTE["red"])

    draw.text((1290, top + 34), "失败定位入口", font=font(24, True), fill=PALETTE["ink"])
    y = top + 78
    for item in ["速率恢复地址错", "BG/Zc 配置错", "LDPC 不收敛", "CB/TB CRC 边界错"]:
        draw.ellipse((1300, y + 8, 1310, y + 18), fill=PALETTE["red"])
        draw.text((1322, y), item, font=font(24), fill=PALETTE["muted"])
        y += 40


def draw_descriptor(draw: ImageDraw.ImageDraw) -> None:
    top = 1154
    box = (70, top, 1770, top + 230)
    draw.rounded_rectangle(box, radius=16, fill="#FFFDF6", outline="#E0C874", width=2)
    draw.text((100, top + 32), "最小 decoder descriptor v0", font=font(28, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (100, top + 76),
        "这些字段不是同一个协议表里的连续列，而是接收端把 TS 38.212 的编码链路和 TS 38.214 的调度背景汇合成可执行译码任务时必须携带的上下文。",
        font(24),
        PALETTE["muted"],
        860,
    )
    labels = [
        ("BG", PALETTE["accent"]),
        ("Zc", PALETTE["accent"]),
        ("rvidx", PALETTE["red"]),
        ("E", PALETTE["green"]),
        ("Ncb", PALETTE["green"]),
        ("Qm", PALETTE["purple"]),
        ("C", PALETTE["purple"]),
        ("cb_id", "#728399"),
        ("CRC", "#728399"),
        ("HARQ", "#728399"),
        ("CBGTI", PALETTE["red"]),
    ]
    x = 1040
    y = top + 42
    for i, (label, color) in enumerate(labels):
        x = tag(draw, x, y, label, color)
        if i in {4, 8}:
            x = 1040
            y += 46


def main() -> None:
    img = Image.new("RGB", (1970, 1420), PALETTE["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "NR LDPC 接收侧译码链路总览", font=font(40, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (70, 102),
        "读图顺序从左到右：软解调器给出 LLR；接收端先恢复速率匹配前的 LDPC 母码位置，再译码每个 CB；CB 全部通过后拼接 TB，由 TB CRC 决定 HARQ 反馈。",
        font(24),
        PALETTE["muted"],
        1820,
    )

    y = 198
    w = 242
    h = 200
    gap = 30
    nodes = [
        ("Demapper LLR", "来自软解调 LLR，保留软可靠度。", PALETTE["llr"], PALETTE["accent"]),
        ("Rate recovery", "按 RV/E/Ncb/Qm 回填母码环形缓存。", PALETTE["recover"], PALETTE["green"]),
        ("LDPC decoder", "按 BG/Zc 生成 H，迭代更新并查 syndrome。", PALETTE["core"], "#C69220"),
        ("CB CRC", "逐 CB 判断；失败则保留 HARQ 软信息。", PALETTE["crc"], PALETTE["purple"]),
        ("CB concat", "按 CB 序号拼接，不能按完成时间。", "#F0F7F4", PALETTE["green"]),
        ("TB CRC", "整 TB 终检，决定交付边界。", PALETTE["crc"], PALETTE["purple"]),
        ("HARQ/CBG", "输出 ACK/NACK；管理 CBG 重传和 soft buffer。", PALETTE["harq"], PALETTE["red"]),
    ]

    boxes = []
    x = 55
    for title, body, fill, stripe in nodes:
        box = (x, y, x + w, y + h)
        draw_node(draw, box, title, body, fill, stripe)
        boxes.append(box)
        x += w + gap

    for left, right in zip(boxes, boxes[1:]):
        arrow(draw, (left[2], (left[1] + left[3]) // 2), (right[0], (right[1] + right[3]) // 2))

    band = (55, 458, 1910, 824)
    draw.rounded_rectangle(band, radius=16, fill="#F7F9FC", outline=PALETTE["line"], width=2)
    draw.text((100, 492), "协议锚点如何落到接收端动作", font=font(29, True), fill=PALETTE["ink"])
    rows = [
        ("TS 38.212 §5.2.2", "CB segmentation / CB CRC / filler", "确定 C、Kr、CB CRC 和 filler 删除边界"),
        ("TS 38.212 §5.3.2", "LDPC coding / BG / Zc / H", "确定译码器必须使用的校验结构"),
        ("TS 38.212 §5.4.2", "bit selection / interleaving", "确定顺序 LLR 如何回到环形缓存"),
        ("TS 38.212 §6.2 / §7.2", "UL-SCH / DL-SCH 链路", "确定 TB CRC、BG 选择、分段、编码、rate matching、拼接顺序"),
        ("TS 38.214 §5.1.7 / §6.1.5", "CBG and scheduling context", "提供 CBG、CBGTI、MCS/RV/TBS 等译码上下文来源"),
    ]
    x1, x2, x3 = 110, 555, 1025
    yrow = 552
    for anchor, subject, action in rows:
        draw.text((x1, yrow), anchor, font=font(24, True), fill=PALETTE["accent"])
        draw.text((x2, yrow), subject, font=font(24), fill=PALETTE["ink"])
        draw_wrapped(draw, (x3, yrow - 2), action, font(24), PALETTE["muted"], 760, line_gap=4)
        yrow += 54

    draw_two_cb_example(draw)
    draw_descriptor(draw)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
