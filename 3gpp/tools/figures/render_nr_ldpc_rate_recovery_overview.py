#!/usr/bin/env python3
"""@file render_nr_ldpc_rate_recovery_overview.py
@brief 渲染 NR LDPC 接收侧速率恢复（rate recovery）总览图，展示从解调 LLR 到 LDPC 译码器输入的反交织、循环缓存恢复和软合并链路。
@date 2025
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
OUT_PATH = ROOT / "docs/L2/assets/T9.1_NR_LDPC_rate_recovery_overview.png"

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
    "panel": "#F7F9FC",
}



def center_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    """@brief 在给定矩形区域内居中绘制文本，用于流程节点和表格单元格的文字居中对齐。
    @param draw PIL ImageDraw 绘制上下文
    @param box 目标矩形区域 (x0, y0, x1, y1)
    @param text 要绘制的文本内容
    @param fnt PIL 字体对象
    @param fill 文本颜色（十六进制字符串）
    @return None
    """
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill: str, width: int, gap: int = 6) -> int:
    """@brief 在指定宽度内自动换行绘制文本，返回绘制结束后的 y 坐标用于链式布局。
    @param draw PIL ImageDraw 绘制上下文
    @param xy 起始左上角坐标 (x, y)
    @param text 需要换行的长文本
    @param fnt PIL 字体对象
    @param fill 文本颜色
    @param width 文字最大宽度（像素）
    @param gap 行间距（像素），默认 6
    @return 绘制结束后的 y 坐标，便于连续排版
    """
    x, y = xy
    for line in fit_wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#61758A") -> None:
    """@brief 绘制带箭头线段，连接流程节点表示数据流向。
    @param draw PIL ImageDraw 绘制上下文
    @param start 箭头起点坐标 (x, y)
    @param end 箭头终点坐标 (x, y)
    @param color 线条和箭头填充颜色，默认 "#61758A"
    @return None
    @note 箭杆线宽 3px，箭头长度 14px、宽度 8px。
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


def node(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, body: str, fill: str, stripe: str) -> None:
    """@brief 绘制带彩色顶部条纹的流程节点框，用于展示译码链路上的处理步骤。
    @param draw PIL ImageDraw 绘制上下文
    @param box 矩形区域 (x0, y0, x1, y1)
    @param title 节点标题（粗体，24px）
    @param body 节点正文（24px，自动换行）
    @param fill 框内填充色
    @param stripe 顶部 12px 彩色条纹颜色，同时作为视觉分类标记
    @return None
    """
    draw.rounded_rectangle(box, radius=12, fill=fill, outline=PALETTE["line"], width=2)
    draw.rounded_rectangle((box[0], box[1], box[2], box[1] + 12), radius=12, fill=stripe, outline=stripe)
    center_text(draw, (box[0] + 10, box[1] + 24, box[2] - 10, box[1] + 62), title, font(24, True), PALETTE["ink"])
    draw_wrapped(draw, (box[0] + 16, box[1] + 72), body, font(24), PALETTE["muted"], box[2] - box[0] - 32, gap=5)


