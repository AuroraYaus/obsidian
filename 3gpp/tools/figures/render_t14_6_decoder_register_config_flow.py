#!/usr/bin/env python3
"""Render T14.6 decoder register map and configuration flow figure."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T14.6_decoder_register_map_configuration_flow.png"



TITLE = font(42, True)
SUB = font(24)
HEAD = font(27, True)
TEXT = font(24)
TABLE = font(24)
TABLE_HEAD = font(24, True)

INK = "#102027"
MUTED = "#455a64"
LINE = "#546e7a"
BLUE = "#e3f2fd"
GREEN = "#e8f5e9"
AMBER = "#fff8e1"
PURPLE = "#f3e5f5"
RED = "#ffebee"
GRAY = "#eceff1"
WHITE = "#ffffff"


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
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


def centered(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    lines: list[str],
    fnt: ImageFont.ImageFont,
    fill: str = INK,
    gap: int = 7,
) -> None:
    x0, y0, x1, y1 = rect
    heights = [text_size(draw, line, fnt)[1] for line in lines]
    total = sum(heights) + gap * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    cx = (x0 + x1) / 2
    for line, height in zip(lines, heights):
        draw.text((cx, y + height / 2), line, font=fnt, fill=fill, anchor="mm")
        y += height + gap


def card(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, body: str, fill: str) -> None:
    x0, y0, x1, y1 = rect
    draw.rounded_rectangle(rect, radius=8, fill=fill, outline="#37474f", width=2)
    title_font = HEAD if text_size(draw, title, HEAD)[0] <= (x1 - x0 - 52) else font(24, True)
    draw.text(((x0 + x1) / 2, y0 + 36), title, font=title_font, fill=INK, anchor="mm")
    centered(draw, (x0 + 24, y0 + 84, x1 - 24, y1 - 24), wrap(draw, body, TEXT, x1 - x0 - 48), TEXT, MUTED)


def mid(rect: tuple[int, int, int, int], side: str, offset: int = 0) -> tuple[float, float]:
    x0, y0, x1, y1 = rect
    if side == "left":
        return x0, (y0 + y1) / 2 + offset
    if side == "right":
        return x1, (y0 + y1) / 2 + offset
    if side == "top":
        return (x0 + x1) / 2 + offset, y0
    if side == "bottom":
        return (x0 + x1) / 2 + offset, y1
    raise ValueError(side)


def boundary_point(rect: tuple[int, int, int, int], side: str, offset: int = 0) -> tuple[float, float]:
    return mid(rect, side, offset)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color: str = LINE, width: int = 4) -> None:
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill=color, width=width)
    px, py = -uy, ux
    pts = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=color)


def table(
    draw: ImageDraw.ImageDraw,
    x0: int,
    y0: int,
    headers: list[str],
    rows: list[list[str]],
    widths: list[int],
    row_h: int = 86,
) -> None:
    total_w = sum(widths)
    total_h = row_h * (len(rows) + 1)
    draw.rounded_rectangle((x0, y0, x0 + total_w, y0 + total_h), radius=8, fill=WHITE, outline="#607d8b", width=2)
    x = x0
    for header, width in zip(headers, widths):
        draw.rectangle((x, y0, x + width, y0 + row_h), fill="#e3f2fd", outline="#b0bec5", width=1)
        centered(draw, (x + 10, y0 + 6, x + width - 10, y0 + row_h - 6), wrap(draw, header, TABLE_HEAD, width - 20), TABLE_HEAD)
        x += width
    y = y0 + row_h
    for row in rows:
        x = x0
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill=WHITE, outline="#cfd8dc", width=1)
            centered(draw, (x + 10, y + 6, x + width - 10, y + row_h - 6), wrap(draw, value, TABLE, width - 20), TABLE)
            x += width
        y += row_h


def main() -> None:
    width, height = 2800, 2500
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((width / 2, 58), "T14.6 Decoder Register Map and Configuration Flow", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Protocol-derived fields, scheduler context and implementation policy are locked into one auditable hardware task."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    sources = [
        ((80, 175, 600, 355), "36.212 / 38.212", "Algorithm parameters: Turbo K/f1/f2/E/Ncb, LDPC BG/Zc/k0/E, Polar N/K/E/CRC context.", BLUE),
        ((720, 175, 1240, 355), "38.214 / 36.213", "Scheduler context: MCS, Qm, target rate, TBS, RV, HARQ process, NDI and CBG mask.", GREEN),
        ((1360, 175, 1880, 355), "MAC / RRC", "Configured limits: HARQ process count, CBG capability, MCS tables and serving-cell context. Exact fields pending where noted.", AMBER),
        ((2000, 175, 2520, 355), "Implementation Policy", "List size, max iterations, timeout, trace mask, IRQ enable, LLR width and error handling.", PURPLE),
    ]
    for rect, title, body, fill in sources:
        card(draw, rect, title, body, fill)

    regs = [
        ((90, 520, 430, 710), "CAPABILITY", "families, llr widths, banks, trace depth", GRAY),
        ((480, 520, 820, 710), "COMMON_CFG", "family, task_id, carrier, cw, cb, llr_width", BLUE),
        ((870, 520, 1210, 710), "SOFTBUF_CFG", "harq_id, ndi, rv, cbg_mask, cbgfi, sat_mode", GREEN),
        ((1260, 520, 1600, 710), "TURBO_CFG", "K, f1, f2, E, Ncb, max_iter", AMBER),
        ((1650, 520, 1990, 710), "LDPC_CFG", "BG, Zc, iLS, E, Ncb, max_iter", AMBER),
        ((2040, 520, 2380, 710), "POLAR_CFG", "N, K, E, list_size, crc_type, mask_hash", AMBER),
        ((2430, 520, 2710, 710), "CTRL / IRQ", "start, abort, busy, done, error, irq, trace", RED),
    ]
    for rect, title, body, fill in regs:
        card(draw, rect, title, body, fill)

    for i, (src_rect, _, _, _) in enumerate(sources):
        dst_rect = regs[min(i + 1, len(regs) - 1)][0]
        arrow(draw, boundary_point(src_rect, "bottom"), boundary_point(dst_rect, "top"), "#607d8b", 3)
    for (a, *_), (b, *__) in zip(regs, regs[1:]):
        arrow(draw, boundary_point(a, "right"), boundary_point(b, "left"), "#78909c", 3)

    fsm_title = (90, 825, 2710, 875)
    centered(draw, fsm_title, ["Configuration FSM: descriptor writes are mutable only before LOCK_DESCRIPTOR"], HEAD, INK)
    fsm = [
        ((120, 920, 410, 1055), "IDLE", "no active task", BLUE),
        ((470, 920, 760, 1055), "WRITE_CFG", "software writes fields", GREEN),
        ((820, 920, 1110, 1055), "LOCK_DESCRIPTOR", "freeze snapshot", AMBER),
        ((1170, 920, 1460, 1055), "LEGALITY_CHECK", "range and source checks", PURPLE),
        ((1520, 920, 1810, 1055), "START", "one-cycle launch", RED),
        ((1870, 920, 2160, 1055), "BUSY", "engine owns task", GRAY),
        ((2220, 920, 2510, 1055), "DONE / ERROR", "status + irq", BLUE),
    ]
    for rect, title, body, fill in fsm:
        card(draw, rect, title, body, fill)
    for (a, *_), (b, *__) in zip(fsm, fsm[1:]):
        arrow(draw, boundary_point(a, "right"), boundary_point(b, "left"), "#546e7a", 3)

    table(
        draw,
        120,
        1180,
        ["Register group", "Representative fields", "Field source", "Receiver-side consequence"],
        [
            ["COMMON_CFG", "family, K/N/E, cb index, llr width", "36.212 / 38.212 + local descriptor", "selects engine and input/output buffer size"],
            ["SOFTBUF_CFG", "HARQ ID, NDI, RV, CBG mask, CBGFI", "38.214, 36.213 pending, MAC context", "selects old evidence, flush/combine and release policy"],
            ["TURBO_CFG", "K, f1, f2, E, Ncb, max iter", "36.212 Table 5.1.3-3 and rate matching", "drives LTE Turbo interleaver and circular-buffer recovery"],
            ["LDPC_CFG", "BG, Zc, iLS, k0, E, Ncb", "38.212 LDPC segmentation, lifting and bit selection", "drives parity-check schedule, address generator and RV window"],
            ["POLAR_CFG", "N, K, E, list size, CRC type", "38.212 Polar construction/rate matching + implementation policy", "drives frozen mask, rate recovery and CA-SCL selector"],
            ["CTRL / STATUS", "start, abort, busy, pass/fail, error code, IRQ", "implementation interface", "turns protocol task into a recoverable hardware transaction"],
        ],
        [380, 650, 690, 780],
        row_h=94,
    )

    table(
        draw,
        120,
        1950,
        ["Rule", "Engineering check"],
        [
            ["Do not write while BUSY", "writes after LOCK_DESCRIPTOR either ignored or raise ERR_WRITE_WHILE_BUSY"],
            ["Protocol vs policy", "list_size and max_iterations are implementation policy, not 3GPP forced values"],
            ["Evidence logging", "trace descriptor hash, bad field id, source group and final status for every task"],
        ],
        [620, 1940],
        row_h=92,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
