# N=1

# def multiply_list_by_number(lst, multiplier):
#     return list(map(lambda x: x * multiplier, lst))

# original_list = [1, 2, 3, 4, 5]
# multiplier = 2

# result_list = multiply_list_by_number(original_list, multiplier)

# print(f"Original List: {original_list}")
# print(f"Result List after multiplying by {multiplier}: {result_list}")

# N=2

# def filter_and_get_length(input_list):
#     filtered_list = list(filter(lambda x: x[0].isupper(), input_list))
#     return len(filtered_list)

# names = ["msxali", "Vashli", "mandarini", "Fortxali", "kivi"]
# result_length = filter_and_get_length(names)
# print("Length after filtering:", result_length)

# N=3
# def sum_positive_and_negative(numbers):
#     positive_sum = sum(filter(lambda x: x > 0, numbers))
#     negative_sum = sum(filter(lambda x: x < 0, numbers))
#     return positive_sum, negative_sum

# number_list = [1, -2, 3, -4, 5, -6]
# positive_sum, negative_sum = sum_positive_and_negative(number_list)

# print("Positive Sum:", positive_sum)
# print("Negative Sum:", negative_sum)

# N=4

# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.balance}")
#         else:
#             print("Invalid deposit amount. Please enter a positive value.")

#     def display_balance(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Current Balance: ${self.balance}")

# def create_account():
#     account_holder = input("Enter your name: ")
#     initial_balance = float(input("Enter initial deposit amount: "))
#     return BankAccount(account_holder, initial_balance)

# def main():
#     try:
#         account = create_account()

#         deposit_amount = float(input("Enter deposit amount: "))
#         account.deposit(deposit_amount)

#         account.display_balance()

#     except ValueError as ve:
#         print(f"Error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()
