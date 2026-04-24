# MY DAY FOUR OF LEARNING PYTHON BY YOUTUBE

class student:
    name = "zainul0"

s1 = student()
print(s1.name)


class student:
    

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding some student data in datalist")

      

s1 = student("zaynul", 55)
print(s1.name, s1.marks)



s2 = student("arwaz", 66)
print(s2.name, s2.marks)


class student:
  def __init__(self, name, marks):
      self.name = name
      self.marks = marks

  def get_avg(self):
      sum = 0
      for val in self.marks:
          sum += val
      print("hii =", self.name, "your num avg =", sum/3)

s1 = student("zaynul", [55, 88, 64])
s1.get_avg()

#Abstraction
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "left was your account")
        print("total balance", self.get_balance())


    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was your account")
        print("total balance", self.get_balance())


    def get_balance(self):
        return self.balance
    
acc1 = Account(100000, 1800002353535)
print(acc1.balance)
print(acc1.account_no)