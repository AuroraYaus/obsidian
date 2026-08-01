#!/usr/bin/env python3
""" @file render_t13_5_simd_memory_layout_decoders.py
    @brief 渲染 T13.5 三种译码器（Turbo/LDPC/Polar）的 SIMD 通道映射和存储布局对比图
    @date 2025
    @see render_t13_3_nr_ldpc_fixed_point_model.py LDPC 定点化模型
    @see render_t13_4_nr_polar_fixed_point_model.py Polar 定点化模型
    @see render_t14_1_lte_turbo_rtl_microarchitecture.py Turbo 微架构中的存储体设计
"""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T13.5_SIMD_memory_layout_decoders.png"



TITLE = font(42, True)
HEAD = font(27, True)
TEXT = font(24)
SMALL = font(24)
TABLE = font(24)
TABLE_HEAD = font(24, True)

INK = "#102027"
MUTED = "#455a64"
LINE = "#b0bec5"


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:

    """ @brief 计算文本在指定字体下的渲染像素宽高，用于布局和自动换行宽度判断
        @param draw PIL ImageDraw 绘制上下文
        @param text 待测量的文本字符串
        @param fnt PIL ImageFont 字体对象
        @return 元组 (width, height) 表示文本占据的像素尺寸
    """
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:

    """ @brief 按指定宽度自动换行文本，单词边界处断行，确保每行渲染宽度不超过给定像素宽度上限
        @param draw PIL ImageDraw 绘制上下文
        @param text 待换行的英文字符串
        @param fnt PIL ImageFont 字体对象
        @param width 像素宽度上限
        @return 换行后的字符串列表，每行为一个文本块
    """
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        cand = word if not cur else f"{cur} {word}"
        if text_size(draw, cand, fnt)[0] <= width:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centered(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], lines: list[str], fnt, fill=INK, gap=7) -> None:

    """ @brief 在给定矩形区域内垂直居中绘制多行文本，支持行间距控制
        @param draw PIL ImageDraw 绘制上下文
        @param lines 多行文本列表
        @param fnt PIL ImageFont 字体对象
        @param rect 绘制的矩形边界 (x0, y0, x1, y1)
        @param fill 文字颜色
        @param gap 行间距像素值
        @note 先计算总高度再做垂直偏移，确保文本块在矩形内视觉居中
    """
    x0, y0, x1, y1 = rect
    heights = [text_size(draw, line, fnt)[1] for line in lines]
    total = sum(heights) + gap * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    cx = (x0 + x1) / 2
    for line, height in zip(lines, heights):
        draw.text((cx, y + height / 2), line, font=fnt, fill=fill, anchor="mm")
        y += height + gap


def card(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, body: str, fill: str) -> None:

    """ @brief 绘制圆角卡片（标题 + 正文），作为知识图的基本信息容器
        @param draw PIL ImageDraw 绘制上下文
        @param rect 矩形的 (x0, y0, x1, y1) 坐标
        @param title 卡片标题（粗体渲染）
        @param body 卡片正文（自动换行后居中绘制）
        @param fill 卡片背景色
        @note 卡片是教学图中承载概念说明的主要视觉组件，边距和标题位置由参数内置
    """
    x0, y0, x1, y1 = rect
    draw.rounded_rectangle(rect, radius=8, fill=fill, outline="#37474f", width=2)
    draw.text(((x0 + x1) / 2, y0 + 34), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 24, y0 + 82, x1 - 24, y1 - 24), wrap(draw, body, SMALL, x1 - x0 - 48), SMALL, MUTED)


def table(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 66) -> None:

    """ @brief 绘制带表头的圆角数据表格，含行分隔线和列分隔线。
        @param draw PIL ImageDraw 绘制上下文。
        @param rect 表格容器的外边框 (x0, y0, x1, y1)。
        @param headers 表头文本列表。
        @param rows 数据行列表，每行为字符串列表。
        @param widths 每列宽度列表（像素）。
        @param row_h 每行高度（像素），默认 66。
        @return 无返回值。
        @note 表格是教学图中展示 checkpoint、寄存器映射、对比规则等结构化信息的主要组件。
    """
    x0, y0, _, _ = rect
    total_w = sum(widths)
    draw.rounded_rectangle((x0, y0, x0 + total_w, y0 + row_h * (len(rows) + 1)), radius=8, fill="#ffffff", outline="#607d8b", width=2)
    y = y0
    x = x0
    for header, width in zip(headers, widths):
        draw.rectangle((x, y, x + width, y + row_h), fill="#e3f2fd", outline="#b0bec5", width=1)
        centered(draw, (x + 8, y + 4, x + width - 8, y + row_h - 4), wrap(draw, header, TABLE_HEAD, width - 16), TABLE_HEAD)
        x += width
    for row in rows:
        y += row_h
        x = x0
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill="#ffffff", outline="#cfd8dc", width=1)
            centered(draw, (x + 8, y + 4, x + width - 8, y + row_h - 4), wrap(draw, value, TABLE, width - 16), TABLE)
            x += width


