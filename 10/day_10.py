from dataclasses import dataclass
from typing import Self

FILENAME = "test.txt"


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        return Coord(self.x + other.x, self.y + other.y) # type: ignore

    def __str__(self):
        return f"({self.x}, {self.y})"


def getMap() -> list[list[int]]:
    with open(FILENAME, "r") as f:
        return [[int(c) for c in line] for line in f.read().splitlines()]


def printMap(map: list[list[int]]):
    print("========")
    for line in map:
        for value in line:
            print(f"{value:02}", end=" ")
        print("")
    print("========")


def valueOf(coord: Coord, map: list[list[int]]) -> int:
    return map[coord.y][coord.x]


def setValue(coord: Coord, map: list[list[int]], value: int):
    map[coord.y][coord.x] = value


def isInsideMap(coord: Coord, map: list[list[int]]):
    height = len(map)
    width = len(map[0])
    return 0 <= coord.x < width and 0 <= coord.y < height


def getAllNeighbors(coord: Coord, map: list[list[int]]) -> list[Coord]:
    directions = [Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1)]
    return [
        n
        for direction in directions
        if isInsideMap(n := coord + direction, map)
        and valueOf(n, map) == valueOf(coord, map) + 1
    ]


def peaksReachableFrom(coord: Coord, map: list[list[int]]) -> set[Coord]:
    if valueOf(coord, map) == 9:
        return set([coord])
    peaks: set[Coord] = set()
    for n in getAllNeighbors(coord, map):
        # print("Considering", n)
        peaks.update(peaksReachableFrom(n, map))
    return peaks


def calculateTotalScore(map: list[list[int]]):
    total_score = 0
    # print(peaksReachableFrom(Coord(0,4), map))
    for y, line in enumerate(map):
        for x, value in enumerate(line):
            if value == 0:
                peaks = peaksReachableFrom(Coord(x, y), map)
                total_score += len(peaks)
    return total_score


def createBlankMap(map: list[list[int]]) -> list[list[int]]:
    height = len(map)
    width = len(map[0])
    return [[-1] * width for _ in range(height)]


def trailsFrom(
    coord: Coord, map: list[list[int]], trail_count_map: list[list[int]]
) -> int:
    if (v := valueOf(coord, trail_count_map)) != -1:
        return v
    else:
        if valueOf(coord, map) == 9:
            setValue(coord, trail_count_map, 1)
            # printMap(trail_count_map)
            return 1
        # The value is still -1, we need to get neighbor values
        trails_from_coord = sum(
            [trailsFrom(n, map, trail_count_map) for n in getAllNeighbors(coord, map)]
        )
        setValue(coord, trail_count_map, trails_from_coord)
        # printMap(trail_count_map)
        return trails_from_coord


def calculateTotalRating(map: list[list[int]])-> int:
    trail_count_map = createBlankMap(map)
    trailsFrom(Coord(0,0), map, trail_count_map)

    total_rating = 0
    for y, line in enumerate(map):
        for x, value in enumerate(line):
            if value == 0:
                total_rating += trailsFrom(Coord(x, y), map, trail_count_map)
    return total_rating


if __name__ == "__main__":
    map = getMap()
    print("total score:", calculateTotalScore(map))
    print("total rating", calculateTotalRating(map))
