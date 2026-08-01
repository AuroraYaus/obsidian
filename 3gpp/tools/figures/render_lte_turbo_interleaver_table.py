#!/usr/bin/env python3
"""@file render_lte_turbo_interleaver_table.py
@brief 渲染 TS 36.212 Table 5.1.3-3：LTE Turbo 内部交织器参数的完整教学表格
@date 2025
@note 设计意图：以四个分面展示 188 条 (i,K,f1,f2) 参数，黄色高亮 B=10001 手算用到的 K=4992/5056
  和最大块长 K=6144，确保 Markdown 缩放后仍可逐行核验。
@see docs/L1/T3.3_TS36.212_Table_5.1.3-3_interleaver.md
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
CSV_PATH = ROOT / "3GPP_Rel19/processed/TS_36.212_36212-j30/tables/table_0009.csv"
OUT_PATH = ROOT / "docs/L1/assets/T3.3_TS36.212_Table_5.1.3-3.png"


def load_entries() -> list[tuple[int, int, int, int]]:
    """@brief 从 CSV 文件加载 Turbo 内部交织器参数表
    @return 按 i 升序排列的 (i, K, f1, f2) 元组列表，共 188 条
    @note CSV 源自 TS 36.212 j30，一行包含 4 个 (i,K,f1,f2) 组，
      读取时按 offset 展开并排序"""
    entries: list[tuple[int, int, int, int]] = []
    for row in csv.reader(CSV_PATH.read_text(encoding="utf-8").splitlines()):
        if not row or row[0] == "i":
            continue
        for offset in (0, 4, 8, 12):
            if offset + 3 < len(row) and row[offset].strip():
                entries.append(tuple(int(x) for x in row[offset : offset + 4]))
    return sorted(entries)


def centered_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    """@brief 在矩形单元格内居中绘制单行文本
    @param draw PIL 绘图上下文
    @param box 目标矩形 (x0, y0, x1, y1)
    @param text 要绘制的文本
    @param fnt 字体对象
    @param fill 文字颜色
    @note 水平和垂直双向居中"""
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = box[0] + (box[2] - box[0] - tw) / 2
    y = box[1] + (box[3] - box[1] - th) / 2 - 1
    draw.text((x, y), text, fill=fill, font=fnt)


def wrapped_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str, gap: int = 4) -> None:
    """@brief 在矩形内绘制自动换行文本（左对齐）
    @param draw PIL 绘图上下文
    @param box 目标矩形 (x0, y0, x1, y1)
    @param text 原始文本
    @param fnt 字体对象
    @param fill 文字颜色
    @param gap 行间距像素，默认 4
    @note 按空格分词后贪心换行，不做断词处理"""
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
    """@brief 绘制单个带边框的表格单元格并居中文字
    @param draw PIL 绘图上下文
    @param xy 单元格矩形 (x0, y0, x1, y1)
    @param text 单元格内文字
    @param fill 填充颜色
    @param outline 边框颜色
    @param text_fill 文字颜色
    @param fnt 字体对象
    @note 边框宽度固定 1px"""
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
    """@brief 绘制一个参数分面面板（含标题、表头和所有数据行）
    @param draw PIL 绘图上下文
    @param entries 该分面的 (i,K,f1,f2) 条目列表
    @param title 分面标题（如 "i = 1 .. 47"）
    @param subtitle 分面副标题
    @param x0 面板左上角 X 坐标
    @param y0 面板左上角 Y 坐标
    @param panel_w 面板宽度
    @param row_h 行高像素
    @note 表头深蓝色底色白字，数据行斑马条纹，高亮 K 值用黄色背景"""
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
    """@brief 渲染 TS 36.212 Table 5.1.3-3 完整交织器参数表
    @note 输出文件: docs/L1/assets/T3.3_TS36.212_Table_5.1.3-3.png
    @note 四个分面按 i 范围 (1-47, 48-94, 95-141, 142-188) 布局，
      高亮色标注教学关键 K 值，底部附证据链说明
    @throws SystemExit CSV 解析后条目数不为 188 时退出"""
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
