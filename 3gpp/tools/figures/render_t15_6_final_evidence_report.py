#!/usr/bin/env python3
"""Render T15.6 final decoder verification evidence report figure."""

from __future__ import annotations

from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T15.6_final_decoder_evidence_report.png"



TITLE = font(42, True)
SUB = font(24)
HEAD = font(28, True)
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
) -> tuple[int, int, int, int]:
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
    return x0, y0, x0 + total_w, y0 + total_h


def main() -> None:
    width, height = 3000, 3060
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((width / 2, 58), "T15.6 Final Decoder Verification Evidence Report", font=TITLE, fill=INK, anchor="mm")
    subtitle = "A sign-off package connects protocol evidence, model results, RTL regression, coverage, synthesis boundaries and known limits."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    cards = {
        "protocol": (90, 180, 520, 430),
        "model": (630, 180, 1060, 430),
        "rtl": (1170, 180, 1600, 430),
        "synth": (1710, 180, 2140, 430),
        "signoff": (2250, 180, 2680, 430),
    }
    card(draw, cards["protocol"], "Protocol Evidence", "TS package, section, table, formula, local path, extraction boundary and owner.", BLUE)
    card(draw, cards["model"], "Model Evidence", "floating-point, fixed-point, bit-exact traces, seeds, hashes and thresholds.", GREEN)
    card(draw, cards["rtl"], "RTL Regression", "directed tests, assertions, reset/timeout, failure bundle and replay command.", AMBER)
    card(draw, cards["synth"], "Synthesis Boundary", "DC availability, timing, area, power, constraints, waivers and not-run items.", PURPLE)
    card(draw, cards["signoff"], "Sign-off Report", "pass/fail gate, known limitations, waivers, evidence index and release decision.", RED)
    for left, right in [("protocol", "model"), ("model", "rtl"), ("rtl", "synth"), ("synth", "signoff")]:
        arrow(draw, boundary_point(cards[left], "right"), boundary_point(cards[right], "left"))

    note = (140, 540, 2860, 725)
    draw.rounded_rectangle(note, radius=8, fill=GRAY, outline="#607d8b", width=2)
    centered(
        draw,
        note,
        [
            "Final evidence is not a narrative summary. It is an indexed proof that every claim has a source, command, artifact, result and limitation.",
            "Current repository evidence includes plans, scripts and audits; unavailable tools and missing real reports must remain explicit limitations.",
        ],
        TEXT,
        MUTED,
        gap=12,
    )

    table1 = table(
        draw,
        120,
        835,
        ["Evidence Area", "Required Fields", "Current Boundary"],
        [
            ["Protocol", "TS, Rel-19 package, section, table/figure/formula, local path", "Use extracted 3GPP_Rel19/processed artifacts and upstream lessons"],
            ["Simulation", "seed, Eb/N0, vector id, command, BLER/BER or bit-exact result", "T12/T13 plans and toy snippets exist; no full BLER campaign here"],
            ["Fixed-point", "LLR width, saturation, loss budget, bit-exact diff, trace hash", "T13 model plans define fields; final report records real run status"],
            ["RTL", "testbench, directed vector suite, assertions, reset/timeout, coverage bins", "T15.1-T15.3 define architecture and gates; real simulator not run"],
            ["Synthesis", "DC version, library, SDC, WNS/TNS, area, power, timing fixes", "DC not installed; no mapped netlist or true reports in current environment"],
        ],
        [420, 1180, 1160],
        row_h=122,
    )

    table2 = table(
        draw,
        120,
        1665,
        ["Sign-off Gate", "Pass Evidence", "Fail / Hold Condition"],
        [
            ["Protocol traceability", "all vectors cite exact TS package and local extracted path", "aggregate wording, missing section, or unverified table"],
            ["Golden and fixed models", "seeded commands, thresholds and bit-exact summaries archived", "missing seed, missing threshold, unexplained mismatch"],
            ["RTL regression", "directed suites pass and expected-fail classes match", "unexpected pass/fail, timeout, reset half-commit"],
            ["Coverage", "required bins hit and waivers approved", "unhit critical cross or unclassified failure"],
            ["Synthesis/timing", "reports archived or unavailable boundary stated", "claiming timing closure without real report"],
            ["Known limitations", "owner, impact, close condition and waiver expiry recorded", "silent limitation or indefinite waiver"],
        ],
        [420, 1120, 1220],
        row_h=118,
    )

    foot = (120, 2660, 2880, 2950)
    draw.rounded_rectangle(foot, radius=8, fill=WHITE, outline="#607d8b", width=2)
    centered(
        draw,
        foot,
        [
            "Audit-ready rule: every green cell must name the command or file that proves it.",
            "A not-run item is acceptable only when it is explicit, scoped and assigned a close condition.",
            "Visual check: all flow arrows are straight two-point shafts; table text is centered at 24px with adequate row height.",
        ],
        TEXT,
        MUTED,
        gap=12,
    )

    title_to_node_gap = cards["protocol"][1] - 124
    flow_to_table_gap = table1[1] - note[3]
    table_gap = table2[1] - table1[3]
    bottom_margin = height - foot[3]
    if title_to_node_gap < 36 or flow_to_table_gap < 80 or table_gap < 80 or bottom_margin < 80:
        raise AssertionError(
            "T15.6 local spacing failed: "
            f"title_to_node_gap={title_to_node_gap}, flow_to_table_gap={flow_to_table_gap}, "
            f"table_gap={table_gap}, bottom_margin={bottom_margin}"
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
