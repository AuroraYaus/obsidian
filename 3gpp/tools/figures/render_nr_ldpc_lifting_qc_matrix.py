#!/usr/bin/env python3
"""Render NR LDPC lifting and QC matrix teaching figures."""

from __future__ import annotations

import csv
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
TABLE_DIR = ROOT / "3GPP_Rel19/processed/TS_38.212_38212-j30/tables"
ASSET_DIR = ROOT / "docs/L2/assets"

PALETTE = {
    "ink": "#17212F",
    "muted": "#5B6877",
    "line": "#C9D4DF",
    "bg": "#FFFFFF",
    "panel": "#F7F9FC",
    "head": "#DDE8F5",
    "blue": "#2457A6",
    "green": "#2D8F5D",
    "amber": "#C69220",
    "red": "#C64B59",
    "purple": "#7457A6",
    "zero": "#F4F7FA",
    "cell": "#FFFFFF",
}



def center_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill: str, width: int) -> int:
    x, y = xy
    lines = fit_wrap_text(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + 7
    return y


def read_csv(name: str) -> list[list[str]]:
    path = TABLE_DIR / f"{name}.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.reader(handle))


def render_shift_table(table_name: str, title: str, out_name: str) -> None:
    rows = read_csv(table_name)
    data = rows[1:]
    row_h = 56  # TEXT_FIT_OK: shift-table cells contain short numeric labels centered at 24px.
    col_w = [88, 106] + [72] * 8 + [88, 106] + [72] * 8
    width = 80 + sum(col_w) + 80
    height = 190 + row_h * len(data) + 70
    img = Image.new("RGB", (width, height), PALETTE["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((60, 36), title, font=font(34, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (60, 88),
        "协议原表为横向双栏排版。每个半栏包含 row index、column index 和 set index 0-7 下的 shift value。空白 row index 表示延续上一行的 row group；数值 0 是有效零移位，不是空项。",
        font(24),
        PALETTE["muted"],
        width - 120,
    )

    x0, y0 = 60, 160
    headers = ["Row", "Col", "iLS=0", "1", "2", "3", "4", "5", "6", "7"] * 2
    for c, text in enumerate(headers):
        x = x0 + sum(col_w[:c])
        box = (x, y0, x + col_w[c], y0 + row_h)
        draw.rectangle(box, fill=PALETTE["head"], outline=PALETTE["line"])
        center_text(draw, box, text, font(24, True), PALETTE["ink"])

    y = y0 + row_h
    for ridx, row in enumerate(data[1:], start=1):
        if len(row) < 20:
            row = row + [""] * (20 - len(row))
        for c in range(20):
            x = x0 + sum(col_w[:c])
            text = row[c].strip()
            fill = "#FFFFFF" if ridx % 2 else "#F6F9FD"
            if c in {0, 1, 10, 11}:
                fill = "#EEF4FB" if text else "#F8FAFD"
            elif text == "0":
                fill = PALETTE["zero"]
            box = (x, y, x + col_w[c], y + row_h)
            draw.rectangle(box, fill=fill, outline=PALETTE["line"])
            center_text(draw, box, text, font(24, c in {0, 10}), PALETTE["ink"])
        y += row_h

    draw.text(
        (60, height - 52),
        f"Local evidence: TS 38.212 38212-j30 tables/{table_name}.csv and .html; rendered by tools/figures/render_nr_ldpc_lifting_qc_matrix.py",
        font=font(24),
        fill=PALETTE["muted"],
    )
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    out = ASSET_DIR / out_name
    img.save(out)
    print(f"WROTE {out}")


def circulant_identity(z: int, shift: int) -> list[list[int]]:
    return [[1 if j == (i + shift) % z else 0 for j in range(z)] for i in range(z)]


def render_toy_expansion() -> None:
    z = 4
    base = [[0, -1, 2], [1, 0, -1]]
    block = 34
    gap = 10
    left_x, top_y = 80, 240
    h_rows, h_cols = len(base) * z, len(base[0]) * z
    matrix_w, matrix_h = h_cols * block, h_rows * block
    width, height = 1640, 800
    img = Image.new("RGB", (width, height), PALETTE["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "QC-LDPC 玩具基矩阵展开示例", font=font(38, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (70, 100),
        "基矩阵元素 -1 表示零矩阵；非负数 p 表示把 Zc x Zc 单位矩阵向右循环移位 p 次。这里取 Zc=4，把 2x3 基矩阵展开为 8x12 的完整奇偶校验矩阵 H。",
        font(24),
        PALETTE["muted"],
        width - 140,
    )

    draw.text((80, 185), "基矩阵 B", font=font(25, True), fill=PALETTE["blue"])
    bx, by = 80, 225
    for r in range(2):
        for c in range(3):
            box = (bx + c * 72, by + r * 52, bx + (c + 1) * 72, by + (r + 1) * 52)
            fill = "#FFF4DE" if base[r][c] >= 0 else "#F0F3F7"
            draw.rectangle(box, fill=fill, outline=PALETTE["line"], width=2)
            center_text(draw, box, str(base[r][c]), font(24, True), PALETTE["ink"])

    draw.text((380, 185), "展开后的 H", font=font(25, True), fill=PALETTE["green"])
    hx, hy = 380, 225
    for br, row in enumerate(base):
        for bc, p in enumerate(row):
            sub = [[0] * z for _ in range(z)] if p < 0 else circulant_identity(z, p)
            for i in range(z):
                for j in range(z):
                    rr, cc = br * z + i, bc * z + j
                    box = (hx + cc * block, hy + rr * block, hx + (cc + 1) * block, hy + (rr + 1) * block)
                    fill = "#2D8F5D" if sub[i][j] else "#F7FAFC"
                    draw.rectangle(box, fill=fill, outline="#D4DEE8")
                    if sub[i][j]:
                        center_text(draw, box, "1", font(24, True), "#FFFFFF")
            outline = (hx + bc * z * block, hy + br * z * block, hx + (bc + 1) * z * block, hy + (br + 1) * z * block)
            draw.rectangle(outline, outline=PALETTE["amber"] if p >= 0 else PALETTE["red"], width=3)
            label = "zero" if p < 0 else f"P^{p}"
            label_font = font(24, True)
            bbox = draw.textbbox((0, 0), label, font=label_font)
            pill = (
                outline[0] + 6,
                outline[1] + 5,
                outline[0] + 18 + (bbox[2] - bbox[0]),
                outline[1] + 13 + (bbox[3] - bbox[1]),
            )
            draw.rounded_rectangle(pill, radius=5, fill="#FFFFFF")
            draw.text((pill[0] + 6, pill[1] + 3), label, font=label_font, fill=PALETTE["red"] if p < 0 else PALETTE["amber"])

    panel = (1010, 225, 1565, 720)
    draw.rounded_rectangle(panel, radius=18, fill=PALETTE["panel"], outline=PALETTE["line"], width=2)
    draw.text((1040, 255), "读图要点", font=font(26, True), fill=PALETTE["ink"])
    notes = [
        "-1 不是 shift=-1，而是整个 Zc x Zc 子块全为 0。",
        "0 是有效 shift value，表示不移位的单位矩阵。",
        "p=2 表示每一行的 1 向右循环移动 2 格。",
        "真实 NR 不保存完整 H，而保存 BG 表、iLS、Zc 和移位值。",
        "地址生成器只需做模 Zc 加法，即可找到循环移位后的列地址。",
    ]
    y = 310
    for note in notes:
        y = draw_wrapped(draw, (1040, y), note, font(24), PALETTE["muted"], 480) + 10

    out = ASSET_DIR / "T8.3_NR_LDPC_toy_QC_expansion.png"
    img.save(out)
    print(f"WROTE {out}")


def draw_arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str) -> None:
    sx, sy = start
    ex, ey = end
    length = math.hypot(ex - sx, ey - sy)
    if length == 0:
        return
    ux, uy = (ex - sx) / length, (ey - sy) / length
    px, py = -uy, ux
    head_len, head_w = 18, 10
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line((sx, sy, *line_end), fill=color, width=4)
    head = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(head, fill=color)


def label_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    fill: str,
    accent: str,
) -> None:
    draw.rounded_rectangle(box, radius=10, fill=fill, outline=accent, width=3)
    draw.text((box[0] + 18, box[1] + 14), title, font=font(25, True), fill=PALETTE["ink"])
    draw_wrapped(draw, (box[0] + 18, box[1] + 54), body, font(24), PALETTE["muted"], box[2] - box[0] - 36)


def render_bg_regions_qc_receiver() -> None:
    width, height = 2200, 1080
    img = Image.new("RGB", (width, height), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "NR LDPC BG 子矩阵区域、QC lifting 与接收端用途", font=font(42, True), fill=PALETTE["ink"])
    draw_wrapped(
        draw,
        (70, 104),
        "A/B/C/D/E 是工程教学分区，用来理解核心 parity、扩展 parity、近似双对角结构和 Raptor-like 扩展。协议依据仍是 TS 38.212 Table 5.3.2-2/3 的 row、column、iLS 和 shift values。",
        font(24),
        PALETTE["muted"],
        width - 140,
    )

    # Left panel: base graph regions.
    panel = (70, 205, 900, 990)
    draw.rounded_rectangle(panel, radius=18, fill=PALETTE["panel"], outline=PALETTE["line"], width=2)
    draw.text((105, 238), "1. BG 五区结构", font=font(30, True), fill=PALETTE["blue"])
    gx, gy = 132, 334
    cell_w, cell_h = 66, 54
    rows, cols = 8, 10
    regions = {}
    for r in range(rows):
        for c in range(cols):
            if r < 4 and c < 4:
                regions[(r, c)] = ("A", "#DDEBFF")
            elif r < 4 and 4 <= c < 6:
                regions[(r, c)] = ("B", "#E5F4EA")
            elif r >= 4 and c < 4:
                regions[(r, c)] = ("C", "#FFF2D9")
            elif r >= 4 and 4 <= c < 6:
                regions[(r, c)] = ("D", "#F2E9FF")
            else:
                regions[(r, c)] = ("E", "#FBE4E7")
    for r in range(rows):
        for c in range(cols):
            label, fill = regions[(r, c)]
            x0 = gx + c * cell_w
            y0 = gy + r * cell_h
            draw.rectangle((x0, y0, x0 + cell_w, y0 + cell_h), fill=fill, outline="#FFFFFF", width=2)
            # Sparse non-zero markers, not a real BG table.
            if (r * 3 + c * 5) % 7 in {0, 1, 4}:
                draw.ellipse((x0 + 34, y0 + 22, x0 + 52, y0 + 40), fill=PALETTE["ink"])
    region_boxes = {
        "A": (gx, gy, gx + 4 * cell_w, gy + 4 * cell_h),
        "B": (gx + 4 * cell_w, gy, gx + 6 * cell_w, gy + 4 * cell_h),
        "C": (gx, gy + 4 * cell_h, gx + 4 * cell_w, gy + rows * cell_h),
        "D": (gx + 4 * cell_w, gy + 4 * cell_h, gx + 6 * cell_w, gy + rows * cell_h),
        "E": (gx + 6 * cell_w, gy, gx + cols * cell_w, gy + rows * cell_h),
    }
    for label, box in region_boxes.items():
        draw.rectangle(box, outline=PALETTE["ink"], width=3)
        center_text(draw, box, label, font(42, True), PALETTE["ink"])
    draw.text((gx, gy - 36), "systematic columns", font=font(24, True), fill=PALETTE["muted"])
    draw.text((gx + 4 * cell_w, gy - 36), "core parity", font=font(24, True), fill=PALETTE["muted"])
    draw.text((gx + 6 * cell_w, gy - 36), "extension parity", font=font(24, True), fill=PALETTE["muted"])
    draw.text((105, 804), "rows: upper=core, lower=extension", font=font(24, True), fill=PALETTE["muted"])
    draw_wrapped(
        draw,
        (105, 850),
        "B/E 区的双对角或近似双对角形状降低编码求解复杂度；C/D/E 让更多 parity 逐步加入，形成 Raptor-like 扩展。",
        font(24),
        PALETTE["muted"],
        700,
    )

    # Middle panel: QC lifting.
    panel2 = (960, 205, 1505, 990)
    draw.rounded_rectangle(panel2, radius=18, fill="#FFFDF6", outline="#E2CD7A", width=2)
    draw.text((995, 238), "2. QC lifting", font=font(30, True), fill=PALETTE["amber"])
    label_box(
        draw,
        (1010, 315, 1455, 450),
        "BG edge",
        "row i, column j, iLS selects shift value V_ij",
        "#FFFFFF",
        PALETTE["amber"],
    )
    draw_arrow(draw, (1230, 460), (1230, 535), PALETTE["amber"])
    label_box(
        draw,
        (1010, 545, 1455, 690),
        "P_ij = V_ij mod Zc",
        "0 is a valid shift; missing BG entries become all-zero blocks",
        "#FFFFFF",
        PALETTE["green"],
    )
    mx, my = 1055, 735
    z, block = 5, 42
    shift = 2
    for r in range(z):
        for c in range(z):
            box = (mx + c * block, my + r * block, mx + (c + 1) * block, my + (r + 1) * block)
            hit = c == (r + shift) % z
            draw.rectangle(box, fill=PALETTE["green"] if hit else "#FFFFFF", outline=PALETTE["line"], width=1)
            if hit:
                center_text(draw, box, "1", font(24, True), "#FFFFFF")
    draw.text((1305, 770), "Zc=5, shift=2", font=font(24, True), fill=PALETTE["ink"])
    draw_wrapped(draw, (1305, 812), "Receiver address: base(column)+(local+shift) mod Zc.", font(24), PALETTE["muted"], 160)

    # Right panel: receiver use.
    panel3 = (1560, 205, 2130, 990)
    draw.rounded_rectangle(panel3, radius=18, fill=PALETTE["panel"], outline=PALETTE["line"], width=2)
    draw.text((1595, 238), "3. 接收端用途", font=font(30, True), fill=PALETTE["purple"])
    steps = [
        ("Descriptor", "BG, Zc, iLS, N, Ncb, RV"),
        ("Shift ROM", "row group, column group, shift"),
        ("Rate recovery", "mother-code LLR and masks"),
        ("Layered core", "RMW LLR and message memory"),
        ("HARQ view", "new/repeated/unknown parity coverage"),
    ]
    y = 315
    for idx, (title, body) in enumerate(steps):
        box = (1605, y, 2085, y + 125)
        label_box(draw, box, title, body, "#FFFFFF", PALETTE["purple"] if idx % 2 else PALETTE["blue"])
        if idx < len(steps) - 1:
            draw_arrow(draw, (1845, y + 128), (1845, y + 135), PALETTE["muted"])
        y += 135
    out = ASSET_DIR / "T8.3_NR_LDPC_BG_regions_QC_receiver.png"
    img.save(out)
    print(f"WROTE {out}")


def main() -> None:
    print(
        "SKIP BG1/BG2 shift tables: use "
        "tools/figures/render_nr_ldpc_bg_tables_from_pdf.py to crop the "
        "Word/PDF original tables."
    )
    render_bg_regions_qc_receiver()
    render_toy_expansion()


if __name__ == "__main__":
    main()
