#!/usr/bin/env python3
""" @file render_ldpc_tanner_syndrome.py
    @brief 渲染 LDPC Tanner 图、syndrome 计算与消息流入口教学图。
    @date 2025
    @note 教学 H=[[1,1,0,1,0,0],[0,1,1,0,1,0],[1,0,1,0,0,1]]，含 GF(2) 手算例子。
    @see render_ldpc_bp_spa_round.py 对应的 SPA 一轮消息传递图
"""

from __future__ import annotations

import math
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T8.4_LDPC_Tanner_syndrome_toy.png"

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
    """ @brief 在矩形内居中绘制单行文本。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 绘制区域。
        @param text 待绘制的单行字符串。
        @param fnt PIL 字体对象。
        @param fill 文字颜色。
        @return 无返回值。
    """
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill: str, width: int) -> int:
    """ @brief 在指定坐标处绘制自动换行的左对齐多行文本。
        @param draw PIL ImageDraw 实例。
        @param xy 起始坐标 (x, y)。
        @param text 待绘制的长文本。
        @param fnt 字体对象。
        @param fill 文字颜色。
        @param width 每行最大像素宽度。
        @return 最后一行的底部 Y 坐标。
    """
    x, y = xy
    current = ""
    lines: list[str] = []
    tokens = re.findall(r"[A-Za-z0-9_./'()+-]+|[ \t]+|.", text)
    for token in tokens:
        candidate = current + token
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= width or not current:
            current = candidate
        else:
            lines.append(current)
            current = token.lstrip()
            while draw.textbbox((0, 0), current, font=fnt)[2] > width and len(current) > 1:
                split = len(current) - 1
                while split > 1 and draw.textbbox((0, 0), current[:split], font=fnt)[2] > width:
                    split -= 1
                lines.append(current[:split])
                current = current[split:]
    if current:
        lines.append(current)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + 7
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str) -> None:
    """ @brief 绘制带三角箭头的直线。
        @param draw PIL ImageDraw 实例。
        @param start 起点 (x, y)。
        @param end 终点 (x, y)。
        @param color CSS 颜色字符串。
        @return 无返回值。
    """
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


