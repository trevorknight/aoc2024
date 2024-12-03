import sys

with open('input.txt', 'r') as f:
    raw_lines = f.readlines()


a, b = zip(*[line.strip().split() for line in raw_lines])

a, b = sorted(map(int, a)), sorted(map(int, b))

if (len(a) != len(b)):
  print('Unequal lists of numbers somehow.')
  sys.exit()

cumulative_difference = 0

for i in range(len(a)):
   cumulative_difference += abs(int(a[i]) - int(b[i]))

print('Cumulative difference: ', cumulative_difference)

similarity_score = 0
b_index = 0

for a_val in a:
  b_count = 0
  while b_index < len(b) and b[b_index] < a_val:
     b_index += 1
  while b_index < len(b) and b[b_index] == a_val:
    #  print(a_val, "found")
     b_count += 1
     b_index += 1
  similarity_score += a_val * b_count

print('Similarity score', similarity_score)
