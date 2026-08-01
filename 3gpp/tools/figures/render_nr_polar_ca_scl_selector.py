#!/usr/bin/env python3
"""@file render_nr_polar_ca_scl_selector.py
@brief 渲染 CRC 辅助 SCL（CA-SCL）最终路径选择示例图，展示 PM 排名与 CRC/RNTI 过滤后选择最佳候选的过程。
@date 2025
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T10.6_NR_Polar_CA_SCL_final_selector.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#5B6778",
    "line": "#91A1B7",
    "blue": "#2457A6",
    "blue_fill": "#EAF1FB",
    "green": "#237A57",
    "green_fill": "#E8F6EF",
    "red": "#B83E4A",
    "red_fill": "#FCEBED",
    "orange": "#B7662D",
    "orange_fill": "#FFF2E6",
    "gray_fill": "#F7F9FC",
}



def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], fill: str) -> None:
    """@brief 绘制带箭头线段，连接流程节点。
    @param draw PIL ImageDraw 绘制上下文
    @param start 箭头起点坐标 (x, y)
    @param end 箭头终点坐标 (x, y)
    @param fill 线条和箭头填充颜色
    @return None
    @note 箭杆线宽 3px，箭头长度 14px、宽度 8px。
    """
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length == 0:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    px, py = -uy, ux
    head_len, head_w = 14, 8
    line_end = (x1 - ux * head_len, y1 - uy * head_len)
    draw.line((x0, y0, *line_end), fill=fill, width=3)
    pts = [
        (x1, y1),
        (x1 - ux * head_len + px * head_w, y1 - uy * head_len + py * head_w),
        (x1 - ux * head_len - px * head_w, y1 - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=fill)


def center_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], text: str, fnt: ImageFont.ImageFont, fill: str) -> None:
    """@brief 在矩形区域内居中绘制文本，使用 PIL 的 anchor="mm" 实现精确居中。
    @param draw PIL ImageDraw 绘制上下文
    @param xy 目标矩形区域 (x0, y0, x1, y1)
    @param text 要绘制的文本
    @param fnt PIL 字体对象
    @param fill 文本颜色
    @return None
    """
    draw.text(((xy[0] + xy[2]) / 2, (xy[1] + xy[3]) / 2), text, font=fnt, fill=fill, anchor="mm")


def text_h(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    """@brief 获取文本在指定字体下的像素高度。
    @param draw PIL ImageDraw 绘制上下文
    @param text 要测量的文本
    @param fnt PIL 字体对象
    @return 文本的像素高度（整数）
    """
    box_xy = draw.textbbox((0, 0), text, font=fnt)
    return box_xy[3] - box_xy[1]


def centered_lines(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    lines: list[str],
    fnt: ImageFont.ImageFont,
    fill: str,
    gap: int = 8,
) -> None:
    """@brief 在指定区域内垂直居中绘制多行文本，整体文本块在区域内水平和垂直居中对齐。
    @param draw PIL ImageDraw 绘制上下文
    @param xy 目标矩形区域 (x0, y0, x1, y1)
    @param lines 多行文本字符串列表
    @param fnt PIL 字体对象
    @param fill 文本颜色
    @param gap 行间距（像素），默认 8
    @return None
    """
    heights = [text_h(draw, line, fnt) for line in lines]
    total = sum(heights) + gap * max(0, len(lines) - 1)
    y = xy[1] + (xy[3] - xy[1] - total) / 2
    x = (xy[0] + xy[2]) / 2
    for line, height in zip(lines, heights):
        draw.text((x, y + height / 2), line, font=fnt, fill=fill, anchor="mm")
        y += height + gap


def box(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, lines: list[str], fill: str, outline: str) -> None:
    """@brief 绘制带标题和多行正文的圆角信息框，用于流程节点和状态说明。
    @param draw PIL ImageDraw 绘制上下文
    @param xy 矩形区域 (x0, y0, x1, y1)
    @param title 框内左上角标题（24px 粗体）
    @param lines 正文多行文本列表
    @param fill 框内填充色
    @param outline 边框和标题颜色（2px）
    @return None
    """
    draw.rounded_rectangle(xy, radius=14, fill=fill, outline=outline, width=2)
    draw.text((xy[0] + 24, xy[1] + 16), title, font=font(24, True), fill=outline)
    body = (xy[0] + 28, xy[1] + 72, xy[2] - 28, xy[3] - 26)
    centered_lines(draw, body, lines, font(24), COL["ink"], gap=10)


def main() -> None:
    """@brief 脚本入口：生成 CRC 辅助 SCL 最终路径选择教学图 T10.6_NR_Polar_CA_SCL_final_selector.png。
    @note 图中展示 L=4 路径的 SCL 输出候选经过并行 CRC/RNTI 检查后由 final selector 选出最佳路径的过程。
    关键教学点：最终输出不是 PM 最小路径，而是通过 CRC/RNTI 检查的最佳候选。
    底部表格列出一条具体路径选择案例：P0(PM=0.8, CRC fail) 被淘汰，P1(PM=1.3, CRC pass) 被选中。
    @see render_nr_polar_decoder_chain_overview.py Polar 译码链路总览
    """
    img = Image.new("RGB", (2000, 1280), COL["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "T10.6 CRC-aided SCL：PM 排名与 CRC/RNTI 最终选择", font=font(34, True), fill=COL["ink"])
    draw.text(
        (70, 94),
        "例子展示最佳 PM 路径 CRC fail，次优路径 CRC pass；最终输出不是 PM 最小路径，而是通过 CRC/RNTI 的最佳候选。",
        font=font(24),
        fill=COL["muted"],
    )

    box(
        draw,
        (80, 190, 475, 435),
        "SCL 输出候选",
        ["L=4 paths", "每条含 bits、PM", "每条含 CRC/RNTI context", "PM 越小越好"],
        COL["gray_fill"],
        COL["line"],
    )
    box(
        draw,
        (610, 190, 1035, 435),
        "并行 CRC/RNTI 检查",
        ["P0: PM=0.8 -> fail", "P1: PM=1.3 -> pass", "P2: PM=2.0 -> fail", "P3: PM=3.6 -> pass"],
        COL["blue_fill"],
        COL["blue"],
    )
    box(
        draw,
        (1170, 190, 1555, 435),
        "Final selector",
        ["先过滤 CRC/RNTI pass", "再按 PM 选最小", "selected: P1", "输出 payload"],
        COL["green_fill"],
        COL["green"],
    )
    box(
        draw,
        (1620, 190, 1855, 435),
        "输出",
        ["P1 bits", "status=valid", "context match"],
        COL["green_fill"],
        COL["green"],
    )

    arrow(draw, (475, 312), (610, 312), COL["line"])
    arrow(draw, (1035, 312), (1170, 312), COL["line"])
    arrow(draw, (1555, 312), (1620, 312), COL["green"])

    # Candidate table.
    tx = 145
    ty = 575
    col_w = [130, 310, 145, 160, 170, 260, 330]
    row_h = 64  # TEXT_FIT_OK: candidate rows use short path/PM/CRC labels centered at 24px.
    headers = ["rank", "path bits", "PM", "CRC", "RNTI", "selector view", "result"]
    rows = [
        ["1", "P0: 101011", "0.8", "fail", "n/a", "discard", "best PM but invalid"],
        ["2", "P1: 101001", "1.3", "pass", "match", "candidate #1", "selected"],
        ["3", "P2: 001001", "2.0", "fail", "n/a", "discard", "invalid"],
        ["4", "P3: 111001", "3.6", "pass", "match", "candidate #2", "kept as backup"],
    ]

    draw.text((tx, ty - 54), "完整路径选择表：CRC 是路径选择辅助，不是替代 SCL 的树译码", font=font(25, True), fill=COL["ink"])
    cx = tx
    for htxt, cw in zip(headers, col_w):
        cell = (cx, ty, cx + cw, ty + row_h)
        draw.rectangle(cell, fill=COL["blue_fill"], outline=COL["line"])
        center_text(draw, cell, htxt, font(24, True), COL["blue"])
        cx += cw
    for r, row in enumerate(rows):
        cy = ty + row_h * (r + 1)
        fill = COL["green_fill"] if row[-1] == "selected" else COL["red_fill"] if row[3] == "fail" else COL["orange_fill"]
        cx = tx
        for cell, cw in zip(row, col_w):
            cell_box = (cx, cy, cx + cw, cy + row_h)
            draw.rectangle(cell_box, fill=fill, outline=COL["line"])
            is_key = cell in {"selected", "pass", "fail", "match", "discard"}
            center_text(draw, cell_box, cell, font(24, is_key), COL["ink"])
            cx += cw

    note = (145, 995, 1855, 1230)
    draw.rounded_rectangle(note, radius=14, fill=COL["orange_fill"], outline=COL["orange"], width=2)
    draw.text((note[0] + 24, note[1] + 20), "工程检测点", font=font(26, True), fill=COL["orange"])
    notes = [
        "1. 只选 PM 最小会误选 P0；只看 CRC pass 不排序会在 P1/P3 之间不稳定。",
        "2. DCI blind detection 必须带 RNTI context；CRC pass 但 RNTI 不匹配仍不能输出。",
        "3. 多路径 CRC checker 要和 path reorder 同步，否则 CRC 结果可能贴到错误路径。",
    ]
    y = note[1] + 62
    for line in notes:
        draw.text((note[0] + 24, y), line, font=font(24), fill=COL["ink"])
        y += 42

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
