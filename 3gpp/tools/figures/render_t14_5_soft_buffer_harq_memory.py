#!/usr/bin/env python3
""" @file render_t14_5_soft_buffer_harq_memory.py
    @brief 渲染 T14.5 软缓冲和 HARQ 存储架构图——逻辑标识到物理存储体映射、RV 访问事务和生命周期 FSM
    @date 2025
    @see render_t14_4_unified_decoder_subsystem.py 统一译码子系统，软缓冲管理器的宿主架构
    @see render_t14_6_decoder_register_config_flow.py 寄存器配置流程中的 SOFTBUF_CFG 字段定义
"""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T14.5_soft_buffer_HARQ_memory_architecture.png"



TITLE = font(42, True)
SUB = font(24)
HEAD = font(27, True)
TEXT = font(24)
TABLE = font(24)
TABLE_HEAD = font(24, True)

INK = "#102027"
MUTED = "#455a64"
LINE = "#546e7a"
BLUE = "#e3f2fd"
GREEN = "#e8f5e9"
AMBER = "#fff8e1"
PURPLE = "#f3e5f5"
RED = "#ffebee"
GRAY = "#eceff1"
WHITE = "#ffffff"


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


def centered(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], lines: list[str], fnt, fill=INK, gap: int = 7) -> None:

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
    draw.text(((x0 + x1) / 2, y0 + 36), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 22, y0 + 82, x1 - 22, y1 - 22), wrap(draw, body, TEXT, x1 - x0 - 44), TEXT, MUTED)


def mid(rect: tuple[int, int, int, int], side: str, offset: int = 0) -> tuple[float, float]:

    """ @brief 获取矩形指定边中点的坐标，用于组件间连线的标准化端口定位
        @param rect 矩形 (x0, y0, x1, y1)
        @param side 边的方向: "left"、"right"、"top"、"bottom"
        @param offset 沿边方向的偏移量，正值为向右（水平边）或向下（垂直边）
        @return 边中点坐标 (x, y)
        @note left/right 返回垂直中点的 x 坐标；top/bottom 返回水平中点的 y 坐标
    """
    x0, y0, x1, y1 = rect
    if side == "left":
        return x0, (y0 + y1) / 2 + offset
    if side == "right":
        return x1, (y0 + y1) / 2 + offset
    if side == "top":
        return (x0 + x1) / 2 + offset, y0
    if side == "bottom":
        return (x0 + x1) / 2 + offset, y1
    raise ValueError(side)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color: str = LINE, width: int = 4) -> None:

    """ @brief 在两点之间绘制带箭头的连接线。
        @param draw PIL ImageDraw 绘制上下文。
        @param start 起点坐标 (x, y)。
        @param end 终点坐标 (x, y)。
        @param color 线条颜色，默认 LINE。
        @param width 线宽（像素），默认 4。
        @return 无返回值。
        @note 箭头头部为三角形，自动计算方向并在目标边界处终止。
    """
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill=color, width=width)
    px, py = -uy, ux
    pts = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=color)


def segment_intersects_rect(
    p0: tuple[float, float],
    p1: tuple[float, float],
    rect: tuple[int, int, int, int],
    margin: int = 0,
) -> bool:

    """ @brief 判断线段是否与矩形相交（含边界），用于折线路由路径的合法性校验
        @param p0 线段起点 (x, y)
        @param p1 线段终点 (x, y)
        @param rect 矩形 (x0, y0, x1, y1)
        @param margin 矩形外扩边距，默认 0
        @return 相交则返回 True
        @note 处理水平和垂直线段的退化情况，避免除以零
    """
    x0, y0, x1, y1 = rect
    x0 -= margin
    y0 -= margin
    x1 += margin
    y1 += margin
    ax, ay = p0
    bx, by = p1
    if (x0 < ax < x1 and y0 < ay < y1) or (x0 < bx < x1 and y0 < by < y1):
        return True
    if ax == bx:
        return x0 <= ax <= x1 and min(ay, by) <= y1 and max(ay, by) >= y0
    if ay == by:
        return y0 <= ay <= y1 and min(ax, bx) <= x1 and max(ax, bx) >= x0
    for x in (x0, x1):
        t = (x - ax) / (bx - ax)
        if 0 <= t <= 1:
            y = ay + t * (by - ay)
            if y0 <= y <= y1:
                return True
    for y in (y0, y1):
        t = (y - ay) / (by - ay)
        if 0 <= t <= 1:
            x = ax + t * (bx - ax)
            if x0 <= x <= x1:
                return True
    return False


