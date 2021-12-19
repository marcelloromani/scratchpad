import copy
import unittest

from main import is_hor, is_ver, apply_line, apply_lines, count_lines_overlap, parse_line, read_input, \
    required_board_size, day5_part1, init_board


class TestReadInput(unittest.TestCase):

    def test_parse_line(self):
        line = "6,4 -> 2,0"
        expected = (6, 4, 2, 0)
        self.assertEqual(expected, parse_line(line))

    def test_parse_line_blanks(self):
        line = "    6, 4  ->   2, 0   "
        expected = (6, 4, 2, 0)
        self.assertEqual(expected, parse_line(line))

    def test_read_input_file(self):
        expected = [
            (0, 9, 5, 9),
            (8, 0, 0, 8),
        ]
        filename = 'input_00.txt'
        with open(filename) as f:
            actual = read_input(f)
        self.assertListEqual(expected, actual, filename)

    def test_get_board_required_size(self):
        test_cases = [
            {
                "lines": [
                    (1, 1, 2, 1),
                    (3, 2, 0, 6),
                ],
                "expected": (7, 4),
            },
        ]
        for t in test_cases:
            actual = required_board_size(t["lines"])
            self.assertEqual(t["expected"], actual, t["lines"])


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

    def test_reject_diagonal_lines(self):
        lines = [
            (0, 1, 2, 1),  # OK (horizontal)
            (0, 0, 2, 2),  # not OK (diagonal)
        ]
        board = init_board(3, 3)
        apply_lines(board, lines)


class TestIdentifyPoints(unittest.TestCase):

    def count_where_lines_overlap(self):
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


class TestEnd2End(unittest.TestCase):
    file = "sample_input.txt"

    def test_board_size(self):
        with open(self.file, 'r') as f:
            lines = read_input(f)
            row_count, col_count = required_board_size(lines)
            self.assertEqual((10, 10), (row_count, col_count))

    def test_final_value(self):
        expected = 5
        with open(self.file, 'r') as f:
            actual = day5_part1(f)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
