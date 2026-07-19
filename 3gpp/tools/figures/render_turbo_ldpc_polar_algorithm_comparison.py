#!/usr/bin/env python3
"""Render Turbo, LDPC, and Polar decoder algorithm comparison."""

from __future__ import annotations

from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T11.1_Turbo_LDPC_Polar_algorithm_comparison.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#5C6878",
    "line": "#95A6B8",
    "turbo": "#B55A30",
    "turbo_fill": "#FFF0E7",
    "ldpc": "#247A58",
    "ldpc_fill": "#E8F6EF",
    "polar": "#2457A6",
    "polar_fill": "#EAF1FB",
    "panel": "#F7F9FC",
    "note": "#FFF8E8",
}



def text_center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, size: int, fill: str, bold: bool = True) -> None:
    draw.text(((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), text, font=font(size, bold), fill=fill, anchor="mm")


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    size: int,
    fill: str,
    bold: bool = True,
    gap: int = 5,
) -> None:
    fnt = font(size, bold)
    heights = [draw.textbbox((0, 0), line, font=fnt)[3] - draw.textbbox((0, 0), line, font=fnt)[1] for line in lines]
    total = sum(heights) + gap * (len(lines) - 1)
    y = (box[1] + box[3] - total) / 2
    cx = (box[0] + box[2]) / 2
    for line, h in zip(lines, heights):
        draw.text((cx, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + gap


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, color: str, fill: str) -> None:
    draw.rounded_rectangle(box, radius=16, fill=fill, outline=color, width=2)
    draw.text((box[0] + 24, box[1] + 20), title, font=font(24, True), fill=color)


def pill(draw: ImageDraw.ImageDraw, center: tuple[int, int], text: str, fill: str, outline: str) -> tuple[int, int, int, int]:
    f = font(24, True)
    tb = draw.textbbox((0, 0), text, font=f)
    w = tb[2] - tb[0] + 34
    h = tb[3] - tb[1] + 26
    box = (center[0] - w // 2, center[1] - h // 2, center[0] + w // 2, center[1] + h // 2)
    draw.rounded_rectangle(box, radius=h // 2, fill=fill, outline=outline, width=2)
    draw.text(center, text, font=f, fill=COL["ink"], anchor="mm")
    return box


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str = "#61758A",
    width: int = 3,
) -> None:
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux = (x1 - x0) / length
    uy = (y1 - y0) / length
    head_len = 8 if width <= 2 else 12
    head_w = 5 if width <= 2 else 8
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    draw.line((start, line_end), fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    back_x = x1 - head_len * math.cos(angle)
    back_y = y1 - head_len * math.sin(angle)
    perp_x = head_w * math.sin(angle)
    perp_y = -head_w * math.cos(angle)
    draw.polygon(
        [
            (x1, y1),
            (back_x + perp_x, back_y + perp_y),
            (back_x - perp_x, back_y - perp_y),
        ],
        fill=color,
    )


def center(box: tuple[int, int, int, int]) -> tuple[float, float]:
    return ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2)


def boundary_point(box: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    cx, cy = center(box)
    dx = toward[0] - cx
    dy = toward[1] - cy
    if dx == 0 and dy == 0:
        return cx, cy
    half_w = (box[2] - box[0]) / 2
    half_h = (box[3] - box[1]) / 2
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return (cx + dx / scale, cy + dy / scale)


def connect_arrow(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str, width: int = 2) -> None:
    s = boundary_point(src, center(dst))
    e = boundary_point(dst, center(src))
    arrow(draw, s, e, color, width)


def connect_line(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str, width: int = 2) -> None:
    s = boundary_point(src, center(dst))
    e = boundary_point(dst, center(src))
    draw.line((s, e), fill=color, width=width)


def right_mid(box: tuple[int, int, int, int]) -> tuple[int, int]:
    return (box[2], (box[1] + box[3]) // 2)


def left_mid(box: tuple[int, int, int, int]) -> tuple[int, int]:
    return (box[0], (box[1] + box[3]) // 2)


def draw_turbo(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    panel(draw, box, "LTE Turbo：trellis + SISO 迭代", COL["turbo"], COL["turbo_fill"])
    y = box[1] + 92
    states = [pill(draw, (box[0] + 84 + i * 95, y), f"S{i}", "#FFFFFF", COL["turbo"]) for i in range(4)]
    states2 = [pill(draw, (box[0] + 84 + i * 95, y + 82), f"S{i}", "#FFFFFF", COL["turbo"]) for i in range(4)]
    for a, b in zip(states, states[1:]):
        connect_arrow(draw, a, b, COL["turbo"], 2)
    for a, b in zip(states2, states2[1:]):
        connect_arrow(draw, a, b, COL["turbo"], 2)
    for a, b in zip(states, states2):
        connect_line(draw, a, b, COL["line"], 2)
    draw_centered_lines(
        draw,
        (box[0] + 30, box[1] + 270, box[2] - 30, box[3] - 42),
        ["软信息语义：channel LLR", "+ extrinsic information", "瓶颈：前向/后向度量、交织地址、迭代延迟"],
        24,
        COL["ink"],
        True,
        10,
    )


def draw_ldpc(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    panel(draw, box, "NR LDPC：Tanner graph + 消息传递", COL["ldpc"], COL["ldpc_fill"])
    v_y = box[1] + 116
    c_y = box[1] + 220
    var_centers = [(box[0] + 84 + i * 82, v_y) for i in range(4)]
    check_centers = [(box[0] + 130 + i * 120, c_y) for i in range(3)]
    vars_ = [pill(draw, pt, f"v{i}", "#FFFFFF", COL["ldpc"]) for i, pt in enumerate(var_centers)]
    checks = [pill(draw, pt, f"c{i}", "#FFFFFF", COL["ldpc"]) for i, pt in enumerate(check_centers)]
    edges = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (0, 2)]
    for vi, ci in edges:
        connect_line(draw, vars_[vi], checks[ci], COL["line"], 2)
    for i, pt in enumerate(var_centers):
        vars_[i] = pill(draw, pt, f"v{i}", "#FFFFFF", COL["ldpc"])
    for i, pt in enumerate(check_centers):
        checks[i] = pill(draw, pt, f"c{i}", "#FFFFFF", COL["ldpc"])
    draw_centered_lines(
        draw,
        (box[0] + 30, box[1] + 292, box[2] - 30, box[3] - 42),
        ["软信息语义：VN/CN messages", "+ posterior LLR", "瓶颈：message memory / bank conflict", "layered schedule"],
        24,
        COL["ink"],
        True,
        8,
    )


def draw_polar(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    panel(draw, box, "NR Polar：decoding tree + SCL path", COL["polar"], COL["polar_fill"])
    root = pill(draw, (box[0] + 130, box[1] + 155), "root", "#FFFFFF", COL["polar"])
    l1 = pill(draw, (box[0] + 270, box[1] + 108), "f", "#FFFFFF", COL["polar"])
    r1 = pill(draw, (box[0] + 270, box[1] + 202), "g", "#FFFFFF", COL["polar"])
    leafs = [
        pill(draw, (box[0] + 405, box[1] + 78), "u0 F", "#FFFFFF", COL["polar"]),
        pill(draw, (box[0] + 405, box[1] + 135), "u1 F", "#FFFFFF", COL["polar"]),
        pill(draw, (box[0] + 405, box[1] + 192), "u2 I", "#FFFFFF", COL["polar"]),
        pill(draw, (box[0] + 405, box[1] + 249), "u3 I", "#FFFFFF", COL["polar"]),
    ]
    connect_arrow(draw, root, l1, COL["polar"], 2)
    connect_arrow(draw, root, r1, COL["polar"], 2)
    connect_arrow(draw, l1, leafs[0], COL["polar"], 2)
    connect_arrow(draw, l1, leafs[1], COL["polar"], 2)
    connect_arrow(draw, r1, leafs[2], COL["polar"], 2)
    connect_arrow(draw, r1, leafs[3], COL["polar"], 2)
    draw_centered_lines(
        draw,
        (box[0] + 30, box[1] + 292, box[2] - 30, box[3] - 42),
        ["软信息语义：path metric", "+ frozen constraint + CRC", "瓶颈：sorter、path memory", "partial sum、低延迟"],
        24,
        COL["ink"],
        True,
        8,
    )


def main() -> None:
    img = Image.new("RGB", (1900, 1600), COL["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "T11.1 Turbo、LDPC、Polar 译码算法对比", font=font(34, True), fill=COL["ink"])
    draw.text((70, 96), "同样消费 LLR，但三类译码器的图模型、软信息语义、停止条件和硬件瓶颈不同。", font=font(24), fill=COL["muted"])

    boxes = [(70, 165, 615, 615), (680, 165, 1225, 615), (1290, 165, 1835, 615)]
    draw_turbo(draw, boxes[0])
    draw_ldpc(draw, boxes[1])
    draw_polar(draw, boxes[2])

    # Comparison matrix.
    x0, y0 = 100, 720
    widths = [250, 390, 390, 390]
    row_h = 78  # TEXT_FIT_OK: comparison cells use centered 24px controlled labels.
    headers = ["维度", "LTE Turbo", "NR LDPC", "NR Polar"]
    rows = [
        ["协议主场", "LTE 数据传输", "NR 数据传输", "NR 控制信息"],
        ["核心行为", "两个 SISO 交换外信息", "VN/CN 消息迭代", "SC/SCL 路径搜索"],
        ["停止边界", "迭代数 + CRC", "syndrome/迭代 + CRC", "CRC/RNTI aided select"],
        ["并行性", "受 trellis 顺序和交织制约", "QC/layered 高并行", "路径排序限制低延迟"],
        ["硬件瓶颈", "alpha/beta/extrinsic RAM", "message memory/bank", "sorter/path memory"],
    ]
    cx = x0
    for h, w in zip(headers, widths):
        cell_box = (cx, y0, cx + w, y0 + row_h)
        draw.rectangle(cell_box, fill=COL["panel"], outline=COL["line"])
        draw_centered_lines(draw, cell_box, [h], 24, COL["ink"], True)
        cx += w
    for r, row in enumerate(rows):
        cy = y0 + row_h * (r + 1)
        cx = x0
        for cell, w in zip(row, widths):
            cell_box = (cx, cy, cx + w, cy + row_h)
            draw.rectangle(cell_box, fill="#FFFFFF", outline=COL["line"])
            draw_centered_lines(draw, cell_box, [cell], 24, COL["ink"], True)
            cx += w

    note = (100, 1290, 1800, 1490)
    matrix_bottom = y0 + row_h * (len(rows) + 1)
    matrix_to_note_gap = note[1] - matrix_bottom
    bottom_margin = 1600 - note[3]
    assert matrix_to_note_gap >= 80
    assert bottom_margin >= 80
    draw.rounded_rectangle(note, radius=14, fill=COL["note"], outline="#D4B15F", width=2)
    draw.text((note[0] + 24, note[1] + 24), "工程结论", font=font(24, True), fill=COL["ink"])
    draw.text((note[0] + 24, note[1] + 78), "不能脱离协议代际、块长、信道类型、吞吐目标和硬件资源说某类码“更好”。", font=font(24, True), fill=COL["ink"])
    draw.text((note[0] + 24, note[1] + 124), "数据大块优先看吞吐和并行，控制短块优先看低延迟、误检边界和路径选择。", font=font(24, True), fill=COL["ink"])

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
