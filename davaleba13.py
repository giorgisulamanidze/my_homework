#     N=1

# def write_to_file_until_enough():

#     with open("user_input.txt", "w") as file: 
#         while True:
#             user_input = input("Enter information (type 'enough' to stop): ")
#             if user_input.lower() == "enough":
#                 break 
#             file.write(user_input + "\n")  

#         print("Information saved to user_input.txt")

# write_to_file_until_enough()


#      N=2
# import os

# def create_file_and_list_files():
#    folder_location = input("Enter the folder location: ")
#    file_name = input("Enter the name of the file to create: ")

#    if not os.path.exists(folder_location):
#        print("Error: Folder location does not exist.")
#        return

#    file_path = os.path.join(folder_location, file_name)

#    try:
#        with open(file_path, "w") as file:
#            file.write("")  
#        print(f"File '{file_name}' created successfully in '{folder_location}'.")
#    except Exception as e:
#        print(f"Error creating file: {e}")
#        return

#    files = os.listdir(folder_location)
#    print("Files in the folder:")
#    for file in files:
#        print(file)

# create_file_and_list_files()
