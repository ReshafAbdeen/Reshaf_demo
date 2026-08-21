class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance  # Protected attribute

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self._balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self._balance}")
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self) -> float:
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.04):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest((self) -> None:
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest added: ₹{interest}. New Balance: ₹{self._balance}")


# Usage
acc = SavingsAccount("Rahul", 10000.0)
acc.deposit(2000)
acc.apply_interest()
acc.withdraw(3000)