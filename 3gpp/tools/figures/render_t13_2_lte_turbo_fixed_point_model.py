#!/usr/bin/env python3
""" @file render_t13_2_lte_turbo_fixed_point_model.py
@brief 渲染 T13.2 LTE Turbo 定点模型计划图，展示从协议向量到 CRC/报告的 C/C++ 整数数据通路与位精确检查点。
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
OUT = ROOT / "docs/L3/assets/T13.2_LTE_Turbo_fixed_point_model.png"



TITLE = font(40, True)
HEAD = font(26, True)
TEXT = font(24)
SMALL = font(24)
TINY = font(24)


def text_box(draw, text, fnt):
    """ @brief 计算文本渲染后的宽高。
    @param draw PIL 绘图上下文。
    @param text 待测量的文本字符串。
    @param fnt PIL 字体对象。
    @return (宽度, 高度) px。
    """
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0], b[3] - b[1]


def wrap(draw, text, fnt, width):
    """ @brief 按单词边界自动换行，返回行列表。
    @param draw PIL 绘图上下文。
    @param text 待换行的英文字符串。
    @param fnt PIL 字体对象。
    @param width 最大行宽（px）。
    @return 换行后的行列表。
    """
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        cand = word if not cur else f"{cur} {word}"
        if text_box(draw, cand, fnt)[0] <= width:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def line_h(draw, text, fnt):
    """ @brief 计算单行文本的渲染高度。
    @param draw PIL 绘图上下文。
    @param text 待测量的文本字符串。
    @param fnt PIL 字体对象。
    @return 高度（px）。
    """
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[3] - b[1]


def centered(draw, lines, fnt, rect, fill="#263238", gap=7):
    """ @brief 在矩形区域内居中对齐绘制多行文本。
    @param draw PIL 绘图上下文。
    @param lines 文本行列表。
    @param fnt PIL 字体对象。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @param fill 文本颜色 hex 字符串。
    @param gap 行间距，默认 7px。
    @return None
    """
    x0, y0, x1, y1 = rect
    hs = [line_h(draw, line, fnt) for line in lines]
    total = sum(hs) + gap * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    cx = (x0 + x1) / 2
    for line, h in zip(lines, hs):
        draw.text((cx, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + gap


def card(draw, rect, title, body, fill):
    """ @brief 绘制带标题和正文的圆角矩形卡片，用于 Turbo 定点模型各阶段。
    @param draw PIL 绘图上下文。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @param title 卡片标题。
    @param body 正文描述字符串。
    @param fill 填充色 hex 字符串。
    @return None
    """
    x0, y0, x1, y1 = rect
    draw.rounded_rectangle(rect, radius=8, fill=fill, outline="#263238", width=2)
    draw.text(((x0 + x1) / 2, y0 + 32), title, font=HEAD, fill="#102027", anchor="mm")
    centered(draw, wrap(draw, body, TINY, x1 - x0 - 44), TINY, (x0 + 22, y0 + 72, x1 - 22, y1 - 22))


def center(rect):
    """ @brief 计算矩形几何中心坐标。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @return 中心点坐标 (cx, cy)。
    """
    return (rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2


def edge(src, dst):
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
    ax, ay = edge(src, dst)
    bx, by = edge(dst, src)
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


def cell(draw, rect, text, fnt=TINY, fill="#263238"):
    """ @brief 在单元格内自动换行并居中绘制文本，用于 Turbo 定点检查点表格。
    @param draw PIL 绘图上下文。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @param text 待绘制的文本字符串。
    @param fnt PIL 字体对象。
    @param fill 文本颜色 hex 字符串。
    @return None
    """
    centered(draw, wrap(draw, text, fnt, rect[2] - rect[0] - 18), fnt, (rect[0] + 7, rect[1] + 4, rect[2] - 7, rect[3] - 4), fill, gap=4)


def table(draw, rect):
    """ @brief 绘制 Turbo 定点检查点表格，列出速率恢复、分支度量、前后向递推、外信息和 CRC 门控的位精确比较字段。
    @param draw PIL 绘图上下文。
    @param rect 表格外框矩形 (x0, y0, x1, y1)。
    @return None
    """
    x0, y0, x1, y1 = rect
    draw.rounded_rectangle(rect, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text(((x0 + x1) / 2, y0 + 36), "Turbo Fixed-Point Checkpoints", font=HEAD, fill="#102027", anchor="mm")
    cols = [x0 + 35, x0 + 285, x0 + 610, x0 + 940, x1 - 35]
    rows = [y0 + 82, y0 + 145, y0 + 235, y0 + 325, y0 + 415, y0 + 505, y0 + 595]
    headers = ["Stage", "Integer Object", "Compare Field", "Failure Signal"]
    data = [
        ["Rate recovery", "sys/parity LLR, soft buffer", "quantized_input, combined_llr", "RV or address mismatch"],
        ["Branch metric", "G_k for 8-state trellis", "gamma_trace", "stream/sign/scale error"],
        ["Forward/backward", "alpha/beta columns", "alpha_beta_snapshot", "normalization or saturation"],
        ["Extrinsic", "posterior - channel - apriori", "extrinsic_trace", "repeated evidence"],
        ["CRC gate", "hard bits and CB/TB CRC", "crc_status, iter_used", "late first mismatch"],
    ]
    for r in rows:
        draw.line([(cols[0], r), (cols[-1], r)], fill="#cfd8dc", width=1)
    for c in cols:
        draw.line([(c, rows[0]), (c, rows[-1])], fill="#e0e7ea", width=1)
    for i, h in enumerate(headers):
        cell(draw, (cols[i], rows[0], cols[i + 1], rows[1]), h, SMALL, "#102027")
    for r, row in enumerate(data):
        for c, text in enumerate(row):
            cell(draw, (cols[c], rows[r + 1], cols[c + 1], rows[r + 2]), text)


def main():
    """ @brief 渲染 T13.2 LTE Turbo 定点模型计划图，保存为 PNG 到 docs/L3/assets/。
    @note 该图展示从协议向量、LLR 量化器、SISO 核心、迭代交换到 CRC/报告的 C/C++ 整数数据通路，
     包含 Turbo 定点检查点表格和位宽/算法选项卡（Log-MAP/Max-Log-MAP/度量归一化/外信息缩放/饱和计数）。
    @return None
    """
    W, H = 2200, 1780
    img = Image.new("RGB", (W, H), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((W / 2, 56), "T13.2 LTE Turbo Fixed-Point Model Plan", font=TITLE, fill="#102027", anchor="mm")
    subtitle = "C/C++ integer data path, Log-MAP options, interleaver addresses and bit-exact checkpoints"
    centered(draw, wrap(draw, subtitle, TEXT, W - 220), TEXT, (110, 78, W - 110, 124), "#455a64")

    top = [
        (75, 160, 420, 410),
        (500, 160, 845, 410),
        (925, 160, 1270, 410),
        (1350, 160, 1695, 410),
        (1775, 160, 2120, 410),
    ]
    titles = ["Protocol Vector", "LLR Quantizer", "SISO Core", "Iterative Exchange", "CRC/Report"]
    bodies = [
        "K, f1, f2, RV, E, Ncb, filler mask, d0/d1/d2 streams and TS 36.212 evidence.",
        "Apply T13.1 width, scale, round and saturation to system and parity LLR streams.",
        "Compute branch metric, alpha, beta, posterior and extrinsic with Log-MAP or Max-Log-MAP.",
        "Interleave and deinterleave extrinsic LLR; update apriori for the next half-iteration.",
        "Hard decision, CB/TB CRC, early stop, metrics.csv and replay bundle.",
    ]
    fills = ["#e3f2fd", "#fff8e1", "#e8f5e9", "#ede7f6", "#fce4ec"]
    for rect, title, body, fill in zip(top, titles, bodies, fills):
        card(draw, rect, title, body, fill)
    for a, b in zip(top, top[1:]):
        arrow(draw, a, b)

    table(draw, (75, 505, 2120, 1110))

    bottom = (75, 1220, 2120, 1665)
    draw.rounded_rectangle(bottom, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((W / 2, 1258), "Bitwidth and Algorithm Options", font=HEAD, fill="#102027", anchor="mm")
    opts = [
        ("Log-MAP", "max-star correction LUT, higher accuracy, wider trace checks"),
        ("Max-Log-MAP", "max only, hardware friendly, needs BLER loss budget"),
        ("Metric Norm", "subtract column max to prevent growth without changing decisions"),
        ("Extrinsic Scale", "clip or scale external evidence before next SISO"),
        ("Saturation", "count alpha/beta/extrinsic clamps and dump first hit"),
    ]
    x = 125
    boxes = []
    for title, body in opts:
        rect = (x, 1325, x + 350, 1535)
        boxes.append(rect)
        card(draw, rect, title, body, "#f3e5f5")
        x += 390
    for a, b in zip(boxes, boxes[1:]):
        arrow(draw, a, b)
    centered(
        draw,
        ["Requirement rule: compare branch metric, alpha/beta, extrinsic and CRC layers before judging a fixed-point Turbo BLER loss."],
        SMALL,
        (bottom[0] + 40, 1570, bottom[2] - 40, 1645),
        "#37474f",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
