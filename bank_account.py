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