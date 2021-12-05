import json
from sys import stdin


class Move:
    DIRECTIONS = [
        "forward",
        "down",
        "up",
    ]

    def __init__(self, direction: str, distance: int):
        self._validate_direction(direction)
        self._dir = direction
        self._d = distance

    @property
    def direction(self):
        return self._dir

    @property
    def distance(self):
        return self._d

    @classmethod
    def _validate_direction(cls, d: str):
        if d not in cls.DIRECTIONS:
            raise ValueError(f"Invalid move: {d}")

    @staticmethod
    def _validate_distance(d: str):
        if not d.isnumeric():
            raise ValueError(f"{d} does not look like a number")

    @classmethod
    def parse_move(cls, s: str):
        (move, dist) = s.split()
        cls._validate_distance(dist)
        return Move(move, int(dist))

    def keys(self):
        return ["direction", "distance"]

    def __getitem__(self, key):
        if key == "direction":
            return self._dir
        if key == "distance":
            return self._d
        raise KeyError(f"Invalid key: {key}")

    def __str__(self):
        return json.dumps(dict(self))

    def next_pos(self, hor: int, depth: int) -> (int, int):
        if self.direction == "forward":
            return hor + self.distance, depth
        if self.direction == "down":
            return hor, depth + self.distance
        if self.direction == "up":
            return hor, depth - self.distance


def parse_moves(moves_str: list[str]) -> list[Move]:
    result = []
    for s in moves_str:
        s = s.strip()
        if not s:
            continue
        m = Move.parse_move(s)
        result.append(m)
    return result


def multiply_hor_depth(moves: list[Move]) -> int:
    hor = 0
    depth = 0
    for m in moves:
        hor, depth = m.next_pos(hor, depth)
    return hor * depth


def main():
    lines = stdin.readlines()

    moves = parse_moves(lines)
    for m in moves:
        print(m)
    print(multiply_hor_depth(moves))


if __name__ == "__main__":
    main()
