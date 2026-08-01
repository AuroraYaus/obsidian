#!/usr/bin/env python3
""" @file render_t12_1_golden_model_layout.py
@brief 渲染 T12.1 黄金模型（Golden Model）项目布局图，展示从协议证据到可复现仿真产物的完整工程流。
@date 2025
"""

from __future__ import annotations

from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/L3/assets/T12.1_golden_model_project_layout.png"



TITLE = font(34, True)
HEAD = font(24, True)
TEXT = font(24)
SMALL = font(24)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:
    """ @brief 计算文本渲染后的宽高。
    @param draw PIL 绘图上下文。
    @param text 待测量的文本字符串。
    @param fnt PIL 字体对象。
    @return (宽度, 高度) px。
    """
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
    """ @brief 按单词边界自动换行，返回行列表。
    @param draw PIL 绘图上下文。
    @param text 待换行的英文字符串。
    @param fnt PIL 字体对象。
    @param width 最大行宽（px）。
    @return 换行后的行列表。
    """
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


def rounded_box(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: str, outline: str = "#263238") -> None:
    """ @brief 绘制统一风格的圆角矩形。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @param fill 填充色 hex 字符串。
    @param outline 描边色 hex 字符串，默认 "#263238"。
    @return None
    """
    draw.rounded_rectangle(xy, radius=14, fill=fill, outline=outline, width=2)


def centered_lines(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    body: list[str],
    fill: str,
) -> None:
    """ @brief 绘制带标题和正文列表的居中卡片，用于黄金模型工程流的各个阶段节点。
    @param draw PIL 绘图上下文。
    @param xy 矩形四边坐标 (x0, y0, x1, y1)。
    @param title 卡片标题。
    @param body 正文行列表。
    @param fill 填充色 hex 字符串。
    @return None
    """
    x0, y0, x1, y1 = xy
    rounded_box(draw, xy, fill)
    tw, th = text_size(draw, title, HEAD)
    y = y0 + 24
    draw.text(((x0 + x1) / 2, y + th / 2), title, font=HEAD, fill="#102027", anchor="mm")
    y += th + 18
    wrapped: list[str] = []
    for item in body:
        wrapped.extend(wrap(draw, item, SMALL, x1 - x0 - 48))
    line_h = max(text_size(draw, "Ag", SMALL)[1] + 10, 34)
    total = len(wrapped) * line_h
    y_start = max(y, y0 + (y1 - y0 + th) / 2 - total / 2)
    for i, line in enumerate(wrapped):
        draw.text(((x0 + x1) / 2, y_start + i * line_h + line_h / 2), line, font=SMALL, fill="#263238", anchor="mm")


