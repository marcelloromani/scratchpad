import unittest

from main import most_common_bits, purge_blanks


class TestCommonBits(unittest.TestCase):

    def test_purge_blanks(self):
        test_cases = [
            {
                "data": ["0\n"],
                "expected": ["0"],
            },
            {
                "data": ["0\n", "   \n", "   "],
                "expected": ["0"],
            },
            {
                "data": [" \n", " 11  \n", "   01"],
                "expected": ["11", "01"],
            },
        ]
        for t in test_cases:
            data = t["data"]
            expected = t["expected"]
            actual = purge_blanks(data)
            self.assertListEqual(expected, list(actual), data)

    def test_common_bit(self):
        test_cases = [
            {
                "data": ["0"],
                "expected": "0",
            },
            {
                "data": ["1"],
                "expected": "1",
            },
            {
                "data": ["0", "0", "0"],
                "expected": "0",
            },
            {
                "data": ["1", "1", "1"],
                "expected": "1",
            },
            {
                "data": ["0", "0", "1"],
                "expected": "0",
            },
            {
                "data": ["1", "1", "0"],
                "expected": "1",
            },
            {
                "data": ["00", "11", "10"],
                "expected": "10",
            },
            {
                "data": ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
                         "00010", "01010"],
                "expected": "10110",
            },
        ]
        for t in test_cases:
            data = t["data"]
            expected = t["expected"]
            actual = most_common_bits(data)
            self.assertEqual(expected, actual, data)


if __name__ == '__main__':
    unittest.main()
