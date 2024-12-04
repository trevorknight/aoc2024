with open("input.txt", "r") as f:
    grid = f.read().splitlines()

width = len(grid[0])
height = len(grid)

count = 0

MS_SUM = ord("M") + ord("S")

for y in range(1, height - 1):
    for x in range(1, width - 1):
        if (
            grid[y][x] == "A"
            and ord(grid[y - 1][x - 1]) + ord(grid[y + 1][x + 1]) == MS_SUM
            and ord(grid[y - 1][x + 1]) + ord(grid[y + 1][x - 1]) == MS_SUM
        ):
            print("Found X-MAS centered at", x, y)
            count += 1

print("Count", count)
