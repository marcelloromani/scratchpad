import unittest

from main import parse_moves, multiply_hor_depth, Move


class TestMoveSubmarine(unittest.TestCase):

    def test_next_pos_f(self):
        m = Move("forward", 5)
        h, d = m.next_pos(10, 20)
        self.assertEqual(15, h)
        self.assertEqual(20, d)

    def test_next_pos_d(self):
        m = Move("down", 5)
        h, d = m.next_pos(10, 20)
        self.assertEqual(10, h)
        self.assertEqual(25, d)

    def test_next_pos_u(self):
        m = Move("up", 5)
        h, d = m.next_pos(10, 20)
        self.assertEqual(10, h)
        self.assertEqual(15, d)

    def test_moves(self):
        tests_cases = [
            {
                "data": ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"],
                "expected": 150,
            },
        ]
        for t in tests_cases:
            expected = t["expected"]
            moves = parse_moves(t["data"])
            actual = multiply_hor_depth(moves)
            self.assertEqual(expected, actual, t["data"])


if __name__ == '__main__':
    unittest.main()
