#   N=1
# import random

# random_list = [random.randint(1, 100) for _ in range(10)]
# print("random list: ", random_list)
# random_list.sort()
# print("sorted list: ", random_list)

#   N=2

# import random

# random_list = [random.randint(1, 100) for _ in range(10)]
# print("random list: ", random_list)

# sorted_list = sorted(random_list, reverse=True)
# print("sorted list: ", sorted_list)

#   N=3
# import random
# import time

# def bubble_sort(list):
#    """Sorts a list using the bubble sort algorithm."""
#    n = len(list)
#    for i in range(n - 1):
#        for j in range(n - i - 1):
#            if list[j] > list[j + 1]:
#                list[j], list[j + 1] = list[j + 1], list[j]

# def selection_sort(list):
#    """Sorts a list using the selection sort algorithm."""
#    n = len(list)
#    for i in range(n):
#        min_index = i
#        for j in range(i + 1, n):
#            if list[j] < list[min_index]:
#                min_index = j
#        list[i], list[min_index] = list[min_index], list[i]

# def main():
#    """Generates lists of varying sizes, sorts them using bubble and selection sort, and compares the times."""
#    for list_size in [1000, 2000, 3000]:
#        list_random = [random.randint(1, 10000) for _ in range(list_size)]

#        start_time = time.time()
#        bubble_sort(list_random.copy()) 
#        bubble_sort_time = time.time() - start_time

#        start_time = time.time()
#        selection_sort(list_random.copy()) 
#        selection_sort_time = time.time() - start_time

#        print(f"List size: {list_size}")
#        print(f"Bubble sort time: {bubble_sort_time:.4f} seconds")
#        print(f"Selection sort time: {selection_sort_time:.4f} seconds")
#        print("----------------------------------")

# if __name__ == "__main__":
#    main()
