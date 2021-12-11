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


def bit_count_in_position(data: list[str], bit_position: int) -> (int, int):
    """Returns the number of 0 and 1 in the specified position"""
    bit_count = [0, 0]  # number of '0's, number of '1's
    str_index = bit_pos_to_str_index(data, bit_position)
    for d in data:
        if d[str_index] == '0':
            bit_count[0] += 1
        else:
            bit_count[1] += 1
    return bit_count[0], bit_count[1]


class BitSelectionPolicy:
    MOST_COMMON: int = 0
    LEAST_COMMON: int = 1


def bit_pos_to_str_index(data: list[str], bit_position: int) -> int:
    """
    Convert bit position (right-based) to position in the strinc (left-based)
    :param data: list of strings representing binary numbers
    :param bit_position: position to convert. Example: 0 => last char of the string
    """
    if len(data) == 0:
        raise ValueError("No data")
    data_width = len(data[0])
    return data_width - bit_position - 1


def filter_data(data: list[str], bit_position: int, bit_selection_policy: int) -> list[str]:
    result = []
    char_position = bit_pos_to_str_index(data, bit_position)
    zero_count, one_count = bit_count_in_position(data, bit_position)
    for d in data:
        if bit_selection_policy == BitSelectionPolicy.MOST_COMMON:
            if zero_count > one_count and d[char_position] == '0':
                result.append(d)
            elif one_count >= zero_count and d[char_position] == '1':
                result.append(d)
        elif bit_selection_policy == BitSelectionPolicy.LEAST_COMMON:
            if zero_count > one_count and d[char_position] == '1':
                result.append(d)
            elif one_count >= zero_count and d[char_position] == '0':
                result.append(d)
    return result


def oxygen_co2_rate(data: list[str]) -> (int, int):
    d = data
    pos = 0
    while len(d) > 1:
        d = filter_data(d, pos, BitSelectionPolicy.MOST_COMMON)
        pos += 1
    ox_rate = int(d[0], 2)

    d = data
    pos = 0
    while len(d) > 1:
        d = filter_data(d, pos, BitSelectionPolicy.LEAST_COMMON)
        pos += 1
    co2_rate = int(d[0], 2)

    return ox_rate, co2_rate


def main():
    lines = stdin.readlines()

    lines = list(purge_blanks(lines))

    gamma, epsilon = gamma_epsilon_rate(lines)
    print(gamma * epsilon)


if __name__ == "__main__":
    main()
