import copy
from sys import stdin


def parse_line(line: str) -> tuple[int, int, int, int]:
    line = line.strip()
    line = line.replace('->', ',')
    coords = [int(x) for x in line.split(',')]
    return coords[0], coords[1], coords[2], coords[3]


def is_hor(line: tuple[int, int, int, int]) -> bool:
    return line[1] == line[3]


def is_ver(line: tuple[int, int, int, int]) -> bool:
    return line[0] == line[2]


def apply_line(board: list[list[int]], line: tuple[int, int, int, int]) -> list[list[int]]:
    result = copy.deepcopy(board)
    x0, y0, x1, y1 = line
    if is_hor(line):
        for x in range(x0, x1 + 1):
            result[y0][x] += 1
    elif is_ver(line):
        for y in range(y0, y1 + 1):
            result[y][x0] += 1
    else:
        raise ValueError("Diagonal lines not supported")
    return result


def apply_lines(board: list[list[int]], lines: list[tuple[int, int, int, int]]) -> list[list[int]]:
    # deep copy is performed by apply_line
    result = board
    for line in lines:
        result = apply_line(result, line)
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


def main():
    board = init_board(10, 10)
    lines = read_input(stdin)
    board = apply_lines(board, lines)
    print(count_lines_overlap(board))


if __name__ == "__main__":
    main()
