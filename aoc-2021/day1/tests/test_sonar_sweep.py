import unittest

from main import count_increases, parse_int_array


class SonarSweepTest(unittest.TestCase):

    def test_increase_count_empty(self):
        tests_cases = [
            {
                "data": [],
                "expected": 0
            },
            {
                "data": [100],
                "expected": 0
            },
            {
                "data": [100, 101],
                "expected": 1
            },
            {
                "data": [100, 90],
                "expected": 0
            },
            {
                "data": [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],
                "expected": 7
            },
        ]
        for t in tests_cases:
            expected = t["expected"]
            actual = count_increases(t["data"])
            self.assertEqual(expected, actual, t["data"])

    def test_read_array(self):
        test_cases = [
            {
                "data": [],
                "expected": [],
            },
            {
                "data": ["10"],
                "expected": [10],
            },
            {
                "data": ["10\n"],
                "expected": [10],
            },
            {
                "data": [" 10 \n"],
                "expected": [10],
            },
            {
                "data": [" 10", "\n15"],
                "expected": [10, 15],
            },
        ]
        for t in test_cases:
            expected = t["expected"]
            actual = parse_int_array(t["data"])
            self.assertListEqual(expected, actual, t["data"])


if __name__ == '__main__':
    unittest.main()
