# N1

# import random

# human_point = 0
# computer_point = 0

# while True:
#     human_choice = int(input("""
#     Choose Number:
#     1. Stone
#     2. Scissors
#     3. Paper              
#     """))
    
#     computer_choice = random.randint(1,3)
    
    
#     human_win1 = (human_choice == 1 and computer_choice == 2)
#     human_win2 = (human_choice == 2 and computer_choice == 3)
#     human_win3 = (human_choice == 3 and computer_choice == 1)
#     print(f'Score: {human_point} : {computer_point}')
#     if human_point !=3 and computer_point!=3:
#         if human_choice == computer_choice:
#             continue
#         elif human_win1 or human_win2 or human_win3:
#             human_point += 1
#         else:
#             computer_point += 1
#     elif human_point == 1:
#         print("You Won !!!")
#         break
#     else:
#         print("You Lose !!!")
#         break

# N2

# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     for j in range(1, num +1):
#         print(i * j, end=' ')
#     print()

# N3
# total_balance = 3000

# while True:
#  amount = input("Enter the amount to deduct (or 0 to stop): ")
 
#  if amount == '0':
#     break

#  amount = int(amount)
#  if amount > total_balance:
#     print("Not enough money on the account to continue functioning.")
#     break
 
#  total_balance -= amount

# if amount == '0':
#    print("The remaining balance is: ", total_balance)

# N4
while True:
 user_input = input("User Said Whaaat !? : ")

 if user_input.lower() == "quit":
    break

 print("User Said Whaaat!? \nUser Said", user_input)