def draw_matrix(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制小校验矩阵 H 的格子图：3x6，1 为蓝色填充。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
        @note 行标 c0-c2，列标 v0-v5，每格 56px，含标题与节点间距断言。
    """
    H = [[1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1]]
    x0, y0 = 70, 250
    cell = 56
    title_y = 162
    title_font = font(28, True)
    draw.text((x0, title_y), "小型校验矩阵 H", font=title_font, fill=PALETTE["blue"])
    title_bbox = draw.textbbox((x0, title_y), "小型校验矩阵 H", font=title_font)
    title_to_node_gap = (y0 - 36) - title_bbox[3]
    assert title_to_node_gap >= 8, f"matrix title/header overlap risk: {title_to_node_gap}px"
    for r, row in enumerate(H):
        for c, val in enumerate(row):
            box = (x0 + c * cell, y0 + r * cell, x0 + (c + 1) * cell, y0 + (r + 1) * cell)
            fill = "#EAF3FF" if val else "#F7FAFC"
            draw.rectangle(box, fill=fill, outline=PALETTE["line"], width=2)
            center_text(draw, box, str(val), font(24, True), PALETTE["ink"])
    for c in range(6):
        center_text(draw, (x0 + c * cell, y0 - 36, x0 + (c + 1) * cell, y0 - 6), f"v{c}", font(24, True), PALETTE["muted"])
    for r in range(3):
        center_text(draw, (x0 - 44, y0 + r * cell, x0 - 8, y0 + (r + 1) * cell), f"c{r}", font(24, True), PALETTE["muted"])


def draw_graph(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制 Tanner 图：6 个变量节点（圆）+ 3 个校验节点（方）+ 边。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
        @note 节点间距 88px(VN)/135px(CN)，边来自 H 矩阵的 1 元素。
    """
    H = [[1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1]]
    vx = [500 + i * 88 for i in range(6)]
    vy = 245
    cx = [560 + i * 135 for i in range(3)]
    cy = 505
    draw.text((500, 160), "Tanner 图", font=font(26, True), fill=PALETTE["green"])
    title_bbox = draw.textbbox((500, 160), "Tanner 图", font=font(26, True))
    title_to_node_gap = (vy - 30) - title_bbox[3]
    assert title_to_node_gap >= 16, f"tanner title/node overlap risk: {title_to_node_gap}px"
    for r, row in enumerate(H):
        for c, val in enumerate(row):
            if val:
                draw.line((vx[c], vy + 22, cx[r], cy - 22), fill="#9FB0C3", width=3)
    for i, x in enumerate(vx):
        draw.ellipse((x - 30, vy - 30, x + 30, vy + 30), fill="#EAF3FF", outline=PALETTE["blue"], width=3)
        center_text(draw, (x - 30, vy - 30, x + 30, vy + 30), f"v{i}", font(24, True), PALETTE["ink"])
    for i, x in enumerate(cx):
        draw.rounded_rectangle((x - 38, cy - 30, x + 38, cy + 30), radius=8, fill="#EAF8F1", outline=PALETTE["green"], width=3)
        center_text(draw, (x - 38, cy - 30, x + 38, cy + 30), f"c{i}", font(24, True), PALETTE["ink"])
    draw.text((500, 590), "H 中每个 1 对应一条边：变量节点 vj 连接到校验节点 ci。", font=font(24), fill=PALETTE["muted"])


def draw_syndrome(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制 GF(2) syndrome 手算面板：三条校验方程的逐位异或计算。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
        @note 展示 x=[1,0,1,1,1,0] 通过全部三条校验；翻转 x5 后 s2 非零的反例。
    """
    panel = (70, 690, 1510, 1115)
    draw.rounded_rectangle(panel, radius=18, fill=PALETTE["panel"], outline=PALETTE["line"], width=2)
    draw.text((105, 720), "GF(2) syndrome 手算例子", font=font(28, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (105, 767),
        "取硬判决 x=[1,0,1,1,1,0]。每一行是一条奇偶校验方程；在 GF(2) 中求和就是异或。",
        font(24),
        PALETTE["muted"],
        1180,
    )
    equations = [
        ("s0 = x0 xor x1 xor x3", "1 xor 0 xor 1 = 0", "通过"),
        ("s1 = x1 xor x2 xor x4", "0 xor 1 xor 1 = 0", "通过"),
        ("s2 = x0 xor x2 xor x5", "1 xor 1 xor 0 = 0", "通过"),
    ]
    y = 845
    for eq, calc, status in equations:
        draw.text((120, y), eq, font=font(24, True), fill=PALETTE["blue"])
        draw.text((540, y), calc, font=font(24), fill=PALETTE["ink"])
        draw.rounded_rectangle((920, y - 4, 1040, y + 40), radius=8, fill=PALETTE["green"], outline=PALETTE["green"])
        center_text(draw, (920, y - 4, 1040, y + 40), status, font(24, True), "#FFFFFF")
        y += 60
    end_y = draw_wrapped(
        draw,
        (105, 1035),
        "若翻转 x5 得到 x'=[1,0,1,1,1,1]，第三行变成 1 xor 1 xor 1 = 1，syndrome 非零，说明当前硬判决不满足 LDPC 校验。",
        font(24),
        PALETTE["red"],
        1250,
    )
    bottom_margin = panel[3] - end_y
    assert bottom_margin >= 24, f"syndrome panel bottom text overflow risk: {bottom_margin}px"


def draw_message_flow(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制右侧消息流入口面板：四步消息传递流程说明。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
        @note 步骤：VN 发 LLR -> CN 生成外信息 -> VN 汇总 -> hard decision + 早停。
    """
    panel = (1110, 210, 1530, 650)
    draw.rounded_rectangle(panel, radius=18, fill="#FFFDF6", outline="#E2CD7A", width=2)
    draw.text((1140, 240), "一轮消息流入口", font=font(28, True), fill=PALETTE["ink"])
    notes = [
        "1. 变量节点先带着 channel LLR 给相邻校验节点。",
        "2. 校验节点根据其他相邻变量的消息生成外信息。",
        "3. 变量节点汇总 channel LLR 和校验消息得到 posterior LLR。",
        "4. hard decision 后算 syndrome 并在全零时早停。",
    ]
    y = 295
    for note in notes:
        y = draw_wrapped(draw, (1140, y), note, font(24), PALETTE["muted"], 355) + 14
    bottom_margin = panel[3] - y
    assert bottom_margin >= 24, f"message-flow panel text overflow risk: {bottom_margin}px"


def main() -> None:
    """ @brief 脚本入口：生成 T8.4 LDPC Tanner 图、syndrome 与消息流教学图。
        @return 无返回值。
        @note 产出 1600x1180 PNG：H 矩阵 + Tanner 图 + 消息流说明 + syndrome 手算例子。
    """
    img = Image.new("RGB", (1600, 1180), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "LDPC Tanner 图、syndrome 与消息流", font=font(40, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (70, 102),
        "小校验矩阵用于教学，不是 NR conformance vector。真实 NR 的 H 由 TS 38.212 的 BG、Zc、iLS 和 shift table 生成，但 Tanner 图和 syndrome 的解释完全相同。",
        font(24),
        PALETTE["muted"],
        1400,
    )
    draw_matrix(draw)
    draw_graph(draw)
    draw_message_flow(draw)
    draw_syndrome(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
