import re

with open("input.txt", "r") as f:
    input = f.read()


regex = re.compile("mul\((\d{1,3}),(\d{1,3})\)")

# Part 1, Version 1
# total = 0
# for v in regex.finditer(input):d
#     groups = v.groups()
#     total += int(groups[0])*int(groups[1])

# Part 1, Version 2
# total = sum(int(v.groups()[0]) * int(v.groups()[1]) for v in regex.finditer(input))

# Part 1, Version 3
total = sum(int(a) * int(b) for a, b in (v.groups() for v in regex.finditer(input)))

print(total)


# mul\(\d{1,3},\d{1,3}\)
# mul\((\d{1,3}),(\d{1,3})\)
