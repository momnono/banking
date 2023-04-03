"""bankapp and user interface"""
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []

    def open_account(self, account_type, account_holder_name, initial_balance):
        if account_type == "SavingsAccount":
            account = SavingsAccount(account_holder_name, initial_balance)
        elif account_type == "ChequingAccount":
            account = ChequingAccount(account_holder_name, initial_balance)
        else:
            raise ValueError("Invalid account type")

        self.accounts.append(account)
        return account

    def search_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None




class Account:
    account_count = 0

def __init__(self, account_holder_name, initial_balance):
    self.account_number = Account.account_count
    Account.account_count += 1
    self.account_holder_name = account_holder_name
    self.current_balance = initial_balance


    def get_account_number(self):
        return self.account_number

    def get_account_holder_name(self):
        return self.account_holder_name

    def get_current_balance(self):
        return self.current_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if amount <= self.current_balance:
            self.current_balance -= amount
        else:
            raise ValueError("Insufficient balance")


class SavingsAccount(Account):
    minimum_balance = 1000

    def __init__(self, account_holder_name, initial_balance):
        super().__init__(account_holder_name, initial_balance)


    def withdraw(self, amount):
        if self.current_balance - amount >= SavingsAccount.minimum_balance:
            super().withdraw(amount)
        else:
            raise ValueError("Minimum balance not there")


class ChequingAccount(Account):
    def __init__(self, account_holder_name, initial_balance, overdraft_allowed=False):
        super().__init__(account_holder_name, initial_balance)
        self.overdraft_allowed = overdraft_allowed

    def withdraw(self, amount):
        if self.overdraft_allowed or amount <= self.current_balance:
            self.current_balance -= amount
        else:
            raise ValueError("Insufficient balance")

class Program:
    def __init__(self):
        pass

    def show_main_menu(self):
        pass

    def open_account(self):
        pass

    def select_account(self):
        pass

    def show_account_menu(self, account):
        pass
