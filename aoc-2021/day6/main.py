from sys import stdin


def read_world_state(f) -> list[int]:
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        return line.split(',')


def world_state_next_day(state: list[int]):
    for i in range(len(state)):
        if state[i] > 0:
            state[i] -= 1
        else:
            state[i] = 6
            state.append(8)


def world_state_next_days(state: list[int], days: int):
    for _ in range(days):
        world_state_next_day(state)


def fish_count_after_days(state: list[int], days: int) -> int:
    world_state_next_days(state, days)
    return len(state)


def main():
    w = read_world_state(stdin)
    days = 80
    n = fish_count_after_days(w, days)
    print(n)


if __name__ == "__main__":
    main()
