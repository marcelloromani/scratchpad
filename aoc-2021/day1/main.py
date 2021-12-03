from sys import stdin


def count_increases(measurements: list) -> int:
    if len(measurements) <= 1:
        return 0
    increase_count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            increase_count += 1
    return increase_count


def parse_int_array(string_list: list) -> list:
    result = []
    for s in string_list:
        s = s.strip()
        if not s.isnumeric():
            raise ValueError(f"{s} is not numeric")
        result.append(int(s))
    return result


def main():
    m = stdin.readlines()
    print(len(m))
    m = parse_int_array(m)
    c = count_increases(m)
    print(c)


if __name__ == "__main__":
    main()
