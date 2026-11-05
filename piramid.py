<<<<<<< HEAD
#Duplicate Key
num = [1,3,4,2,6,4,5,3,7,8,8,9,5,6,3,5,2,1,6,9]
n = num

hash_map = dict()
for i in range(0, len(n)):
    hash_map[num[i]] = hash_map.get(num[i],0) + 1

print(hash_map)
=======

num = 5
for i in range(0, num):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")

for i in range(num, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')

    print("\r")
>>>>>>> 11f0370ede66ad54bf8d1ab9d6a4a73a8a7e40c1
