#!/usr/bin/env python3
"""Render T13.4 NR Polar fixed-point model flow."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T13.4_NR_Polar_fixed_point_model.png"



TITLE = font(40, True)
HEAD = font(26, True)
TEXT = font(24)
SMALL = font(24)
TINY = font(24)


def text_box(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0], b[3] - b[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        cand = word if not cur else f"{cur} {word}"
        if text_box(draw, cand, fnt)[0] <= width:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def line_h(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[3] - b[1]


def centered(draw, lines, fnt, rect, fill="#263238", gap=7):
    x0, y0, x1, y1 = rect
    hs = [line_h(draw, line, fnt) for line in lines]
    total = sum(hs) + gap * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    cx = (x0 + x1) / 2
    for line, h in zip(lines, hs):
        draw.text((cx, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + gap


def card(draw, rect, title, body, fill):
    x0, y0, x1, y1 = rect
    draw.rounded_rectangle(rect, radius=8, fill=fill, outline="#263238", width=2)
    draw.text(((x0 + x1) / 2, y0 + 34), title, font=HEAD, fill="#102027", anchor="mm")
    centered(draw, wrap(draw, body, TINY, x1 - x0 - 44), TINY, (x0 + 22, y0 + 78, x1 - 22, y1 - 24))


def center(rect):
    return (rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2


def edge(src, dst):
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


def arrow(draw, src, dst):
    ax, ay = edge(src, dst)
    bx, by = edge(dst, src)
    vx, vy = bx - ax, by - ay
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    end = (bx - ux * head_len, by - uy * head_len)
    draw.line([(ax, ay), end], fill="#37474f", width=4)
    px, py = -uy, ux
    draw.polygon(
        [(bx, by), (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w), (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w)],
        fill="#37474f",
    )


def cell(draw, rect, text, fnt=TINY, fill="#263238"):
    centered(draw, wrap(draw, text, fnt, rect[2] - rect[0] - 18), fnt, (rect[0] + 7, rect[1] + 4, rect[2] - 7, rect[3] - 4), fill, gap=4)


def table(draw, rect):
    x0, y0, x1, y1 = rect
    draw.rounded_rectangle(rect, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text(((x0 + x1) / 2, y0 + 38), "Polar Fixed-Point Checkpoints", font=HEAD, fill="#102027", anchor="mm")
    cols = [x0 + 35, x0 + 285, x0 + 630, x0 + 1000, x1 - 35]
    rows = [y0 + 88, y0 + 154, y0 + 250, y0 + 346, y0 + 442, y0 + 538, y0 + 634]
    headers = ["Stage", "Integer Object", "Compare Field", "Failure Signal"]
    data = [
        ["Rate recovery", "LLR, masks, repetition", "rate_llr_trace", "puncture/shorten mix"],
        ["f/g tree", "node LLR and stage", "fg_llr_trace", "wrong sign or min"],
        ["Partial sum", "path beta memory", "partial_sum_trace", "bad g input"],
        ["Split/prune", "PM, path id, sorter", "candidate_pm, sort_order", "unstable path"],
        ["CRC/RNTI", "pass mask, selected path", "crc_pass_vec, selected_path", "invalid output"],
    ]
    for r in rows:
        draw.line([(cols[0], r), (cols[-1], r)], fill="#cfd8dc", width=1)
    for c in cols:
        draw.line([(c, rows[0]), (c, rows[-1])], fill="#e0e7ea", width=1)
    for i, h in enumerate(headers):
        cell(draw, (cols[i], rows[0], cols[i + 1], rows[1]), h, SMALL, "#102027")
    for r, row in enumerate(data):
        for c, text in enumerate(row):
            cell(draw, (cols[c], rows[r + 1], cols[c + 1], rows[r + 2]), text)


def main():
    W, H = 2200, 1840
    img = Image.new("RGB", (W, H), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((W / 2, 56), "T13.4 NR Polar Fixed-Point Model Plan", font=TITLE, fill="#102027", anchor="mm")
    subtitle = "f/g LLRs, path metric saturation, partial sums, sorter pruning and CRC-aided selection"
    centered(draw, wrap(draw, subtitle, TEXT, W - 220), TEXT, (110, 78, W - 110, 124), "#455a64")

    top = [
        (60, 160, 335, 430),
        (395, 160, 670, 430),
        (730, 160, 1005, 430),
        (1065, 160, 1340, 430),
        (1400, 160, 1675, 430),
        (1735, 160, 2140, 430),
    ]
    titles = ["Protocol Vector", "Rate Recovery", "Quantizer", "SC/SCL Core", "PM Sort/Prune", "CRC/RNTI Selector"]
    bodies = [
        "A, K, E, N, CRC, RNTI, info/frozen masks and TS 38.212 evidence. L belongs to fixed config.",
        "Restore codeword-order LLR with punctured, shortened and repeated position masks.",
        "Apply LLR width, Q format, clipping, strong known-zero and saturation rules.",
        "Compute f/g node LLRs and 1-bit partial sums for every active path.",
        "Update PM, normalize or saturate, sort 2L candidates and remap path state.",
        "Filter CRC/RNTI pass paths, select best PM path, emit valid/fail and replay trace.",
    ]
    fills = ["#e3f2fd", "#fff8e1", "#e8f5e9", "#ede7f6", "#f3e5f5", "#fce4ec"]
    for rect, title, body, fill in zip(top, titles, bodies, fills):
        card(draw, rect, title, body, fill)
    for a, b in zip(top, top[1:]):
        arrow(draw, a, b)

    table(draw, (60, 520, 2140, 1175))

    bottom = (60, 1285, 2140, 1730)
    draw.rounded_rectangle(bottom, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((W / 2, 1325), "Bitwidth and State Objects", font=HEAD, fill="#102027", anchor="mm")
    opts = [
        ("f/g LLR", "min-sum f, signed g, guard bits and node-stage trace"),
        ("Partial Sum", "1-bit GF(2) beta memory per path or lazy-copy state"),
        ("Path Metric", "PM increment, width, normalization, saturation and tie-break"),
        ("Sorter", "2L candidates to L survivors, stable path id remap"),
        ("Selector", "CRC/RNTI pass mask before PM comparison"),
    ]
    x = 110
    boxes = []
    for title, body in opts:
        rect = (x, 1390, x + 370, 1585)
        boxes.append(rect)
        card(draw, rect, title, body, "#e0f2f1")
        x += 400
    for a, b in zip(boxes, boxes[1:]):
        arrow(draw, a, b)
    centered(
        draw,
        ["Requirement rule: integer-exact comparison must preserve path id, LLR tree state, partial sums, PM, CRC/RNTI pass mask and selected path."],
        SMALL,
        (bottom[0] + 40, 1620, bottom[2] - 40, 1705),
        "#37474f",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
