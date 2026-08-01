#!/usr/bin/env python3
"""
@file    convert_md_to_pdf.py
@brief   将 T2.1–T3.5 的 Markdown 讲义转换为 PDF，方便截图导入 PPT
@date    2026-07-25
@usage   python3 convert_md_to_pdf.py
@output  ~/Downloads/3GPP_PPT_Screenshots/*.pdf
"""

import os, re, subprocess, sys
from pathlib import Path

PUPPETEER = "/home/yys/.npm-global/lib/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer"
DOCS_DIR  = Path(__file__).resolve().parent.parent.parent / "docs" / "L1"
OUT_DIR   = Path.home() / "Downloads" / "3GPP_PPT_Screenshots"

FILES = [
    "T2.1_AWGN_noise_scaling.md",
    "T2.2_BPSK_QPSK_soft_demapping.md",
    "T2.3_QAM_Max_Log_MAP_demapping.md",
    "T2.4_fading_channel_LLR_reliability.md",
    "T2.5_LLR_clipping_scaling_quantization.md",
    "T3.1_LTE_NR_CRC_families.md",
    "T3.2_transport_code_block_filler_bits.md",
    "T3.3_LTE_Turbo_segmentation_rules.md",
    "T3.4_NR_LDPC_segmentation_rules.md",
    "T3.5_NR_Polar_segmentation_crc.md",
]

CSS = """
body {
  font-family: "DejaVu Sans", "Noto Sans CJK SC", sans-serif;
  font-size: 11px; line-height: 1.65; color: #1a1a1a;
  max-width: 920px; margin: 25px auto; padding: 0 18px;
}
h1 { font-size: 21px; border-bottom: 2px solid #065A82; padding-bottom: 5px; color: #065A82; }
h2 { font-size: 16px; margin-top: 22px; color: #1C7293; }
h3 { font-size: 14px; color: #21295C; }
h4 { font-size: 12px; color: #2C3E50; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 10px; }
th, td { border: 1px solid #bbb; padding: 4px 7px; text-align: left; }
th { background: #D6E8F0; font-weight: bold; }
code { background: #f5f5f5; padding: 1px 3px; border-radius: 2px; font-size: 10px; }
pre { background: #f5f5f5; padding: 9px; border-radius: 4px; overflow-x: auto; font-size: 10px; }
pre code { background: none; padding: 0; }
blockquote { border-left: 3px solid #1C7293; margin: 8px 0; padding: 5px 12px;
             background: #F4F7FA; color: #2C3E50; }
img { max-width: 100%; height: auto; }
.MathJax { font-size: 10px; }
mjx-container { font-size: 10px !important; }
"""

