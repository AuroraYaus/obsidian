#!/usr/bin/env python3
""" @file render_ldpc_bp_spa_round.py
    @brief 渲染 LDPC BP/SPA 单轮消息传递教学图：Tanner 图 + SPA 公式 + 数值结果。
    @date 2025
    @note 教学 H=[[1,1,1,0],[0,1,1,1]]，channel LLR=[2.0,-1.0,0.7,1.2]。
    @see render_ldpc_tanner_syndrome.py 对应的 Tanner 图和 syndrome 教学图
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T8.5_LDPC_BP_SPA_one_round.png"

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


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill: str, width: int, gap: int = 6) -> int:
    """ @brief 在指定坐标处绘制自动换行的左对齐多行文本。
        @param draw PIL ImageDraw 实例。
        @param xy 起始坐标 (x, y)。
        @param text 待绘制的长文本。
        @param fnt 字体对象。
        @param fill 文字颜色。
        @param width 每行最大像素宽度。
        @param gap 行间距，默认 6。
        @return 最后一行的底部 Y 坐标。
    """
    x, y = xy
    for line in fit_wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
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


def table(draw: ImageDraw.ImageDraw, x: int, y: int, headers: list[str], rows: list[list[str]], widths: list[int]) -> int:
    """ @brief 绘制带表头的简单表格。
        @param draw PIL ImageDraw 实例。
        @param x 表格左上角 X。
        @param y 表格左上角 Y。
        @param headers 表头列名列表。
        @param rows 数据行（二维列表）。
        @param widths 每列像素宽度列表。
        @return 表格底部 Y 坐标。
    """
    h = 56
    header_fill = "#EAF3FF"
    cell_fill = "#FFFFFF"
    xx = x
    for header, width in zip(headers, widths):
        draw.rectangle((xx, y, xx + width, y + h), fill=header_fill, outline=PALETTE["line"], width=2)
        center_text(draw, (xx + 4, y, xx + width - 4, y + h), header, font(24, True), PALETTE["ink"])
        xx += width
    y += h
    for row in rows:
        xx = x
        for value, width in zip(row, widths):
            draw.rectangle((xx, y, xx + width, y + h), fill=cell_fill, outline=PALETTE["line"], width=1)
            center_text(draw, (xx + 4, y, xx + width - 4, y + h), value, font(24), PALETTE["ink"])
            xx += width
        y += h
    return y


def draw_graph(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制玩具 Tanner 图：4 个变量节点 v0-v3 + 2 个校验节点 c0-c1 + 6 条边。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
    """
    draw.text((70, 162), "玩具 Tanner 图", font=font(30, True), fill=PALETTE["blue"])
    vx = [120, 250, 380, 510]
    vy = 265
    cx = [205, 425]
    cy = 475
    edges = [(0, 0), (1, 0), (2, 0), (1, 1), (2, 1), (3, 1)]
    for v, c in edges:
        draw.line((vx[v], vy + 24, cx[c], cy - 24), fill="#A9B7C7", width=3)
    for i, x in enumerate(vx):
        draw.ellipse((x - 32, vy - 32, x + 32, vy + 32), fill="#EAF3FF", outline=PALETTE["blue"], width=3)
        center_text(draw, (x - 32, vy - 32, x + 32, vy + 32), f"v{i}", font(24, True), PALETTE["ink"])
        center_text(draw, (x - 70, vy - 78, x + 70, vy - 40), f"Lch={ [2.0,-1.0,0.7,1.2][i] }", font(24), PALETTE["muted"])
    for i, x in enumerate(cx):
        draw.rounded_rectangle((x - 42, cy - 32, x + 42, cy + 32), radius=8, fill="#EAF8F1", outline=PALETTE["green"], width=3)
        center_text(draw, (x - 42, cy - 32, x + 42, cy + 32), f"c{i}", font(24, True), PALETTE["ink"])
    draw_wrapped(
        draw,
        (70, 535),
        "第一轮：变量节点先把 channel LLR 发到相邻校验节点；校验节点只用“其他边”的消息计算外信息。",
        font(24),
        PALETTE["muted"],
        520,
    )


