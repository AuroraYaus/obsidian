#!/usr/bin/env python3
"""Render T14.5 soft-buffer and HARQ memory architecture figure."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T14.5_soft_buffer_HARQ_memory_architecture.png"



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
    draw.text(((x0 + x1) / 2, y0 + 36), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 22, y0 + 82, x1 - 22, y1 - 22), wrap(draw, body, TEXT, x1 - x0 - 44), TEXT, MUTED)


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


def assert_no_unrelated_crossing(name: str, points: list[tuple[float, float]], forbidden: dict[str, tuple[int, int, int, int]]) -> None:
    for p0, p1 in zip(points, points[1:]):
        for rect_name, rect in forbidden.items():
            if segment_intersects_rect(p0, p1, rect, margin=3):
                raise AssertionError(f"{name} segment {p0}->{p1} crosses {rect_name} {rect}")


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


def table(draw: ImageDraw.ImageDraw, x0: int, y0: int, headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 78) -> None:
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
    width, height = 2600, 2500
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((width / 2, 58), "T14.5 Soft Buffer and HARQ Memory Architecture", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Protocol identity selects the logical evidence store; implementation maps it to banks, transactions and lifecycle states."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    lte_ctx = (80, 170, 620, 350)
    nr_ctx = (1980, 170, 2520, 350)
    lte_addr = (80, 445, 620, 650)
    nr_addr = (1980, 445, 2520, 650)
    manager = (760, 210, 1840, 430)
    journal = (760, 515, 1840, 690)
    banks = (520, 805, 2080, 1045)
    sat = (80, 805, 430, 1045)
    masks = (2170, 805, 2520, 1045)
    life = (80, 1210, 2520, 1465)

    card(draw, lte_ctx, "LTE Turbo context", "Key: harq_id, codeword, TB epoch and CB id. RV belongs to the access transaction, not to a separate cache copy.", BLUE)
    card(draw, nr_ctx, "NR LDPC context", "Key extends with CBG id and CBGTI/CBGFI policy. Unscheduled CBG keeps old evidence.", GREEN)
    card(draw, manager, "Soft Buffer Manager", "Looks up logical evidence, opens read-modify-write transactions, applies NDI/epoch/CRC policy and owns release decisions.", AMBER)
    card(draw, lte_addr, "LTE address walk", "TS 36.212: per-CB circular buffer, NIR/Ncb, E and rvidx. NULL positions are skipped.", BLUE)
    card(draw, nr_addr, "NR address walk", "TS 38.212/38.214: per-CB k0/RV, E_r, CBGTI mask and optional CBGFI flush/combine.", GREEN)
    card(draw, journal, "Transaction Journal", "prepare -> write-combine -> commit. Reset, timeout or abort rolls back partial writes or marks them invalid.", PURPLE)
    card(draw, sat, "Saturation Unit", "Same code-bit address: old LLR + new LLR, then clamp to configured signed range and count sat events.", RED)
    card(draw, masks, "Masks and Status", "observed, valid, null, scheduled CBG, CB CRC, TB CRC, stale epoch and release eligibility.", GRAY)
    card(draw, banks, "Banked LLR SRAM", "Example mapping: bank = hash(harq, cb, addr) mod B; row = floor(addr / (B * lanes)); lane = addr mod lanes.", WHITE)

    arrow(draw, mid(lte_ctx, "right"), mid(manager, "left", -45))
    arrow(draw, mid(nr_ctx, "left"), mid(manager, "right", -45))
    arrow(draw, mid(lte_addr, "right"), mid(journal, "left"))
    arrow(draw, mid(nr_addr, "left"), mid(journal, "right"))
    arrow(draw, mid(manager, "bottom"), mid(journal, "top"))
    arrow(draw, mid(journal, "bottom"), mid(banks, "top"))
    arrow(draw, mid(sat, "right"), mid(banks, "left"))
    arrow(draw, mid(masks, "left"), mid(banks, "right"))

    release_route = [mid(life, "top", 750), (2050, 1140), (1800, 1140), mid(banks, "bottom", 490)]
    assert_no_unrelated_crossing("release_to_banks", release_route, {"sat": sat, "masks": masks})
    polyline_arrow(draw, release_route, "#78909c")

    table(
        draw,
        80,
        1585,
        ["Layer", "LTE Turbo", "NR LDPC", "Hardware rule"],
        [
            ["Logical key", "harq, codeword, TB epoch, CB", "harq, codeword, TB epoch, CBG, CB", "key selects evidence owner"],
            ["RV placement", "rvidx chooses LTE circular-buffer walk", "rv chooses k0; CBGTI may set E_r = 0", "RV is access metadata"],
            ["Combine", "same address accumulates LLR", "same address accumulates unless CBGFI flushes", "saturating add + sat counter"],
            ["CRC fail", "retain CB/TB evidence for retransmission", "retain scheduled CBG/CB evidence by policy", "never release on partial fail"],
            ["Eviction", "release on TB pass or new epoch", "release on TB pass, CBG flush or new epoch", "reclaim invalid/released only"],
        ],
        [390, 570, 610, 770],
        82,
    )

    draw.rounded_rectangle(life, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((width / 2, 1252), "Lifecycle FSM", font=HEAD, fill=INK, anchor="mm")
    states = [
        ("EMPTY", 210),
        ("ACTIVE_NEW", 560),
        ("ACCUMULATING", 970),
        ("CRC_FAIL_RETAIN", 1420),
        ("RELEASED", 1890),
        ("ABORT_ROLLBACK", 2310),
    ]
    y = 1350
    for label, x in states:
        draw.rounded_rectangle((x - 145, y - 38, x + 145, y + 38), radius=8, fill="#eef7ff", outline="#607d8b", width=2)
        draw.text((x, y), label, font=TABLE_HEAD, fill=INK, anchor="mm")
    for (_, x0), (_, x1) in zip(states[:4], states[1:5]):
        arrow(draw, (x0 + 145, y), (x1 - 145, y), "#607d8b", 3)
    abort_route = [
        (states[2][1], y + 38),
        (states[2][1], y + 92),
        (states[5][1], y + 92),
        (states[5][1], y + 38),
    ]
    state_boxes = {
        label: (x - 145, y - 38, x + 145, y + 38)
        for label, x in states
        if label not in {"ACCUMULATING", "ABORT_ROLLBACK"}
    }
    assert_no_unrelated_crossing("abort_route", abort_route, state_boxes)
    polyline_arrow(draw, abort_route, "#8d6e63", 3)

    note = (80, 2225, 2520, 2425)
    draw.rounded_rectangle(note, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((width / 2, 2265), "Read Order and Checks", font=HEAD, fill=INK, anchor="mm")
    lines = [
        "1. 3GPP identities determine the logical evidence space; bank formula is an implementation example.",
        "2. RV, rvidx, k0 and CBGTI describe one access, while the main cache key names the TB/CB/CBG owner.",
        "3. CRC failure retains evidence; TB pass, CBG flush, new epoch or abort decides release/rollback.",
    ]
    yy = 2315
    for line in lines:
        draw.text((width / 2, yy), line, font=TEXT, fill=MUTED, anchor="mm")
        yy += 36

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
