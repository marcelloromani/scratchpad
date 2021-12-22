from sys import stdin


class LineTypeNotSupported(ValueError):
    pass


def parse_line(line: str) -> tuple[int, int, int, int]:
    line = line.strip()
    line = line.replace('->', ',')
    coords = [int(x) for x in line.split(',')]
    return coords[0], coords[1], coords[2], coords[3]


def is_hor(line: tuple[int, int, int, int]) -> bool:
    return line[1] == line[3]


def is_ver(line: tuple[int, int, int, int]) -> bool:
    return line[0] == line[2]


def is_diag45(line: tuple[int, int, int, int]) -> bool:
    x0, y0, x1, y1 = line
    x_delta = abs(x0 - x1)
    y_delta = abs(y0 - y1)
    return x_delta == y_delta


def deepcopy_2d(board: list[list[int]]) -> list[list[int]]:
    return [row[:] for row in board]


def apply_line(board: list[list[int]], line: tuple[int, int, int, int], diag: bool = False) -> list[list[int]]:
    """
    :param board: initial board
    :param line: line to apply to the board
    :param diag: True if 45deg diagonal lines should also be considered
    :return: a new board where the line has been applied
    """
    result = deepcopy_2d(board)
    x0, y0, x1, y1 = line
    if is_hor(line):
        begin, end = (x0, x1) if x0 < x1 else (x1, x0)
        for x in range(begin, end + 1):
            result[y0][x] += 1
    elif is_ver(line):
        begin, end = (y0, y1) if y0 < y1 else (y1, y0)
        for y in range(begin, end + 1):
            result[y][x0] += 1
    elif is_diag45(line):
        if not diag:
            raise LineTypeNotSupported("Diagonal lines not supported")
        if x0 < x1 and y0 < y1:
            for i in range(x1 - x0):
                board[y0 + i][x0 + i] += 1
        elif x0 > x1 and y0 < y1:
            for i in range(x0 - x1):
                board[y0 + i][x1 + 1] += 1
        elif x0 < x1 and y0 > y1:
            for i in range(x1 - x0):
                board[y1 + 1][x0 + 1] += 1
        else:  # x0 > x1 and y0 > y1
            for i in range(x1 - x0):
                board[y1 + i][x0 + i] += 1
    return result


def apply_lines(board: list[list[int]], lines: list[tuple[int, int, int, int]]) -> list[list[int]]:
    # deep copy is performed by apply_line
    result = board
    for line in lines:
        try:
            result = apply_line(result, line)
        except LineTypeNotSupported:
            pass
    return result


def count_lines_overlap(board: list[list[int]]) -> int:
    result = 0
    for line in board:
        for col in line:
            if col >= 2:
                result += 1
    return result


def init_board(row_count: int, col_count: int) -> list[list[int]]:
    rows = [0 for _ in range(col_count)]
    board = [rows for _ in range(row_count)]
    return board


def read_input(f) -> list[tuple[int, int, int, int]]:
    result = []
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        t = parse_line(line)
        result.append(t)
    return result


def required_board_size(lines: list[tuple[int, int, int, int]]) -> tuple[int, int]:
    """
    :return: row_count, col_count
    """
    max_r = 0
    max_c = 0
    for line in lines:
        if line[0] > max_c:
            max_c = line[0]
        if line[2] > max_c:
            max_c = line[2]
        if line[1] > max_r:
            max_r = line[1]
        if line[3] > max_r:
            max_r = line[3]
    return max_r + 1, max_c + 1


def day5_part1(f) -> int:
    lines = read_input(f)
    row_count, col_count = required_board_size(lines)
    board = init_board(row_count, col_count)
    board = apply_lines(board, lines)
    return count_lines_overlap(board)


def main():
    print(day5_part1(stdin))


if __name__ == "__main__":
    main()
