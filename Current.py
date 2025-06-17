# Current Account with no limit
class CurrentAccount(Account):
    def __init__(self, name):
        super().__init__(name, "current")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn from current account."
        return "Insufficient funds."
