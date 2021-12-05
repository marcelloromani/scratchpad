import unittest

from main import parse_moves, multiply_hor_depth, Move


class TestMoveSubmarine(unittest.TestCase):

    def test_next_pos_f_aim_zero(self):
        m = Move("forward", 5)
        h, d, a = m.next_pos(10, 20, 0)
        self.assertEqual(15, h)
        self.assertEqual(20, d)
        self.assertEqual(0, a)

    def test_next_pos_f_aim_nonzero(self):
        m = Move("forward", 5)
        h, d, a = m.next_pos(10, 20, 3)
        self.assertEqual(15, h)
        self.assertEqual(35, d)
        self.assertEqual(3, a)

    def test_next_pos_d(self):
        m = Move("down", 5)
        h, d, a = m.next_pos(10, 20, 0)
        self.assertEqual(10, h)
        self.assertEqual(20, d)
        self.assertEqual(5, a)

    def test_next_pos_u(self):
        m = Move("up", 5)
        h, d, a = m.next_pos(10, 20, 0)
        self.assertEqual(10, h)
        self.assertEqual(20, d)
        self.assertEqual(-5, a)

    def test_moves(self):
        tests_cases = [
            {
                "data": ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"],
                "expected": 900,
            },
        ]
        for t in tests_cases:
            expected = t["expected"]
            moves = parse_moves(t["data"])
            actual = multiply_hor_depth(moves)
            self.assertEqual(expected, actual, t["data"])


if __name__ == '__main__':
    unittest.main()
