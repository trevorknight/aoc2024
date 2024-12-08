from dataclasses import dataclass

FILENAME = "input.txt"


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)


@dataclass(frozen=True)
class CoordWithDirection:
    coord: Coord
    direction: Coord


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




def getBlockadeCandidates(map, start, start_direction):
    location = start
    current_direction = start_direction
    visited_coords: set[Coord] = set()
    visited_coords.add(location)
    while True:
        direction = direction_order[current_direction % len(direction_order)]
        next_location = location + direction
        if offMap(map, next_location):
            break
        if blocked(map, next_location):
            current_direction += 1
            continue
        location = next_location
        visited_coords.add(location)
    return visited_coords


def testBlockadeCandidates(
    map: list[str], start: Coord, start_direction: int, blockade_candidates: list[Coord]
):
    found_blockade_locations = 0
    for candidate in blockade_candidates:
        location = start
        current_direction = start_direction
        direction = direction_order[current_direction % len(direction_order)]
        visited: set[CoordWithDirection] = set()
        visited.add(CoordWithDirection(location, direction))
        while True:
            direction = direction_order[current_direction % len(direction_order)]
            next_location = location + direction
            next_location_with_direction = CoordWithDirection(next_location, direction)
            if next_location_with_direction in visited:
                print('Loop detected!')
                found_blockade_locations += 1
                break
            if offMap(map, next_location):
                print('Went off map.  Not a good blockade location')
                break
            # Block if it's blocked OR if it's the candidate blockade
            if next_location == candidate or blocked(map, next_location):
                current_direction += 1
                continue
            # Otherwise, we're moving there
            visited.add(next_location_with_direction)
            location = next_location
    return found_blockade_locations


if __name__ == "__main__":
    map = readMap()
    start: Coord = findStart(map)
    start_direction = 0
    candidates = getBlockadeCandidates(map, start, start_direction)
    print('Found', len(candidates), 'candidates')
    successful_blockade_locations = testBlockadeCandidates(map, start, start_direction, candidates)
    print("Total successful locations", successful_blockade_locations)

