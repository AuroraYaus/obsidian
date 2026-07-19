#!/usr/bin/env python3
"""Render T13.3 NR LDPC fixed-point model flow."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T13.3_NR_LDPC_fixed_point_model.png"



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
    draw.text(((x0 + x1) / 2, y0 + 32), title, font=HEAD, fill="#102027", anchor="mm")
    centered(draw, wrap(draw, body, TINY, x1 - x0 - 44), TINY, (x0 + 22, y0 + 72, x1 - 22, y1 - 22))


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
    draw.text(((x0 + x1) / 2, y0 + 36), "LDPC Fixed-Point Checkpoints", font=HEAD, fill="#102027", anchor="mm")
    cols = [x0 + 35, x0 + 285, x0 + 650, x0 + 1015, x1 - 35]
    rows = [y0 + 82, y0 + 145, y0 + 235, y0 + 325, y0 + 415, y0 + 505, y0 + 595]
    headers = ["Stage", "Integer Object", "Compare Field", "Failure Signal"]
    data = [
        ["Rate recovery", "LLR, masks, soft buffer", "quantized_llr, observed_mask", "RV or filler mismatch"],
        ["CN update", "sign, min1, min2, NMS/OMS", "cn_trace", "wrong sign or min2"],
        ["Layered RMW", "old_R, q, new_R, L", "layer_trace", "old/new message mix"],
        ["VN/posterior", "posterior LLR and hard bits", "posterior_snapshot", "saturation or sign error"],
        ["Syndrome/CRC", "syndrome, CB/TB CRC", "stop_status, iter_used", "false early stop"],
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
    W, H = 2200, 1800
    img = Image.new("RGB", (W, H), "#f8fbfa")
    draw = ImageDraw.Draw(img)
    draw.text((W / 2, 56), "T13.3 NR LDPC Fixed-Point Model Plan", font=TITLE, fill="#102027", anchor="mm")
    subtitle = "LLR and message bitwidth, min1/min2, NMS/OMS, layered update and bit-exact evidence"
    centered(draw, wrap(draw, subtitle, TEXT, W - 220), TEXT, (110, 78, W - 110, 124), "#455a64")

    top = [
        (75, 160, 420, 410),
        (500, 160, 845, 410),
        (925, 160, 1270, 410),
        (1350, 160, 1695, 410),
        (1775, 160, 2120, 410),
    ]
    titles = ["Protocol Vector", "LLR Quantizer", "CN Unit", "Layered Memory", "Syndrome/Report"]
    bodies = [
        "BG, Zc, lifting set, RV, k0, E, Ncb, CBG masks and TS 38.212 evidence.",
        "Apply width, Q format, sign convention, clipping and soft-combine saturation.",
        "Compute sign product, min1/min2, MS/NMS/OMS correction and output saturation.",
        "Read old_R, form q=L-old_R, write new_R and updated posterior LLR per layer.",
        "Check syndrome, CB/TB CRC, stop reason, BLER loss and replay bundle.",
    ]
    fills = ["#e3f2fd", "#fff8e1", "#e8f5e9", "#ede7f6", "#fce4ec"]
    for rect, title, body, fill in zip(top, titles, bodies, fills):
        card(draw, rect, title, body, fill)
    for a, b in zip(top, top[1:]):
        arrow(draw, a, b)

    table(draw, (75, 505, 2120, 1110))

    bottom = (75, 1225, 2120, 1685)
    draw.rounded_rectangle(bottom, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    draw.text((W / 2, 1263), "Bitwidth and Algorithm Options", font=HEAD, fill="#102027", anchor="mm")
    opts = [
        ("MS", "sign product plus min1/min2; cheapest baseline"),
        ("NMS", "multiply MS magnitude by alpha_q with fixed rounding"),
        ("OMS", "subtract beta_q and clamp negative magnitude to zero"),
        ("Layered", "subtract old_R and add new_R before next layer"),
        ("Saturation", "count LLR, CN, VN and posterior clamp events"),
    ]
    x = 125
    boxes = []
    for title, body in opts:
        rect = (x, 1332, x + 350, 1545)
        boxes.append(rect)
        card(draw, rect, title, body, "#f3e5f5")
        x += 390
    for a, b in zip(boxes, boxes[1:]):
        arrow(draw, a, b)
    centered(
        draw,
        ["Requirement rule: compare CN min1/min2, layered read-modify-write, posterior LLR and syndrome before judging fixed-point LDPC BLER loss."],
        SMALL,
        (bottom[0] + 40, 1580, bottom[2] - 40, 1660),
        "#37474f",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
