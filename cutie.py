
class BudgetTracker:
   def __init__(self, total_budget):
      self.total_budget = total_budget
      self.expense = []
    # user = int(input("Apna monthly budget daale : "))
    # print(f"Apka mothly budget : {user} ")

   def add_expense(self, item_naam, amount, category):
    naya_kharcha = {
        "item": item_naam,
        "amount": amount,
        "category":category
        }
    self.expense.append(naya_kharcha)
    print(f"{item_naam} ${amount} succesfully addd ho gya hai.")


   def view_suumry(self):
    total_sum = []

    for k in self.expense:
       total_sum = total_sum + k['amount']
       print(f"{k['item']} {k['category']} : Rs{k['amount']}")

    bacha_paisa = self.expense - total_sum
    print(bacha_paisa)


    if total_sum > (self.expense * 0.8):
        print("Waarnig!!! Kharcha 80% paar gya hai....")
    else:
        print("Moj lo bhai abhi bohot paise hai...")

if __name__ == "__main__":
    print("Welcome to budget analyzer")
    budgte = float(input("Apna budget daale : "))
    tarker = BudgetTracker(budgte)

    print("Apne kharche add karen..")
    naam = input("Item naam dalo : ")
    amo = int(input("Amount daalo : "))
    cat = input("Category Daalo : ")
    tarker.add_expense(naam, amo, cat)







    