def center(rect: tuple[int, int, int, int]) -> tuple[float, float]:

    """ @brief 计算矩形几何中心坐标，用于箭头起止点的方向计算
        @param rect 矩形 (x0, y0, x1, y1)
        @return 中心坐标 (cx, cy)
    """
    return (rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2


def edge(src: tuple[int, int, int, int], dst: tuple[int, int, int, int]) -> tuple[float, float]:

    """ @brief 计算从矩形中心出发到目标方向的矩形边界交点，用于箭头的精确起止定位
        @param src 源矩形 (x0, y0, x1, y1)
        @param dst 目标矩形 (x0, y0, x1, y1)
        @return 源矩形边界上的交点坐标 (x, y)
        @note 通过射线与矩形求交得到箭头起点或终点，避免箭头穿入矩形内部
    """
    sx, sy = center(src)
    dx, dy = center(dst)
    vx, vy = dx - sx, dy - sy
    hw, hh = (src[2] - src[0]) / 2, (src[3] - src[1]) / 2
    tx = hw / abs(vx) if vx else float("inf")
    ty = hh / abs(vy) if vy else float("inf")
    t = min(tx, ty)
    return sx + vx * t, sy + vy * t


def arrow(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color="#546e7a") -> None:

    """ @brief 在两个矩形组件之间绘制带箭头的连接线。
        @param draw PIL ImageDraw 绘制上下文。
        @param src 源矩形 (x0, y0, x1, y1)。
        @param dst 目标矩形 (x0, y0, x1, y1)。
        @param color 线条颜色，默认 "#546e7a"。
        @return 无返回值。
        @note 箭头头部为三角形，自动计算方向并在目标边界处终止，不侵入目标矩形内部。
    """
    ax, ay = edge(src, dst)
    bx, by = edge(dst, src)
    vx, vy = bx - ax, by - ay
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    line_end = (bx - ux * head_len, by - uy * head_len)
    draw.line([(ax, ay), line_end], fill=color, width=4)
    px, py = -uy, ux
    draw.polygon(
        [(bx, by), (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w), (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w)],
        fill=color,
    )


def point_arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color="#546e7a") -> None:

    """ @brief 在两点之间绘制带三角箭头的连接线，适用于自由路由路径
        @param draw PIL ImageDraw 绘制上下文
        @param start 起点坐标 (x, y)
        @param end 终点坐标 (x, y)
        @param color 线条颜色
        @note 与 arrow() 不同，本函数不依赖矩形边界计算，直接使用像素坐标
    """
    sx, sy = start
    bx, by = end
    vx, vy = bx - sx, by - sy
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    line_end = (bx - ux * head_len, by - uy * head_len)
    draw.line([start, line_end], fill=color, width=4)
    px, py = -uy, ux
    draw.polygon(
        [(bx, by), (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w), (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w)],
        fill=color,
    )


def draw_lane_strip(draw: ImageDraw.ImageDraw, x: int, y: int, title: str, labels: list[str], color: str) -> None:

    """ @brief 绘制 SIMD 通道条带——按列排列的 lane 标签方块，用于展示向量化通道布局
        @param draw PIL ImageDraw 绘制上下文
        @param x 条带左上角 x 坐标
        @param y 条带左上角 y 坐标
        @param title 条带标题
        @param labels 各通道标签列表
        @param color 通道方块背景色
        @note 每条通道为等宽等高的圆角矩形，间距固定，标题在通道上方
    """
    draw.text((x, y), title, font=HEAD, fill=INK)
    cell_w, cell_h, gap = 92, 58, 10
    for idx, label in enumerate(labels):
        x0 = x + idx * (cell_w + gap)
        rect = (x0, y + 54, x0 + cell_w, y + 54 + cell_h)
        draw.rounded_rectangle(rect, radius=8, fill=color, outline="#607d8b", width=2)
        centered(draw, rect, [label], TABLE_HEAD, INK)


