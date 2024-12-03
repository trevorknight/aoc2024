def pos(x):
    return x > 0

def is_safe(values):
    differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    v0_pos = pos(differences[0])
    return all(0 < abs(v) <= 3 and pos(v) == v0_pos for v in differences)

def create_dropouts(values):
    yield values
    for i in range(0, len(values)):
        yield values[:i] + values[i+1:]

def safe_report(report):
    values = [int(v) for v in report]
    return any(is_safe(subset) for subset in create_dropouts(values))

with open("input.txt", "r") as f:
    raw_lines = f.readlines()

reports = (line.strip().split(' ') for line in raw_lines)
safe_reports = sum(safe_report(report) for report in reports)
print(safe_reports)