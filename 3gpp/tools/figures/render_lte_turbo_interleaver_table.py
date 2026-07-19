#!/usr/bin/env python3
"""Render TS 36.212 Table 5.1.3-3 as a readable teaching figure."""

from __future__ import annotations

import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "3GPP_Rel19/processed/TS_36.212_36212-j30/tables/table_0009.csv"
OUT_PATH = ROOT / "docs/L1/assets/T3.3_TS36.212_Table_5.1.3-3.png"



def load_entries() -> list[tuple[int, int, int, int]]:
    entries: list[tuple[int, int, int, int]] = []
    for row in csv.reader(CSV_PATH.read_text(encoding="utf-8").splitlines()):
        if not row or row[0] == "i":
            continue
        for offset in (0, 4, 8, 12):
            if offset + 3 < len(row) and row[offset].strip():
                entries.append(tuple(int(x) for x in row[offset : offset + 4]))
    return sorted(entries)


def centered_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = box[0] + (box[2] - box[0] - tw) / 2
    y = box[1] + (box[3] - box[1] - th) / 2 - 1
    draw.text((x, y), text, fill=fill, font=fnt)


def wrapped_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str, gap: int = 4) -> None:
    words = text.split()
    lines: list[str] = []
    current = ""
    max_w = box[2] - box[0]
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= max_w or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    y = box[1]
    for line in lines:
        draw.text((box[0], y), line, fill=fill, font=fnt)
        y += draw.textbbox((0, 0), line, font=fnt)[3] + gap


def draw_cell(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fill: str,
    outline: str,
    text_fill: str,
    fnt: ImageFont.FreeTypeFont,
) -> None:
    draw.rectangle(xy, fill=fill, outline=outline, width=1)
    centered_text(draw, xy, text, fnt, text_fill)


def draw_group(
    draw: ImageDraw.ImageDraw,
    entries: list[tuple[int, int, int, int]],
    title: str,
    subtitle: str,
    x0: int,
    y0: int,
    panel_w: int,
    row_h: int,
    *,
    highlight_ks: set[int],
) -> None:
    border = "#C8D0DA"
    panel_bg = "#F8FAFC"
    header_bg = "#123B63"
    cell_bg = "#FFFFFF"
    zebra_bg = "#F3F7FB"
    highlight_bg = "#FFF0C2"
    text = "#18212F"
    muted = "#4B5B6B"
    blue = "#0A5FB4"

    panel_h = 104 + row_h * (len(entries) + 1)
    draw.rounded_rectangle((x0, y0, x0 + panel_w, y0 + panel_h), radius=18, fill=panel_bg, outline=border, width=2)
    draw.text((x0 + 18, y0 + 12), title, fill="#0E2F4F", font=font(24, bold=True))
    draw.text((x0 + 18, y0 + 48), subtitle, fill=muted, font=font(24))

    cols = [92, 136, 120, 120]
    table_w = sum(cols)
    tx = x0 + (panel_w - table_w) // 2
    ty = y0 + 96
    header_labels = ["i", "K", "f1", "f2"]
    x = tx
    for label, width in zip(header_labels, cols):
        draw_cell(draw, (x, ty, x + width, ty + row_h), label, header_bg, "#0B2B49", "#FFFFFF", font(24, bold=True))
        x += width

    for ridx, (idx, k, f1, f2) in enumerate(entries):
        y = ty + row_h * (ridx + 1)
        row_fill = highlight_bg if k in highlight_ks else (zebra_bg if ridx % 2 else cell_bg)
        values = [idx, k, f1, f2]
        x = tx
        for cidx, (value, width) in enumerate(zip(values, cols)):
            color = blue if cidx == 1 else (muted if cidx in (2, 3) else text)
            draw_cell(draw, (x, y, x + width, y + row_h), str(value), row_fill, "#D6DEE8", color, font(24))
            x += width


def main() -> None:
    entries = load_entries()
    if len(entries) != 188:
        raise SystemExit(f"expected 188 entries, got {len(entries)}")

    width, height = 2360, 6060
    img = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw.text((70, 38), "TS 36.212 Table 5.1.3-3：LTE Turbo 内部交织器参数", fill="#0A2540", font=font(38, bold=True))
    wrapped_text(
        draw,
        (70, 88, 2260, 150),
        "Rel-19 36212-j30，Table 5.1.3-3。四个分面按 i 分组展示；主体表格按 56px 行高和 24px 文字重排，保证 Markdown 缩放后仍能直接核对参数。黄色高亮：T3.3 的 B=10001 手算例子使用 K=4992 和 K=5056；K=6144 是最大支持块长。",
        font(24),
        "#425466",
    )

    groups = [
        (1, 47, (70, 190)),
        (48, 94, (1210, 190)),
        (95, 141, (70, 3090)),
        (142, 188, (1210, 3090)),
    ]
    panel_w = 1080
    row_h = 56  # TEXT_FIT_OK: numeric table cells use centered 24px labels with fixed-width columns.
    for lo, hi, (x, y) in groups:
        draw_group(
            draw,
            entries[lo - 1 : hi],
            f"i = {lo} .. {hi}",
            "i / K / f1 / f2",
            x,
            y,
            panel_w,
            row_h,
            highlight_ks={4992, 5056, 6144},
        )

    foot_box = (70, 5920, 2290, 6015)
    draw.rounded_rectangle(foot_box, radius=14, fill="#FBFCFE", outline="#D2DDE9", width=2)
    centered_text(draw, (95, 5934, 310, 5998), "证据", font(24, bold=True), "#0A2540")
    wrapped_text(
        draw,
        (320, 5930, 2250, 6005),
        "生成依据：3GPP_Rel19/processed/TS_36.212_36212-j30/tables/table_0009.csv；脚本：tools/figures/render_lte_turbo_interleaver_table.py",
        font(24),
        "#5F6B7A",
    )
    draw.text((320, 5968), "例外：左上角 i 为短索引字段，可低于主体说明密度；其余正文、表头、首列和证据说明均已提升到 24px。", fill="#5F6B7A", font=font(24))

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH, optimize=True)
    print(OUT_PATH)


if __name__ == "__main__":
    main()
