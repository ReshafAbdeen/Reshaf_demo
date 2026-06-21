def infinite_sequence(start=0):
    num = start
    while True:
        yield num
        num += 1

gen = infinite_sequence()

print(next(gen))  
print(next(gen))  
print(next(gen))  

for val in infinite_sequence(10):
    print(val)
    if val >= 13:
        break  