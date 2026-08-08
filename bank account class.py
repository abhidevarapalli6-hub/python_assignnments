class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print(f"Current Balance: ₹{self.balance:.2f}")


# Example
account = BankAccount("Abhinash", 1000)

account.display_balance()
account.deposit(500)
account.withdraw(300)
account.display_balance()
