with open("input.txt", "r") as f:
    input = f.read()


2333133121414131402

output_visualization = []

file_id = 0
file_block = 0
currently_moving_i = len(input) - 1 if len(input) % 2 == 1 else len(input) - 2
number_left_to_move = int(input[currently_moving_i])
checksum = 0

for input_i, value in enumerate(input):
  if input_i >= currently_moving_i:
    # Special case, we only want to add blocks we have left
    file_id = currently_moving_i // 2
    for _ in range(number_left_to_move):
      print("Adding file_id", file_id, "* file_block", file_block)
      checksum += file_id * file_block
      output_visualization.append(file_id)
      file_block += 1
    break
  if input_i % 2 == 0:
    # This a file, let's add to the checksum
    file_id = input_i // 2
    for _ in range(int(input[input_i])):
      print("Adding file_id", file_id, "* file_block", file_block)
      checksum += file_id * file_block
      output_visualization.append(file_id)
      file_block += 1
  else:
    # This is a blank, let's pull from the back.
    for _ in range(int(input[input_i])):
      moving_file_id = currently_moving_i // 2
      print("Adding file_id", moving_file_id, "* file_block", file_block)
      checksum += moving_file_id * file_block
      output_visualization.append(moving_file_id)
      file_block += 1
      number_left_to_move -= 1
      if number_left_to_move <= 0:
        print('Moving the move location')
        currently_moving_i -= 2
        number_left_to_move = int(input[currently_moving_i])




print(output_visualization)

checksum2 = 0

for i, v in enumerate(output_visualization):
  checksum2 += i * v

print(checksum)
print(checksum2)

