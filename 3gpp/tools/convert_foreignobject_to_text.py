#!/usr/bin/env python3
"""
Post-process Mermaid SVG: convert all foreignObject text to native SVG <text> + <tspan>.
Native SVG <text> scales perfectly with browser zoom; foreignObject HTML text does not.

Usage: python3 convert_foreignobject_to_text.py input.svg output.svg
"""
import re
import sys
from html import unescape
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    """Extract text lines from HTML fragment, splitting on <br/> tags."""

    def __init__(self):
        super().__init__()
        self.lines = []
        self.current = ""

    def handle_starttag(self, tag, attrs):
        if tag == "br":
            self.lines.append(self.current)
            self.current = ""

    def handle_data(self, data):
        self.current += data

    def get_lines(self):
        if self.current:
            self.lines.append(self.current)
        return [ln.strip() for ln in self.lines if ln.strip() or not self.lines]


def convert(svg_content):
    """Replace <foreignObject> blocks with native SVG <text> elements."""

    # --- node labels: <g class="label" transform="translate(x,y)"><foreignObject>...</foreignObject></g> ---
    node_fo = re.compile(
        r'(<g class="label"[^>]*transform="translate\(([^)]+)\)"[^>]*>)'
        r'(.*?<foreignObject[^>]*>(.*?)</foreignObject>.*?)'
        r'(</g>)',
        re.DOTALL,
    )

    def _node_repl(m):
        g_open = m.group(1)
        tx, ty = m.group(2).split(",")
        html_inner = m.group(4)
        g_close = m.group(5)

        extr = TextExtractor()
        try:
            extr.feed(unescape(html_inner))
        except Exception:
            return m.group(0)
        lines = extr.get_lines()
        if not lines:
            return m.group(0)

        color_m = re.search(r"color:\s*([^;\"]+)", html_inner)
        text_color = color_m.group(1).strip() if color_m else "#333"

        fs_m = re.search(r"font-size:\s*(\d+)px", html_inner)
        font_size = fs_m.group(1) if fs_m else "14"

        lh = int(font_size) * 1.5
        x, y = float(tx), float(ty)

        if len(lines) == 1:
            return (
                f'<g transform="translate({x},{y})">'
                f'<text text-anchor="middle" font-size="{font_size}px" fill="{text_color}" '
                f'font-family="trebuchet ms,verdana,arial,sans-serif" '
                f'y="{lh * 0.35:.1f}">{lines[0]}</text>'
                f"</g>"
            )

        total_h = lh * len(lines)
        start_y = -total_h / 2 + lh * 0.8
        tspans = "\n".join(
            f'<tspan x="0" y="{start_y + i * lh:.1f}">{ln}</tspan>'
            for i, ln in enumerate(lines)
        )
        return (
            f'<g transform="translate({x},{y})">'
            f'<text text-anchor="middle" font-size="{font_size}px" fill="{text_color}" '
            f'font-family="trebuchet ms,verdana,arial,sans-serif">\n{tspans}\n</text>'
            f"</g>"
        )

    result = node_fo.sub(_node_repl, svg_content)

    # --- edge labels: <g class="edgeLabel"><g class="label" transform="..."><foreignObject>...</foreignObject></g></g> ---
    edge_fo = re.compile(
        r'(<g class="edgeLabel"[^>]*>)'
        r'(<g class="label"[^>]*transform="translate\(([^)]+)\)"[^>]*>)'
        r'(.*?<foreignObject[^>]*>(.*?)</foreignObject>.*?)'
        r"(</g>)\s*(</g>)",
        re.DOTALL,
    )

    def _edge_repl(m):
        prefix = m.group(1)
        tx, ty = m.group(3).split(",")
        mid = m.group(4)  # between g.label open and foreignObject
        html_inner = m.group(5)
        suffix = m.group(7)

        extr = TextExtractor()
        try:
            extr.feed(unescape(html_inner))
        except Exception:
            return m.group(0)
        lines = extr.get_lines()
        if not lines:
            return m.group(0)

        color_m = re.search(r"color:\s*([^;\"]+)", html_inner)
        text_color = color_m.group(1).strip() if color_m else "#333"

        fs_m = re.search(r"font-size:\s*(\d+)px", html_inner)
        font_size = fs_m.group(1) if fs_m else "14"

        # Preserve background rect if present
        bkg_m = re.search(r"(<rect[^>]*>)", mid)
        bkg = bkg_m.group(1) if bkg_m else ""

        lh = int(font_size) * 1.5
        x, y = float(tx), float(ty)

        if len(lines) == 1:
            return (
                f'{prefix}<g transform="translate({x},{y})">{bkg}'
                f'<text text-anchor="middle" font-size="{font_size}px" fill="{text_color}" '
                f'font-family="trebuchet ms,verdana,arial,sans-serif" '
                f'y="{lh * 0.35:.1f}">{lines[0]}</text>'
                f"</g>{suffix}"
            )

        total_h = lh * len(lines)
        start_y = -total_h / 2 + lh * 0.8
        tspans = "\n".join(
            f'<tspan x="0" y="{start_y + i * lh:.1f}">{ln}</tspan>'
            for i, ln in enumerate(lines)
        )
        return (
            f'{prefix}<g transform="translate({x},{y})">{bkg}'
            f'<text text-anchor="middle" font-size="{font_size}px" fill="{text_color}" '
            f'font-family="trebuchet ms,verdana,arial,sans-serif">\n{tspans}\n</text>'
            f"</g>{suffix}"
        )

    result = edge_fo.sub(_edge_repl, result)

    # --- cluster labels: <g class="cluster-label" transform="..."><foreignObject>...</foreignObject></g> ---
    cluster_fo = re.compile(
        r'(<g class="cluster-label"[^>]*transform="translate\(([^)]+)\)"[^>]*>)'
        r'(.*?<foreignObject[^>]*>(.*?)</foreignObject>.*?)'
        r"(</g>)",
        re.DOTALL,
    )

    def _cluster_repl(m):
        g_open = m.group(1)
        tx, ty = m.group(2).split(",")
        html_inner = m.group(4)
        g_close = m.group(5)

        extr = TextExtractor()
        try:
            extr.feed(unescape(html_inner))
        except Exception:
            return m.group(0)
        lines = extr.get_lines()
        if not lines:
            return m.group(0)

        color_m = re.search(r"color:\s*([^;\"]+)", html_inner)
        text_color = color_m.group(1).strip() if color_m else "#333"

        fs_m = re.search(r"font-size:\s*(\d+)px", html_inner)
        font_size = fs_m.group(1) if fs_m else "14"

        lh = int(font_size) * 1.5
        x, y = float(tx), float(ty)

        if len(lines) == 1:
            return (
                f'<g transform="translate({x},{y})">'
                f'<text font-size="{font_size}px" fill="{text_color}" '
                f'font-family="trebuchet ms,verdana,arial,sans-serif" '
                f'y="{lh * 0.35:.1f}">{lines[0]}</text>'
                f"</g>"
            )

        total_h = lh * len(lines)
        start_y = -total_h / 2 + lh * 0.8
        tspans = "\n".join(
            f'<tspan x="0" y="{start_y + i * lh:.1f}">{ln}</tspan>'
            for i, ln in enumerate(lines)
        )
        return (
            f'<g transform="translate({x},{y})">'
            f'<text font-size="{font_size}px" fill="{text_color}" '
            f'font-family="trebuchet ms,verdana,arial,sans-serif">\n{tspans}\n</text>'
            f"</g>"
        )

    return cluster_fo.sub(_cluster_repl, result)


if __name__ == "__main__":
    inp, outp = sys.argv[1], sys.argv[2]
    svg = open(inp).read()
    result = convert(svg)
    fo_before = svg.count("<foreignObject")
    fo_after = result.count("<foreignObject")
    text_before = svg.count("<text")
    text_after = result.count("<text")
    open(outp, "w").write(result)
    print(f"foreignObject: {fo_before} → {fo_after}")
    print(f"native <text>:  {text_before} → {text_after}")
    print(f"Output: {outp}")
