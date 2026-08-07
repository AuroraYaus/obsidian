"""
@file test_gf2.py
@brief GF(2) 线性代数运算的单元测试
@date 2026-07-19

测试 gf2.py 中所有公开函数的正确性：
- GF(2) 加法（gf2_add = XOR）
- GF(2) 矩阵乘法（gf2_matmul）
- GF(2) 矩阵求秩（gf2_rank，高斯消元）
- Hamming(7,4) 编码与伴随式计算（端到端集成测试）
- 输入校验（拒绝空矩阵、非矩形矩阵、float/bool 输入）

使用 Python 标准库 unittest 框架，无需外部依赖。

@see gf2.py — 被测模块
"""

import unittest

from gf2 import encode_linear_block, gf2_add, gf2_matmul, gf2_rank, syndrome


class GF2Tests(unittest.TestCase):
    """@brief GF(2) 运算的单元测试套件"""

    def test_gf2_add_is_xor(self) -> None:
        """@brief 验证 gf2_add 在四种输入组合下等价于 XOR"""
        self.assertEqual(gf2_add(0, 0), 0)
        self.assertEqual(gf2_add(0, 1), 1)
        self.assertEqual(gf2_add(1, 0), 1)
        self.assertEqual(gf2_add(1, 1), 0)

    def test_gf2_matmul_uses_and_then_xor_reduction(self) -> None:
        """@brief 验证矩阵乘法：每个输出位 = AND 累加 + XOR 归约

        测试用例：2×3 矩阵 × 3×2 矩阵 = 2×2 结果。
        a[0] = [1,0,1], b 第 0 列 = [1,0,1]^T → (1&1)^(0&0)^(1&1) = 1^0^1 = 0
        """
        a = [
            [1, 0, 1],
            [0, 1, 1],
        ]
        b = [
            [1, 1],
            [0, 1],
            [1, 0],
        ]
        self.assertEqual(gf2_matmul(a, b), [[0, 1], [1, 1]])

    def test_gf2_rank_counts_independent_rows(self) -> None:
        """@brief 验证含全零行的矩阵秩为 2

        4×4 矩阵中含一行全零，前 3 行中 1 行可由其余线性表示，
        因此独立行数 = 2。
        """
        matrix = [
            [1, 0, 1, 1],
            [0, 1, 1, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
        ]
        self.assertEqual(gf2_rank(matrix), 2)

    def test_hamming_7_4_encoding_and_single_bit_syndrome(self) -> None:
        """@brief Hamming(7,4) 端到端测试：编码 + 单比特错误伴随式

        信息位 [1,0,1,1] → 编码 → [1,0,1,1,0,1,0]。
        翻转第 3 位后伴随式应为 [0,1,1]，对应 H 的第 3 列（错误位置）。
        """
        g = [
            [1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1],
        ]
        h = [
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 0, 1],
        ]

        u = [1, 0, 1, 1]
        codeword = encode_linear_block(u, g)
        self.assertEqual(codeword, [1, 0, 1, 1, 0, 1, 0])
        self.assertEqual(syndrome(codeword, h), [0, 0, 0])

        received = codeword[:]
        received[2] ^= 1
        self.assertEqual(syndrome(received, h), [0, 1, 1])

    def test_encode_linear_block_rejects_empty_u(self) -> None:
        """@brief 空信息向量应抛出 ValueError"""
        g = [[1, 0, 0, 0, 1, 1, 0]]
        with self.assertRaises(ValueError):
            encode_linear_block([], g)

    def test_syndrome_rejects_empty_r(self) -> None:
        """@brief 空接收向量应抛出 ValueError"""
        h = [[1, 0, 1]]
        with self.assertRaises(ValueError):
            syndrome([], h)

    def test_syndrome_rejects_length_mismatch(self) -> None:
        """@brief 接收向量长度 ≠ 校验矩阵列数时应抛出 ValueError"""
        h = [[1, 0, 1, 1]]
        with self.assertRaises(ValueError):
            syndrome([1, 0, 1], h)

    def test_require_bit_rejects_float(self) -> None:
        """@brief float 输入应被 _require_bit 拒绝"""
        with self.assertRaises(ValueError):
            gf2_add(0.0, 1)

    def test_require_bit_rejects_bool(self) -> None:
        """@brief bool 输入应被拒绝（bool 是 int 子类但不属于 GF(2) 语境）"""
        with self.assertRaises(ValueError):
            gf2_add(True, False)

    def test_gf2_rank_empty_matrix(self) -> None:
        """@brief 空矩阵的秩为 0"""
        self.assertEqual(gf2_rank([]), 0)

    def test_gf2_rank_full_rank(self) -> None:
        """@brief 单位矩阵的秩等于其维度（满秩）"""
        matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
        self.assertEqual(gf2_rank(matrix), 3)

    def test_gf2_matmul_non_rectangular_is_rejected(self) -> None:
        """@brief 非矩形矩阵应抛出 ValueError"""
        a = [[1, 0], [1]]
        b = [[1], [0]]
        with self.assertRaises(ValueError):
            gf2_matmul(a, b)


if __name__ == "__main__":
    unittest.main()
