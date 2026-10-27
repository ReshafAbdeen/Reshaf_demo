n = [5, 4,2,3,6,8,4,9,0,5,3,5,6,3,8,0,10]
m = [10,111,1,9,5,67,2]
hash_list = [0]*11
for num in n:
    hash_list[num] += 1

for num in m:
    if num<1 or num>10:
        print(0)

    else:
        print(hash_list[num])
