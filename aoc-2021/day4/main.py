from sys import stdin


def purge_blanks(data: list[str]):
    for d in data:
        d = d.strip()
        if len(d) == 0:
            continue
        yield d


def parse_board(board_text: str) -> list[list[int]]:
    b = []
    for line in board_text.split("\n"):
        line = line.strip()
        if len(line) == 0:
            continue
        b.append([int(x) for x in line.split()])
    return b


def read_input(filename: str) -> (list[int], list[list[list[int]]]):
    WAITING_FOR_NUMBERS: int = 1
    WAITING_FOR_BOARDS: int = 2
    READING_BOARD: int = 3

    state = WAITING_FOR_NUMBERS

    numbers = []
    boards = []
    board_txt = ""

    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if state == WAITING_FOR_NUMBERS:
                if len(line) == 0:
                    continue
                else:
                    numbers = [int(x) for x in line.split(",")]
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
                    board_txt = ""          # signal that the board has been parsed and added to the result
                    state = WAITING_FOR_BOARDS
                else:
                    # still reading the board
                    board_txt += '\n'       # need new line to separate lines
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


def is_winning_board(board: list[list[int]], numbers: list[int]) -> bool:
    row_count = len(board)
    col_count = len(board[0])
    # these array count how many times each row is found having a matching number
    row_match_count = [0 for _ in range(row_count)]
    col_match_count = [0 for _ in range(col_count)]
    # look for all numbers in the board
    for n in numbers:
        row, col = num_pos_in_board(board, n)
        if row != -1 and col != -1:
            row_match_count[row] += 1
            col_match_count[col] += 1
    for r in row_match_count:
        if r == col_count:
            return True
    for c in col_match_count:
        if c == row_count:
            return True
    return False


def main():
    lines = stdin.readlines()

    lines = list(purge_blanks(lines))


if __name__ == "__main__":
    main()