import copy


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


def is_hor(line: tuple[int, int, int, int]) -> bool:
    return line[1] == line[3]


def is_ver(line: tuple[int, int, int, int]) -> bool:
    return line[0] == line[2]


def main():
    pass


if __name__ == "__main__":
    main()
