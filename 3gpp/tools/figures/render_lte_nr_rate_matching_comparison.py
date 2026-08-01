#!/usr/bin/env python3
"""@file render_lte_nr_rate_matching_comparison.py
@brief 渲染 LTE Turbo / NR LDPC / NR Polar 三协议速率匹配与速率恢复对比教学图
@date 2025
@note 设计意图：将三类协议的接收端反向流程并排放置，配合差异对比表和循环缓存示例，
  使读者能从“空口 LLR 到译码器输入”的完整路径理解 unknown/repeated/shortened 三种空洞语义。
@see docs/L2/T11.2_LTE_NR_rate_matching.md
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
OUT_PATH = ROOT / "docs/L2/assets/T11.2_LTE_NR_rate_matching_comparison.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#152033",
    "muted": "#5B6878",
    "line": "#8FA1B5",
    "panel": "#F6F8FB",
    "turbo": "#B65B2E",
    "turbo_fill": "#FFF1E8",
    "ldpc": "#22785A",
    "ldpc_fill": "#E8F6EF",
    "polar": "#2457A6",
    "polar_fill": "#EAF1FB",
    "warn": "#FFF7DF",
    "bad": "#FCE9E8",
    "good": "#EAF7EF",
}


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    """@brief 按指定最大宽度对文本进行自动换行
    @param draw PIL 绘图上下文
    @param text 待换行的原始文本
    @param fnt 使用的字体对象
    @param max_width 每行最大像素宽度
    @return 换行后的字符串列表
    @note 委托给 figure_text_fit.wrap_text，统一全项目换行策略"""
    return fit_wrap_text(draw, text, fnt, max_width)


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    size: int,
    fill: str,
    bold: bool = True,
    line_gap: int = 8,
) -> None:
    """@brief 在矩形区域内居中绘制多行文本
    @param draw PIL 绘图上下文
    @param box 目标矩形 (x0, y0, x1, y1)
    @param lines 要绘制的文本行列表
    @param size 字体像素大小
    @param fill 文字颜色
    @param bold 是否加粗，默认 True
    @param line_gap 行间距像素，默认 8
    @note 所有行整体在 box 内水平和垂直居中，逐行 anchor="mm" 布局"""
    fnt = font(size, bold)
    heights = []
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=fnt)
        heights.append(bb[3] - bb[1])
    total = sum(heights) + line_gap * (len(lines) - 1)
    y = (box[1] + box[3] - total) / 2
    cx = (box[0] + box[2]) / 2
    for line, h in zip(lines, heights):
        draw.text((cx, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + line_gap


def assert_text_fits(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    size: int,
    bold: bool,
    line_gap: int,
    padding: int = 8,
) -> None:
    """@brief 断言多行文本不超出给定矩形区域
    @param draw PIL 绘图上下文
    @param box 目标矩形 (x0, y0, x1, y1)
    @param lines 文本行列表
    @param size 字体像素大小
    @param bold 是否加粗
    @param line_gap 行间距像素
    @param padding 内边距像素，默认 8
    @throws RuntimeError 文本尺寸超出 box 时抛出
    @note 用于自测验证：确保表格单元格能容纳其内容文本"""
    fnt = font(size, bold)
    heights = []
    max_width = 0
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=fnt)
        heights.append(bb[3] - bb[1])
        max_width = max(max_width, bb[2] - bb[0])
    total_h = sum(heights) + line_gap * max(0, len(lines) - 1)
    if max_width > (box[2] - box[0]) - 2 * padding or total_h > (box[3] - box[1]) - 2 * padding:
        raise RuntimeError(f"text does not fit box={box}: width={max_width}, height={total_h}, lines={lines}")


def rounded_node(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    outline: str,
    fill: str = "#FFFFFF",
    text_fill: str = COL["ink"],
    size: int = 24,
    bold: bool = True,
    line_gap: int = 8,
) -> tuple[int, int, int, int]:
    """@brief 绘制圆角矩形节点并居中填充多行文本
    @param draw PIL 绘图上下文
    @param box 节点矩形 (x0, y0, x1, y1)
    @param lines 节点内文本行列表
    @param outline 描边颜色
    @param fill 填充颜色，默认白色
    @param text_fill 文字颜色，默认 COL["ink"]
    @param size 字体像素大小，默认 24
    @param bold 是否加粗，默认 True
    @param line_gap 行间距像素，默认 8
    @return 节点矩形 box（与输入相同，便于链式传递）
    @note 圆角半径固定为 18，描边宽度固定为 2"""
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=outline, width=2)
    draw_centered_lines(draw, box, lines, size=size, fill=text_fill, bold=bold, line_gap=line_gap)
    return box


def center(box: tuple[int, int, int, int]) -> tuple[float, float]:
    """@brief 计算矩形几何中心坐标
    @param box 矩形 (x0, y0, x1, y1)
    @return 中心坐标 (cx, cy)"""
    return ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2)


def boundary_point(box: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    """@brief 计算从矩形中心射向目标点时与矩形边界的交点
    @param box 矩形 (x0, y0, x1, y1)
    @param toward 目标点坐标 (tx, ty)
    @return 边界交点坐标
    @note 用于连接线的精确起止定位：连线从源矩形边界出发，到达目标矩形边界"""
    cx, cy = center(box)
    dx = toward[0] - cx
    dy = toward[1] - cy
    if abs(dx) < 1e-6 and abs(dy) < 1e-6:
        return cx, cy
    half_w = max((box[2] - box[0]) / 2, 1)
    half_h = max((box[3] - box[1]) / 2, 1)
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return cx + dx / scale, cy + dy / scale


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str,
    width: int = 3,
) -> None:
    """@brief 绘制带箭头头的线段
    @param draw PIL 绘图上下文
    @param start 起点坐标
    @param end 终点（箭头尖端）坐标
    @param color 线条和箭头颜色
    @param width 线条宽度，默认 3
    @note 箭头头长 14px、宽 9px，自动预留空间避免线段穿入箭头三角形"""
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux = (x1 - x0) / length
    uy = (y1 - y0) / length
    head_len = 14
    head_w = 9
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    draw.line((start, line_end), fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    back_x = x1 - head_len * math.cos(angle)
    back_y = y1 - head_len * math.sin(angle)
    perp_x = head_w * math.sin(angle)
    perp_y = -head_w * math.cos(angle)
    draw.polygon([(x1, y1), (back_x + perp_x, back_y + perp_y), (back_x - perp_x, back_y - perp_y)], fill=color)


def connect_arrow(
    draw: ImageDraw.ImageDraw,
    src: tuple[int, int, int, int],
    dst: tuple[int, int, int, int],
    color: str,
    width: int = 3,
) -> None:
    """@brief 在两个矩形节点之间绘制自动取边界交点的箭頭连线
    @param draw PIL 绘图上下文
    @param src 源矩形 (x0, y0, x1, y1)
    @param dst 目标矩形 (x0, y0, x1, y1)
    @param color 连线颜色
    @param width 线宽，默认 3
    @note 自动计算从 src 边界到 dst 边界的最短连线路径"""
    s = boundary_point(src, center(dst))
    e = boundary_point(dst, center(src))
    arrow(draw, s, e, color=color, width=width)


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, color: str, fill: str) -> None:
    """@brief 绘制带标题的圆角面板容器
    @param draw PIL 绘图上下文
    @param box 面板矩形
    @param title 面板左上角标题
    @param color 标题文字和描边颜色
    @param fill 面板填充色
    @note 标题位于面板内左上角 (x+24, y+18)，字号 25 加粗"""
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=color, width=3)
    draw.text((box[0] + 24, box[1] + 18), title, font=font(25, True), fill=color)


def draw_flow_panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, color: str, fill: str, nodes: list[list[str]]) -> None:
    """@brief 绘制协议接收端反向流程面板
    @param draw PIL 绘图上下文
    @param box 面板矩形
    @param title 面板标题（如 "LTE Turbo"）
    @param color 主题色
    @param fill 面板填充色
    @param nodes 流程节点列表，每个元素为 [标题行, 副标题行]
    @note 节点自上而下排列并通过箭头连接，每个节点高 92px、间距 24px"""
    panel(draw, box, title, color, fill)
    left = box[0] + 30
    top = box[1] + 98
    w = box[2] - box[0] - 60
    h = 92
    gap = 24
    node_boxes = []
    for i, lines in enumerate(nodes):
        nb = (left, top + i * (h + gap), left + w, top + i * (h + gap) + h)
        node_boxes.append(rounded_node(draw, nb, lines, color, "#FFFFFF", size=24))
    for a, b in zip(node_boxes, node_boxes[1:]):
        connect_arrow(draw, a, b, color, 3)


def draw_table(draw: ImageDraw.ImageDraw, min_top: int) -> int:
    """@brief 绘制三协议速率恢复差异对比表
    @param draw PIL 绘图上下文
    @param min_top 上方面板底部的最低 Y 坐标，用于检测间距不足
    @return 表格底部 Y 坐标
    @throws RuntimeError 表格与上方内容间距不足 80px 时抛出
    @note 表格第一行和第一列为灰色表头，其余使用居中 24px 文字"""
    x0, y0 = 90, 925
    if y0 - min_top < 80:
        raise RuntimeError(f"flow-to-table spacing too small: {y0 - min_top} px")
    widths = [230, 455, 455, 455]
    row_h = 86  # TEXT_FIT_OK: draw_table wraps every cell and centers 24px text.
    rows = [
        ["对象", "LTE Turbo", "NR LDPC", "NR Polar"],
        ["恢复目标", "三路 Turbo LLR", "LDPC 母码位置 LLR", "Polar codeword LLR"],
        ["核心长度", "E, K_w", "E, N_cb, N", "E, N"],
        ["交织", "三路 sub-block", "bit interleaving", "sub-block + coded-bit"],
        ["RV", "rvidx 选窗口", "RV/k0 选窗口", "通常非数据 HARQ 语义"],
        ["未发送", "unknown LLR", "unknown LLR", "punctured unknown"],
        ["已知空洞", "<NULL> 删除", "filler/shortened mask", "shortened strong known"],
        ["重复", "soft buffer 累加", "soft buffer 累加", "同位置 LLR 累加"],
    ]
    for r, row in enumerate(rows):
        x = x0
        for c, cell in enumerate(row):
            box = (x, y0 + r * row_h, x + widths[c], y0 + (r + 1) * row_h)
            fill = COL["panel"] if r == 0 or c == 0 else "#FFFFFF"
            draw.rectangle(box, fill=fill, outline=COL["line"], width=1)
            lines = wrap_text(draw, cell, font(24, True), widths[c] - 30)
            assert_text_fits(draw, box, lines, 24, True, 6)
            draw_centered_lines(draw, box, lines, 24, COL["ink"], True, 6)
            x += widths[c]
    return y0 + len(rows) * row_h


def draw_ring(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制小型循环缓存示例图：含未发送、重复和已知位置
    @param draw PIL 绘图上下文
    @note 将环形缓冲区 12 个地址可视化，用颜色区分 new/repeat/unsent/short 四种状态，
      并在线性写回序列中展示 repeat 累加和 unsent 保持中性的工程语义"""
    cx, cy = 420, 2005
    radius = 205
    positions = list(range(12))
    labels = {
        0: ("new", COL["good"]),
        1: ("repeat", "#DDF0FF"),
        2: ("unsent", COL["warn"]),
        3: ("new", COL["good"]),
        4: ("short", "#ECE5FF"),
        5: ("new", COL["good"]),
        6: ("unsent", COL["warn"]),
        7: ("repeat", "#DDF0FF"),
        8: ("new", COL["good"]),
        9: ("new", COL["good"]),
        10: ("unsent", COL["warn"]),
        11: ("new", COL["good"]),
    }
    title_pos = (90, 1660)
    title_text = "小型循环缓存例子：含未发送、重复和已知位置"
    title_bbox = draw.textbbox(title_pos, title_text, font=font(30, True))
    draw.text(title_pos, title_text, font=font(30, True), fill=COL["ink"])
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=COL["line"], width=3)
    node_boxes: dict[int, tuple[int, int, int, int]] = {}
    for i in positions:
        ang = -math.pi / 2 + 2 * math.pi * i / len(positions)
        x = cx + radius * math.cos(ang)
        y = cy + radius * math.sin(ang)
        state, fill = labels[i]
        node_boxes[i] = rounded_node(draw, (int(x - 56), int(y - 38), int(x + 56), int(y + 38)), [str(i), state], "#6C7A89", fill, size=24, line_gap=4)
    top_node_y = min(b[1] for b in node_boxes.values())
    if top_node_y - title_bbox[3] < 36:
        raise RuntimeError(f"ring title spacing too small: {top_node_y - title_bbox[3]} px")
    order = [8, 9, 11, 0, 1, 3, 5, 7, 1]
    x0, y0 = 740, 2000
    draw.text((x0, y0 - 66), "示例写回序列", font=font(29, True), fill=COL["ink"])
    prev_box = None
    for idx, addr in enumerate(order):
        box = (x0 + idx * 126, y0, x0 + idx * 126 + 104, y0 + 74)
        fill = "#DDF0FF" if addr in {1, 7} else COL["good"]
        rounded_node(draw, box, [f"rx{idx}", f"a={addr}"], "#6C7A89", fill, size=24)
        if prev_box:
            connect_arrow(draw, prev_box, box, "#6C7A89", 2)
        prev_box = box
    notes = [
        ("unsent", "中性 LLR，不等于业务 0"),
        ("repeat", "同地址 LLR 相加，定点需饱和"),
        ("short", "已知 0/约束位，不能当 unknown"),
    ]
    for i, (tag, desc) in enumerate(notes):
        b = (740, 2160 + i * 84, 1680, 2225 + i * 84)
        rounded_node(draw, b, [f"{tag}: {desc}"], "#C59A30", COL["warn"], size=24)


