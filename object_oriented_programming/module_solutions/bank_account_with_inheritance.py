from datetime import datetime


class BankAccount:
    def __init__(self, owner_name, balance, fees_owed, overdraft_fee):
        self.owner_name = owner_name
        self.balance = balance
        self.fees_owed = fees_owed
        self.overdraft_fee = overdraft_fee

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
            self.fees_owed += self.overdraft_fee

    def pay_fees(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        elif amount > self.fees_owed:
            raise ValueError(
                f"Fee payment cannot exceed `fees_owed` amount of {self.fees_owed}"
            )
        else:
            self.fees_owed -= amount


class CheckingAccount(BankAccount):
    def __init__(self, owner_name, balance, fees_owed):
        super().__init__(owner_name, balance, fees_owed, overdraft_fee=30)


class SavingsAccount(BankAccount):
    def __init__(self, owner_name, balance, fees_owed):
        super().__init__(owner_name, balance, fees_owed, overdraft_fee=10)
        self._last_withdrawal_month = datetime.today().month
        self._withdrawals_in_last_withdrawal_month = 0

    def withdraw(self, amount):
        if self._last_withdrawal_month == datetime.today().month:
            self._withdrawals_in_last_withdrawal_month += 1
            if self._withdrawals_in_last_withdrawal_month >= 6:
                raise NotPermittedError(
                    "Customer has used all allowed transactions for the month"
                )
        else:
            self._last_withdrawal_month = datetime.today().month
            self._withdrawals_in_last_withdrawal_month = 1

        super().withdraw(amount)


class NotPermittedError(Exception):
    pass
