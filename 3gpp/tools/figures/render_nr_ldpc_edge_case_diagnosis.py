#!/usr/bin/env python3
"""@file render_nr_ldpc_edge_case_diagnosis.py
@brief 渲染 NR LDPC Decoder Edge Case Diagnosis 排查流程图
@date 2025
@note 设计意图：按协议链路从左到右展示失败排查流程（Descriptor→Rate recovery→LDPC core→CRC/reassembly），
  配合八类边界案例卡片和核心排查原则（先检查输入边界和地址轨迹，最后才怀疑 LDPC core）。
@see docs/L2/T9.6_NR_LDPC_edge_case_diagnosis.md
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T9.6_NR_LDPC_edge_case_diagnosis.png"

COLORS = {
    "ink": "#17212F",
    "muted": "#5A6675",
    "line": "#C7D1DC",
    "bg": "#FFFFFF",
    "blue": "#2457A6",
    "blue_l": "#EAF3FF",
    "green": "#278760",
    "green_l": "#EAF8EF",
    "amber": "#B9841A",
    "amber_l": "#FFF5DD",
    "red": "#B94A55",
    "red_l": "#FFECEF",
    "purple": "#6E55A4",
    "purple_l": "#F1EDFF",
}


def center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill: str) -> None:
    """@brief 在矩形内居中绘制单行文本
    @param draw PIL 绘图上下文
    @param box 目标矩形
    @param text 文本
    @param fnt 字体对象
    @param fill 文字颜色"""
    bbox = draw.textbbox((0, 0), text, font=fnt)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    x = box[0] + ((box[2] - box[0]) - width) / 2 - bbox[0]
    y = box[1] + ((box[3] - box[1]) - height) / 2 - bbox[1]
    draw.text((x, y), text, font=fnt, fill=fill)


def wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, width: int, fill: str, gap: int = 4) -> int:
    """@brief 在指定位置绘制自动换行文本
    @param draw PIL 绘图上下文
    @param xy 起始坐标
    @param text 原始文本
    @param fnt 字体对象
    @param width 每行最大像素宽度
    @param fill 文字颜色
    @param gap 行间距，默认 4
    @return 绘制后的下一行 Y 坐标"""
    x, y = xy
    for line in fit_wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    """@brief 绘制带箭头头的线段（固定灰色）
    @param draw PIL 绘图上下文
    @param start 起点坐标
    @param end 终点（箭头尖端）坐标
    @note 固定颜色 #66788A，箭头头长 14px、宽 8px"""
    sx, sy = start
    ex, ey = end
    length = math.hypot(ex - sx, ey - sy)
    if length == 0:
        return
    ux, uy = (ex - sx) / length, (ey - sy) / length
    px, py = -uy, ux
    head_len, head_w = 14, 8
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line((sx, sy, *line_end), fill="#66788A", width=3)
    draw.polygon(
        [
            (ex, ey),
            (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
            (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
        ],
        fill="#66788A",
    )


def stage(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], num: str, title: str, checks: list[str], fill: str, edge: str) -> None:
    """@brief 绘制排查流程的一个阶段卡片
    @param draw PIL 绘图上下文
    @param box 卡片矩形
    @param num 阶段编号（如 "1"）
    @param title 阶段标题（如 "Descriptor"）
    @param checks 该阶段的检查项列表，每项前有圆点标记
    @param fill 卡片填充色
    @param edge 编号圆点和卡片边框颜色
    @note 编号在左上角圆角框中显示，检查项以圆点列表形式排列"""
    draw.rounded_rectangle(box, radius=14, fill=fill, outline=edge, width=2)
    center(draw, (box[0] + 14, box[1] + 14, box[0] + 60, box[1] + 58), num, font(24, True), edge)
    draw.text((box[0] + 70, box[1] + 20), title, font=font(24, True), fill=COLORS["ink"])
    y = box[1] + 70
    for item in checks:
        draw.ellipse((box[0] + 28, y + 6, box[0] + 36, y + 14), fill=edge)
        y = wrapped(draw, (box[0] + 48, y), item, font(24), box[2] - box[0] - 72, COLORS["muted"], gap=3) + 4


def draw_flow(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制四阶段排查流程卡片链
    @param draw PIL 绘图上下文
    @note 从左到右排列：Descriptor → Rate recovery → LDPC core → CRC/reassembly，
      每阶段列出具体检查字段"""
    y = 185
    boxes = [
        ("1", "Descriptor", ["BG, Zc, K/Kb, C", "Qm, E, Ncb, RV", "CBG mask, NDI, HARQ id"], COLORS["blue_l"], COLORS["blue"]),
        ("2", "Rate recovery", ["bit deinterleaving", "RV/k0 address trace", "unknown / shortened / repeat"], COLORS["purple_l"], COLORS["purple"]),
        ("3", "LDPC core", ["layer/edge schedule", "LLR sign and saturation", "syndrome curve"], COLORS["green_l"], COLORS["green"]),
        ("4", "CRC/reassembly", ["filler and CB CRC strip", "CB concat order", "TB CRC and HARQ feedback"], COLORS["amber_l"], COLORS["amber"]),
    ]
    x = 60
    prev = None
    for num, title, checks, fill, edge in boxes:
        box = (x, y, x + 345, y + 228)
        stage(draw, box, num, title, checks, fill, edge)
        if prev:
            arrow(draw, (prev[2], y + 95), (box[0], y + 95))
        prev = box
        x += 382


def draw_cases(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制八类典型边界案例卡片网格
    @param draw PIL 绘图上下文
    @note 4x2 网格排列，每张卡片含标题、关联字段和典型现象"""
    draw.text((70, 422), "典型边界案例与首查字段", font=font(28, True), fill=COLORS["ink"])
    cases = [
        ("BG boundary", "A/R -> BG", "syndrome 不收敛，CB CRC fail"),
        ("Zc boundary", "iLS/Zc/table", "矩阵尺寸或地址错位"),
        ("filler", "filler ranges", "TB CRC fail 或长度异常"),
        ("RV mismatch", "rvid/k0/Ncb", "soft buffer 命中区域异常"),
        ("CBG mismatch", "CBGTI/CBGFI", "held CBG 被覆盖或未更新"),
        ("LLR saturation", "sat_count/range", "syndrome 曲线停滞"),
        ("syndrome vs CRC", "hard bits/ranges", "syndrome pass 但 CRC fail"),
        ("upper assembly", "tb_id/cw_id/MAC", "CRC pass 但上层组包失败"),
    ]
    cols = 4
    x0, y0 = 90, 486
    w, h = 330, 154
    for idx, (title, field, symptom) in enumerate(cases):
        col = idx % cols
        row = idx // cols
        x = x0 + col * 360
        y = y0 + row * 168
        draw.rounded_rectangle((x, y, x + w, y + h), radius=10, fill="#FFFFFF", outline=COLORS["line"], width=1)
        draw.text((x + 18, y + 14), title, font=font(24, True), fill=COLORS["ink"])
        draw.text((x + 18, y + 54), f"字段：{field}", font=font(24), fill=COLORS["blue"])
        wrapped(draw, (x + 18, y + 86), f"现象：{symptom}", font(24), 298, COLORS["muted"], gap=3)


def draw_warning(draw: ImageDraw.ImageDraw) -> None:
    """@brief 绘制核心排查原则说明面板
    @param draw PIL 绘图上下文
    @note 强调排查顺序：先 descriptor/rate recovery/重组边界，最后才怀疑 LDPC core。
      附带六个建议采集的调试字段标签"""
    panel = (70, 900, 1495, 1155)
    draw.rounded_rectangle(panel, radius=14, fill="#FFFDF7", outline="#DDBB60", width=2)
    draw.text((100, 898), "排查原则：不要优先怀疑 LDPC core", font=font(27, True), fill=COLORS["amber"])
    text = (
        "先确认 descriptor、rate recovery 和重组边界。如果 BG/Zc/RV/CBG/filler/order 错，"
        "LDPC core 即使完全正确也会输出失败。只有在输入边界和地址轨迹被固定 pattern 证明正确后，"
        "再排查 Min-Sum、layer schedule、定点饱和和 syndrome checker。"
    )
    wrapped(draw, (100, 986), text, font(24), 1385, COLORS["muted"], gap=5)
    fields = ["descriptor_dump", "addr_trace", "llr_range", "syndrome_curve", "crc_ranges", "harq_state"]
    x = 100
    for field in fields:
        fnt = font(24, True)
        bbox = draw.textbbox((0, 0), field, font=fnt)
        width = max(215, bbox[2] - bbox[0] + 36)
        box = (x, 1070, x + width, 1122)
        draw.rounded_rectangle(box, radius=7, fill="#FFFFFF", outline=COLORS["line"], width=1)
        center(draw, box, field, fnt, COLORS["ink"])
        x += width + 10


def main() -> None:
    """@brief 渲染 NR LDPC Decoder Edge Case Diagnosis 排查图
    @note 输出文件: docs/L2/assets/T9.6_NR_LDPC_edge_case_diagnosis.png
    @note 图中包含四阶段排查流程卡、八类边界案例网格和核心排查原则面板，
      核心信息：先检查输入边界和地址轨迹，最后才怀疑 LDPC core"""
    img = Image.new("RGB", (1600, 1220), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 40), "NR LDPC Decoder Edge Case Diagnosis", font=font(40, True), fill=COLORS["ink"])
    wrapped(
        draw,
        (70, 104),
        "失败排查按协议链路从左到右推进：先 descriptor，再 rate recovery，再 LDPC core，最后 CRC 和重组。每一步都必须有可复现字段和最小 dump。",
        font(24),
        1460,
        COLORS["muted"],
    )
    draw_flow(draw)
    draw_cases(draw)
    draw_warning(draw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
