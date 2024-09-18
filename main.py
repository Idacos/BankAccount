#Author: Ilton da Costa Neto
#Partner: Jack King
from bank_account import BankAccount
from checking_account import CheckingAccount
from savings_account import SavingsAccount

new_bank_one = BankAccount("Zach",100, 20)
new_bank_two = BankAccount("Sarah",170, 30)

optionOne = 0
while optionOne != 3:
    print("Which account would you like to access: ")
    print("1. Zach")
    print("2. Sarah")
    print("3. Exit")
    accountNumber = int(input())
    optionTwo = 0
    if accountNumber == 1:
        while optionTwo != 4:
            print("What option would you like to do?")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Print Customer Info")
            print("4. Exit")
            option = input("Enter your choice: ")
            if option == "1":
                new_bank_one.deposit()
            elif option == "2":
                new_bank_one.withdraw()
            elif option == "3":
                new_bank_one.print_customer_information()
            elif option == "4":
                optionTwo = 4
            else:
                print("Invalid option, exiting")
                exit()
    elif accountNumber == 2:
        while optionTwo != 4:
            print("What option would you like to do?")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Print Customer Info")
            print("4. Exit")
            option = input("Enter your choice: ")
            if option == "1":
                new_bank_two.deposit()
            elif option == "2":
                new_bank_two.withdraw()
            elif option == "3":
                new_bank_two.print_customer_information()
            elif option == "4":
                optionTwo = 4
            else:
                print("Invalid option, exiting")
                exit()
        else:
            exit()