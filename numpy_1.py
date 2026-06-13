import numpy as np
arr = np.array([ 9, 10, 11, 12, 13, 14])
print(arr)
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
 
new_row = np.array([1, 4, -5])

result = matrix + new_row
print(result)


rand_decimal = np.random.rand(5)
print(rand_decimal)

rand_matrix = np.random.randint(10 , 50 , size = (6,4))
print(rand_matrix)


game = np.array(["Valorant", "PUBG", "GTA V", "Python Game", "Minecraft"])
lucky_game = np.random.choice(game)

print(f"Aaj laptop kiya chalega dekhte hai Lucky Game : {lucky_game}")



#numpy practice

a = np.array([1,3,6,4])
b = np.array([5,3,6,2])

result_loop = []

for i in range(len(a)):
    result_loop.append(a[i]* b[i])

result_numpy = a * b
print("Vectorized ka result :", result_numpy)