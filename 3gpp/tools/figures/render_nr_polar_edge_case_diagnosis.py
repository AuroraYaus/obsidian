#!/usr/bin/env python3
"""Render NR Polar decoder edge-case diagnosis flow."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T10.8_NR_Polar_edge_case_diagnosis.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#182334",
    "muted": "#5A6678",
    "line": "#8FA1B7",
    "blue": "#2457A6",
    "blue_fill": "#EAF1FB",
    "green": "#247A58",
    "green_fill": "#E8F6EF",
    "orange": "#B66328",
    "orange_fill": "#FFF0E4",
    "red": "#B83E4A",
    "red_fill": "#FCEBED",
    "purple": "#6651A6",
    "purple_fill": "#F0EDFA",
    "gray_fill": "#F7F9FC",
}



def draw_box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    lines: list[str],
    fill: str,
    outline: str,
) -> None:
    draw.rounded_rectangle(xy, radius=14, fill=fill, outline=outline, width=2)
    draw.text((xy[0] + 22, xy[1] + 16), title, font=font(24, True), fill=outline)
    y = xy[1] + 64
    for line in lines:
        draw.text((xy[0] + 22, y), line, font=font(24, True), fill=COL["ink"])
        y += 39


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str) -> None:
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length == 0:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    px, py = -uy, ux
    head_len, head_w = 14, 8
    line_end = (x1 - ux * head_len, y1 - uy * head_len)
    draw.line((x0, y0, *line_end), fill=color, width=3)
    draw.polygon(
        [
            (x1, y1),
            (x1 - ux * head_len + px * head_w, y1 - uy * head_len + py * head_w),
            (x1 - ux * head_len - px * head_w, y1 - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def main() -> None:
    img = Image.new("RGB", (1900, 1560), COL["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 44), "T10.8 NR Polar 译码边界案例：定位路径与最小证据包", font=font(34, True), fill=COL["ink"])
    draw.text(
        (70, 96),
        "读图顺序：先固定 descriptor，再逐层排查 rate recovery、mask、SC/SCL、CRC/RNTI selector。",
        font=font(24),
        fill=COL["muted"],
    )

    y0 = 175
    w = 310
    h = 230
    xs = [70, 430, 790, 1150, 1510]
    boxes = [
        ("descriptor", ["context: UCI/DCI", "A/K/E/N, crc_len", "i_il, i_bil, L", "RNTI context"], COL["gray_fill"], COL["line"]),
        ("rate recovery", ["sub-block reverse", "bit selection reverse", "punctured=0", "shortened=+Lmax"], COL["blue_fill"], COL["blue"]),
        ("mask generator", ["reliability slice", "info set", "frozen set", "index base"], COL["green_fill"], COL["green"]),
        ("SC/SCL core", ["f/g tree", "path split/prune", "PM list", "partial sums"], COL["purple_fill"], COL["purple"]),
        ("CRC/RNTI select", ["CRC type", "pass vector", "PM tie-break", "selected path"], COL["orange_fill"], COL["orange"]),
    ]
    for x, (title, lines, fill, outline) in zip(xs, boxes):
        draw_box(draw, (x, y0, x + w, y0 + h), title, lines, fill, outline)
    for i in range(4):
        arrow(draw, (xs[i] + w, y0 + h // 2), (xs[i + 1], y0 + h // 2), COL["line"])

    # Fault injection strips.
    draw.text((90, 455), "典型故障注入点", font=font(25, True), fill=COL["ink"])
    cases = [
        ("无 CRC 小负载", ["selector 没有 CRC 约束", "必须靠分支和 PM 策略记录原因"], COL["orange_fill"], COL["orange"]),
        ("CRC 长度错", ["UCI 6/11 bit 或 DCI 24 bit 用错", "候选全 fail 或误 pass"], COL["red_fill"], COL["red"]),
        ("L 太小", ["正确路径在中途被剪掉", "末端 CRC 无法恢复"], COL["purple_fill"], COL["purple"]),
        ("PM 并列", ["排序不稳定", "回归同种子结果漂移"], COL["purple_fill"], COL["purple"]),
        ("puncture/shorten 错", ["unknown 与 known-zero 互换", "高 SNR 仍失败"], COL["blue_fill"], COL["blue"]),
        ("frozen mask 错", ["信息位被强制或冻结位被分裂", "路径系统性偏移"], COL["green_fill"], COL["green"]),
        ("UCI/DCI mismatch", ["context 错导致 crc_len、RNTI、E", "或输出解释错误"], COL["red_fill"], COL["red"]),
        ("RNTI 边界错", ["DCI 盲检", "误通过或漏检"], COL["orange_fill"], COL["orange"]),
    ]
    grid_x = 90
    grid_y = 505
    card_w = 410
    card_h = 148
    gap_x = 38
    gap_y = 28
    for idx, (title, desc_lines, fill, outline) in enumerate(cases):
        row = idx // 4
        col = idx % 4
        x = grid_x + col * (card_w + gap_x)
        y = grid_y + row * (card_h + gap_y)
        draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=12, fill=fill, outline=outline, width=2)
        draw.text((x + 18, y + 16), title, font=font(24, True), fill=outline)
        draw.text((x + 18, y + 62), desc_lines[0], font=font(24, True), fill=COL["ink"])
        draw.text((x + 18, y + 100), desc_lines[1], font=font(24, True), fill=COL["ink"])

    # Minimum dump package.
    dump = (90, 960, 1810, 1290)
    draw.rounded_rectangle(dump, radius=16, fill=COL["gray_fill"], outline=COL["line"], width=2)
    draw.text((dump[0] + 24, dump[1] + 22), "最小 dump 包", font=font(24, True), fill=COL["ink"])
    dump_lines = [
        "descriptor: context_type, A, K, E, N, crc_len, crc_poly_id, rnti_context, i_il, i_bil, list_size",
        "sets: reliability_slice, info_set, frozen_set, frozen_mask_hash, info_mask_hash",
        "rate recovery: punctured_set, shortened_set, repeated_addr, llr_init_snapshot, saturation_count",
        "SCL: path_bits, PM list, sort_order, tie_break_key, prune_stage, partial_sum_hash",
        "selector: CRC input range, CRC results, RNTI check, selected_path, fail_reason",
    ]
    y = dump[1] + 78
    for line in dump_lines:
        draw.text((dump[0] + 24, y), line, font=font(24, True), fill=COL["ink"])
        y += 46

    # Bottom note with ample padding.
    note = (90, 1350, 1810, 1485)
    draw.rounded_rectangle(note, radius=14, fill=COL["green_fill"], outline=COL["green"], width=2)
    draw.text((note[0] + 24, note[1] + 22), "工程定位原则", font=font(24, True), fill=COL["green"])
    draw.text(
        (note[0] + 24, note[1] + 58),
        "先证明输入和索引坐标正确，再怀疑 SC/SCL core；CRC fail 是现象，不是根因分类。",
        font=font(24, True),
        fill=COL["ink"],
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
