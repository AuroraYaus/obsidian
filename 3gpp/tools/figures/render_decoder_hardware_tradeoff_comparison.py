#!/usr/bin/env python3
""" @file render_decoder_hardware_tradeoff_comparison.py
    @brief 渲染 Turbo/LDPC/Polar 三种译码器硬件架构取舍对比图。
    @date 2025
    @note 对比并行度、存储访问、排序、迭代/列表深度、延迟、吞吐、功耗和验证风险六个维度。
    @see render_decoder_selection_by_channel_type.py 对应的译码器选择决策图
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T11.4_decoder_hardware_tradeoff_comparison.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#5B6878",
    "line": "#A8B6C7",
    "turbo": "#B65B2E",
    "turbo_l": "#FFF0E6",
    "ldpc": "#22785A",
    "ldpc_l": "#E8F6EF",
    "polar": "#2457A6",
    "polar_l": "#EAF1FB",
    "shared": "#6E55A4",
    "shared_l": "#F1EDFF",
    "amber": "#B9841A",
    "amber_l": "#FFF5DD",
    "panel": "#F6F8FB",
}



def tokenize(text: str) -> list[str]:
    """ @brief 将文本按单词和空白符分解为 token 列表，用于后续自动换行。
        @param text 待分词的原始字符串，可含中英文混排和换行符。
        @return 分词结果列表：每个元素为完整单词、单个空白或单个特殊字符。
        @note ASCII 字母数字和常见符号 /_-+.[] 视为单词内字符，其余按字符单独拆分。
    """
    tokens: list[str] = []
    cur = ""
    for ch in text:
        if ch == "\n":
            if cur:
                tokens.append(cur)
                cur = ""
            tokens.append("\n")
        elif ch.isascii() and (ch.isalnum() or ch in "/_-+.[]"):
            cur += ch
        else:
            if cur:
                tokens.append(cur)
                cur = ""
            if ch.isspace():
                tokens.append(" ")
            else:
                tokens.append(ch)
    if cur:
        tokens.append(cur)
    return tokens


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    """ @brief 按给定像素宽度对文本自动换行，返回分行后的字符串列表。
        @param draw PIL ImageDraw 实例，用于测量文本实际渲染宽度。
        @param text 待分行的原始文本，可含换行符和中文。
        @param fnt PIL 字体对象，决定字符宽度度量。
        @param width 每行最大像素宽度（整数）。
        @return 按宽度裁剪后的字符串行列表。
        @note 调用 tokenize() 分词后再逐 token 拼接，超过宽度则换行。
    """
    lines: list[str] = []
    cur = ""
    for tok in tokenize(text):
        if tok == "\n":
            if cur:
                lines.append(cur.strip())
                cur = ""
            continue
        nxt = cur + tok
        if draw.textlength(nxt, font=fnt) <= width or not cur.strip():
            cur = nxt
        else:
            if cur.strip():
                lines.append(cur.strip())
            cur = tok
    if cur:
        lines.append(cur.strip())
    return lines


def center(box: tuple[int, int, int, int]) -> tuple[float, float]:
    """ @brief 返回矩形包围盒的几何中心坐标。
        @param box (left, top, right, bottom) 四元组。
        @return (cx, cy) 中心浮点坐标。
    """
    return ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2)


def draw_centered(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str | list[str],
    size: int,
    color: str = COL["ink"],
    bold: bool = True,
    gap: int = 7,
) -> None:
    """ @brief 在指定矩形内竖直居中对齐绘制多行文本。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 绘制区域。
        @param text 待绘制的字符串或字符串列表。
        @param size 字体大小（像素）。
        @param color CSS 颜色字符串，默认为 ink 色。
        @param bold 是否使用粗体，默认 True。
        @param gap 行间距（像素），默认 7。
        @return 无返回值。
        @throws RuntimeError 当文本总高度超出 box 可用高度时抛出，防止文字溢出不可见。
    """
    fnt = font(size, bold)
    raw_lines = text if isinstance(text, list) else [text]
    lines: list[str] = []
    for line in raw_lines:
        lines.extend(wrap(draw, line, fnt, box[2] - box[0] - 28))
    heights = [draw.textbbox((0, 0), line, font=fnt)[3] - draw.textbbox((0, 0), line, font=fnt)[1] for line in lines]
    total = sum(heights) + gap * (len(lines) - 1)
    available = box[3] - box[1]
    if total > available:
        preview_parts: list[str] = []
        for line in lines:
            if len(preview_parts) >= 2:
                break
            preview_parts.append(line)
        preview = " / ".join(preview_parts)
        raise RuntimeError(f"text overflow in {box}: need {total}px, available {available}px: {preview}")
    x = (box[0] + box[2]) / 2
    y = (box[1] + box[3] - total) / 2
    for line, h in zip(lines, heights):
        draw.text((x, y + h / 2), line, font=fnt, fill=color, anchor="mm")
        y += h + gap


def boundary_point(box: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    """ @brief 计算矩形边界上与目标方向对齐的交点，用于绘制箭头连接线。
        @param box (left, top, right, bottom) 矩形包围盒。
        @param toward 目标点 (x, y)，从矩形中心指向该点的射线与边界相交的位置。
        @return 边界交点坐标 (x, y)。
        @note 按半宽/半高比例缩放方向向量，确保交点落在矩形边界上而非内部。
    """
    cx, cy = center(box)
    dx, dy = toward[0] - cx, toward[1] - cy
    if abs(dx) < 1e-6 and abs(dy) < 1e-6:
        return cx, cy
    half_w = max((box[2] - box[0]) / 2, 1)
    half_h = max((box[3] - box[1]) / 2, 1)
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return cx + dx / scale, cy + dy / scale


def arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color: str, width: int = 3) -> None:
    """ @brief 从起点到终点绘制带三角箭头的直线。
        @param draw PIL ImageDraw 实例。
        @param start 箭头起始坐标 (x, y)。
        @param end 箭头终点坐标 (x, y)，箭头尖端位于此处。
        @param color CSS 颜色字符串。
        @param width 线条宽度（像素），默认 3。
        @return 无返回值。
        @note 箭头尖端尺寸：head_len=15px, head_w=9px；线体在箭头尖端前 head_len 处截断以免覆盖箭头。
    """
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    head_len, head_w = 15, 9
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    draw.line((start, line_end), fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    back_x = x1 - head_len * math.cos(angle)
    back_y = y1 - head_len * math.sin(angle)
    perp_x = head_w * math.sin(angle)
    perp_y = -head_w * math.cos(angle)
    draw.polygon([(x1, y1), (back_x + perp_x, back_y + perp_y), (back_x - perp_x, back_y - perp_y)], fill=color)


def connect(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str) -> None:
    """ @brief 在两个矩形节点之间绘制连接箭头，自动计算边界交点。
        @param draw PIL ImageDraw 实例。
        @param src 源矩形 (left, top, right, bottom)。
        @param dst 目标矩形 (left, top, right, bottom)。
        @param color CSS 颜色字符串。
        @return 无返回值。
        @note 箭头从源边界指向目标边界，不穿入矩形内部。
    """
    arrow(draw, boundary_point(src, center(dst)), boundary_point(dst, center(src)), color)


def node(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str | list[str],
    color: str,
    fill: str,
    size: int = 24,
) -> tuple[int, int, int, int]:
    """ @brief 绘制一个圆角矩形节点，内含居中对齐文本。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 节点包围盒。
        @param text 节点内显示的文本字符串或行列表。
        @param color 边框颜色 CSS 字符串。
        @param fill 背景填充颜色 CSS 字符串。
        @param size 字体大小（像素），默认 24。
        @return 节点包围盒（传入的 box 原样返回，便于链式操作）。
        @note 圆角半径固定为 16，边框宽度 2。
    """
    draw.rounded_rectangle(box, radius=16, fill=fill, outline=color, width=2)
    draw_centered(draw, box, text, size=size, color=COL["ink"], bold=False)
    return box


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, color: str, fill: str) -> None:
    """ @brief 绘制一个带标题的圆角面板区域。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 面板包围盒。
        @param title 面板左上角标题文字。
        @param color 边框颜色 CSS 字符串。
        @param fill 背景填充颜色 CSS 字符串。
        @return 无返回值。
        @note 圆角半径 22，边框宽度 3；标题字号 31，加粗，颜色与边框相同。
    """
    draw.rounded_rectangle(box, radius=22, fill=fill, outline=color, width=3)
    draw.text((box[0] + 26, box[1] + 22), title, font=font(31, True), fill=color)


def draw_datapath(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    color: str,
    fill: str,
    nodes: list[str],
    bottom_note: str,
) -> None:
    """ @brief 绘制单个译码器的硬件数据通路：面板标题 + 流水节点链 + 底部说明。
        @param draw PIL ImageDraw 实例。
        @param box (left, top, right, bottom) 整条数据通路面板的包围盒。
        @param title 面板左上角标题（如"Turbo 硬件数据通路"）。
        @param color 主题色 CSS 字符串。
        @param fill 面板背景色 CSS 字符串。
        @param nodes 流水线各阶段名称列表，从左到右依次绘制并箭头连接。
        @param bottom_note 面板底部的说明文字。
        @return 无返回值。
        @note 每个节点宽度 225、高度 102、间距 18；底部说明区带浅灰边框。
    """
    panel(draw, box, title, color, fill)
    left = box[0] + 40
    y = box[1] + 105
    w, h, gap = 225, 102, 18
    boxes = []
    for i, text in enumerate(nodes):
        b = (left + i * (w + gap), y, left + i * (w + gap) + w, y + h)
        boxes.append(node(draw, b, text, color, "#FFFFFF", 24))
    for a, b in zip(boxes, boxes[1:]):
        connect(draw, a, b, color)
    note_box = (box[0] + 40, box[1] + 245, box[2] - 40, box[1] + 340)
    draw.rounded_rectangle(note_box, radius=14, fill="#FFFFFF", outline=COL["line"], width=1)
    draw_centered(draw, note_box, bottom_note, 24, COL["ink"], False, 6)


def draw_datapaths(draw: ImageDraw.ImageDraw) -> int:
    """ @brief 自上而下绘制 Turbo、LDPC、Polar 三条数据通路面板并对比瓶颈。
        @param draw PIL ImageDraw 实例。
        @return 三条面板底部的 Y 坐标，供后续模块使用。
        @note 每条面板高 380，间距 40；Turbo 瓶颈在 trellis 递推，LDPC 在 message memory，Polar 在 sorter/path copy。
    """
    y0 = 165
    draw_datapath(
        draw,
        (70, y0, 1830, y0 + 380),
        "Turbo 硬件数据通路：顺序 SISO 与交织外信息",
        COL["turbo"],
        COL["turbo_l"],
        ["LLR RAM", "SISO / BCJR", "alpha/beta memory", "interleaver", "extrinsic RAM", "iteration controller"],
        "瓶颈：trellis 前后向递推有顺序依赖；interleaver/deinterleaver 造成外信息 RAM 随机访问；迭代次数直接放大最坏延迟。",
    )
    y1 = y0 + 420
    draw_datapath(
        draw,
        (70, y1, 1830, y1 + 380),
        "LDPC 硬件数据通路：layered schedule 与消息存储",
        COL["ldpc"],
        COL["ldpc_l"],
        ["LLR RAM", "layered controller", "check-node unit", "variable-node update", "message memory", "bank conflict guard"],
        "优势：QC-LDPC 的 row/column group 适合并行；瓶颈：message memory、read-modify-write、bank conflict 和 pipeline stall。",
    )
    y2 = y1 + 420
    draw_datapath(
        draw,
        (70, y2, 1830, y2 + 380),
        "Polar 硬件数据通路：SCL 路径管理与排序",
        COL["polar"],
        COL["polar_l"],
        ["LLR memory", "SC/SCL tree controller", "partial sum memory", "path memory", "sorter", "CRC selector"],
        "瓶颈：information bit 分裂产生 2L 候选；sorter、path copy、partial sum 和 CRC state 必须同步重映射，控制延迟敏感。",
    )
    return y2 + 380


def draw_shared_table(draw: ImageDraw.ImageDraw, top: int) -> int:
    """ @brief 绘制"可共享 vs 不宜共享"的译码子系统分类表。
        @param draw PIL ImageDraw 实例。
        @param top 表格顶部 Y 坐标（上一模块底部的 Y 值）。
        @return 表格底部 Y 坐标，供后续模块使用。
        @note 四行五类：输入输出、控制、计算、存储，分别列出可共享与不宜共享的模块。
    """
    y0 = top + 105
    draw.text((90, y0 - 52), "统一译码子系统：可共享与不宜共享", font=font(32, True), fill=COL["ink"])
    x0 = 90
    widths = [320, 610, 610]
    row_h = 92
    rows = [
        ["类别", "可以共享", "不宜共享"],
        ["输入输出", "DMA、输入 LLR buffer、输出 hard bits FIFO、状态/中断寄存器", "codec-specific decoder input layout"],
        ["控制", "descriptor FIFO、配置寄存器、CRC checker wrapper", "Turbo iteration、LDPC layer、Polar path schedule"],
        ["计算", "饱和加法、比较器、CRC 多项式单元的封装", "Turbo SISO、LDPC CN/VN、Polar sorter/path memory"],
        ["存储", "顶层 SRAM allocator、bank 监控、trace buffer", "interleaver RAM、message memory、path copy memory"],
    ]
    for r, row in enumerate(rows):
        x = x0
        for c, cell in enumerate(row):
            b = (x, y0 + r * row_h, x + widths[c], y0 + (r + 1) * row_h)
            fill = COL["panel"] if r == 0 or c == 0 else "#FFFFFF"
            draw.rectangle(b, fill=fill, outline=COL["line"], width=1)
            is_head = r == 0 or c == 0
            draw_centered(draw, b, cell, 24, COL["ink"], is_head, 6)
            x += widths[c]
    return y0 + len(rows) * row_h


def draw_decision_matrix(draw: ImageDraw.ImageDraw, top: int) -> int:
    """ @brief 绘制 Turbo/LDPC/Polar 工程决策矩阵表，按维度横向对比三种译码器。
        @param draw PIL ImageDraw 实例。
        @param top 表格顶部 Y 坐标（上一模块底部的 Y 值）。
        @return 表格底部 Y 坐标，供后续模块使用。
        @throws RuntimeError 当与上一模块间距不足 90px 时抛出，防止视觉重叠。
        @note 六个维度：并行度、延迟、吞吐、面积/功耗、验证难度；每行高 84。
    """
    y0 = top + 105
    if y0 - top < 90:
        raise RuntimeError("shared-to-decision spacing too small")
    draw.text((90, y0 - 52), "工程决策矩阵", font=font(32, True), fill=COL["ink"])
    x0 = 90
    widths = [250, 430, 430, 430]
    row_h = 84  # TEXT_FIT_OK: cells use draw_centered() with wrap() and 24px text.
    rows = [
        ["维度", "Turbo", "LDPC", "Polar SCL"],
        ["并行度", "受 trellis 顺序依赖限制", "layer/edge/local index 并行友好", "路径并行受 sorter 限制"],
        ["延迟", "迭代次数放大最坏延迟", "高吞吐但轮数和 stall 影响尾延迟", "短块低延迟，排序关键路径敏感"],
        ["吞吐", "多 SISO 或多 CB 并行提升", "最适合宽并行数据业务", "控制块吞吐够用，非长块主力"],
        ["面积/功耗", "SISO 和外信息 RAM 主导", "CN/VN 阵列和 message RAM 主导", "path memory、sorter、copy network 主导"],
        ["验证难度", "外信息/交织/迭代早停", "bank conflict、message RMW、syndrome/CRC", "PM 排序、路径复制、CRC selector"],
    ]
    for r, row in enumerate(rows):
        x = x0
        for c, cell in enumerate(row):
            b = (x, y0 + r * row_h, x + widths[c], y0 + (r + 1) * row_h)
            fill = COL["panel"] if r == 0 or c == 0 else "#FFFFFF"
            draw.rectangle(b, fill=fill, outline=COL["line"], width=1)
            is_head = r == 0 or c == 0
            draw_centered(draw, b, cell, 24, COL["ink"], is_head, 5)
            x += widths[c]
    return y0 + len(rows) * row_h


def draw_footer(draw: ImageDraw.ImageDraw, top: int) -> None:
    """ @brief 绘制底部三列总结卡片：周期估算、验证重点、设计结论。
        @param draw PIL ImageDraw 实例。
        @param top 卡片区顶部 Y 坐标（上一模块底部的 Y 值）。
        @return 无返回值。
        @throws RuntimeError 当与上一模块间距不足 90px 时抛出。
        @note 每张卡片宽 540、高 260，琥珀色主题，含标题和正文两行。
    """
    y0 = top + 105
    if y0 - top < 90:
        raise RuntimeError("decision-to-footer spacing too small")
    boxes = [
        ("周期估算", "吞吐约等于 block_bits / cycles；Turbo cycles 随 2*SISO*iteration 增长，LDPC cycles 随 layers*iterations+stall 增长，Polar cycles 受 tree steps 和 sorter stages 影响。"),
        ("验证重点", "不要只比计算单元：必须同时 dump 地址、bank、message/path 状态、CRC/syndrome/PM、flush/reset 和 backpressure。"),
        ("设计结论", "LDPC 高吞吐友好来自稀疏图和 QC 规律；Polar SCL 延迟敏感来自 2L 候选排序和路径状态同步。"),
    ]
    x = 90
    for title, body in boxes:
        b = (x, y0, x + 540, y0 + 260)
        draw.rounded_rectangle(b, radius=16, fill=COL["amber_l"], outline=COL["amber"], width=2)
        draw_centered(draw, (b[0] + 20, b[1] + 18, b[2] - 20, b[1] + 60), title, 27, COL["ink"], True)
        draw_centered(draw, (b[0] + 24, b[1] + 68, b[2] - 24, b[3] - 20), body, 24, COL["ink"], False, 6)
        x += 590


def main(output: Path | None = None) -> None:
    """ @brief 脚本入口：生成 T11.4 Turbo/LDPC/Polar 硬件架构取舍对比图。
        @param output 自定义输出路径（可选），默认写入 OUT_PATH。
        @return 无返回值。
        @note 产出单张 PNG，1900x3040，含数据通路、共享子系统和决策矩阵三个模块。
    """
    out = output or OUT_PATH
    img = Image.new("RGB", (1900, 3040), COL["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "T11.4 Turbo / LDPC / Polar 硬件架构取舍", font=font(44, True), fill=COL["ink"])
    draw.text((70, 110), "对比并行度、存储访问、排序、迭代/列表深度、延迟、吞吐、功耗和验证风险。", font=font(26), fill=COL["muted"])
    bottom = draw_datapaths(draw)
    bottom = draw_shared_table(draw, bottom)
    bottom = draw_decision_matrix(draw, bottom)
    draw_footer(draw, bottom)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print(f"WROTE {out}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=None, help=f"output PNG path (default: {OUT_PATH})")
    args = parser.parse_args()
    main(output=args.output)
