#!/usr/bin/env python3
"""Render T14.4 unified decoder subsystem architecture."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T14.4_unified_decoder_subsystem_architecture.png"



TITLE = font(42, True)
SUB = font(24)
HEAD = font(27, True)
TEXT = font(24)
SMALL = font(24)
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


def segment_intersects_rect(
    p0: tuple[float, float],
    p1: tuple[float, float],
    rect: tuple[int, int, int, int],
    margin: int = 0,
) -> bool:
    x0, y0, x1, y1 = rect
    x0 -= margin
    y0 -= margin
    x1 += margin
    y1 += margin
    ax, ay = p0
    bx, by = p1
    if (x0 < ax < x1 and y0 < ay < y1) or (x0 < bx < x1 and y0 < by < y1):
        return True
    if ax == bx:
        return x0 <= ax <= x1 and min(ay, by) <= y1 and max(ay, by) >= y0
    if ay == by:
        return y0 <= ay <= y1 and min(ax, bx) <= x1 and max(ax, bx) >= x0
    for x in (x0, x1):
        t = (x - ax) / (bx - ax)
        if 0 <= t <= 1:
            y = ay + t * (by - ay)
            if y0 <= y <= y1:
                return True
    for y in (y0, y1):
        t = (y - ay) / (by - ay)
        if 0 <= t <= 1:
            x = ax + t * (bx - ax)
            if x0 <= x <= x1:
                return True
    return False


def assert_no_unrelated_crossing(
    name: str,
    points: list[tuple[float, float]],
    forbidden: dict[str, tuple[int, int, int, int]],
) -> None:
    for p0, p1 in zip(points, points[1:]):
        for rect_name, rect in forbidden.items():
            if segment_intersects_rect(p0, p1, rect, margin=3):
                raise AssertionError(f"{name} segment {p0}->{p1} crosses {rect_name} {rect}")


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


def centered(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], lines: list[str], fnt, fill=INK, gap: int = 7) -> None:
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
    draw.text(((x0 + x1) / 2, y0 + 35), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 22, y0 + 80, x1 - 22, y1 - 22), wrap(draw, body, TEXT, x1 - x0 - 44), TEXT, MUTED)


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


def polyline_arrow(draw: ImageDraw.ImageDraw, points: list[tuple[float, float]], color: str = LINE, width: int = 4) -> None:
    if len(points) < 2:
        raise ValueError("polyline_arrow needs at least two points")
    *shaft, start_last, end = points
    sx, sy = start_last
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    line_points = [*shaft, start_last, line_end]
    for a, b in zip(line_points, line_points[1:]):
        draw.line([a, b], fill=color, width=width)
    px, py = -uy, ux
    pts = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=color)


def table(draw: ImageDraw.ImageDraw, x0: int, y0: int, headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 82) -> None:
    total_w = sum(widths)
    total_h = row_h * (len(rows) + 1)
    draw.rounded_rectangle((x0, y0, x0 + total_w, y0 + total_h), radius=8, fill="#ffffff", outline="#607d8b", width=2)
    x = x0
    for header, width in zip(headers, widths):
        draw.rectangle((x, y0, x + width, y0 + row_h), fill="#e3f2fd", outline="#b0bec5", width=1)
        centered(draw, (x + 10, y0 + 6, x + width - 10, y0 + row_h - 6), wrap(draw, header, TABLE_HEAD, width - 20), TABLE_HEAD)
        x += width
    y = y0 + row_h
    for row in rows:
        x = x0
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill="#ffffff", outline="#cfd8dc", width=1)
            centered(draw, (x + 10, y + 6, x + width - 10, y + row_h - 6), wrap(draw, value, TABLE, width - 20), TABLE)
            x += width
        y += row_h


def main() -> None:
    width, height = 2600, 2400
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)

    draw.text((width / 2, 58), "T14.4 Unified LTE / NR Decoder Subsystem", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Shared DMA, soft buffer, register control, three independent decoder engines, status, IRQ and trace."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    regs = (80, 175, 500, 390)
    dispatch = (590, 175, 1050, 390)
    in_dma = (1140, 175, 1540, 390)
    out_dma = (1640, 175, 2040, 390)
    irq = (2140, 175, 2520, 390)

    card(draw, regs, "Config Registers", "family, task id, length, soft-buffer key, bitwidth profile, start, timeout and trace mask.", BLUE)
    card(draw, dispatch, "Descriptor Dispatcher", "Checks common fields, selects Turbo / LDPC / Polar engine and locks immutable task context.", GREEN)
    card(draw, in_dma, "Input DMA", "Fetches LLR blocks or rate-recovered vectors with valid masks and byte-lane tags.", AMBER)
    card(draw, out_dma, "Output DMA", "Writes decoded payload, CB status, selected path metadata and result descriptors.", AMBER)
    card(draw, irq, "Status / IRQ", "done, fail, error code, stop reason, counter snapshot and interrupt moderation.", RED)

    turbo = (190, 560, 730, 845)
    ldpc = (930, 560, 1470, 845)
    polar = (1670, 560, 2210, 845)
    card(draw, turbo, "LTE Turbo Engine", "SISO A/B, alpha/beta RAM, extrinsic RAM, interleaver address and CRC early stop.", "#e1f5fe")
    card(draw, ldpc, "NR LDPC Engine", "QC schedule ROM, layered controller, CN min1/min2, VN RMW, bank conflict counters.", "#e8f5e9")
    card(draw, polar, "NR Polar Engine", "SC/SCL tree, LLR and partial-sum state, PM sorter, path remap and CRC/RNTI selector.", "#f3e5f5")

    soft = (330, 990, 1040, 1265)
    arb = (1190, 990, 1710, 1265)
    trace = (1860, 990, 2380, 1265)
    card(draw, soft, "HARQ Soft Buffer Manager", "Keyed by carrier / HARQ / TB epoch / CB / family; RV belongs to access transaction and trace.", "#fff3e0")
    card(draw, arb, "Shared Memory / DMA Arbiter", "Schedules input, output, soft-buffer RMW and engine-local burst access without crossing task ownership.", "#eceff1")
    card(draw, trace, "Trace FIFO / Failure Bundle", "Stores checkpoint id, descriptor hash, first mismatch fields, counters and optional waveform handles.", "#ede7f6")

    # Top flow.
    arrow(draw, mid(regs, "right"), mid(dispatch, "left"))
    arrow(draw, mid(dispatch, "right"), mid(in_dma, "left"))
    arrow(draw, mid(in_dma, "right"), mid(out_dma, "left"))
    arrow(draw, mid(out_dma, "right"), mid(irq, "left"))

    # Dispatcher to engines, with symmetric fanout on dispatcher bottom and engine top.
    arrow(draw, mid(dispatch, "bottom", -145), mid(turbo, "top"))
    arrow(draw, mid(dispatch, "bottom"), mid(ldpc, "top"))
    arrow(draw, mid(dispatch, "bottom", 145), mid(polar, "top"))

    # DMA and soft-buffer routes.
    arrow(draw, mid(in_dma, "bottom", -105), mid(turbo, "top", 130), "#78909c")
    arrow(draw, mid(in_dma, "bottom"), mid(ldpc, "top", 130), "#78909c")
    arrow(draw, mid(in_dma, "bottom", 105), mid(polar, "top", 130), "#78909c")
    arrow(draw, mid(turbo, "bottom"), mid(soft, "top", -190), "#8d6e63")
    arrow(draw, mid(ldpc, "bottom"), mid(arb, "top"), "#8d6e63")
    arrow(draw, mid(polar, "bottom"), mid(trace, "top", 0), "#8d6e63")

    arrow(draw, mid(soft, "right"), mid(arb, "left"))
    arrow(draw, mid(arb, "right"), mid(trace, "left"))
    # This diagnostic route must avoid the Polar card; the elbow runs in the
    # clear corridor above the engine row, then enters Output DMA from below.
    trace_to_output = [mid(trace, "top", 190), (2310, 470), (1840, 470), mid(out_dma, "bottom")]
    assert_no_unrelated_crossing("trace_to_output", trace_to_output, {"NR Polar Engine": polar})
    polyline_arrow(draw, trace_to_output, "#7e57c2")
    arrow(draw, mid(trace, "right", -30), mid(irq, "bottom"), "#7e57c2")

    rows = [
        ["Common regs", "start, family, task_id, llr_width, timeout", "All engines", "bad descriptor, timeout, reset abort"],
        ["Turbo private", "K, f1, f2, rvidx, max_iter", "Turbo only", "iter_used, crc_pass, extrinsic sat"],
        ["LDPC private", "BG, Zc, iLS, RV, CBG mask", "LDPC only", "syndrome weight, bank conflict"],
        ["Polar private", "N, K, E, list size, RNTI context", "Polar only", "selected path, CRC/RNTI pass mask"],
        ["Soft buffer", "main key plus RV transaction", "Turbo / LDPC data", "miss, stale epoch, partial write"],
    ]
    table(draw, 120, 1390, ["Block", "Register / context", "Owner", "Status evidence"], rows, [390, 640, 430, 720], 84)

    fsm_rows = [
        ["IDLE", "No active task; regs writable except sticky status.", "ready=1"],
        ["ACCEPT", "Descriptor locked and family-specific legality checks run.", "desc_hash"],
        ["LOAD", "DMA / soft buffer provide LLR and masks.", "input_count, key"],
        ["RUN_ENGINE", "Only selected engine owns local memories.", "engine_state"],
        ["COMMIT", "Output DMA, status and soft-buffer lifetime update.", "done or fail"],
        ["ERROR", "Abort without half-committed shared state.", "error_code"],
    ]
    table(draw, 120, 1930, ["FSM state", "Subsystem action", "Observable"], fsm_rows, [350, 1160, 590], 56)

    note = (2240, 1385, 2520, 2330)
    draw.rounded_rectangle(note, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text(((note[0] + note[2]) / 2, note[1] + 35), "Integration Rules", font=HEAD, fill=INK, anchor="mm")
    bullets = [
        "3GPP specs define task context, not this register map.",
        "Each engine can run with private mock DMA and private trace.",
        "Shared resources never own algorithm state.",
        "Soft-buffer writes are atomic per transaction.",
        "Trace uses T13.6 checkpoint names.",
        "IRQ summarizes status; debug keeps evidence.",
    ]
    y = note[1] + 88
    for item in bullets:
        lines = wrap(draw, item, SMALL, note[2] - note[0] - 44)
        centered(draw, (note[0] + 22, y, note[2] - 22, y + 82), lines, SMALL, MUTED, 5)
        y += 92

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
