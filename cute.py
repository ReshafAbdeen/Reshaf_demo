# Bank Account Management System

from datetime import datetime

class BankAccount:
    """Basic bank account eith deposit, widrawl aru transaction"""
    bank_name = "Python Bankof Zaynul"
    total_account = 0

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance
        self.transaction = []
        BankAccount.total_account += 1
        self.account_no = 1000 + BankAccount.total_account

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount positive hona chahiye!!!!")
            return

        self._balance += amount
        self._log(f"Deposit : ${amount}")
        print(f"${amount} deposit ho gya  hai. Naya balance {self._balance}")

    def withdrawl(self, amount):
        if amount > self._balance:
           print("Insuficent Balance")
           return
        self._balance -= amount
        self._log(f"Withdrawl {amount}")
        print(f"${amount} nikal gya. Naya balance {self._balance}")

    def _log(self, msg):
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.transaction.append(f"[{time}] {msg}")


    def show_statement(self):
        print(f"Statment for {self.name} (A/C : {self.account_no})")
        for t in self.transaction:
            print(" ", t)

        print(f"Current Balance : {self._balance}")

    def __str__(self):
        return f"{self.name} | A/C : {self.account_no} | Balance : {self._balance}"

class SavingAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=4.0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest @{self.interest_rate}% add gya hai.")

if __name__ == "__main__":
    acc1 = SavingAccount("Zaynul Abdeen", balance=5000, interest_rate=5)
    acc1.deposit(2000)
    acc1.withdrawl(1000)
    acc1.add_interest()
    acc1.show_statement()

    print(acc1)
    print("Total account created:", BankAccount.total_account)
 


