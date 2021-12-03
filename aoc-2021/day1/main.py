from sys import stdin


def parse_int_array(string_list: list) -> list:
    result = []
    for s in string_list:
        s = s.strip()
        if not s.isnumeric():
            raise ValueError(f"{s} is not numeric")
        result.append(int(s))
    return result


def count_increases(measurements: list) -> int:
    if len(measurements) <= 1:
        return 0
    increase_count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            increase_count += 1
    return increase_count


def _sum_of_triplets(measurements: list) -> list:
    if len(measurements) < 3:
        raise ValueError("Array must contain at least 3 elements")
    result = []
    for i in (range(len(measurements) - 2)):
        result.append(measurements[i] + measurements[i + 1] + measurements[i + 2])
    return result


def count_triplet_increases(measurements: list) -> int:
    if len(measurements) <= 3:
        return 0
    m = _sum_of_triplets(measurements)
    increase_count = count_increases(m)
    return increase_count


def main():
    m = stdin.readlines()

    m = parse_int_array(m)

    c = count_increases(m)
    print(f"Single measurement increases: {c}")

    c = count_triplet_increases(m)
    print(f"Triple measurements increases: {c}")


if __name__ == "__main__":
    main()
