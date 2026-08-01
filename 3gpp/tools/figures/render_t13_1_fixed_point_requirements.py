#!/usr/bin/env python3
""" @file render_t13_1_fixed_point_requirements.py
@brief 渲染 T13.1 定点译码器需求图，展示从浮点 LLR 实验到可审计位宽、饱和、损失预算的完整需求封闭流程。
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
OUT = ROOT / "docs/L3/assets/T13.1_fixed_point_decoder_requirements.png"



TITLE = font(40, True)
HEAD = font(26, True)
TEXT = font(24)
SMALL = font(24)
TINY = font(24)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:
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
        if text_size(draw, cand, fnt)[0] <= width:
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
    return draw.textbbox((0, 0), text, font=fnt)[3]


def centered_lines(draw, lines, fnt, box, fill="#263238", gap=7):
    """ @brief 在矩形区域内居中对齐绘制多行文本。
    @param draw PIL 绘图上下文。
    @param lines 文本行列表。
    @param fnt PIL 字体对象。
    @param box 矩形四边坐标 (x0, y0, x1, y1)。
    @param fill 文本颜色 hex 字符串。
    @param gap 行间距，默认 7px。
    @return None
    """
    x0, y0, x1, y1 = box
    heights = [text_h(draw, line, fnt) for line in lines]
    total = sum(heights) + gap * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    cx = (x0 + x1) / 2
    for line, h in zip(lines, heights):
        draw.text((cx, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + gap


def card(draw, rect, title, body, fill):
    """ @brief 绘制带标题和正文的圆角矩形卡片，用于定点需求流程各阶段。
    @param draw PIL 绘图上下文。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @param title 卡片标题。
    @param body 正文描述字符串。
    @param fill 填充色 hex 字符串。
    @return None
    """
    x0, y0, x1, y1 = rect
    draw.rounded_rectangle(rect, radius=10, fill=fill, outline="#263238", width=2)
    draw.text(((x0 + x1) / 2, y0 + 34), title, font=HEAD, fill="#102027", anchor="mm")
    lines = wrap(draw, body, TINY, x1 - x0 - 42)
    centered_lines(draw, lines, TINY, (x0 + 22, y0 + 76, x1 - 22, y1 - 22))


def center(rect):
    """ @brief 计算矩形几何中心坐标。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @return 中心点坐标 (cx, cy)。
    """
    return (rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2


def boundary_point(src, dst):
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
    ax, ay = boundary_point(src, dst)
    bx, by = boundary_point(dst, src)
    vx, vy = bx - ax, by - ay
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    end = (bx - ux * head_len, by - uy * head_len)
    draw.line([(ax, ay), end], fill="#37474f", width=4)
    px, py = -uy, ux
    draw.polygon(
        [
            (bx, by),
            (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w),
            (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w),
        ],
        fill="#37474f",
    )


def cell(draw, rect, text, fnt=SMALL, fill="#263238"):
    """ @brief 在单元格内自动换行并居中绘制文本，用于需求模板表格。
    @param draw PIL 绘图上下文。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @param text 待绘制的文本字符串。
    @param fnt PIL 字体对象。
    @param fill 文本颜色 hex 字符串。
    @return None
    """
    lines = wrap(draw, text, fnt, rect[2] - rect[0] - 22)
    centered_lines(draw, lines, fnt, (rect[0] + 8, rect[1] + 5, rect[2] - 8, rect[3] - 5), fill, gap=5)


def draw_table(draw, rect):
    """ @brief 绘制"进入 C/C++ 前必须固定的决定"需求模板表格。
    @param draw PIL 绘图上下文。
    @param rect 表格外框矩形 (x0, y0, x1, y1)。
    @return None
    """
    x0, y0, x1, y1 = rect
    draw.rounded_rectangle(rect, radius=12, fill="#ffffff", outline="#607d8b", width=2)
    draw.text(((x0 + x1) / 2, y0 + 36), "Requirement Template: What Must Be Fixed Before C/C++", font=HEAD, fill="#102027", anchor="mm")
    cols = [x0 + 36, x0 + 270, x0 + 610, x0 + 985, x1 - 36]
    rows = [y0 + 82, y0 + 145, y0 + 235, y0 + 325, y0 + 415, y0 + 505, y0 + 595]
    headers = ["Decision", "Required Fields", "Evidence", "Failure if Missing"]
    data = [
        ["LLR format", "width, frac, sign convention, clip", "histogram + no-noise vector", "wrong hard decisions"],
        ["Internal messages", "metric width, guard bits, scale", "per-stage max/min trace", "iteration saturation"],
        ["Arithmetic", "rounding, saturation, extension", "edge-codeword tests", "wraparound sign flip"],
        ["Loss budget", "float baseline, fixed budget, CI", "BER/BLER report", "unprovable performance claim"],
        ["Compare policy", "bit-exact checkpoints, tolerance", "replay bundle", "C/RTL mismatch triage stalls"],
    ]
    for r in rows:
        draw.line([(cols[0], r), (cols[-1], r)], fill="#cfd8dc", width=1)
    for c in cols:
        draw.line([(c, rows[0]), (c, rows[-1])], fill="#e0e7ea", width=1)
    for i, h in enumerate(headers):
        cell(draw, (cols[i], rows[0], cols[i + 1], rows[1]), h, SMALL, "#102027")
    for r, row in enumerate(data):
        for c, text in enumerate(row):
            cell(draw, (cols[c], rows[r + 1], cols[c + 1], rows[r + 2]), text, TINY)


def main() -> None:
    """ @brief 渲染 T13.1 定点译码器需求图，保存为 PNG 到 docs/L3/assets/。
    @note 该图展示从浮点基线、量化契约、定点模型到回归证据的完整需求封闭流程，
     包含需求模板表格（LLR 格式/内部消息/算术/损失预算/比较策略）、Q 格式示例和审查关卡。
    @return None
    """
    W, H = 2200, 1760
    img = Image.new("RGB", (W, H), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((W / 2, 56), "T13.1 Fixed-Point Decoder Requirements", font=TITLE, fill="#102027", anchor="mm")
    subtitle = "Turn floating LLR experiments into auditable bitwidth, saturation, loss-budget and bit-exact requirements"
    centered_lines(draw, wrap(draw, subtitle, TEXT, W - 220), TEXT, (110, 78, W - 110, 124), "#455a64")

    top = [
        (80, 165, 430, 415),
        (520, 165, 870, 415),
        (960, 165, 1310, 415),
        (1400, 165, 1750, 415),
    ]
    titles = ["Float Baseline", "Quantization Contract", "Fixed Model", "Regression Evidence"]
    bodies = [
        "T12 metrics, LLR histograms, first failures and protocol descriptors define the starting point.",
        "Choose width, Q format, clipping, scaling, rounding, saturation and sign convention.",
        "C/C++ uses integer arithmetic, saturating adders, explicit checkpoints and trace dumps.",
        "Compare against Python fixed reference, record BLER loss, bit-exact pass/fail and replay paths.",
    ]
    fills = ["#e3f2fd", "#fff8e1", "#e8f5e9", "#ede7f6"]
    for rect, title, body, fill in zip(top, titles, bodies, fills):
        card(draw, rect, title, body, fill)
    for a, b in zip(top, top[1:]):
        arrow(draw, a, b)

    q = (1785, 168, 2140, 412)
    draw.rounded_rectangle(q, radius=12, fill="#ffffff", outline="#607d8b", width=2)
    draw.text(((q[0] + q[2]) / 2, q[1] + 34), "Q Format Example", font=HEAD, fill="#102027", anchor="mm")
    centered_lines(
        draw,
        ["Q4.2, W=6", "scale = 2^2 = 4", "q = round(4L)", "raw range [-32, 31]", "example uses [-31, 31]"],
        SMALL,
        (q[0] + 16, q[1] + 76, q[2] - 16, q[3] - 20),
    )
    arrow(draw, top[-1], q)

    draw_table(draw, (80, 500, 2110, 1110))

    bottom = (80, 1210, 2110, 1665)
    draw.rounded_rectangle(bottom, radius=12, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((W / 2, 1248), "Checkpoints and Review Gates", font=HEAD, fill="#102027", anchor="mm")
    checks = [
        ("Input", "LLR sign, width, fraction, clip, histogram"),
        ("Soft Buffer", "HARQ accumulation, saturation count, repeat merge"),
        ("Core", "branch metric, CN/VN message, PM update"),
        ("Output", "hard bits, CRC, syndrome, false-pass flags"),
        ("Report", "fixed loss budget, CI overlap, replay command"),
    ]
    x = 130
    boxes = []
    for title, body in checks:
        rect = (x, 1315, x + 350, 1535)
        boxes.append(rect)
        card(draw, rect, title, body, "#fce4ec")
        x += 390
    for a, b in zip(boxes, boxes[1:]):
        arrow(draw, a, b)
    centered_lines(
        draw,
        ["Requirement rule: if a field affects integer value, saturation, ordering or pass/fail status, it must be in the descriptor and in the replay bundle."],
        SMALL,
        (bottom[0] + 40, 1570, bottom[2] - 40, 1645),
        "#37474f",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
