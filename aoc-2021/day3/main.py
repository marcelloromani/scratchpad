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


def reverse_bits(s: str) -> str:
    return "".join([('1' if x == '0' else '0') for x in s])


def gamma_epsilon_rate(data: list[str]) -> (int, int):
    gamma_str = most_common_bits(data)
    epsilon_str = reverse_bits(gamma_str)
    return int(gamma_str, 2), int(epsilon_str, 2)


def oxygen_co2_rate(dat: list[str]) -> (int, int):
    return 0, 0


def main():
    lines = stdin.readlines()

    lines = list(purge_blanks(lines))

    gamma, epsilon = gamma_epsilon_rate(lines)
    print(gamma * epsilon)


if __name__ == "__main__":
    main()
