from dataclasses import dataclass
from enum import Enum

FILENAME = "input.txt"


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)  # type: ignore

    def __str__(self):
        return f"({self.x}, {self.y})"


def readMap():
    with open(FILENAME, "r") as f:
        return f.read().splitlines()


def valueOf(coord: Coord, map):
    return map[coord.y][coord.x]


def setValue(coord: Coord, map, value):
    map[coord.y][coord.x] = value


def isInsideMap(coord: Coord, map: list[list[int]]):
    height = len(map)
    width = len(map[0])
    return 0 <= coord.x < width and 0 <= coord.y < height


class Comp(Enum):
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8


def getOrthogonalMatchingCoordinates(coord: Coord, map) -> list[Coord]:
    directions = [
        Coord(0, -1),
        Coord(1, 0),
        Coord(0, 1),
        Coord(-1, 0),
    ]
    return [
        n
        for direction in directions
        if isInsideMap(n := coord + direction, map)
        and valueOf(n, map) == valueOf(coord, map)
    ]


def findMatchingEightDirections(coord: Coord, map) -> set[Comp]:
    directions = [
        (Comp.N, Coord(0, -1)),
        (Comp.NE, Coord(1, -1)),
        (Comp.E, Coord(1, 0)),
        (Comp.SE, Coord(1, 1)),
        (Comp.S, Coord(0, 1)),
        (Comp.SW, Coord(-1, 1)),
        (Comp.W, Coord(-1, 0)),
        (Comp.NW, Coord(-1, -1)),
    ]
    return set(
        (
            direction[0]
            for direction in directions
            if isInsideMap(n := coord + direction[1], map)
            and valueOf(n, map) == valueOf(coord, map)
        )
    )


def countConvexCorners(ortho: set[Comp]):
    pass


# 00000
# 01110
# 00000
# 00000

NS = {Comp.N, Comp.S}
EW = {Comp.E, Comp.W}


def countCorners(all_matching_compass: set[Comp]) -> int:
    all = all_matching_compass
    print(all)
    ortho = all.intersection({Comp.N, Comp.E, Comp.S, Comp.W})
    print(ortho)
    len_ortho = len(ortho)
    # breakpoint()
    count = 0
    # External corners
    if len_ortho == 0:
        print("4 ext corners")
        count += 4
        return count
    if len_ortho == 1:
        print("Only one ortho neighbor")
        count += 2
        return count
    if len_ortho == 2 and ortho != NS and ortho != EW:
        print("1 external corner")
        count += 1
    # Internal (or concave) corners
    if {Comp.N, Comp.E} <= all and Comp.NE not in all:
        print("NE internal")
        count += 1
    if {Comp.E, Comp.S} <= all and Comp.SE not in all:
        print("SE internal")
        count += 1
    if {Comp.S, Comp.W} <= all and Comp.SW not in all:
        print("SW internal")
        count += 1
    if {Comp.W, Comp.N} <= all and Comp.NW not in all:
        print("NW internal")
        count += 1
    return count


def process(start_coord: Coord, map, processed):
    area = 0
    total_corners = 0
    to_process = set()
    to_process.add(start_coord)
    while to_process:
        coord = to_process.pop()
        print("=======================")
        print(f"Now processing {coord}")
        area += 1
        setValue(coord, processed, True)
        coord_corners = countCorners(findMatchingEightDirections(coord, map))
        print(f"Found {coord_corners} corners for {coord}")
        total_corners += coord_corners
        ortho_coords = getOrthogonalMatchingCoordinates(coord, map)
        for c in ortho_coords:
            if not valueOf(c, processed):
                to_process.add(c)
    print(f"For {valueOf(start_coord, map)}, {total_corners=}, {area=}")
    return total_corners * area


def processMap(map):
    map_height = len(map)
    map_width = len(map[0])
    processed = [[False] * map_width for _ in range(map_height)]
    price = 0
    for y in range(map_height):
        for x in range(map_width):
            if not processed[y][x]:
                price += process(Coord(x, y), map, processed)
    return price


if __name__ == "__main__":
    map = readMap()
    print(processMap(map))
