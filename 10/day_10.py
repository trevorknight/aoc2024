with open('test.txt', 'r') as f:
  input = [[int(c) for c in line] for line in f.read().splitlines() ]

for y, line in enumerate(input):
  for x, value in enumerate(line):
