# THIS IS MY DAR FOUR OF LEARING PYTHON


#fist code
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
   
    print(avg)
    return avg

calc_avg(4, 8, 4)






#second code
def calc_avg(a, b, c):
    sum = a + b + c
    return  sum / 3

avg = calc_avg(4, 8, 6,)
print(avg)






#WAF to print the lenght of list. (list in parameter)

village = ["sindhouli", "meerganj", "saijna", "jouner", "sillapur"]
movies = ["hulk", "thor" "avenger", "avatar", "veer zaraa",]

def print_len(list):
    print(len(list))

print_len(village)
print_len(movies)






#WAF to print the element of a list in a single line (list is the parametr)

village = ["sindhouli", "meerganj", "saijna", "jouner", "sillapur"]
movies = ["hulk", "thor" "avenger", "avatar", "veerb" ]

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(village)        






#WAF to find the factorial of n. (n is the parameter)

def calc_fac(n):
    fact = 1
    for i in range(1, n+1):
          fact *= i
    print(fact)

calc_fac(8)






#WAFto convert USD to INNR.

def converter(usd_val):
    inr_val = usd_val * 94.027
    print(usd_val, "USD", inr_val, "INR")

converter(7)






#Recursion

#first code
def show(n):
    if(n == 0):
        return
    print(n)
    show(n -1)
show(6)



#seond code
def fact(n):
    if(n == 1 or n == 0):
        return 1 
    return fact(n - 1) * n

print(fact(5))
    