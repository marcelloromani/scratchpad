from sys import stdin


def count_increases(measurements: list) -> int:
    if len(measurements) <= 1:
        return 0
    increase_count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            increase_count += 1
    return increase_count


def main():
    m = stdin.readlines()
    print(len(m))
    c = count_increases(m)
    print(c)


if __name__ == "__main__":
    main()
