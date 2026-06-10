
print("\033[1m" + "Welcome to Number Jumper" + "\033[0m")

pass
user = int(input("Enter a randome number : "))
for i in range(1 ,user+1):
    if( i % 5 == 0):
       print("Jump")

    else:
        print(i)