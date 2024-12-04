from dataclasses import dataclass

with open('input.txt', 'r') as f:
    grid = f.read().splitlines() 

count = 0
width = len(grid[0])
height = len(grid)

@dataclass
class Coord:
   x: int
   y: int

def checkDirection(start: Coord, modifier, direction: str):
  coords = start
  for char in ['X', 'M', 'A', 'S']:
     if not 0 <= coords.x < width or not 0 <= coords.y < height:
        return
     if grid[coords.y][coords.x] != char:
        return
     coords = modifier(coords)
  print('Found', direction, 'at', start.x, start.y)
  global count
  count += 1

for y in range(height):
    for x in range(width):
        start = Coord(x, y)
        checkDirection(start, lambda before: Coord(before.x + 1, before.y), 'W->E')
        checkDirection(start, lambda before: Coord(before.x - 1, before.y), 'E->W')
        checkDirection(start, lambda before: Coord(before.x, before.y + 1), 'N->S')
        checkDirection(start, lambda before: Coord(before.x, before.y - 1), 'S->N')
        checkDirection(start, lambda before: Coord(before.x - 1, before.y + 1), 'NE->SW')
        checkDirection(start, lambda before: Coord(before.x + 1, before.y - 1), 'SW->NE')
        checkDirection(start, lambda before: Coord(before.x + 1, before.y + 1), 'NW->SE')
        checkDirection(start, lambda before: Coord(before.x - 1, before.y - 1), 'SE->NW')

print("Count", count)