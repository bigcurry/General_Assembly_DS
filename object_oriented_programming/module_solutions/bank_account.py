class BankAccount:
    def __init__(self, owner_name, balance, fees_owed):
        self.owner_name = owner_name
        self.balance = balance
        self.fees_owed = fees_owed

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        else:
            self.balance -= amount
        if self.balance < 0:
            self.fees_owed += 20

    def pay_fees(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        elif amount > self.fees_owed:
            raise ValueError(
                f"Fee payment cannot exceed `fees_owed` amount of {self.fees_owed}"
            )
        else:
            self.fees_owed -= amount