def assert_no_unrelated_crossing(name: str, points: list[tuple[float, float]], forbidden: dict[str, tuple[int, int, int, int]]) -> None:

    """ @brief 断言折线路径不穿越禁止区域中的任何矩形，用于保证绕行路径的视觉清晰度
        @param name 路径名称，用于错误信息
        @param points 折线顶点列表 [(x, y), ...]
        @param forbidden 禁止穿越的矩形字典 {名称: (x0,y0,x1,y1), ...}
        @throws AssertionError 当任一线段穿越任一禁止矩形时抛出，帮助开发期发现视觉冲突
        @note 本函数是绘图质量保障而非运行期功能断言——穿越不会导致数据错误但会使图不可读
    """
    for p0, p1 in zip(points, points[1:]):
        for rect_name, rect in forbidden.items():
            if segment_intersects_rect(p0, p1, rect, margin=3):
                raise AssertionError(f"{name} segment {p0}->{p1} crosses {rect_name} {rect}")


def polyline_arrow(draw: ImageDraw.ImageDraw, points: list[tuple[float, float]], color: str = LINE, width: int = 4) -> None:

    """ @brief 沿多点折线路径绘制带箭头的连接线，用于绕行和反馈路径。
        @param draw PIL ImageDraw 绘制上下文。
        @param points 折线顶点列表 [(x,y), ...]。
        @param color 线条颜色，默认 LINE。
        @param width 线宽（像素），默认 4。
        @return 无返回值。
        @throws ValueError 当顶点数少于 2 时抛出。
        @note 最后一个点为箭头尖端，倒数第二个点为箭杆终点，其余点直线连接。
    """
    if len(points) < 2:
        raise ValueError("polyline_arrow needs at least two points")
    *shaft, start_last, end = points
    sx, sy = start_last
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    line_points = [*shaft, start_last, line_end]
    for a, b in zip(line_points, line_points[1:]):
        draw.line([a, b], fill=color, width=width)
    px, py = -uy, ux
    pts = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=color)


def table(draw: ImageDraw.ImageDraw, x0: int, y0: int, headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 78) -> None:

    """ @brief 绘制带表头的圆角数据表格，含行分隔线和列分隔线。
        @param draw PIL ImageDraw 绘制上下文。
        @param x0 表格左上角 X 坐标。
        @param y0 表格左上角 Y 坐标。
        @param headers 表头文本列表。
        @param rows 数据行列表，每行为字符串列表。
        @param widths 每列宽度列表（像素）。
        @param row_h 每行高度（像素），默认 78。
        @return 无返回值。
        @note 表格是教学图中展示 checkpoint、寄存器映射、对比规则等结构化信息的主要组件。
    """
    total_w = sum(widths)
    total_h = row_h * (len(rows) + 1)
    draw.rounded_rectangle((x0, y0, x0 + total_w, y0 + total_h), radius=8, fill=WHITE, outline="#607d8b", width=2)
    x = x0
    for header, width in zip(headers, widths):
        draw.rectangle((x, y0, x + width, y0 + row_h), fill="#e3f2fd", outline="#b0bec5", width=1)
        centered(draw, (x + 10, y0 + 6, x + width - 10, y0 + row_h - 6), wrap(draw, header, TABLE_HEAD, width - 20), TABLE_HEAD)
        x += width
    y = y0 + row_h
    for row in rows:
        x = x0
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill=WHITE, outline="#cfd8dc", width=1)
            centered(draw, (x + 10, y + 6, x + width - 10, y + row_h - 6), wrap(draw, value, TABLE, width - 20), TABLE)
            x += width
        y += row_h


