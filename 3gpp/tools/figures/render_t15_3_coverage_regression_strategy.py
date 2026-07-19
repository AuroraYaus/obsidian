#!/usr/bin/env python3
"""Render T15.3 coverage and regression strategy figure."""

from __future__ import annotations

from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T15.3_coverage_regression_strategy.png"



TITLE = font(42, True)
SUB = font(24)
HEAD = font(28, True)
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
    gap: int = 8,
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
    draw.text(((x0 + x1) / 2, y0 + 42), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 24, y0 + 92, x1 - 24, y1 - 24), wrap(draw, body, TEXT, x1 - x0 - 48), TEXT, MUTED)


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
        centered(draw, (x + 12, y0 + 8, x + width - 12, y0 + row_h - 8), wrap(draw, header, TABLE_HEAD, width - 24), TABLE_HEAD)
        x += width
    y = y0 + row_h
    for idx, row in enumerate(rows):
        x = x0
        fill = WHITE if idx % 2 == 0 else "#fafafa"
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill=fill, outline="#cfd8dc", width=1)
            centered(draw, (x + 12, y + 8, x + width - 12, y + row_h - 8), wrap(draw, value, TABLE, width - 24), TABLE)
            x += width
        y += row_h


def main() -> None:
    width, height = 3000, 2860
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((width / 2, 58), "T15.3 Coverage and Regression Strategy", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Coverage answers what evidence exists; regression tiers decide when evidence is strong enough to sign off."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    cards = {
        "protocol": (90, 180, 520, 410),
        "vectors": (630, 180, 1060, 410),
        "coverage": (1170, 180, 1600, 410),
        "regression": (1710, 180, 2140, 410),
        "signoff": (2250, 180, 2680, 410),
    }
    card(draw, cards["protocol"], "Protocol Fields", "family, block length, RV, Qm, CRC, reset and CBG context from upstream vectors.", BLUE)
    card(draw, cards["vectors"], "Vector Suites", "smoke, directed, negative expected-fail, stress and replay tests with stable seeds.", GREEN)
    card(draw, cards["coverage"], "Coverage DB", "functional bins, cross bins, code coverage, assertion coverage and regression health.", AMBER)
    card(draw, cards["regression"], "Regression Tiers", "pre-commit, commit, nightly, weekly and release runs with deterministic replay.", PURPLE)
    card(draw, cards["signoff"], "Sign-off Gate", "required bins closed, no unclassified failures, failure bundles complete and reports archived.", RED)
    for left, right in [("protocol", "vectors"), ("vectors", "coverage"), ("coverage", "regression"), ("regression", "signoff")]:
        arrow(draw, boundary_point(cards[left], "right"), boundary_point(cards[right], "left"))

    middle = (140, 520, 2860, 710)
    draw.rounded_rectangle(middle, radius=8, fill=GRAY, outline="#607d8b", width=2)
    centered(
        draw,
        middle,
        [
            "Coverage is not test count. A thousand random frames can still miss RV2 with reset, Polar CRC24 with PM tie, or LDPC CBG hold after partial retransmission.",
            "Every bin must map to an observable field, a vector class, a failure class, or a coverage report line.",
        ],
        SMALL,
        MUTED,
        gap=12,
    )

    table(
        draw,
        120,
        820,
        ["Coverage object", "Core bins", "Cross bins", "Close condition"],
        [
            ["Algorithm family", "LTE Turbo, NR LDPC, NR Polar", "family x tier x expected status", "all required directed bins hit"],
            ["Protocol dimensions", "block length, RV, Qm, CRC status, reset", "family x length x RV x CRC; reset x soft-buffer state", "each legal bin hit; illegal bins classified"],
            ["Family-specific", "Turbo filler/Ncb; LDPC BG/Zc/CBG; Polar CRC/list/frozen", "LDPC BG x Zc x RV x CBG; Polar context x crc_len x L", "boundary bins hit by directed vectors"],
            ["Implementation health", "code coverage, assertion coverage, timeout, saturation", "module x tier; assertion x negative case", "threshold met and no waived critical hole"],
        ],
        [420, 680, 820, 800],
        row_h=118,
    )

    table(
        draw,
        120,
        1590,
        ["Tier", "When it runs", "Content", "Gate"],
        [
            ["pre-commit", "developer local change", "schema, smoke vectors, short assertions, no long BLER", "fast pass, no new unclassified fail"],
            ["commit", "merge queue or CI", "directed positive/negative, reset, timeout, LLR sign, saturation", "all required directed vectors pass"],
            ["nightly", "scheduled full run", "random seeds, stress sizes, cross coverage, replay of known failures", "coverage trend improves; no critical regression"],
            ["weekly/release", "sign-off window", "long seed sweep, BLER spot checks, code/assertion coverage, report freeze", "coverage thresholds and waiver review closed"],
        ],
        [360, 620, 1020, 760],
        row_h=122,
    )

    foot = (120, 2435, 2880, 2750)
    draw.rounded_rectangle(foot, radius=8, fill=WHITE, outline="#607d8b", width=2)
    centered(
        draw,
        foot,
        [
            "Failure triage order: reproduce by seed -> classify infrastructure/DUT/golden/protocol descriptor -> find first mismatch -> attach bundle -> decide fix, waiver, or new bin.",
            "Sign-off requires evidence, not confidence: bin report, code/assertion report, nightly summary, replay commands, open-risk list and owner approval.",
            "Visual check: all arrows are straight two-point shafts with vector-derived heads; tables use 24px text and centered cells.",
        ],
        SMALL,
        MUTED,
        gap=12,
    )

    title_to_node_gap = cards["protocol"][1] - 124
    flow_to_table_gap = 820 - middle[3]
    bottom_margin = height - foot[3]
    if title_to_node_gap < 36 or flow_to_table_gap < 80 or bottom_margin < 80:
        raise AssertionError(
            "T15.3 local spacing failed: "
            f"title_to_node_gap={title_to_node_gap}, "
            f"flow_to_table_gap={flow_to_table_gap}, bottom_margin={bottom_margin}"
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
