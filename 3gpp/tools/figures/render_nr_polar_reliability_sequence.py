#!/usr/bin/env python3
"""@file render_nr_polar_reliability_sequence.py
@brief 渲染 TS 38.212 Table 5.3.1.2-1 Polar 可靠性序列本地复现表格，展示 rank 与 Q(rank) 的完整映射关系。
@date 2025
"""

from __future__ import annotations

import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "3GPP_Rel19/processed/TS_38.212_38212-j30/tables/table_0012.csv"
OUT_PATH = ROOT / "docs/L2_协议算法/assets/T10.3_TS38.212_Table_5.3.1.2-1_Polar_sequence.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#596879",
    "line": "#CBD5E1",
    "head": "#DDE8F5",
    "subhead": "#EEF4FA",
    "cell": "#FFFFFF",
    "alt": "#F8FAFD",
    "blue": "#2457A6",
    "green": "#2D8F5D",
    "red": "#C64B59",
}



def center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    """@brief 在矩形区域内居中绘制文本，用于表格单元格的 rank/Q(rank) 数据对齐。
    @param draw PIL ImageDraw 绘制上下文
    @param box 目标矩形区域 (x0, y0, x1, y1)
    @param text 要绘制的文本内容
    @param fnt PIL 字体对象
    @param fill 文本颜色
    @return None
    """
    b = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + (box[2] - box[0] - (b[2] - b[0])) / 2
    y = box[1] + (box[3] - box[1] - (b[3] - b[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def read_pairs() -> list[tuple[int, int]]:
    """@brief 从 TS 38.212 table_0012.csv 读取 Polar 可靠性序列的 (rank, Q(rank)) 配对数据并进行完整性校验。
    @return 按 rank 升序排列的 (rank, Q(rank)) 元组列表，共 1024 对
    @throws AssertionError 当数据对数不为 1024 或 rank 不连续时抛出
    @note rank 是可靠性升序位置（0 最不可靠，1023 最可靠），Q(rank) 是编码前 bit index。
    """
    pairs: list[tuple[int, int]] = []
    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        for row in csv.reader(handle):
            vals = [cell.strip() for cell in row if cell.strip()]
            for i in range(0, len(vals) - 1, 2):
                if vals[i].isdigit() and vals[i + 1].isdigit():
                    pairs.append((int(vals[i]), int(vals[i + 1])))
    pairs = sorted(pairs)
    assert len(pairs) == 1024
    assert [rank for rank, _ in pairs] == list(range(1024))
    return pairs


def main() -> None:
    """@brief 脚本入口：生成 TS 38.212 Table 5.3.1.2-1 Polar 可靠性序列本地复现表格 T10.3_TS38.212_Table_5.3.1.2-1_Polar_sequence.png。
    @note 表格按 8 组、每组 128 行的格式展示 1024 对 (rank, Q(rank)) 映射。
    每组两列：rank（可靠性升序位置）和 Q(rank)（编码前 bit index）。
    检查点：Q(0)=0, Q(1)=1, Q(2)=2, Q(3)=4, Q(1023)=1023。
    数据来源：3GPP_Rel19/processed/TS_38.212_38212-j30/tables/table_0012.csv。
    @see docs/L2_协议算法/assets/T10.2_NR_Polar_N4_transform_frozen_mask.svg N=4 Polar 极化变换图（手绘 SVG，原 render_nr_polar_channel_polarization.py 已删除）
    """
    pairs = read_pairs()
    groups = 8
    rows = 128
    cell_w = 120
    cell_h = 56  # TEXT_FIT_OK: cells contain only short numeric rank/Q(rank) labels at 24px.
    left = 70
    top = 150
    title_h = 90
    width = left * 2 + groups * cell_w * 2
    height = top + title_h + 2 * cell_h + rows * cell_h + 120
    img = Image.new("RGB", (width, height), COL["bg"])
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "TS 38.212 Table 5.3.1.2-1 Polar sequence 可靠性序列", font=font(32, True), fill=COL["ink"])
    draw.text((70, 92), "每组两列：rank 是可靠性升序位置，Q(rank) 是编码前 bit index。rank 越大，可靠性越高。", font=font(24), fill=COL["muted"])

    y0 = top
    x0 = left
    for g in range(groups):
        gx = x0 + g * cell_w * 2
        draw.rectangle((gx, y0, gx + cell_w * 2, y0 + cell_h), fill=COL["head"], outline=COL["line"])
        center(draw, (gx, y0, gx + cell_w * 2, y0 + cell_h), f"group {g}", font(24, True), COL["ink"])
        draw.rectangle((gx, y0 + cell_h, gx + cell_w, y0 + 2 * cell_h), fill=COL["subhead"], outline=COL["line"])
        draw.rectangle((gx + cell_w, y0 + cell_h, gx + 2 * cell_w, y0 + 2 * cell_h), fill=COL["subhead"], outline=COL["line"])
        center(draw, (gx, y0 + cell_h, gx + cell_w, y0 + 2 * cell_h), "rank", font(24, True), COL["blue"])
        center(draw, (gx + cell_w, y0 + cell_h, gx + 2 * cell_w, y0 + 2 * cell_h), "Q(rank)", font(24, True), COL["green"])

    body_y = y0 + 2 * cell_h
    for r in range(rows):
        for g in range(groups):
            rank, q = pairs[g * rows + r]
            gx = x0 + g * cell_w * 2
            gy = body_y + r * cell_h
            fill = COL["alt"] if r % 2 else COL["cell"]
            draw.rectangle((gx, gy, gx + cell_w, gy + cell_h), fill=fill, outline=COL["line"])
            draw.rectangle((gx + cell_w, gy, gx + 2 * cell_w, gy + cell_h), fill=fill, outline=COL["line"])
            center(draw, (gx, gy, gx + cell_w, gy + cell_h), str(rank), font(24), COL["ink"])
            center(draw, (gx + cell_w, gy, gx + 2 * cell_w, gy + cell_h), str(q), font(24, True), COL["ink"])

    note_y = body_y + rows * cell_h + 28
    draw.text((70, note_y), "读表检查：Q(0)=0, Q(1)=1, Q(2)=2, Q(3)=4, Q(1023)=1023；", font=font(24, True), fill=COL["red"])
    draw.text((70, note_y + 34), "本图由本地 table_0012.csv 生成。", font=font(24, True), fill=COL["red"])
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")
    print("TABLE_0012_PAIRS", len(pairs), pairs[:4], pairs[-1])


if __name__ == "__main__":
    main()
