#!/usr/bin/env python3
"""Shared text-fit and font helpers for PIL-generated teaching figures."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Protocol

from PIL import ImageFont


class TextMeasure(Protocol):
    def textbbox(self, xy, text: str, font=None): ...


TOKEN_RE = re.compile(r"[A-Za-z0-9_./'()+\[\]=:;-]+|[ \t]+|\n|.")
CJK_RE = re.compile(r"[\u3400-\u9fff]")
TERMINAL_PUNCTUATION = set("。，、；：？！,.!?;:")


def text_width(draw: TextMeasure, text: str, fnt) -> int:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    return bbox[2] - bbox[0]


def split_oversize_token(draw: TextMeasure, token: str, fnt, width: int) -> list[str]:
    parts: list[str] = []
    remaining = token
    while remaining and text_width(draw, remaining, fnt) > width:
        split = len(remaining) - 1
        while split > 1 and text_width(draw, remaining[:split], fnt) > width:
            split -= 1
        parts.append(remaining[:split])
        remaining = remaining[split:]
    if remaining:
        parts.append(remaining)
    return parts


def visual_units(text: str) -> int:
    return sum(1 for ch in text if CJK_RE.match(ch) or ch in TERMINAL_PUNCTUATION)


def rebalance_short_final_line(lines: list[str]) -> list[str]:
    if len(lines) < 2:
        return lines

    final = lines[-1].strip()
    if not final:
        return lines

    has_ascii_word = any(ch.isascii() and ch.isalnum() for ch in final)
    if has_ascii_word and not all(ch in TERMINAL_PUNCTUATION for ch in final):
        return lines

    if not all(ch in TERMINAL_PUNCTUATION for ch in final) and visual_units(final) > 2:
        return lines

    previous = lines[-2].rstrip()
    while previous and visual_units(final) < 3:
        ch = previous[-1]
        if not (CJK_RE.match(ch) or ch in TERMINAL_PUNCTUATION):
            break
        previous = previous[:-1].rstrip()
        final = ch + final

    if previous and final != lines[-1].strip():
        lines[-2] = previous
        lines[-1] = final
    return lines


def wrap_text(draw: TextMeasure, text: str, fnt, width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for token in TOKEN_RE.findall(text):
        if token == "\n":
            lines.append(current)
            current = ""
            continue

        candidate = current + token
        if text_width(draw, candidate, fnt) <= width or not current:
            current = candidate
            if text_width(draw, current, fnt) > width:
                parts = split_oversize_token(draw, current, fnt, width)
                lines.extend(parts[:-1])
                current = parts[-1] if parts else ""
            continue

        if current.strip():
            lines.append(current.rstrip())
        current = token.lstrip()
        if text_width(draw, current, fnt) > width:
            parts = split_oversize_token(draw, current, fnt, width)
            lines.extend(parts[:-1])
            current = parts[-1] if parts else ""

    if current.strip() or not lines:
        lines.append(current.rstrip())
    return rebalance_short_final_line(lines)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Load a CJK-capable font with fallback to DejaVu Sans.

    Tries Noto Sans CJK first, then DejaVu Sans as fallback.
    """
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
        if bold
        else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    raise FileNotFoundError(
        "No suitable font found. Install Noto Sans CJK or DejaVu Sans."
    )
