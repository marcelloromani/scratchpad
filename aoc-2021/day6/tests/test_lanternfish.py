import copy
import unittest

from main import world_state_next_day, world_state_next_days, fish_count_after_days


class TestWorldState(unittest.TestCase):

    def test_next_day(self):
        test_cases = [
            {
                "current": [1],
                "next": [0],
            },
            {
                "current": [0],
                "next": [6, 8]
            },
        ]
        for t in test_cases:
            w = copy.deepcopy(t["current"])
            world_state_next_day(w)
            self.assertListEqual(t["next"], w, t["current"])

    def test_next_days(self):
        test_cases = [
            {
                "current": [1],
                "next": [0],
                "days": 1,
            },
            {
                "current": [1],
                "next": [6, 8],
                "days": 2,
            },
        ]
        for t in test_cases:
            w = copy.deepcopy(t["current"])
            world_state_next_days(w, t["days"])
            self.assertListEqual(t["next"], w, f"{t['current']} {t['days']}")

    def test_sample_input(self):
        w = [3, 4, 3, 1, 2]
        final = [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]
        days = 18
        world_state_next_days(w, days)
        self.assertListEqual(final, w)

    def test_fish_count_after_days_a(self):
        w = [3, 4, 3, 1, 2]
        self.assertEqual(26, fish_count_after_days(w, 18))

    def test_fish_count_after_days_b(self):
        w = [3, 4, 3, 1, 2]
        self.assertEqual(5934, fish_count_after_days(w, 80))


if __name__ == '__main__':
    unittest.main()
