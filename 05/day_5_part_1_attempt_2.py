with open("input.txt", "r") as f:
    raw_data = f.read().splitlines()

# Map from page number to pages which must come before
rules = {}
updates = []

for line in raw_data:
    if "|" in line:
        before, after = line.split("|")
        before, after = int(before), int(after)
        rules.setdefault(after, set()).add(before)
    if "," in line:
        updates.append([int(p) for p in line.split(",")])


def isValidUpdate(update, rules):
    unacceptable_pages = set()
    for page in update:
        if page in unacceptable_pages:
            print(
                "Rejecting update",
                update,
                "because",
                page,
                "should have already been printed",
            )
            return False
        unacceptable_pages.update(rules.get(page, set()))
    print("Update ok.")
    return True


def getMiddlePage(update):
    assert len(update) % 2 == 1
    return update[len(update) // 2]


total = 0
for update in updates:
    print("============")
    print("Now considering update:", update)
    if isValidUpdate(update, rules):
        total += getMiddlePage(update)

print("Total:", total)
