# N=1
# user_input = input("Please enter a string: ")

# num_alphabets = num_digits = num_unknown = 0

# for character in user_input:
#   if character.isalpha():
#       num_alphabets += 1
#   elif character.isdigit():
#       num_digits += 1
#   else:
#       num_unknown += 1

# print("Number of alphabets: ", num_alphabets)
# print("Number of digits: ", num_digits)
# print("Number of unknown characters: ", num_unknown)

# N=2

# sentence1 = input("Enter the first sentence: ")
# sentence2 = input("Enter the second sentence: ")

# third_sentence = sentence1[0] + sentence2[-1] + sentence1[1] + sentence2[1]
# print("The third sentence is: ", third_sentence)

# N=3

sentence1 = input("Please enter the first sentence: ")
sentence2 = input("Please enter the second sentence: ")

for character in sentence1:
   if character not in sentence2:
       print("Strings are not balanced!")
       break
else:
   for character in sentence2:
       if character not in sentence1:
           print("Strings are not balanced!")
           break
   else:
       print("Strings are balanced!")