#!/usr/bin/env python3
"""Render TS 38.212 LDPC lifting and base graph tables for T3.4."""

from __future__ import annotations

import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
TABLE_DIR = ROOT / "3GPP_Rel19/processed/TS_38.212_38212-j30/tables"
OUT_DIR = ROOT / "docs/L1/assets"



def text_center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def wrap_lines(draw: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def wrapped_center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str, gap: int = 5) -> None:
    lines = wrap_lines(draw, text, fnt, box[2] - box[0] - 18)
    heights = [draw.textbbox((0, 0), line, font=fnt)[3] for line in lines]
    total_h = sum(heights) + gap * max(0, len(lines) - 1)
    y = box[1] + ((box[3] - box[1]) - total_h) / 2
    for line, height in zip(lines, heights):
        bbox = draw.textbbox((0, 0), line, font=fnt)
        x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
        draw.text((x, y), line, font=fnt, fill=fill)
        y += height + gap


def read_csv(name: str) -> list[list[str]]:
    with (TABLE_DIR / f"{name}.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.reader(handle))


def render_lifting_sets() -> None:
    rows = read_csv("table_0013")[1:]
    width, height = 2040, 900
    img = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "TS 38.212 Table 5.3.2-1 本地复现：LDPC lifting size sets", font=font(40, True), fill="#102033")
    wrapped_center(
        draw,
        (70, 88, 1970, 140),
        "每个 set index 对应一组允许的提升大小 Zc。接收端选定 Zc 后，后续 BG1/BG2 shift table 按同一个 set index 取列。",
        font(24),
        "#526171",
    )

    x0, y0 = 100, 178
    col_w = [220, 1540]
    row_h = 72  # TEXT_FIT_OK: lifting-set rows are centered 24px text in 1540px value column.
    headers = ["Set index", "Set of lifting sizes Zc"]
    x = x0
    for header, w in zip(headers, col_w):
        draw.rectangle((x, y0, x + w, y0 + row_h), fill="#DDE8F5", outline="#B9C8D8", width=2)
        text_center(draw, (x, y0, x + w, y0 + row_h), header, font(24, True), "#102033")
        x += w

    y = y0 + row_h
    for idx, row in enumerate(rows):
        fill = "#FFFFFF" if idx % 2 == 0 else "#F6F9FD"
        x = x0
        draw.rectangle((x, y, x + col_w[0], y + row_h), fill="#EEF4FB", outline="#D7DEE8", width=1)
        text_center(draw, (x, y, x + col_w[0], y + row_h), row[0].strip(), font(24, True), "#102033")
        x += col_w[0]
        draw.rectangle((x, y, x + col_w[1], y + row_h), fill=fill, outline="#D7DEE8", width=1)
        text_center(draw, (x, y, x + col_w[1], y + row_h), row[1].strip(), font(24), "#102033")
        y += row_h

    wrapped_center(
        draw,
        (70, height - 76, width - 70, height - 24),
        "Local evidence: TS 38.212 38212-j30 tables/table_0013.csv and .html; rendered by tools/figures/render_nr_ldpc_tables.py",
        font(24),
        "#607085",
    )
    out = OUT_DIR / "T3.4_TS38.212_Table_5.3.2-1_lifting_sets.png"
    img.save(out, optimize=True)
    print(f"WROTE {out}")


def render_shift_table(table_name: str, title: str, out_name: str) -> None:
    rows = read_csv(table_name)
    data = rows[3:]
    row_h = 60  # TEXT_FIT_OK: shift-table cells are numeric/short labels centered in fixed columns.
    col_w = [124, 142] + [102] * 8 + [124, 142] + [102] * 8
    width = 120 + sum(col_w) + 120
    height = 232 + row_h * len(data) + 92
    img = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw.text((60, 36), title, font=font(38, True), fill="#09243D")
    wrapped_center(
        draw,
        (60, 78, width - 60, 138),
        "协议原表为横向双栏排版。每个半栏包含 row index、column index 和 set index 0-7 下的 shift value；空白 row index 表示延续上一行 row group，数值 0 是有效零移位。",
        font(24),
        "#43566B",
    )

    x0, y0 = 60, 178
    headers = ["Row", "Col", "iLS=0", "1", "2", "3", "4", "5", "6", "7"] * 2
    x = x0
    for text, w in zip(headers, col_w):
        draw.rectangle((x, y0, x + w, y0 + row_h), fill="#DDE8F5", outline="#B9C8D8", width=2)
        text_center(draw, (x, y0, x + w, y0 + row_h), text, font(24, True), "#102033")
        x += w

    y = y0 + row_h
    for ridx, row in enumerate(data):
        row = row + [""] * max(0, 20 - len(row))
        x = x0
        for c, w in enumerate(col_w):
            text = row[c].strip()
            fill = "#FFFFFF" if ridx % 2 == 0 else "#F6F9FD"
            if c in {0, 1, 10, 11}:
                fill = "#EEF4FB" if text else "#F8FAFD"
            elif text == "0":
                fill = "#F4F7FA"
            draw.rectangle((x, y, x + w, y + row_h), fill=fill, outline="#D7DEE8", width=1)
            wrapped_center(draw, (x + 4, y + 3, x + w - 4, y + row_h - 3), text, font(24, c in {0, 10}), "#102033", gap=3)
            x += w
        y += row_h

    draw.text((60, height - 54), f"Local evidence: TS 38.212 38212-j30 tables/{table_name}.csv and .html; rendered by tools/figures/render_nr_ldpc_tables.py", font=font(24), fill="#607085")
    out = OUT_DIR / out_name
    img.save(out, optimize=True)
    print(f"WROTE {out}")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    render_lifting_sets()
    print(
        "SKIP BG1/BG2 shift tables: use "
        "tools/figures/render_nr_ldpc_bg_tables_from_pdf.py to crop the "
        "Word/PDF original tables."
    )


if __name__ == "__main__":
    main()
