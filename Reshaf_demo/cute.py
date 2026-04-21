# # # # # count = 1
# # # # # while count < 5 :
# # # # #     print("Yasmin cutie")
# # # # #     count += 1


# # # # n = int(input("enter a number for table = "))
# # # # i = 1
# # # # while i <= 10 :
# # # #     print(n * i)
# # # #     i += 1


# # nums = ( 2, 12, 4, 3, 92, 99, 45, 5, 8, 20, 4, )
# # idx = 0
# # while idx < len(nums) :
# #     print(nums(idx))
# #     idx += 1

nums = ( 2, 12, 4, 3, 92, 99, 45, 5, 8, 20, 4, 36, )
x = 99
i = 0 
found = False


while i < len(nums):
    if nums[i] == x :
     print("found", i)
     found = True
     break
    i += 1
if not found:
   print("not found")    
    