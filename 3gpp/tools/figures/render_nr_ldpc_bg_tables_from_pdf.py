#!/usr/bin/env python3
"""Crop TS 38.212 LDPC BG1/BG2 tables from the locally rendered PDF."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT / "3GPP_Rel19/processed/TS_38.212_38212-j30/source.pdf"
L1_ASSET_DIR = ROOT / "docs/L1/assets"
L2_ASSET_DIR = ROOT / "docs/L2/assets"

PAGE_SPECS = {
    "bg1": {
        "pieces": [
            (
                "ts38212-021.png",
                650,
                2408,
                L2_ASSET_DIR / "T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table_part1.png",
            ),
            (
                "ts38212-022.png",
                205,
                2388,
                L2_ASSET_DIR / "T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table_part2.png",
            ),
            (
                "ts38212-023.png",
                205,
                682,
                L2_ASSET_DIR / "T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table_part3.png",
            ),
        ],
        "outputs": [
            L1_ASSET_DIR / "T3.4_TS38.212_Table_5.3.2-2_BG1.png",
            L2_ASSET_DIR / "T8.3_TS38.212_Table_5.3.2-2_BG1_shift_table.png",
        ],
    },
    "bg2": {
        "pieces": [
            (
                "ts38212-023.png",
                720,
                2408,
                L2_ASSET_DIR / "T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table_part1.png",
            ),
            (
                "ts38212-024.png",
                205,
                1350,
                L2_ASSET_DIR / "T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table_part2.png",
            ),
        ],
        "outputs": [
            L1_ASSET_DIR / "T3.4_TS38.212_Table_5.3.2-3_BG2.png",
            L2_ASSET_DIR / "T8.3_TS38.212_Table_5.3.2-3_BG2_shift_table.png",
        ],
    },
}


def render_pages(tmpdir: Path) -> None:
    if not PDF.exists():
        raise FileNotFoundError(f"missing PDF source: {PDF}")
    if shutil.which("pdftoppm") is None:
        raise RuntimeError("pdftoppm is required to rasterize source.pdf")
    subprocess.run(
        [
            "pdftoppm",
            "-r",
            "220",
            "-png",
            "-f",
            "21",
            "-l",
            "24",
            str(PDF),
            str(tmpdir / "ts38212"),
        ],
        check=True,
    )


def make_table_image(tmpdir: Path, key: str) -> Image.Image:
    x0, x1 = 170, 1650
    gap = 28
    crops: list[Image.Image] = []
    for filename, y0, y1, _ in PAGE_SPECS[key]["pieces"]:
        page = Image.open(tmpdir / filename).convert("RGB")
        crops.append(page.crop((x0, y0, x1, y1)))

    width = max(crop.width for crop in crops)
    height = sum(crop.height for crop in crops) + gap * (len(crops) - 1) + 80
    canvas = Image.new("RGB", (width + 80, height), "white")
    y = 40
    for crop in crops:
        x = 40 + (width - crop.width) // 2
        canvas.paste(crop, (x, y))
        y += crop.height + gap
    return canvas


def save_split_table_images(tmpdir: Path, key: str) -> None:
    x0, x1 = 170, 1650
    for filename, y0, y1, output in PAGE_SPECS[key]["pieces"]:
        page = Image.open(tmpdir / filename).convert("RGB")
        crop = page.crop((x0, y0, x1, y1))
        canvas = Image.new("RGB", (crop.width + 80, crop.height + 80), "white")
        canvas.paste(crop, (40, 40))
        output.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(output)
        print(f"WROTE {output} {canvas.size}")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="ts38212_pdf_pages_") as tmp:
        tmpdir = Path(tmp)
        render_pages(tmpdir)
        for key in ("bg1", "bg2"):
            image = make_table_image(tmpdir, key)
            for output in PAGE_SPECS[key]["outputs"]:
                output.parent.mkdir(parents=True, exist_ok=True)
                image.save(output)
                print(f"WROTE {output} {image.size}")
            save_split_table_images(tmpdir, key)


if __name__ == "__main__":
    main()
