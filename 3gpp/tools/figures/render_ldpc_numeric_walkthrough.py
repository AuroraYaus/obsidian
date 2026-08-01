#!/usr/bin/env python3
""" @file render_ldpc_numeric_walkthrough.py
    @brief 渲染 LDPC Min-Sum 数值走读教学图（两张：H/CN 消息 + Posterior/早停/调试字段）。
    @date 2025
    @note 教学 H=[[1,1,0,1,0,0],[0,1,1,0,1,0],[1,0,1,0,0,1]]，初始 LLR 和 CN 消息均为手算可复现。
    @see render_ldpc_min_sum_variants.py 对应的 MS/NMS/OMS 算法对比图
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T8.8_LDPC_numeric_walkthrough.png"
PART1_PATH = ROOT / "docs/L2/assets/T8.8_LDPC_numeric_walkthrough_part1.png"
PART2_PATH = ROOT / "docs/L2/assets/T8.8_LDPC_numeric_walkthrough_part2.png"

PALETTE = {
    "ink": "#17212F",
    "muted": "#5B6877",
    "line": "#C9D4DF",
    "bg": "#FFFFFF",
    "panel": "#F7F9FC",
    "blue": "#2457A6",
    "green": "#2D8F5D",
    "amber": "#C69220",
    "red": "#C64B59",
    "purple": "#7457A6",
}



def center_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    """ @brief 在矩形内居中绘制单行文本。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 绘制区域。
        @param text 待绘制的单行字符串。
        @param fnt PIL 字体对象。
        @param fill 文字颜色。
        @return 无返回值。
    """
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill: str, width: int, gap: int = 6) -> int:
    """ @brief 在指定坐标处绘制自动换行的左对齐多行文本。
        @param draw PIL ImageDraw 实例。
        @param xy 起始坐标 (x, y)。
        @param text 待绘制的长文本。
        @param fnt 字体对象。
        @param fill 文字颜色。
        @param width 每行最大像素宽度。
        @param gap 行间距，默认 6。
        @return 最后一行的底部 Y 坐标。
    """
    x, y = xy
    for line in fit_wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def table(draw: ImageDraw.ImageDraw, x: int, y: int, headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 56) -> int:
    """ @brief 绘制带表头的简单表格。
        @param draw PIL ImageDraw 实例。
        @param x 表格左上角 X。
        @param y 表格左上角 Y。
        @param headers 表头列名列表。
        @param rows 数据行。
        @param widths 每列像素宽度列表。
        @param row_h 行高，默认 56。
        @return 表格底部 Y 坐标。
    """
    xx = x
    for header, width in zip(headers, widths):
        draw.rectangle((xx, y, xx + width, y + row_h), fill="#EAF3FF", outline=PALETTE["line"], width=2)
        center_text(draw, (xx + 6, y, xx + width - 6, y + row_h), header, font(24, True), PALETTE["ink"])
        xx += width
    y += row_h
    for row in rows:
        xx = x
        for value, width in zip(row, widths):
            draw.rectangle((xx, y, xx + width, y + row_h), fill="#FFFFFF", outline=PALETTE["line"], width=1)
            center_text(draw, (xx + 6, y, xx + width - 6, y + row_h), value, font(24), PALETTE["ink"])
            xx += width
        y += row_h
    return y


def draw_matrix_and_initial(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制 Toy H 矩阵格子 + 初始 channel LLR 和硬判决表。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
        @note H 为 3x6 矩阵，初始 syndrome=[0,1,1]，c1 和 c2 校验失败。
    """
    draw.text((80, 165), "Toy H 与初始判决", font=font(34, True), fill=PALETTE["blue"])
    H = [[1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1]]
    x0, y0, cell = 85, 235, 52
    for r, row in enumerate(H):
        for c, val in enumerate(row):
            box = (x0 + c * cell, y0 + r * cell, x0 + (c + 1) * cell, y0 + (r + 1) * cell)
            draw.rectangle(box, fill="#EAF3FF" if val else "#FFFFFF", outline=PALETTE["line"], width=1)
            center_text(draw, box, str(val), font(24, True), PALETTE["ink"])
    rows = [
        ["LLR", "+0.9", "-0.8", "+0.4", "-0.6", "+0.7", "-0.5"],
        ["hard0", "0", "1", "0", "1", "0", "1"],
    ]
    table(draw, 80, 430, ["", "v0", "v1", "v2", "v3", "v4", "v5"], rows, [95, 88, 88, 88, 88, 88, 88], row_h=56)
    draw_wrapped(draw, (80, 625), "初始 syndrome=[0,1,1]，weight=2，说明 c1 和 c2 校验失败。", font(24), PALETTE["red"], 680)


