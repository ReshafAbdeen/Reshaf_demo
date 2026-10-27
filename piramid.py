#Duplicate Key
num = [1,3,4,2,6,4,5,3,7,8,8,9,5,6,3,5,2,1,6,9]
n = num

hash_map = dict()
for i in range(0, len(n)):
    hash_map[num[i]] = hash_map.get(num[i],0) + 1

print(hash_map)
