# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