def draw_messages(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制一轮 Min-Sum CN 消息表：9 条边消息及其符号/幅度推导说明。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
    """
    draw.text((900, 165), "一轮 Min-Sum CN 消息", font=font(34, True), fill=PALETTE["green"])
    rows = [
        ["r0->v0", "+0.6"], ["r0->v1", "-0.6"], ["r0->v3", "-0.8"],
        ["r1->v1", "+0.4"], ["r1->v2", "-0.7"], ["r1->v4", "-0.4"],
        ["r2->v0", "-0.4"], ["r2->v2", "-0.5"], ["r2->v5", "+0.4"],
    ]
    table(draw, 900, 225, ["edge", "message"], rows, [155, 130], row_h=56)
    draw_wrapped(
        draw,
        (1240, 235),
        "例：r1->v2 排除 v2，只看 v1=-0.8 与 v4=+0.7；符号为负，幅度取 min(0.8,0.7)=0.7，所以 r1->v2=-0.7。",
        font(24),
        PALETTE["muted"],
        680,
    )


def draw_posterior(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制 Posterior LLR 合成、硬判决与早停条件说明。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
        @note 更新后 hard=[0,1,1,1,0,1]，syndrome=[0,0,0]，满足 LDPC 早停条件。
    """
    draw.text((900, 800), "Posterior、硬判决与早停", font=font(34, True), fill=PALETTE["purple"])
    rows = [
        ["v0", "+0.9+0.6-0.4", "+1.1", "0"],
        ["v1", "-0.8-0.6+0.4", "-1.0", "1"],
        ["v2", "+0.4-0.7-0.5", "-0.8", "1"],
        ["v3", "-0.6-0.8", "-1.4", "1"],
        ["v4", "+0.7-0.4", "+0.3", "0"],
        ["v5", "-0.5+0.4", "-0.1", "1"],
    ]
    table(draw, 900, 860, ["VN", "sum", "Lpost", "hard1"], rows, [85, 285, 115, 100], row_h=56)
    draw_wrapped(draw, (80, 1265), "更新后 hard=[0,1,1,1,0,1]；syndrome=[0,0,0]。教学译码器可 syndrome early stop；真实链路还要执行循环冗余校验边界。", font(24), PALETTE["red"], 1760)


def draw_bottom(draw: ImageDraw.ImageDraw) -> None:
    """ @brief 绘制底部调试字段与真实 NR 对应关系表。
        @param draw PIL ImageDraw 实例。
        @return 无返回值。
        @note 四行：iteration、edge messages、posterior LLR、syndrome weight 的 toy vs NR 对照。
    """
    panel = (80, 1415, 1920, 1900)
    draw.rounded_rectangle(panel, radius=16, fill="#FFFDF6", outline="#E2CD7A", width=2)
    draw.text((120, 1455), "调试字段与真实 NR 对应关系", font=font(34, True), fill=PALETTE["ink"])
    rows = [
        ["iteration", "0 -> 1", "本例只跑一轮 Min-Sum。"],
        ["edge messages", "9 条 r", "真实 NR 由 BG/Zc/shift 生成大量边。"],
        ["posterior LLR", "6 个", "真实 NR 是 68Zc 或 52Zc 个 H 列位置。"],
        ["syndrome weight", "2 -> 0", "早停只说明 LDPC 约束通过。"],
    ]
    table(draw, 120, 1530, ["field", "toy value", "meaning"], rows, [260, 230, 1250], row_h=64)


def render_overview() -> Image.Image:
    """ @brief 渲染第一部分：Toy H 矩阵 + channel LLR 初始状态 + 一轮 CN 消息。
        @return 2000x840 的 PIL Image 对象。
        @note 输出为 PART1_PATH，侧重信道输入和 CN 处理阶段。
    """
    img = Image.new("RGB", (2000, 840), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((80, 48), "Toy LDPC Min-Sum 数值走读", font=font(46, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (80, 112),
        "教学例子，不是 NR conformance vector。目标是把 channel LLR、H、CN 消息、posterior LLR、hard decision、syndrome 与 early stop 串成可复现路径。",
        font(24),
        PALETTE["muted"],
        1760,
    )
    draw_matrix_and_initial(draw)
    draw_messages(draw)
    return img


def render_posterior_debug() -> Image.Image:
    """ @brief 渲染第二部分：VN posterior 合成、hard decision、syndrome 早停和调试字段表。
        @return 2000x1320 的 PIL Image 对象。
        @note 输出为 PART2_PATH，承接第一部分的消息展示最终判决和验证字段。
    """
    img = Image.new("RGB", (2000, 1320), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((80, 48), "Posterior、早停与调试字段", font=font(46, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (80, 112),
        "第二张图承接第一张的 9 条 CN 消息，展示 VN posterior 合成、更新后 hard decision、syndrome early stop 和最小 dump 字段。",
        font(24),
        PALETTE["muted"],
        1760,
    )
    # Reuse the existing drawing helpers by positioning their content into the
    # shorter second canvas.
    draw.text((80, 210), "Posterior、硬判决与早停", font=font(34, True), fill=PALETTE["purple"])
    rows = [
        ["v0", "+0.9+0.6-0.4", "+1.1", "0"],
        ["v1", "-0.8-0.6+0.4", "-1.0", "1"],
        ["v2", "+0.4-0.7-0.5", "-0.8", "1"],
        ["v3", "-0.6-0.8", "-1.4", "1"],
        ["v4", "+0.7-0.4", "+0.3", "0"],
        ["v5", "-0.5+0.4", "-0.1", "1"],
    ]
    table(draw, 80, 270, ["VN", "sum", "Lpost", "hard1"], rows, [95, 360, 140, 120], row_h=64)
    draw_wrapped(
        draw,
        (860, 282),
        "更新后 hard=[0,1,1,1,0,1]；syndrome=[0,0,0]。toy 译码器可 syndrome early stop；真实链路还要执行 CRC 边界。",
        font(26),
        PALETTE["red"],
        950,
    )

    panel = (80, 760, 1920, 1265)
    draw.rounded_rectangle(panel, radius=16, fill="#FFFDF6", outline="#E2CD7A", width=2)
    draw.text((120, 800), "调试字段与真实 NR 对应关系", font=font(34, True), fill=PALETTE["ink"])
    debug_rows = [
        ["iteration", "0 -> 1", "本例只跑一轮 Min-Sum。"],
        ["edge messages", "9 条 r", "真实 NR 由 BG/Zc/shift 生成大量边。"],
        ["posterior LLR", "6 个", "真实 NR 是 68Zc 或 52Zc 个 H 列位置。"],
        ["syndrome weight", "2 -> 0", "早停只说明 LDPC 约束通过。"],
    ]
    table(draw, 120, 880, ["field", "toy value", "meaning"], debug_rows, [260, 230, 1250], row_h=64)
    return img


def main() -> None:
    """ @brief 脚本入口：生成 T8.8 LDPC 数值走读两张独立图 + 一张历史拼接图。
        @return 无返回值。
        @note 产出一张 PART1（2000x840）、一张 PART2（2000x1320）和一张组合全景图 OUT_PATH。
    """
    overview = render_overview()
    posterior = render_posterior_debug()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    overview.save(PART1_PATH)
    posterior.save(PART2_PATH)

    # Keep the historical combined asset as a contact sheet for existing
    # references, but the lesson body now uses the two readable parts.
    combined = Image.new("RGB", (2000, overview.height + posterior.height), PALETTE["bg"])
    combined.paste(overview, (0, 0))
    combined.paste(posterior, (0, overview.height))
    combined.save(OUT_PATH)
    print(f"WROTE {PART1_PATH}")
    print(f"WROTE {PART2_PATH}")
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
