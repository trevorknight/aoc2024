with open("input.txt", "r") as f:
    # lines = [(int(left), right.split(' ')) for line in f.read().splitlines() for left, right in line.split(': ')]
    # lines = [(l, *r) for line in f.read().splitlines() for l, r in line.split(': ')]
    lines = []
    for line in f.readlines():
        left, right = line.strip().split(": ")
        lines.append((int(left), [int(v) for v in right.split(" ")]))
    # lines = [(int(l), r.split(" ")) for line in f.readlines() for l, r in line.strip().split(": ")]


valid_total = 0
for line in lines:
    target = line[0]
    values = line[1]
    print('======')
    print('Now aiming for', target)
    possible_running_totals = [values[0]]
    for value in values[1:]:
        # print('New value', value)
        new_possibilities = []
        for running_total in possible_running_totals:
            if running_total + value <= target:
                # print("New possibility", running_total + value)
                new_possibilities.append(running_total + value)
            if running_total * value <= target:
                new_possibilities.append(running_total * value)
                # print("New possibility", running_total * value)
        possible_running_totals = new_possibilities
        # print('Current possible', possible_running_totals)
    if target in possible_running_totals:
        print('Target possible!', target, sorted(possible_running_totals))
        valid_total += target
    else: 
        print('Target not possible.', target, sorted(possible_running_totals))


print('Valid total', valid_total)