HTML_TPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8">
<style>{css}</style>
<script>
MathJax = {{
  tex: {{ inlineMath: [['$','$'],['\\\\(','\\\\)']], displayMath: [['$$','$$'],['\\\\[','\\\\]']] }},
  svg: {{ fontCache: 'global' }},
  startup: {{ typeset: false }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>{body}
<script>MathJax.typesetPromise()</script>
</body>
</html>"""


def md_to_html(text: str) -> str:
    """Convert project Markdown to basic HTML with table/blockquote/code support."""
    lines = text.split("\n")
    out = []
    in_code = False
    in_quote = False
    table_rows = []

    def flush():
        nonlocal table_rows
        if not table_rows: return
        sep_idx = None
        for idx, row in enumerate(table_rows):
            if idx == 0: continue
            if all(set(c.strip()) <= set(":- |") for c in row if c.strip()):
                sep_idx = idx; break
        html = ["<table>"]
        for idx, row in enumerate(table_rows):
            if idx == sep_idx: continue
            tag = "th" if (sep_idx is not None and idx < sep_idx) or (sep_idx is None and idx == 0) else "td"
            html.append("<tr>")
            for cell in row:
                html.append(f"<{tag}>{cell.strip()}</{tag}>")
            html.append("</tr>")
        html.append("</table>")
        out.append("".join(html))
        table_rows.clear()

    def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

    def inline(s):
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1">', s)
        s = re.sub(r"\[\[([^\]]+)\]\]", r"<em>\1</em>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    i = 0
    while i < len(lines):
        L = lines[i]

        # --- Display math: $$...$$ cross-line or $$...$$ single-line ---
        stripped = L.strip()
        if stripped == "$$":
            math_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() != "$$":
                math_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            out.append("<p>$$" + "".join(math_lines) + "$$</p>")
            continue
        if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) > 4:
            out.append("<p>" + stripped + "</p>")
            i += 1
            continue

        if L.startswith("```"):
            if in_code: out.append("</code></pre>"); in_code = False
            else: out.append("<pre><code>"); in_code = True
            i += 1; continue
        if in_code: out.append(esc(L)); i += 1; continue

        # Skip mermaid / text diagram blocks
        if L.strip() in ("```mermaid", "```text"):
            i += 1
            while i < len(lines) and not lines[i].startswith("```"): i += 1
            i += 1; continue

        if "|" in L and L.strip().startswith("|"):
            if not table_rows: flush()
            cells = [c.strip() for c in L.strip().split("|")]
            if cells and cells[0] == "": cells = cells[1:]
            if cells and cells[-1] == "": cells = cells[:-1]
            table_rows.append(cells); i += 1; continue
        elif table_rows: flush()

        if L.startswith(">"):
            if not in_quote: out.append("<blockquote>"); in_quote = True
            c = L[1:].strip()

            # Display math inside blockquote: keep $$...$$ intact
            if c == "$$":
                math_lines = []
                i += 1
                while i < len(lines) and lines[i].startswith(">") and lines[i][1:].strip() != "$$":
                    math_lines.append(lines[i][1:])  # strip leading >
                    i += 1
                if i < len(lines):
                    i += 1  # skip closing > $$
                out.append("<p>$$" + "".join(math_lines) + "$$</p>")
                continue
            if c.startswith("$$") and c.endswith("$$") and len(c) > 4:
                out.append(f"<p>{c}</p>")
                i += 1
                continue

            if c.startswith("#### "): out.append(f"<h4>{inline(c[5:])}</h4>")
            elif c.startswith("**") and c.endswith("**"): out.append(f"<p><strong>{inline(c[2:-2])}</strong></p>")
            else: out.append(f"<p>{inline(c)}</p>")
            i += 1; continue
        elif in_quote: out.append("</blockquote>"); in_quote = False

        if L.startswith("# "): out.append(f"<h1>{inline(L[2:])}</h1>")
        elif L.startswith("## "): out.append(f"<h2>{inline(L[3:])}</h2>")
        elif L.startswith("### "): out.append(f"<h3>{inline(L[4:])}</h3>")
        elif L.startswith("#### "): out.append(f"<h4>{inline(L[5:])}</h4>")
        elif L.strip() == "":
            if in_quote: out.append("</blockquote>"); in_quote = False
            out.append("")
        elif L.strip() == "---": out.append("<hr>")
        else: out.append(f"<p>{inline(L)}</p>")
        i += 1

    flush()
    if in_quote: out.append("</blockquote>")
    return "\n".join(out)


def convert_one(md_path: Path, out_dir: Path) -> bool:
    name = md_path.stem
    html_path = out_dir / f"{name}.html"
    pdf_path  = out_dir / f"{name}.pdf"

    html_body = md_to_html(md_path.read_text(encoding="utf-8"))
    html_full = HTML_TPL.format(css=CSS, body=html_body)
    # Fix relative image paths to absolute
    assets = (DOCS_DIR / "assets").resolve()
    html_full = html_full.replace('src="assets/', f'src="{assets}/')
    html_path.write_text(html_full, encoding="utf-8")

    js = f"""
const pp = require('{PUPPETEER}');
const fs = require('fs');
(async () => {{
  const browser = await pp.launch({{
    args: ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage']
  }});
  const page = await browser.newPage();
  await page.goto('file://{html_path}', {{ waitUntil: 'load', timeout: 90000 }});
  // Wait for MathJax typesetting to complete
  try {{
    await page.waitForFunction(() => window.MathJax && window.MathJax.typesetPromise ?
      window.MathJax.startup.document.getComponents().length > 0 : true,
      {{ timeout: 20000 }});
  }} catch(e) {{}}
  await new Promise(r => setTimeout(r, 5000));
  await page.pdf({{
    path: '{pdf_path}', format: 'A4',
    margin: {{ top: '14mm', bottom: '14mm', left: '11mm', right: '11mm' }},
    printBackground: true
  }});
  await browser.close();
  console.log('OK');
}})().catch(e => {{ console.error(e.message); process.exit(1); }});
"""
    js_path = out_dir / f"_r_{name}.js"
    js_path.write_text(js)

    r = subprocess.run(["node", str(js_path)], capture_output=True, text=True, timeout=180, cwd=str(out_dir))
    js_path.unlink(missing_ok=True)
    if r.returncode != 0:
        print(f"  FAIL {name}: {r.stderr[:200]}")
        return False
    print(f"  OK  {name}  ({pdf_path.stat().st_size//1024} KB)")
    return True


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    ok = 0
    print(f"Output: {OUT_DIR}\n")
    for f in FILES:
        p = DOCS_DIR / f
        if not p.exists():
            print(f"  SKIP {f}")
            continue
        if convert_one(p, OUT_DIR):
            ok += 1
    print(f"\nDone: {ok}/{len(FILES)}")


if __name__ == "__main__":
    main()
