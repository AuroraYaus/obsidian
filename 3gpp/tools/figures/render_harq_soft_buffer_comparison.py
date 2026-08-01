#!/usr/bin/env python3
""" @file render_harq_soft_buffer_comparison.py
    @brief 渲染 LTE/NR HARQ 软缓存（soft buffer）生命周期的对比教学图。
    @date 2025
    @note 覆盖生命周期、环缓冲区 RV 窗口、CBG 粒度差异和 descriptor 对比表。
    @see render_lte_harq_rv_windows.py 对应的 LTE HARQ RV 窗口详解图
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
OUT_PATH = ROOT / "docs/L2/assets/T11.3_HARQ_soft_buffer_comparison.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#5B6878",
    "line": "#9FB0C2",
    "panel": "#F6F8FB",
    "lte": "#B65B2E",
    "lte_l": "#FFF1E8",
    "nr": "#22785A",
    "nr_l": "#E8F6EF",
    "blue": "#2457A6",
    "blue_l": "#EAF1FB",
    "amber": "#B9841A",
    "amber_l": "#FFF5DD",
    "purple": "#6E55A4",
    "purple_l": "#F1EDFF",
    "bad": "#FFECEF",
}



def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    """ @brief 委托 figure_text_fit.wrap_text 执行自动换行。
        @param draw PIL ImageDraw 实例。
        @param text 待换行的原始文本。
        @param fnt 字体对象。
        @param width 每行最大像素宽度。
        @return 分行后的字符串列表。
    """
    return fit_wrap_text(draw, text, fnt, width)


def center(box: tuple[int, int, int, int]) -> tuple[float, float]:
    """ @brief 返回矩形包围盒的几何中心坐标。
        @param box (left, top, right, bottom) 四元组。
        @return (cx, cy) 中心浮点坐标。
    """
    return ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2)


def draw_centered(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: str | list[str],
    size: int,
    color: str = COL["ink"],
    bold: bool = True,
    gap: int = 7,
) -> None:
    """ @brief 在指定矩形内竖直居中对齐绘制多行文本。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 绘制区域。
        @param lines 待绘制的字符串或字符串列表。
        @param size 字体大小（像素）。
        @param color CSS 颜色字符串，默认 ink。
        @param bold 是否粗体。
        @param gap 行间距。
        @return 无返回值。
    """
    fnt = font(size, bold)
    lines = [lines] if isinstance(lines, str) else lines
    heights = [draw.textbbox((0, 0), line, font=fnt)[3] - draw.textbbox((0, 0), line, font=fnt)[1] for line in lines]
    total = sum(heights) + gap * (len(lines) - 1)
    x = (box[0] + box[2]) / 2
    y = (box[1] + box[3] - total) / 2
    for line, h in zip(lines, heights):
        draw.text((x, y + h / 2), line, font=fnt, fill=color, anchor="mm")
        y += h + gap


def draw_wrapped_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    size: int,
    color: str = COL["ink"],
    bold: bool = True,
    width: int = 600,
    line_gap: int = 34,
) -> int:
    """ @brief 在指定坐标处绘制自动换行的多行文本（左对齐）。
        @param draw PIL ImageDraw 实例。
        @param xy 左上角起始坐标 (x, y)。
        @param text 待绘制的长文本。
        @param size 字体大小。
        @param color 文字颜色。
        @param bold 是否粗体。
        @param width 每行最大像素宽度。
        @param line_gap 行间距（像素）。
        @return 文本最后一行的底部 Y 坐标。
    """
    fnt = font(size, bold)
    y = xy[1]
    for line in wrap(draw, text, fnt, width):
        draw.text((xy[0], y), line, font=fnt, fill=color)
        y += line_gap
    return y


def draw_wrapped_centered(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    size: int,
    color: str = COL["ink"],
    bold: bool = True,
    width: int | None = None,
    gap: int = 7,
) -> None:
    """ @brief 先在指定宽度内自动换行，然后在矩形内竖直居中绘制。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 绘制区域。
        @param text 待绘制的长文本。
        @param size 字体大小。
        @param color 文字颜色。
        @param bold 是否粗体。
        @param width 换行宽度（None 则自动取 box 宽度 - 32）。
        @param gap 行间距。
        @return 无返回值。
    """
    fnt = font(size, bold)
    lines = wrap(draw, text, fnt, width or (box[2] - box[0] - 32))
    draw_centered(draw, box, lines, size=size, color=color, bold=bold, gap=gap)


def node(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    outline: str,
    fill: str = "#FFFFFF",
    size: int = 22,
) -> tuple[int, int, int, int]:
    """ @brief 绘制一个含多行自动换行文本的圆角矩形节点。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 节点区域。
        @param lines 节点内文本行列表。
        @param outline 边框颜色。
        @param fill 背景填充色，默认白色。
        @param size 字体大小，默认 22。
        @return 节点包围盒（传入 box 原样返回）。
    """
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=outline, width=2)
    wrapped: list[str] = []
    fnt = font(size)
    for line in lines:
        wrapped.extend(wrap(draw, line, fnt, box[2] - box[0] - 28))
    draw_centered(draw, box, wrapped, size=size, color=COL["ink"], bold=False, gap=6)
    return box


def boundary_point(box: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    """ @brief 计算矩形边界上与目标方向对齐的交点。
        @param box (left, top, right, bottom) 矩形包围盒。
        @param toward 目标点 (x, y)。
        @return 边界交点坐标 (x, y)。
    """
    cx, cy = center(box)
    dx, dy = toward[0] - cx, toward[1] - cy
    if abs(dx) < 1e-6 and abs(dy) < 1e-6:
        return cx, cy
    half_w = max((box[2] - box[0]) / 2, 1)
    half_h = max((box[3] - box[1]) / 2, 1)
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return cx + dx / scale, cy + dy / scale


def arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color: str, width: int = 3) -> None:
    """ @brief 从起点到终点绘制带三角箭头的直线。
        @param draw PIL ImageDraw 实例。
        @param start 起点坐标 (x, y)。
        @param end 终点坐标（箭头尖位置）。
        @param color CSS 颜色字符串。
        @param width 线条宽度，默认 3。
        @return 无返回值。
        @note 箭头头长 14、头宽 9。
    """
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    head_len, head_w = 14, 9
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    draw.line((start, line_end), fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    back_x = x1 - head_len * math.cos(angle)
    back_y = y1 - head_len * math.sin(angle)
    perp_x = head_w * math.sin(angle)
    perp_y = -head_w * math.cos(angle)
    draw.polygon([(x1, y1), (back_x + perp_x, back_y + perp_y), (back_x - perp_x, back_y - perp_y)], fill=color)


def connect(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str) -> None:
    """ @brief 在两个矩形节点之间绘制连接箭头。
        @param draw PIL ImageDraw 实例。
        @param src 源矩形 (left, top, right, bottom)。
        @param dst 目标矩形。
        @param color CSS 颜色字符串。
        @return 无返回值。
    """
    arrow(draw, boundary_point(src, center(dst)), boundary_point(dst, center(src)), color, 3)


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, color: str, fill: str) -> None:
    """ @brief 绘制带标题的圆角面板。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 面板区域。
        @param title 左上角标题。
        @param color 边框颜色。
        @param fill 背景填充色。
        @return 无返回值。
    """
    draw.rounded_rectangle(box, radius=22, fill=fill, outline=color, width=3)
    draw.text((box[0] + 28, box[1] + 22), title, font=font(31, True), fill=color)


def draw_lifecycles(draw: ImageDraw.ImageDraw) -> int:
    """ @brief 并排绘制 LTE 和 NR HARQ soft buffer 生命周期四阶段流程图。
        @param draw PIL ImageDraw 实例。
        @return 面板底部 Y 坐标。
        @note 左侧 LTE：新数据分配 -> RV0 失败保留 -> RV2 累加 -> CRC pass 释放；右侧 NR 额外包含 CBG 维度。
    """
    y0 = 165
    panel_h = 470
    panel(draw, (70, y0, 900, y0 + panel_h), "LTE HARQ soft buffer 生命周期", COL["lte"], COL["lte_l"])
    panel(draw, (1000, y0, 1830, y0 + panel_h), "NR HARQ soft buffer 生命周期", COL["nr"], COL["nr_l"])
    lte_nodes = [
        ["新数据", "按HARQ进程", "分配/清缓存"],
        ["RV0失败", "soft buffer", "保留LLR"],
        ["RV2重传", "同地址累加", "新地址补证据"],
        ["TB CRC通过", "释放缓存"],
    ]
    nr_nodes = [
        ["新数据/NDI", "按HARQ/TB", "CBG/CB分配"],
        ["CRC失败", "CB/CBG", "状态保留"],
        ["CBGTI部分重传", "只更新", "被调度CBG"],
        ["CRC结果", "释放或", "继续保留"],
    ]
    for left, color, items in [(115, COL["lte"], lte_nodes), (1045, COL["nr"], nr_nodes)]:
        boxes = []
        for i, lines in enumerate(items):
            b = (left + i * 198, y0 + 135, left + i * 198 + 184, y0 + 330)
            boxes.append(node(draw, b, lines, color, "#FFFFFF", 24))
        for a, b in zip(boxes, boxes[1:]):
            connect(draw, a, b, color)
    return y0 + panel_h


def ring_point(cx: int, cy: int, r: int, idx: int, total: int) -> tuple[float, float]:
    """ @brief 计算圆环上第 idx 个位置（从 12 点钟方向开始顺时针）的坐标。
        @param cx 圆心 X。
        @param cy 圆心 Y。
        @param r 半径。
        @param idx 位置索引（0-based）。
        @param total 总位置数。
        @return (x, y) 坐标。
    """
    ang = -math.pi / 2 + 2 * math.pi * idx / total
    return cx + r * math.cos(ang), cy + r * math.sin(ang)


def draw_lte_ring(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    """ @brief 绘制 LTE 环缓冲区 RV 窗口示意图：16 个地址环形排列，RV0 和 RV2 部分重叠。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 面板区域。
        @return 无返回值。
        @note RV0 覆盖地址 0-5，RV2 覆盖地址 4-9，地址 4/5 为重叠区执行 LLR 饱和累加。
    """
    panel(draw, box, "LTE: RV 是同一 ring buffer 的窗口", COL["lte"], COL["lte_l"])
    cx, cy = box[0] + 270, box[1] + 305
    total, radius = 16, 150
    rv0 = {0, 1, 2, 3, 4, 5}
    rv2 = {4, 5, 6, 7, 8, 9}
    for i in range(total):
        x, y = ring_point(cx, cy, radius, i, total)
        if i in rv0 and i in rv2:
            fill, edge = COL["amber_l"], COL["amber"]
        elif i in rv0:
            fill, edge = COL["blue_l"], COL["blue"]
        elif i in rv2:
            fill, edge = COL["lte_l"], COL["lte"]
        else:
            fill, edge = "#FFFFFF", COL["line"]
        node(draw, (int(x - 38), int(y - 34), int(x + 38), int(y + 34)), [str(i)], edge, fill, 24)
    draw.ellipse((cx - 95, cy - 95, cx + 95, cy + 95), outline=COL["line"], width=2)
    draw_centered(draw, (cx - 90, cy - 50, cx + 90, cy + 50), ["soft", "buffer"], 24, COL["muted"])
    draw_wrapped_centered(
        draw,
        (box[0] + 60, box[1] + 525, box[2] - 60, box[1] + 625),
        "RV0: addr 0-5；RV2: addr 4-9；addr 4/5 重叠执行 LLR 饱和累加。",
        24,
        width=700,
    )


def draw_nr_cbg(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    """ @brief 绘制 NR CBG mask 重传粒度示意图：TB -> CBG0/CBG1 -> CB/CB 的层次关系。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 面板区域。
        @return 无返回值。
        @note CBGTI=[0,1] 时 mask=0 的 CBG0 保持不动，mask=1 的 CBG1 按 RV2 更新；CBGFI=1 才合并。
    """
    panel(draw, box, "NR: CBG mask 改变重传粒度", COL["nr"], COL["nr_l"])
    tb = node(draw, (box[0] + 55, box[1] + 110, box[2] - 55, box[1] + 190), ["TB0: NDI=old, RV=2, CBGTI=[0,1], CBGFI=1"], COL["nr"], "#FFFFFF", 24)
    cbg0 = node(draw, (box[0] + 80, box[1] + 250, box[0] + 390, box[1] + 368), ["CBG0 mask=0", "CB0/CB1 保持"], COL["line"], "#F3F6F9", 24)
    cbg1 = node(draw, (box[0] + 460, box[1] + 250, box[0] + 770, box[1] + 368), ["CBG1 mask=1", "CB2/CB3 合并"], COL["nr"], "#FFFFFF", 24)
    connect(draw, tb, cbg0, COL["line"])
    connect(draw, tb, cbg1, COL["nr"])
    cb2 = node(draw, (box[0] + 485, box[1] + 435, box[0] + 745, box[1] + 535), ["CB2 RV2", "addr 3-6"], COL["nr"], COL["nr_l"], 24)
    connect(draw, cbg1, cb2, COL["nr"])
    draw_wrapped_centered(
        draw,
        (box[0] + 80, box[1] + 565, box[2] - 80, box[1] + 665),
        "未传输 CBG 不清零、不覆盖；被传输 CBG 按 RV/k0 写回，CBGFI=1 才可与旧实例合并。",
        24,
        width=710,
    )


def draw_middle(draw: ImageDraw.ImageDraw, top: int) -> int:
    """ @brief 绘制中间对比区：左侧 LTE RV 环 + 右侧 NR CBG 粒度图。
        @param draw PIL ImageDraw 实例。
        @param top 本区顶部 Y 坐标。
        @return 本区底部 Y 坐标。
        @throws RuntimeError 当与上一模块间距不足 70px 时抛出。
    """
    y0 = top + 80
    draw_lte_ring(draw, (70, y0, 900, y0 + 700))
    draw_nr_cbg(draw, (1000, y0, 1830, y0 + 700))
    # Geometry spacing assertion: middle panels have enough space under lifecycle panels.
    if y0 - top < 70:
        raise RuntimeError("lifecycle-to-middle spacing too small")
    return y0 + 700


def draw_table(draw: ImageDraw.ImageDraw, top: int) -> int:
    """ @brief 绘制 LTE/NR HARQ descriptor 对比表：soft buffer key、RV、重传粒度、NDI、CRC。
        @param draw PIL ImageDraw 实例。
        @param top 表格顶部 Y 坐标。
        @return 表格底部 Y 坐标。
        @throws RuntimeError 当与上一模块间距不足 95px 时抛出。
        @note 五列：字段、LTE Turbo、NR LDPC、译码器检查；每行高 92。
    """
    y0 = top + 105
    if y0 - top < 95:
        raise RuntimeError("middle-to-table spacing too small")
    x0 = 90
    widths = [250, 465, 465, 465]
    row_h = 92
    rows = [
        ["字段", "LTE Turbo", "NR LDPC", "译码器检查"],
        ["soft buffer key", "harq_id, tb_id, cb_id", "harq_id, tb_id, cbg_id, cb_id", "防止 HARQ 进程串扰"],
        ["RV 字段", "rvidx 选择 Turbo ring 窗口", "RV/k0 选择 LDPC circular buffer 窗口", "RV 必须进入地址生成"],
        ["重传粒度", "TB/CB 主线，无 NR-style CBG", "CBG partial retransmission", "mask=0 的 CBG 保持"],
        ["new data", "NDI toggled 清旧 TB 上下文", "NDI toggled 清 TB/CBG/CB 上下文", "新旧 TB 不能合并"],
        ["CRC fail/pass", "fail 保留，pass 释放", "fail 保留，pass 释放或保留未完成 CBG", "释放条件可追溯"],
    ]
    draw.text((90, y0 - 52), "Descriptor 对比表", font=font(32, True), fill=COL["ink"])
    for r, row in enumerate(rows):
        x = x0
        for c, cell in enumerate(row):
            b = (x, y0 + r * row_h, x + widths[c], y0 + (r + 1) * row_h)
            fill = COL["panel"] if r == 0 or c == 0 else "#FFFFFF"
            draw.rectangle(b, fill=fill, outline=COL["line"], width=1)
            is_head = r == 0 or c == 0
            lines = wrap(draw, cell, font(24, is_head), widths[c] - 34)
            draw_centered(draw, b, lines, 24, COL["ink"], is_head, 6)
            x += widths[c]
    return y0 + len(rows) * row_h


def draw_examples(draw: ImageDraw.ImageDraw, top: int) -> int:
    """ @brief 绘制三个 LLR 累加实例卡片：LTE RV0->RV2、NR CBG partial、定点饱和。
        @param draw PIL ImageDraw 实例。
        @param top 卡片区顶部 Y 坐标。
        @return 卡片区底部 Y 坐标。
        @throws RuntimeError 当间距不足 90px 时抛出。
    """
    y0 = top + 105
    if y0 - top < 90:
        raise RuntimeError("table-to-examples spacing too small")
    draw.text((90, y0), "小型 LLR 累加例子", font=font(32, True), fill=COL["ink"])
    examples = [
        ("LTE RV0 -> RV2", "RV0 addr0..5，RV2 addr4..9；addr4: +2.0 + +1.5 = +3.5；addr6/7/8/9 为新覆盖。"),
        ("NR CBG partial", "CBGTI=[0,1]；CBG0 的 CB0/CB1 本次不写；CBG1 的 CB2/CB3 按 RV2 写回。"),
        ("定点饱和", "6 bit signed LLR：+28 + +10 -> +31；记录正饱和次数，禁止补码回绕。"),
    ]
    x = 90
    boxes = []
    for title, body in examples:
        b = (x, y0 + 70, x + 540, y0 + 250)
        draw.rounded_rectangle(b, radius=18, fill=COL["amber_l"], outline=COL["amber"], width=2)
        draw_centered(draw, (b[0] + 20, b[1] + 18, b[2] - 20, b[1] + 62), [title], 26, COL["ink"], True)
        draw_wrapped_centered(draw, (b[0] + 24, b[1] + 72, b[2] - 24, b[3] - 26), body, 24, COL["ink"], False, 490, 6)
        boxes.append(b)
        x += 590
    return y0 + 300


def draw_footer(draw: ImageDraw.ImageDraw, top: int) -> None:
    """ @brief 绘制底部紫色总结卡片：读图顺序与四条验证重点。
        @param draw PIL ImageDraw 实例。
        @param top 卡片区顶部 Y 坐标。
        @return 无返回值。
        @note 四步验证：生命周期 -> 中部对比 -> 表格字段 dump -> 负测试。
    """
    y0 = top + 95
    b = (90, y0, 1830, y0 + 300)
    draw.rounded_rectangle(b, radius=18, fill=COL["purple_l"], outline=COL["purple"], width=2)
    draw_centered(draw, (b[0] + 28, b[1] + 24, b[2] - 28, b[1] + 72), ["读图顺序与验证重点"], 32, COL["ink"], True)
    checks = [
        "1. 先看生命周期：soft buffer 是译码器状态，CRC fail 后保留，CRC pass 后释放。",
        "2. 再看中部对比：LTE RV 是 ring window；NR CBG mask 决定哪些 CB 本次有新 LLR。",
        "3. 表格字段必须进 dump：LTE 查 RV/k0/Ncb；NR 额外查 CBG mask、CBGFI、BG、Zc。",
        "4. 负测试：HARQ process 串扰、RV mismatch、CBG mask bit order 反、定点饱和回绕。",
    ]
    draw_centered(draw, (b[0] + 28, b[1] + 92, b[2] - 28, b[3] - 28), checks, 24, COL["ink"], False, 13)


def main() -> None:
    """ @brief 脚本入口：生成 T11.3 LTE/NR HARQ Soft Buffer 对比教学图。
        @return 无返回值。
        @note 产出 1900x3040 PNG：生命周期、环缓冲区、CBG 粒度、descriptor 表和 LLR 累加实例。
    """
    img = Image.new("RGB", (1900, 3040), COL["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "T11.3 LTE/NR HARQ Soft Buffer 对比", font=font(44, True), fill=COL["ink"])
    subtitle = "共同点是 LLR soft combining；关键差异是 NR CBG partial retransmission 改变 soft buffer 更新粒度。"
    draw_centered(draw, (70, 112, 1830, 155), subtitle, 26, COL["muted"], False)
    bottom = draw_lifecycles(draw)
    bottom = draw_middle(draw, bottom)
    bottom = draw_table(draw, bottom)
    bottom = draw_examples(draw, bottom)
    draw_footer(draw, bottom)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
