#!/usr/bin/env python3
"""@file render_nr_ldpc_circular_buffer_states.py
@brief 渲染 NR LDPC Circular Buffer 状态对比教学图
@date 2025
@note 设计意图：将 punctured/unknown、shortened/filler、repeated 三类位置放在同一条母码
  circular buffer 上可视化，并展示接收端动作链（地址流→掩码检查→LLR 动作→LDPC 输入）
  和四种常见错误的对照表。
@see docs/L2/T9.2_NR_LDPC_circular_buffer_states.md
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
OUT_PATH = ROOT / "docs/L2/assets/T9.2_NR_LDPC_circular_buffer_states.png"

PALETTE = {
    "ink": "#17212F",
    "muted": "#5B6877",
    "line": "#C9D4DF",
    "bg": "#FFFFFF",
    "blue": "#2457A6",
    "green": "#2D8F5D",
    "amber": "#C69220",
    "red": "#C64B59",
    "purple": "#7457A6",
    "gray": "#EEF2F6",
}


def center_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    """@brief 在矩形内居中绘制单行文本
    @param draw PIL 绘图上下文
    @param box 目标矩形
    @param text 文本
    @param fnt 字体对象
    @param fill 文字颜色"""
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, width: int, fill: str, gap: int = 5) -> int:
    """@brief 在指定位置绘制自动换行文本
    @param draw PIL 绘图上下文
    @param xy 起始坐标
    @param text 原始文本
    @param fnt 字体对象
    @param width 每行最大像素宽度
    @param fill 文字颜色
    @param gap 行间距，默认 5
    @return 绘制后下一行 Y 坐标"""
    x, y = xy
    for line in fit_wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#61758A") -> None:
    """@brief 绘制带箭头头的线段
    @param draw PIL 绘图上下文
    @param start 起点坐标
    @param end 终点（箭头尖端）坐标
    @param color 颜色，默认灰色
    @note 箭头头长 12px、宽 7px"""
    sx, sy = start
    ex, ey = end
    length = math.hypot(ex - sx, ey - sy)
    if length == 0:
        return
    ux, uy = (ex - sx) / length, (ey - sy) / length
    px, py = -uy, ux
    head_len, head_w = 12, 7
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


def draw_buffer(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制同一条 circular buffer 上的 12 个位置及其三类状态
    @param draw PIL 绘图上下文
    @note 每个位置显示 pos 编号、LLR 值和状态标签（new/punct/short/rep/unk），
      下方三个图例解释 punctured/unknown、shortened/filler、repeated 的工程语义"""
    x0, y0 = 78, 292
    cell_w, cell_h = 118, 96
    states = [
        ("0", "+1.2", "new", "#EAF6FF"),
        ("1", "0", "punct", "#F2F4F7"),
        ("2", "+8.0", "short", "#EAF8EF"),
        ("3", "-2.3", "rep", "#FFF7E5"),
        ("4", "+0.4", "new", "#EAF6FF"),
        ("5", "0", "punct", "#F2F4F7"),
        ("6", "+8.0", "short", "#EAF8EF"),
        ("7", "-0.6", "new", "#EAF6FF"),
        ("8", "+3.1", "rep", "#FFF7E5"),
        ("9", "0", "unk", "#F2F4F7"),
        ("10", "+0.9", "new", "#EAF6FF"),
        ("11", "-1.4", "new", "#EAF6FF"),
    ]
    for i, (pos, value, state, color) in enumerate(states):
        x = x0 + i * cell_w
        draw.rectangle((x, y0, x + cell_w, y0 + 30), fill="#EAF3FF", outline=PALETTE["line"], width=1)
        center_text(draw, (x, y0, x + cell_w, y0 + 30), f"pos {pos}", font(24, True), PALETTE["ink"])
        draw.rectangle((x, y0 + 30, x + cell_w, y0 + cell_h), fill=color, outline=PALETTE["line"], width=1)
        center_text(draw, (x, y0 + 30, x + cell_w, y0 + 62), value, font(24, True), PALETTE["ink"])
        center_text(draw, (x + 4, y0 + 62, x + cell_w - 4, y0 + cell_h - 4), state, font(24), PALETTE["muted"])

    legend = [
        ("punctured / unknown", "没有空口观测：LLR=0，unknown_mask=1，不是业务 0", "#F2F4F7"),
        ("shortened / filler", "协议已知约束：强 0 LLR 或 known_mask 固定", "#EAF8EF"),
        ("repeated", "同一母码位置多次观测：旧 LLR + 新 LLR，定点需饱和", "#FFF7E5"),
    ]
    y = y0 + 124
    x = 78
    for title, body, color in legend:
        draw.rounded_rectangle((x, y, x + 470, y + 138), radius=10, fill=color, outline=PALETTE["line"], width=1)
        draw.text((x + 18, y + 12), title, font=font(24, True), fill=PALETTE["ink"])
        wrapped(draw, (x + 18, y + 50), body, font(24), 428, PALETTE["muted"], gap=4)
        x += 500