def main() -> None:

    """ @brief 绘制本文件对应的教学示意图，输出为 PNG 格式
        @note 本脚本是单文件渲染器，通过 PIL 直接绘制，不依赖外部图表库
        @note 输出路径由全局变量 OUT 定义，对应 docs/L3/assets/ 下的同名 PNG
    """
    W, H = 2400, 1900
    img = Image.new("RGB", (W, H), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((W / 2, 58), "T13.5 SIMD and Memory Layout for Decoders", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Protocol bit order is fixed; array layout is an implementation contract for cache, SIMD lanes and replay."
    centered(draw, (110, 82, W - 110, 132), wrap(draw, subtitle, TEXT, W - 220), TEXT, MUTED)

    top_cards = [
        (70, 165, 720, 405),
        (875, 165, 1525, 405),
        (1680, 165, 2330, 405),
    ]
    card(draw, top_cards[0], "Turbo", "Three LLR streams, interleaver/deinterleaver address maps, alpha/beta traces and extrinsic ping-pong buffers.", "#e3f2fd")
    card(draw, top_cards[1], "LDPC", "Layer-major edges, Zc-lane groups, posterior LLR read-modify-write and conflict-free message memory.", "#e8f5e9")
    card(draw, top_cards[2], "Polar", "Path-major state, node LLR memory, partial sums, path metric arrays and lazy-copy indirection.", "#f3e5f5")

    draw_lane_strip(draw, 80, 485, "SIMD lane examples", ["lane0", "lane1", "lane2", "lane3", "lane4", "lane5", "lane6", "lane7"], "#fff8e1")
    simd_src = (80, 540, 884, 598)
    lane_targets = [
        (80, 660, 700, 835),
        (890, 660, 1510, 835),
        (1700, 660, 2320, 835),
    ]
    card(draw, lane_targets[0], "Turbo lane map", "Run multiple code blocks or trellis windows in parallel; interleaver gathers must be staged or cached.", "#ffffff")
    card(draw, lane_targets[1], "LDPC lane map", "Map local index 0..Zc-1 to lanes; keep edge messages contiguous within a layer.", "#ffffff")
    card(draw, lane_targets[2], "Polar lane map", "Vectorize path candidates, node groups or PM comparisons; avoid copying full path state.", "#ffffff")
    bus_y = 625
    draw.line([(180, bus_y), (2010, bus_y)], fill="#546e7a", width=3)
    draw.line([(482, 598), (482, bus_y)], fill="#546e7a", width=3)
    lane_sources = [(390, bus_y), (1200, bus_y), (2010, bus_y)]
    lane_ends = [
        ((lane_targets[0][0] + lane_targets[0][2]) / 2, lane_targets[0][1]),
        ((lane_targets[1][0] + lane_targets[1][2]) / 2, lane_targets[1][1]),
        ((lane_targets[2][0] + lane_targets[2][2]) / 2, lane_targets[2][1]),
    ]
    for start, end in zip(lane_sources, lane_ends):
        point_arrow(draw, start, end)

    rows = [
        ["Object", "Turbo layout", "LDPC layout", "Polar layout"],
        ["Hot LLR", "stream-major int16 arrays", "layer-major posterior", "node-major or path-major"],
        ["Message", "extrinsic ping-pong", "edge-major CN/VN msg", "partial sum + node LLR"],
        ["SIMD unit", "multi-CB or trellis slice", "Zc lanes or edge block", "path pair or sorter block"],
        ["Failure", "random interleaver gather", "stride/bank conflict", "path copy storm"],
    ]
    table(draw, (335, 930, 2065, 0), rows[0], rows[1:], [230, 500, 500, 500], row_h=74)

    fail_panel = (90, 1380, 2310, 1745)
    draw.rounded_rectangle(fail_panel, radius=8, fill="#fff3e0", outline="#ef6c00", width=2)
    draw.text((W / 2, 1422), "Non-coalesced Access Failure Case", font=HEAD, fill="#7a3e00", anchor="mm")
    fail_cards = [
        (130, 1480, 660, 1685),
        (720, 1480, 1250, 1685),
        (1310, 1480, 1840, 1685),
        (1900, 1480, 2270, 1685),
    ]
    card(draw, fail_cards[0], "Gather storm", "Turbo pi[j] jumps across cache lines; SIMD lanes wait for scattered loads.", "#ffffff")
    card(draw, fail_cards[1], "Bank conflict", "LDPC two edges hit the same SRAM bank in one cycle; pipeline stalls.", "#ffffff")
    card(draw, fail_cards[2], "Path copy storm", "Polar prune copies full path arrays; bandwidth grows with list size.", "#ffffff")
    card(draw, fail_cards[3], "Cold trace", "Debug fields share hot arrays; cache lines carry data not used by decoder.", "#ffffff")

    centered(
        draw,
        (100, 1785, 2300, 1860),
        ["Audit rule: separate protocol indexing from implementation layout, then prove scalar equivalence before enabling SIMD."],
        SMALL,
        "#37474f",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
