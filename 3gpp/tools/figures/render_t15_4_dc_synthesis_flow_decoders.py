#!/usr/bin/env python3
"""Render T15.4 Design Compiler synthesis flow figure."""

from __future__ import annotations

from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T15.4_DC_synthesis_flow_decoders.png"



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
    draw.text((width / 2, 58), "T15.4 Design Compiler Synthesis Flow for Decoders", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Synthesis turns RTL into a technology-mapped netlist, then reports timing, area, power and structural risks."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    cards = {
        "rtl": (90, 180, 520, 410),
        "setup": (630, 180, 1060, 410),
        "constraints": (1170, 180, 1600, 410),
        "compile": (1710, 180, 2140, 410),
        "reports": (2250, 180, 2680, 410),
    }
    card(draw, cards["rtl"], "RTL Inputs", "filelist, top module, decoder family, libraries, memory wrappers and design parameters.", BLUE)
    card(draw, cards["setup"], "DC Setup", "analyze, elaborate, link, uniquify, check_design and compile environment snapshot.", GREEN)
    card(draw, cards["constraints"], "SDC Constraints", "clock, reset, input/output delay, false paths, multicycle paths and load model.", AMBER)
    card(draw, cards["compile"], "Compile", "compile or compile_ultra, mapping, optimization, hierarchy policy and incremental compile.", PURPLE)
    card(draw, cards["reports"], "Reports", "timing, area, power, constraint violations, unmapped cells, DRC and netlist handoff.", RED)
    for left, right in [("rtl", "setup"), ("setup", "constraints"), ("constraints", "compile"), ("compile", "reports")]:
        arrow(draw, boundary_point(cards[left], "right"), boundary_point(cards[right], "left"))

    note = (140, 520, 2860, 710)
    draw.rounded_rectangle(note, radius=8, fill=GRAY, outline="#607d8b", width=2)
    centered(
        draw,
        note,
        [
            "Tool boundary: if dc_shell is not installed, only the script skeleton and report interpretation can be verified locally.",
            "Protocol vectors do not drive synthesis, but post-synthesis sanity and sign-off reports must link back to T15.1-T15.3 evidence.",
        ],
        TEXT,
        MUTED,
        gap=12,
    )

    table(
        draw,
        120,
        820,
        ["Artifact", "Decoder-specific risk", "DC check or report", "Evidence to archive"],
        [
            ["filelist", "missing engine file, duplicate package, wrong top", "analyze/elaborate/link/check_design", "filelist, top, git hash, log"],
            ["clock/reset", "async reset assumption, missing generated clock", "report_clock, report_timing, check_timing", "SDC, reset note, unconstrained paths"],
            ["compile plan", "flattening breaks debug, over-optimizing trace, memory wrapper mismatch", "compile log, report_qor, report_resources", "compile options and hierarchy policy"],
            ["reports", "negative slack, large area, high power, unmapped cells", "timing/area/power/constraint/DRC", "reports directory and issue triage"],
        ],
        [420, 760, 760, 820],
        row_h=120,
    )

    table(
        draw,
        120,
        1590,
        ["Path family", "Likely critical logic", "First action", "Do not hide"],
        [
            ["LTE Turbo", "ACS/branch metric, alpha-beta recursion, interleaver address", "check max delay and pipeline candidates", "wrong K/f1/f2 or rate-recovery metadata"],
            ["NR LDPC", "check-node min tree, layered message RAM mux, bank conflict logic", "separate combinational tree from memory path", "BG/Zc schedule or CBG control errors"],
            ["NR Polar", "SCL sorter, path-metric update, lazy-copy mux, CRC selector", "inspect sorter depth and list-size scaling", "CRC/RNTI or frozen-mask mistakes"],
            ["Unified subsystem", "dispatcher, soft-buffer key compare, DMA arbitration, IRQ/status fan-in", "split data path and control path reports", "reset/abort half-commit behavior"],
        ],
        [380, 880, 760, 740],
        row_h=122,
    )

    foot = (120, 2435, 2880, 2750)
    draw.rounded_rectangle(foot, radius=8, fill=WHITE, outline="#607d8b", width=2)
    centered(
        draw,
        foot,
        [
            "Read order: RTL inputs -> DC setup -> constraints -> compile -> reports -> triage -> verification handoff.",
            "A timing report is not a functional proof: failing or passing synthesis must be tied back to regression, coverage and known protocol-derived parameters.",
            "Visual check: arrows are straight two-point shafts with vector-derived heads; table text is centered and 24px.",
        ],
        TEXT,
        MUTED,
        gap=12,
    )

    title_to_node_gap = cards["rtl"][1] - 124
    flow_to_table_gap = 820 - note[3]
    bottom_margin = height - foot[3]
    if title_to_node_gap < 36 or flow_to_table_gap < 80 or bottom_margin < 80:
        raise AssertionError(
            "T15.4 local spacing failed: "
            f"title_to_node_gap={title_to_node_gap}, "
            f"flow_to_table_gap={flow_to_table_gap}, bottom_margin={bottom_margin}"
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
