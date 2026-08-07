"""
@file render_t3.2_trellis_termination_shuffle.py
@brief T3.2 Turbo 网格终止跨流重排 — 竖排版 SVG (宽框 + 双向自检)
@date 2026-07-24
"""

import sys, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def text_width_estimate(text: str, font_size: float) -> float:
    """
    @brief 估算文本渲染宽度 (像素)
    @param text       待估算的文本字符串
    @param font_size  字号（像素）
    @return           估算的像素宽度
    @note  中文字符 ≈ font_size px; ASCII/数字 ≈ font_size * 0.6 px; 上下标 ≈ font_size * 0.4 px
    """
    w = 0.0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch in (' ', '|', '/', '(', ')', '[', ']', '{', '}', '=', ',', '.', ':', ';'):
            w += font_size * 0.35
        elif ch == '<':
            # skip HTML tag like <sub> or <sup>
            j = text.index('>', i)
            i = j
        elif ord(ch) < 128:
            w += font_size * 0.6
        else:
            w += font_size
        i += 1
    return w


def render_svg(output_path: str = "") -> str:
    UP, UP_BG   = "#1565C0", "#E3F2FD"
    LO, LO_BG   = "#E65100", "#FFF3E0"
    DIS, DIS_BG = "#90A4AE", "#ECEFF1"

    # ====== 布局 ======
    row_h   = 72
    row_gap = 14
    group_gap = 22

    left_w  = 490
    right_w = 570
    mid_w   = 140
    margin  = 20
    svg_w   = margin * 2 + left_w + mid_w + right_w

    # 子格尺寸 (留足 padding: 文字宽 + 两侧各 16px 边距)
    sub_cw   = 130  # 步骤内小格宽
    sub_ch   = 26
    out_cw   = 170  # 输出内小格宽
    out_ch   = 26

    y_title      = 22
    y_subtitle   = y_title + 26
    y_steps_start = y_subtitle + 26
    y_outs_start  = y_steps_start + row_h

    y_bottom = max(
        y_steps_start + 3*(row_h+row_gap) + group_gap + 3*(row_h+row_gap) - row_gap,
        y_outs_start  + 4*(row_h+row_gap) - row_gap
    )
    y_legend = y_bottom + 28
    svg_h = y_legend + 24

    left_cx  = margin + left_w // 2
    mid_cx   = margin + left_w + mid_w // 2
    right_cx = margin + left_w + mid_w + right_w // 2

    steps = [
        ("步骤 1", True,  "x_K",      "z_K"),
        ("步骤 2", True,  "x_{K+1}",  "z_{K+1}"),
        ("步骤 3", True,  "x_{K+2}",  "z_{K+2}"),
        ("步骤 4", False, "x'_K",     "z'_K"),
        ("步骤 5", False, "x'_{K+1}", "z'_{K+1}"),
        ("步骤 6", False, "x'_{K+2}", "z'_{K+2}"),
    ]

    outs = [
        ("位置 K",   [("x_K",0),      ("z_K",0),      ("x_{K+1}",1)]),
        ("位置 K+1", [("z_{K+1}",1),  ("x_{K+2}",2),  ("z_{K+2}",2)]),
        ("位置 K+2", [("x'_K",3),     ("z'_K",3),     ("x'_{K+1}",4)]),
        ("位置 K+3", [("z'_{K+1}",4), ("x'_{K+2}",5), ("z'_{K+2}",5)]),
    ]

    def step_y(si):
        if si < 3:
            return y_steps_start + si * (row_h + row_gap)
        else:
            return y_steps_start + 3*(row_h+row_gap) + group_gap + (si-3)*(row_h+row_gap)

    def out_y(pi):
        return y_outs_start + pi * (row_h + row_gap)

    # ====== 预记录: 用于自检 ======
    check_rects = []   # (x1, y1, x2, y2, label)
    check_texts = []   # (x_center, y, estimated_width, font_size, text, zone)

    # ====== SVG 生成 ======
    L = []
    A = L.append

    A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">')
    A('<style>')
    A('  text { font-family: "DejaVu Sans", "Noto Sans", sans-serif; }')
    A('  .t   { font-size: 17px; font-weight: bold; fill: #263238; text-anchor: middle; }')
    A('  .st  { font-size: 13px; font-weight: bold; fill: #37474F; text-anchor: middle; }')
    A('  .lb  { font-size: 13px; font-weight: bold; text-anchor: middle; dominant-baseline: central; }')
    A('  .vl  { font-size: 13px; font-weight: bold; text-anchor: middle; dominant-baseline: central; }')
    A('  .lg  { font-size: 11px; fill: #37474F; }')
    A('</style>')

    # 标题
    A(f'<text x="{svg_w//2}" y="{y_title}" class="t">Turbo 网格终止: 6 步内部操作 → 跨流重排 → 4 个输出位置</text>')
    check_texts.append((svg_w//2, y_title, text_width_estimate("Turbo 网格终止: 6 步内部操作 → 跨流重排 → 4 个输出位置", 17), 17, "title", "T"))

    # 列标题
    A(f'<text x="{left_cx}" y="{y_subtitle}" class="st">6 步内部操作 (产生 12 个尾比特)</text>')
    check_texts.append((left_cx, y_subtitle, text_width_estimate("6 步内部操作 (产生 12 个尾比特)", 13), 13, "hdr-L", "L"))
    A(f'<text x="{mid_cx}" y="{y_subtitle}" class="st">重排</text>')
    check_texts.append((mid_cx, y_subtitle, text_width_estimate("重排", 13), 13, "hdr-M", "M"))
    A(f'<text x="{right_cx}" y="{y_subtitle}" class="st">4 个输出位置 (12 个槽位)</text>')
    check_texts.append((right_cx, y_subtitle, text_width_estimate("4 个输出位置 (12 个槽位)", 13), 13, "hdr-R", "R"))

    # ---- 左侧: 步骤格 ----
    for si, (lbl, is_up, xb, zb) in enumerate(steps):
        sy = step_y(si)
        clr = UP if is_up else LO
        bg  = UP_BG if is_up else LO_BG
        sx = margin

        check_rects.append((sx, sy, sx+left_w, sy+row_h, f"step-{si+1}"))

        A(f'<rect x="{sx}" y="{sy}" width="{left_w}" height="{row_h}" rx="6" fill="{bg}" stroke="{clr}" stroke-width="1.2"/>')

        enc = "上编码器" if is_up else "下编码器"
        title_text = f"{lbl} ({enc})"
        A(f'<text x="{sx+left_w//2}" y="{sy+row_h//2-15}" class="lb" fill="{clr}">{title_text}</text>')
        check_texts.append((sx+left_w//2, sy+row_h//2-15, text_width_estimate(title_text, 13), 13, f"step{si+1}-title", "L"))

        # 三列子格: 系统 | 校验 | 禁用
        sub_gap = 12
        sub_x0 = sx + (left_w - 3*sub_cw - 2*sub_gap) // 2
        sub_y  = sy + row_h//2 + 0
        for ci, (val, vclr, vbg, dash) in enumerate([
            (xb,  clr, bg, ""),
            (zb,  clr, bg, ""),
            ("(空)", DIS, DIS_BG, "3,2"),
        ]):
            cx = sub_x0 + ci * (sub_cw + sub_gap)
            check_rects.append((cx, sub_y, cx+sub_cw, sub_y+sub_ch, f"step{si+1}-sub{ci}"))
            sd = f'stroke-dasharray="{dash}"' if dash else ""
            A(f'<rect x="{cx}" y="{sub_y}" width="{sub_cw}" height="{sub_ch}" rx="4" fill="{vbg}" stroke="{vclr}" stroke-width="0.8" {sd}/>')
            label = "系统" if ci == 0 else ("校验" if ci == 1 else "禁用")
            sub_text = f"{label}: {val}"
            A(f'<text x="{cx+sub_cw//2}" y="{sub_y+sub_ch//2}" class="vl" fill="{vclr}">{sub_text}</text>')
            check_texts.append((cx+sub_cw//2, sub_y+sub_ch//2, text_width_estimate(sub_text, 13), 13, f"step{si+1}-sub{ci}-val", "L"))

    # ---- 分隔线 ----
    sep_y = y_steps_start + 3*(row_h+row_gap) + group_gap//2
    A(f'<line x1="{margin+4}" y1="{sep_y}" x2="{margin+left_w-4}" y2="{sep_y}" stroke="#B0BEC5" stroke-width="1" stroke-dasharray="4,4"/>')

    # ---- 右侧: 输出位置 ----
    stream_names = ["d^(0)", "d^(1)", "d^(2)"]
    stream_colors = ["#2E7D32", "#6A1B9A", "#C62828"]

    for pi, (pos_lbl, stream_vals) in enumerate(outs):
        oy = out_y(pi)
        ox = margin + left_w + mid_w

        check_rects.append((ox, oy, ox+right_w, oy+row_h, f"out-{pi}"))

        A(f'<rect x="{ox}" y="{oy}" width="{right_w}" height="{row_h}" rx="6" fill="#FAFAFA" stroke="#B0BEC5" stroke-width="1"/>')
        A(f'<text x="{ox+right_w//2}" y="{oy+row_h//2-15}" class="lb" fill="#37474F">{pos_lbl}</text>')
        check_texts.append((ox+right_w//2, oy+row_h//2-15, text_width_estimate(pos_lbl, 13), 13, f"out{pi}-title", "R"))

        out_gap = 14
        out_x0 = ox + (right_w - 3*out_cw - 2*out_gap) // 2
        out_y0 = oy + row_h//2 + 0
        for si, (val, src_step) in enumerate(stream_vals):
            is_up = src_step < 3
            vclr = UP if is_up else LO
            vbg  = UP_BG if is_up else LO_BG
            sc = stream_colors[si]
            sn = stream_names[si]

            vx = out_x0 + si * (out_cw + out_gap)
            vy = out_y0
            check_rects.append((vx, vy, vx+out_cw, vy+out_ch, f"out{pi}-s{si}"))

            A(f'<rect x="{vx}" y="{vy}" width="{out_cw}" height="{out_ch}" rx="4" fill="{vbg}" stroke="{vclr}" stroke-width="1"/>')
            out_text = f"{sn} = {val}"
            A(f'<text x="{vx+out_cw//2}" y="{vy+out_ch//2}" class="vl" fill="{vclr}">{out_text}</text>')
            check_texts.append((vx+out_cw//2, vy+out_ch//2, text_width_estimate(out_text, 13), 13, f"out{pi}-s{si}-val", "R"))

    # ---- 贝塞尔箭头 ----
    ax1 = margin + left_w + 6
    ax2 = margin + left_w + mid_w - 6
    step_to_out = {0: [0], 1: [0, 1], 2: [1], 3: [2], 4: [2, 3], 5: [3]}
    for si, dests in step_to_out.items():
        sy_c = step_y(si) + row_h // 2
        for di in dests:
            dy_c = out_y(di) + row_h // 2
            cx1 = ax1 + 35; cx2 = ax2 - 35
            path = f'M {ax1} {sy_c} C {cx1} {sy_c}, {cx2} {dy_c}, {ax2} {dy_c}'
            clr = UP if si < 3 else LO
            A(f'<path d="{path}" fill="none" stroke="{clr}" stroke-width="1.3" opacity="0.35"/>')
            A(f'<polygon points="{ax2},{dy_c} {ax2-7},{dy_c-4} {ax2-7},{dy_c+4}" fill="{clr}" opacity="0.35"/>')

    # ---- 图例 ----
    lg_y = y_legend
    lg_items = [
        (UP, UP_BG, "上编码器来源"),
        (LO, LO_BG, "下编码器来源"),
        (DIS, DIS_BG, "被禁用空槽"),
    ]
    lg_x0 = (svg_w - len(lg_items) * 200) // 2
    for i, (fg, bg, lbl) in enumerate(lg_items):
        lx = lg_x0 + i * 200
        A(f'<rect x="{lx}" y="{lg_y-7}" width="14" height="14" rx="3" fill="{bg}" stroke="{fg}" stroke-width="1"/>')
        A(f'<text x="{lx+18}" y="{lg_y+3}" class="lg" fill="{fg}">{lbl}</text>')
        check_texts.append((lx+18, lg_y+3, text_width_estimate(lbl, 11), 11, f"legend-{i}", "T"))

    A('</svg>')
    svg_text = "\n".join(L)

    # ============================================================
    # 双向自检: Y 间距 + 文字宽度 vs 容器宽度
    # ============================================================
    failed = []

    # 1) 分区 Y 间距检查
    texts_by_zone = {"L": [], "M": [], "R": []}
    for xc, y, tw, fs, label, zone in check_texts:
        if zone in texts_by_zone:
            texts_by_zone[zone].append((round(y), label))
    for zone, items in texts_by_zone.items():
        items.sort()
        for i in range(len(items)-1):
            g = items[i+1][0] - items[i][0]
            if 0 < g < 5:
                failed.append(f"Y 间距过小: {zone}区 {items[i][1]} ↔ {items[i+1][1]} gap={g}px")

    # 2) 文字宽度 + 边距 vs 容器宽度 (两侧各 ≥ 16px 留白)
    PAD = 16
    for xc, y, tw, fs, label, zone in check_texts:
        inside = False
        for rx1, ry1, rx2, ry2, rlabel in check_rects:
            if rx1 <= xc - tw/2 and xc + tw/2 <= rx2 and ry1 <= y - fs/2 and y + fs/2 <= ry2:
                inside = True
                rect_w = rx2 - rx1
                need_w = tw + PAD * 2
                if need_w > rect_w:
                    failed.append(f"缺边距: {label} 需{need_w:.0f}px(文{tw:.0f}+边{PAD*2}) > 容器{rlabel}宽{rect_w:.0f}px")
                break
        if not inside and zone != "T":
            pass

    # 3) 同层相邻文字水平交叠检查 (同一 Y 附近 ±3px, 同一 zone)
    for zone in ["L", "M", "R"]:
        items = [(round(y), xc, tw, label) for xc, y, tw, fs, label, z in check_texts if z == zone]
        items.sort()
        for i in range(len(items)):
            for j in range(i+1, len(items)):
                y1, x1, w1, l1 = items[i]
                y2, x2, w2, l2 = items[j]
                if abs(y2 - y1) < 6:
                    # 同一行, 检查水平交叠
                    x1l, x1r = x1 - w1/2, x1 + w1/2
                    x2l, x2r = x2 - w2/2, x2 + w2/2
                    if x1l < x2r and x2l < x1r:
                        overlap = min(x1r, x2r) - max(x1l, x2l)
                        if overlap > 2:
                            failed.append(f"文字水平交叠: {zone}区 {l1} ↔ {l2} overlap={overlap:.0f}px at y={y1}")

    if failed:
        for msg in failed:
            print(f"FAIL: {msg}", file=sys.stderr)
        raise SystemExit(f"自检失败 ({len(failed)} 项)")

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(svg_text)
        print(f"OK (width+XY 自检通过): {output_path}")
    return svg_text


if __name__ == "__main__":
    """@brief 脚本入口：生成 T3.2 网格终止跨流重排 SVG 并运行双向自检。
    @usage python3 tools/figures/render_t3.2_trellis_termination_shuffle.py
    @args  无参数（输出路径固定为 docs/L1_基础/assets/T3.2_trellis_termination_shuffle.svg）
    @env   无外部依赖（纯标准库，输出 SVG 文本）
    @exit_code 0 = 生成成功且自检通过；非 0 = 自检失败（SystemExit）"""
    render_svg(str(ROOT / "docs/L1_基础/assets/T3.2_trellis_termination_shuffle.svg"))
