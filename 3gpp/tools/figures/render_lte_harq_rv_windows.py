#!/usr/bin/env python3
"""Render LTE HARQ redundancy versions as ring-buffer windows."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T7.3_LTE_HARQ_RV_windows.png"


PALETTE = {
    "ink": "#102033",
    "muted": "#5B6B7D",
    "line": "#C8D4E2",
    "panel": "#F7FAFD",
    "rv0": "#2F80ED",
    "rv1": "#00A676",
    "rv2": "#F2994A",
    "rv3": "#9B51E0",
    "overlap": "#F2C94C",
    "unknown": "#EEF2F7",
    "history": "#D8E9FF",
}



def text_center(
    draw: ImageDraw.ImageDraw,
    box: tuple[float, float, float, float],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    x = box[0] + ((box[2] - box[0]) - width) / 2 - bbox[0]
    y = box[1] + ((box[3] - box[1]) - height) / 2 - bbox[1]
    draw.text((x, y), text, font=fnt, fill=fill)


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
    lines = fit_wrap_text(draw, text, fnt, max_width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def ring_point(cx: int, cy: int, radius: int, idx: int, total: int) -> tuple[float, float]:
    angle = 2 * math.pi * idx / total - math.pi / 2
    return cx + radius * math.cos(angle), cy + radius * math.sin(angle)


def window(start: int, length: int, total: int) -> list[int]:
    return [(start + offset) % total for offset in range(length)]


def segment_ranges(addresses: list[int], total: int) -> list[tuple[int, int]]:
    selected = set(addresses)
    ranges: list[tuple[int, int]] = []
    visited: set[int] = set()
    for addr in addresses:
        if addr in visited:
            continue
        prev = (addr - 1) % total
        if prev in selected:
            continue
        end = addr
        visited.add(addr)
        while (end + 1) % total in selected and (end + 1) % total not in visited:
            end = (end + 1) % total
            visited.add(end)
        ranges.append((addr, end))
    return ranges


def draw_arc_window(
    draw: ImageDraw.ImageDraw,
    cx: int,
    cy: int,
    radius: int,
    addresses: list[int],
    total: int,
    color: str,
    width: int,
) -> None:
    box = (cx - radius, cy - radius, cx + radius, cy + radius)
    for start, end in segment_ranges(addresses, total):
        a0 = 360 * start / total - 90
        a1 = 360 * (end + 1) / total - 90
        if a1 <= a0:
            a1 += 360
        draw.arc(box, a0, a1, fill=color, width=width)


def draw_arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str = "#50657B",
    width: int = 4,
) -> None:
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.hypot(dx, dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    size = 15
    line_end = (end[0] - ux * size, end[1] - uy * size)
    draw.line((start, line_end), fill=color, width=width)
    wing = 8
    px, py = -uy, ux
    p1 = (end[0] - ux * size + px * wing, end[1] - uy * size + py * wing)
    p2 = (end[0] - ux * size - px * wing, end[1] - uy * size - py * wing)
    draw.polygon([end, p1, p2], fill=color)


def draw_rv_ring(draw: ImageDraw.ImageDraw) -> dict[int, list[int]]:
    total = 32
    win_len = 11
    starts = {0: 0, 1: 8, 2: 16, 3: 24}
    colors = {0: PALETTE["rv0"], 1: PALETTE["rv1"], 2: PALETTE["rv2"], 3: PALETTE["rv3"]}
    rv_windows = {rv: window(start, win_len, total) for rv, start in starts.items()}
    cx, cy = 520, 610
    ring_r = 286
    dot_r = 24

    draw.text((145, 175), "同一循环缓存上的四个冗余版本窗口", font=font(30, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (145, 216),
        "教学参数：环长 Kw=32，每个 RV 读取 E=11 个非 NULL 位置。四个起点 k0 示意为 0、8、16、24，突出 RV 是同一环上的窗口选择。",
        font(24),
        PALETTE["muted"],
        760,
    )

    draw.ellipse((cx - ring_r, cy - ring_r, cx + ring_r, cy + ring_r), outline="#CFDAE7", width=4)
    for rv in [0, 1, 2, 3]:
        draw_arc_window(draw, cx, cy, ring_r + rv * 18, rv_windows[rv], total, colors[rv], 10)

    for idx in range(total):
        px, py = ring_point(cx, cy, ring_r, idx, total)
        fill = "#FFFFFF"
        outline = "#B5C4D5"
        if idx in rv_windows[0]:
            fill = "#DCEBFF"
            outline = PALETTE["rv0"]
        if idx in set(rv_windows[0]) & set(rv_windows[1]):
            fill = "#FFF1B8"
            outline = "#C99A00"
        draw.ellipse((px - dot_r, py - dot_r, px + dot_r, py + dot_r), fill=fill, outline=outline, width=2)
        text_center(draw, (px - dot_r, py - dot_r, px + dot_r, py + dot_r), str(idx), font(24, True), PALETTE["ink"])

    for rv, start in starts.items():
        px, py = ring_point(cx, cy, 348 + rv * 18, start, total)
        if rv == 0:
            px, py = cx + 382, cy - 318
        label = f"RV{rv}  k0={start}"
        label_font = font(24, True)
        label_bbox = draw.textbbox((0, 0), label, font=label_font)
        label_w = label_bbox[2] - label_bbox[0] + 36
        label_h = label_bbox[3] - label_bbox[1] + 20
        label_box = (px - label_w / 2, py - label_h / 2, px + label_w / 2, py + label_h / 2)
        draw.rounded_rectangle(label_box, radius=8, fill=colors[rv], outline=colors[rv])
        text_center(draw, label_box, label, label_font, "#FFFFFF")
        px2, py2 = ring_point(cx, cy, ring_r + 22 + rv * 18, start, total)
        draw.line((px, label_box[3], px2, py2), fill=colors[rv], width=3)

    draw.text((405, 493), "ring buffer", font=font(26, True), fill=PALETTE["ink"])
    draw.text((362, 530), "地址递增到末尾后回到 0", font=font(24), fill=PALETTE["muted"])

    legend_x, legend_y = 102, 940
    legend = [
        (PALETTE["rv0"], "RV0 窗口：初传常见起点"),
        (PALETTE["rv1"], "RV1 窗口：从另一段开始"),
        (PALETTE["rv2"], "RV2 窗口：继续覆盖新区"),
        (PALETTE["rv3"], "RV3 窗口：可跨越环尾回到 0"),
        (PALETTE["overlap"], "重叠地址：不是覆盖旧值，而是 LLR 累加"),
    ]
    for pos, (color, label) in enumerate(legend):
        y = legend_y + pos * 52
        draw.rounded_rectangle((legend_x, y, legend_x + 42, y + 28), radius=6, fill=color, outline=color)
        draw.text((legend_x + 58, y - 2), label, font=font(24), fill=PALETTE["ink"])

    return rv_windows


def draw_address_chips(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    addresses: list[int],
    repeated: set[int],
    primary_color: str,
    *,
    cell_w: int,
    cell_h: int,
    gap: int,
    per_row: int,
    show_llr_index: bool = False,
) -> int:
    row_gap = 14
    for idx, addr in enumerate(addresses):
        row = idx // per_row
        col = idx % per_row
        sx = x + col * (cell_w + gap)
        sy = y + row * (cell_h + row_gap)
        is_repeated = addr in repeated
        cell_fill = "#FFF1B8" if is_repeated else "#E4F7EF"
        outline = "#C99A00" if is_repeated else primary_color
        draw.rounded_rectangle((sx, sy, sx + cell_w, sy + cell_h), radius=8, fill=cell_fill, outline=outline, width=2)
        if show_llr_index:
            text_center(draw, (sx, sy + 4, sx + cell_w, sy + cell_h / 2), f"L{idx}", font(24, True), PALETTE["ink"])
            text_center(draw, (sx, sy + cell_h / 2, sx + cell_w, sy + cell_h - 4), f"a={addr}", font(24), PALETTE["ink"])
        else:
            text_center(draw, (sx, sy, sx + cell_w, sy + cell_h), f"a={addr}", font(24, True), PALETTE["ink"])
    rows = math.ceil(len(addresses) / per_row)
    return y + rows * cell_h + max(0, rows - 1) * row_gap


def draw_transmission_stream(draw: ImageDraw.ImageDraw, rv_windows: dict[int, list[int]]) -> None:
    x, y = 1040, 185
    draw.text((x, y), "本次重传示例：RV1 输出 LLR 流", font=font(28, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (x, y + 42),
        "发送端从 RV1 起点开始扫描环，跳过 <NULL>，取到 E 个编码比特；接收端收到的是 L0...L10 这串软信息，但写回时必须恢复到环地址 a=8...18。",
        font(24),
        PALETTE["muted"],
        980,
    )
    addrs = rv_windows[1]
    start_y = y + 132
    end_y = draw_address_chips(
        draw,
        x,
        start_y,
        addrs,
        set(rv_windows[0]),
        PALETTE["rv1"],
        cell_w=104,
        cell_h=76,
        gap=12,
        per_row=6,
        show_llr_index=True,
    )
    draw.text((x, end_y + 20), "黄色：RV0 已命中过的地址，本次执行饱和累加；绿色：RV1 首次补充的地址。", font=font(24), fill=PALETTE["ink"])


def draw_soft_buffer_panel(draw: ImageDraw.ImageDraw, rv_windows: dict[int, list[int]]) -> None:
    x, y = 1040, 600
    draw.rounded_rectangle((x - 24, y - 30, x + 1010, y + 526), radius=18, fill=PALETTE["panel"], outline="#D6E0EB", width=2)
    draw.text((x, y), "接收端 HARQ soft buffer 更新", font=font(28, True), fill=PALETTE["ink"])
    rows = [
        ("a=8..10", "RV0 已有旧 LLR，RV1 再命中", "sat(L_old + L_rx)", "重复覆盖"),
        ("a=11..18", "之前未知，RV1 首次命中", "0 + L_rx", "增量冗余"),
        ("a=19..31", "本次 RV1 未命中", "保持旧值或中性 0", "未观测"),
        ("<NULL>", "协议补入的空位置", "跳过，不消费 LLR", "非编码比特"),
    ]
    headers = ["环地址", "状态", "写回动作", "含义"]
    widths = [150, 330, 270, 185]
    header_h = 56
    row_h = 72  # TEXT_FIT_OK: four-column HARQ table uses centered 24px wrapped labels.
    tx, ty = x, y + 58
    for col, (header, width) in enumerate(zip(headers, widths)):
        sx = tx + sum(widths[:col])
        draw.rectangle((sx, ty, sx + width, ty + header_h), fill="#173B61", outline="#173B61")
        text_center(draw, (sx, ty, sx + width, ty + header_h), header, font(24, True), "#FFFFFF")
    for ridx, row in enumerate(rows):
        ry = ty + header_h + row_h * ridx
        for col, (value, width) in enumerate(zip(row, widths)):
            sx = tx + sum(widths[:col])
            fill = "#FFFFFF" if ridx % 2 == 0 else "#EDF5FC"
            draw.rectangle((sx, ry, sx + width, ry + row_h), fill=fill, outline="#D6E0EB")
            text_center(draw, (sx, ry, sx + width, ry + row_h), value, font(24), PALETTE["ink"])

    formula_y = y + 448
    draw.text((x, formula_y), "核心公式：同一环地址 a 上的独立观测在 LLR 域相加，硬件实现用饱和加法。", font=font(24), fill=PALETTE["ink"])


def draw_rv_transmission_model(draw: ImageDraw.ImageDraw, rv_windows: dict[int, list[int]]) -> None:
    x, y = 100, 1240
    draw.text((x, y), "四个冗余版本的传输与接收模型", font=font(30, True), fill=PALETTE["ink"])
    draw.text(
        (x, y + 42),
        "每一行表示一次 HARQ 传输。发送端按 RV 起点读环；接收端按同一环地址写回 soft buffer，并区分新覆盖、重复覆盖和仍未知位置。",
        font=font(24),
        fill=PALETTE["muted"],
    )
    headers = ["传输", "发送端读取窗口", "LLR 流地址", "接收端写回动作", "传输后累计状态"]
    widths = [130, 455, 520, 450, 455]
    header_h = 58
    row_h = 206
    table_x = x
    table_y = y + 98
    for col, (header, width) in enumerate(zip(headers, widths)):
        sx = table_x + sum(widths[:col])
        draw.rectangle((sx, table_y, sx + width, table_y + header_h), fill="#173B61", outline="#173B61")
        text_center(draw, (sx, table_y, sx + width, table_y + header_h), header, font(24, True), "#FFFFFF")

    covered: set[int] = set()
    colors = {0: PALETTE["rv0"], 1: PALETTE["rv1"], 2: PALETTE["rv2"], 3: PALETTE["rv3"]}
    for rv in [0, 1, 2, 3]:
        addresses = rv_windows[rv]
        repeated = [a for a in addresses if a in covered]
        fresh = [a for a in addresses if a not in covered]
        covered.update(addresses)
        unknown = 32 - len(covered)
        row_y = table_y + header_h + row_h * rv
        fill = "#FFFFFF" if rv % 2 == 0 else "#F1F7FD"
        for col, width in enumerate(widths):
            sx = table_x + sum(widths[:col])
            draw.rectangle((sx, row_y, sx + width, row_y + row_h), fill=fill, outline="#D6E0EB")
        text_center(draw, (table_x, row_y, table_x + widths[0], row_y + row_h), f"RV{rv}", font(24, True), colors[rv])
        draw_wrapped(
            draw,
            (table_x + widths[0] + 14, row_y + 14),
            f"k0={addresses[0]}，顺时针扫描，跳过 <NULL>，取 E=11 个有效编码比特。",
            font(24),
            PALETTE["ink"],
            widths[1] - 28,
            8,
        )
        stream_x = table_x + widths[0] + widths[1] + 12
        stream_y = row_y + 16
        end_y = draw_address_chips(
            draw,
            stream_x,
            stream_y,
            addresses,
            set(repeated),
            colors[rv],
            cell_w=76,
            cell_h=56,
            gap=8,
            per_row=6,
        )
        draw.text((stream_x, end_y + 16), "黄色=重复命中；浅底=首次命中新地址", font=font(24), fill=PALETTE["muted"])
        action_x = table_x + sum(widths[:3]) + 14
        if repeated:
            action = f"新覆盖 {len(fresh)} 个地址；重复 {len(repeated)} 个地址执行饱和累加。"
        else:
            action = f"初次覆盖 {len(fresh)} 个地址；soft buffer 原值由中性 0 变为接收 LLR。"
        draw_wrapped(draw, (action_x, row_y + 14), action, font(24), PALETTE["ink"], widths[3] - 28, 8)
        state_x = table_x + sum(widths[:4]) + 14
        draw_wrapped(
            draw,
            (state_x, row_y + 14),
            f"已覆盖 {len(covered)}/32；仍未知 {unknown}/32。CRC 失败则保留缓存，等待下一 RV。",
            font(24),
            PALETTE["ink"],
            widths[4] - 28,
            8,
        )


def draw_bottom_notes(draw: ImageDraw.ImageDraw) -> None:
    x, y = 100, 2290
    draw.rounded_rectangle((x, y, 2120, y + 210), radius=16, fill="#FFF9E8", outline="#E3C45B", width=2)
    draw.text((x + 24, y + 20), "读图顺序与工程检查点", font=font(24, True), fill="#6F4B00")
    notes = [
        "1. 左侧同一个环：RV0、RV1、RV2、RV3 是读取窗口，不是四套编码器。",
        "2. 右上 LLR 流：按 RV 起点映射回环地址，不能按流序号合并。",
        "3. 右下 soft buffer：首次命中写入，重复命中累加，未命中保持，<NULL> 跳过。",
        "4. 验证记录：k0、E、命中地址、新覆盖数、重复覆盖数、饱和次数和 CRC 结果。",
    ]
    col_w = 960
    for idx, note in enumerate(notes):
        col = idx % 2
        row = idx // 2
        draw_wrapped(
            draw,
            (x + 30 + col * col_w, y + 72 + row * 62),
            note,
            font(24),
            PALETTE["ink"],
            col_w - 45,
            8,
        )


def main(output: Path | None = None) -> None:
    out = output or OUT_PATH
    img = Image.new("RGB", (2220, 3060), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    draw.text((58, 38), "LTE HARQ 冗余版本在循环缓存中的位置", font=font(38, True), fill="#0A2540")
    draw_wrapped(
        draw,
        (58, 88),
        "图 T7.3-1：四个 RV 共享同一个 rate-matching ring buffer；接收端按相同环地址写回 HARQ soft buffer。",
        font(24),
        PALETTE["muted"],
        1780,
    )
    draw.line((58, 132, 2162, 132), fill="#D5DFEA", width=2)

    rv_windows = draw_rv_ring(draw)
    draw_transmission_stream(draw, rv_windows)
    draw_soft_buffer_panel(draw, rv_windows)
    draw_arrow(draw, (850, 460), (1015, 365), PALETTE["rv1"], 5)
    draw_arrow(draw, (1560, 550), (1560, 600), PALETTE["rv1"], 5)
    draw_rv_transmission_model(draw, rv_windows)
    draw_bottom_notes(draw)

    foot = "生成脚本：tools/figures/render_lte_harq_rv_windows.py；教学参数非规范向量；协议依据见正文证据表。"
    draw.text((58, 3002), foot, font=font(24), fill="#647386")
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, optimize=True)
    print(out)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=None, help=f"output PNG path (default: {OUT_PATH})")
    args = parser.parse_args()
    main(output=args.output)
