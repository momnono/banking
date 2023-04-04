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

    def is_overdraft_allowed(self):
        return self.overdraft_allowed


class Program:
    def __init__(self):
        self.bank = Bank("Your Bank Name")

    def show_main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Open Account")
            print("2. Select Account")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.open_account()
            elif choice == '2':
                self.select_account()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def open_account(self):
        print("\nOpen Account:")
        account_type = input("Enter account type (SavingsAccount or ChequingAccount): ")
        account_holder_name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))

        if account_type == "ChequingAccount":
            overdraft_allowed = input("Is overdraft allowed for this account? (y/n): ")
            if overdraft_allowed.lower() == 'y':
                account = ChequingAccount(account_holder_name, initial_balance, True)
            else:
                account = ChequingAccount(account_holder_name, initial_balance)
        else:
            account = self.bank.open_account(account_type, account_holder_name, initial_balance)

        print(f"Account opened successfully. Your account number is {account.get_account_number()}.")

    def select_account(self):
        print("\nSelect Account:")
        account_number = int(input("Enter the account number: "))
        account = self.bank.search_account(account_number)

        if account:
            self.show_account_menu(account)
        else:
            print("Account not found. Please try again.")

    def show_account_menu(self, account):
        while True:
            print("\nAccount Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                print(f"Current balance: {account.get_current_balance()}")
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
                print("Amount deposited successfully.")
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                try:
                    account.withdraw(amount)
                    print("Amount withdrawn successfully.")
                except ValueError as e:
                    print(str(e))
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == '__main__':
    program = Program()
    program.show_main_menu()
