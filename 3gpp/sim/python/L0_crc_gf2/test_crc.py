import unittest

from crc import crc_attach, crc_check, crc_remainder, poly_div_mod2


class CRCTests(unittest.TestCase):
    def test_poly_div_mod2_matches_hand_worked_example(self):
        dividend = [1, 0, 0, 1, 1, 0, 0, 0]
        generator = [1, 0, 1, 1]

        self.assertEqual(poly_div_mod2(dividend, generator), [1, 0, 0])

    def test_crc_attach_and_check_match_hand_worked_example(self):
        message = [1, 0, 0, 1, 1]
        generator = [1, 0, 1, 1]

        self.assertEqual(crc_remainder(message, generator), [1, 0, 0])
        self.assertEqual(crc_attach(message, generator), [1, 0, 0, 1, 1, 1, 0, 0])
        self.assertTrue(crc_check(crc_attach(message, generator), generator))

    def test_crc_check_rejects_single_bit_error(self):
        message = [1, 0, 0, 1, 1]
        generator = [1, 0, 1, 1]
        codeword = crc_attach(message, generator)

        codeword[3] ^= 1

        self.assertFalse(crc_check(codeword, generator))

    def test_crc_handles_all_zero_and_short_messages(self):
        generator = [1, 0, 1, 1]

        self.assertEqual(crc_remainder([0, 0, 0, 0], generator), [0, 0, 0])
        self.assertTrue(crc_check(crc_attach([0, 0, 0, 0], generator), generator))
        self.assertTrue(crc_check(crc_attach([1, 1], generator), generator))

    def test_invalid_generator_is_rejected(self):
        with self.assertRaises(ValueError):
            crc_remainder([1, 0, 1], [0, 1, 1])
        with self.assertRaises(ValueError):
            crc_remainder([1, 0, 1], [1])

    def test_dividend_length_equals_generator_length(self):
        generator = [1, 0, 1, 1]
        self.assertEqual(poly_div_mod2([1, 0, 0, 1], generator), [0, 1, 0])

    def test_float_input_is_rejected(self):
        with self.assertRaises(ValueError):
            crc_remainder([0.0, 1.0, 0.0, 1.0], [1, 0, 1, 1])

    def test_bool_input_is_rejected(self):
        with self.assertRaises(ValueError):
            crc_remainder([True, False, True, False], [1, 0, 1, 1])


if __name__ == "__main__":
    unittest.main()
