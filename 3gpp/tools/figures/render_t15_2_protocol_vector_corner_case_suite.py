#!/usr/bin/env python3
"""Render T15.2 protocol vector and corner-case suite figure."""

from __future__ import annotations

from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T15.2_protocol_vector_corner_case_suite.png"



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
    draw.text(((x0 + x1) / 2, y0 + 38), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 24, y0 + 86, x1 - 24, y1 - 24), wrap(draw, body, TEXT, x1 - x0 - 48), TEXT, MUTED)


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
    width, height = 3000, 3060
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((width / 2, 58), "T15.2 Protocol Vector and Corner-Case Suite", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Directed vectors turn Rel-19 clauses and decoder edge cases into replayable pass/fail evidence."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    top = {
        "evidence": (80, 180, 520, 390),
        "manifest": (620, 180, 1060, 390),
        "lte": (1160, 165, 1600, 405),
        "ldpc": (1700, 165, 2140, 405),
        "polar": (2240, 165, 2680, 405),
    }
    card(draw, top["evidence"], "Rel-19 Evidence", "TS section, table, formula, local path, extraction note and upstream lesson link.", BLUE)
    card(draw, top["manifest"], "Suite Manifest", "schema version, vector id, family, seed, expected status, dump policy and hash list.", GREEN)
    card(draw, top["lte"], "LTE Turbo Lane", "segmentation, filler, interleaver, RV window, soft combine, CB/TB CRC and timeout.", AMBER)
    card(draw, top["ldpc"], "NR LDPC Lane", "BG/Zc, filler, puncture, limited buffer, RV/k0, CBG, syndrome and CRC.", PURPLE)
    card(draw, top["polar"], "NR Polar Lane", "small block, CRC length, frozen mask, rate recovery, list pressure, RNTI selector.", RED)

    for a, b in [("evidence", "manifest"), ("manifest", "lte"), ("lte", "ldpc"), ("ldpc", "polar")]:
        arrow(draw, boundary_point(top[a], "right"), boundary_point(top[b], "left"), "#546e7a", 4)

    outcomes = {
        "policy": (640, 540, 1120, 760),
        "expected": (1260, 540, 1740, 760),
        "bundle": (1880, 540, 2360, 760),
    }
    card(draw, outcomes["policy"], "Pass / Fail Policy", "positive vectors require exact payload and checkpoints; negative vectors require expected fail class.", GREEN)
    card(draw, outcomes["expected"], "Expected Outcome", "payload, CRC/syndrome, status, trace checkpoints, latency bound and saturation counters.", BLUE)
    card(draw, outcomes["bundle"], "Failure Bundle", "descriptor, address trace, LLR snapshot, first mismatch, replay command and protocol evidence.", AMBER)
    arrow(draw, boundary_point(top["manifest"], "bottom"), boundary_point(outcomes["policy"], "top"), "#607d8b", 3)
    arrow(draw, boundary_point(top["ldpc"], "bottom"), boundary_point(outcomes["expected"], "top"), "#607d8b", 3)
    arrow(draw, boundary_point(outcomes["policy"], "right"), boundary_point(outcomes["expected"], "left"), "#607d8b", 3)
    arrow(draw, boundary_point(outcomes["expected"], "right"), boundary_point(outcomes["bundle"], "left"), "#607d8b", 3)

    band = (160, 860, 2840, 1010)
    draw.rounded_rectangle(band, radius=8, fill=GRAY, outline="#607d8b", width=2)
    centered(
        draw,
        band,
        [
            "Cross-family directed vectors: no-noise smoke, min/max sizes, LLR sign and saturation, CRC fail, expected-fail classification, mid-run reset, timeout and replay.",
            "Protocol-derived fields live in vector.json; implementation policies live in suite_policy.json and checkpoint_manifest.",
        ],
        TEXT,
        MUTED,
        gap=10,
    )

    table(
        draw,
        120,
        1120,
        ["Family", "Directed vector cases", "Bug caught", "Minimum dump fields"],
        [
            ["LTE Turbo", "small B, F>0, <NULL>, puncture/repetition, max C, Ncb<Kw, RV mismatch", "filler leaked into TB, wrong k0, soft combine overwrite, descriptor overflow", "B,C,r,K,F,E,Ncb,Kw,rv,k0, masks, soft before/after, CB/TB CRC"],
            ["NR LDPC", "BG/Zc boundary, filler, punctured systematic, limited buffer, RV, CBG, saturation", "wrong H shape, wrong circular-buffer address, held CBG corruption, syndrome/CRC mismatch", "A,R,BG,Zc,iLS,C,E,Ncb,rv,k0,CBGTI,CBGFI, syndrome, sat count"],
            ["NR Polar", "small block/no CRC, CRC length, list pressure, PM tie, puncture/shorten, frozen mask, RNTI", "wrong branch, wrong selector, path pruned, unstable tie-break, mask index error", "context,A,K,E,N,crc_len,RNTI,info/frozen hash, L, PM list, selector result"],
            ["Cross-family", "LLR sign, saturation, reset/abort, timeout, expected fail, schema/hash mismatch", "wrong soft-information convention, half commit, deadlock, false pass, non-replayable vector", "seed, llr format, quant profile, status/error, first mismatch, replay command"],
        ],
        [300, 760, 740, 960],
        row_h=132,
    )

    table(
        draw,
        120,
        1900,
        ["Suite tier", "Purpose", "Examples", "Pass criteria"],
        [
            ["smoke", "prove harness and sign convention", "no-noise LTE/LDPC/Polar, single CB, fixed seed", "payload and basic checkpoints pass"],
            ["directed positive", "prove protocol boundaries that should decode", "valid filler, valid RV sequence, valid CBG hold, valid RNTI", "payload/status/checkpoints match"],
            ["directed negative", "prove errors are detected and classified", "RV mismatch, wrong CRC length, wrong frozen mask, bad descriptor hash", "expected fail class and dump fields match"],
            ["stress/replay", "prove robustness and reproducibility", "max sizes, saturation, timeout, mid-run reset, random seed replay", "no silent pass; replay reproduces first mismatch"],
        ],
        [360, 700, 840, 860],
        row_h=122,
    )

    foot = (120, 2645, 2880, 2955)
    draw.rounded_rectangle(foot, radius=8, fill=WHITE, outline="#607d8b", width=2)
    centered(
        draw,
        foot,
        [
            "Read order: evidence -> manifest -> family lane -> expected outcome -> failure bundle -> regression tier.",
            "Engineering check: every vector must say whether it is protocol-derived, implementation-policy-derived, or negative expected-fail.",
            "Visual check: tables use 24px text and 122px+ row height; arrows use edge midpoints and vector-derived arrowheads.",
        ],
        TEXT,
        MUTED,
        gap=12,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
