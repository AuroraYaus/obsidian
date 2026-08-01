#!/usr/bin/env python3
"""@file render_nr_polar_decoder_chain_overview.py
@brief 渲染 NR Polar 接收侧译码链路总览图，涵盖 UCI/DCI 共用主链路、descriptor 字段和工程检查点。
@date 2025
"""

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
    """@brief 获取文本在指定字体下的像素宽度和高度。
    @param draw PIL ImageDraw 绘制上下文
    @param text 要测量的文本
    @param fnt PIL 字体对象
    @return (宽度, 高度) 像素元组
    """
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def center_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
) -> None:
    """@brief 在矩形区域内居中绘制文本，修正 bbox 原点偏移以确保精确对齐。
    @param draw PIL ImageDraw 绘制上下文
    @param box 目标矩形区域 (x0, y0, x1, y1)
    @param text 要绘制的文本
    @param fnt PIL 字体对象
    @param fill 文本颜色
    @return None
    """
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
    """@brief 按最大字符数换行绘制文本，支持段落（\\n）分隔，返回绘制结束后的 y 坐标。
    @param draw PIL ImageDraw 绘制上下文
    @param xy 起始左上角坐标 (x, y)
    @param text 需要换行的文本（可含 \\n 段落分隔）
    @param fnt PIL 字体对象
    @param fill 文本颜色
    @param max_chars 每行最大字符数
    @param line_gap 行间距（像素），默认 6
    @return 绘制结束后的 y 坐标
    @note 使用 textwrap.wrap 按字符宽度换行，段落间额外添加一个 line_gap。
    """
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
    """@brief 绘制带彩色顶部条纹的流程节点框，用于展示译码链路中的处理步骤。
    @param draw PIL ImageDraw 绘制上下文
    @param box 矩形区域 (x0, y0, x1, y1)
    @param title 节点标题（24px 粗体）
    @param body 节点正文（24px 常规，按字符宽度自动换行）
    @param fill 框内填充色
    @param stripe 顶部 12px 彩色条纹颜色
    @return None
    """
    draw.rounded_rectangle(box, radius=12, fill=fill, outline=PALETTE["line"], width=2)
    draw.rounded_rectangle((box[0], box[1], box[2], box[1] + 12), radius=12, fill=stripe, outline=stripe)
    center_text(draw, (box[0] + 8, box[1] + 22, box[2] - 8, box[1] + 66), title, font(24, True), PALETTE["ink"])
    wrap_draw(draw, (box[0] + 18, box[1] + 84), body, font(24), PALETTE["muted"], 12, line_gap=5)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#61758A") -> None:
    """@brief 绘制带箭头线段，连接流程节点展示译码链路的数据流向。
    @param draw PIL ImageDraw 绘制上下文
    @param start 箭头起点坐标 (x, y)
    @param end 箭头终点坐标 (x, y)
    @param color 线条和箭头填充颜色，默认 "#61758A"
    @return None
    @note 箭杆线宽 4px，箭头长度 15px、宽度 9px。
    """
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
    """@brief 绘制彩色标签徽章（圆角矩形+白色文字），返回下一个标签的起始 x 坐标用于水平链式排列。
    @param draw PIL ImageDraw 绘制上下文
    @param x 标签左上角 x 坐标
    @param y 标签左上角 y 坐标
    @param label 标签文字（白色绘制）
    @param fill 标签背景色
    @return 下一个标签应放置的 x 坐标（当前标签右边界+10px）
    @note 用于排列 descriptor 字段标签和流程步骤标签。
    """
    fnt = font(24, True)
    w, h = text_size(draw, label, fnt)
    pad_x, pad_y = 24, 10
    box = (x, y, x + w + pad_x * 2, y + h + pad_y * 2)
    draw.rounded_rectangle(box, radius=9, fill=fill, outline=fill)
    center_text(draw, box, label, fnt, "#FFFFFF")
    return box[2] + 10


def main() -> None:
    """@brief 脚本入口：生成 NR Polar 控制信息接收侧译码链路总览图 T10.1_NR_Polar_decoder_chain_overview.png。
    @note 图中包含四个主区域：
    - 顶部：六节点水平链路（Demapper LLR -> Rate recovery -> Polar decoder -> Path list -> CRC aided select -> Control bits）。
    - 中部：UCI/DCI 共同主链路和差异字段对照表。
    - 左下：小型控制块流程例子教学面板。
    - 右下：最小 Polar decoder descriptor 字段标签集。
    关键教学点：UCI 与 DCI 共用 Polar 主链路，但 CRC、RNTI 和上下文字段不同。
    @see render_nr_polar_ca_scl_selector.py CA-SCL 最终路径选择图
    @see render_nr_polar_channel_polarization.py N=4 Polar 极化变换图
    """
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
