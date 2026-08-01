#!/usr/bin/env python3
"""
@file    render_circular_buffer_decision3.py
@brief   生成"决策三：循环缓冲区统一速率匹配框架"的教学 SVG 图
@date    2026-07-25

画面左右两幅环形缓冲区图，展示同一个 circular buffer 在不同 E 值下
分别表现为打孔（puncturing）和重复（repetition）两种速率匹配策略。

@usage   python3 render_circular_buffer_decision3.py
@env     无特殊环境变量要求
@exit_code  0: 成功输出 SVG 文件
@see     [[T3.2_transport_code_block_filler_bits]] 决策三段落
"""

import math
import os

# ---------------------------------------------------------------------------
# 几何工具函数
# ---------------------------------------------------------------------------


def clock_xy(cx: float, cy: float, r: float, clock_deg: float) -> tuple[float, float]:
    """
    @brief  将钟面角度（0°=12 点方向，顺时针）转换为 SVG 画布坐标

    在 SVG 坐标系中 y 轴向下，因此钟面 0°（正上方）对应
    SVG 极坐标角度 -90°（即 -π/2）。

    @param cx        圆心 x
    @param cy        圆心 y
    @param r         半径
    @param clock_deg 钟面角度（度），0=12h，顺时针递增
    @return  (x, y) SVG 坐标
    """
    rad = math.radians(clock_deg - 90.0)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)


def ring_wedge(
    cx: float, cy: float, ro: float, ri: float,
    start_deg: float, end_deg: float,
) -> str:
    """
    @brief  生成环形楔形（donut wedge）的 SVG path d 字符串

    从 start_deg 到 end_deg 的环形段（钟面角度制），
    外侧弧沿顺时针，内侧弧沿逆时针返回。

    @param cx        圆心 x
    @param cy        圆心 y
    @param ro        外半径
    @param ri        内半径
    @param start_deg 起始钟面角度（度）
    @param end_deg   终止钟面角度（度）
    @return  SVG path 的 d 属性字符串
    """
    sweep = end_deg - start_deg
    large = 1 if sweep > 180.0 else 0

    x1o, y1o = clock_xy(cx, cy, ro, start_deg)
    x2o, y2o = clock_xy(cx, cy, ro, end_deg)
    x2i, y2i = clock_xy(cx, cy, ri, end_deg)
    x1i, y1i = clock_xy(cx, cy, ri, start_deg)

    return (
        f"M {x1o:.2f} {y1o:.2f} "
        f"A {ro:.2f} {ro:.2f} 0 {large} 1 {x2o:.2f} {y2o:.2f} "
        f"L {x2i:.2f} {y2i:.2f} "
        f"A {ri:.2f} {ri:.2f} 0 {large} 0 {x1i:.2f} {y1i:.2f} Z"
    )


def ring_arc(
    cx: float, cy: float, r: float,
    start_deg: float, end_deg: float,
) -> str:
    """
    @brief  生成环形上的一段圆弧 path 字符串（仅弧线，无填充）

    用于以描边方式绘制读取路径轨线。
    end_deg 可以超过 360° 以表达绕回行为。

    @param cx        圆心 x
    @param cy        圆心 y
    @param r         弧线半径
    @param start_deg 起始钟面角度（度）
    @param end_deg   终止钟面角度（度），允许 >360
    @return  SVG path 的 d 属性字符串
    """
    total = end_deg - start_deg
    if total <= 0:
        return ""

    segments: list[str] = []
    seg_start = start_deg
    remaining = total
    r_current = r

    while remaining > 0.1:
        seg_sweep = min(remaining, 180.0)
        seg_end = seg_start + seg_sweep
        large = 1 if seg_sweep > 180.0 else 0

        x1, y1 = clock_xy(cx, cy, r_current, seg_start)
        x2, y2 = clock_xy(cx, cy, r_current, seg_end)

        segments.append(
            f"M {x1:.2f} {y1:.2f} "
            f"A {r_current:.2f} {r_current:.2f} 0 {large} 1 {x2:.2f} {y2:.2f}"
        )

        seg_start = seg_end
        remaining -= seg_sweep
        if remaining > 0.1:
            r_current += 8.0  # 第二圈外扩以形成螺旋层次

    return "\n".join(segments)


# ---------------------------------------------------------------------------
# 单幅环形缓冲区的绘制函数
# ---------------------------------------------------------------------------


