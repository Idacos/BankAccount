#Author: Ilton da Costa Neto
#Partner: Jack King
from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, routing_number, interest_rate, customer_name, current_balance, minimum_balance):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"Interest added: {interest}, New balance: {self.current_balance}")

    def print_savings_information(self):
        print("\n")
        print(SavingsAccount.title)
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Interest Rate: {self.interest_rate} \n")
