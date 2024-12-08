from enum import Enum
from dataclasses import dataclass

FILENAME = "input.txt"


@dataclass(frozen=True)
class Coord:
    x: int
    y: int


NORTH = Coord(0, -1)
EAST = Coord(1, 0)
SOUTH = Coord(0, 1)
WEST = Coord(-1, 0)

direction_order: list[Coord] = [NORTH, EAST, SOUTH, WEST]


def readMap():
    with open(FILENAME, "r") as f:
        return f.read().splitlines()


def findStart(map: list[str]) -> Coord:
    for y, row in enumerate(map):
        if (x := row.find("^")) >= 0:
            return Coord(x, y)


def blocked(map, location):
    return map[location.y][location.x] == "#"


def offMap(map, location):
    height = len(map)
    width = len(map[0])
    return (
        location.x < 0 or location.y < 0 or location.x >= width or location.y >= height
    )


def add(location, direction):
    return Coord(location.x + direction.x, location.y + direction.y)


def navigate(map: list[str], start: Coord, current_direction: int) -> int:
    location = start
    visited: set[Coord] = set()
    visited.add(location)
    while True:
        direction = direction_order[current_direction % len(direction_order)]
        next_location = add(location, direction)
        # print("Considering location (", next_location.x, next_location.y, ")")
        if offMap(map, next_location):
            break
        if blocked(map, next_location):
            current_direction += 1
            continue
        location = next_location
        visited.add(location)
    # print(visited)
    return len(visited)


if __name__ == "__main__":
    map = readMap()
    start: Coord = findStart(map)
    current_direction = 0
    print(navigate(map, start, current_direction))
