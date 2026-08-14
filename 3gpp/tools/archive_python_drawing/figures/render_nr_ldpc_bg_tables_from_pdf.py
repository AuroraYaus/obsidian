#!/usr/bin/env python3
"""@file render_nr_ldpc_bg_tables_from_pdf.py
@brief 从 TS 38.212 本地渲染 PDF 中裁剪拼接 LDPC BG1/BG2 移位表图片
@date 2026-07-19
@note 设计意图：使用 pdftoppm 将 PDF 源文件的第 21-24 页光栅化，然后按预定坐标裁剪、
  拼接表格片段，输出完整移位表（给 L1 讲义）和分段清晰表（给 L2 讲义）。
@see docs/L1_基础/T3.4_TS38.212_BG_shift_tables.md
@see docs/L2_协议算法/T8.3_TS38.212_BG_shift_table_detail.md
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[3]
PDF = ROOT / "3GPP_Rel19/processed/TS_38.212_38212-j30/source.pdf"
L1_ASSET_DIR = ROOT / "docs/L1_基础/assets"
L2_ASSET_DIR = ROOT / "docs/L2_协议算法/assets"

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
    """@brief 用 pdftoppm 将 PDF 源文件第 21-24 页渲染为 PNG
    @param tmpdir 输出临时目录
    @throws FileNotFoundError PDF 源文件不存在时抛出
    @throws RuntimeError pdftoppm 命令行工具不可用时抛出
    @note 渲染分辨率 220 DPI，文件名格式 ts38212-{页码}.png"""
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
    """@brief 将指定基图的多个片段裁剪拼接为完整表格图片
    @param tmpdir 含渲染 PNG 的临时目录
    @param key 基图标识："bg1" 或 "bg2"
    @return 拼接完成的 PIL Image 对象
    @note 裁剪区域 x 坐标固定 [170, 1650]，片段间留 28px 间距，四周留 40px 白边"""
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
    """@brief 保存每个片段为独立的 L2 讲义用表格图片
    @param tmpdir 含渲染 PNG 的临时目录
    @param key 基图标识："bg1" 或 "bg2"
    @note 每个片段单独裁剪并加 40px 白边保存"""
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
    """@brief 从 TS 38.212 PDF 中提取并拼接 BG1/BG2 移位表图片
    @usage python3 tools/figures/render_nr_ldpc_bg_tables_from_pdf.py
    @args  无参数
    @env  需要 PIL/Pillow、pdftoppm（poppler-utils）、
         TS 38.212 本地渲染 PDF source.pdf（3GPP_Rel19/processed/TS_38.212_38212-j30/）
    @exit_code 0 = 成功；非 0 = pdftoppm 渲染失败（由 check=True 传播）
    @note 输出产物：对 BG1 和 BG2 各生成一张完整拼接图和若干张分段清晰图，
      分别放入 docs/L1_基础/assets/ 和 docs/L2_协议算法/assets/
    @throws subprocess.CalledProcessError pdftoppm 渲染失败时由 check=True 传播"""
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
