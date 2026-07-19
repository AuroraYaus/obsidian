#!/usr/bin/env python3
"""Render T15.1 decoder SystemVerilog testbench architecture figure."""

from __future__ import annotations

from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T15.1_decoder_testbench_architecture.png"



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
    draw.text(((x0 + x1) / 2, y0 + 36), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 24, y0 + 82, x1 - 24, y1 - 24), wrap(draw, body, TEXT, x1 - x0 - 48), TEXT, MUTED)


def boundary_point(rect: tuple[int, int, int, int], side: str, offset: int = 0) -> tuple[float, float]:
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
    length = math.hypot(vx, vy)
    if length == 0:
        return
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill=color, width=width)
    px, py = -uy, ux
    draw.polygon(
        [
            (ex, ey),
            (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
            (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
        ],
        fill=color,
    )


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
    if max(ax, bx) < x0 or min(ax, bx) > x1 or max(ay, by) < y0 or min(ay, by) > y1:
        return False
    if x0 < ax < x1 and y0 < ay < y1:
        return True
    if x0 < bx < x1 and y0 < by < y1:
        return True
    for x in (x0, x1):
        if bx != ax:
            t = (x - ax) / (bx - ax)
            if 0 <= t <= 1:
                y = ay + t * (by - ay)
                if y0 <= y <= y1:
                    return True
    for y in (y0, y1):
        if by != ay:
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


def polyline_arrow(draw: ImageDraw.ImageDraw, points: list[tuple[float, float]], color: str = LINE, width: int = 4) -> None:
    if len(points) < 2:
        return
    head_len, head_w = 18, 9
    start = points[-2]
    ex, ey = points[-1]
    vx, vy = ex - start[0], ey - start[1]
    length = math.hypot(vx, vy)
    if length == 0:
        return
    ux, uy = vx / length, vy / length
    line_points = list(points[:-1]) + [(ex - ux * head_len, ey - uy * head_len)]
    for p0, p1 in zip(line_points, line_points[1:]):
        draw.line([p0, p1], fill=color, width=width)
    px, py = -uy, ux
    draw.polygon(
        [
            (ex, ey),
            (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
            (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def table(
    draw: ImageDraw.ImageDraw,
    x0: int,
    y0: int,
    headers: list[str],
    rows: list[list[str]],
    widths: list[int],
    row_h: int,
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
    width, height = 2800, 2380
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((width / 2, 58), "T15.1 Decoder SystemVerilog Testbench Architecture", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Golden vectors drive RTL; monitors capture responses; scoreboards compare status, payload and checkpoints."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    top = {
        "vectors": (90, 180, 470, 380),
        "loader": (560, 180, 940, 380),
        "driver": (1030, 180, 1410, 380),
        "dut": (1500, 160, 2070, 405),
        "monitor": (2160, 180, 2540, 380),
    }
    card(draw, top["vectors"], "Reference Vectors", "vector.json, LLR binary, expected bits, checkpoints, seed and Rel-19 evidence links.", BLUE)
    card(draw, top["loader"], "Vector Loader", "parse schema, validate hashes, build descriptor, preload memories and replay metadata.", GREEN)
    card(draw, top["driver"], "SV Driver", "reset, write registers, stream LLR, model backpressure and launch start pulse.", AMBER)
    card(draw, top["dut"], "Decoder DUT", "Turbo, LDPC, Polar engines behind register, DMA, soft-buffer and trace interfaces.", PURPLE)
    card(draw, top["monitor"], "SV Monitor", "sample outputs, status, IRQ, trace packets, counters and assertion events.", GREEN)

    for a, b in [("vectors", "loader"), ("loader", "driver"), ("driver", "dut"), ("dut", "monitor")]:
        arrow(draw, boundary_point(top[a], "right"), boundary_point(top[b], "left"), "#546e7a", 4)

    mid_cards = {
        "scoreboard": (600, 570, 1160, 780),
        "assertions": (1260, 570, 1820, 780),
        "failure": (1920, 570, 2480, 780),
    }
    card(draw, mid_cards["scoreboard"], "Scoreboard", "compare descriptor hash, payload, CRC/syndrome status, checkpoints and latency after alignment.", RED)
    card(draw, mid_cards["assertions"], "Assertions", "protocol-free hardware invariants: stable valid data, no write while busy, one-hot engine ownership.", AMBER)
    card(draw, mid_cards["failure"], "Failure Bundle", "first mismatch, vector id, waveform pointer, trace slice, register dump and replay command.", BLUE)

    arrow(draw, boundary_point(top["monitor"], "bottom", -80), boundary_point(mid_cards["scoreboard"], "top", 80), "#607d8b", 3)
    arrow(draw, boundary_point(top["driver"], "bottom"), boundary_point(mid_cards["assertions"], "top", -160), "#607d8b", 3)
    arrow(draw, boundary_point(top["dut"], "bottom"), boundary_point(mid_cards["assertions"], "top", 160), "#607d8b", 3)
    scoreboard_route = [
        boundary_point(mid_cards["scoreboard"], "bottom", 120),
        (1280, 835),
        (1900, 835),
        boundary_point(mid_cards["failure"], "bottom", -120),
    ]
    assert_no_unrelated_crossing(
        "scoreboard_to_failure_avoidance",
        scoreboard_route,
        {"assertions": mid_cards["assertions"]},
    )
    polyline_arrow(draw, scoreboard_route, "#78909c", 3)
    arrow(draw, boundary_point(mid_cards["assertions"], "right"), boundary_point(mid_cards["failure"], "left", 55), "#78909c", 3)

    reset_title = (90, 870, 2710, 925)
    centered(draw, reset_title, ["Reset and Timeout Tests are first-class sequences, not afterthoughts"], HEAD, INK)
    seqs = [
        ((120, 980, 505, 1145), "Clean Reset", "reset before start; registers and memories return to known state", BLUE),
        ((590, 980, 975, 1145), "Mid-run Reset", "abort during BUSY; no half-commit; status records abort", RED),
        ((1060, 980, 1445, 1145), "Timeout", "stall engine or DMA; ERROR and trace identify last checkpoint", AMBER),
        ((1530, 980, 1915, 1145), "Backpressure", "toggle ready; valid payload and sideband remain stable", GREEN),
        ((2000, 980, 2385, 1145), "Replay", "rerun failure bundle with full trace enabled", PURPLE),
    ]
    for rect, title, body, fill in seqs:
        card(draw, rect, title, body, fill)
    for (a, *_), (b, *__) in zip(seqs, seqs[1:]):
        arrow(draw, boundary_point(a, "right"), boundary_point(b, "left"), "#78909c", 3)

    table(
        draw,
        120,
        1250,
        ["Testbench role", "Consumes", "Produces", "Must catch"],
        [
            ["Reference loader", "T13.6 vector schema, T7/T9/T10 evidence", "typed descriptor and expected trace", "wrong vector version or protocol hash"],
            ["Driver", "descriptor, LLR, reset/timeout scenario", "register writes, DMA beats, start/abort", "bad ordering, unstable sideband, missing clear"],
            ["Monitor", "RTL interfaces and trace ports", "observed transactions and counters", "lost IRQ, wrong status, late trace"],
            ["Scoreboard", "expected + observed streams", "pass/fail, first mismatch, bundle", "payload/status/checkpoint divergence"],
            ["Assertions", "clocked interface invariants", "fatal or recoverable assertion event", "write while busy, one-hot violation, timeout"],
        ],
        [470, 690, 690, 750],
        row_h=98,
    )

    table(
        draw,
        120,
        1850,
        ["Decoder family", "Minimum directed focus", "Scoreboard checkpoint"],
        [
            ["LTE Turbo", "filler, RV window, CB CRC fail/pass, interleaver address", "turbo.branch, alpha_beta, extrinsic, crc"],
            ["NR LDPC", "BG/Zc, k0/RV, CBG hold/flush, syndrome early stop", "ldpc.rate_recovery, cn_update, layer, syndrome"],
            ["NR Polar", "frozen mask, rate recovery, list-size pressure, CRC/RNTI select", "polar.rate_recovery, fg, pm_prune, final"],
        ],
        [450, 930, 1190],
        row_h=96,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
