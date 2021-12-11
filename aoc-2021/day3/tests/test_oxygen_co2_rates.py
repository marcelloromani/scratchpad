import unittest

from main import oxygen_co2_rate, bit_count_in_position, BitSelectionPolicy, filter_data


class TestOxygenCO2(unittest.TestCase):

    def test_bit_count_in_position(self):
        test_cases = [
            {
                "data": ["00", "01", "11"],
                "position": 0,
                "expected": (1, 2),
            },
            {
                "data": ["00", "01", "11"],
                "position": 1,
                "expected": (2, 1),
            },
        ]
        for t in test_cases:
            actual = bit_count_in_position(t["data"], t["position"])
            self.assertEqual(t["expected"], actual, t["data"])

    def test_filter_data(self):
        test_cases = [
            {
                "data": ["00", "10", "11"],
                "position": 1,
                "policy": BitSelectionPolicy.MOST_COMMON,
                "expected": ["10", "11"],
            },
            {
                "data": ["00", "10", "11"],
                "position": 1,
                "policy": BitSelectionPolicy.LEAST_COMMON,
                "expected": ["00"],
            },
            {
                "data": ["00", "10", "11"],
                "position": 0,
                "policy": BitSelectionPolicy.MOST_COMMON,
                "expected": ["00", "10"],
            },
            {
                "data": ["00", "10", "11"],
                "position": 0,
                "policy": BitSelectionPolicy.LEAST_COMMON,
                "expected": ["11"],
            },
            {
                "data": ["10", "11", "01"],
                "position": 0,
                "policy": BitSelectionPolicy.LEAST_COMMON,
                "expected": ["10"],
            },
            {
                "data": ["10", "11", "01"],
                "position": 1,
                "policy": BitSelectionPolicy.LEAST_COMMON,
                "expected": ["01"],
            },
        ]
        for t in test_cases:
            actual = filter_data(t["data"], t["position"], t["policy"])
            self.assertListEqual(t["expected"], actual, t["data"])

    def test_oxygen_co2_rates(self):
        test_cases = [
            {
                "data": ["00000"],
                "expected": (0, 0),
            },
            {
                "data": ["00100"],
                "expected": (4, 4),
            },
            {
                "data": ["10", "11", "01"],
                "expected": (3, 1),
            },
            {
                "data": ["10", "00", "01"],
                "expected": (1, 2),
            },
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
