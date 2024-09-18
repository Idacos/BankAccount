# Author: Ilton da Costa Neto
# Partner: Jack King
from bank_account import BankAccount
from checking_account import CheckingAccount
from savings_account import SavingsAccount

new_bank_one = BankAccount("Zach", 100, 20)
new_bank_two = BankAccount("Sarah", 170, 30)

new_savings_one = SavingsAccount("001", "121314151", 0.05,
                                 "Ryan", 500, 20)
new_savings_two = SavingsAccount("007", "911171222", 0.1,
                                 "Klara", 250, 50)

new_checking_one = CheckingAccount("203817263845", "293847162",
                                   "Mike", 150, 10,
                                   50)

new_checking_two = CheckingAccount("817204626548", "619304926",
                                   "Alex", 100, 50,
                                   20)

new_checking_one.print_checking_information()

new_checking_one.checking_deposit(10)
new_checking_one.print_checking_information()

new_checking_one.checking_withdraw(60)
new_checking_one.print_checking_information()

new_checking_two.print_checking_information()

new_checking_two.checking_deposit(30)
new_checking_two.print_checking_information()

new_checking_two.checking_withdraw(15)
new_checking_two.print_checking_information()

print("Accessing Ryan's savings account...")
print("Adding amount to current balance")
new_savings_one.deposit()
new_savings_one.print_savings_information()
print("Adding interest...")
new_savings_one.add_interest()

print("Accessing Klara's savings account...")
print("Adding amount to current balance")
new_savings_two.deposit()
new_savings_two.print_savings_information()
print("Adding interest...")
new_savings_two.add_interest()

# optionOne = 0
# while optionOne != 3:
#     print("Which account would you like to access: ")
#     print("1. Zach")
#     print("2. Sarah")
#     print("3. Exit")
#     accountNumber = int(input())
#     optionTwo = 0
#     if accountNumber == 1:
#         while optionTwo != 4:
#             print("What option would you like to do?")
#             print("1. Deposit")
#             print("2. Withdraw")
#             print("3. Print Customer Info")
#             print("4. Exit")
#             option = input("Enter your choice: ")
#             if option == "1":
#                 new_bank_one.deposit()
#             elif option == "2":
#                 new_bank_one.withdraw()
#             elif option == "3":
#                 new_bank_one.print_customer_information()
#             elif option == "4":
#                 optionTwo = 4
#             else:
#                 print("Invalid option, exiting")
#                 exit()
#     elif accountNumber == 2:
#         while optionTwo != 4:
#             print("What option would you like to do?")
#             print("1. Deposit")
#             print("2. Withdraw")
#             print("3. Print Customer Info")
#             print("4. Exit")
#             option = input("Enter your choice: ")
#             if option == "1":
#                 new_bank_two.deposit()
#             elif option == "2":
#                 new_bank_two.withdraw()
#             elif option == "3":
#                 new_bank_two.print_customer_information()
#             elif option == "4":
#                 optionTwo = 4
#             else:
#                 print("Invalid option, exiting")
#                 exit()
#         else:
#             exit()