def draw_ring_scenario(
    svg: list[str],
    cx: float, cy: float,
    ro: float, ri: float,
    read_start: float,
    read_end: float,
    label: str,
    tag: str,
) -> None:
    """
    @brief  绘制一幅环形缓冲区图（含三色段、RV 标记、读取弧线、标题）

    @param svg         累积输出的 SVG 行列表
    @param cx          圆心 x
    @param cy          圆心 y
    @param ro          外半径
    @param ri          内半径
    @param read_start  读取起始钟面角度（度）
    @param read_end    读取终止钟面角度（度），可 >360
    @param label       场景中文名称
    @param tag         英文缩写标签
    """

    # ---- 三个数据段 ----
    SEGMENTS = [
        (0, 120, "#BBDEFB", "#1565C0", "系统流 v⁽⁰⁾", 60),
        (120, 240, "#FFE0B2", "#E65100", "校验流 v⁽¹⁾", 180),
        (240, 360, "#C8E6C9", "#2E7D32", "校验流 v⁽²⁾", 300),
    ]

    for s_deg, e_deg, fill, stroke, name, mid in SEGMENTS:
        svg.append(
            f'<path d="{ring_wedge(cx, cy, ro, ri, s_deg, e_deg)}"'
            f' fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
        )
        tx, ty = clock_xy(cx, cy, (ro + ri) / 2, mid)
        svg.append(
            f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="middle"'
            f' dominant-baseline="central" font-size="11"'
            f' fill="{stroke}">{name}</text>'
        )

    # ---- 环内文字: K_w = 3K_Π ----
    svg.append(
        f'<text x="{cx:.1f}" y="{cy-6:.1f}" text-anchor="middle"'
        f' font-size="13" font-style="italic" fill="#37474F">'
        f'K<tspan font-size="9" dy="2">w</tspan><tspan dy="-2">=3K</tspan>'
        f'<tspan font-size="9" dy="2">Π</tspan></text>'
    )

    # ---- 逆时针指示箭头（环外侧） ----
    for ang in [30, 150, 270]:
        ax, ay = clock_xy(cx, cy, ro + 22, ang)
        bx, by = clock_xy(cx, cy, ro + 22, ang + 15)
        svg.append(
            f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}"'
            f' stroke="#90A4AE" stroke-width="1.2"'
            f' marker-end="url(#arrowGray)"/>'
        )

    # ---- 2 个 RV 起点标记 ----
    RV_POSITIONS = [
        (0, "RV 0"),
        (120, "RV 1"),
    ]
    for rv_deg, rv_name in RV_POSITIONS:
        dx, dy = clock_xy(cx, cy, ro + 5, rv_deg)
        svg.append(
            f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="6"'
            f' fill="#EF5350" stroke="#B71C1C" stroke-width="1.5"/>'
        )
        lx, ly = clock_xy(cx, cy, ro + 28, rv_deg)
        svg.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle"'
            f' dominant-baseline="central" font-size="10"'
            f' fill="#B71C1C" font-weight="bold">{rv_name}</text>'
        )

    # ---- 读取轨迹弧线 ----
    svg.append(
        f'<path d="{ring_arc(cx, cy, ro + 4, read_start, read_end)}"'
        f' fill="none" stroke="#EF5350" stroke-width="3.5"'
        f' stroke-linecap="round"/>'
    )

    # 读取末端箭头
    end_clock = read_end % 360.0
    if end_clock < 0.01:
        end_clock = 360.0
    ex, ey = clock_xy(cx, cy, ro + 4, end_clock)
    tangent_deg = end_clock + 90.0
    trad = math.radians(tangent_deg - 90.0)
    tip_len = 10
    px = ex - tip_len * math.cos(trad)
    py = ey - tip_len * math.sin(trad)
    qx = ex + tip_len * math.cos(trad - 0.6)
    qy = ey + tip_len * math.sin(trad - 0.6)
    rx_pt = ex + tip_len * math.cos(trad + 0.6)
    ry_pt = ey + tip_len * math.sin(trad + 0.6)
    svg.append(
        f'<polygon points="{px:.1f},{py:.1f} {qx:.1f},{qy:.1f} {rx_pt:.1f},{ry_pt:.1f}"'
        f' fill="#EF5350"/>'
    )

    # ---- 读取路径标签 E ----
    mid_deg = (read_start + read_end) / 2.0
    mx, my = clock_xy(cx, cy, ro + 24, mid_deg)
    svg.append(
        f'<text x="{mx:.1f}" y="{my:.1f}" text-anchor="middle"'
        f' font-size="13" font-weight="bold" fill="#B71C1C"'
        f' font-style="italic">E</text>'
    )

    # ---- 场景标题 ----
    svg.append(
        f'<text x="{cx:.1f}" y="{cy + ro + 60:.1f}" text-anchor="middle"'
        f' font-size="14" font-weight="bold" fill="#263238">{label}</text>'
    )
    svg.append(
        f'<text x="{cx:.1f}" y="{cy + ro + 78:.1f}" text-anchor="middle"'
        f' font-size="11" fill="#546E7A">{tag}</text>'
    )