def draw_centered_wrapped(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    fnt: ImageFont.ImageFont,
    fill: str,
    gap: int = 6,
) -> None:
    """ @brief 在矩形区域内居中绘制多行文本。
    @param draw PIL 绘图上下文。
    @param box 矩形四边坐标 (x0, y0, x1, y1)。
    @param lines 文本行列表。
    @param fnt PIL 字体对象。
    @param fill 文本颜色 hex 字符串。
    @param gap 行间距，默认 6px。
    @return None
    """
    heights = [text_size(draw, line, fnt)[1] for line in lines]
    total = sum(heights) + gap * max(0, len(lines) - 1)
    y = box[1] + (box[3] - box[1] - total) / 2
    cx = (box[0] + box[2]) / 2
    for line, height in zip(lines, heights):
        draw.text((cx, y + height / 2), line, font=fnt, fill=fill, anchor="mm")
        y += height + gap


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#37474f") -> None:
    """ @brief 绘制带三角形箭头的直线段，表示黄金模型工程流的数据传递方向。
    @param draw PIL 绘图上下文。
    @param start 线段起点坐标 (x, y)。
    @param end 线段终点坐标 (x, y)。
    @param color 线条与箭头填充色 hex 字符串，默认 "#37474f"。
    @return None
    """
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = math.hypot(vx, vy)
    if length == 0:
        return
    ux, uy = vx / length, vy / length
    head_len, head_w = 18, 9
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill=color, width=4)
    px, py = -uy, ux
    pts = [
        (ex, ey),
        (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
        (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
    ]
    draw.polygon(pts, fill=color)


def mid(rect: tuple[int, int, int, int], side: str, offset: int = 0) -> tuple[int, int]:
    """ @brief 计算矩形指定边的中点坐标（支持水平偏移），用于箭头端点定位。
    @param rect 矩形四边坐标 (x0, y0, x1, y1)。
    @param side 边标识："left"、"right"、"top"、"bottom"。
    @param offset 沿边方向的水平偏移量，默认 0。
    @return 中点坐标 (x, y)。
    @throws ValueError 当 side 不是有效值时抛出。
    """
    x0, y0, x1, y1 = rect
    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2
    if side == "left":
        return x0, cy + offset
    if side == "right":
        return x1, cy + offset
    if side == "top":
        return cx + offset, y0
    if side == "bottom":
        return cx + offset, y1
    raise ValueError(side)


def main() -> None:
    """ @brief 渲染 T12.1 黄金模型项目布局图，保存为 PNG 到 docs/L3/assets/。
    @note 该图展示从协议证据、配置模式、种子注册到仿真运行、产出扇出（模型/向量/日志/归档）
     的完整工程流，并附带布局间距断言和阅读顺序说明。
    @see render_t0_1_lte_nr_decoder_protocol_map.py 协议阅读地图。
    @return None
    """
    W, H = 2500, 1760
    img = Image.new("RGB", (W, H), "#f8faf7")
    draw = ImageDraw.Draw(img)
    draw.text((W / 2, 55), "T12.1 Python Golden Model Project Layout", font=TITLE, fill="#102027", anchor="mm")
    subtitle = "From 3GPP evidence and fixed seeds to reproducible decoder simulation artifacts"
    draw_centered_wrapped(draw, (110, 78, W - 110, 124), wrap(draw, subtitle, TEXT, W - 220), TEXT, "#455a64")

    boxes = {
        "protocol": (80, 160, 500, 390),
        "config": (540, 160, 960, 390),
        "seed": (1040, 160, 1460, 390),
        "runner": (875, 480, 1625, 700),
        "bus": (80, 800, 2420, 950),
        "models": (80, 1060, 500, 1340),
        "vectors": (590, 1060, 1010, 1340),
        "logs": (1490, 1060, 1910, 1340),
        "archive": (2000, 1060, 2420, 1340),
    }
    centered_lines(draw, boxes["protocol"], "Protocol Evidence", [
        "TS 36.212 and TS 38.212 sections, tables, formulas, local paths, extraction notes.",
    ], "#e3f2fd")
    centered_lines(draw, boxes["config"], "Config Schema", [
        "family, channel, block length, CRC, rate matching, HARQ/RV, algorithm knobs.",
    ], "#e8f5e9")
    centered_lines(draw, boxes["seed"], "Seed Registry", [
        "global seed, per-stage seed, vector id, rerun command, deterministic failure replay.",
    ], "#fff3e0")
    centered_lines(draw, boxes["runner"], "Simulation Runner", [
        "load config, build vectors, dispatch LTE Turbo / NR LDPC / NR Polar golden models, collect metrics.",
    ], "#ede7f6")
    centered_lines(draw, boxes["bus"], "Artifact Fanout", [
        "one run produces model results, reusable vectors, metrics/logs, and a reproducible evidence package.",
    ], "#eceff1")
    centered_lines(draw, boxes["models"], "Golden Models", [
        "lte_turbo, nr_ldpc, nr_polar packages share descriptor, status, error, debug contracts.",
    ], "#fce4ec")
    centered_lines(draw, boxes["vectors"], "Vector Store", [
        "input LLR, expected bits, protocol metadata, trace checkpoints, failure dumps.",
    ], "#e0f2f1")
    centered_lines(draw, boxes["logs"], "Metrics and Logs", [
        "BER/BLER, iteration count, CRC result, syndrome, path metric, timing proxy, CSV/JSONL.",
    ], "#f1f8e9")
    centered_lines(draw, boxes["archive"], "Evidence Archive", [
        "plots, CSV, configs, seeds, git hash, command line, audit notes for exact reproduction.",
    ], "#fffde7")

    arrow(draw, mid(boxes["protocol"], "right"), mid(boxes["config"], "left"))
    arrow(draw, mid(boxes["config"], "right"), mid(boxes["seed"], "left"))
    arrow(draw, mid(boxes["seed"], "bottom"), mid(boxes["runner"], "top"))
    arrow(draw, mid(boxes["runner"], "bottom"), mid(boxes["bus"], "top"))
    fanout_order = ("models", "vectors", "logs", "archive")
    fanout_offsets = [mid(boxes[key], "top")[0] - W // 2 for key in fanout_order]
    if fanout_offsets != [-960, -450, 450, 960]:
        raise AssertionError(f"fanout anchors must stay symmetric around center: {fanout_offsets}")
    if mid(boxes["seed"], "bottom")[0] != mid(boxes["runner"], "top")[0]:
        raise AssertionError("seed to runner must be a vertical centerline connection")
    if mid(boxes["runner"], "bottom")[0] != mid(boxes["bus"], "top")[0]:
        raise AssertionError("runner to artifact fanout must be a vertical centerline connection")
    for key, offset in zip(fanout_order, fanout_offsets):
        arrow(draw, mid(boxes["bus"], "bottom", offset), mid(boxes[key], "top"))

    note = (80, 1430, 2420, 1700)
    title_to_node_gap = boxes["protocol"][1] - 112
    flow_to_table_gap = boxes["models"][1] - boxes["bus"][3]
    bottom_margin = H - note[3]
    if title_to_node_gap < 36 or flow_to_table_gap < 80 or bottom_margin < 48:
        raise AssertionError(
            "T12.1 local spacing failed: "
            f"title_to_node_gap={title_to_node_gap}, "
            f"flow_to_table_gap={flow_to_table_gap}, bottom_margin={bottom_margin}"
        )

    rounded_box(draw, note, "#ffffff", "#607d8b")
    note_title = "Read Order and Engineering Checks"
    draw.text((W / 2, 1472), note_title, font=HEAD, fill="#102027", anchor="mm")
    note_lines = [
        "1. Protocol evidence and config schema define what the model is allowed to simulate.",
        "2. Seed registry and runner make every failed frame replayable.",
        "3. Vector store, logs and archive preserve enough evidence for bit-exact and RTL comparison later.",
        "4. Flow arrows use edge midpoints; Artifact Fanout outputs are symmetric around the bottom midpoint.",
    ]
    y = 1516
    for line in note_lines:
        draw.text((W / 2, y), line, font=SMALL, fill="#37474f", anchor="mm")
        y += 42

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"WROTE {OUT} {img.size}")


if __name__ == "__main__":
    main()
