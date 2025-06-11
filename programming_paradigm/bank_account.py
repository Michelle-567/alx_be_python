class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

#class BankAccount: Defines a blueprint for bank accounts.
#__init__: A constructor method. It creates the account with a starting balance.
#self: Refers to the current object (instance) of the class.
#account_balance: A private attribute for storing money in the account.
#deposit, withdraw, display_balance: These are instance methods that interact with the account.