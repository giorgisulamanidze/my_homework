# N=1

# consumer_info = []

# for _ in range(3):
#    name = input("Enter your name: ")
#    surname = input("Enter your surname: ")
#    age = int(input("Enter your age: "))
#    user_info = {"Name": name, "Lastname": surname, "Age": age}
#    consumer_info.append(user_info)

# user_index = int(input("Enter a user index: "))
# selected_user = consumer_info[user_index]

# print(f"Name: {selected_user['Name']} Lastname: {selected_user['Lastname']} Age: {selected_user['Age']}")

# N=2
# users = []

# for _ in range(1):
#  name = input("Enter your name: ")
#  password = input("Enter your password: ")
#  if name and len(password) >= 8:
#      user_info = {"Name": name, "Password": password}
#      users.append(user_info)
#      print("User registered successfully.")
#  else:
#     print("Registration failed.")

# name = input("Enter your name: ")
# password = input("Enter your password: ")
# for user in users:
#  if user['Name'] == name and user['Password'] == password:
#    print("Login successful.")
#    break
# else:
#  print("Login failed. Please check your name and password.")

# N=3

# actors = {
#   'tom hanks': {'full_name': 'Tom Hanks', 'birth_date': 'July 9, 1956', 'awards': ['Academy Award', 'Golden Globe']},
#   'leonardo dicaprio': {'full_name': 'Leonardo DiCaprio', 'birth_date': 'November 11, 1974', 'awards': ['Academy Award', 'BAFTA']}
# }

# search_username = input("Enter actor's first or last name: ").lower()

# for actor in actors.values():
#   if search_username in actor['full_name'].lower():
#       print(f"Actor: {actor['full_name']}")
#       print(f"Birth Date: {actor['birth_date']}")
#       if actor['awards']:
#           print("Awards: " + ", ".join(actor['awards']))
#       else:
#           print("Awards: None")
#       break
# else:
#   print(f"Actor with name '{search_username}' not found.")

