with open("input.txt", "r") as f:
    input = f.read()
input = [int(c) for c in input]


file_block = 0
currently_moving_i = len(input) - 1 if len(input) % 2 == 1 else len(input) - 2
number_left_to_move = int(input[currently_moving_i])

arranged_blocks = []
for i, v in enumerate(input):
  if i > currently_moving_i:
    break
  if i % 2 == 0:
    # This a file, let's add to the checksum
    print("====FILE====")
    file_id = i // 2
    print(f"{i=} {file_id=} {currently_moving_i=}")
    if i == currently_moving_i:
      print("APPENDING REMAINDER")
      # Only append what remains
      for _ in range(number_left_to_move):
        arranged_blocks.append(file_id)
      break
    for _ in range(input[i]):
      print("Appending", file_id)
      arranged_blocks.append(file_id)
  else:
    # This is a blank, let's pull from the back.
    print("====BLANK====")
    for _ in range(input[i]):
      moving_file_id = currently_moving_i // 2
      print(f"{i=} {currently_moving_i=} {moving_file_id=}")  
      arranged_blocks.append(moving_file_id)
      print("Appending", moving_file_id)
      number_left_to_move -= 1
      if number_left_to_move <= 0:
        currently_moving_i -= 2
        if (currently_moving_i < i):
          break
        number_left_to_move = int(input[currently_moving_i])
        print(f"UPDATE! {currently_moving_i=} {number_left_to_move=}")


checksum = 0
for i, v in enumerate(arranged_blocks):
  checksum += i*v

print(checksum)