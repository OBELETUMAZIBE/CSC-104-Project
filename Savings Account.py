# Savings Account with withdrawal limit
class SavingsAccount(Account):
    def __init__(self, name):
        super().__init__(name, "savings")
        self.withdrawal_limit = 5000

    def withdraw(self, amount):
        if amount <= self.balance and amount <= self.withdrawal_limit:
            self.balance -= amount
            return f"{amount} withdrawn from savings account."
        return "Withdrawal exceeds limit or insufficient funds."
