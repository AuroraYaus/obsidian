#!/usr/bin/env python3
"""Render LTE DL/UL decoder context and soft-buffer namespace comparison."""

from __future__ import annotations

from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont
try:
    from tools.figures.figure_text_fit import font, wrap_text as fit_wrap_text
except ModuleNotFoundError:  # Allow direct execution: python tools/figures/render_*.py
    from figure_text_fit import font, wrap_text as fit_wrap_text


ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = ROOT / "docs/L2/assets/T7.5_LTE_DL_UL_decoder_context.png"

PALETTE = {
    "ink": "#102033",
    "muted": "#5A6A7A",
    "line": "#C9D5E3",
    "panel_dl": "#F6FAFF",
    "panel_ul": "#F5FCF8",
    "dl": "#2F80ED",
    "ul": "#0BA574",
    "soft": "#FFF8E8",
    "core": "#EAF2FF",
    "warn_bg": "#FFF3F3",
    "warn": "#D64545",
    "ok": "#246B47",
}



def center_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    x = box[0] + ((box[2] - box[0]) - width) / 2 - bbox[0]
    y = box[1] + ((box[3] - box[1]) - height) / 2 - bbox[1]
    draw.text((x, y), text, font=fnt, fill=fill)


def wrap_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 6,
) -> int:
    x, y = xy
    for line in fit_wrap_text(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color: str = "#556A80") -> None:
    sx, sy = start
    ex, ey = end
    vx, vy = ex - sx, ey - sy
    length = math.hypot(vx, vy)
    if length == 0:
        return
    ux, uy = vx / length, vy / length
    head_len, head_w = 16, 10
    line_end = (ex - ux * head_len, ey - uy * head_len)
    draw.line([start, line_end], fill=color, width=4)
    px, py = -uy, ux
    draw.polygon(
        [
            (ex, ey),
            (ex - ux * head_len + px * head_w, ey - uy * head_len + py * head_w),
            (ex - ux * head_len - px * head_w, ey - uy * head_len - py * head_w),
        ],
        fill=color,
    )


def draw_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    fill: str,
    outline: str = PALETTE["line"],
) -> None:
    draw.rounded_rectangle(box, radius=12, fill=fill, outline=outline, width=2)
    center_text(draw, (box[0] + 12, box[1] + 10, box[2] - 12, box[1] + 48), title, font(24, True), PALETTE["ink"])
    center_text(draw, (box[0] + 14, box[1] + 48, box[2] - 14, box[3] - 12), body, font(24), PALETTE["muted"])


def token_row(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    tokens: list[tuple[str, str]],
    fnt: ImageFont.FreeTypeFont | None = None,
) -> None:
    if fnt is None:
        fnt = font(24, True)
    cursor = x
    for label, color in tokens:
        width = max(92, draw.textbbox((0, 0), label, font=fnt)[2] + 32)
        draw.rounded_rectangle((cursor, y, cursor + width, y + 46), radius=10, fill=color, outline=color)
        center_text(draw, (cursor, y, cursor + width, y + 46), label, fnt, "#FFFFFF")
        cursor += width + 12


def draw_pipeline(
    draw: ImageDraw.ImageDraw,
    *,
    x: int,
    y: int,
    width: int,
    accent: str,
    panel_fill: str,
    title: str,
    source: tuple[str, str],
    desc: tuple[str, str],
    key_tokens: list[tuple[str, str]],
    key_caption: str,
    notes: list[str],
) -> None:
    panel = (x, y, x + width, y + 806)
    draw.rounded_rectangle(panel, radius=16, fill=panel_fill, outline=accent, width=2)
    draw.rounded_rectangle((x, y, x + width, y + 58), radius=16, fill=accent, outline=accent)
    center_text(draw, (x, y, x + width, y + 58), title, font(25, True), "#FFFFFF")

    box_w = width - 160
    box_x = x + 80
    boxes = [
        (box_x, y + 98, box_x + box_w, y + 194, source[0], source[1], "#FFFFFF"),
        (box_x, y + 226, box_x + box_w, y + 322, desc[0], desc[1], "#FFFFFF"),
        (box_x, y + 354, box_x + box_w, y + 450, "soft buffer key", key_caption, PALETTE["soft"]),
        (box_x, y + 482, box_x + box_w, y + 578, "shared Turbo core", "同一译码数学核心；上下文在 core 外侧隔离", PALETTE["core"]),
    ]

    for bx0, by0, bx1, by1, t, b, fill in boxes:
        draw_box(draw, (bx0, by0, bx1, by1), t, b, fill)

    mid_x = x + width // 2
    arrow(draw, (mid_x, y + 194), (mid_x, y + 226))
    arrow(draw, (mid_x, y + 322), (mid_x, y + 354))
    arrow(draw, (mid_x, y + 450), (mid_x, y + 482))

    draw.text((box_x, y + 600), "key tokens", font=font(24, True), fill=PALETTE["ink"])
    token_row(draw, box_x, y + 640, key_tokens)

    note_box = (box_x, y + 694, box_x + box_w, y + 792)
    draw.rounded_rectangle(note_box, radius=12, fill="#FFFFFF", outline=PALETTE["line"], width=1)
    note_y = note_box[1] + 14
    for note in notes:
        draw.text((note_box[0] + 18, note_y), note, font=font(24), fill=PALETTE["muted"])
        note_y += 36


