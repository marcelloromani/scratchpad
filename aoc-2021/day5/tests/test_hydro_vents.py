import copy
import unittest

from main import is_hor, is_ver, is_diag45, apply_line, apply_lines, count_lines_overlap, parse_line, read_input, \
    required_board_size, day5_part1, day5_part2, init_board, LineTypeNotSupported


class TestInitBoard(unittest.TestCase):

    def test_init_board(self):
        expected = [
            [0, 0],
            [0, 0],
        ]
        actual = init_board(2, 2)
        self.assertListEqual(expected, actual)

    def test_modify_row(self):
        expected = [
            [0, 0],
            [1, 1],
        ]
        actual = init_board(2, 2)
        actual[1][0] += 1
        actual[1][1] += 1
        self.assertListEqual(expected, actual)


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

    def test_diag45(self):
        self.assertTrue(is_diag45((1, 1, 5, 5)))
        self.assertTrue(is_diag45((1, 3, 3, 1)))
        self.assertFalse(is_diag45((1, 3, 5, 3)))


class TestApplyLinesToBoard(unittest.TestCase):
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    def test_functional_hor(self):
        """
        Ensures that applying a line to the board doesn't change the board passed in as argument.
        """
        line = (1, 1, 2, 1)
        self.assertTrue(is_hor(line))
        board_before = copy.deepcopy(self.board)
        b = apply_line(self.board, line)
        self.assertIsNot(self.board, b)
        self.assertListEqual(board_before, self.board)

    def test_functional_ver(self):
        """
        Ensures that applying a line to the board doesn't change the board passed in as argument.
        """
        line = (1, 1, 1, 2)
        self.assertTrue(is_ver(line))
        board_before = copy.deepcopy(self.board)
        b = apply_line(self.board, line)
        self.assertIsNot(self.board, b)
        self.assertListEqual(board_before, self.board)

    def test_functional_diag45(self):
        """
        Ensures that applying a line to the board doesn't change the board passed in as argument.
        """
        line = (1, 1, 2, 2)
        self.assertTrue(is_diag45(line))
        board_before = copy.deepcopy(self.board)
        b = apply_line(self.board, line, diag=True)
        self.assertIsNot(self.board, b)
        self.assertListEqual(board_before, self.board)

    def test_apply_line_hor_ver(self):
        test_cases = [
            {
                "desc": "hor left -> right",
                "line": (1, 1, 2, 1),
                "expected": [
                    [0, 0, 0],
                    [0, 1, 1],
                    [0, 0, 0],
                ]
            },
            {
                "desc": "ver top -> bottom",
                "line": (1, 0, 1, 1),
                "expected": [
                    [0, 1, 0],
                    [0, 1, 0],
                    [0, 0, 0],
                ]
            },
            {
                "desc": "ver top -> bottom",
                "line": (0, 0, 0, 2),
                "expected": [
                    [1, 0, 0],
                    [1, 0, 0],
                    [1, 0, 0],
                ]
            },
            {
                "desc": "hor right -> left",
                "line": (2, 1, 0, 1),
                "expected": [
                    [0, 0, 0],
                    [1, 1, 1],
                    [0, 0, 0],
                ]
            },
        ]
        for t in test_cases:
            actual = apply_line(self.board, t["line"])
            self.assertListEqual(t["expected"], actual, f"{t['line']} {t['desc']}")

    def test_reject_diag45(self):
        line = (0, 0, 2, 2)
        self.assertTrue(is_diag45(line))  # sanity check on test data
        self.assertRaises(LineTypeNotSupported, apply_line, self.board, line)

    def test_apply_line_diag45(self):
        test_cases = [
            {
                "desc": "diag topLeft -> botRight",
                "line": (0, 0, 2, 2),
                "expected": [
                    [1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                ]
            },
            {
                "desc": "diag botRight -> topLeft",
                "line": (2, 2, 0, 0),
                "expected": [
                    [1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                ]
            },
            {
                "desc": "diag topRight -> botLeft",
                "line": (2, 0, 0, 2),
                "expected": [
                    [0, 0, 1],
                    [0, 1, 0],
                    [1, 0, 0],
                ]
            },
            {
                "desc": "diag botLeft -> topRight",
                "line": (0, 2, 2, 0),
                "expected": [
                    [0, 0, 1],
                    [0, 1, 0],
                    [1, 0, 0],
                ]
            },
            {
                "desc": "diag topLeft -> botRight",
                "line": (1, 1, 2, 2),
                "expected": [
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                ]
            },
            {
                "desc": "diag botRight -> topLeft",
                "line": (2, 2, 1, 1),
                "expected": [
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                ]
            },
        ]
        for t in test_cases:
            actual = apply_line(self.board, t["line"], diag=True)
            self.assertListEqual(t["expected"], actual, f"{t['line']} {t['desc']}")

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


class TestSampleInput(unittest.TestCase):
    file = "sample_input.txt"

    def test_board_size(self):
        with open(self.file, 'r') as f:
            lines = read_input(f)
            row_count, col_count = required_board_size(lines)
            self.assertEqual((10, 10), (row_count, col_count))

    def test_board(self):
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
        ]
        with open(self.file, 'r') as f:
            lines = read_input(f)
            row_count, col_count = required_board_size(lines)
            board = init_board(row_count, col_count)
            board = apply_lines(board, lines)
            self.assertListEqual(expected, board)

    def test_day5_part1(self):
        expected = 5
        with open(self.file, 'r') as f:
            actual = day5_part1(f)
        self.assertEqual(expected, actual)

    def test_day5_part2(self):
        expected = 12
        with open(self.file, 'r') as f:
            actual = day5_part2(f)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
