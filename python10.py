import random
import time

# N=1
def generate_random_list(n):
  return [random.randint(1, 100) for _ in range(n)]

# N=2
def merge_sort(data):
  if len(data) <= 1:
    return data
  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])
  return merge(left, right)


def merge(left, right):
  i, j = 0, 0
  merged = []
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  merged.extend(left[i:])
  merged.extend(right[j:])
  return merged

# N=3
def linear_search(data, target):

  for i, element in enumerate(data):
    if element == target:
      return i
  return -1


def binary_search(data, target):

  low, high = 0, len(data) - 1
  while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
      return mid
    elif data[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

# N=4
def calculate_time(func, *args):
 
  start_time = time.time()
  func(*args)
  end_time = time.time()
  return end_time - start_time

list_sizes = [10, 100, 1000, 10000]
targets = [50, 75, 99]

for list_size in list_sizes:
  print(f"\nList size: {list_size}")
  data = generate_random_list(list_size)
  sorted_data = merge_sort(data)

  for target in targets:
    print(f"\tLinear search for {target}:")
    time_taken = calculate_time(linear_search, sorted_data, target)
    print(f"\t\tTime taken: {time_taken:.6f} seconds")

  for target in targets:
    print(f"\tBinary search for {target}:")
    time_taken = calculate_time(binary_search, sorted_data, target)
    print(f"\t\tTime taken: {time_taken:.6f} seconds")

