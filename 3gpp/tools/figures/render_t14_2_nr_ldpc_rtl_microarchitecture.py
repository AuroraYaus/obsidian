#!/usr/bin/env python3
"""Render T14.2 NR LDPC RTL microarchitecture."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T14.2_NR_LDPC_RTL_microarchitecture.png"



TITLE = font(42, True)
SUB = font(24)
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
    draw.text(((x0 + x1) / 2, y0 + 35), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 22, y0 + 78, x1 - 22, y1 - 22), wrap(draw, body, TEXT, x1 - x0 - 44), TEXT, MUTED)


def center(rect: tuple[int, int, int, int]) -> tuple[float, float]:
    return (rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2


def boundary_point(src: tuple[int, int, int, int], dst: tuple[int, int, int, int]) -> tuple[float, float]:
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


def assert_no_unrelated_crossing(
    name: str,
    points: list[tuple[float, float]],
    forbidden: dict[str, tuple[int, int, int, int]],
) -> None:
    for p0, p1 in zip(points, points[1:]):
        for rect_name, rect in forbidden.items():
            if segment_intersects_rect(p0, p1, rect, margin=3):
                raise AssertionError(f"{name} segment {p0}->{p1} crosses {rect_name} {rect}")


def connect_arrow(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str = LINE) -> None:
    ax, ay = boundary_point(src, dst)
    bx, by = boundary_point(dst, src)
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


def polyline_arrow(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], color: str = LINE) -> None:
    if len(points) < 2:
        return
    for a, b in zip(points[:-2], points[1:-1]):
        draw.line([a, b], fill=color, width=4)
    start = points[-2]
    bx, by = points[-1]
    vx, vy = bx - start[0], by - start[1]
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 20, 10
    end = (bx - ux * head_len, by - uy * head_len)
    draw.line([start, end], fill=color, width=4)
    px, py = -uy, ux
    draw.polygon(
        [
            (bx, by),
            (bx - ux * head_len + px * head_w, by - uy * head_len + py * head_w),
            (bx - ux * head_len - px * head_w, by - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def draw_table(
    draw: ImageDraw.ImageDraw,
    x0: int,
    y0: int,
    headers: list[str],
    rows: list[list[str]],
    widths: list[int],
    row_h: int = 86,
) -> None:
    total_w = sum(widths)
    total_h = row_h * (len(rows) + 1)
    draw.rounded_rectangle((x0, y0, x0 + total_w, y0 + total_h), radius=8, fill="#ffffff", outline="#607d8b", width=2)
    x = x0
    for header, width in zip(headers, widths):
        draw.rectangle((x, y0, x + width, y0 + row_h), fill="#e3f2fd", outline="#b0bec5", width=1)
        centered(draw, (x + 10, y0 + 6, x + width - 10, y0 + row_h - 6), wrap(draw, header, TABLE_HEAD, width - 20), TABLE_HEAD)
        x += width
    y = y0 + row_h
    for row in rows:
        x = x0
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill="#ffffff", outline="#cfd8dc", width=1)
            centered(draw, (x + 10, y + 6, x + width - 10, y + row_h - 6), wrap(draw, value, TABLE, width - 20), TABLE)
            x += width
        y += row_h


def main() -> None:
    width, height = 2500, 2440
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)

    draw.text((width / 2, 58), "T14.2 NR LDPC RTL Microarchitecture", font=TITLE, fill=INK, anchor="mm")
    subtitle = "Layered controller, QC address generation, CN min1/min2 datapath, VN read-modify-write and banked memories."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    blocks = [
        (80, 185, 390, 430),
        (485, 185, 795, 430),
        (890, 185, 1200, 430),
        (1295, 185, 1605, 430),
        (1700, 185, 2010, 430),
        (2105, 185, 2420, 430),
    ]
    titles = ["Protocol Descriptor", "QC Table ROM", "Layered Controller", "CN Unit", "VN RMW", "Stop & Trace"]
    bodies = [
        "BG, Zc, iLS, K, N, E, Ncb, RV, CBG mask and bitwidth profile.",
        "Table 5.3.2 shifts, row groups, column groups and edge schedule hash.",
        "Iteration, layer, local index and valid/stall control.",
        "Sign product, min1, min2, argmin, NMS or OMS scaling.",
        "Read old R, subtract, add new R, update posterior LLR.",
        "Hard bits, syndrome, CB/TB CRC boundary, status and checkpoint stream.",
    ]
    fills = ["#e3f2fd", "#fff8e1", "#e8f5e9", "#ede7f6", "#fce4ec", "#e0f2f1"]
    for rect, title, body, fill in zip(blocks, titles, bodies, fills):
        card(draw, rect, title, body, fill)
    for a, b in zip(blocks, blocks[1:]):
        connect_arrow(draw, a, b)

    # Memory/bank region.
    section = (80, 520, 2420, 590)
    draw.rounded_rectangle(section, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    centered(draw, section, ["Banked Memory and QC Address Path"], HEAD)

    left = (120, 650, 820, 1005)
    mid = (930, 650, 1570, 1005)
    right = (1680, 650, 2380, 1005)
    card(draw, left, "Address Generator", "row_group, col_group, shift and local index produce address = base + ((local + shift) mod Zc).", "#ffffff")
    card(draw, mid, "Bank Arbiter / Crossbar", "Maps parallel column-group accesses to LLR banks and R-message banks; stalls or bypasses on hazards.", "#ffffff")
    card(draw, right, "LLR / Message RAM", "posterior LLR banks, old/new check-message RAM, valid masks and saturation counters.", "#ffffff")
    connect_arrow(draw, left, mid, "#607d8b")
    connect_arrow(draw, mid, right, "#607d8b")
    layered_feedback = [(2030, 1005), (2030, 1065), (520, 1065), (520, 1005)]
    assert_no_unrelated_crossing("layered_feedback", layered_feedback, {"Bank Arbiter / Crossbar": mid})
    polyline_arrow(draw, layered_feedback, "#90a4ae")
    feedback_note = "layered feedback: new posterior is consumed by later layers in the same iteration"
    centered(draw, (610, 1072, 1940, 1122), wrap(draw, feedback_note, TEXT, 1280), TEXT, MUTED)

    draw_table(
        draw,
        135,
        1180,
        ["Path", "RTL Object", "Why It Matters", "Required Debug"],
        [
            ["QC address", "BG/Zc/iLS/shift/local", "Keeps hardware connection equal to TS 38.212 H.", "edge_hash, shift_dir"],
            ["CN datapath", "sign, min1, min2, argmin", "Excludes target edge and avoids echo information.", "cn_trace, tie_count"],
            ["VN RMW", "old_L - old_R + new_R", "Layered decoding replaces message, not accumulates forever.", "old/new R, old/new L"],
            ["Banking", "LLR banks, R banks, arbiter", "Parallel access can stall or need crossbar/bypass.", "bank_conflict_count"],
        ],
        [360, 520, 790, 560],
        row_h=90,
    )

    # FSM and early stop.
    fsm_title = (80, 1695, 2420, 1765)
    draw.rounded_rectangle(fsm_title, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    centered(draw, fsm_title, ["Layered Decoder FSM and Early-Stop Boundary"], HEAD)
    fsm = [
        (150, 1820, 410, 2015),
        (520, 1820, 780, 2015),
        (890, 1820, 1150, 2015),
        (1260, 1820, 1520, 2015),
        (1630, 1820, 1890, 2015),
        (2000, 1820, 2260, 2015),
    ]
    fsm_titles = ["LOAD", "LAYER", "CN UPDATE", "VN WRITEBACK", "CHECK", "DONE/ERROR"]
    fsm_bodies = [
        "Latch descriptor and schedule hash.",
        "Walk row group and local index.",
        "Compute sign, min1, min2 and scaled message.",
        "Update R memory and posterior LLR.",
        "Full-H syndrome, optional CRC gate.",
        "Commit status, trace and failure bundle.",
    ]
    for rect, title, body in zip(fsm, fsm_titles, fsm_bodies):
        card(draw, rect, title, body, "#ffffff")
    for a, b in zip(fsm, fsm[1:]):
        connect_arrow(draw, a, b)
    retry_loop = [(1760, 2015), (1760, 2085), (650, 2085), (650, 2015)]
    assert_no_unrelated_crossing(
        "retry_loop",
        retry_loop,
        {"CN UPDATE": fsm[2], "VN WRITEBACK": fsm[3], "DONE/ERROR": fsm[5]},
    )
    polyline_arrow(draw, retry_loop, "#78909c")
    draw.text((1205, 2115), "syndrome fail and iter < max_iter", font=TEXT, fill=MUTED, anchor="mm")

    foot = (130, 2240, 2370, 2370)
    draw.rounded_rectangle(foot, radius=8, fill="#fffde7", outline="#b0bec5", width=2)
    centered(
        draw,
        foot,
        wrap(
            draw,
            "Protocol evidence fixes the QC-LDPC matrix identity: BG, Zc, lifting set and shift tables. RTL choices such as layered order, CN lane count, memory banking, stall policy, NMS/OMS constants and early-stop timing are implementation strategy and must be closed by bit-exact checkpoint traces.",
            TEXT,
            2130,
        ),
        TEXT,
        MUTED,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
