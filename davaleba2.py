# N = 1

user_answer = input("Which is the water supply system (aqueduct) built by the empire still functioning today?\nPossible answers:\n1. Sumerians\n2. Seljuks\n3. Rome\n4. Mongols\n")

correct_answer = "Rome".lower()

if user_answer == correct_answer or user_answer == "3":
    print("Correct")
else:
    print("False ! Correct Answer is Rome")

# N = 2

# category = input("Choose the category: \n1. Laptops\n2. PC\n3. Phones\n")
# # choose_budget = input("Please choose max budget : \n1.2000 Gel\n2.3500 Gel\n3.5000 Gel\n")
# if (category == "Laptops") or (category == ("1")):
#     choose_budget = int(input("Please choose max budget : "))
#     if (choose_budget < 2000) and (choose_budget >= 300 ):
#         print("Asus Chromebook Flip CX5")
#     elif (choose_budget >= 2000) and (choose_budget <= 3500):
#         print("Acer Nitro Gaming Laptop	")
#     elif (choose_budget >= 3500):
#         print("ASUS ROG Strix G16 ")
#     else:
#         print("There isn't any laptop for this price ")
# else:
#     print("Good Luck")

# if category == "PC" or category == "2":
#     choose_budget = int(input("Please choose max budget : "))
#     if choose_budget >= 500 and choose_budget <=1500:
#         print("ASUS ROG Hyperion GR701")
#     elif choose_budget > 1500 and choose_budget <=3000:
#         print("CLX SET TGMSETRXM2500BM Gaming Desktop Computer - AMD Ryzen 5 5600G Hexa-core")
#     elif choose_budget > 3000:
#         print("Skytech Nebula Gaming PC Desktop (R5 5600X, RTX 4070)")
#     else:
#         print("There isn't any PC for this price ")

# if category == "Phones" or category == "3":
#     choose_budget = int(input("Please choose max budget : "))
#     if choose_budget >= 300 and choose_budget <=1000:
#         print("Samsung Galaxy A14 5G")
#     elif choose_budget > 1000 and choose_budget <=2000:
#         print("Google Pixel 7A")
#     elif choose_budget > 2000:
#         print("iPhone: Apple iPhone 15")
#     else:
#         print("There isn't any Phones for this price ")


# # N3

# print("""
# კეთილი იყოს შენი მობრძანება ტექსტზე დაფუძვნებულ თამასში
# შენ ხარ დაკარგულ კუნძულზე და შენი მისია არის, იპოვო განძი
# იყავი ფრთხილად, რადგან ბევრი საფრთხეა!""")

# print("რას გააკეთებ ? ")
# print("1. წახვალ მარცხნივ")
# print("2. წახვალ მარჯვნინ")
# print("3. წახვალ პირდაპირ")

# choice = input("აირჩიე (1, 2, or 3): ")

# if choice == "1":
#     print("\n შენ აირჩიე მარცხნივ წასვლა და იპოვე ხიდი.")

#     print("რას გააკეთებ შემდეგ ?")
#     print("1. გადახვალ ხიდზე")
#     print("2. უკან დაბრუნდები")

#     choice = input("აირჩიე (1 or 2): ")

#     if choice == "1":
#         print("\n შენ წარმატები გადალახე ხიდი.")
#         print("გილოცავ! შენ იპოვე განძი!")
#     else:
#         print("\n შენ უკან დაბრუნდი. თავგადასავალი გრძელდება...")

# elif choice == "2":
#     print("\n შენ აირჩიე მარჯვნივ წასვლა. შენ შეხვდი კაციჭამიებს!")
#     print("რას გააკეთბ შემდეგ?")
#     print("1. იჩხუბებ")
#     print("2. გაიქცევი")

#     choice = input("აირჩიე (1 or 2): ")

#     if choice == "1":
#         print("\n შენ დაამარცხე ისინი")
#         print("გილოცავ! შენ მოიპოვე განძი!")
#     else:
#         print("\nშენ გაიქეცი და ვერ დაგეწიენ, ამიტომ თავგადასაველი გრძელდება...")

# elif choice == "3":
#     print("\n შენ აირჩიე პირდაპირ წასვლა. შენ იპოვე გამოქვაბული.")

#     print("რას გააკეთებ შემდეგ?")
#     print("1. შეხვალ გამოქვაბულში")
#     print("2. იპოვი სხვა გზას")

#     choice = input("აირჩიე (1 or 2): ")

#     if choice == "1":
#         print("\n შენ შეხვედი გამოქვაბულში და იპოვე სკივრი.")
#         print("გილოცავ ! შენ იპოვე განძი!")
#     else:
#         print("\n შენ აირჩიე სხვა გზა და სამწუხაროდ შენი თავგადასავალი დასრულდა.")
