#RasmlaiBank

class RasmaliBank:
    print("\n===Welcome to Rasmlai Bank===")
    def __init__(self, holder_name, account_num, balance):
        self.holder_name = holder_name
        self.account_num = account_num
        self.balance = balance
        
    def check_balance(self):
        print(f"Your name : {self.holder_name}\nYour account number : {self.account_num}\nYour Balance : {self.balance}")


    def deposite(self):
        while True:
            print("\n--- DEPOSIT MENU ---")
            ammount = int(input("You want to add some in your account : "))
            self.balance = self.balance + ammount
            if ammount == 0:
                print("Returning to Main Menu... No money added.")
                break
            elif ammount > 0:
                self.balance = self.balance + ammount
                print(f"₹{ammount} successfully credited to your account.")
                break
            else:
                print("Invalid Amount! Aap minus mein deposit nahi kar sakte. Try Again!")


    def widrawl(self):
        ammount = int(input("How much money you TO widrawl in your account : "))
        if ammount <= 0:
            print("Invalid Ammount!!!")
        elif ammount <= self.balance:
            self.balance = self.balance - ammount
            print(f"{ammount} Succesfully debited.")
        else:
            print(f"\nOnly {self.balance} money in your account")

my_rasmlai = RasmaliBank("Zaynul", '9927165792', 10000)
my_rasmlai.deposite()
my_rasmlai.widrawl()
my_rasmlai.check_balance()