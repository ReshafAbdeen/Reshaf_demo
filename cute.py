list =  [1, 4, 6, 4, 7, 9, 8, 5, 9, 0, 3, 5, 6, 3 ]
unique_number = []
duplicate_num = []


for i in list:
    if i not in unique_number:
     unique_number.append(i)
    else:
       duplicate_num.append(i)
       
print(unique_number)
print(duplicate_num)


