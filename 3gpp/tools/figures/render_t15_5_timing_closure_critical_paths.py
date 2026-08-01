#!/usr/bin/env python3
""" @file render_t15_5_timing_closure_critical_paths.py
@brief 渲染T15.5时序收敛与关键路径调试图 —— 时序收敛是一个受控循环：分类路径、修改架构、重新运行回归证据
@date 2025 """

from __future__ import annotations

from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T15.5_timing_closure_critical_paths.png"



TITLE = font(42, True)
SUB = font(24)
HEAD = font(28, True)
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
    """ @brief 计算文本渲染后的像素尺寸，用于卡片/表格布局中的宽度高度约束判断
    @param draw PIL ImageDraw 绘图上下文
    @param text 待测量的文本字符串
    @param fnt PIL ImageFont 字体对象
    @return (width, height) 文本边界框的宽高像素值
    @note 使用 textbbox 替代已废弃的 textsize 方法 """
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
    """ @brief 按最大像素宽度自动换行，将单行长文本拆分为多行
    @param draw PIL ImageDraw 绘图上下文
    @param text 待换行的原始文本字符串
    @param fnt PIL ImageFont 字体对象
    @param width 每行允许的最大像素宽度
    @return 换行后的字符串列表，每项为一行
    @note 按空格切分单词逐词累加宽度 """
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
    gap: int = 8,
) -> None:
    """ @brief 在指定矩形区域内居中绘制多行文本，自动计算垂直起始位置
    @param draw PIL ImageDraw 绘图上下文
    @param rect (x0, y0, x1, y1) 目标矩形区域
    @param lines 待绘制的文本行列表
    @param fnt PIL ImageFont 字体对象
    @param fill 文本颜色，默认 INK
    @param gap 行间距像素值，默认 8
    @return None """
    x0, y0, x1, y1 = rect
    heights = [text_size(draw, line, fnt)[1] for line in lines]
    total = sum(heights) + gap * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    cx = (x0 + x1) / 2
    for line, height in zip(lines, heights):
        draw.text((cx, y + height / 2), line, font=fnt, fill=fill, anchor="mm")
        y += height + gap


def card(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, body: str, fill: str) -> None:
    """ @brief 绘制一个带圆角边框、标题和正文的语义卡片组件
    @param draw PIL ImageDraw 绘图上下文
    @param rect (x0, y0, x1, y1) 卡片矩形区域
    @param title 卡片标题文本
    @param body 卡片正文文本（自动换行后居中绘制）
    @param fill 卡片背景填充颜色
    @return None """
    x0, y0, x1, y1 = rect
    draw.rounded_rectangle(rect, radius=8, fill=fill, outline="#37474f", width=2)
    draw.text(((x0 + x1) / 2, y0 + 42), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 24, y0 + 92, x1 - 24, y1 - 24), wrap(draw, body, TEXT, x1 - x0 - 48), TEXT, MUTED)


