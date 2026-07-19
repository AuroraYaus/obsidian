#!/usr/bin/env python3
"""Render a rebuilt teaching figure for TS 36.212 Figure 5.1.3-2."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T6.3_TS36.212_Figure_5.1.3-2_turbo_encoder_rebuild.png"

INK = "#102033"
MUTED = "#526579"
LINE = "#93A6BA"
BLUE = "#2F80ED"
GREEN = "#00A676"
ORANGE = "#F2994A"
PURPLE = "#7B61FF"
RED = "#D94C4C"
PANEL = "#F7FAFD"
PALE_BLUE = "#EAF3FF"
PALE_GREEN = "#E9F8F1"
PALE_ORANGE = "#FFF4E7"
PALE_PURPLE = "#F2EFFF"



def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 7,
) -> int:
    x, y = xy
    lines = fit_wrap_text(draw, text, fnt, max_width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def wrapped_lines(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    return fit_wrap_text(draw, text, fnt, max_width)


def text_height(draw: ImageDraw.ImageDraw, lines: list[str], fnt: ImageFont.FreeTypeFont, gap: int) -> int:
    heights = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=fnt)
        heights.append(bbox[3] - bbox[1])
    return sum(heights) + gap * max(len(lines) - 1, 0)


def draw_centered_multiline(
    draw: ImageDraw.ImageDraw,
    box_xy: tuple[int, int, int, int],
    text: str | list[str],
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 6,
) -> None:
    if isinstance(text, list):
        lines: list[str] = []
        for item in text:
            lines.extend(wrapped_lines(draw, item, fnt, max_width))
    else:
        lines = wrapped_lines(draw, text, fnt, max_width)
    total = text_height(draw, lines, fnt, line_gap)
    x = (box_xy[0] + box_xy[2]) / 2
    y = (box_xy[1] + box_xy[3] - total) / 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=fnt)
        h = bbox[3] - bbox[1]
        draw.text((x, y + h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += h + line_gap


def center_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 1
    draw.text((x, y), text, font=fnt, fill=fill)


def center(box_xy: tuple[int, int, int, int]) -> tuple[float, float]:
    return (box_xy[0] + box_xy[2]) / 2, (box_xy[1] + box_xy[3]) / 2


def boundary_point(box_xy: tuple[int, int, int, int], toward: tuple[float, float]) -> tuple[float, float]:
    cx, cy = center(box_xy)
    dx, dy = toward[0] - cx, toward[1] - cy
    if abs(dx) < 1e-6 and abs(dy) < 1e-6:
        return cx, cy
    half_w = max((box_xy[2] - box_xy[0]) / 2, 1)
    half_h = max((box_xy[3] - box_xy[1]) / 2, 1)
    scale = max(abs(dx) / half_w, abs(dy) / half_h)
    return cx + dx / scale, cy + dy / scale


def box(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, subtitle: str, fill: str, outline: str) -> None:
    draw.rounded_rectangle(xy, radius=12, fill=fill, outline=outline, width=3)
    center_text(draw, (xy[0] + 14, xy[1] + 12, xy[2] - 14, xy[1] + 54), title, font(24, True), INK)
    if subtitle:
        draw_wrapped(draw, (xy[0] + 22, xy[1] + 60), subtitle, font(24), MUTED, xy[2] - xy[0] - 44, 7)


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str = LINE,
    width: int = 4,
    dotted: bool = False,
) -> None:
    sx, sy = start
    ex, ey = end
    dx = ex - sx
    dy = ey - sy
    length = max((dx * dx + dy * dy) ** 0.5, 1)
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    size = 15
    line_end = (ex - ux * size, ey - uy * size)
    if dotted:
        steps = max(int(max(abs(ex - sx), abs(ey - sy)) // 14), 1)
        for i in range(0, steps, 2):
            x0 = sx + (line_end[0] - sx) * i / steps
            y0 = sy + (line_end[1] - sy) * i / steps
            frac = min(i + 1, steps) / steps
            x1 = sx + (line_end[0] - sx) * frac
            y1 = sy + (line_end[1] - sy) * frac
            draw.line((x0, y0, x1, y1), fill=color, width=width)
    else:
        draw.line((start, line_end), fill=color, width=width)
    p1 = (ex - ux * size + px * size * 0.55, ey - uy * size + py * size * 0.55)
    p2 = (ex - ux * size - px * size * 0.55, ey - uy * size - py * size * 0.55)
    draw.polygon([end, p1, p2], fill=color)


def connect(
    draw: ImageDraw.ImageDraw,
    src: tuple[int, int, int, int],
    dst: tuple[int, int, int, int],
    color: str = LINE,
    width: int = 4,
    dotted: bool = False,
) -> None:
    arrow(draw, boundary_point(src, center(dst)), boundary_point(dst, center(src)), color, width, dotted)


def pill(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], text: str, fill: str, outline: str | None = None) -> None:
    draw.rounded_rectangle(xy, radius=18, fill=fill, outline=outline or fill, width=2)
    center_text(draw, xy, text, font(24, True), "#FFFFFF" if fill not in {"#FFFFFF", PALE_BLUE, PALE_GREEN, PALE_ORANGE, PALE_PURPLE} else INK)


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (2040, 1570), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw.rectangle((0, 0, 2040, 1570), fill="#FFFFFF")
    draw.text((80, 50), "TS 36.212 Figure 5.1.3-2 重建：LTE rate 1/3 Turbo 编码器结构", font=font(36, True), fill=INK)
    draw_wrapped(
        draw,
        (80, 108),
        "依据 TS 36.212 Rel-19 §5.1.3.2.1/§5.1.3.2.2 和本地 media/image79.wmf 重建。实线表示信息编码阶段；虚线表示网格终止阶段使用的尾比特路径。",
        font(24),
        MUTED,
        1860,
    )

    # Main input and systematic path.
    input_box = (85, 250, 320, 394)
    box(draw, input_box, "码块输入", "c0...cK-1", PALE_BLUE, BLUE)
    pill(draw, (390, 292, 616, 356), "系统路 d(0)", BLUE)
    arrow(draw, (320, 315), (390, 315), BLUE)

    # First constituent encoder.
    first_enc = (420, 150, 770, 286)
    box(draw, first_enc, "第一 8 状态组成编码器", "原始顺序输入；产生第一校验路", PALE_GREEN, GREEN)
    pill(draw, (840, 186, 1078, 250), "第一校验 d(1)", GREEN)
    connect(draw, input_box, first_enc, GREEN)
    arrow(draw, (770, 205), (840, 205), GREEN)

    # Interleaver and second encoder.
    interleaver = (420, 430, 770, 566)
    second_enc = (860, 430, 1210, 566)
    box(draw, interleaver, "Turbo 内部交织器", "同一组输入比特重排后送入第二编码器", PALE_ORANGE, ORANGE)
    box(draw, second_enc, "第二 8 状态组成编码器", "交织后顺序输入；产生第二校验路", PALE_GREEN, GREEN)
    pill(draw, (1290, 466, 1528, 530), "第二校验 d(2)", GREEN)
    connect(draw, input_box, interleaver, ORANGE)
    connect(draw, interleaver, second_enc, ORANGE)
    arrow(draw, (1210, 482), (1290, 482), GREEN)

    # Output stream collection.
    mother_stream = (1410, 250, 1775, 394)
    box(draw, mother_stream, "三路母码流", "d(0), d(1), d(2)；每路长度 D=K+4", PALE_PURPLE, PURPLE)
    arrow(draw, (586, 315), (1410, 315), BLUE)
    arrow(draw, (1050, 205), (mother_stream[0], 295), GREEN)
    arrow(draw, (1510, 482), (1590, 380), GREEN)

    # Trellis termination section.
    draw.rounded_rectangle((85, 630, 1955, 1115), radius=18, fill=PANEL, outline="#D2DDE9", width=3)
    draw.text((115, 660), "网格终止路径", font=font(28, True), fill=INK)
    draw_wrapped(
        draw,
        (115, 705),
        "全部信息比特编码完成后，从移位寄存器反馈取尾比特。前 3 个尾比特终止第一组成编码器，同时第二组成编码器关闭；后 3 个尾比特终止第二组成编码器，同时第一组成编码器关闭。接收端必须为这些尾比特准备软输入，否则末端状态边界会被破坏。",
        font(24),
        MUTED,
        1770,
    )

    tail_feedback = (145, 820, 465, 980)
    tail_first = (520, 782, 900, 958)
    tail_second = (520, 930, 900, 1106)
    tail_output = (1030, 835, 1415, 995)
    box(draw, tail_feedback, "反馈取尾比特", "来自组成编码器反馈端", "#FFFFFF", RED)
    box(draw, tail_first, "前 3 个尾比特", "upper switch lower position；终止第一编码器", "#FFFFFF", GREEN)
    box(draw, tail_second, "后 3 个尾比特", "lower switch lower position；终止第二编码器", "#FFFFFF", GREEN)
    box(draw, tail_output, "尾比特输出排列", "进入三路母码流尾部，使每路长度从 K 变为 D=K+4", "#FFFFFF", PURPLE)
    connect(draw, tail_feedback, tail_first, RED, dotted=True)
    connect(draw, tail_feedback, tail_second, RED, dotted=True)
    connect(draw, tail_first, tail_output, GREEN, dotted=True)
    connect(draw, tail_second, tail_output, GREEN, dotted=True)
    arrow(draw, (1415, 905), (1650, 905), PURPLE)
    pill(draw, (1650, 876, 1805, 934), "尾部软输入", PURPLE)

    # Engineering notes.
    note_box = (80, 1165, 1955, 1495)
    draw.rounded_rectangle(note_box, radius=14, fill="#FBFCFE", outline="#D2DDE9", width=2)
    title_box = (110, note_box[1] + 22, 370, note_box[3] - 22)
    draw_centered_multiline(draw, title_box, "接收端读图顺序", font(24, True), INK, title_box[2] - title_box[0] - 20)
    notes = [
        "1. d(0) 是系统路，d(1)/d(2) 是两路组成编码器校验。",
        "2. 内部交织器只改变第二编码器看到的输入顺序，不产生新的信息比特。",
        "3. 虚线路径只在 trellis termination 阶段生效，影响尾比特和 D=K+4。",
        "4. Turbo 译码器的三路 LLR、终止状态和尾部地址必须与该结构一致。",
    ]
    body_box = (400, note_box[1] + 22, note_box[2] - 30, note_box[3] - 22)
    draw_centered_multiline(draw, body_box, notes, font(24), MUTED, body_box[2] - body_box[0] - 20, 10)

    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
