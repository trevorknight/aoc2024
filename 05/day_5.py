with open("input.txt", "r") as f:
    raw_data = f.read().splitlines()

rules = {}
updates = []

for line in raw_data:
    if "|" in line:
        a, b = line.split("|")
        a, b = int(a), int(b)
        rules.setdefault(a, set())
        rules[a].add(b)
    if "," in line:
        updates.append([int(p) for p in line.split(",")])

for k, v in rules.items():
  rules[k] = sorted(v)

def isValidUpdate(update, rules):
    seen_pages = []
    for page in update:
        must_be_after = rules.get(page, set())
        for seen_page in seen_pages:
            if seen_page in must_be_after:
                print('Rejecting update', update, 'because', seen_page, 'is before', page)
                return False
        seen_pages.append(page)
    print('Update ok.')
    return True


def getMiddlePage(update):
    assert len(update) % 2 == 1
    return update[len(update) // 2]


total = 0
for update in updates:
    print('============')
    print('Now considering update:', update)
    if isValidUpdate(update, rules):
        total += getMiddlePage(update)

print("Total:", total)