def boundary_point(rect: tuple[int, int, int, int], side: str, offset: int = 0) -> tuple[float, float]:
    """ @brief 计算矩形某条边上的点坐标，用于箭头起止点的精确定位
    @param rect (x0, y0, x1, y1) 矩形区域
    @param side 边的方向："left"/"right"/"top"/"bottom"
    @param offset 沿该边的偏移量（像素）
    @return (x, y) 边界点坐标
    @throws ValueError 当 side 参数不是合法方向时抛出 """
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
    """ @brief 绘制带箭头尖端的直线段，用于表示时序收敛循环流程
    @param draw PIL ImageDraw 绘图上下文
    @param start (x, y) 线段起点坐标
    @param end (x, y) 线段终点坐标（箭头尖端位置）
    @param color 线条和箭头填充颜色，默认 LINE
    @param width 线条宽度像素值，默认 4
    @return None """
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = math.hypot(vx, vy)
    if length == 0:
        return
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill=color, width=width)
    px, py = -uy, ux
    draw.polygon(
        [
            (ex, ey),
            (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
            (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def table(
    draw: ImageDraw.ImageDraw,
    x0: int,
    y0: int,
    headers: list[str],
    rows: list[list[str]],
    widths: list[int],
    row_h: int,
) -> None:
    """ @brief 绘制带圆角外框、表头和交替行颜色的数据表格
    @param draw PIL ImageDraw 绘图上下文
    @param x0 表格左上角 x 坐标
    @param y0 表格左上角 y 坐标
    @param headers 表头文本列表
    @param rows 表格数据行列表
    @param widths 各列宽度像素值列表
    @param row_h 每行的像素高度
    @return None
    @note 数据行交替白色/#fafafa 以提高可读性 """
    total_w = sum(widths)
    total_h = row_h * (len(rows) + 1)
    draw.rounded_rectangle((x0, y0, x0 + total_w, y0 + total_h), radius=8, fill=WHITE, outline="#607d8b", width=2)
    x = x0
    for header, width in zip(headers, widths):
        draw.rectangle((x, y0, x + width, y0 + row_h), fill="#e3f2fd", outline="#b0bec5", width=1)
        centered(draw, (x + 12, y0 + 8, x + width - 12, y0 + row_h - 8), wrap(draw, header, TABLE_HEAD, width - 24), TABLE_HEAD)
        x += width
    y = y0 + row_h
    for idx, row in enumerate(rows):
        x = x0
        fill = WHITE if idx % 2 == 0 else "#fafafa"
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill=fill, outline="#cfd8dc", width=1)
            centered(draw, (x + 12, y + 8, x + width - 12, y + row_h - 8), wrap(draw, value, TABLE, width - 24), TABLE)
            x += width
        y += row_h


def main() -> None:
    """ @brief 渲染T15.5时序收敛与关键路径调试图的主入口
    @note 生成的图片展示从 Timing Report → Classify Path → Architecture Fix → Regression → Tradeoff 的时序收敛循环。
    上半部分为五张流程卡片和设计原则说明，中间为关键路径诊断表（Path/Why slow/Candidate fix/Regression focus），下半部分为优化技术代价分析表（Technique/Improves/Cost/When to use）。
    包含布局间距的自检断言。
    输出至 docs/L3/assets/T15.5_timing_closure_critical_paths.png
    @see render_t15_4_dc_synthesis_flow_decoders.py, render_t15_6_final_evidence_report.py """
    width, height = 3000, 2940
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((width / 2, 58), "T15.5 Timing Closure and Decoder Critical Paths", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Timing closure is a controlled loop: classify the path, change architecture, then re-run regression evidence."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    cards = {
        "report": (90, 180, 520, 410),
        "classify": (630, 180, 1060, 410),
        "fix": (1170, 180, 1600, 410),
        "verify": (1710, 180, 2140, 410),
        "tradeoff": (2250, 180, 2680, 410),
    }
    card(draw, cards["report"], "Timing Report", "startpoint, endpoint, slack, logic depth, cell list and hierarchy context.", BLUE)
    card(draw, cards["classify"], "Classify Path", "Turbo ACS, LDPC min tree, Polar sorter, soft-buffer merge or top-level fan-in.", GREEN)
    card(draw, cards["fix"], "Architecture Fix", "pipeline, retiming, register duplication, tree split, banking or hierarchy change.", AMBER)
    card(draw, cards["verify"], "Regression", "rerun directed vectors, checkpoint alignment, reset/abort and coverage bins.", PURPLE)
    card(draw, cards["tradeoff"], "Tradeoff", "area, latency, power, debug trace, throughput and sign-off risk.", RED)
    for left, right in [("report", "classify"), ("classify", "fix"), ("fix", "verify"), ("verify", "tradeoff")]:
        arrow(draw, boundary_point(cards[left], "right"), boundary_point(cards[right], "left"))

    note = (140, 520, 2860, 710)
    draw.rounded_rectangle(note, radius=8, fill=GRAY, outline="#607d8b", width=2)
    centered(
        draw,
        note,
        [
            "Do not close timing by hiding paths. Every false path, multicycle path, retiming change or added pipeline register needs verification evidence.",
            "The safest fix is the one that improves slack while preserving protocol-derived ordering, reset behavior and scoreboard checkpoints.",
        ],
        TEXT,
        MUTED,
        gap=12,
    )

    table(
        draw,
        120,
        820,
        ["Path", "Why it is slow", "Candidate fix", "Regression focus"],
        [
            ["Turbo ACS", "branch metric plus add-compare-select plus saturation", "pipeline metric update or split window", "iteration trace, extrinsic alignment"],
            ["LDPC min tree", "min1/min2 compare tree, sign parity, bank mux", "split compare tree and register bank select", "layer schedule and syndrome"],
            ["Polar sorter", "path metric update, compare/swap network, lazy-copy mux", "partial sort or staged sorter", "PM tie-break and CRC selector"],
            ["Soft buffer", "key compare, RV address, saturating add, CBG mask merge", "early key hash, pipeline merge", "HARQ reset/abort, held CBG"],
        ],
        [380, 780, 720, 880],
        row_h=122,
    )

    table(
        draw,
        120,
        1590,
        ["Technique", "Improves", "Cost", "When to use"],
        [
            ["Pipeline", "setup slack and frequency", "latency, trace alignment, extra registers", "long arithmetic or compare tree"],
            ["Retiming", "register placement without RTL rewrite", "reset/scan/equivalence complexity", "clean synchronous datapath"],
            ["Register duplication", "fanout and route delay", "area and coherency checks", "status fan-out or shared enables"],
            ["Hierarchy/banking", "memory mux depth and route congestion", "control complexity", "LDPC/soft-buffer memory paths"],
            ["Algorithmic change", "large structural bottlenecks", "BLER/area/power tradeoff", "sorter width, min-sum variant, parallelism"],
        ],
        [420, 620, 760, 960],
        row_h=118,
    )

    foot = (120, 2520, 2880, 2828)
    draw.rounded_rectangle(foot, radius=8, fill=WHITE, outline="#607d8b", width=2)
    centered(
        draw,
        foot,
        [
            "Example diagnostic: slack -0.31 ns in polar_sorter means the first fix candidate is sorter staging, not a protocol workaround.",
            "Every timing fix must update latency assumptions, trace checkpoints, coverage bins and failure bundles before sign-off.",
            "Visual check: arrows are straight two-point shafts with vector-derived heads; table cells use centered 24px text.",
        ],
        TEXT,
        MUTED,
        gap=12,
    )

    title_to_node_gap = cards["report"][1] - 124
    flow_to_table_gap = 820 - note[3]
    bottom_margin = height - foot[3]
    if title_to_node_gap < 36 or flow_to_table_gap < 80 or bottom_margin < 80:
        raise AssertionError(
            "T15.5 local spacing failed: "
            f"title_to_node_gap={title_to_node_gap}, "
            f"flow_to_table_gap={flow_to_table_gap}, bottom_margin={bottom_margin}"
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