def draw_checks(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制读图顺序与工程检查点说明面板
    @param draw PIL 绘图上下文
    @note 四条检查点按序列排列：反向流程→字段表→循环缓存→RTL 抽象分层"""
    box = (90, 2590, 1830, 2955)
    draw.rounded_rectangle(box, radius=18, fill=COL["warn"], outline="#C59A30", width=2)
    draw.text((box[0] + 28, box[1] + 28), "读图顺序与工程检查点", font=font(31, True), fill=COL["ink"])
    checks = [
        "1. 先看三条接收端反向流程：空口 LLR 不是 decoder input，必须先恢复到母码位置。",
        "2. 再看字段表：E 是收到长度，K_w/N_cb/N 是不同坐标系，不能混写。",
        "3. 最后看循环缓存：未发送保持 unknown，重复位置累加，shortened/known 位置按强约束或 mask 处理。",
        "4. RTL 可共享 address generator/mask RAM 抽象，但不能共享三类协议规则和 interleaver 表。",
    ]
    y = box[1] + 88
    for line in checks:
        draw.text((box[0] + 28, y), line, font=font(24, True), fill=COL["ink"])
        y += 58


def main() -> None:
    """@brief 渲染 LTE/NR 三协议速率匹配与速率恢复对比图
    @note 输出文件: docs/L2/assets/T11.2_LTE_NR_rate_matching_comparison.png
    @note 图中包含三个并排接收端流程面板（LTE Turbo / NR LDPC / NR Polar）、
      一个七行对比表、一个环形缓存示例和工程检查点说明"""
    img = Image.new("RGB", (1900, 3060), COL["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "T11.2 LTE/NR 速率匹配与速率恢复对比", font=font(42, True), fill=COL["ink"])
    draw.text((70, 108), "共同目标：把线性接收 LLR 流恢复为译码器母码位置软信息；差异在协议坐标系、交织和空洞语义。", font=font(25), fill=COL["muted"])

    panel_w = 560
    draw_flow_panel(
        draw,
        (70, 180, 70 + panel_w, 800),
        "LTE Turbo",
        COL["turbo"],
        COL["turbo_fill"],
        [
            ["Demapper LLR", "rx_llr[0:E-1]"],
            ["RV / K_w", "写回循环软缓存"],
            ["拆成三路流", "systematic / parity1 / parity2"],
            ["sub-block 解交织", "删除 <NULL>"],
            ["Turbo decoder", "三路 LLR 输入"],
        ],
    )
    draw_flow_panel(
        draw,
        (670, 180, 670 + panel_w, 800),
        "NR LDPC",
        COL["ldpc"],
        COL["ldpc_fill"],
        [
            ["Demapper LLR", "rx_llr[0:E-1]"],
            ["bit deinterleaver", "按 Q_m 反交织"],
            ["RV / N_cb / k0", "写回 soft buffer"],
            ["mask / combine", "unknown + repeated"],
            ["LDPC decoder", "母码位置 LLR"],
        ],
    )
    draw_flow_panel(
        draw,
        (1270, 180, 1270 + panel_w, 800),
        "NR Polar",
        COL["polar"],
        COL["polar_fill"],
        [
            ["Demapper LLR", "rx_llr[0:E-1]"],
            ["coded-bit 反交织", "按配置启用"],
            ["bit selection reverse", "puncture / shorten / repeat"],
            ["sub-block 解交织", "32 sub-block 反置换"],
            ["SC/SCL decoder", "codeword LLR"],
        ],
    )

    table_bottom = draw_table(draw, min_top=800)
    draw_ring(draw)
    draw_checks(draw)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
