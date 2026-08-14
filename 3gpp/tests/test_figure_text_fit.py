""" @file test_figure_text_fit.py
    @brief 测试 tools.figures.figure_text_fit 模块——换行文本的孤儿标点重平衡功能。
    @date 2025 """

import unittest

from PIL import Image, ImageDraw, ImageFont

from tools.archive_python_drawing.figures.figure_text_fit import wrap_text


def _font(size: int = 22) -> ImageFont.FreeTypeFont:
    """ @brief 加载 Noto Sans CJK 常规字体。
        @param size 字号（像素），默认 22。
        @return PIL FreeTypeFont 对象。
    """
    return ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", size=size)


class FigureTextFitHelperTests(unittest.TestCase):
    """ @brief 测试 figure_text_fit 模块：验证 wrap_text 的孤儿中文标点重平衡逻辑。 """

    def test_wrap_text_rebalances_orphan_chinese_punctuation(self) -> None:
        """ @brief 验证 wrap_text 能将行尾孤立的句号（。）重平衡到上一行，确保末行至少包含 3 个字符。 """
        img = Image.new("RGB", (500, 200), "white")
        draw = ImageDraw.Draw(img)
        fnt = _font()

        text = "减 β 后截零，弱消息会被压到 0，β 过大会损失信息。"
        lines = wrap_text(draw, text, fnt, 284)

        self.assertGreater(len(lines), 1)
        self.assertNotEqual(lines[-1], "。")
        self.assertGreaterEqual(len(lines[-1].strip()), 3)


if __name__ == "__main__":
    unittest.main()
