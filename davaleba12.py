# N=1
# def remove_duplicates(original_dict):
#     unique_values = set() 
#     result_dict = {}

#     for key, value in original_dict.items():
#         if value not in unique_values:
#             result_dict[key] = value
#             unique_values.add(value)

#     return result_dict

# my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

# unique_dict = remove_duplicates(my_dict)

# print(unique_dict) 

# N=2

# def check_empty_dict(my_dict):
#     if len(my_dict) == 0:
#         print("The dictionary is empty (using len())")

#     if not my_dict:
#         print("The dictionary is empty (using not operator)")

#     if bool(my_dict) is False:
#         print("The dictionary is empty (using bool())")

#     if my_dict.__len__() == 0:
#         print("The dictionary is empty (using __len__() method)")

#     if not any(my_dict.items()):
#         print("The dictionary is empty (using any() with items())")

# empty_dict = {}
# non_empty_dict = {"name": "John", "age": 30}

# print("Checking empty dictionary:")
# check_empty_dict(empty_dict)

# print("\nChecking non-empty dictionary:")
# check_empty_dict(non_empty_dict)

# N=3

# def string_to_dict(text):

#   letter_counts = {}
#   for char in text:
#     if not char.isalnum():
#       continue

#     char = char.lower()

#     letter_counts[char] = letter_counts.get(char, 0) + 1

#   return letter_counts

# sample_string = "Giorgi"
# letter_dict = string_to_dict(sample_string)

# print(f"Letter counts for '{sample_string}': {letter_dict}")
