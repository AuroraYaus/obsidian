#!/usr/bin/env python3
"""Render the LTE/NR decoder protocol reading map."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L1/assets/T0.1_LTE_NR_decoder_protocol_reading_map.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#152033",
    "muted": "#5C6978",
    "line": "#AAB7C8",
    "lte": "#B65B2E",
    "lte_l": "#FFF0E6",
    "nr": "#236B5A",
    "nr_l": "#E8F6EF",
    "proto": "#2457A6",
    "proto_l": "#EAF1FB",
    "evidence": "#6E55A4",
    "evidence_l": "#F1EDFF",
    "warn": "#B9841A",
    "warn_l": "#FFF6DD",
    "panel": "#F6F8FB",
}



def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    cur = ""
    for ch in text:
        if ch == "\n":
            if cur:
                tokens.append(cur)
                cur = ""
            tokens.append("\n")
        elif ch.isascii() and (ch.isalnum() or ch in "/_-+.[]=():"):
            cur += ch
        else:
            if cur:
                tokens.append(cur)
                cur = ""
            tokens.append(" " if ch.isspace() else ch)
    if cur:
        tokens.append(cur)
    return tokens


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    cur = ""
    for tok in tokenize(text):
        if tok == "\n":
            if cur.strip():
                lines.append(cur.strip())
            cur = ""
            continue
        nxt = cur + tok
        if draw.textlength(nxt, font=fnt) <= width or not cur.strip():
            cur = nxt
        else:
            lines.append(cur.strip())
            cur = tok
    if cur.strip():
        lines.append(cur.strip())
    return lines


def text_height(draw: ImageDraw.ImageDraw, lines: list[str], fnt: ImageFont.FreeTypeFont, gap: int) -> int:
    total = 0
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=fnt)
        total += bbox[3] - bbox[1]
        if i + 1 < len(lines):
            total += gap
    return total


def assert_inside(inner: tuple[int, int, int, int], bbox: tuple[int, int, int, int], label: str) -> None:
    if bbox[0] < inner[0] or bbox[1] < inner[1] or bbox[2] > inner[2] or bbox[3] > inner[3]:
        raise AssertionError(f"{label} text bbox {bbox} exceeds padded box {inner}")


def draw_centered(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str | list[str],
    size: int,
    color: str = COL["ink"],
    bold: bool = False,
    gap: int = 7,
    pad: int = 24,
) -> None:
    fnt = font(size, bold)
    inner = (box[0] + pad, box[1] + pad, box[2] - pad, box[3] - pad)
    if inner[2] <= inner[0] or inner[3] <= inner[1]:
        raise AssertionError(f"text box too small after padding: {box}, pad={pad}")
    raw = text if isinstance(text, list) else [text]
    lines: list[str] = []
    for item in raw:
        lines.extend(wrap(draw, item, fnt, max(inner[2] - inner[0], 90)))
    total = text_height(draw, lines, fnt, gap)
    if total > inner[3] - inner[1]:
        raise AssertionError(f"text height {total} exceeds padded box height {inner[3] - inner[1]} for {text!r}")
    x = (inner[0] + inner[2]) / 2
    y = inner[1] + ((inner[3] - inner[1]) - total) / 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=fnt)
        line_w = bbox[2] - bbox[0]
        if line_w > inner[2] - inner[0]:
            raise AssertionError(f"text width {line_w} exceeds padded box width {inner[2] - inner[0]} for {line!r}")
        h = bbox[3] - bbox[1]
        text_x = x - line_w / 2 - bbox[0]
        text_y = y - bbox[1]
        actual_bbox = draw.textbbox((text_x, text_y), line, font=fnt)
        assert_inside(inner, actual_bbox, line)
        draw.text((text_x, text_y), line, font=fnt, fill=color)
        y += h + gap


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str, radius: int = 16, width: int = 2) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def node(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    fill: str,
    outline: str,
) -> tuple[int, int, int, int]:
    rounded(draw, box, fill, outline, 16, 2)
    draw_centered(draw, (box[0] + 18, box[1] + 18, box[2] - 18, box[1] + 70), title, 25, outline, True, 5, 8)
    draw_centered(draw, (box[0] + 20, box[1] + 82, box[2] - 20, box[3] - 20), body, 24, COL["ink"], False, 7, 10)
    return box


def center(box: tuple[int, int, int, int]) -> tuple[float, float]:
    return ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2)


def boundary_point(box: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    cx, cy = center(box)
    dx, dy = toward[0] - cx, toward[1] - cy
    if abs(dx) < 1e-6 and abs(dy) < 1e-6:
        return cx, cy
    half_w = max((box[2] - box[0]) / 2, 1)
    half_h = max((box[3] - box[1]) / 2, 1)
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return cx + dx / scale, cy + dy / scale


def arrow(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str) -> None:
    x0, y0 = boundary_point(src, center(dst))
    x1, y1 = boundary_point(dst, center(src))
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    head_len, head_w = 20, 11
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    draw.line(((x0, y0), line_end), fill=color, width=4)
    angle = math.atan2(y1 - y0, x1 - x0)
    bx = x1 - head_len * math.cos(angle)
    by = y1 - head_len * math.sin(angle)
    px = head_w * math.sin(angle)
    py = -head_w * math.cos(angle)
    draw.polygon([(x1, y1), (bx + px, by + py), (bx - px, by - py)], fill=color)


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


def elbow_arrow(draw: ImageDraw.ImageDraw, points: list[tuple[float, float]], color: str) -> None:
    if len(points) < 2:
        return
    x0, y0 = points[-2]
    x1, y1 = points[-1]
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    head_len, head_w = 20, 11
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    shaft = points[:-1] + [line_end]
    for start, end in zip(shaft, shaft[1:]):
        draw.line((start, end), fill=color, width=4)
    bx, by = line_end
    px, py = -uy * head_w, ux * head_w
    draw.polygon([(x1, y1), (bx + px, by + py), (bx - px, by - py)], fill=color)


def draw_table(draw: ImageDraw.ImageDraw, x: int, y: int) -> int:
    draw.text((x, y), "读协议时先问的问题", font=font(34, True), fill=COL["ink"])
    y += 58
    cols = [235, 455, 390, 420, 420]
    rows = [
        ["问题", "先查哪里", "接收端对象", "主讲章节", "常见误区"],
        ["CRC 失败", "TS 36.212/38.212 §5.1", "TB/CB/control CRC checker", "T3.1, T7.4, T9.5, T10.6", "把 CRC 当纠错器，或忽略 DCI RNTI 边界"],
        ["TB/CB/filler", "TS 36.212 §5.1.2; TS 38.212 §5.2", "segmentation descriptor", "T3.2-T3.5", "把 filler 当 payload 或把 CB 顺序弄反"],
        ["译码器选择", "TS 36.212/38.212 channel coding tables", "decoder_type", "T6.1, T8.1, T10.1, T11.5", "用 NR LDPC 解释控制信息，或用 Polar 解释 LTE"],
        ["Rate matching/HARQ", "TS 36.212 §5.1.4; TS 38.212 §5.4; TS 38.214 HARQ/CBG", "RV, Ncb, E, k0, soft buffer", "T7.1-T7.3, T9.1-T9.4, T11.2", "只看 RV 标签，不看 circular buffer 地址"],
        ["MCS/TBS", "TS 38.214 §5.1.3/§6.1.4", "Qm, R, TBS, CB pressure", "T9.0, T14.6, T15.2", "把调度元数据写成译码核内部算法"],
        ["证据归档", "processed content/tables/equations/media", "evidence manifest", "T12-T15", "把模板或候选清单写成真实通过"],
    ]
    row_h = [70, 118, 118, 118, 136, 118, 118]
    for r, row in enumerate(rows):
        x0 = x
        fill = COL["panel"] if r == 0 else "#FFFFFF"
        for c, cell in enumerate(row):
            box = (x0, y, x0 + cols[c], y + row_h[r])
            draw.rectangle(box, fill=fill, outline=COL["line"], width=2)
            draw_centered(draw, box, cell, 24, COL["ink"], r == 0, 5, 14)
            x0 += cols[c]
        y += row_h[r]
    return y


def edge_check(img: Image.Image) -> dict[str, int]:
    pix = img.load()
    w, h = img.size

    def nonwhite(points: list[tuple[int, int]]) -> int:
        return sum(1 for x, y in points if pix[x, y] != (255, 255, 255))

    return {
        "top": nonwhite([(x, 0) for x in range(w)]),
        "bottom": nonwhite([(x, h - 1) for x in range(w)]),
        "left": nonwhite([(0, y) for y in range(h)]),
        "right": nonwhite([(w - 1, y) for y in range(h)]),
    }


def main() -> None:
    img = Image.new("RGB", (2200, 2300), COL["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((80, 58), "T0.1 LTE/NR 译码协议阅读地图", font=font(46, True), fill=COL["ink"])
    draw.text((82, 118), "从 3GPP 协议源到接收端对象、译码器家族和证据归档的导航图。", font=font(25), fill=COL["muted"])

    src = node(draw, (80, 210, 470, 480), "协议源", "TS 36/38.211 调制映射\nTS 36/38.212 信道编码\nTS 36/38.213/214 调度\nTS 36/38.321/331 上下文", COL["proto_l"], COL["proto"])
    rx = node(
        draw,
        (520, 210, 910, 480),
        "接收端对象",
        "LLR、CRC、TB/CB、filler、RV、soft buffer、descriptor\n和 evidence",
        "#FFFFFF",
        COL["line"],
    )
    lte = node(draw, (980, 95, 1370, 365), "LTE 主线", "Turbo 数据译码\nTS 36.212 §5.1.3.2\nrate recovery 与 HARQ", COL["lte_l"], COL["lte"])
    nr_ldpc = node(draw, (980, 415, 1370, 685), "NR 数据主线", "LDPC 数据译码\nTS 38.212 §5.3.2\nBG/Zc/rate recovery", COL["nr_l"], COL["nr"])
    nr_polar = node(draw, (1440, 250, 1830, 520), "NR 控制主线", "Polar 控制译码\nTS 38.212 §5.3.1\nSC/SCL/CRC aided", COL["proto_l"], COL["proto"])
    evidence = node(draw, (520, 625, 910, 925), "证据闭环", "本地 content.md\nsections.jsonl\ntables/html/csv\nequations/media\naudit logs", COL["evidence_l"], COL["evidence"])
    rtl = node(draw, (980, 750, 1370, 1020), "工程落点", "浮点模型、定点模型、RTL/ASIC、testbench、coverage、sign-off 模板", COL["warn_l"], COL["warn"])
    for a, b, color in [
        (src, rx, COL["proto"]),
        (rx, lte, COL["lte"]),
        (rx, nr_ldpc, COL["nr"]),
        (rx, nr_polar, COL["proto"]),
        (src, evidence, COL["evidence"]),
        (evidence, rtl, COL["warn"]),
        (nr_ldpc, rtl, COL["nr"]),
        (nr_polar, rtl, COL["proto"]),
    ]:
        arrow(draw, a, b, color)
    # Avoidance path: direct LTE->engineering would pass through the NR data box.
    lte_to_engineering = [
        boundary_point(lte, (1410, 210)),
        (1410, 710),
        boundary_point(rtl, (1410, 885)),
    ]
    assert_no_unrelated_crossing(
        "lte_to_engineering_avoidance",
        lte_to_engineering,
        {
            "receiver": rx,
            "nr_ldpc": nr_ldpc,
            "nr_polar": nr_polar,
            "evidence": evidence,
        },
    )
    elbow_arrow(draw, lte_to_engineering, COL["lte"])

    y = draw_table(draw, 90, 1120)
    note_box = (90, y + 80, 2110, y + 210)
    rounded(draw, note_box, "#FFFFFF", COL["line"], 16, 2)
    draw_centered(
        draw,
        note_box,
        "读图顺序：先定位协议源，再把发送端规则翻译成接收端对象，最后选择 LTE Turbo、NR LDPC 或 NR Polar 主线。工程检测点：每个结论都要能回到本地协议证据或明确标为模板/待生成。",
        25,
        COL["ink"],
        False,
        7,
        28,
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")
    print(f"IMAGE_EDGE_CHECK {img.size} {edge_check(img)}")


if __name__ == "__main__":
    main()