def main() -> None:
    img = Image.new("RGB", (1920, 1600), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw.text((70, 42), "LTE DL-SCH 与 UL-SCH：同一 Turbo core，不同 soft buffer namespace", font=font(38, True), fill=PALETTE["ink"])
    wrap_text(
        draw,
        (70, 102),
        "读图顺序：左边是 UE 接收下行，右边是 eNB 接收上行。两条链路都进入 shared Turbo core，但进入 soft buffer 前的 key 不同；UL 必须包含 UE context，否则多 UE 会命中同一缓存。",
        font(24),
        PALETTE["muted"],
        1760,
    )

    draw_pipeline(
        draw,
        x=70,
        y=190,
        width=800,
        accent=PALETTE["dl"],
        panel_fill=PALETTE["panel_dl"],
        title="DL-SCH 接收：UE 侧",
        source=("PDSCH demapper", "输出 DL LLR 流"),
        desc=("DL descriptor", "direction, HARQ, RV, TBS, MCS"),
        key_tokens=[("DL", PALETTE["dl"]), ("HARQ3", "#668BDA"), ("TB17", "#7FA0D8"), ("CB0", "#9AB6E6")],
        key_caption="direction=DL / harq_id / tb_id / cb_id",
        notes=["要点：UE 只代表本机，通常不需要显式 ue_id。", "风险：RV、Ncb 或 HARQ key 错会污染重传合并。"],
    )

    draw_pipeline(
        draw,
        x=1050,
        y=190,
        width=800,
        accent=PALETTE["ul"],
        panel_fill=PALETTE["panel_ul"],
        title="UL-SCH 接收：eNB 侧",
        source=("PUSCH demapper", "输出 UL LLR 流"),
        desc=("UL descriptor", "direction, UE, HARQ, RV, TBS, MCS"),
        key_tokens=[("UL", PALETTE["ul"]), ("UE17", "#2C9A70"), ("HARQ3", "#58BA8D"), ("TB17", "#7ACBA2"), ("CB0", "#9EDBBB")],
        key_caption="direction=UL / ue_id / harq_id / tb_id / cb_id",
        notes=["要点：eNB 同时服务多个 UE，key 必须带 UE 维度。", "风险：少一个 ue_id，就可能把 UE17 和 UE18 的 LLR 合并。"],
    )

    # Shared-core band between panels and the negative example.
    band = (70, 990, 1850, 1090)
    draw.rounded_rectangle(band, radius=14, fill="#FFF9EA", outline="#E1C36B", width=2)
    center_text(draw, (band[0] + 20, band[1] + 10, band[0] + 240, band[3] - 12), "可共享", font(24, True), PALETTE["ink"])
    center_text(draw, (band[0] + 250, band[1] + 10, band[2] - 20, band[3] - 12), "Turbo 译码数学核心在两侧复用；soft buffer key 不能复用", font(24), PALETTE["muted"])

    # Collision example.
    draw.rounded_rectangle((70, 1125, 1850, 1450), radius=16, fill=PALETTE["warn_bg"], outline="#F0B8B8", width=2)
    draw.text((105, 1158), "负例：UL soft buffer key 缺少 UE context", font=font(28, True), fill=PALETTE["warn"])
    wrap_text(
        draw,
        (105, 1210),
        "如果 eNB 侧 key 只写 direction=UL / HARQ3 / TB17 / CB0，那么 UE17 和 UE18 的重传会命中同一缓存地址。Turbo core 仍然会运行，但输入 LLR 已经混入错误历史。",
        font(24),
        PALETTE["muted"],
        1690,
    )
    draw.text((120, 1268), "UE17 错误 key", font=font(24, True), fill=PALETTE["ink"])
    token_row(draw, 120, 1306, [("UL", PALETTE["ul"]), ("HARQ3", "#58BA8D"), ("TB17", "#7ACBA2"), ("CB0", "#9EDBBB")])
    draw.text((760, 1268), "UE18 错误 key", font=font(24, True), fill=PALETTE["ink"])
    token_row(draw, 760, 1306, [("UL", PALETTE["ul"]), ("HARQ3", "#58BA8D"), ("TB17", "#7ACBA2"), ("CB0", "#9EDBBB")])
    draw.text((1350, 1288), "同一个 key -> 同一个缓存", font=font(24, True), fill=PALETTE["warn"])
    draw.text((1350, 1330), "结果：LLR 被错误软合并", font=font(24), fill=PALETTE["muted"])

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"WROTE {OUT_PATH}")


if __name__ == "__main__":
    main()
