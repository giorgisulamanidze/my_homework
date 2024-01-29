# N=1

# def triple_input():
#     user_input = input("Enter a string: ")
#     triple_string = user_input * 3
#     print(f"Tripled: {triple_string}")

# triple_input()


# N=2

# def calculate_moon_weight(earth_weight):
#     moon_weight = earth_weight / 6
#     return moon_weight

# user_weight_earth = float(input("Enter your weight on Earth: "))
# user_weight_moon = calculate_moon_weight(user_weight_earth)
# print(f"Your weight on the Moon would be: {user_weight_moon} kilograms.")

# N=3
# def calculator():
#     expression = input("Enter a mathematical expression: ")

#     parts = expression.split()
    
#     if len(parts) != 3:
#         print("Please enter a valid mathematical expression.")
#         return

#     num1, operator, num2 = parts

#     if not num1.isnumeric() or not num2.isnumeric():
#         print("Please enter valid numbers.")
#         return

#     num1 = float(num1)
#     num2 = float(num2)

#     result = None
#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             print("Cannot divide by zero. Please enter a non-zero divisor.")
#             return
#         else:
#             result = num1 / num2
#     elif operator == '^':
#         result = num1 ** num2
#     else:
#         print("Error. Please enter a valid operator (+, -, *, /, ^).")
#         return

#     print(f"The result of {expression} is: {result}")
#     return result

# calculator()

   