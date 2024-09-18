#Author: Ilton da Costa Neto
#Partner: Jack King

from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_number, routing_number, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member
        self.transfer_limit = transfer_limit

    def check_transfer(self, transfer_amount):
        if transfer_amount > self.transfer_limit:
            print("Not allowed to transfer.")
            return False
        else:
            print("Transfer allowed.")
            return True