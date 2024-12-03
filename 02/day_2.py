def pos(x):
    return x > 0

def safe_report(report):
    values = [int(v) for v in report]
    differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    v0_pos = pos(differences[0])
    is_safe = all(0 < abs(v) <= 3 and pos(v) == v0_pos for v in differences)
    # print(values, differences, is_safe)
    return is_safe


with open("input.txt", "r") as f:
    raw_lines = f.readlines()

reports = (line.strip().split(' ') for line in raw_lines)

safe_reports = sum(safe_report(report) for report in reports)
print(safe_reports)