def main() -> None:

    """ @brief 绘制本文件对应的教学示意图，输出为 PNG 格式
        @note 本脚本是单文件渲染器，通过 PIL 直接绘制，不依赖外部图表库
        @note 输出路径由全局变量 OUT 定义，对应 docs/L3/assets/ 下的同名 PNG
    """
    width, height = 2600, 2500
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((width / 2, 58), "T14.5 Soft Buffer and HARQ Memory Architecture", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Protocol identity selects the logical evidence store; implementation maps it to banks, transactions and lifecycle states."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    lte_ctx = (80, 170, 620, 350)
    nr_ctx = (1980, 170, 2520, 350)
    lte_addr = (80, 445, 620, 650)
    nr_addr = (1980, 445, 2520, 650)
    manager = (760, 210, 1840, 430)
    journal = (760, 515, 1840, 690)
    banks = (520, 805, 2080, 1045)
    sat = (80, 805, 430, 1045)
    masks = (2170, 805, 2520, 1045)
    life = (80, 1210, 2520, 1465)

    card(draw, lte_ctx, "LTE Turbo context", "Key: harq_id, codeword, TB epoch and CB id. RV belongs to the access transaction, not to a separate cache copy.", BLUE)
    card(draw, nr_ctx, "NR LDPC context", "Key extends with CBG id and CBGTI/CBGFI policy. Unscheduled CBG keeps old evidence.", GREEN)
    card(draw, manager, "Soft Buffer Manager", "Looks up logical evidence, opens read-modify-write transactions, applies NDI/epoch/CRC policy and owns release decisions.", AMBER)
    card(draw, lte_addr, "LTE address walk", "TS 36.212: per-CB circular buffer, NIR/Ncb, E and rvidx. NULL positions are skipped.", BLUE)
    card(draw, nr_addr, "NR address walk", "TS 38.212/38.214: per-CB k0/RV, E_r, CBGTI mask and optional CBGFI flush/combine.", GREEN)
    card(draw, journal, "Transaction Journal", "prepare -> write-combine -> commit. Reset, timeout or abort rolls back partial writes or marks them invalid.", PURPLE)
    card(draw, sat, "Saturation Unit", "Same code-bit address: old LLR + new LLR, then clamp to configured signed range and count sat events.", RED)
    card(draw, masks, "Masks and Status", "observed, valid, null, scheduled CBG, CB CRC, TB CRC, stale epoch and release eligibility.", GRAY)
    card(draw, banks, "Banked LLR SRAM", "Example mapping: bank = hash(harq, cb, addr) mod B; row = floor(addr / (B * lanes)); lane = addr mod lanes.", WHITE)

    arrow(draw, mid(lte_ctx, "right"), mid(manager, "left", -45))
    arrow(draw, mid(nr_ctx, "left"), mid(manager, "right", -45))
    arrow(draw, mid(lte_addr, "right"), mid(journal, "left"))
    arrow(draw, mid(nr_addr, "left"), mid(journal, "right"))
    arrow(draw, mid(manager, "bottom"), mid(journal, "top"))
    arrow(draw, mid(journal, "bottom"), mid(banks, "top"))
    arrow(draw, mid(sat, "right"), mid(banks, "left"))
    arrow(draw, mid(masks, "left"), mid(banks, "right"))

    release_route = [mid(life, "top", 750), (2050, 1140), (1800, 1140), mid(banks, "bottom", 490)]
    assert_no_unrelated_crossing("release_to_banks", release_route, {"sat": sat, "masks": masks})
    polyline_arrow(draw, release_route, "#78909c")

    table(
        draw,
        80,
        1585,
        ["Layer", "LTE Turbo", "NR LDPC", "Hardware rule"],
        [
            ["Logical key", "harq, codeword, TB epoch, CB", "harq, codeword, TB epoch, CBG, CB", "key selects evidence owner"],
            ["RV placement", "rvidx chooses LTE circular-buffer walk", "rv chooses k0; CBGTI may set E_r = 0", "RV is access metadata"],
            ["Combine", "same address accumulates LLR", "same address accumulates unless CBGFI flushes", "saturating add + sat counter"],
            ["CRC fail", "retain CB/TB evidence for retransmission", "retain scheduled CBG/CB evidence by policy", "never release on partial fail"],
            ["Eviction", "release on TB pass or new epoch", "release on TB pass, CBG flush or new epoch", "reclaim invalid/released only"],
        ],
        [390, 570, 610, 770],
        82,
    )

    draw.rounded_rectangle(life, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((width / 2, 1252), "Lifecycle FSM", font=HEAD, fill=INK, anchor="mm")
    states = [
        ("EMPTY", 210),
        ("ACTIVE_NEW", 560),
        ("ACCUMULATING", 970),
        ("CRC_FAIL_RETAIN", 1420),
        ("RELEASED", 1890),
        ("ABORT_ROLLBACK", 2310),
    ]
    y = 1350
    for label, x in states:
        draw.rounded_rectangle((x - 145, y - 38, x + 145, y + 38), radius=8, fill="#eef7ff", outline="#607d8b", width=2)
        draw.text((x, y), label, font=TABLE_HEAD, fill=INK, anchor="mm")
    for (_, x0), (_, x1) in zip(states[:4], states[1:5]):
        arrow(draw, (x0 + 145, y), (x1 - 145, y), "#607d8b", 3)
    abort_route = [
        (states[2][1], y + 38),
        (states[2][1], y + 92),
        (states[5][1], y + 92),
        (states[5][1], y + 38),
    ]
    state_boxes = {
        label: (x - 145, y - 38, x + 145, y + 38)
        for label, x in states
        if label not in {"ACCUMULATING", "ABORT_ROLLBACK"}
    }
    assert_no_unrelated_crossing("abort_route", abort_route, state_boxes)
    polyline_arrow(draw, abort_route, "#8d6e63", 3)

    note = (80, 2225, 2520, 2425)
    draw.rounded_rectangle(note, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((width / 2, 2265), "Read Order and Checks", font=HEAD, fill=INK, anchor="mm")
    lines = [
        "1. 3GPP identities determine the logical evidence space; bank formula is an implementation example.",
        "2. RV, rvidx, k0 and CBGTI describe one access, while the main cache key names the TB/CB/CBG owner.",
        "3. CRC failure retains evidence; TB pass, CBG flush, new epoch or abort decides release/rollback.",
    ]
    yy = 2315
    for line in lines:
        draw.text((width / 2, yy), line, font=TEXT, fill=MUTED, anchor="mm")
        yy += 36

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
