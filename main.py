#Frequency Map/ Dictionary

num = [2,3,4,1,3,5,6,7,8,9,0,9,5,7,6,4,3,4,7,8]
x = 8

fre_map = dict()
for i in range(0, len(num)):
    if num[i] in fre_map:
        fre_map[num[i]] += 1 #Duplicate ko plus karo

    else:
        fre_map[num[i]] = 1

print(fre_map[x])


        
    