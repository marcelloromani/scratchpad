import copy
import unittest

from main import is_hor, is_ver, apply_line


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


if __name__ == '__main__':
    unittest.main()
