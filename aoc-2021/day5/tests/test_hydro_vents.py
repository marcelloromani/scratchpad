import copy
import unittest

from main import is_hor, is_ver, apply_line, apply_lines, count_lines_overlap


class TestLines(unittest.TestCase):

    def test_hor(self):
        self.assertTrue(is_hor((0, 0, 1, 0)))
        self.assertTrue(is_hor((3, 2, 5, 2)))
        self.assertFalse(is_hor((1, 1, 5, 5)))

    def test_ver(self):
        self.assertTrue(is_ver((2, 5, 2, 9)))
        self.assertFalse(is_ver((1, 1, 6, 1)))


class TestApplyLinesToBoard(unittest.TestCase):
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    def test_functional(self):
        """
        Ensures that applying a line to the board doesn't change the board passed in as argument.
        """
        board_before = copy.deepcopy(self.board)
        b = apply_line(self.board, (1, 0, 1, 1))
        self.assertIsNot(self.board, b)
        self.assertListEqual(board_before, self.board)

    def test_apply_line(self):
        test_cases = [
            {
                "line": (1, 1, 2, 1),
                "expected": [
                    [0, 0, 0],
                    [0, 1, 1],
                    [0, 0, 0],
                ]
            },
            {
                "line": (0, 0, 0, 2),
                "expected": [
                    [1, 0, 0],
                    [1, 0, 0],
                    [1, 0, 0],
                ]
            },
        ]
        for t in test_cases:
            actual = apply_line(self.board, t["line"])
            self.assertListEqual(t["expected"], actual, t["line"])

    def test_apply_lines(self):
        test_cases = [
            {
                "lines": [
                    (1, 1, 2, 1)
                ],
                "expected": [
                    [0, 0, 0],
                    [0, 1, 1],
                    [0, 0, 0],
                ]
            },
            {
                "lines": [
                    (0, 0, 0, 2),
                    (0, 1, 2, 1),
                ],
                "expected": [
                    [1, 0, 0],
                    [2, 1, 1],
                    [1, 0, 0],
                ]
            },
            {
                "lines": [
                    (0, 0, 0, 2),
                    (0, 1, 2, 1),
                    (0, 1, 1, 1),
                ],
                "expected": [
                    [1, 0, 0],
                    [3, 2, 1],
                    [1, 0, 0],
                ]
            },
        ]
        for t in test_cases:
            actual = apply_lines(self.board, t["lines"])
            self.assertListEqual(t["expected"], actual, t["lines"])


class TestIdentifyPoints(unittest.TestCase):

    def test_apply_lines(self):
        test_cases = [
            {
                "board": [
                    [0, 0],
                    [0, 1],
                ],
                "expected": 0,
            },
            {
                "board": [
                    [2, 0],
                    [3, 1],
                ],
                "expected": 2,
            },
        ]
        for t in test_cases:
            actual = count_lines_overlap(t["board"])
            self.assertEqual(t["expected"], actual, t["board"])


if __name__ == '__main__':
    unittest.main()
