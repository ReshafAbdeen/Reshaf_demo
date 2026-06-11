#The Tech Interview Puzzel

print("\033[1m"+"Welcome to The Tech Interview Puzzel"+"\033[0m")

user = int(input("Enter a random number : "))
for i in range(1, user + 1 ):
    if i % 3== 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif  i % 3 == 0 and i % 5 == 0:
        print("FizzBuss")
            
    else:
        print(i)
          
        
