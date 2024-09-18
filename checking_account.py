# Author: Ilton da Costa Neto
# Partner: Jack King

from bank_account import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, account_number, routing_number, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member
        self.transfer_limit = transfer_limit

    def check_transfer(self, transfer_amount):
        if transfer_amount > self.transfer_limit:
            print("Transfer Denied: Transfer limit exceeded.")
            return False
        else:
            print("Transfer allowed.")
            return True

    def checking_deposit(self, deposit_amount):
        print(f"Amount to deposit: ${deposit_amount}")
        if self.check_transfer(deposit_amount):
            self.current_balance += deposit_amount
            print(f"Deposited ${deposit_amount} into checking account.")

    def checking_withdraw(self, withdraw_amount):
        print(f"Amount to withdraw: ${withdraw_amount}")
        if self.check_transfer(withdraw_amount):
            self.current_balance -= withdraw_amount
            print(f"Withdrew ${withdraw_amount} from checking account.")

    def print_checking_information(self):
        print("\n")
        print(CheckingAccount.title)
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Transfer Limit: {self.transfer_limit} \n")
