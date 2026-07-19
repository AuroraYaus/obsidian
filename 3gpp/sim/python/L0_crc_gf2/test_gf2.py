import unittest

from gf2 import encode_linear_block, gf2_add, gf2_matmul, gf2_rank, syndrome


class GF2Tests(unittest.TestCase):
    def test_gf2_add_is_xor(self):
        self.assertEqual(gf2_add(0, 0), 0)
        self.assertEqual(gf2_add(0, 1), 1)
        self.assertEqual(gf2_add(1, 0), 1)
        self.assertEqual(gf2_add(1, 1), 0)

    def test_gf2_matmul_uses_and_then_xor_reduction(self):
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

    def test_gf2_rank_counts_independent_rows(self):
        matrix = [
            [1, 0, 1, 1],
            [0, 1, 1, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
        ]
        self.assertEqual(gf2_rank(matrix), 2)

    def test_hamming_7_4_encoding_and_single_bit_syndrome(self):
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

    def test_encode_linear_block_rejects_empty_u(self):
        g = [[1, 0, 0, 0, 1, 1, 0]]
        with self.assertRaises(ValueError):
            encode_linear_block([], g)

    def test_syndrome_rejects_empty_r(self):
        h = [[1, 0, 1]]
        with self.assertRaises(ValueError):
            syndrome([], h)

    def test_syndrome_rejects_length_mismatch(self):
        h = [[1, 0, 1, 1]]
        with self.assertRaises(ValueError):
            syndrome([1, 0, 1], h)

    def test_require_bit_rejects_float(self):
        with self.assertRaises(ValueError):
            gf2_add(0.0, 1)

    def test_require_bit_rejects_bool(self):
        with self.assertRaises(ValueError):
            gf2_add(True, False)

    def test_gf2_rank_empty_matrix(self):
        self.assertEqual(gf2_rank([]), 0)

    def test_gf2_rank_full_rank(self):
        matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
        self.assertEqual(gf2_rank(matrix), 3)

    def test_gf2_matmul_non_rectangular_is_rejected(self):
        a = [[1, 0], [1]]
        b = [[1], [0]]
        with self.assertRaises(ValueError):
            gf2_matmul(a, b)


if __name__ == "__main__":
    unittest.main()
