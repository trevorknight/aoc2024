import re

with open("input.txt", "r") as f:
    input = f.read()

# mul\(\d{1,3},\d{1,3}\)
# mul\((\d{1,3}),(\d{1,3})\)
regex = re.compile("mul\((\d{1,3}),(\d{1,3})\)")

# Part 1, Version 1
# total = 0
# for v in regex.finditer(input):d
#     groups = v.groups()
#     total += int(groups[0])*int(groups[1])

# Part 1, Version 2
# total = sum(int(v.groups()[0]) * int(v.groups()[1]) for v in regex.finditer(input))

# Part 1, Version 3
# total = sum(int(a) * int(b) for a, b in (v.groups() for v in regex.finditer(input)))

# Part 1, Version 4
total = sum(int(v.group(1)) * int(v.group(2)) for v in regex.finditer(input))


print('Part 1 total:', total)

# Part 2

mul_matches = [
    (v.span()[0], int(v.group(1)) * int(v.group(2))) for v in regex.finditer(input)
]
do_regex = re.compile("do\(\)")
do_matches = [(v.span()[0], True) for v in do_regex.finditer(input)]
dont_regex = re.compile("don't\(\)")
dont_matches = [(v.span()[0], False) for v in dont_regex.finditer(input)]

all_matches = (v[1] for v in sorted(mul_matches + do_matches + dont_matches, key=lambda x: x[0]))

do_add = True
total = 0
for value in all_matches:
    if type(value) is bool:
        do_add = value
    elif do_add:
      total += value

print('Do and don\'t total:', total)
        
