import re
from dataclasses import dataclass

A_COST = 3
B_COST = 1
FILENAME = "input.txt"


@dataclass
class Coeffs:
    x: int
    y: int

    def __add__(self, other):
        return Coeffs(self.x + other.x, self.y + other.y)


class Machine:
    a: Coeffs
    b: Coeffs
    prize: Coeffs

    def __str__(self):
        return f"Machine Button A: X+{self.a.x}, Y+{self.a.y} Button B: X+{self.b.x}, Y+{self.b.y} Prize: X={self.prize.x}, Y={self.prize.y}"


def parseLine(line, re_x, re_y) -> Coeffs:
    x = int(re_x.search(line).group()[2:])
    y = int(re_y.search(line).group()[2:])
    return Coeffs(x, y)


def getMachines() -> list[Machine]:
    with open("input.txt", "r") as f:
        input = f.read().splitlines()
    button_x_re = re.compile("X\+\d+")
    button_y_re = re.compile("Y\+\d+")
    prize_x_re = re.compile("X=\d+")
    prize_y_re = re.compile("Y=\d+")
    machines = []
    for line in input:
        if "Button A:" in line:
            machine = Machine()
            machine.a = parseLine(line, button_x_re, button_y_re)
            continue
        if "Button B:" in line:
            machine.b = parseLine(line, button_x_re, button_y_re)
            continue
        if "Prize:" in line:
            machine.prize = parseLine(line, prize_x_re, prize_y_re)
            machines.append(machine)
            machine = None
    return machines


def floatCloseEnough(a: float, b: float, epsilon: float = 0.0001) -> bool:
    return abs(a - b) < epsilon


def areButtonsScaledEquivalent(machine: Machine) -> bool:
    x_ratio = machine.a.x / machine.b.x
    y_ratio = machine.a.y / machine.b.y
    return floatCloseEnough(x_ratio, y_ratio)


def tryValues(A: int, B: int, machine: Machine) -> bool:
    return (
        A * machine.a.x + B * machine.b.x == machine.prize.x
        and A * machine.a.y + B * machine.b.y == machine.prize.y
    )


def getMachineCost(m) -> int:
    if areButtonsScaledEquivalent(m):
        print("ERROR scaled equivalent!")
        print(m)
        breakpoint()

    # COST = 3A + 1B
    # m.prize.x == A * m.a.x + B * m.b.x
    # m.prize.x - B * m.b.x == A * m.a.x
    # (m.prize.x - B * m.b.x) / m.a.x == A

    # m.prize.y == A * m.a.y + B * m.b.y
    # m.prize.y == ((m.prize.x - B * m.b.x) / m.a.x) * m.a.y + B * m.b.y
    # m.prize.y == ((m.prize.x - B * m.b.x) * m.a.y) / m.a.x + B * m.b.y
    # m.prize.y == (m.prize.x * m.a.y - B * m.b.x * m.a.y) / m.a.x + B * m.b.y
    # m.prize.y == m.prize.x * m.a.y / m.a.x - B * m.b.x * m.a.y / m.a.x + B * m.b.y
    # m.prize.y == m.prize.x * m.a.y / m.a.x + B * m.b.y - B * m.b.x * m.a.y / m.a.x
    # m.prize.y == m.prize.x * m.a.y / m.a.x + B * (m.b.y -  m.b.x * m.a.y / m.a.x)
    # m.prize.y / (m.b.y -  m.b.x * m.a.y / m.a.x) == (m.prize.x * m.a.y / m.a.x)/(m.b.y -  m.b.x * m.a.y / m.a.x) + B
    # m.prize.y / (m.b.y -  m.b.x * m.a.y / m.a.x) - (m.prize.x * m.a.y / m.a.x)/(m.b.y -  m.b.x * m.a.y / m.a.x) ==  B
    # B = m.prize.y / (m.b.y -  m.b.x * m.a.y / m.a.x) - (m.prize.x * m.a.y / m.a.x)/(m.b.y -  m.b.x * m.a.y / m.a.x)
    B = (m.prize.y - m.prize.x * m.a.y / m.a.x) / (m.b.y - m.b.x * m.a.y / m.a.x)
    A = (m.prize.x - B * m.b.x) / m.a.x
    print(machine, A, B, round(A), round(B))
    A = round(A)
    B = round(B)
    if tryValues(A, B, m):
        print(f"Machine", m, "successful with {A=}, {B=}")
        return A_COST * A + B_COST * B
    return 0


def getMachineCostPart2(m) -> int:
    new_machine = Machine()
    new_machine.a = m.a
    new_machine.b = m.b
    new_machine.prize = Coeffs(m.prize.x + 10000000000000, m.prize.y + 10000000000000)
    return getMachineCost(new_machine)


if __name__ == "__main__":
    machines = getMachines()
    total_cost = 0
    for machine in machines:
        total_cost += getMachineCostPart2(machine)
    print("Total cost", total_cost)
