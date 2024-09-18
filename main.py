#Author: Ilton da Costa Neto
#Partner: Jack King

class BankAccount:

    #class attribute
    title = "The Best Bank in the World"

    #constructor
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    #method 1
    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        if amount <= self.minimum_balance:
            print()
        self.current_balance += amount

    #method 2
    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        calculation = self.current_balance - amount
        if calculation < self.minimum_balance:
            print("\nMinimum balance not met, cannot withdraw\n")
        else:
            self.current_balance -= amount
            print(f"Your current balance is now {self.current_balance}")

    #method 3
    def print_customer_information(self):
        print("\n")
        print(BankAccount.title)
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance} \n")

class Savings(BankAccount):
    def __init__(self, account_number, routing_number, customer_name, current_balance, minimum_balance):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member

class Checking(BankAccount):
    def __init__(self, account_number, routing_number, customer_name, current_balance, minimum_balance):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member


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