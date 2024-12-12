NUM_BLINKS = 25

TEST = [int(v) for v in "125 17".split(" ")]
INPUT = [int(v) for v in "2 77706 5847 9258441 0 741 883933 12".split(" ")]

stones = INPUT

for _ in range(NUM_BLINKS):
  new_stones = []
  for i, stone in enumerate(stones):
    if stone == 0:
      new_stones.append(1)
      continue
    str_stone = str(stone)
    l = len(str_stone)
    if len(str_stone) % 2 == 0:
      a = int(str_stone[:l//2])
      b = int(str_stone[l//2:])
      new_stones.append(a)
      new_stones.append(b)
      continue
    new_stones.append(stone * 2024)
  stones = new_stones

print(stones)
print(len(stones))

