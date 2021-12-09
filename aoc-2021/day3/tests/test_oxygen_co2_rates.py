import unittest

from main import oxygen_co2_rate


class TestOxygenCO2(unittest.TestCase):

    def test_oxygen_co2_rates(self):
        test_cases = [
            {
                "data": ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
                         "00010", "01010"],
                "expected": (23, 10),
            },
        ]
        for t in test_cases:
            data = t["data"]
            expected = t["expected"]
            actual = oxygen_co2_rate(data)
            self.assertEqual(expected, actual, data)


if __name__ == '__main__':
    unittest.main()
