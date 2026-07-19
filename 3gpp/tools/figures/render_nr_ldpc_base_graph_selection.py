#!/usr/bin/env python3
"""Render the NR LDPC base graph selection flow."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T8.2_NR_LDPC_base_graph_selection_flow.png"

PALETTE = {
    "ink": "#17212F",
    "muted": "#5A6877",
    "line": "#C8D3DF",
    "bg": "#FFFFFF",
    "panel": "#F7F9FC",
    "blue": "#2457A6",
    "green": "#2D8F5D",
    "amber": "#C69220",
    "red": "#C64B59",
    "purple": "#7457A6",
    "soft_blue": "#EAF3FF",
    "soft_green": "#EDF8F1",
    "soft_amber": "#FFF6DE",
    "soft_red": "#FFF0F2",
}



def boundary_point(box: tuple[int, int, int, int], side: str) -> tuple[int, int]:
    mid_x = (box[0] + box[2]) // 2
    mid_y = (box[1] + box[3]) // 2
    if side == "left":
        return box[0], mid_y
    if side == "right":
        return box[2], mid_y
    if side == "top":
        return mid_x, box[1]
    if side == "bottom":
        return mid_x, box[3]
    raise ValueError(f"Unsupported side: {side}")


def center_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def wrap_lines(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    return fit_wrap_text(draw, text, fnt, max_width)


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 6,
) -> int:
    x, y = xy
    for line in wrap_lines(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def draw_centered_wrapped(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 5,
) -> None:
    lines = wrap_lines(draw, text, fnt, max_width)
    metrics = [draw.textbbox((0, 0), line, font=fnt) for line in lines]
    heights = [bbox[3] - bbox[1] for bbox in metrics]
    total_h = sum(heights) + line_gap * max(0, len(lines) - 1)
    y = box[1] + max(0, ((box[3] - box[1]) - total_h) / 2)
    for line, h, bbox in zip(lines, heights, metrics):
        x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
        draw.text((x, y), line, font=fnt, fill=fill)
        y += h + line_gap


def rounded_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    fill: str,
    stripe: str,
) -> None:
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=PALETTE["line"], width=2)
    draw.rounded_rectangle((box[0], box[1], box[2], box[1] + 18), radius=18, fill=stripe, outline=stripe)
    center_text(draw, (box[0] + 16, box[1] + 34, box[2] - 16, box[1] + 78), title, font(26, True), PALETTE["ink"])
    draw_centered_wrapped(
        draw,
        (box[0] + 20, box[1] + 88, box[2] - 20, box[3] - 16),
        body,
        font(24),
        PALETTE["muted"],
        box[2] - box[0] - 40,
    )


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str = "#66798C",
    width: int = 4,
) -> None:
    sx, sy = start
    ex, ey = end
    length = math.hypot(ex - sx, ey - sy)
    if length == 0:
        return
    ux, uy = (ex - sx) / length, (ey - sy) / length
    px, py = -uy, ux
    head_len, head_w = 16, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line((sx, sy, *line_end), fill=color, width=width)
    points = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(points, fill=color)


def label(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, color: str) -> None:
    fnt = font(24, True)
    w = draw.textbbox((0, 0), text, font=fnt)[2] + 28
    draw.rounded_rectangle((x, y, x + w, y + 34), radius=10, fill=color, outline=color)
    center_text(draw, (x, y, x + w, y + 34), text, fnt, "#FFFFFF")


def branch_table(draw: ImageDraw.ImageDraw) -> None:
    box = (72, 850, 1860, 1388)
    draw.rounded_rectangle(box, radius=18, fill=PALETTE["panel"], outline=PALETTE["line"], width=2)
    draw.text((112, 886), "选择条件的协议复现", font=font(31, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (112, 940),
        "三条 BG2 分支是逻辑 OR，只要满足任一条就选 BG2；全部不满足才选 BG1。初传和同一 TB 的后续重传使用同一个基图。",
        font(24),
        PALETTE["muted"],
        1260,
    )

    headers = ["分支", "判定条件", "工程含义", "输出"]
    xs = [118, 352, 852, 1468]
    widths = [200, 470, 560, 250]
    y = 1024
    for x, w, h in zip(xs, widths, headers):
        draw.rounded_rectangle((x, y, x + w, y + 56), radius=8, fill="#DEE8F5", outline="#DEE8F5")
        center_text(draw, (x, y, x + w, y + 56), h, font(24, True), PALETTE["ink"])

    rows = [
        ("1", "A <= 292", "极短 payload 优先短块友好结构", "BG2"),
        ("2", "A <= 3824 且 R <= 0.67", "中小 payload 且码率不高，偏稳健", "BG2"),
        ("3", "R <= 0.25", "低码率场景，即使 payload 较大也进入 BG2", "BG2"),
        ("默认", "以上均不满足", "大 payload 或较高码率，走高吞吐长块结构", "BG1"),
    ]
    y += 66
    for i, row in enumerate(rows):
        fill = "#FFFFFF" if i % 2 == 0 else "#F1F5FA"
        draw.rounded_rectangle((118, y - 6, 1718, y + 62), radius=8, fill=fill, outline=fill)
        for x, text, max_w in zip(xs, row, widths):
            cell = (x, y - 2, x + max_w, y + 58)
            if max_w <= 220:
                center_text(draw, cell, text, font(24, True if text in {"BG1", "BG2"} else False), PALETTE["ink"])
            else:
                draw_centered_wrapped(draw, cell, text, font(24), PALETTE["ink"], max_w - 20)
        y += 70


def example_panel(draw: ImageDraw.ImageDraw) -> None:
    box = (72, 1444, 1860, 1970)
    draw.rounded_rectangle(box, radius=18, fill="#FFFDF6", outline="#E3D18C", width=2)
    draw.text((112, 1478), "边界读图与接收端落点", font=font(31, True), fill=PALETTE["ink"])
    examples = [
        ("A=292, R=0.90", "满足 A <= 292", "BG2", "短 payload 分支覆盖高码率极短块。"),
        ("A=3824, R=0.67", "满足 A <= 3824 且 R <= 0.67", "BG2", "两个阈值取等号仍进入 BG2。"),
        ("A=3825, R=0.67", "不满足前三条", "BG1", "只越过 A 阈值就会切到 BG1。"),
        ("A=6000, R=0.25", "满足 R <= 0.25", "BG2", "低码率分支独立于 payload 大小。"),
    ]
    xs = [112, 520, 930, 1138]
    headers = ["输入", "判定路径", "输出", "接收端影响"]
    widths = [340, 382, 140, 650]
    y = 1570
    for x, h in zip(xs, headers):
        draw.text((x, y), h, font=font(24, True), fill=PALETTE["blue"])
    y += 44
    for values in examples:
        for x, value, w in zip(xs, values, widths):
            draw_centered_wrapped(draw, (x, y, x + w, y + 70), value, font(24), PALETTE["ink"], w - 18, line_gap=4)
        y += 82


def main(output: Path | None = None) -> None:
    out = output or OUT_PATH
    img = Image.new("RGB", (1940, 2025), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((80, 46), "NR LDPC 基图选择流程", font=font(42, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (80, 106),
        "输入是传输块 payload size A 与由 MCS 指示的 coding rate R；输出是 LDPC Base Graph 1 或 Base Graph 2。选择结果会进入 Zc、矩阵表、地址生成和译码器配置。",
        font(24),
        PALETTE["muted"],
        1760,
    )

    input_box = (120, 220, 480, 420)
    rounded_box(
        draw,
        input_box,
        "输入上下文",
        "A: payload size\nR: MCS 指示码率\n方向: UL-SCH 或 DL-SCH/PCH",
        PALETTE["soft_blue"],
        PALETTE["blue"],
    )

    b1 = (620, 192, 1000, 368)
    b2 = (620, 402, 1000, 594)
    b3 = (620, 630, 1000, 778)
    rounded_box(draw, b1, "分支 1", "A <= 292", PALETTE["soft_green"], PALETTE["green"])
    rounded_box(draw, b2, "分支 2", "A <= 3824 且 R <= 0.67", PALETTE["soft_amber"], PALETTE["amber"])
    rounded_box(draw, b3, "分支 3", "R <= 0.25", PALETTE["soft_red"], PALETTE["red"])

    out_bg2 = (1148, 300, 1578, 502)
    out_bg1 = (1148, 596, 1578, 778)
    rounded_box(draw, out_bg2, "输出 BG2", "短块、低码率或中小负载场景；更偏稳健。", PALETTE["soft_green"], PALETTE["green"])
    rounded_box(draw, out_bg1, "输出 BG1", "前三个 BG2 条件均不满足；更偏长块和高吞吐。", PALETTE["soft_blue"], PALETTE["blue"])

    config_box = (1606, 366, 1894, 654)
    rounded_box(draw, config_box, "配置落点", "bg_id 写入描述符，选择基图表、提升规则、移位 ROM 与地址生成器。", "#F3F0FA", PALETTE["purple"])

    for target in [b1, b2, b3]:
        arrow(draw, boundary_point(input_box, "right"), boundary_point(target, "left"))
    arrow(draw, boundary_point(b1, "right"), (out_bg2[0], out_bg2[1] + 88), PALETTE["green"])
    arrow(draw, boundary_point(b2, "right"), (out_bg2[0], out_bg2[1] + 112), PALETTE["amber"])
    arrow(draw, boundary_point(b3, "right"), (out_bg2[0], out_bg2[1] + 136), PALETTE["red"])
    arrow(draw, boundary_point(b3, "right"), boundary_point(out_bg1, "left"), PALETTE["blue"])
    arrow(draw, boundary_point(out_bg2, "right"), boundary_point(config_box, "left"), PALETTE["purple"])
    arrow(draw, boundary_point(out_bg1, "right"), boundary_point(config_box, "left"), PALETTE["purple"])

    label(draw, 1030, 238, "任一满足", PALETTE["green"])
    label(draw, 1006, 666, "全部不满足", PALETTE["blue"])

    branch_table(draw)
    example_panel(draw)

    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print(f"WROTE {out}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=None, help=f"output PNG path (default: {OUT_PATH})")
    args = parser.parse_args()
    main(output=args.output)
