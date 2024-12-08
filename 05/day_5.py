with open("test.txt", "r") as f:
    raw_data = f.read().splitlines()

rules = {}
updates = []

for line in raw_data:
    if "|" in line:
        a, b = line.split("|")
        a, b = int(a), int(b)
        rules.setdefault(a, set()).add(b)
    if "," in line:
        updates.append([int(p) for p in line.split(",")])


def isValidUpdate(update, rules):
    seen_pages = []
    for page in update:
        must_be_after = rules.get(page, set())
        for seen_page in seen_pages:
            if seen_page in must_be_after:
                print(
                    "Rejecting update", update, "because", seen_page, "is before", page
                )
                return False
        seen_pages.append(page)
    print("Update ok.")
    return True


def repair(update, rules):
    print("REPAIR BEFORE", update)
    repaired = []
    for page in update:
        these_must_be_after_current_page = rules.get(page, set())
        insertion_point = len(repaired)
        for repaired_i, repaired_page in enumerate(repaired):
            if repaired_page in these_must_be_after_current_page:
                print(
                    repaired_page,
                    "must come after",
                    page,
                    "i.e.",
                    page,
                    "must be inserted before",
                    repaired_page,
                )
                insertion_point = min(insertion_point, repaired_i)
        repaired.insert(insertion_point, page)
    print("AFTER", repaired)
    return repaired


def getMiddlePage(update):
    assert len(update) % 2 == 1
    return update[len(update) // 2]


total_for_correct = 0
total_for_repaired = 0

for update in updates:
    print("============")
    print("Now considering update:", update)
    if isValidUpdate(update, rules):
        total_for_correct += getMiddlePage(update)
    else:
        total_for_repaired += getMiddlePage(repair(update, rules))


print("total_for_correct:", total_for_correct)
print("total_for_repaired:", total_for_repaired)
