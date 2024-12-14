from dataclasses import dataclass

FILENAME = "test.txt"
STEPS = 100
MAP_WIDTH = 101
MAP_HEIGHT = 103


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other):
        return Coord((self.x + other.x) % MAP_WIDTH, (self.y + other.y) % MAP_HEIGHT)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Robot:
    position: Coord
    velocity: Coord

    def update(self):
        self.position = self.position + self.velocity


def loadRobots() -> list[Robot]:
    # TODO
    return []


def calculateSafetyFactor(robots: list[Robot]) -> int:
    # TODO
    return 0


if __name__ == "__main__":
    robots = loadRobots()
    for _ in range(STEPS):
        for robot in robots:
            robot.update()
    print("Safety factor:", calculateSafetyFactor(robots))
