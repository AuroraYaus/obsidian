#!/usr/bin/env python3
""" @file render_t12_5_ber_bler_curve_reporting.py
@brief 渲染 T12.5 BER/BLER 曲线报告流程图，展示从仿真运行到标准化 CSV、曲线绘制和失败诊断的完整报告管线。
@date 2025
"""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T12.5_BER_BLER_curve_reporting.png"



TITLE = font(36, True)
HEAD = font(24, True)
TEXT = font(24)
SMALL = font(24)
TINY = font(24)
axis_font = font(24)


def bbox_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:
    """ @brief 计算文本渲染后的宽高。
    @param draw PIL 绘图上下文。
    @param text 待测量的文本字符串。
    @param fnt PIL 字体对象。
    @return (宽度, 高度) px。
    """
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
    """ @brief 按单词边界自动换行，返回行列表。
    @param draw PIL 绘图上下文。
    @param text 待换行的英文字符串。
    @param fnt PIL 字体对象。
    @param width 最大行宽（px）。
    @return 换行后的行列表。
    """
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        cand = word if not cur else f"{cur} {word}"
        if bbox_size(draw, cand, fnt)[0] <= width:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_h(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    """ @brief 计算单行文本的渲染高度。
    @param draw PIL 绘图上下文。
    @param text 待测量的文本字符串。
    @param fnt PIL 字体对象。
    @return 高度（px）。
    """
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[3] - b[1]


def centered_lines(draw, lines, fnt, x0, y0, x1, y1, fill="#263238", gap=8):
    """ @brief 在矩形区域内居中对齐绘制多行文本。
    @param draw PIL 绘图上下文。
    @param lines 文本行列表。
    @param fnt PIL 字体对象。
    @param x0 矩形左边界。
    @param y0 矩形上边界。
    @param x1 矩形右边界。
    @param y1 矩形下边界。
    @param fill 文本颜色 hex 字符串。
    @param gap 行间距，默认 8px。
    @return None
    """
    heights = [text_h(draw, line, fnt) for line in lines]
    total = sum(heights) + gap * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    cx = (x0 + x1) / 2
    for line, h in zip(lines, heights):
        draw.text((cx, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + gap


def card(draw, xy, title, body, fill):
    """ @brief 绘制带标题和正文的圆角矩形卡片，用于 BLER 报告流程各阶段。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @param title 卡片标题。
    @param body 正文描述字符串。
    @param fill 填充色 hex 字符串。
    @return None
    """
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=12, fill=fill, outline="#263238", width=2)
    draw.text(((x0 + x1) / 2, y0 + 34), title, font=HEAD, fill="#102027", anchor="mm")
    lines = wrap(draw, body, TINY, x1 - x0 - 44)
    centered_lines(draw, lines, TINY, x0 + 22, y0 + 76, x1 - 22, y1 - 24)


def center(rect):
    """ @brief 计算矩形几何中心坐标。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @return 中心点坐标 (cx, cy)。
    """
    return (rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2


def boundary(src, dst):
    """ @brief 计算从源矩形中心向目标矩形方向的边界交点，用于箭头起点/终点定位。
    @param src 源矩形 (x0, y0, x1, y1)。
    @param dst 目标矩形 (x0, y0, x1, y1)。
    @return 源矩形边界上的交点坐标 (bx, by)。
    """
    sx, sy = center(src)
    dx, dy = center(dst)
    vx, vy = dx - sx, dy - sy
    if vx == 0 and vy == 0:
        return sx, sy
    hw, hh = (src[2] - src[0]) / 2, (src[3] - src[1]) / 2
    tx = hw / abs(vx) if vx else float("inf")
    ty = hh / abs(vy) if vy else float("inf")
    t = min(tx, ty)
    return sx + vx * t, sy + vy * t


def arrow(draw, src, dst):
    """ @brief 绘制两个矩形节点之间的直连箭头。
    @param draw PIL 绘图上下文。
    @param src 源矩形 (x0, y0, x1, y1)。
    @param dst 目标矩形 (x0, y0, x1, y1)。
    @return None
    """
    ax, ay = boundary(src, dst)
    bx, by = boundary(dst, src)
    vx, vy = bx - ax, by - ay
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    end = (bx - ux * head_len, by - uy * head_len)
    draw.line([(ax, ay), end], fill="#37474f", width=4)
    px, py = -uy, ux
    draw.polygon(
        [(bx, by), (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w), (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w)],
        fill="#37474f",
    )


def cell(draw, xy, text, fnt, fill="#263238"):
    """ @brief 在矩形区域内居中绘制单行文本，用于表格单元格。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @param text 待绘制的文本字符串。
    @param fnt PIL 字体对象。
    @param fill 文本颜色 hex 字符串。
    @return None
    """
    draw.text(((xy[0] + xy[2]) / 2, (xy[1] + xy[3]) / 2), text, font=fnt, fill=fill, anchor="mm")


def wrapped_cell(draw, xy, text, fnt, fill="#263238"):
    """ @brief 在单元格内自动换行并居中绘制文本，用于 BLER 表格中较长的描述字段。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @param text 待绘制的文本字符串。
    @param fnt PIL 字体对象。
    @param fill 文本颜色 hex 字符串，默认 "#263238"。
    @return None
    """
    lines = wrap(draw, text, fnt, xy[2] - xy[0] - 18)
    centered_lines(draw, lines, fnt, xy[0] + 9, xy[1] + 4, xy[2] - 9, xy[3] - 4, fill, gap=5)


def draw_curve(draw, xy):
    """ @brief 在指定矩形区域内绘制一幅示意性 BLER 曲线（含坐标轴、数据点和误差棒）。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @return None
    @note 该曲线为示意图，用于教学展示 BLER 报告的标准输出格式，非真实仿真数据。
    """
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=12, fill="#ffffff", outline="#607d8b", width=2)
    draw.text(((x0 + x1) / 2, y0 + 34), "Report-Ready BLER Curve", font=HEAD, fill="#102027", anchor="mm")
    px0, py0, px1, py1 = x0 + 74, y0 + 86, x1 - 48, y1 - 94
    draw.line([(px0, py1), (px1, py1)], fill="#263238", width=3)
    draw.line([(px0, py0), (px0, py1)], fill="#263238", width=3)
    for i, lab in enumerate(["0", "1", "2", "3", "4"]):
        x = px0 + i * (px1 - px0) / 4
        draw.line([(x, py1), (x, py1 + 8)], fill="#263238", width=2)
        draw.text((x, py1 + 28), lab, font=axis_font, fill="#263238", anchor="mm")
    for j, lab in enumerate(["1e-1", "1e-2", "1e-3"]):
        y = py0 + j * (py1 - py0) / 2
        draw.line([(px0 - 8, y), (px0, y)], fill="#263238", width=2)
        draw.text((px0 - 34, y), lab, font=axis_font, fill="#263238", anchor="mm")
    pts = [(px0, py0 + 16), (px0 + 115, py0 + 58), (px0 + 230, py0 + 124), (px0 + 345, py0 + 205), (px1 - 10, py1 - 18)]
    draw.line(pts, fill="#1565c0", width=5)
    for x, y in pts:
        draw.ellipse((x - 8, y - 8, x + 8, y + 8), fill="#1565c0")
        draw.line([(x, y - 22), (x, y + 22)], fill="#1565c0", width=2)
        draw.line([(x - 10, y - 22), (x + 10, y - 22)], fill="#1565c0", width=2)
        draw.line([(x - 10, y + 22), (x + 10, y + 22)], fill="#1565c0", width=2)
    draw.text(((px0 + px1) / 2, y1 - 22), "Eb/N0 (dB)", font=SMALL, fill="#263238", anchor="mm")
    draw.text((px0 + 66, py0 - 28), "BLER (log scale)", font=SMALL, fill="#263238", anchor="mm")


def main() -> None:
    """ @brief 渲染 T12.5 BER/BLER 曲线报告图，保存为 PNG 到 docs/L3/assets/。
    @note 该图展示从仿真运行到标准化 CSV、曲线构建和报告包的报告管线，
     包含 metrics.csv 要求的列定义、BLER 示意曲线和失败诊断闭环流程。
    @return None
    """
    W, H = 2200, 1780
    img = Image.new("RGB", (W, H), "#f9fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((W / 2, 56), "T12.5 BER/BLER Curve Reporting", font=TITLE, fill="#102027", anchor="mm")
    subtitle = "CSV schema, confidence intervals, stopping rules, plots and failure diagnosis for LTE Turbo, NR LDPC and NR Polar"
    centered_lines(draw, wrap(draw, subtitle, TEXT, W - 220), TEXT, 110, 78, W - 110, 124, "#455a64")

    top = [
        (90, 170, 455, 420),
        (540, 170, 905, 420),
        (990, 170, 1355, 420),
        (1440, 170, 1805, 420),
    ]
    titles = ["Simulation Runs", "Normalized CSV", "Curve Builder", "Report Package"]
    bodies = [
        "LTE Turbo, NR LDPC and NR Polar emit metrics.csv, frames.jsonl, seeds and failures.",
        "One row per SNR point: totals, errors, BER, BLER, CI bounds, stop reason and config hash.",
        "Read CSV only; draw log-scale BLER/BER curves with confidence intervals and labels.",
        "Save PNG/PDF, data CSV, command, protocol anchors, failure table and replay pointers.",
    ]
    fills = ["#e3f2fd", "#e8f5e9", "#fff3e0", "#ede7f6"]
    for rect, title, body, fill in zip(top, titles, bodies, fills):
        card(draw, rect, title, body, fill)
    for a, b in zip(top, top[1:]):
        arrow(draw, a, b)

    table = (90, 515, 1135, 1200)
    draw.rounded_rectangle(table, radius=12, fill="#ffffff", outline="#607d8b", width=2)
    draw.text(((table[0] + table[2]) / 2, table[1] + 36), "metrics.csv Required Columns", font=HEAD, fill="#102027", anchor="mm")
    headers = ["Group", "Columns", "Why it matters"]
    rows = [
        ["Identity", "run_id, decoder, channel, config_hash", "compare only like-for-like curves"],
        ["Protocol", "TB/CB/Polar params, CRC mode, rate definition", "tie BLER to protocol objects"],
        ["Counts", "frames, blocks, bits, error counts", "raw evidence before ratios"],
        ["Ratios", "BER, BLER, FER, false-pass", "report values and diagnostics"],
        ["Confidence", "ci_method, ci_low, ci_high", "show statistical uncertainty"],
        ["Stopping", "min frames, min errors, max frames, stop reason", "avoid false zero-BLER claims"],
    ]
    col_edges = [120, 310, 735, 1105]
    row_edges = [580 + i * 84 for i in range(8)]
    for yy in row_edges:
        draw.line([(120, yy), (1080, yy)], fill="#cfd8dc", width=1)
    for xx in col_edges[1:-1]:
        draw.line([(xx, row_edges[0]), (xx, row_edges[-1])], fill="#e0e7ea", width=1)
    for i, h in enumerate(headers):
        cell(draw, (col_edges[i], row_edges[0], col_edges[i + 1], row_edges[1]), h, SMALL, "#102027")
    for r, row in enumerate(rows):
        for c, text in enumerate(row):
            wrapped_cell(draw, (col_edges[c], row_edges[r + 1], col_edges[c + 1], row_edges[r + 2]), text, TINY)

    draw_curve(draw, (1235, 515, 2110, 1200))

    bottom = (90, 1305, 2110, 1700)
    draw.rounded_rectangle(bottom, radius=12, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((W / 2, 1342), "Failure Diagnosis Closure", font=HEAD, fill="#102027", anchor="mm")
    diag = [
        ("Curve anomaly", "non-monotonic BLER, zero-error point, wide CI, algorithm gap"),
        ("Locate SNR row", "config hash, seed range, stop reason, confidence_limited flag"),
        ("Open failures", "frames.jsonl, first mismatch, CRC status, syndrome or PM trace"),
        ("Replay vector", "vector.json, input_llr.npy, descriptor, protocol evidence anchors"),
        ("Classify root cause", "LLR sign, rate recovery, CRC boundary, decoder algorithm, quantization"),
    ]
    x = 145
    boxes = []
    for title, body in diag:
        rect = (x, 1400, x + 350, 1595)
        boxes.append(rect)
        card(draw, rect, title, body, "#fce4ec")
        x += 390
    for a, b in zip(boxes, boxes[1:]):
        arrow(draw, a, b)
    centered_lines(
        draw,
        ["Never report BLER=0 without an upper bound or confidence note; every plotted point must link back to CSV, seeds, command and protocol anchors."],
        SMALL,
        bottom[0] + 40,
        1628,
        bottom[2] - 40,
        1685,
        "#37474f",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