# ---------------------------------------------------------------------------
# 主入口
# ---------------------------------------------------------------------------


def main() -> None:
    """
    @brief  生成决策三 SVG 示意图并写入 assets 目录

    画面 = 左图（打孔 E &lt; K_w）+ 右图（重复 E &gt; K_w）

    @return  None
    @note   生成后应运行 Y 坐标扫描验证无交叠（≥8 px 间距）
    """
    W, H = 960, 560
    RO, RI = 175.0, 75.0

    SVG_HEAD = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<style>
  text {{ font-family: "DejaVu Sans", "Noto Sans", sans-serif; }}
  .legend-title {{ font-size: 13px; font-weight: bold; fill: #263238; }}
  .legend-item {{ font-size: 11px; fill: #37474F; }}
</style>'''

    lines: list[str] = [SVG_HEAD]

    # ---- 全局 defs (箭头标记) ----
    lines.append("<defs>")
    lines.append(
        '<marker id="arrowGray" markerWidth="8" markerHeight="6"'
        ' refX="8" refY="3" orient="auto">'
        '<path d="M0,0 L8,3 L0,6 Z" fill="#90A4AE"/></marker>'
    )
    lines.append("</defs>")

    # ---- 全局标题 ----
    lines.append(
        f'<text x="{W/2:.1f}" y="32" text-anchor="middle"'
        f' font-size="18" font-weight="bold" fill="#263238">'
        f'决策三：循环缓冲区 — 同一环形结构，两种速率匹配策略</text>'
    )
    lines.append(
        f'<text x="{W/2:.1f}" y="54" text-anchor="middle"'
        f' font-size="12" fill="#546E7A">'
        f'circular buffer w (长度 K<tspan font-size="9" dy="2">w</tspan>'
        f'<tspan dy="-2">=3K</tspan><tspan font-size="9" dy="2">Π</tspan>'
        f'<tspan dy="-2">) ，灰色箭头指示环形读取方向，红线表示从 RV 起点读取 E 个比特的轨迹</tspan></text>'
    )

    # ---- 左侧：打孔 ----
    draw_ring_scenario(
        lines, cx=260, cy=280, ro=RO, ri=RI,
        read_start=15, read_end=200,
        label="打孔 (Puncturing)",
        tag="E &lt; K_w  → 部分比特未发送（未被红线覆盖的环段即被打孔）",
    )

    # ---- 右侧：重复 ----
    draw_ring_scenario(
        lines, cx=700, cy=280, ro=RO, ri=RI,
        read_start=15, read_end=400,
        label="重复 (Repetition)",
        tag="E &gt; K_w  → 读取超过一圈后绕回开头，部分比特被重复发送",
    )

    # ---- 图例 ----
    LY = 488
    LX = 110
    GAP = 190
    LEGEND_ITEMS = [
        ("#BBDEFB", "#1565C0", "系统流 v⁽⁰⁾  (systematic)"),
        ("#FFE0B2", "#E65100", "校验流 v⁽¹⁾  (parity 1)"),
        ("#C8E6C9", "#2E7D32", "校验流 v⁽²⁾  (parity 2)"),
    ]
    for i, (fill, stroke, label_text) in enumerate(LEGEND_ITEMS):
        x0 = LX + i * GAP
        lines.append(
            f'<rect x="{x0}" y="{LY}" width="18" height="13" rx="2"'
            f' fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
        )
        lines.append(
            f'<text x="{x0+24}" y="{LY+7}" class="legend-item"'
            f' dominant-baseline="central">{label_text}</text>'
        )

    # RV 标记图例
    rv_x = LX + 3 * GAP + 20
    lines.append(
        f'<circle cx="{rv_x}" cy="{LY+6.5}" r="5"'
        f' fill="#EF5350" stroke="#B71C1C" stroke-width="1.2"/>'
    )
    lines.append(
        f'<text x="{rv_x+12}" y="{LY+7}" class="legend-item"'
        f' dominant-baseline="central">RV 起始位置 (k₀)</text>'
    )

    lines.append("</svg>")

    # ---- 写入文件 ----
    out_dir = os.path.join(
        os.path.dirname(__file__), "..", "..", "docs", "L1", "assets"
    )
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "T3.2_circular_buffer_decision3.svg")

    svg_text = "\n".join(lines)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_text)
    print(f"[OK] SVG written → {out_path}")
    print(f"     size: {len(svg_text):,} bytes, {len(lines)} lines")


if __name__ == "__main__":
    main()