def draw_chain(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制接收侧 rate recovery 的五个主处理节点水平链路（Demapper -> Deinterleaver -> Circular restore -> Soft combine -> LDPC core）。
    @param draw PIL ImageDraw 绘制上下文
    @return None
    @note 五个节点从左到右水平排列，节点间用箭头连接。
    每个节点包含标题、功能描述和彩色顶部条纹用于视觉区分。
    """
    draw.text((70, 180), "接收侧 rate recovery 主链路", font=font(28, True), fill=PALETTE["blue"])
    nodes = [
        ("Demapper LLR", "顺序软信息 rx_llr[0:E-1]", "#EAF6FF", PALETTE["blue"]),
        ("Bit deinterleaver", "按 Qm 反交织，恢复 bit 顺序", "#F4F0FF", PALETTE["purple"]),
        ("Circular restore", "按 RV 起点扫描 Ncb，跳过空位，写回母码位置", "#F0F7F4", PALETTE["green"]),
        ("Soft combine", "重复位 LLR 累加，未发送位保持未知", "#FFF7E5", PALETTE["amber"]),
        ("LDPC core", "输出 ldpc_llr[0:N-1] 给 BG/Zc/H", "#FFF4D8", PALETTE["red"]),
    ]
    x = 70
    y = 252
    w = 250
    h = 150
    boxes = []
    for title, body, fill, stripe in nodes:
        box = (x, y, x + w, y + h)
        node(draw, box, title, body, fill, stripe)
        boxes.append(box)
        x += w + 56
    for left, right in zip(boxes, boxes[1:]):
        arrow(draw, (left[2], y + 75), (right[0], y + 75))


def draw_buffer_example(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制小型循环缓存（circular buffer）示例，展示 new/repeat/short/unknown 四种 LLR 状态及图例。
    @param draw PIL ImageDraw 绘制上下文
    @return None
    @note 展示 12 个位置的循环缓冲区：new（首次写入）、repeat（重复观测累加）、short（shortened/filler 强已知 0）、unknown（未发送中性 LLR）。
    """
    draw.text((70, 482), "小型 circular buffer 例子：新写入、重复、未知和 shortened", font=font(28, True), fill=PALETTE["green"])
    x0, y0 = 80, 552
    cell_w = 102
    header_h = 42
    value_h = 38
    cell_h = header_h + value_h
    labels = list(range(12))
    values = ["+1.0", "-1.4", "+8.0", "0", "+0.2", "-1.5", "?", "+1.4", "-0.8", "+0.6", "?", "+0.9"]
    states = ["new", "repeat", "short", "unknown", "new", "repeat", "unknown", "new", "new", "new", "unknown", "new"]
    colors = {
        "new": "#EAF6FF",
        "repeat": "#FFF7E5",
        "short": "#EAF8EF",
        "unknown": "#F2F4F7",
    }
    for i, label in enumerate(labels):
        x = x0 + i * cell_w
        draw.rectangle((x, y0, x + cell_w, y0 + header_h), fill="#EAF3FF", outline=PALETTE["line"], width=1)
        center_text(draw, (x, y0 + 4, x + cell_w, y0 + header_h - 4), f"pos {label}", font(24, True), PALETTE["ink"])
        draw.rectangle((x, y0 + header_h, x + cell_w, y0 + cell_h), fill=colors[states[i]], outline=PALETTE["line"], width=1)
        center_text(draw, (x, y0 + header_h, x + cell_w, y0 + cell_h), values[i], font(24), PALETTE["ink"])
    legend_y = y0 + cell_h + 32
    legend = [
        ("new", "首次写入：rx LLR 放入该母码位置", colors["new"]),
        ("repeat", "重复观测：与旧 LLR 饱和相加", colors["repeat"]),
        ("short", "shortened/filler：强已知 0 或掩码固定", colors["short"]),
        ("unknown", "未发送：中性 LLR，等待校验或重传", colors["unknown"]),
    ]
    x = 80
    for key, text, color in legend:
        draw.rounded_rectangle((x, legend_y, x + 340, legend_y + 112), radius=9, fill=color, outline=PALETTE["line"], width=1)
        text_center_box = (x + 12, legend_y + 10, x + 328, legend_y + 40)
        center_text(draw, text_center_box, key, font(24, True), PALETTE["ink"])
        draw_wrapped(draw, (x + 18, legend_y + 50), text, font(24), PALETTE["muted"], 302, gap=4)
        x += 365


def draw_descriptor_and_checks(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制 rate recovery descriptor 字段表和验证计数器面板，列出关键参数及其错误后果与统计检查项。
    @param draw PIL ImageDraw 绘制上下文
    @return None
    @note descriptor 表包含 BG/Zc/iLS、rvidx/k0、E/Ncb/N、Qm、cb_id/HARQ_id 五个关键字段，每项列出来源协议条款和错误后果。
    右侧列出最小覆盖率统计计数器：new_write_count、repeat_accum_count、unknown_count 等。
    """
    panel = (70, 830, 1530, 1340)
    draw.rounded_rectangle(panel, radius=16, fill="#FFFDF6", outline="#E2CD7A", width=2)
    draw.text((105, 824), "descriptor 与验证计数器", font=font(28, True), fill=PALETTE["ink"])

    headers = ["字段", "来源", "错误后果"]
    rows = [
        ["BG/Zc/iLS", "TS 38.212 §5.3.2", "H 尺寸和地址周期错"],
        ["rvidx/k0", "TS 38.212 §5.4.2.1", "RV 窗口错"],
        ["E/Ncb/N", "TS 38.212 §5.4.2.1", "写入数量或缓存长度错"],
        ["Qm", "TS 38.214 MCS", "解交织顺序错"],
        ["cb_id/HARQ id", "调度与 HARQ 上下文", "软缓存污染"],
    ]
    x0, y0 = 105, 888
    widths = [165, 300, 360]
    row_h = 60  # TEXT_FIT_OK: descriptor table cells are short controlled labels centered at 24px.
    x = x0
    for header, width in zip(headers, widths):
        draw.rectangle((x, y0, x + width, y0 + row_h), fill="#EAF3FF", outline=PALETTE["line"], width=2)
        center_text(draw, (x, y0, x + width, y0 + row_h), header, font(24, True), PALETTE["ink"])
        x += width
    y = y0 + row_h
    for row in rows:
        x = x0
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill="#FFFFFF", outline=PALETTE["line"], width=1)
            center_text(draw, (x + 4, y, x + width - 4, y + row_h), value, font(24), PALETTE["ink"])
            x += width
        y += row_h

    draw.text((920, 888), "最小覆盖率统计", font=font(24, True), fill=PALETTE["ink"])
    checks = [
        "new_write_count",
        "repeat_accum_count",
        "unknown_count",
        "shortened_count",
        "saturation_count",
        "deinterleave_perm_ok",
    ]
    y = 934
    for item in checks:
        draw.rounded_rectangle((920, y, 1288, y + 40), radius=7, fill="#FFFFFF", outline=PALETTE["line"], width=1)
        draw.text((935, y + 8), item, font=font(24), fill=PALETTE["muted"])
        y += 48


def main() -> None:
    """@brief 脚本入口：生成 NR LDPC Rate Recovery 接收侧总览图 T9.1_NR_LDPC_rate_recovery_overview.png。
    @note 图中包含三个主区域：
    - 顶部：五个处理节点的水平链路（Demapper LLR -> Bit deinterleaver -> Circular restore -> Soft combine -> LDPC core）。
    - 中部：小型 circular buffer 示例，展示 new/repeat/short/unknown 四种 LLR 状态。
    - 底部：descriptor 字段表与验证计数器面板。
    @see render_nr_ldpc_reassembly_tb_crc.py LDPC 译码后的 CB 重组与 TB CRC 流程
    """
    img = Image.new("RGB", (1680, 1360), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "NR LDPC Rate Recovery 接收侧总览", font=font(40, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (70, 104),
        "目标：把顺序接收 LLR 流恢复成 LDPC decoder 需要的母码位置软信息。发送端 rate matching 是选择和交织；接收端 rate recovery 是反交织、按 RV 起点放回、软合并和 mask 初始化。",
        font(24),
        PALETTE["muted"],
        1460,
    )
    draw_chain(draw)
    draw_buffer_example(draw)
    draw_descriptor_and_checks(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
