#!/usr/bin/env python3
"""Render T14.3 NR Polar RTL microarchitecture."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T14.3_NR_Polar_RTL_microarchitecture.png"



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


def centered(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], lines: list[str], fnt, fill=INK, gap: int = 7) -> None:
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
    title_font = HEAD if text_size(draw, title, HEAD)[0] <= (x1 - x0 - 52) else font(24, True)
    draw.text(((x0 + x1) / 2, y0 + 35), title, font=title_font, fill=INK, anchor="mm")
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


def table(draw: ImageDraw.ImageDraw, x0: int, y0: int, headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 88) -> None:
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
    width, height = 2500, 2500
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)

    draw.text((width / 2, 58), "T14.3 NR Polar RTL Microarchitecture", font=TITLE, fill=INK, anchor="mm")
    subtitle = "CA-SCL tree traversal, f/g engine, path memories, PM sorter, CRC/RNTI selector and low-latency control."
    centered(draw, (110, 82, width - 110, 134), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    blocks = [
        (70, 185, 385, 430),
        (455, 185, 785, 430),
        (855, 185, 1170, 430),
        (1240, 185, 1555, 430),
        (1625, 185, 1940, 430),
        (2010, 185, 2430, 430),
    ]
    titles = ["Protocol Descriptor", "Mask / Rate Recovery", "Tree Controller", "f/g Engine", "Path Manager", "CRC Final Selector"]
    bodies = [
        "A, K, E, N, crc_type, UCI/DCI context, RNTI context and list-size config.",
        "Deinterleaved LLR, info/frozen/PC masks, valid bits and rate-recovery mode.",
        "SC/SCL node order, frozen/information decisions and low-latency schedule.",
        "LLR f and g functions, saturation, partial-sum input and path-local state.",
        "Path split, PM update, 2L candidates, sorter, prune and lazy-copy remap.",
        "Parallel CRC/RNTI checks and final path selection among surviving candidates.",
    ]
    fills = ["#e3f2fd", "#fff8e1", "#e8f5e9", "#ede7f6", "#fce4ec", "#e0f2f1"]
    for rect, title, body, fill in zip(blocks, titles, bodies, fills):
        card(draw, rect, title, body, fill)
    for a, b in zip(blocks, blocks[1:]):
        connect_arrow(draw, a, b)

    mem_title = (80, 520, 2420, 590)
    draw.rounded_rectangle(mem_title, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    centered(draw, mem_title, ["Path-State Memories and Sorter Bottleneck"], HEAD)

    left = (120, 655, 610, 1015)
    mid1 = (720, 655, 1210, 1015)
    mid2 = (1320, 655, 1810, 1015)
    right = (1920, 655, 2380, 1015)
    card(draw, left, "LLR Memory", "Stores node LLRs per stage and path. Lazy-copy uses state ids instead of full copy.", "#ffffff")
    card(draw, mid1, "Partial Sum Memory", "Stores decided bits used by g function and tree backtracking per path.", "#ffffff")
    card(draw, mid2, "PM / Path State", "Path bits, PM, CRC state, valid flags, parent id and remap table.", "#ffffff")
    card(draw, right, "2L -> L Sorter", "Critical bottleneck: compare candidate PM, tie-break, prune and copy state.", "#fff3e0")
    connect_arrow(draw, left, mid1, "#607d8b")
    connect_arrow(draw, mid1, mid2, "#607d8b")
    connect_arrow(draw, mid2, right, "#607d8b")
    remap_feedback = [(2150, 1015), (2150, 1075), (365, 1075), (365, 1015)]
    assert_no_unrelated_crossing("remap_feedback", remap_feedback, {"Partial Sum Memory": mid1, "PM / Path State": mid2})
    polyline_arrow(draw, remap_feedback, "#90a4ae")
    remap_note = "prune remap feeds next f/g traversal: bits, PM, LLR state, partial sum and CRC state must move together"
    centered(draw, (520, 1080, 2000, 1130), wrap(draw, remap_note, TEXT, 1440), TEXT, MUTED)

    table(
        draw,
        135,
        1190,
        ["Structure", "RTL Object", "Bottleneck / Risk", "Required Debug"],
        [
            ["Tree traversal", "node_state, stage, path_id", "Wrong node order changes f/g input.", "node_trace, stage_id"],
            ["Path split", "frozen/info mask, 0/1 candidates", "Frozen bit split or info bit forced.", "split_count, mask_hash"],
            ["PM sorter", "candidate_pm[2L], sort_order", "Comparator direction or tie-break unstable.", "pm_trace, prune_order"],
            ["State copy", "lazy-copy refs, remap table", "PM moves but LLR/partial/CRC state lags.", "parent_id, state_id"],
        ],
        [370, 560, 780, 560],
        row_h=92,
    )

    fsm_title = (80, 1685, 2420, 1755)
    draw.rounded_rectangle(fsm_title, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    centered(draw, fsm_title, ["CA-SCL Low-Latency Control FSM"], HEAD)
    fsm = [
        (135, 1815, 405, 2015),
        (500, 1815, 770, 2015),
        (865, 1815, 1135, 2015),
        (1230, 1815, 1500, 2015),
        (1595, 1815, 1865, 2015),
        (1960, 1815, 2230, 2015),
    ]
    fsm_titles = ["LOAD", "TRAVERSE", "SPLIT", "SORT / PRUNE", "CRC CHECK", "DONE/ERROR"]
    fsm_bodies = [
        "Latch descriptor, masks and rate-recovered LLR.",
        "Run f/g nodes and update partial sums.",
        "Frozen keeps one; information creates 0/1 candidates.",
        "Select best L paths and remap all state ids.",
        "Parallel CRC and optional RNTI final selector.",
        "Commit selected path, status and failure bundle.",
    ]
    for rect, title, body in zip(fsm, fsm_titles, fsm_bodies):
        card(draw, rect, title, body, "#ffffff")
    for a, b in zip(fsm, fsm[1:]):
        connect_arrow(draw, a, b)
    next_bit_loop = [(1365, 2015), (1365, 2090), (635, 2090), (635, 2015)]
    assert_no_unrelated_crossing(
        "next_bit_loop",
        next_bit_loop,
        {"BRANCH": fsm[2], "CRC SELECT": fsm[4]},
    )
    polyline_arrow(draw, next_bit_loop, "#78909c")
    draw.text((1000, 2120), "next bit while paths remain active", font=TEXT, fill=MUTED, anchor="mm")

    foot = (130, 2290, 2370, 2425)
    draw.rounded_rectangle(foot, radius=8, fill="#fffde7", outline="#b0bec5", width=2)
    centered(
        draw,
        foot,
        wrap(
            draw,
            "Protocol evidence fixes Polar construction inputs: reliability sequence, information/frozen/PC sets, CRC/RNTI context and rate recovery. RTL choices such as list size implementation, lazy copy, sorter topology, PM normalization and pipeline cuts are implementation strategy and must be closed by bit-exact path traces.",
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
