class InsufficientFundsError(Exception):

    pass


class BankAccount:
    bank_name = "Apex Digital Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> float:
        """Deposits money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.__balance += amount
        print(f"-$ {amount:.2f} deposited successfully.")
        return self.__balance

    def withdraw(self, amount: float) -> float:
        """Withdraws money, raising a custom error if funds are low."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.__balance:
            raise InsufficientFundsError(
                f"Attempted to withdraw ${amount:.2f}, but only ${self.__balance:.2f} is available."
            )

        self.__balance -= amount
        print(f"-$ {amount:.2f} withdrawn successfully.")
        return self.__balance

    def __str__(self) -> str:
        return f"Account[{self.account_holder}] at {self.bank_name} | Balance: ${self.__balance:.2f}"


if __name__ == "__main__":
    print(f"--- Welcome to {BankAccount.bank_name} ---")

    user_account = BankAccount("Alex Mercer", 500.00)
    print(user_account)

    user_account.deposit(250.50)
    print(f"New Balance: ${user_account.balance:.2f}")

    try:
        print("\nAttempting to withdraw $1,000...")
        user_account.withdraw(1000.00)
    except InsufficientFundsError as e:
        print(f"Transaction Declined: {e}")


    print(f"\nFinal State: {user_account}")