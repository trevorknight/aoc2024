from collections import defaultdict


from dataclasses import dataclass

with open("input.txt", "r") as f:
    input = f.read().splitlines()

original_map = [[c for c in line] for line in input]
map_width = len(original_map[0])
map_height = len(original_map)


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)


all_nodes_map = defaultdict(list)
for y, line in enumerate(original_map):
    for x, c in enumerate(line):
        if c != ".":
            all_nodes_map[c].append(Coord(x, y))


def printMap(a_map):
    for line in a_map:
        print("".join(line))


def isInsideMap(coord: Coord):
    return 0 <= coord.x < map_width and 0 <= coord.y < map_height


def findAntinodes(node_1: Coord, node_2: Coord):
    print(f"Finding antinodes for {node_1}, {node_2}")
    left_x = node_1.x - (node_2.x - node_1.x)
    left_y = node_1.y - (node_2.y - node_1.y)
    left = Coord(left_x, left_y)
    right_x = node_2.x + (node_2.x - node_1.x)
    right_y = node_2.y + (node_2.y - node_1.y)
    right = Coord(right_x, right_y)
    return [node for node in [left, right] if isInsideMap(node)]


def findAntinodesPart2(node_1: Coord, node_2: Coord):
    results = set([node_1, node_2])
    offset = Coord(node_2.x - node_1.x, node_2.y - node_1.y)    
    left = node_1
    while isInsideMap(left := left - offset):
        results.add(left)
    right = node_2
    while isInsideMap(right := right + offset):
        results.add(right)
    return results



antinodes = set()

for character, nodes in all_nodes_map.items():
    for i, node_1 in enumerate(nodes):
        for node_2 in nodes[i + 1 :]:
            antinodes.update(findAntinodesPart2(node_1, node_2))

print("original map")
printMap(original_map)

updated_map = original_map.copy()

for antinode in antinodes:
    updated_map[antinode.y][antinode.x] = "#"

print(len(antinodes))
print("updated map")
printMap(updated_map)
