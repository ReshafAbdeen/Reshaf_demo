class Person:
    def __init__(self, n, a):
        self._name = n
        self._age = a

    def display(self):
        print(self._name, self._age, end=' ')

class Student(Person):
    def __init__(self, n, a, r, m1, m2, m3):
        super().__init__(n, a)
        self.rollno = r
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3
    def display(self):
        super().display()
        print(self.rollno, self.mark1, self.mark2, self.mark3)

list = []
s = Student("Zayunl", 21, 53, 89, 90, 94)
list.append(s)
s = Student("akjfh", 22, 57, 90, 98, 94)
list.append(s)
s = Student("Varish", 21, 68, 89, 91, 45)
list.append(s)
s = Student("Kamrul", 23, 64, 89, 95, 80)
list.append(s)
for item in list:
    item.display()



    

    