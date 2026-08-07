"""
@file test_crc.py
@brief CRC（循环冗余校验）多项式长除法的单元测试
@date 2026-07-19

测试 crc.py 中所有公开函数的正确性：
- poly_div_mod2 — 多项式长除法（手算验证）
- crc_remainder / crc_attach / crc_check 的端到端流程
- 单比特错误检测能力
- 全零消息和短消息的边界情况
- 非法输入校验（无效生成多项式、float/bool 输入）

使用 Python 标准库 unittest 框架，无需外部依赖。

@see crc.py — 被测模块
"""

import unittest

from crc import crc_attach, crc_check, crc_remainder, poly_div_mod2


class CRCTests(unittest.TestCase):
    """@brief CRC 运算的单元测试套件"""

    def test_poly_div_mod2_matches_hand_worked_example(self) -> None:
        """@brief 多项式长除法的结果与手算对照验证

        x^7+x^4+x^3 除以 x^3+x+1：
        dividend = [1,0,0,1,1,0,0,0], generator = [1,0,1,1]
        手算余式 = [1,0,0]（即 x^2）
        """
        dividend = [1, 0, 0, 1, 1, 0, 0, 0]
        generator = [1, 0, 1, 1]

        self.assertEqual(poly_div_mod2(dividend, generator), [1, 0, 0])

    def test_crc_attach_and_check_match_hand_worked_example(self) -> None:
        """@brief CRC 编码 → 校验的完整流程验证

        消息 [1,0,0,1,1] + 生成多项式 [1,0,1,1] →
        余式 [1,0,0] → 码字 [1,0,0,1,1,1,0,0] → crc_check 应返回 True
        """
        message = [1, 0, 0, 1, 1]
        generator = [1, 0, 1, 1]

        self.assertEqual(crc_remainder(message, generator), [1, 0, 0])
        self.assertEqual(crc_attach(message, generator), [1, 0, 0, 1, 1, 1, 0, 0])
        self.assertTrue(crc_check(crc_attach(message, generator), generator))

    def test_crc_check_rejects_single_bit_error(self) -> None:
        """@brief 单比特翻转应被 CRC 检测到

        在正确码字中翻转一个比特 → crc_check 应返回 False。
        CRC 能检测所有单比特错误（只要生成多项式至少有两项）。
        """
        message = [1, 0, 0, 1, 1]
        generator = [1, 0, 1, 1]
        codeword = crc_attach(message, generator)

        codeword[3] ^= 1

        self.assertFalse(crc_check(codeword, generator))

    def test_crc_handles_all_zero_and_short_messages(self) -> None:
        """@brief 全零消息和短消息的边界测试

        全零消息 → 余式也为全零 → 码字通过校验。
        两位短消息 [1,1] 也应正确编码和校验。
        """
        generator = [1, 0, 1, 1]

        self.assertEqual(crc_remainder([0, 0, 0, 0], generator), [0, 0, 0])
        self.assertTrue(crc_check(crc_attach([0, 0, 0, 0], generator), generator))
        self.assertTrue(crc_check(crc_attach([1, 1], generator), generator))

    def test_invalid_generator_is_rejected(self) -> None:
        """@brief 非法生成多项式应抛出 ValueError

        首项为 0 → 生成多项式必须以 1 开头（首一多项式）。
        长度 < 2 → 度至少为 1（deg=0 的 CRC 无意义）。
        """
        with self.assertRaises(ValueError):
            crc_remainder([1, 0, 1], [0, 1, 1])
        with self.assertRaises(ValueError):
            crc_remainder([1, 0, 1], [1])

    def test_dividend_length_equals_generator_length(self) -> None:
        """@brief 被除数长度等于生成多项式长度时的边界情况

        当被除数和生成多项式等长时，余式 = deg(generator)-1 位（此处为 3 位）。
        """
        generator = [1, 0, 1, 1]
        self.assertEqual(poly_div_mod2([1, 0, 0, 1], generator), [0, 1, 0])

    def test_float_input_is_rejected(self) -> None:
        """@brief float 类型输入应被拒绝"""
        with self.assertRaises(ValueError):
            crc_remainder([0.0, 1.0, 0.0, 1.0], [1, 0, 1, 1])

    def test_bool_input_is_rejected(self) -> None:
        """@brief bool 类型输入应被拒绝（bool 是 int 子类但不属于 GF(2) 语境）"""
        with self.assertRaises(ValueError):
            crc_remainder([True, False, True, False], [1, 0, 1, 1])


if __name__ == "__main__":
    unittest.main()
