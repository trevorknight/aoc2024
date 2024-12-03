import sys

with open('input.txt', 'r') as f:
    raw_lines = f.readlines()


a, b = zip(*(line.strip().split() for line in raw_lines))

a, b = sorted(int(v) for v in a), sorted(int(v) for v in b)

if (len(a) != len(b)):
  print('Unequal lists of numbers somehow.')
  sys.exit()

cumulative_difference = 0

for i in range(len(a)):
   cumulative_difference += abs(int(a[i]) - int(b[i]))

print('Cumulative difference: ', cumulative_difference)

similarity_score = 0

#  Version 1
# b_index = 0
# for a_val in a:
#   b_count = 0
#   while b_index < len(b) and b[b_index] < a_val:
#      b_index += 1
#   while b_index < len(b) and b[b_index] == a_val:
#     #  print(a_val, "found")
#      b_count += 1
#      b_index += 1
#   similarity_score += a_val * b_count

# Version 2
from collections import Counter
b_counter = Counter(b)
for a_val in a:
   similarity_score += a_val * b_counter[a_val]

print('Similarity score', similarity_score)
