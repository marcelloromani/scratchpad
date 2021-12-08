from sys import stdin


def purge_blanks(data: list[str]):
    for d in data:
        d = d.strip()
        if len(d) == 0:
            continue
        yield d


def most_common_bits(data: list[str]) -> str:
    if len(data) == 0:
        raise ValueError("Empty input")
    if len(data) == 1:
        return data[0]

    # all entries in the list must have the same length
    input_length = len(data[0])

    bit_count = [0 for _ in range(input_length)]
    for d in data:
        bit_count = [bit_count[i] + int(d[i]) for i in range(input_length)]

    result = [0 for _ in range(input_length)]
    for i in range(input_length):
        result[i] = 1 if bit_count[i] > len(data) / 2 else 0

    return "".join([str(x) for x in result])


def main():
    lines = stdin.readlines()

    lines = list(purge_blanks(lines))

    result_str = most_common_bits(lines)
    print(int(result_str, 2))


if __name__ == "__main__":
    main()
