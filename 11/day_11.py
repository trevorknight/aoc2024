from typing import Dict


NUM_BLINKS = 75

TEST = [int(v) for v in "125 17".split(" ")]
INPUT = [int(v) for v in "2 77706 5847 9258441 0 741 883933 12".split(" ")]

stones = INPUT

cache: Dict[int, Dict[int, int]] = {}
# Gen #      0  1     2     3        4
# Stones     0  1  2024 20 24  2 0 2 4
# Cache  0: [1, 1,    1,    2,       4]


def evolveStone(stone_value):
    if stone_value == 0:
        return [1]
    str_stone = str(stone_value)
    length = len(str_stone)
    if length % 2 == 0:
        a = int(str_stone[: length // 2])
        b = int(str_stone[length // 2 :])
        return [a, b]
    return [stone_value * 2024]


def getNumStonesAfterGens(start_value, num_gens):
    if num_gens == 0:
        return 1
    if start_value in cache and num_gens in cache[start_value]:
        # print(f"Found {start_value=} {num_gens=} in cache: cache[start_value][num_gens]")
        return cache[start_value][num_gens]
    new_stones = evolveStone(start_value)
    num_descendants = sum([getNumStonesAfterGens(v, num_gens - 1) for v in new_stones])
    # print(f"New entry {start_value=} {num_gens=} in cache: {num_descendants=}")
    cache.setdefault(start_value, {})[num_gens] = num_descendants
    return num_descendants


total = sum([getNumStonesAfterGens(value, NUM_BLINKS) for value in INPUT])


# print(cache)
print(total)
