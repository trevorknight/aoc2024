from dataclasses import dataclass
import re
from collections import Counter

FILENAME = "input.txt"
STEPS = 100
MAP_WIDTH = 101
MAP_HEIGHT = 103


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    @staticmethod
    def fromString(str_coord: str):
        values = str_coord.strip().split(",")
        return Coord(int(values[0]), int(values[1]))

    def __add__(self, other):
        return Coord((self.x + other.x) % MAP_WIDTH, (self.y + other.y) % MAP_HEIGHT)

    def __mul__(self, scalar):
        return Coord(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"


@dataclass
class Robot:
    position: Coord
    velocity: Coord

    def update(self, steps=1):
        self.position = self.position + self.velocity * steps

    def __str__(self):
        return f"{self.position=} {self.velocity=}"


def loadRobots() -> list[Robot]:
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    position_re = re.compile("p=\d+,\d+")
    velocity_re = re.compile("v=-?\d+,-?\d+")
    robots = []
    for line in lines:
        pos = Coord.fromString(position_re.search(line).group()[2:])
        vel = Coord.fromString(velocity_re.search(line).group()[2:])
        robots.append(Robot(pos, vel))
    return robots


def loadRobots2() -> list[Robot]:
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    robots = []
    for line in lines:
        v_offset = line.find(" v=")
        position_string = line[2:v_offset]
        velocity_string = line[v_offset + 3 :]
        pos = Coord.fromString(position_string)
        vel = Coord.fromString(velocity_string)
        robots.append(Robot(pos, vel))
    return robots


def countQuadrants(robots: list[Robot]) -> tuple[int, int, int, int]:
    middle_col = MAP_WIDTH // 2
    print(f"{middle_col=}")
    middle_row = MAP_HEIGHT // 2
    print(f"{middle_row=}")

    quad_1 = 0
    quad_2 = 0
    quad_3 = 0
    quad_4 = 0
    for robot in robots:
        if robot.position.x < middle_col and robot.position.y < middle_row:
            print(f"{robot.position} in quad 1")
            quad_1 += 1
        elif robot.position.x > middle_col and robot.position.y < middle_row:
            print(f"{robot.position} in quad 2")
            quad_2 += 1
        elif robot.position.x < middle_col and robot.position.y > middle_row:
            print(f"{robot.position} in quad 3")
            quad_3 += 1
        elif robot.position.x > middle_col and robot.position.y > middle_row:
            print(f"{robot.position} in quad 4")
            quad_4 += 1
        else:
            print(f"{robot.position} on the line")

    return (quad_1, quad_2, quad_3, quad_4)


def printRobots(robots, step_num):
    locations = Counter((robot.position for robot in robots))
    map = [[" "] * MAP_WIDTH for _ in range(MAP_HEIGHT)]
    for location, count in locations.items():
        if count > 9:
            map[location.y][location.x] = "*"
        else:
            map[location.y][location.x] = str(count)
    with open(f"output_{step_num:08}.txt", "w") as f:
        for line in map:
            line.append("\n")
            f.write("".join(line))


def duplicates(robots):
    locations = Counter((robot.position for robot in robots))
    return any((v != 1 for v in locations.values()))


def isInteresting(robots):
    if duplicates(robots):
        return False
    return True
    # quad1, quad2, quad3, quad4 = countQuadrants(robots)
    # if abs(quad1 - quad2) / quad1 > 0.9:
    #     return True


if __name__ == "__main__":
    robots = loadRobots2()
    step = 0
    while True:
        step += 1
        for robot in robots:
            robot.update()
        if isInteresting(robots):
            printRobots(robots, step)
        if step > 10000:
            break