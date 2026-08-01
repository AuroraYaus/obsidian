"""
@file render_t3.2_circular_buffer_interleaving.py
@brief 生成 T3.2 bit collection 后 circular buffer w 的交错布局 SVG 图
@date 2026-07-23
@date 2026-07-25 修复 Y 层交叠，拉大行间距至 ≥8px，完善标签层次

展示三路 sub-block interleaver 输出 v^(0)/v^(1)/v^(2) 如何按
TS 36.212 §5.1.4.1.2 规则填入 circular buffer w:

  前半段: v^(0) 独占
  后半段: v^(1) 与 v^(2) 逐比特交替 (偶位置 v^(1), 奇位置 v^(2))

使用 K_Π=5 的具体例子，共 15 个位置，颜色区分三路来源。
"""

import sys, re


def render_svg(kpi: int = 5, output_path: str = "circular_buffer_interleaving.svg") -> str:
    """
    @brief 渲染 circular buffer bit collection 交错布局 SVG

    @param kpi         sub-block interleaver 输出长度 K_Π，默认 5
    @param output_path 输出 SVG 文件路径
    @return            生成的 SVG 文本
    """
    n_total = 3 * kpi  # K_w = 3 * K_Π

    # ----- 布局参数 (像素) -----
    cell_w = 48
    cell_h = 44
    gap = 2
    src_h = 22       # 源流格子高度
    margin_x = 60

    # 颜色
    C_SYS = "#1565C0";   C_SYS_BG = "#BBDEFB"
    C_P1  = "#E65100";   C_P1_BG  = "#FFE0B2"
    C_P2  = "#2E7D32";   C_P2_BG  = "#C8E6C9"
    C_DIV = "#37474F"
    C_ARR = "#90A4AE"

    # ----- Y 坐标：逐层计算，每层间距 ≥8px -----
    y_title       = 24     # 标题 (font 15, top~17, bot~31)
    y_src_label   = 48     # 源流标签 (font 12, top~42, bot~54)
    y_src_row0    = 68     # 源流第 0 行 (h=22, bot=90)
    y_src_row1    = 102    # 源流第 1 行 (h=22, bot=124)  ← gap: 102-90=12px
    y_arrow_text  = 146    # 箭头说明 (font 12, top~140, bot~152) ← gap: 140-124=16px
    y_arrow_top   = 162    # 箭头起点 ← gap: 162-152=10px
    y_arrow_bot   = 198    # 箭头终点 (36px 跨度)
    y_target_label = 212   # 目标标签 (font 12, top~206) ← gap: 206-198=8px
    y_target_cell  = 230   # 目标格子 (h=44, bot=274) ← gap: 230-218=12px
    y_target_idx   = 290   # w 下标 (font 10, top~285) ← gap: 285-274=11px
    y_total        = 312   # 总长 (font 12, top~306) ← gap: 306-295=11px
    y_legend       = 338   # 图例
    svg_h          = 370

    # ----- 预计算 -----
    svg_w = margin_x * 2 + n_total * (cell_w + gap) - gap

    x_sys_mid = margin_x + kpi * (cell_w + gap) // 2
    x_par_mid = margin_x + kpi * (cell_w + gap) + (2 * kpi * (cell_w + gap)) // 2
    sep_x = margin_x + kpi * (cell_w + gap) - gap // 2  # 系统/parity 分隔线

    # 每个 cell: (w 位置, 源下标, 背景色, 前景色, 流短标签)
    cells = []
    for i in range(n_total):
        if i < kpi:
            cells.append((i, i, C_SYS_BG, C_SYS, "v⁰"))
        else:
            offset = i - kpi
            if offset % 2 == 0:
                cells.append((i, offset // 2, C_P1_BG, C_P1, "v¹"))
            else:
                cells.append((i, offset // 2, C_P2_BG, C_P2, "v²"))

    # ============================================================
    # SVG 生成
    # ============================================================
    L = []
    def add(s):
        L.append(s)

    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">')
    add('<style>')
    add('  text { font-family: "DejaVu Sans", "Noto Sans", sans-serif; }')
    add('  .title    { font-size: 15px; font-weight: bold; fill: #263238; }')
    add('  .subtitle { font-size: 12px; fill: #546E7A; }')
    add('  .small    { font-size: 10px; fill: #78909C; text-anchor: middle; }')
    add('  .cell-txt { font-size: 11px; text-anchor: middle; dominant-baseline: central; }')
    add('  .legend   { font-size: 11px; fill: #37474F; }')
    add('</style>')

    # ---- 标题 ----
    add(f'<text x="{svg_w//2}" y="{y_title}" class="title" text-anchor="middle">')
    add(f'  circular buffer w 的交错写入  (K<sub>Π</sub>={kpi},  K<sub>w</sub>={n_total})')
    add(f'</text>')

    # ---- 源流标签 ----
    add(f'<text x="{x_sys_mid}" y="{y_src_label}" class="subtitle" text-anchor="middle">系统流 v<sup>(0)</sup></text>')
    add(f'<text x="{x_par_mid}" y="{y_src_label}" class="subtitle" text-anchor="middle">parity 流 v<sup>(1)</sup> / v<sup>(2)</sup>  逐比特交替</text>')

    # ---- 源流格子 (两行) ----
    for row_i, row_y in enumerate([y_src_row0, y_src_row1]):
        for ci, (w_idx, src_idx, bg, fg, short) in enumerate(cells):
            x = margin_x + ci * (cell_w + gap)
            if row_i == 0:
                txt = short  # v⁰ / v¹ / v²
            else:
                txt = str(src_idx)  # 源下标 0~4
            add(f'<rect x="{x}" y="{row_y}" width="{cell_w}" height="{src_h}" rx="3" fill="{bg}" stroke="{fg}" stroke-width="1.2"/>')
            add(f'<text x="{x + cell_w//2}" y="{row_y + src_h//2}" class="cell-txt" fill="{fg}">{txt}</text>')

    # ---- 箭头区域说明文字 ----
    add(f'<text x="{svg_w//2}" y="{y_arrow_text}" class="subtitle" text-anchor="middle">')
    add('  ↓ sub-block interleaving 后，按 bit collection 规则写入 ↓')
    add('</text>')

    # ---- 虚线箭头 (每个 cell 一根) ----
    for ci in range(n_total):
        x = margin_x + ci * (cell_w + gap) + cell_w // 2
        add(f'<line x1="{x}" y1="{y_arrow_top}" x2="{x}" y2="{y_arrow_bot}" stroke="{C_ARR}" stroke-width="1" stroke-dasharray="3,2"/>')

    # ---- 分隔标签 (目标格子上方) ----
    add(f'<text x="{x_sys_mid}" y="{y_target_label}" class="subtitle" text-anchor="middle">[0, K<sub>Π</sub>−1]</text>')
    add(f'<text x="{x_par_mid}" y="{y_target_label}" class="subtitle" text-anchor="middle">[K<sub>Π</sub>, 3K<sub>Π</sub>−1]</text>')

    # ---- 分隔虚线 (从标签区贯穿至下标区) ----
    add(f'<line x1="{sep_x}" y1="{y_target_label - 2}" x2="{sep_x}" y2="{y_target_idx + 12}" stroke="{C_DIV}" stroke-width="1.8" stroke-dasharray="6,3"/>')

    # ---- 目标 circular buffer w 格子 ----
    for ci, (w_idx, src_idx, bg, fg, short) in enumerate(cells):
        x = margin_x + ci * (cell_w + gap)
        y = y_target_cell
        add(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" rx="4" fill="{bg}" stroke="{fg}" stroke-width="1.5"/>')
        # 流类型 (加粗)
        add(f'<text x="{x + cell_w//2}" y="{y + cell_h//2 - 6}" class="cell-txt" fill="{fg}" font-weight="bold">{short}</text>')
        # 源下标
        add(f'<text x="{x + cell_w//2}" y="{y + cell_h//2 + 9}" class="small">_{src_idx}</text>')
        # w 位置编号
        add(f'<text x="{x + cell_w//2}" y="{y_target_idx}" class="small">w<sub>{w_idx}</sub></text>')

    # ---- 底部总长 ----
    add(f'<text x="{svg_w//2}" y="{y_total}" class="subtitle" text-anchor="middle">w 总长 K<sub>w</sub> = 3 × K<sub>Π</sub> = {n_total}</text>')

    # ---- 图例 ----
    legends = [
        ("v⁽⁰⁾  系统流",    C_SYS_BG, C_SYS),
        ("v⁽¹⁾  parity 1", C_P1_BG,  C_P1),
        ("v⁽²⁾  parity 2", C_P2_BG,  C_P2),
    ]
    for i, (lbl, bg, fg) in enumerate(legends):
        lx = margin_x + i * 175
        add(f'<rect x="{lx}" y="{y_legend}" width="14" height="14" rx="3" fill="{bg}" stroke="{fg}" stroke-width="1.2"/>')
        add(f'<text x="{lx + 18}" y="{y_legend + 11}" class="legend" fill="{fg}">{lbl}</text>')

    add('</svg>')
    svg_text = "\n".join(L)

    # ---- 自检：所有相邻 text Y 层间距 ≥8px ----
    text_ys = sorted({round(float(m.group(1))) for m in re.finditer(r'<text[^>]*y="([\d.]+)"', svg_text)})
    fail = False
    for i in range(len(text_ys)-1):
        d = text_ys[i+1] - text_ys[i]
        if 0 < d < 8:
            print(f"FAIL: Y交叠 y={text_ys[i]} ↔ y={text_ys[i+1]} gap={d}px", file=sys.stderr)
            fail = True
    if fail:
        raise SystemExit("自检失败, 拒绝输出")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_text)
    return svg_text


if __name__ == "__main__":
    render_svg(kpi=5, output_path="/home/yys/AGENT/3gpp/docs/L1/assets/T3.2_circular_buffer_interleaving.svg")
    print("SVG generated: T3.2_circular_buffer_interleaving.svg")
