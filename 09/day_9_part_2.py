from dataclasses import dataclass

with open("input.txt", "r") as f:
    input = f.read()
input = [int(c) for c in input]

@dataclass
class FreeLocation:
  offset: int
  size: int

@dataclass
class FileLocation:
   offset: int
   size: int
   file_id: int

disk = []
file_locations = []
free_locations = []
disk_offset = 0
for i, size in enumerate(input):
  is_file: bool = i % 2 == 0
  file_id = i // 2 if is_file else -1
  for _ in range(size):
     disk.append(file_id)
  if is_file:
     file_locations.append(FileLocation(disk_offset, size, file_id))
  if not is_file and size > 0:
     free_locations.append(FreeLocation(disk_offset, size))
  disk_offset += size


# print(disk)
# print(file_locations)
# print(free_locations)


for file in reversed(file_locations):
   for free in free_locations:
      if file.offset < free.offset:
          break
      if free.size >= file.size:
        print(f'Found {free.offset} of size {free.size} for file {file.file_id}, size {file.size}')
        for i in range(file.size):
          disk[file.offset + i] = -1
          disk[free.offset + i] = file.file_id
        free.size -= file.size
        free.offset += file.size
        if free.size == 0:
           free_locations.remove(free)
           print('Removed empty free space')
        break

# print(disk)
checksum = 0
for i, v in enumerate(disk):
  if v > 0:
     checksum += i * v
print(checksum)



