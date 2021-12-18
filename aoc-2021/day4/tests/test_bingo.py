import unittest

from main import num_pos_in_board, is_winning_board, parse_board, read_input


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

    def test_is_board_winning(self):
        board = [
            [1, 2],
            [3, 4],
        ]
        test_cases = [
            {
                "nums": [1, 2],
                "win": True,
            },
            {
                "nums": [3, 4],
                "win": True,
            },
            {
                "nums": [1, 3],
                "win": True,
            },
            {
                "nums": [2, 4],
                "win": True,
            },
            {
                "nums": [1, 4],
                "win": False,
            },
            {
                "nums": [2, 3],
                "win": False,
            },
        ]
        for t in test_cases:
            self.assertEqual(t["win"], is_winning_board(board, t["nums"]), t["nums"])


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
        n, b = read_input(file)
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
        n, b = read_input(file)
        self.assertListEqual(numbers, n)
        self.assertListEqual(boards, b)


if __name__ == '__main__':
    unittest.main()