def draw_formula_panel(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制 SPA 消息更新公式面板：VN->CN、CN->VN、Posterior 三种对象。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
    """
    panel = (650, 160, 1530, 400)
    draw.rounded_rectangle(panel, radius=16, fill=PALETTE["panel"], outline=PALETTE["line"], width=2)
    draw.text((680, 190), "SPA 更新的三个对象", font=font(30, True), fill=PALETTE["ink"])
    items = [
        ("VN -> CN", "q[j->i] = Lch[j] + 其他校验节点给 vj 的消息"),
        ("CN -> VN", "r[i->j] = 2 atanh( ∏ tanh(q[k->i]/2) ), k != j"),
        ("Posterior", "Lpost[j] = Lch[j] + 所有相邻校验节点消息"),
    ]
    y = 245
    for label, text in items:
        draw.rounded_rectangle((680, y - 8, 808, y + 38), radius=8, fill=PALETTE["blue"], outline=PALETTE["blue"])
        center_text(draw, (680, y - 8, 808, y + 38), label, font(24, True), "#FFFFFF")
        draw.text((820, y), text, font=font(24), fill=PALETTE["ink"])
        y += 60


def draw_numeric_tables(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制一轮 SPA 数值结果表格：CN 外信息、VN posterior、hard decision、syndrome。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
    """
    draw.text((650, 430), "一轮数值结果", font=font(30, True), fill=PALETTE["green"])
    rows1 = [
        ["r0->v0", "-0.313"],
        ["r0->v1", "+0.524"],
        ["r0->v2", "-0.735"],
        ["r1->v1", "+0.365"],
        ["r1->v2", "-0.507"],
        ["r1->v3", "-0.313"],
    ]
    table(draw, 650, 475, ["CN 外信息", "LLR"], rows1, [150, 110])
    rows2 = [
        ["v0", "+1.687", "0"],
        ["v1", "-0.111", "1"],
        ["v2", "-0.542", "1"],
        ["v3", "+0.887", "0"],
    ]
    table(draw, 925, 475, ["VN", "Lpost", "hard"], rows2, [85, 120, 85])
    rows3 = [["c0", "0 xor 1 xor 1", "0"], ["c1", "1 xor 1 xor 0", "0"]]
    table(draw, 1240, 475, ["check", "GF(2)", "s"], rows3, [95, 180, 65])
    draw_wrapped(
        draw,
        (1240, 670),
        "syndrome=[0,0]，该 toy 例子第一轮可早停；真实接收机仍需按协议边界执行 CRC。",
        font(24),
        PALETTE["red"],
        340,
    )


def draw_bottom_notes(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制底部四列工程检测点卡片：外信息、非线性、定点风险、停止边界。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
    """
    panel = (70, 760, 1530, 1060)
    draw.rounded_rectangle(panel, radius=16, fill="#FFFDF6", outline="#E2CD7A", width=2)
    draw.text((105, 790), "读图顺序与工程检测点", font=font(30, True), fill=PALETTE["ink"])
    columns = [
        ("1. 外信息", "给某条边回消息时，不能把这条边自己刚送来的证据带回去。"),
        ("2. 非线性", "校验节点使用 tanh/atanh 把“偶校验约束”转成 LLR 外信息。"),
        ("3. 定点风险", "atanh 接近 1 时数值会变大，硬件通常要裁剪、查表或近似。"),
        ("4. 停止边界", "syndrome 可做 LDPC 早停；CRC 决定 CB/TB 是否可信。"),
    ]
    x = 105
    for title, body in columns:
        draw.rounded_rectangle((x, 850, x + 320, 1000), radius=10, fill="#FFFFFF", outline=PALETTE["line"], width=2)
        draw.text((x + 18, 865), title, font=font(24, True), fill=PALETTE["blue"])
        draw_wrapped(draw, (x + 18, 905), body, font(24), PALETTE["muted"], 282, gap=8)
        x += 350


def main() -> None:
    """ @brief 脚本入口：生成 T8.5 LDPC BP/SPA 一轮消息传递教学图。
        @return 无返回值。
        @note 产出 1600x1120 PNG：Tanner 图 + SPA 公式 + 数值结果 + 检测点。
    """
    img = Image.new("RGB", (1600, 1120), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "LDPC BP/SPA 一轮消息传递", font=font(40, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (70, 102),
        "教学矩阵 H=[[1,1,1,0],[0,1,1,1]]，初始 channel LLR=[2.0,-1.0,0.7,1.2]。图中数值用于解释算法，不是 NR conformance vector。",
        font(24),
        PALETTE["muted"],
        1400,
    )
    draw_graph(draw)
    draw_formula_panel(draw)
    draw_numeric_tables(draw)
    draw_bottom_notes(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
