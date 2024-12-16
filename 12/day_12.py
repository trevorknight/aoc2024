from dataclasses import dataclass

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


def getAllNeighbors(coord: Coord, map) -> list[Coord]:
    directions = [Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1)]
    return [
        n
        for direction in directions
        if isInsideMap(n := coord + direction, map)
        and valueOf(n, map) == valueOf(coord, map)
    ]


def process(start_coord: Coord, map, processed):
    print(f"Starting with {start_coord}")
    perimeter = 0
    area = 0
    to_process = set()
    to_process.add(start_coord)
    while to_process:
        coord = to_process.pop()
        print(f"Processing {coord}")
        area += 1
        setValue(coord, processed, True)
        neighbors = getAllNeighbors(coord, map)
        print(f"Found neighbors {neighbors}")
        perimeter += 4 - len(neighbors)
        for n in neighbors:
            if not valueOf(n, processed):
                to_process.add(n)
    print(f"For {valueOf(start_coord, map)}, {perimeter=}, {area=}")
    return perimeter * area


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
