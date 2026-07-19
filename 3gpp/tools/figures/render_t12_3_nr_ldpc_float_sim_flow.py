#!/usr/bin/env python3
"""Render T12.3 NR LDPC floating-point simulation flow."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T12.3_NR_LDPC_float_sim_flow.png"



TITLE = font(36, True)
HEAD = font(26, True)
TEXT = font(24)
SMALL = font(24)
TINY = font(24)


def size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0], b[3] - b[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        cand = word if not cur else f"{cur} {word}"
        if size(draw, cand, fnt)[0] <= width:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_height(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[3] - b[1]


def centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    fnt: ImageFont.ImageFont,
    center_x: float,
    y0: float,
    y1: float,
    fill: str,
    line_gap: int = 8,
) -> None:
    heights = [text_height(draw, line, fnt) for line in lines]
    total = sum(heights) + line_gap * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    for line, h in zip(lines, heights):
        draw.text((center_x, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + line_gap


def box(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, body: str, fill: str) -> None:
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=12, fill=fill, outline="#263238", width=2)
    draw.text(((x0 + x1) / 2, y0 + 32), title, font=HEAD, fill="#102027", anchor="mm")
    lines = wrap(draw, body, TINY, x1 - x0 - 44)
    centered_lines(draw, lines, TINY, (x0 + x1) / 2, y0 + 76, y1 - 24, "#263238")


def center(rect: tuple[int, int, int, int]) -> tuple[float, float]:
    return (rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2


def boundary_point(src: tuple[int, int, int, int], dst: tuple[int, int, int, int]) -> tuple[float, float]:
    sx, sy = center(src)
    dx, dy = center(dst)
    vx, vy = dx - sx, dy - sy
    if vx == 0 and vy == 0:
        return sx, sy
    hw, hh = (src[2] - src[0]) / 2, (src[3] - src[1]) / 2
    tx = hw / abs(vx) if vx else float("inf")
    ty = hh / abs(vy) if vy else float("inf")
    t = min(tx, ty)
    return sx + vx * t, sy + vy * t


def arrow_between(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int]) -> None:
    ax, ay = boundary_point(src, dst)
    bx, by = boundary_point(dst, src)
    vx, vy = bx - ax, by - ay
    length = max((vx * vx + vy * vy) ** 0.5, 1.0)
    ux, uy = vx / length, vy / length
    head_len = 18
    head_w = 9
    line_end = (bx - ux * head_len, by - uy * head_len)
    draw.line([(ax, ay), line_end], fill="#37474f", width=4)
    px, py = -uy, ux
    draw.polygon(
        [
            (bx, by),
            (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w),
            (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w),
        ],
        fill="#37474f",
    )


def cell(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], text: str, fnt: ImageFont.ImageFont, fill: str = "#263238") -> None:
    x0, y0, x1, y1 = xy
    draw.text(((x0 + x1) / 2, (y0 + y1) / 2), text, font=fnt, fill=fill, anchor="mm")


def main() -> None:
    W, H = 2200, 1800
    img = Image.new("RGB", (W, H), "#f9fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((W / 2, 56), "T12.3 NR LDPC Floating-Point Simulation Plan", font=TITLE, fill="#102027", anchor="mm")
    subtitle = "BG/Zc protocol parameters, rate recovery, BP/MS/NMS/OMS variants, BLER outputs and failure replay"
    centered_lines(draw, wrap(draw, subtitle, TEXT, W - 220), TEXT, W / 2, 80, 126, "#455a64")

    top_y0, top_y1 = 170, 420
    w, gap = 285, 58
    xs = [70 + i * (w + gap) for i in range(6)]
    titles = ["Protocol Config", "TB/CB Builder", "BG + Zc Select", "LDPC Encoder", "Rate Match + RV", "AWGN + LLR"]
    bodies = [
        "TS 38.212/38.214 refs, channel, A, R, Qm, rv, BG rule, max_iter, decoder variant.",
        "TB CRC, LDPC segmentation, CB CRC, filler, CBG and descriptor metadata.",
        "Base graph, Kb, lifting set, Zc, N, K, parity-check matrix identity.",
        "QC-LDPC encode reference, systematic and parity regions, shortened/filler masks.",
        "Circular buffer, k0, limited-buffer mode, bit interleaving and transmitted positions.",
        "Eb/N0 sweep, effective rate, noise seed, demapper LLR, POS_ZERO convention.",
    ]
    fills = ["#e3f2fd", "#e8f5e9", "#fff3e0", "#ede7f6", "#fce4ec", "#e0f2f1"]
    nodes: list[tuple[int, int, int, int]] = []
    for x, title, body, fill in zip(xs, titles, bodies, fills):
        rect = (x, top_y0, x + w, top_y1)
        nodes.append(rect)
        box(draw, rect, title, body, fill)
    for a, b in zip(nodes, nodes[1:]):
        arrow_between(draw, a, b)

    mid = {
        "archive": (250, 600, 760, 855),
        "checks": (845, 600, 1355, 855),
        "decoder": (1440, 600, 1950, 855),
    }
    box(draw, mid["decoder"], "LDPC Decoder Variants", "Flooding or layered BP, MS, NMS and OMS with syndrome and CRC stopping records.", "#f1f8e9")
    box(draw, mid["checks"], "Trace + Metrics", "BG, Zc, rv, k0, E, Ncb, iter, syndrome, CRC, BLER, BER, avg_iter.", "#fffde7")
    box(draw, mid["archive"], "Failure Replay Archive", "resolved config, seeds, vector.json, LLR arrays, decoded bits, trace and evidence.md.", "#e8eaf6")
    arrow_between(draw, nodes[-1], mid["decoder"])
    arrow_between(draw, mid["decoder"], mid["checks"])
    arrow_between(draw, mid["checks"], mid["archive"])

    table = (120, 950, 2080, 1395)
    draw.rounded_rectangle(table, radius=12, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((W / 2, 985), "Experiment Matrix Example", font=HEAD, fill="#102027", anchor="mm")
    headers = ["Case", "Variant", "Protocol params", "Stop rule", "Saved evidence"]
    rows = [
        ["smoke", "MS", "BG1/BG2 small set, rv0", "100 frames or 20 errors", "metrics + first failures"],
        ["reference", "BP + NMS", "BG/Zc/R sweep, rv0", "1000 frames or 100 errors", "config + curve data"],
        ["harq", "NMS", "rv0, rv2, CBG masks", "replay fixed frames", "soft buffer traces"],
        ["edge", "OMS", "limited buffer, filler, short", "injected failures", "full decoder dump"],
    ]
    col_widths = [220, 300, 470, 430, 520]
    x0 = table[0] + 20
    col_edges = [x0]
    for cw in col_widths:
        col_edges.append(col_edges[-1] + cw)
    row_edges = [1028, 1098, 1170, 1242, 1314, 1386]
    for yy in row_edges:
        draw.line([(table[0] + 20, yy), (table[2] - 20, yy)], fill="#cfd8dc", width=1)
    for xx in col_edges[1:-1]:
        draw.line([(xx, 1028), (xx, 1386)], fill="#e0e7ea", width=1)
    for idx, h in enumerate(headers):
        cell(draw, (col_edges[idx], 1028, col_edges[idx + 1], 1088), h, SMALL, "#102027")
    for r, row in enumerate(rows):
        for c, text in enumerate(row):
            cell(draw, (col_edges[c], row_edges[r + 1], col_edges[c + 1], row_edges[r + 2]), text, TINY if c >= 2 else SMALL)

    note = (120, 1485, 2080, 1745)
    draw.rounded_rectangle(note, radius=12, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((W / 2, 1500), "Engineering Checks", font=HEAD, fill="#102027", anchor="mm")
    centered_lines(
        draw,
        [
            "Record BG, Zc, lifting set, k0, Ncb, E, limited-buffer state and bit-interleaver mode for every frame.",
            "Use identical payload/noise seeds when comparing BP, MS, NMS and OMS; otherwise the curves are not comparable.",
            "Protocol evidence constrains BG selection, lifting and rate matching; BLER thresholds remain engineering goals.",
        ],
        SMALL,
        W / 2,
        1538,
        1668,
        "#37474f",
        line_gap=11,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
