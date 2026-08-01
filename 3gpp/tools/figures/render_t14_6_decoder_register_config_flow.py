#!/usr/bin/env python3
""" @file render_t14_6_decoder_register_config_flow.py
    @brief 渲染 T14.6 译码器寄存器映射和配置流程图——协议字段来源、寄存器分组和 LOCK_DESCRIPTOR FSM 状态机
    @date 2025
    @see render_t14_4_unified_decoder_subsystem.py 统一译码子系统，Config Registers 模块的详细实现
    @see render_t14_5_soft_buffer_harq_memory.py 软缓冲配置字段 SOFTBUF_CFG 的语义注释
"""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T14.6_decoder_register_map_configuration_flow.png"



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


def centered(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    lines: list[str],
    fnt: ImageFont.ImageFont,
    fill: str = INK,
    gap: int = 7,
) -> None:

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
    title_font = HEAD if text_size(draw, title, HEAD)[0] <= (x1 - x0 - 52) else font(24, True)
    draw.text(((x0 + x1) / 2, y0 + 36), title, font=title_font, fill=INK, anchor="mm")
    centered(draw, (x0 + 24, y0 + 84, x1 - 24, y1 - 24), wrap(draw, body, TEXT, x1 - x0 - 48), TEXT, MUTED)


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


def boundary_point(rect: tuple[int, int, int, int], side: str, offset: int = 0) -> tuple[float, float]:

    """ @brief 计算矩形指定边中点的坐标，用于箭头起止定位（委托 mid）。
        @param rect 矩形 (x0, y0, x1, y1)。
        @param side 边的方向: "left"、"right"、"top"、"bottom"。
        @param offset 沿边方向的偏移量，默认 0。
        @return 边中点坐标 (x, y)。
    """
    return mid(rect, side, offset)


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