def draw_update_flow(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制接收端动作链：地址流→掩码检查→LLR 动作→LDPC 输入
    @param draw PIL 绘图上下文
    @note 四个节点横向排列，展示从 RV/k0 地址产生到最终 LDPC 输入的完整数据通路"""
    y = 608
    boxes = [
        ("addr stream", "RV/k0/Ncb 产生候选地址", "#EAF6FF"),
        ("mask check", "punctured / shortened / observed", "#F4F0FF"),
        ("LLR action", "0 / strong known / sat_add", "#FFF7E5"),
        ("LDPC input", "ldpc_llr + unknown/known mask", "#EAF8EF"),
    ]
    x = 110
    prev = None
    for title, body, color in boxes:
        box = (x, y, x + 300, y + 160)
        draw.rounded_rectangle(box, radius=12, fill=color, outline=PALETTE["line"], width=2)
        center_text(draw, (box[0] + 10, box[1] + 14, box[2] - 10, box[1] + 50), title, font(24, True), PALETTE["ink"])
        wrapped(draw, (box[0] + 22, box[1] + 66), body, font(24), 256, PALETTE["muted"], gap=4)
        if prev:
            arrow(draw, (prev[2], y + 75), (box[0], y + 75))
        prev = box
        x += 355


def draw_errors(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制错误对照与工程检测点表格
    @param draw PIL 绘图上下文
    @note 四行对比：punctured、shortened、repeated、skip/null 四种状态下的
      正确处理、典型错误和可观测检测点"""
    panel = (70, 814, 1530, 1288)
    draw.rounded_rectangle(panel, radius=16, fill="#FFFDF6", outline="#E2CD7A", width=2)
    draw.text((105, 850), "错误对照与工程检测点", font=font(28, True), fill=PALETTE["ink"])
    headers = ["状态", "正确处理", "典型错误", "可观测检测点"]
    rows = [
        ["punctured", "LLR=0, unknown=1", "填 +MAX 当作业务 0", "unknown_count / CRC fail"],
        ["shortened", "+Known 或 known=1", "填 0 当 unknown", "known_count / syndrome 收敛慢"],
        ["repeated", "sat(old + new)", "覆盖 old LLR", "repeat_count / saturation_count"],
        ["skip/null", "不消耗 rx LLR", "消耗一个 LLR", "write_count != E"],
    ]
    x0, y0 = 105, 912
    widths = [190, 310, 340, 365]
    row_h = 60  # TEXT_FIT_OK: table values are short controlled labels centered at 24px.
    x = x0
    for head, width in zip(headers, widths):
        draw.rectangle((x, y0, x + width, y0 + row_h), fill="#EAF3FF", outline=PALETTE["line"], width=2)
        center_text(draw, (x, y0, x + width, y0 + row_h), head, font(24, True), PALETTE["ink"])
        x += width
    y = y0 + row_h
    for row in rows:
        x = x0
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill="#FFFFFF", outline=PALETTE["line"], width=1)
            center_text(draw, (x + 6, y, x + width - 6, y + row_h), value, font(24), PALETTE["ink"])
            x += width
        y += row_h

    note_y = y + 28
    draw.text((110, note_y), "读图结论：unknown 表示没有证据，known 表示协议已知约束，repeat 表示多次证据累加。三者不能互相替代。", font=font(24, True), fill=PALETTE["red"])


def main() -> None:
    """@brief 渲染 NR LDPC Circular Buffer 状态对比教学图
    @note 输出文件: docs/L2/assets/T9.2_NR_LDPC_circular_buffer_states.png
    @note 图中包含三类状态的可视化 buffer、接收端动作链流程图、
      四行错误对照表，强调 unknown/known/repeat 三种语义不可互替"""
    img = Image.new("RGB", (1700, 1420), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "NR LDPC Circular Buffer 状态对比", font=font(40, True), fill=PALETTE["ink"])
    wrapped(
        draw,
        (70, 108),
        "目标：把 punctured/unknown、shortened/filler、repeated 三类位置放到同一条母码 circular buffer 上看清楚。接收端的关键不是只填一个 LLR 数组，而是同时维护 unknown_mask、known_mask 和 repeat/saturation 计数。",
        font(24),
        1470,
        PALETTE["muted"],
    )
    draw.text((70, 240), "同一条 circular buffer 上的三类状态", font=font(28, True), fill=PALETTE["blue"])
    draw_buffer(draw)
    draw.text((70, 576), "接收端动作链", font=font(28, True), fill=PALETTE["green"])
    draw_update_flow(draw)
    draw_errors(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
