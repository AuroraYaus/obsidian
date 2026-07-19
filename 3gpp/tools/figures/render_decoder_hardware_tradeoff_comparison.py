#!/usr/bin/env python3
"""Render Turbo/LDPC/Polar decoder hardware tradeoff comparison."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T11.4_decoder_hardware_tradeoff_comparison.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#5B6878",
    "line": "#A8B6C7",
    "turbo": "#B65B2E",
    "turbo_l": "#FFF0E6",
    "ldpc": "#22785A",
    "ldpc_l": "#E8F6EF",
    "polar": "#2457A6",
    "polar_l": "#EAF1FB",
    "shared": "#6E55A4",
    "shared_l": "#F1EDFF",
    "amber": "#B9841A",
    "amber_l": "#FFF5DD",
    "panel": "#F6F8FB",
}



def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    cur = ""
    for ch in text:
        if ch == "\n":
            if cur:
                tokens.append(cur)
                cur = ""
            tokens.append("\n")
        elif ch.isascii() and (ch.isalnum() or ch in "/_-+.[]"):
            cur += ch
        else:
            if cur:
                tokens.append(cur)
                cur = ""
            if ch.isspace():
                tokens.append(" ")
            else:
                tokens.append(ch)
    if cur:
        tokens.append(cur)
    return tokens


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    cur = ""
    for tok in tokenize(text):
        if tok == "\n":
            if cur:
                lines.append(cur.strip())
                cur = ""
            continue
        nxt = cur + tok
        if draw.textlength(nxt, font=fnt) <= width or not cur.strip():
            cur = nxt
        else:
            if cur.strip():
                lines.append(cur.strip())
            cur = tok
    if cur:
        lines.append(cur.strip())
    return lines


def center(box: tuple[int, int, int, int]) -> tuple[float, float]:
    return ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2)


def draw_centered(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str | list[str],
    size: int,
    color: str = COL["ink"],
    bold: bool = True,
    gap: int = 7,
) -> None:
    fnt = font(size, bold)
    raw_lines = text if isinstance(text, list) else [text]
    lines: list[str] = []
    for line in raw_lines:
        lines.extend(wrap(draw, line, fnt, box[2] - box[0] - 28))
    heights = [draw.textbbox((0, 0), line, font=fnt)[3] - draw.textbbox((0, 0), line, font=fnt)[1] for line in lines]
    total = sum(heights) + gap * (len(lines) - 1)
    available = box[3] - box[1]
    if total > available:
        preview_parts: list[str] = []
        for line in lines:
            if len(preview_parts) >= 2:
                break
            preview_parts.append(line)
        preview = " / ".join(preview_parts)
        raise RuntimeError(f"text overflow in {box}: need {total}px, available {available}px: {preview}")
    x = (box[0] + box[2]) / 2
    y = (box[1] + box[3] - total) / 2
    for line, h in zip(lines, heights):
        draw.text((x, y + h / 2), line, font=fnt, fill=color, anchor="mm")
        y += h + gap


def boundary_point(box: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    cx, cy = center(box)
    dx, dy = toward[0] - cx, toward[1] - cy
    if abs(dx) < 1e-6 and abs(dy) < 1e-6:
        return cx, cy
    half_w = max((box[2] - box[0]) / 2, 1)
    half_h = max((box[3] - box[1]) / 2, 1)
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return cx + dx / scale, cy + dy / scale


def arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color: str, width: int = 3) -> None:
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    head_len, head_w = 15, 9
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    draw.line((start, line_end), fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    back_x = x1 - head_len * math.cos(angle)
    back_y = y1 - head_len * math.sin(angle)
    perp_x = head_w * math.sin(angle)
    perp_y = -head_w * math.cos(angle)
    draw.polygon([(x1, y1), (back_x + perp_x, back_y + perp_y), (back_x - perp_x, back_y - perp_y)], fill=color)


def connect(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str) -> None:
    arrow(draw, boundary_point(src, center(dst)), boundary_point(dst, center(src)), color)


def node(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str | list[str],
    color: str,
    fill: str,
    size: int = 24,
) -> tuple[int, int, int, int]:
    draw.rounded_rectangle(box, radius=16, fill=fill, outline=color, width=2)
    draw_centered(draw, box, text, size=size, color=COL["ink"], bold=False)
    return box


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, color: str, fill: str) -> None:
    draw.rounded_rectangle(box, radius=22, fill=fill, outline=color, width=3)
    draw.text((box[0] + 26, box[1] + 22), title, font=font(31, True), fill=color)


def draw_datapath(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    color: str,
    fill: str,
    nodes: list[str],
    bottom_note: str,
) -> None:
    panel(draw, box, title, color, fill)
    left = box[0] + 40
    y = box[1] + 105
    w, h, gap = 225, 102, 18
    boxes = []
    for i, text in enumerate(nodes):
        b = (left + i * (w + gap), y, left + i * (w + gap) + w, y + h)
        boxes.append(node(draw, b, text, color, "#FFFFFF", 24))
    for a, b in zip(boxes, boxes[1:]):
        connect(draw, a, b, color)
    note_box = (box[0] + 40, box[1] + 245, box[2] - 40, box[1] + 340)
    draw.rounded_rectangle(note_box, radius=14, fill="#FFFFFF", outline=COL["line"], width=1)
    draw_centered(draw, note_box, bottom_note, 24, COL["ink"], False, 6)


def draw_datapaths(draw: ImageDraw.ImageDraw) -> int:
    y0 = 165
    draw_datapath(
        draw,
        (70, y0, 1830, y0 + 380),
        "Turbo 硬件数据通路：顺序 SISO 与交织外信息",
        COL["turbo"],
        COL["turbo_l"],
        ["LLR RAM", "SISO / BCJR", "alpha/beta memory", "interleaver", "extrinsic RAM", "iteration controller"],
        "瓶颈：trellis 前后向递推有顺序依赖；interleaver/deinterleaver 造成外信息 RAM 随机访问；迭代次数直接放大最坏延迟。",
    )
    y1 = y0 + 420
    draw_datapath(
        draw,
        (70, y1, 1830, y1 + 380),
        "LDPC 硬件数据通路：layered schedule 与消息存储",
        COL["ldpc"],
        COL["ldpc_l"],
        ["LLR RAM", "layered controller", "check-node unit", "variable-node update", "message memory", "bank conflict guard"],
        "优势：QC-LDPC 的 row/column group 适合并行；瓶颈：message memory、read-modify-write、bank conflict 和 pipeline stall。",
    )
    y2 = y1 + 420
    draw_datapath(
        draw,
        (70, y2, 1830, y2 + 380),
        "Polar 硬件数据通路：SCL 路径管理与排序",
        COL["polar"],
        COL["polar_l"],
        ["LLR memory", "SC/SCL tree controller", "partial sum memory", "path memory", "sorter", "CRC selector"],
        "瓶颈：information bit 分裂产生 2L 候选；sorter、path copy、partial sum 和 CRC state 必须同步重映射，控制延迟敏感。",
    )
    return y2 + 380


def draw_shared_table(draw: ImageDraw.ImageDraw, top: int) -> int:
    y0 = top + 105
    draw.text((90, y0 - 52), "统一译码子系统：可共享与不宜共享", font=font(32, True), fill=COL["ink"])
    x0 = 90
    widths = [320, 610, 610]
    row_h = 92
    rows = [
        ["类别", "可以共享", "不宜共享"],
        ["输入输出", "DMA、输入 LLR buffer、输出 hard bits FIFO、状态/中断寄存器", "codec-specific decoder input layout"],
        ["控制", "descriptor FIFO、配置寄存器、CRC checker wrapper", "Turbo iteration、LDPC layer、Polar path schedule"],
        ["计算", "饱和加法、比较器、CRC 多项式单元的封装", "Turbo SISO、LDPC CN/VN、Polar sorter/path memory"],
        ["存储", "顶层 SRAM allocator、bank 监控、trace buffer", "interleaver RAM、message memory、path copy memory"],
    ]
    for r, row in enumerate(rows):
        x = x0
        for c, cell in enumerate(row):
            b = (x, y0 + r * row_h, x + widths[c], y0 + (r + 1) * row_h)
            fill = COL["panel"] if r == 0 or c == 0 else "#FFFFFF"
            draw.rectangle(b, fill=fill, outline=COL["line"], width=1)
            is_head = r == 0 or c == 0
            draw_centered(draw, b, cell, 24, COL["ink"], is_head, 6)
            x += widths[c]
    return y0 + len(rows) * row_h


def draw_decision_matrix(draw: ImageDraw.ImageDraw, top: int) -> int:
    y0 = top + 105
    if y0 - top < 90:
        raise RuntimeError("shared-to-decision spacing too small")
    draw.text((90, y0 - 52), "工程决策矩阵", font=font(32, True), fill=COL["ink"])
    x0 = 90
    widths = [250, 430, 430, 430]
    row_h = 84  # TEXT_FIT_OK: cells use draw_centered() with wrap() and 24px text.
    rows = [
        ["维度", "Turbo", "LDPC", "Polar SCL"],
        ["并行度", "受 trellis 顺序依赖限制", "layer/edge/local index 并行友好", "路径并行受 sorter 限制"],
        ["延迟", "迭代次数放大最坏延迟", "高吞吐但轮数和 stall 影响尾延迟", "短块低延迟，排序关键路径敏感"],
        ["吞吐", "多 SISO 或多 CB 并行提升", "最适合宽并行数据业务", "控制块吞吐够用，非长块主力"],
        ["面积/功耗", "SISO 和外信息 RAM 主导", "CN/VN 阵列和 message RAM 主导", "path memory、sorter、copy network 主导"],
        ["验证难度", "外信息/交织/迭代早停", "bank conflict、message RMW、syndrome/CRC", "PM 排序、路径复制、CRC selector"],
    ]
    for r, row in enumerate(rows):
        x = x0
        for c, cell in enumerate(row):
            b = (x, y0 + r * row_h, x + widths[c], y0 + (r + 1) * row_h)
            fill = COL["panel"] if r == 0 or c == 0 else "#FFFFFF"
            draw.rectangle(b, fill=fill, outline=COL["line"], width=1)
            is_head = r == 0 or c == 0
            draw_centered(draw, b, cell, 24, COL["ink"], is_head, 5)
            x += widths[c]
    return y0 + len(rows) * row_h


def draw_footer(draw: ImageDraw.ImageDraw, top: int) -> None:
    y0 = top + 105
    if y0 - top < 90:
        raise RuntimeError("decision-to-footer spacing too small")
    boxes = [
        ("周期估算", "吞吐约等于 block_bits / cycles；Turbo cycles 随 2*SISO*iteration 增长，LDPC cycles 随 layers*iterations+stall 增长，Polar cycles 受 tree steps 和 sorter stages 影响。"),
        ("验证重点", "不要只比计算单元：必须同时 dump 地址、bank、message/path 状态、CRC/syndrome/PM、flush/reset 和 backpressure。"),
        ("设计结论", "LDPC 高吞吐友好来自稀疏图和 QC 规律；Polar SCL 延迟敏感来自 2L 候选排序和路径状态同步。"),
    ]
    x = 90
    for title, body in boxes:
        b = (x, y0, x + 540, y0 + 260)
        draw.rounded_rectangle(b, radius=16, fill=COL["amber_l"], outline=COL["amber"], width=2)
        draw_centered(draw, (b[0] + 20, b[1] + 18, b[2] - 20, b[1] + 60), title, 27, COL["ink"], True)
        draw_centered(draw, (b[0] + 24, b[1] + 68, b[2] - 24, b[3] - 20), body, 24, COL["ink"], False, 6)
        x += 590


def main(output: Path | None = None) -> None:
    out = output or OUT_PATH
    img = Image.new("RGB", (1900, 3040), COL["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "T11.4 Turbo / LDPC / Polar 硬件架构取舍", font=font(44, True), fill=COL["ink"])
    draw.text((70, 110), "对比并行度、存储访问、排序、迭代/列表深度、延迟、吞吐、功耗和验证风险。", font=font(26), fill=COL["muted"])
    bottom = draw_datapaths(draw)
    bottom = draw_shared_table(draw, bottom)
    bottom = draw_decision_matrix(draw, bottom)
    draw_footer(draw, bottom)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print(f"WROTE {out}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=None, help=f"output PNG path (default: {OUT_PATH})")
    args = parser.parse_args()
    main(output=args.output)
