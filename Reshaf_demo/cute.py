# MY DAY SIX OF LEARNING PYTHON


########Private(like) attributes & method
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("120304920394209", "119099")
print(acc1.acc_no)
print(acc1.reset_pass())

#second code
class Person:

    __name ="Zaynul"

    def __hello(self):
        print("Hello world")
    
    def welcome(self):
        self.__hello()
p1 = Person()
print(p1.welcome())


#########Inheritance
#single iinharitance

class car:
    colour = "Black"

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class Tyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Tyotacar("Fortuner")
car2 = Tyotacar("BMW")

print(car1.colour)
        


#Multi-Level iinharitance

class car:
    colour = "Black"

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class Tyotacar(car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(Tyotacar):
    def __init__(self, type):
        self.type  = type

car1 = Fortuner("Diesel")
print(car1.name)




#Multiple iinharitance
class A:
    val1 = "welcome to class A"

class B:
    val2 = "welcome to class B"

class C(A, B):
    val3 = "welcome to class C"

c1 = C()
print(c1.val3)
print(c1.val2)
print(c1.val1)


#super method

class car:
    colour = "Black"
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class Tyotacar(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.brand = name
       
        super().start()


car1 = Tyotacar("Fortunaer", "electric")
print(car1.type)


#Property Method
class Student:

    def __init__(self, phy, math, che):
        self.phy = phy
        self.math = math
        self.che = che

    @property
    def percentage(self):
            return str((self.phy + self.math + self.che ) / 3) + "%"
        
stu1 = Student(77, 53, 99)
print(stu1.percentage)

stu1.math = 99
print(stu1.percentage)



#Dunder Function
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def shownumber(self):
        print(self.real,"i +",self.imag,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return complex(newReal, newImag)
    
num1 = complex(2, 4)
num1.shownumber()

num2 = complex(3, 8)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()