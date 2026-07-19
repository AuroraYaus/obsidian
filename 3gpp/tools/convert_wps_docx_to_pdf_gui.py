#!/usr/bin/env python3
"""Batch-export 3GPP Word sources to PDF through the WPS GUI.

WPS Office for Linux does not expose a verified headless `--convert-to pdf`
interface on this installation. This script drives the already verified GUI
path: open source.docx, click the toolbar PDF-export shortcut, accept the
default same-directory source.pdf path, handle the WPS font warning, and verify
the resulting PDF with pdfinfo.

For headless (CI-compatible) conversion, use extract_3gpp_word.py with LibreOffice
instead. This script requires a running X11/Wayland session with WPS installed.
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image


ROOT = Path("3GPP_Rel19/processed")
WPS = Path("/usr/bin/wps")


def run(cmd: list[str], *, check: bool = True, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check, timeout=timeout)


def sh(script: str, *, check: bool = True, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["bash", "-lc", script], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check, timeout=timeout)


def wmctrl_lines() -> list[str]:
    proc = run(["wmctrl", "-lx"], check=False)
    return proc.stdout.splitlines()


def close_wps() -> None:
    sh(
        "pkill -f '/opt/kingsoft/wps-office/office6/wpsoffice|"
        "/opt/kingsoft/wps-office/office6/wpscloudsvr|"
        "/opt/kingsoft/wps-office/office6/wps /wps|"
        "/opt/kingsoft/wps-office/office6/promecefpluginhost' || true",
        check=False,
    )
    time.sleep(2.0)


def search_window(name: str) -> str | None:
    proc = run(["xdotool", "search", "--name", name], check=False)
    ids = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    return ids[-1] if ids else None


def search_windows(name: str) -> list[str]:
    proc = run(["xdotool", "search", "--name", name], check=False)
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def window_geometry(win: str) -> tuple[int, int] | None:
    proc = run(["xwininfo", "-id", win], check=False)
    if proc.returncode != 0:
        return None
    width = height = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line.startswith("Width:"):
            width = int(line.split(":", 1)[1].strip())
        elif line.startswith("Height:"):
            height = int(line.split(":", 1)[1].strip())
    if width is None or height is None:
        return None
    return width, height


def content_window_candidates(name: str) -> list[str]:
    lines = wmctrl_lines()
    wins = []
    for line in lines:
        parts = line.split(None, 4)
        if len(parts) >= 5 and parts[2] == "wps.wps" and name in parts[4]:
            wins.append(parts[0])
    if not wins:
        wins = search_windows(name)
    # WPS exposes an outer decorated window and an inner content window with the
    # same title. Prefer the wmctrl wps.wps content window; relative clicks are
    # only valid there.
    scored: list[tuple[int, str]] = []
    for win in wins:
        geom = window_geometry(win)
        if geom is None:
            continue
        w, h = geom
        scored.append((w * h, win))
    return [win for _, win in sorted(scored, reverse=True)]


def window_screenshot(win: str, path: Path) -> Image.Image | None:
    proc = run(["import", "-window", win, str(path)], check=False)
    if proc.returncode != 0 or not path.exists():
        return None
    return Image.open(path).convert("RGB")


def find_blue_button_center(win: str, *, tmp_name: str) -> tuple[int, int] | None:
    img = window_screenshot(win, Path(f"/tmp/{tmp_name}_{win}.png"))
    if img is None:
        return None
    w, h = img.size
    # WPS primary buttons are saturated blue. Detect the largest blue component
    # in the lower half, then click its center.
    mask: set[tuple[int, int]] = set()
    pix = img.load()
    for y in range(h // 2, h):
        for x in range(w):
            r, g, b = pix[x, y]
            if b > 150 and g > 80 and r < 90 and b - r > 80 and b - g > 20:
                mask.add((x, y))
    if not mask:
        return None

    seen: set[tuple[int, int]] = set()
    best: list[tuple[int, int]] = []
    for p in list(mask):
        if p in seen:
            continue
        stack = [p]
        seen.add(p)
        comp: list[tuple[int, int]] = []
        while stack:
            qx, qy = stack.pop()
            comp.append((qx, qy))
            for nx, ny in ((qx + 1, qy), (qx - 1, qy), (qx, qy + 1), (qx, qy - 1)):
                np = (nx, ny)
                if np in mask and np not in seen:
                    seen.add(np)
                    stack.append(np)
        if len(comp) > len(best):
            best = comp
    if len(best) < 200:
        return None
    xs = [p[0] for p in best]
    ys = [p[1] for p in best]
    return (sum(xs) // len(xs), sum(ys) // len(ys))


def find_text_center(win: str, targets: list[str], *, tmp_name: str) -> tuple[int, int] | None:
    img_path = Path(f"/tmp/{tmp_name}_{win}.png")
    img = window_screenshot(win, img_path)
    if img is None:
        return None
    tsv_base = Path(f"/tmp/{tmp_name}_{win}")
    proc = run(
        [
            "tesseract",
            str(img_path),
            str(tsv_base),
            "-l",
            "chi_sim+eng",
            "--psm",
            "6",
            "tsv",
        ],
        check=False,
        timeout=20,
    )
    tsv_path = tsv_base.with_suffix(".tsv")
    if proc.returncode != 0 or not tsv_path.exists():
        return None
    rows: list[dict[str, str]] = []
    with tsv_path.open("r", encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            text = (row.get("text") or "").strip().replace(" ", "")
            if not text:
                continue
            row["text_norm"] = text
            rows.append(row)

    def row_box(row: dict[str, str]) -> tuple[int, int, int, int]:
        left = int(float(row["left"]))
        top = int(float(row["top"]))
        width = int(float(row["width"]))
        height = int(float(row["height"]))
        return left, top, width, height

    for target in targets:
        target_norm = target.replace(" ", "")
        # First try direct OCR token containment.
        matches = [r for r in rows if target_norm in r["text_norm"] or r["text_norm"] in target_norm]
        if matches:
            lefts: list[int] = []
            tops: list[int] = []
            rights: list[int] = []
            bottoms: list[int] = []
            for r in matches:
                left, top, width, height = row_box(r)
                lefts.append(left)
                tops.append(top)
                rights.append(left + width)
                bottoms.append(top + height)
            return ((min(lefts) + max(rights)) // 2, (min(tops) + max(bottoms)) // 2)

        # Then try line-level concatenation, useful when Chinese text is split.
        by_line: dict[tuple[str, str, str], list[dict[str, str]]] = {}
        for r in rows:
            key = (r.get("block_num", ""), r.get("par_num", ""), r.get("line_num", ""))
            by_line.setdefault(key, []).append(r)
        for line_rows in by_line.values():
            line_text = "".join(r["text_norm"] for r in sorted(line_rows, key=lambda x: int(float(x["left"]))))
            if target_norm not in line_text:
                continue
            lefts = []
            tops = []
            rights = []
            bottoms = []
            for r in line_rows:
                left, top, width, height = row_box(r)
                lefts.append(left)
                tops.append(top)
                rights.append(left + width)
                bottoms.append(top + height)
            return ((min(lefts) + max(rights)) // 2, (min(tops) + max(bottoms)) // 2)
    return None


def ocr_window_text(win: str, *, tmp_name: str) -> str:
    img_path = Path(f"/tmp/{tmp_name}_{win}.png")
    img = window_screenshot(win, img_path)
    if img is None:
        return ""
    out_base = Path(f"/tmp/{tmp_name}_{win}_text")
    proc = run(
        ["tesseract", str(img_path), str(out_base), "-l", "chi_sim+eng", "--psm", "6"],
        check=False,
        timeout=20,
    )
    out_path = out_base.with_suffix(".txt")
    if proc.returncode != 0 or not out_path.exists():
        return ""
    return out_path.read_text(encoding="utf-8", errors="ignore").replace(" ", "")


def prompt_image_embed_fallback(win: str) -> tuple[int, int] | None:
    text = ocr_window_text(win, tmp_name="wps_font_prompt_text")
    # Do not use this fallback unless the prompt is clearly the font embedding
    # dialog and the two choices are visible in OCR output. OCR may misread
    # "嵌入" as "庶入", so match the surrounding stable words too.
    has_image_choice = "图片形式" in text or ("图片" in text and "继续输出" in text)
    has_alt_choice = "相似字体" in text
    has_font_context = "字体" in text and ("PDF" in text or "输出" in text)
    if not (has_image_choice and has_alt_choice and has_font_context):
        return None
    img = window_screenshot(win, Path(f"/tmp/wps_font_prompt_fallback_{win}.png"))
    if img is None:
        return None
    w, h = img.size
    # In this verified WPS font prompt, the bottom row has two buttons:
    # left = 以图片形式嵌入, right = 替换相似字体. Use geometry only after
    # OCR has proven this exact dialog semantics.
    return (int(w * 0.72), int(h * 0.91))


def wait_window(name: str, timeout_s: float) -> str | None:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        win = search_window(name)
        if win:
            return win
        time.sleep(0.5)
    return None


def wait_no_window(name: str, timeout_s: float) -> bool:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        if not search_window(name):
            return True
        time.sleep(0.5)
    return False


def wait_pdf(pdf: Path, min_size: int = 1024, timeout_s: float = 180.0) -> bool:
    deadline = time.time() + timeout_s
    last_size = -1
    stable_since: float | None = None
    while time.time() < deadline:
        handle_font_prompt()
        if pdf.exists():
            size = pdf.stat().st_size
            if size >= min_size:
                if size == last_size:
                    stable_since = stable_since or time.time()
                    if time.time() - stable_since >= 2.0:
                        return True
                else:
                    stable_since = None
                    last_size = size
        time.sleep(1.0)
    return False


def verify_pdf(pdf: Path) -> tuple[bool, str]:
    proc = run(["pdfinfo", str(pdf)], check=False)
    text = proc.stdout + proc.stderr
    ok = proc.returncode == 0 and "Pages:" in text
    pages = "UNKNOWN"
    for line in text.splitlines():
        if line.startswith("Pages:"):
            pages = line.split(":", 1)[1].strip()
            break
    return ok, pages


def confirm_export_dialog(export_win: str) -> None:
    run(["xdotool", "windowactivate", "--sync", export_win], check=False)
    time.sleep(0.2)
    center = find_text_center(export_win, ["确定", "确定(O)", "OK"], tmp_name="wps_export_dialog")
    if center is None:
        raise RuntimeError("Cannot locate export dialog confirm button by text OCR")
    run(["xdotool", "mousemove", "--window", export_win, str(center[0]), str(center[1])], check=False)
    run(["xdotool", "click", "1"], check=False)


def handle_font_prompt() -> None:
    candidates = content_window_candidates("提示")
    prompt_win = candidates[-1] if candidates else None
    if not prompt_win:
        return
    run(["xdotool", "windowactivate", "--sync", prompt_win], check=False)
    time.sleep(0.1)
    # The "以图片形式嵌入" button appears in two verified layouts. Try both
    # content-window-relative positions, checking after each click whether the
    # prompt has closed. This is faster and more reliable than OCR for this WPS
    # dialog, whose Chinese button text is often misrecognized.
    for x, y in ((965, 510), (965, 585)):
        run(["xdotool", "mousemove", "--window", prompt_win, str(x), str(y)], check=False)
        run(["xdotool", "click", "1"], check=False)
        time.sleep(0.5)
        if not content_window_candidates("提示"):
            return


def export_one(docx: Path, *, dry_run: bool = False) -> tuple[str, str]:
    pdf = docx.with_name("source.pdf")
    if pdf.exists():
        ok, pages = verify_pdf(pdf)
        return ("skip_existing_ok" if ok else "skip_existing_bad", pages)
    if dry_run:
        return "dry_run", "-"

    close_wps()
    subprocess.Popen(
        [str(WPS), str(docx.resolve())],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    doc_win = wait_window("source.docx - WPS Office", 45)
    if not doc_win:
        return "failed_open_window", "-"

    run(["xdotool", "windowactivate", "--sync", doc_win], check=False)
    time.sleep(0.1)

    # Dismiss the update prompt if it appears.
    update_win = search_window("更新")
    if update_win:
        run(["xdotool", "windowactivate", "--sync", update_win], check=False)
        run(["xdotool", "key", "Escape"], check=False)
        time.sleep(1.0)
        run(["xdotool", "windowactivate", "--sync", doc_win], check=False)

    # Verified on this WPS layout: the toolbar button just right of File, second
    # icon, opens the same "输出 PDF 文件" dialog.
    run(["xdotool", "mousemove", "--window", doc_win, "330", "110"], check=False)
    run(["xdotool", "click", "1"], check=False)
    export_win = wait_window("输出 PDF 文件", 10)
    if not export_win:
        # Fallback through the File menu: Alt+F, then F for 输出为PDF(F).
        run(["xdotool", "windowactivate", "--sync", doc_win], check=False)
        run(["xdotool", "key", "alt+f"], check=False)
        time.sleep(0.4)
        run(["xdotool", "key", "f"], check=False)
        export_win = wait_window("输出 PDF 文件", 10)
    if not export_win:
        return "failed_export_dialog", "-"

    confirm_export_dialog(export_win)
    time.sleep(1.0)
    handle_font_prompt()

    if not wait_pdf(pdf, timeout_s=1200):
        return "failed_pdf_timeout", "-"

    ok, pages = verify_pdf(pdf)
    close_wps()
    return ("converted_ok" if ok else "converted_bad_pdfinfo", pages)


def collect_docs(root: Path) -> list[Path]:
    docs = sorted(root.glob("*/source.docx")) + sorted(root.glob("*/source.doc"))
    return sorted(docs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", type=Path, default=Path("docs/audits/wps_pdf_conversion_report.tsv"))
    args = parser.parse_args()

    docs = [p for p in collect_docs(args.root) if not p.with_name("source.pdf").exists()]
    if args.limit:
        docs = docs[: args.limit]

    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8") as f:
        f.write("document\tstatus\tpages\tpdf\n")
        for i, docx in enumerate(docs, 1):
            print(f"[{i}/{len(docs)}] {docx}", flush=True)
            status, pages = export_one(docx, dry_run=args.dry_run)
            pdf = docx.with_name("source.pdf")
            f.write(f"{docx.parent.name}\t{status}\t{pages}\t{pdf}\n")
            f.flush()
            print(f"  -> {status} pages={pages}", flush=True)
            if not status.endswith("_ok") and status not in {"dry_run"}:
                print(f"Stopping after failure: {docx}", file=sys.stderr)
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
