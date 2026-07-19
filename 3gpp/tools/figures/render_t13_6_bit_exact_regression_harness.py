#!/usr/bin/env python3
"""Render T13.6 bit-exact regression harness pipeline."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T13.6_bit_exact_regression_harness.png"



TITLE = font(42, True)
HEAD = font(27, True)
TEXT = font(24)
TABLE = font(24)
TABLE_HEAD = font(24, True)

INK = "#102027"
MUTED = "#455a64"
LINE = "#546e7a"


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


def centered(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], lines: list[str], fnt, fill=INK, gap=7) -> None:
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
    draw.text(((x0 + x1) / 2, y0 + 34), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 24, y0 + 80, x1 - 24, y1 - 24), wrap(draw, body, TEXT, x1 - x0 - 48), TEXT, MUTED)


def center(rect: tuple[int, int, int, int]) -> tuple[float, float]:
    return (rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2


def boundary(src: tuple[int, int, int, int], dst: tuple[int, int, int, int]) -> tuple[float, float]:
    sx, sy = center(src)
    dx, dy = center(dst)
    vx, vy = dx - sx, dy - sy
    if vx == 0 and vy == 0:
        return sx, sy
    hw = (src[2] - src[0]) / 2
    hh = (src[3] - src[1]) / 2
    tx = hw / abs(vx) if vx else float("inf")
    ty = hh / abs(vy) if vy else float("inf")
    t = min(tx, ty)
    return sx + vx * t, sy + vy * t


def arrow(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color=LINE) -> None:
    ax, ay = boundary(src, dst)
    bx, by = boundary(dst, src)
    vx, vy = bx - ax, by - ay
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 20, 10
    end = (bx - ux * head_len, by - uy * head_len)
    draw.line([(ax, ay), end], fill=color, width=4)
    px, py = -uy, ux
    draw.polygon(
        [
            (bx, by),
            (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w),
            (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def point_arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color=LINE) -> None:
    ax, ay = start
    bx, by = end
    vx, vy = bx - ax, by - ay
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 20, 10
    line_end = (bx - ux * head_len, by - uy * head_len)
    draw.line([start, line_end], fill=color, width=4)
    px, py = -uy, ux
    draw.polygon(
        [
            (bx, by),
            (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w),
            (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def table(draw: ImageDraw.ImageDraw, x0: int, y0: int, headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 74) -> None:
    total_w = sum(widths)
    total_h = row_h * (len(rows) + 1)
    draw.rounded_rectangle((x0, y0, x0 + total_w, y0 + total_h), radius=8, fill="#ffffff", outline="#607d8b", width=2)
    y = y0
    x = x0
    for header, width in zip(headers, widths):
        draw.rectangle((x, y, x + width, y + row_h), fill="#e3f2fd", outline="#b0bec5", width=1)
        centered(draw, (x + 8, y + 5, x + width - 8, y + row_h - 5), wrap(draw, header, TABLE_HEAD, width - 16), TABLE_HEAD)
        x += width
    for row in rows:
        y += row_h
        x = x0
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill="#ffffff", outline="#cfd8dc", width=1)
            centered(draw, (x + 8, y + 5, x + width - 8, y + row_h - 5), wrap(draw, value, TABLE, width - 16), TABLE)
            x += width


def main() -> None:
    width, height = 2300, 2160
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)

    draw.text((width / 2, 58), "T13.6 Bit-Exact Regression Harness", font=TITLE, fill=INK, anchor="mm")
    subtitle = "One vector schema drives Python float/fixed, C/C++ fixed, RTL compare, CI and failure replay."
    centered(draw, (110, 82, width - 110, 132), wrap(draw, subtitle, TEXT, width - 220), TEXT, MUTED)

    top = [
        (70, 180, 430, 405),
        (525, 180, 885, 405),
        (980, 180, 1340, 405),
        (1435, 180, 1795, 405),
        (1890, 180, 2250, 405),
    ]
    titles = ["Protocol Vector", "Python Float", "Python Fixed", "C/C++ Fixed", "RTL Output"]
    bodies = [
        "TS evidence, seed, LLR, RV, code-block order and descriptor hashes.",
        "Numerical reference for BLER curves and algorithm sanity checks.",
        "Integer reference with the same rounding, saturation and trace schema.",
        "Production-style fixed model with layout version and checkpoint dumps.",
        "Cycle-aligned traces, valid masks, saturation counters and status bits.",
    ]
    fills = ["#e3f2fd", "#e8f5e9", "#fff8e1", "#ede7f6", "#fce4ec"]
    for rect, title, body, fill in zip(top, titles, bodies, fills):
        card(draw, rect, title, body, fill)
    for src, dst in zip(top, top[1:]):
        arrow(draw, src, dst)

    compare = (610, 520, 1690, 755)
    card(draw, compare, "Compare Core", "Validate metadata and hashes first, then compare checkpoints, final bits, CRC or syndrome, saturation counts and BLER budgets.", "#ffffff")
    point_arrow(draw, ((top[2][0] + top[2][2]) / 2, top[2][3]), (980, compare[1]))
    point_arrow(draw, ((top[3][0] + top[3][2]) / 2, top[3][3]), ((compare[0] + compare[2]) / 2, compare[1]))
    point_arrow(draw, ((top[4][0] + top[4][2]) / 2, top[4][3]), (1420, compare[1]))

    ci = (130, 840, 620, 1055)
    archive = (1680, 840, 2170, 1055)
    card(draw, ci, "CI Gate", "Smoke, directed, random, nightly and replay suites run with fixed seeds and frozen policy versions.", "#e0f2f1")
    card(draw, archive, "Failure Bundle", "Manifest, vector, inputs, traces, diff, logs and optional waveform are archived for first mismatch replay.", "#fff3e0")
    arrow(draw, compare, ci)
    arrow(draw, compare, archive)

    headers = ["Layer", "Compare Rule", "Failure Evidence"]
    rows = [
        ["Float vs fixed", "Tolerance or BLER budget", "metric diff + curve ref"],
        ["Python fixed vs C/C++", "Exact integer equality", "first mismatch trace"],
        ["C/C++ vs RTL", "Exact with latency align", "trace + waveform"],
        ["Metadata", "Hash equality required", "schema/version diff"],
    ]
    table(draw, 440, 1135, headers, rows, [420, 620, 620], row_h=78)

    lower_title_y = 1585
    draw.text((width / 2, lower_title_y), "Decoder Checkpoint Manifest", font=HEAD, fill=INK, anchor="mm")
    rows2 = [
        ["Turbo", "rate recovery, branch metric, alpha/beta, extrinsic, hard bits, CB/TB CRC"],
        ["LDPC", "rate recovery, quantized LLR, CN min1/min2, layer trace, posterior, syndrome, CRC"],
        ["Polar", "rate recovery, frozen mask, f/g LLR, partial sums, PM, prune order, CRC/RNTI"],
    ]
    table(draw, 185, 1640, ["Decoder", "Required Checkpoints"], rows2, [260, 1670], row_h=88)

    centered(
        draw,
        (100, 1980, 2200, 2095),
        [
            "Rule: final CRC pass is not enough. A passing vector must preserve protocol metadata, deterministic seed, layout hash, checkpoint policy and failure replay evidence."
        ],
        TEXT,
        "#37474f",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
