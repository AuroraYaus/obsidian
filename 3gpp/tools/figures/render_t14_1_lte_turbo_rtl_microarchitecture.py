#!/usr/bin/env python3
"""Render T14.1 LTE Turbo RTL microarchitecture."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T14.1_LTE_Turbo_RTL_microarchitecture.png"



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
    draw.text(((x0 + x1) / 2, y0 + 35), title, font=HEAD, fill=INK, anchor="mm")
    centered(draw, (x0 + 22, y0 + 78, x1 - 22, y1 - 22), wrap(draw, body, TEXT, x1 - x0 - 44), TEXT, MUTED)


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
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    head_len, head_w = 20, 10
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill=color, width=4)
    px, py = -uy, ux
    draw.polygon(
        [
            (ex, ey),
            (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
            (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def table(draw: ImageDraw.ImageDraw, x0: int, y0: int, headers: list[str], rows: list[list[str]], widths: list[int], row_h: int = 84) -> None:
    total_w = sum(widths)
    total_h = row_h * (len(rows) + 1)
    draw.rounded_rectangle((x0, y0, x0 + total_w, y0 + total_h), radius=8, fill="#ffffff", outline="#607d8b", width=2)
    x = x0
    for header, width in zip(headers, widths):
        draw.rectangle((x, y0, x + width, y0 + row_h), fill="#e3f2fd", outline="#b0bec5", width=1)
        centered(draw, (x + 8, y0 + 5, x + width - 8, y0 + row_h - 5), wrap(draw, header, TABLE_HEAD, width - 16), TABLE_HEAD)
        x += width
    y = y0 + row_h
    for row in rows:
        x = x0
        for value, width in zip(row, widths):
            draw.rectangle((x, y, x + width, y + row_h), fill="#ffffff", outline="#cfd8dc", width=1)
            centered(draw, (x + 8, y + 5, x + width - 8, y + row_h - 5), wrap(draw, value, TABLE, width - 16), TABLE)
            x += width
        y += row_h


def main() -> None:
    width, height = 2400, 2140
    img = Image.new("RGB", (width, height), "#f8fbfa")
    draw = ImageDraw.Draw(img)

    draw.text((width / 2, 58), "T14.1 LTE Turbo RTL Microarchitecture", font=TITLE, fill=INK, anchor="mm")
    subtitle = "SISO datapath, alpha/beta memories, extrinsic RAM, interleaver address generation and CRC-gated iteration control."
    centered(draw, (110, 82, width - 110, 132), wrap(draw, subtitle, SUB, width - 220), SUB, MUTED)

    blocks = [
        (70, 180, 370, 405),
        (470, 180, 770, 405),
        (870, 180, 1170, 405),
        (1270, 180, 1570, 405),
        (1670, 180, 1970, 405),
        (2070, 180, 2330, 405),
    ]
    titles = ["Task Descriptor", "Rate Recovery", "SISO Core A/B", "Extrinsic RAM", "CRC Gate", "Status/Trace"]
    bodies = [
        "K, f1, f2, E, Ncb, RV, max_iter, scale and bitwidth profile.",
        "Read soft buffer, place system/parity LLR and valid/null masks.",
        "Branch metric, alpha, beta, posterior and extrinsic update.",
        "Ping-pong apriori/extrinsic storage with pi/depi address maps.",
        "Hard decision, CB CRC, optional early stop and TB status boundary.",
        "iter_used, sat_count, first_mismatch fields and error code.",
    ]
    fills = ["#e3f2fd", "#fff8e1", "#e8f5e9", "#ede7f6", "#fce4ec", "#e0f2f1"]
    for rect, title, body, fill in zip(blocks, titles, bodies, fills):
        card(draw, rect, title, body, fill)
    for a, b in zip(blocks, blocks[1:]):
        arrow(draw, a, b)

    mem_title = (70, 505, 2330, 575)
    draw.rounded_rectangle(mem_title, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    centered(draw, mem_title, ["Key RTL Memories and Address Generators"], HEAD)
    table(
        draw,
        120,
        625,
        ["Object", "Storage / Logic", "Ports and Timing", "Debug Evidence"],
        [
            ["Alpha/Beta", "8 states x K columns per window", "Two read paths for SISO, normalize per column", "alpha_beta_snapshot, norm_offset"],
            ["Extrinsic", "Two ping-pong banks indexed by pi/depi", "One bank read, one bank write per half-iteration", "extrinsic_trace, addr_hash"],
            ["Interleaver", "f1/f2 polynomial address generator or ROM", "Must align with SISO latency and stall", "pi/depi hash, addr_valid"],
            ["CRC Gate", "CRC checker after hard decision", "May stop after full iteration only", "crc_pass, iter_used, stop_reason"],
        ],
        [360, 640, 630, 550],
        row_h=88,
    )

    fsm_title = (70, 1125, 2330, 1195)
    draw.rounded_rectangle(fsm_title, radius=8, fill="#ffffff", outline="#607d8b", width=2)
    centered(draw, fsm_title, ["Iteration Control FSM"], HEAD)
    fsm = [
        (140, 1240, 390, 1445),
        (485, 1240, 735, 1445),
        (830, 1240, 1080, 1445),
        (1175, 1240, 1425, 1445),
        (1520, 1240, 1770, 1445),
        (1865, 1240, 2115, 1445),
    ]
    fsm_titles = ["IDLE", "LOAD", "SISO A", "SISO B", "CRC CHECK", "DONE/ERROR"]
    fsm_bodies = [
        "Wait start and descriptor_valid.",
        "Fetch LLR, masks and interleaver context.",
        "Decode natural order, write interleaved extrinsic.",
        "Decode interleaved order, write deinterleaved extrinsic.",
        "Hard decision and CB CRC after full iteration.",
        "Commit status or timeout/error flags.",
    ]
    for rect, title, body in zip(fsm, fsm_titles, fsm_bodies):
        card(draw, rect, title, body, "#ffffff")
    for a, b in zip(fsm, fsm[1:]):
        arrow(draw, a, b)
    # Repeat path is routed below the FSM cards so it does not cross node text.
    sx = (fsm[4][0] + fsm[4][2]) // 2
    tx = (fsm[2][0] + fsm[2][2]) // 2
    yb = 1495
    repeat_path = [(sx, fsm[4][3]), (sx, yb), (tx, yb), (tx, fsm[2][3])]
    assert_no_unrelated_crossing("repeat_path", repeat_path, {"SISO B": fsm[3], "DONE/ERROR": fsm[5]})
    draw.line([(sx, fsm[4][3]), (sx, yb), (tx, yb)], fill="#78909c", width=4)
    point_arrow(draw, (tx, yb), (tx, fsm[2][3]), "#78909c")
    draw.text(((sx + tx) / 2, yb + 28), "CRC fail and iter < max_iter", font=TEXT, fill=MUTED, anchor="mm")

    table(
        draw,
        160,
        1605,
        ["Metric", "Teaching Formula", "Interpretation"],
        [
            ["Memory", "alpha/beta + extrinsic + LLR + masks", "Size grows with K, states, quantized width and ping-pong banks."],
            ["Latency", "Niter x two half-iterations x SISO cycles", "CRC early stop changes average latency, not worst-case budget."],
            ["Throughput", "payload bits / block latency", "Pipeline and parallel windows improve throughput but increase SRAM ports."],
        ],
        [360, 720, 960],
        row_h=78,
    )

    foot = (120, 1940, 2280, 2075)
    draw.rounded_rectangle(foot, radius=8, fill="#fffde7", outline="#b0bec5", width=2)
    centered(
        draw,
        foot,
        wrap(
            draw,
            "Protocol evidence fixes K, interleaver parameters, tail bits, rate-recovery inputs and CRC boundaries. RTL choices such as window size, SRAM banking, early-stop policy, clock gating and reset sequencing are implementation strategy and must be verified with bit-exact traces.",
            TEXT,
            2050,
        ),
        TEXT,
        MUTED,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
