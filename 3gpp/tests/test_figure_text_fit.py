import unittest

from PIL import Image, ImageDraw, ImageFont

from tools.figures.figure_text_fit import wrap_text


def _font(size: int = 22) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", size=size)


class FigureTextFitHelperTests(unittest.TestCase):
    def test_wrap_text_rebalances_orphan_chinese_punctuation(self) -> None:
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
