from sys import stdin


def count_increases(measurements: list) -> int:
    if len(measurements) <= 1:
        return 0
    prev_meas = measurements[0]
    increase_count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > prev_meas:
            increase_count += 1
        prev_meas = measurements[i]
    return increase_count


m = stdin.readlines()
print(len(m))
c = count_increases(m)
print(c)