def table(
    draw: ImageDraw.ImageDraw,
    x0: int,
    y0: int,
    headers: list[str],
    rows: list[list[str]],
    widths: list[int],
    row_h: int = 86,
) -> None:

    """ @brief 绘制带表头的圆角数据表格，含行分隔线和列分隔线。
        @param draw PIL ImageDraw 绘制上下文。
        @param x0 表格左上角 X 坐标。
        @param y0 表格左上角 Y 坐标。
        @param headers 表头文本列表。
        @param rows 数据行列表，每行为字符串列表。
        @param widths 每列宽度列表（像素）。
        @param row_h 每行高度（像素），默认 86。
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
    width, height = 2800, 2500
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((width / 2, 58), "T14.6 Decoder Register Map and Configuration Flow", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Protocol-derived fields, scheduler context and implementation policy are locked into one auditable hardware task."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    sources = [
        ((80, 175, 600, 355), "36.212 / 38.212", "Algorithm parameters: Turbo K/f1/f2/E/Ncb, LDPC BG/Zc/k0/E, Polar N/K/E/CRC context.", BLUE),
        ((720, 175, 1240, 355), "38.214 / 36.213", "Scheduler context: MCS, Qm, target rate, TBS, RV, HARQ process, NDI and CBG mask.", GREEN),
        ((1360, 175, 1880, 355), "MAC / RRC", "Configured limits: HARQ process count, CBG capability, MCS tables and serving-cell context. Exact fields pending where noted.", AMBER),
        ((2000, 175, 2520, 355), "Implementation Policy", "List size, max iterations, timeout, trace mask, IRQ enable, LLR width and error handling.", PURPLE),
    ]
    for rect, title, body, fill in sources:
        card(draw, rect, title, body, fill)

    regs = [
        ((90, 520, 430, 710), "CAPABILITY", "families, llr widths, banks, trace depth", GRAY),
        ((480, 520, 820, 710), "COMMON_CFG", "family, task_id, carrier, cw, cb, llr_width", BLUE),
        ((870, 520, 1210, 710), "SOFTBUF_CFG", "harq_id, ndi, rv, cbg_mask, cbgfi, sat_mode", GREEN),
        ((1260, 520, 1600, 710), "TURBO_CFG", "K, f1, f2, E, Ncb, max_iter", AMBER),
        ((1650, 520, 1990, 710), "LDPC_CFG", "BG, Zc, iLS, E, Ncb, max_iter", AMBER),
        ((2040, 520, 2380, 710), "POLAR_CFG", "N, K, E, list_size, crc_type, mask_hash", AMBER),
        ((2430, 520, 2710, 710), "CTRL / IRQ", "start, abort, busy, done, error, irq, trace", RED),
    ]
    for rect, title, body, fill in regs:
        card(draw, rect, title, body, fill)

    for i, (src_rect, _, _, _) in enumerate(sources):
        dst_rect = regs[min(i + 1, len(regs) - 1)][0]
        arrow(draw, boundary_point(src_rect, "bottom"), boundary_point(dst_rect, "top"), "#607d8b", 3)
    for (a, *_), (b, *__) in zip(regs, regs[1:]):
        arrow(draw, boundary_point(a, "right"), boundary_point(b, "left"), "#78909c", 3)

    fsm_title = (90, 825, 2710, 875)
    centered(draw, fsm_title, ["Configuration FSM: descriptor writes are mutable only before LOCK_DESCRIPTOR"], HEAD, INK)
    fsm = [
        ((120, 920, 410, 1055), "IDLE", "no active task", BLUE),
        ((470, 920, 760, 1055), "WRITE_CFG", "software writes fields", GREEN),
        ((820, 920, 1110, 1055), "LOCK_DESCRIPTOR", "freeze snapshot", AMBER),
        ((1170, 920, 1460, 1055), "LEGALITY_CHECK", "range and source checks", PURPLE),
        ((1520, 920, 1810, 1055), "START", "one-cycle launch", RED),
        ((1870, 920, 2160, 1055), "BUSY", "engine owns task", GRAY),
        ((2220, 920, 2510, 1055), "DONE / ERROR", "status + irq", BLUE),
    ]
    for rect, title, body, fill in fsm:
        card(draw, rect, title, body, fill)
    for (a, *_), (b, *__) in zip(fsm, fsm[1:]):
        arrow(draw, boundary_point(a, "right"), boundary_point(b, "left"), "#546e7a", 3)

    table(
        draw,
        120,
        1180,
        ["Register group", "Representative fields", "Field source", "Receiver-side consequence"],
        [
            ["COMMON_CFG", "family, K/N/E, cb index, llr width", "36.212 / 38.212 + local descriptor", "selects engine and input/output buffer size"],
            ["SOFTBUF_CFG", "HARQ ID, NDI, RV, CBG mask, CBGFI", "38.214, 36.213 pending, MAC context", "selects old evidence, flush/combine and release policy"],
            ["TURBO_CFG", "K, f1, f2, E, Ncb, max iter", "36.212 Table 5.1.3-3 and rate matching", "drives LTE Turbo interleaver and circular-buffer recovery"],
            ["LDPC_CFG", "BG, Zc, iLS, k0, E, Ncb", "38.212 LDPC segmentation, lifting and bit selection", "drives parity-check schedule, address generator and RV window"],
            ["POLAR_CFG", "N, K, E, list size, CRC type", "38.212 Polar construction/rate matching + implementation policy", "drives frozen mask, rate recovery and CA-SCL selector"],
            ["CTRL / STATUS", "start, abort, busy, pass/fail, error code, IRQ", "implementation interface", "turns protocol task into a recoverable hardware transaction"],
        ],
        [380, 650, 690, 780],
        row_h=94,
    )

    table(
        draw,
        120,
        1950,
        ["Rule", "Engineering check"],
        [
            ["Do not write while BUSY", "writes after LOCK_DESCRIPTOR either ignored or raise ERR_WRITE_WHILE_BUSY"],
            ["Protocol vs policy", "list_size and max_iterations are implementation policy, not 3GPP forced values"],
            ["Evidence logging", "trace descriptor hash, bad field id, source group and final status for every task"],
        ],
        [620, 1940],
        row_h=92,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
