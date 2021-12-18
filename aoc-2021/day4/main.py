from sys import stdin


def parse_board(board_text: str) -> list[list[int]]:
    b = []
    for line in board_text.split("\n"):
        line = line.strip()
        if len(line) == 0:
            continue
        b.append([int(x) for x in line.split()])
    return b


def parse_numbers_line(line: str) -> list[int]:
    line = line.strip()
    if len(line) == 0:
        return []
    return [int(x) for x in line.split(",")]


def read_input(f) -> (list[int], list[list[list[int]]]):
    WAITING_FOR_NUMBERS: int = 1
    WAITING_FOR_BOARDS: int = 2
    READING_BOARD: int = 3

    state = WAITING_FOR_NUMBERS

    numbers = []
    boards = []
    board_txt = ""

    for line in f.readlines():
        line = line.strip()
        if state == WAITING_FOR_NUMBERS:
            if len(line) == 0:
                continue
            else:
                numbers = parse_numbers_line(line)
                state = WAITING_FOR_BOARDS
        elif state == WAITING_FOR_BOARDS:
            if len(line) == 0:
                continue
            else:
                state = READING_BOARD
                board_txt = line
        elif state == READING_BOARD:
            if len(line) == 0:
                # finished reading a board
                board = parse_board(board_txt)
                boards.append(board)
                board_txt = ""  # signal that the board has been parsed and added to the result
                state = WAITING_FOR_BOARDS
            else:
                # still reading the board
                board_txt += '\n'  # need new line to separate lines
                board_txt += line
        else:
            raise ValueError("Unknown state")

    # if the file doesn't end with a new line, we'll miss the last board
    # so, if board_txt is not empty, it means the last board hasn't been parsed
    if board_txt != "":
        board = parse_board(board_txt)
        boards.append(board)

    return numbers, boards


def num_pos_in_board(board: list[list[int]], n: int) -> (int, int):
    row_count = len(board)
    col_count = len(board[0])
    for i in range(row_count):
        for j in range(col_count):
            if board[i][j] == n:
                return i, j
    return -1, -1


def is_winning_board(board: list[list[int]], numbers: list[int]) -> (bool, list[int]):
    row_count = len(board)
    col_count = len(board[0])
    # these array count how many times each row is found having a matching number
    row_match_count = [0 for _ in range(row_count)]
    col_match_count = [0 for _ in range(col_count)]

    drawn = []

    # look for all numbers in the board
    for n in numbers:
        drawn.append(n)
        row, col = num_pos_in_board(board, n)
        if row != -1 and col != -1:
            row_match_count[row] += 1
            col_match_count[col] += 1
        # After each number we check if the board is winning
        for r in row_match_count:
            if r == col_count:
                return True, drawn
        for c in col_match_count:
            if c == row_count:
                return True, drawn
    return False, drawn


def find_winning_board(boards: list[list[list[int]]], numbers: list[int]) -> (list[list[int]], int):
    """
    :param boards: list of 2d boards to check
    :param numbers: numbers drawn
    :return: the board that won, the number drawn when a board won
    """
    for board in boards:
        is_winning, drawn = is_winning_board(board, numbers)
        if is_winning:
            return board, drawn


def main():
    nums, boards = read_input(stdin)

    print(nums)

    print(boards)


if __name__ == "__main__":
    main()
