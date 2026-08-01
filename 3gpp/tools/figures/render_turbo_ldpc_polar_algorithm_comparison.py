#!/usr/bin/env python3
""" @file render_turbo_ldpc_polar_algorithm_comparison.py
@brief 渲染T11.1 Turbo/LDPC/Polar三大译码算法对比图 —— 展示三类译码器的图模型、软信息语义、停止条件和硬件瓶颈差异
@date 2025 """

from __future__ import annotations

from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font
except ModuleNotFoundError:
    from figure_text_fit import font



ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T11.1_Turbo_LDPC_Polar_algorithm_comparison.png"

COL = {
    "bg": "#FFFFFF",
    "ink": "#17212F",
    "muted": "#5C6878",
    "line": "#95A6B8",
    "turbo": "#B55A30",
    "turbo_fill": "#FFF0E7",
    "ldpc": "#247A58",
    "ldpc_fill": "#E8F6EF",
    "polar": "#2457A6",
    "polar_fill": "#EAF1FB",
    "panel": "#F7F9FC",
    "note": "#FFF8E8",
}



def text_center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, size: int, fill: str, bold: bool = True) -> None:
    """ @brief 在矩形区域内居中绘制单行文本的快捷方法，适用于 pill 标签等简单场景
    @param draw PIL ImageDraw 绘图上下文
    @param box (x0, y0, x1, y1) 目标矩形区域
    @param text 待绘制的文本字符串
    @param size 字体大小（像素）
    @param fill 文本颜色
    @param bold 是否加粗，默认 True
    @return None
    @note 使用 anchor="mm" 实现精确居中 """
    draw.text(((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), text, font=font(size, bold), fill=fill, anchor="mm")


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    size: int,
    fill: str,
    bold: bool = True,
    gap: int = 5,
) -> None:
    """ @brief 在指定矩形区域内居中绘制多行文本，自动计算垂直起始位置
    @param draw PIL ImageDraw 绘图上下文
    @param box (x0, y0, x1, y1) 目标矩形区域
    @param lines 待绘制的文本行列表
    @param size 字体大小（像素）
    @param fill 文本颜色
    @param bold 是否加粗，默认 True
    @param gap 行间距像素值，默认 5
    @return None """
    fnt = font(size, bold)
    heights = [draw.textbbox((0, 0), line, font=fnt)[3] - draw.textbbox((0, 0), line, font=fnt)[1] for line in lines]
    total = sum(heights) + gap * (len(lines) - 1)
    y = (box[1] + box[3] - total) / 2
    cx = (box[0] + box[2]) / 2
    for line, h in zip(lines, heights):
        draw.text((cx, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + gap


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, color: str, fill: str) -> None:
    """ @brief 绘制一个带标题和圆角边框的算法面板，作为三种译码器的统一容器框架
    @param draw PIL ImageDraw 绘图上下文
    @param box (x0, y0, x1, y1) 面板矩形区域
    @param title 面板左上角标题文本
    @param color 边框颜色和标题文本颜色
    @param fill 面板背景填充颜色
    @return None
    @note 三种算法面板使用相同框架但不同配色，以区分 Turbo/LDPC/Polar """
    draw.rounded_rectangle(box, radius=16, fill=fill, outline=color, width=2)
    draw.text((box[0] + 24, box[1] + 20), title, font=font(24, True), fill=color)


def pill(draw: ImageDraw.ImageDraw, center: tuple[int, int], text: str, fill: str, outline: str) -> tuple[int, int, int, int]:
    """ @brief 绘制一个胶囊形（两端半圆）的节点标签，用于表示译码器图中的状态/变量/校验节点
    @param draw PIL ImageDraw 绘图上下文
    @param center (cx, cy) 胶囊中心坐标
    @param text 标签文本
    @param fill 胶囊背景填充颜色
    @param outline 胶囊边框颜色
    @return (x0, y0, x1, y1) 胶囊的边界框，用于后续连线计算
    @note 高度取半径的2倍实现胶囊形状；返回边界框供 connect_arrow/connect_line 使用 """
    f = font(24, True)
    tb = draw.textbbox((0, 0), text, font=f)
    w = tb[2] - tb[0] + 34
    h = tb[3] - tb[1] + 26
    box = (center[0] - w // 2, center[1] - h // 2, center[0] + w // 2, center[1] + h // 2)
    draw.rounded_rectangle(box, radius=h // 2, fill=fill, outline=outline, width=2)
    draw.text(center, text, font=f, fill=COL["ink"], anchor="mm")
    return box


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str = "#61758A",
    width: int = 3,
) -> None:
    """ @brief 绘制带箭头尖端的直线段，用于表示译码图中的数据流/消息传递方向
    @param draw PIL ImageDraw 绘图上下文
    @param start (x, y) 线段起点坐标
    @param end (x, y) 线段终点坐标（箭头尖端位置）
    @param color 线条和箭头填充颜色，默认 "#61758A"
    @param width 线条宽度像素值，默认 3
    @return None
    @note 零长度线段静默返回；使用三角函数计算箭头三角形顶点 """
    x0, y0 = start
    x1, y1 = end
    length = math.hypot(x1 - x0, y1 - y0)
    if length < 1:
        return
    ux = (x1 - x0) / length
    uy = (y1 - y0) / length
    head_len = 8 if width <= 2 else 12
    head_w = 5 if width <= 2 else 8
    line_end = (x1 - head_len * ux, y1 - head_len * uy)
    draw.line((start, line_end), fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    back_x = x1 - head_len * math.cos(angle)
    back_y = y1 - head_len * math.sin(angle)
    perp_x = head_w * math.sin(angle)
    perp_y = -head_w * math.cos(angle)
    draw.polygon(
        [
            (x1, y1),
            (back_x + perp_x, back_y + perp_y),
            (back_x - perp_x, back_y - perp_y),
        ],
        fill=color,
    )


def center(box: tuple[int, int, int, int]) -> tuple[float, float]:
    """ @brief 计算矩形的几何中心坐标
    @param box (x0, y0, x1, y1) 矩形区域
    @return (cx, cy) 矩形中心点坐标
    @note 用于 boundary_point 计算方向向量 """
    return ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2)


def boundary_point(box: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    """ @brief 计算矩形边界上朝向目标点的最近交点，用于精确的盒间连线
    @param box (x0, y0, x1, y1) 矩形区域
    @param toward (tx, ty) 连线要朝向的目标点坐标
    @return (x, y) 矩形边界上的交点坐标
    @note 从矩形中心向目标方向发射射线，返回射线与矩形边界的交点；比按边方向取点更通用 """
    cx, cy = center(box)
    dx = toward[0] - cx
    dy = toward[1] - cy
    if dx == 0 and dy == 0:
        return cx, cy
    half_w = (box[2] - box[0]) / 2
    half_h = (box[3] - box[1]) / 2
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return (cx + dx / scale, cy + dy / scale)


def connect_arrow(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str, width: int = 2) -> None:
    """ @brief 在两个矩形盒子之间绘制带箭头的连线，自动计算边界交点和箭头方向
    @param draw PIL ImageDraw 绘图上下文
    @param src (x0, y0, x1, y1) 源矩形盒子
    @param dst (x0, y0, x1, y1) 目标矩形盒子
    @param color 线条和箭头颜色
    @param width 线条宽度像素值，默认 2
    @return None
    @note 自动调用 boundary_point 计算起止边界点，箭头指向 dst """
    s = boundary_point(src, center(dst))
    e = boundary_point(dst, center(src))
    arrow(draw, s, e, color, width)


def connect_line(draw: ImageDraw.ImageDraw, src: tuple[int, int, int, int], dst: tuple[int, int, int, int], color: str, width: int = 2) -> None:
    """ @brief 在两个矩形盒子之间绘制无箭头的直线连接，用于表示双向或无向关系
    @param draw PIL ImageDraw 绘图上下文
    @param src (x0, y0, x1, y1) 源矩形盒子
    @param dst (x0, y0, x1, y1) 目标矩形盒子
    @param color 线条颜色
    @param width 线条宽度像素值，默认 2
    @return None
    @note 与 connect_arrow 的区别：不绘制箭头，用于 Tanner 图边等双向关系 """
    s = boundary_point(src, center(dst))
    e = boundary_point(dst, center(src))
    draw.line((s, e), fill=color, width=width)


def right_mid(box: tuple[int, int, int, int]) -> tuple[int, int]:
    """ @brief 获取矩形右边中点坐标，用于水平连接时的快捷起止点
    @param box (x0, y0, x1, y1) 矩形区域
    @return (x1, mid_y) 右边中点坐标
    @note 仅当需要精确右边中点时使用，避免手动计算 """
    return (box[2], (box[1] + box[3]) // 2)


def left_mid(box: tuple[int, int, int, int]) -> tuple[int, int]:
    """ @brief 获取矩形左边中点坐标，用于水平连接时的快捷起止点
    @param box (x0, y0, x1, y1) 矩形区域
    @return (x0, mid_y) 左边中点坐标
    @note 仅当需要精确左边中点时使用 """
    return (box[0], (box[1] + box[3]) // 2)


def draw_turbo(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    """ @brief 绘制 LTE Turbo 译码器的 trellis + SISO 迭代可视化面板
    @param draw PIL ImageDraw 绘图上下文
    @param box (x0, y0, x1, y1) 面板矩形区域
    @return None
    @note 展示两层状态节点（S0-S3）和层间连线，底部注释软信息语义、瓶颈和迭代延迟 """
    panel(draw, box, "LTE Turbo: trellis + SISO iteration", COL["turbo"], COL["turbo_fill"])
    y = box[1] + 92
    states = [pill(draw, (box[0] + 84 + i * 95, y), f"S{i}", "#FFFFFF", COL["turbo"]) for i in range(4)]
    states2 = [pill(draw, (box[0] + 84 + i * 95, y + 82), f"S{i}", "#FFFFFF", COL["turbo"]) for i in range(4)]
    for a, b in zip(states, states[1:]):
        connect_arrow(draw, a, b, COL["turbo"], 2)
    for a, b in zip(states2, states2[1:]):
        connect_arrow(draw, a, b, COL["turbo"], 2)
    for a, b in zip(states, states2):
        connect_line(draw, a, b, COL["line"], 2)
    draw_centered_lines(
        draw,
        (box[0] + 30, box[1] + 270, box[2] - 30, box[3] - 42),
        ["Soft info semantics: channel LLR", "+ extrinsic information", "Bottleneck: forward/backward metric, interleaver address, iteration latency"],
        24,
        COL["ink"],
        True,
        10,
    )


def draw_ldpc(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    """ @brief 绘制 NR LDPC 译码器的 Tanner graph + 消息传递可视化面板
    @param draw PIL ImageDraw 绘图上下文
    @param box (x0, y0, x1, y1) 面板矩形区域
    @return None
    @note 展示变量节点（v0-v3）和校验节点（c0-c2）之间的稀疏连接关系，底部注释消息内存、bank conflict 和 layered schedule 瓶颈 """
    panel(draw, box, "NR LDPC: Tanner graph + message passing", COL["ldpc"], COL["ldpc_fill"])
    v_y = box[1] + 116
    c_y = box[1] + 220
    var_centers = [(box[0] + 84 + i * 82, v_y) for i in range(4)]
    check_centers = [(box[0] + 130 + i * 120, c_y) for i in range(3)]
    vars_ = [pill(draw, pt, f"v{i}", "#FFFFFF", COL["ldpc"]) for i, pt in enumerate(var_centers)]
    checks = [pill(draw, pt, f"c{i}", "#FFFFFF", COL["ldpc"]) for i, pt in enumerate(check_centers)]
    edges = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (0, 2)]
    for vi, ci in edges:
        connect_line(draw, vars_[vi], checks[ci], COL["line"], 2)
    for i, pt in enumerate(var_centers):
        vars_[i] = pill(draw, pt, f"v{i}", "#FFFFFF", COL["ldpc"])
    for i, pt in enumerate(check_centers):
        checks[i] = pill(draw, pt, f"c{i}", "#FFFFFF", COL["ldpc"])
    draw_centered_lines(
        draw,
        (box[0] + 30, box[1] + 292, box[2] - 30, box[3] - 42),
        ["Soft info semantics: VN/CN messages", "+ posterior LLR", "Bottleneck: message memory / bank conflict", "layered schedule"],
        24,
        COL["ink"],
        True,
        8,
    )


def draw_polar(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    """ @brief 绘制 NR Polar 译码器的 decoding tree + SCL path 可视化面板
    @param draw PIL ImageDraw 绘图上下文
    @param box (x0, y0, x1, y1) 面板矩形区域
    @return None
    @note 展示从根节点到叶节点（u0-u3，标记 F=frozen/I=info）的二叉树结构，底部注释路径度量、frozen 约束、sorter 和部分和瓶颈 """
    panel(draw, box, "NR Polar: decoding tree + SCL path", COL["polar"], COL["polar_fill"])
    root = pill(draw, (box[0] + 130, box[1] + 155), "root", "#FFFFFF", COL["polar"])
    l1 = pill(draw, (box[0] + 270, box[1] + 108), "f", "#FFFFFF", COL["polar"])
    r1 = pill(draw, (box[0] + 270, box[1] + 202), "g", "#FFFFFF", COL["polar"])
    leafs = [
        pill(draw, (box[0] + 405, box[1] + 78), "u0 F", "#FFFFFF", COL["polar"]),
        pill(draw, (box[0] + 405, box[1] + 135), "u1 F", "#FFFFFF", COL["polar"]),
        pill(draw, (box[0] + 405, box[1] + 192), "u2 I", "#FFFFFF", COL["polar"]),
        pill(draw, (box[0] + 405, box[1] + 249), "u3 I", "#FFFFFF", COL["polar"]),
    ]
    connect_arrow(draw, root, l1, COL["polar"], 2)
    connect_arrow(draw, root, r1, COL["polar"], 2)
    connect_arrow(draw, l1, leafs[0], COL["polar"], 2)
    connect_arrow(draw, l1, leafs[1], COL["polar"], 2)
    connect_arrow(draw, r1, leafs[2], COL["polar"], 2)
    connect_arrow(draw, r1, leafs[3], COL["polar"], 2)
    draw_centered_lines(
        draw,
        (box[0] + 30, box[1] + 292, box[2] - 30, box[3] - 42),
        ["Soft info semantics: path metric", "+ frozen constraint + CRC", "Bottleneck: sorter, path memory", "partial sum, low latency"],
        24,
        COL["ink"],
        True,
        8,
    )


def main() -> None:
    """ @brief 渲染T11.1三大译码算法对比图的主入口
    @note 生成的图片并排展示三种译码器的图模型：LTE Turbo（trellis+SISO迭代）、NR LDPC（Tanner图+消息传递）、NR Polar（译码树+SCL路径）。
    下半部分为五维对比矩阵（协议主场/核心行为/停止边界/并行性/硬件瓶颈）和工程结论。
    包含布局间距的自检断言。
    输出至 docs/L2/assets/T11.1_Turbo_LDPC_Polar_algorithm_comparison.png
    @see render_t15_1_decoder_testbench_architecture.py """
    img = Image.new("RGB", (1900, 1600), COL["bg"])
    draw = ImageDraw.Draw(img)
    draw.text((70, 42), "T11.1 Turbo, LDPC, Polar Decoder Algorithm Comparison", font=font(34, True), fill=COL["ink"])
    draw.text((70, 96), "Same LLR input, but three decoder families differ in graph model, soft info semantics, stop criteria, and hardware bottleneck.", font=font(24), fill=COL["muted"])

    boxes = [(70, 165, 615, 615), (680, 165, 1225, 615), (1290, 165, 1835, 615)]
    draw_turbo(draw, boxes[0])
    draw_ldpc(draw, boxes[1])
    draw_polar(draw, boxes[2])

    # Comparison matrix.
    x0, y0 = 100, 720
    widths = [250, 390, 390, 390]
    row_h = 78  # TEXT_FIT_OK: comparison cells use centered 24px controlled labels.
    headers = ["Dimension", "LTE Turbo", "NR LDPC", "NR Polar"]
    rows = [
        ["Protocol Home", "LTE data channel", "NR data channel", "NR control channel"],
        ["Core Behavior", "two SISOs exchange extrinsic info", "VN/CN message iteration", "SC/SCL path search"],
        ["Stop Boundary", "iteration count + CRC", "syndrome/iteration + CRC", "CRC/RNTI aided select"],
        ["Parallelism", "limited by trellis order and interleaver", "QC/layered high parallelism", "path sorting limits low latency"],
        ["HW Bottleneck", "alpha/beta/extrinsic RAM", "message memory/bank", "sorter/path memory"],
    ]
    cx = x0
    for h, w in zip(headers, widths):
        cell_box = (cx, y0, cx + w, y0 + row_h)
        draw.rectangle(cell_box, fill=COL["panel"], outline=COL["line"])
        draw_centered_lines(draw, cell_box, [h], 24, COL["ink"], True)
        cx += w
    for r, row in enumerate(rows):
        cy = y0 + row_h * (r + 1)
        cx = x0
        for cell, w in zip(row, widths):
            cell_box = (cx, cy, cx + w, cy + row_h)
            draw.rectangle(cell_box, fill="#FFFFFF", outline=COL["line"])
            draw_centered_lines(draw, cell_box, [cell], 24, COL["ink"], True)
            cx += w

    note = (100, 1290, 1800, 1490)
    matrix_bottom = y0 + row_h * (len(rows) + 1)
    matrix_to_note_gap = note[1] - matrix_bottom
    bottom_margin = 1600 - note[3]
    assert matrix_to_note_gap >= 80
    assert bottom_margin >= 80
    draw.rounded_rectangle(note, radius=14, fill=COL["note"], outline="#D4B15F", width=2)
    draw.text((note[0] + 24, note[1] + 24), "Engineering conclusion", font=font(24, True), fill=COL["ink"])
    draw.text((note[0] + 24, note[1] + 78), "It is meaningless to say one code family is better without specifying protocol generation, block length, channel type, throughput target, and hardware resources.", font=font(24, True), fill=COL["ink"])
    draw.text((note[0] + 24, note[1] + 124), "Large data blocks prioritize throughput and parallelism; short control blocks prioritize low latency, misdetection boundaries, and path selection.", font=font(24, True), fill=COL["ink"])

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
