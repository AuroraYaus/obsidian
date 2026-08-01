#!/usr/bin/env python3
"""@file render_nr_polar_channel_polarization.py
@brief 渲染 N=4 Polar 极化变换玩具示例图，展示蝶形结构、frozen/information mask 和接收端 mask 语义。
@date 2025
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T10.2_NR_Polar_N4_transform_frozen_mask.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#596879",
    "line": "#BFCBDA",
    "blue": "#2457A6",
    "green": "#2D8F5D",
    "gold": "#B7791F",
    "red": "#C64B59",
    "panel": "#F8FAFD",
    "frozen": "#EAF6FF",
    "info": "#F2F7EA",
}



def center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    """@brief 在矩形区域内居中绘制文本，使用 anchor="mm" 精确居中。
    @param draw PIL ImageDraw 绘制上下文
    @param box 目标矩形区域 (x0, y0, x1, y1)
    @param text 要绘制的文本
    @param fnt PIL 字体对象
    @param fill 文本颜色
    @return None
    """
    cx = (box[0] + box[2]) / 2
    cy = (box[1] + box[3]) / 2
    draw.text((cx, cy), text, font=fnt, fill=fill, anchor="mm")


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    """@brief 按单词边界和指定宽度对文本换行，返回分行列表。
    @param draw PIL ImageDraw 绘制上下文
    @param text 需要换行的文本
    @param fnt PIL 字体对象
    @param width 文字最大宽度（像素）
    @return 换行后的字符串列表
    @note 换行在单词边界处执行，不在单词内部断开。
    """
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill: str, width: int, gap: int = 6) -> None:
    """@brief 在指定宽度内自动换行绘制文本。
    @param draw PIL ImageDraw 绘制上下文
    @param xy 起始左上角坐标 (x, y)
    @param text 需要换行的长文本
    @param fnt PIL 字体对象
    @param fill 文本颜色
    @param width 文字最大宽度（像素）
    @param gap 行间距（像素），默认 6
    @return None
    """
    x, y = xy
    for line in wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += draw.textbbox((0, 0), line, font=fnt)[3] + gap


def node(draw: ImageDraw.ImageDraw, x: int, y: int, label: str, fill: str) -> tuple[int, int, int, int]:
    """@brief 在指定中心坐标绘制自适应大小的圆角节点框，用于 Polar 蝶形图中的输入/输出位节点。
    @param draw PIL ImageDraw 绘制上下文
    @param x 节点中心 x 坐标
    @param y 节点中心 y 坐标
    @param label 节点内显示的标签文字（如 "u0=0", "x0"）
    @param fill 节点填充色，frozen 位用蓝色、information 位用绿色
    @return 节点的外接矩形 (x0, y0, x1, y1)，用于后续连线计算
    @note 框的宽度和高度根据文字尺寸自适应调整，椭圆形圆角。
    """
    f = font(24, True)
    text_box = draw.textbbox((0, 0), label, font=f)
    text_w = text_box[2] - text_box[0]
    text_h = text_box[3] - text_box[1]
    pad_x = 24
    pad_y = 18
    half_w = max(34, text_w // 2 + pad_x)
    half_h = max(28, text_h // 2 + pad_y)
    box = (x - half_w, y - half_h, x + half_w, y + half_h)
    draw.rounded_rectangle(box, radius=half_h, fill=fill, outline=COL["line"], width=2)
    center(draw, box, label, f, COL["ink"])
    return box


def xor(draw: ImageDraw.ImageDraw, x: int, y: int) -> tuple[int, int, int, int]:
    """@brief 在指定坐标绘制 XOR（异或）运算符号，用于 Polar 蝶形图中的模二加节点。
    @param draw PIL ImageDraw 绘制上下文
    @param x 符号中心 x 坐标
    @param y 符号中心 y 坐标
    @return 符号的外接矩形 (x0, y0, x1, y1)，用于连线计算
    @note 符号由圆形边框和内部的加号（十字线）组成，圆形半径 19px。
    """
    r = 19
    draw.ellipse((x - r, y - r, x + r, y + r), fill="#FFFFFF", outline=COL["blue"], width=3)
    draw.line((x - r + 5, y, x + r - 5, y), fill=COL["blue"], width=2)
    draw.line((x, y - r + 5, x, y + r - 5), fill=COL["blue"], width=2)
    return (x - r, y - r, x + r, y + r)


def arrow(draw: ImageDraw.ImageDraw, a: tuple[int, int], b: tuple[int, int], color: str = "#61758A") -> None:
    """@brief 绘制带箭头线段，连接蝶形图中的 XOR 节点和输出节点。
    @param draw PIL ImageDraw 绘制上下文
    @param a 箭头起点坐标 (x, y)
    @param b 箭头终点坐标 (x, y)
    @param color 线条和箭头填充颜色，默认 "#61758A"
    @return None
    @note 箭杆线宽 3px，箭头长度 13px、宽度 7px。
    """
    ax, ay = a
    bx, by = b
    length = math.hypot(bx - ax, by - ay)
    if length == 0:
        return
    ux, uy = (bx - ax) / length, (by - ay) / length
    px, py = -uy, ux
    head_len, head_w = 13, 7
    line_end = (bx - ux * head_len, by - uy * head_len)
    draw.line((ax, ay, *line_end), fill=color, width=3)
    pts = [
        (bx, by),
        (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w),
        (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=color)


def right_mid(box: tuple[int, int, int, int]) -> tuple[int, int]:
    """@brief 返回矩形右边框中点坐标，用于从节点右侧引出连线。
    @param box 矩形区域 (x0, y0, x1, y1)
    @return 右边框中点 (x1, (y0+y1)//2)
    """
    return (box[2], (box[1] + box[3]) // 2)


def left_mid(box: tuple[int, int, int, int]) -> tuple[int, int]:
    """@brief 返回矩形左边框中点坐标，用于连接到节点左侧。
    @param box 矩形区域 (x0, y0, x1, y1)
    @return 左边框中点 (x0, (y0+y1)//2)
    """
    return (box[0], (box[1] + box[3]) // 2)


def tag(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fill: str) -> int:
    """@brief 绘制彩色标签徽章（圆角矩形+白色文字），返回下一个标签的起始 x 坐标用于水平链式排列。
    @param draw PIL ImageDraw 绘制上下文
    @param x 标签左上角 x 坐标
    @param y 标签左上角 y 坐标
    @param text 标签文字（白色绘制）
    @param fill 标签背景色
    @return 下一个标签应放置的 x 坐标（当前标签右边界+10px）
    @note 用于排列 frozen set、information set 等集合标签。
    """
    f = font(24, True)
    b = draw.textbbox((0, 0), text, font=f)
    w = b[2] - b[0] + 28
    box = (x, y, x + w, y + 46)
    draw.rounded_rectangle(box, radius=8, fill=fill, outline=fill)
    center(draw, box, text, f, "#FFFFFF")
    return x + w + 10


def main() -> None:
    """@brief 脚本入口：生成 N=4 Polar 极化变换与 frozen mask 教学图 T10.2_NR_Polar_N4_transform_frozen_mask.png。
    @note 图中包含两部分：
    - 上部：N=4 Polar 蝶形图，展示 u0-u3 输入经异或扩散到 x0-x3 输出的过程，蓝色=frozen 位，绿色=information 位。
    - 下部：接收端 mask 语义面板，展示 frozen set F={0,1}、information set I={2,3} 的互补关系。
    关键教学点：frozen 位是译码树上的已知约束，不是 punctured 也不是低可靠 LLR。
    @see render_nr_polar_decoder_chain_overview.py Polar 译码链路总览
    """
    img = Image.new("RGB", (1900, 1220), COL["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "N=4 Polar 极化变换与 frozen mask", font=font(34, True), fill=COL["ink"])
    draw.text((70, 96), "左侧是编码前位置 u0-u3；右侧是编码输出 x0-x3。蓝色位置为 frozen，绿色位置为 information。", font=font(24), fill=COL["muted"])

    panel = (70, 160, 1830, 675)
    draw.rounded_rectangle(panel, radius=16, fill=COL["panel"], outline=COL["line"], width=2)
    draw.text((100, 180), "蝶形直觉：信息位经过异或扩散到多个输出位置", font=font(25, True), fill=COL["ink"])

    ys = [305, 395, 485, 575]
    left_x, mid_x, right_x = 190, 760, 1360
    labels = ["u0=0", "u1=0", "u2=a", "u3=b"]
    fills = [COL["frozen"], COL["frozen"], COL["info"], COL["info"]]
    left_nodes = [node(draw, left_x, y, label, fill) for y, label, fill in zip(ys, labels, fills)]
    right_nodes = [node(draw, right_x, y, label, "#FFF4D8") for y, label in zip(ys, ["x0", "x1", "x2", "x3"])]

    # Lines matching G4 columns: x0 gets all inputs; x1 gets u1,u3; x2 gets u2,u3; x3 gets u3.
    xors = [(mid_x, ys[0]), (mid_x, ys[1]), (mid_x, ys[2]), (mid_x, ys[3])]
    xor_nodes = [xor(draw, *p) for p in xors]
    connections = {
        0: [0, 1, 2, 3],
        1: [1, 3],
        2: [2, 3],
        3: [3],
    }
    for out_i, in_is in connections.items():
        ox, oy = xors[out_i]
        xor_box = xor_nodes[out_i]
        for in_i in in_is:
            draw.line((right_mid(left_nodes[in_i]), left_mid(xor_box)), fill=COL["line"], width=2)
        arrow(draw, right_mid(xor_box), left_mid(right_nodes[out_i]))

    equations = [
        "x0 = u0 ⊕ u1 ⊕ u2 ⊕ u3 = a ⊕ b",
        "x1 = u1 ⊕ u3 = b",
        "x2 = u2 ⊕ u3 = a ⊕ b",
        "x3 = u3 = b",
    ]
    y = 275
    for eq in equations:
        draw.text((1450, y), eq, font=font(24), fill=COL["muted"])
        y += 66

    bottom = (70, 735, 1830, 1110)
    panel_to_bottom_gap = bottom[1] - panel[3]
    bottom_margin = 1220 - bottom[3]
    assert panel_to_bottom_gap >= 50
    assert bottom_margin >= 80
    draw.rounded_rectangle(bottom, radius=16, fill="#FFFDF6", outline="#E1CC7B", width=2)
    draw.text((100, 670), "接收端 mask 语义", font=font(25, True), fill=COL["ink"])
    draw_wrapped(
        draw,
        (100, 790),
        "frozen set 和 information set 必须互补。frozen 位不是 punctured，也不是低可靠 LLR；它是译码树上的已知约束。",
        font(24),
        COL["muted"],
        1660,
    )
    x = 105
    for label, fill in [
        ("F = {0,1}", COL["blue"]),
        ("I = {2,3}", COL["green"]),
        ("u0,u1 强制为 0", COL["blue"]),
        ("u2,u3 承载 a,b", COL["green"]),
        ("F ∩ I = 空集", COL["gold"]),
        ("F ∪ I = {0,1,2,3}", COL["gold"]),
    ]:
        x = tag(draw, x, 880, label, fill)
        if x > 1540:
            x = 105
    draw_wrapped(
        draw,
        (100, 1010),
        "工程检查点：info/frozen mask 方向、0-based index、bit-reversal 边界、frozen 与 rate-matching punctured 的区别。",
        font(24, True),
        COL["red"],
        1660,
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
