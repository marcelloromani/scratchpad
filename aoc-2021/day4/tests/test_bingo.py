import unittest

from main import num_pos_in_board, is_winning_board, parse_board, read_input, find_winning_board, sum_unmarked_nums


class TestBoard(unittest.TestCase):

    def test_get_num_position(self):
        board = [
            [1, 2],
            [3, 4],
        ]
        test_cases = [
            {
                "n": 1,
                "pos": (0, 0),
            },
            {
                "n": 2,
                "pos": (0, 1),
            },
            {
                "n": 3,
                "pos": (1, 0),
            },
            {
                "n": 4,
                "pos": (1, 1),
            },
            {
                "n": 5,
                "pos": (-1, -1),
            },
        ]
        for t in test_cases:
            self.assertEqual(t["pos"], num_pos_in_board(board, t["n"]), t["n"])

    def test_is_board_winning_2x2(self):
        board = [
            [1, 2],
            [3, 4],
        ]
        test_cases = [
            {
                "nums": [1, 2],
                "win": True,
                "drawn": [1, 2],
            },
            {
                "nums": [3, 4],
                "win": True,
                "drawn": [3, 4],
            },
            {
                "nums": [1, 3],
                "win": True,
                "drawn": [1, 3],
            },
            {
                "nums": [2, 4],
                "win": True,
                "drawn": [2, 4],
            },
            {
                "nums": [1, 4],
                "win": False,
                "drawn": [1, 4],
            },
            {
                "nums": [2, 3],
                "win": False,
                "drawn": [2, 3],
            },
            {
                "nums": [2, 3, 4, 5],
                "win": True,
                "drawn": [2, 3, 4],
            },
            {
                "nums": [1, 2, 3, 4],
                "win": True,
                "drawn": [1, 2],
            },
            {
                "nums": [1, 2, 7, 8],
                "win": True,
                "drawn": [1, 2],
            },
        ]
        for t in test_cases:
            is_winning, drawn_nums = is_winning_board(board, t["nums"])
            self.assertEqual(t["win"], is_winning, t["nums"])
            self.assertListEqual(t["drawn"], drawn_nums, t["nums"])

    def test_find_winning_board(self):
        board0 = [
            [1, 2],
            [3, 4],
        ]
        board1 = [
            [5, 6],
            [7, 8],
        ]
        boards = [board0, board1]
        test_cases = [
            {
                "nums": [1, 2],
                "winning": board0,
                "drawn": [1, 2],
            },
            {
                "nums": [6, 8],
                "winning": board1,
                "drawn": [6, 8],
            },
            {
                "nums": [9, 9, 1, 2],
                "winning": board0,
                "drawn": [9, 9, 1, 2],
            },
            {
                "nums": [9, 9, 5, 7],
                "winning": board1,
                "drawn": [9, 9, 5, 7],
            },
            {
                "nums": [5, 8, 2, 9, 7, 22],
                "winning": board1,
                "drawn": [5, 8, 2, 9, 7],
            },
        ]
        for t in test_cases:
            winning_board, drawn_nums = find_winning_board(boards, t["nums"])
            self.assertListEqual(t["winning"], winning_board, t["nums"])
            self.assertListEqual(t["drawn"], drawn_nums, t["nums"])

    def test_sum_unmarked(self):
        board = [
            [1, 2],
            [3, 4],
        ]
        test_cases = [
            {
                "nums": [],
                "sum": 10,
            },
            {
                "nums": [1],
                "sum": 9,
            },
            {
                "nums": [3],
                "sum": 7,
            },
            {
                "nums": [1, 2, 4],
                "sum": 3,
            },
            {
                "nums": [4, 3, 2, 1],
                "sum": 0,
            },
            {
                "nums": [1, 1, 1, 1],
                "sum": 9,
            },
        ]
        for t in test_cases:
            actual = sum_unmarked_nums(board, t["nums"])
            self.assertEqual(t["sum"], actual, t["nums"])


class TestInput(unittest.TestCase):

    def test_parse_board(self):
        board_txt = """
            22 13 17 11  0
             8  2 23  4 24
            21  9 14 16  7
             6 10  3 18  5
             1 12 20 15 19
        """
        board = [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ]
        self.assertListEqual(board, parse_board(board_txt))

    def test_read_input_00(self):
        file = "input_00.txt"
        numbers = [7, 4, 9]
        boards = [
            [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ]
        ]
        with open(file, "r") as f:
            n, b = read_input(f)
            self.assertListEqual(numbers, n)
            self.assertListEqual(boards, b)

    def test_read_input_01(self):
        file = "input_01.txt"
        numbers = [7, 4, 9]
        boards = [
            [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ]
        ]
        with open(file, "r") as f:
            n, b = read_input(f)
            self.assertListEqual(numbers, n)
            self.assertListEqual(boards, b)

    def test_read_input_02(self):
        file = "input_02.txt"
        numbers = [7, 4, 9]
        boards = [
            [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ],
            [
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6],
            ],
        ]
        with open(file, "r") as f:
            n, b = read_input(f)
            self.assertListEqual(numbers, n)
            self.assertListEqual(boards, b)

    def test_read_input_03(self):
        file = "input_03.txt"
        numbers = [7, 4, 9]
        boards = [
            [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ]
        ]
        with open(file, "r") as f:
            n, b = read_input(f)
            self.assertListEqual(numbers, n)
            self.assertListEqual(boards, b)


if __name__ == '__main__':
    unittest.main()
