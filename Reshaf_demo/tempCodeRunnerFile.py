# import time
# import random

# question = [ { "question" : "What is my cuteis favourite food ?",
#             "options" : ["A. biryani", "B. korma", "C. stoo", "D. paiye" ],
#             "answer": "A",
#             "money" : 1000},
#             {"question" : "How many rakaat in fazr namaz ?",
#             "options" : ["A. 10", "B. 8", "C. 4", "D. 6" ],
#             "answer": "C",
#             "money" : 5000}]

# def play_kbc():
#     total_money = 0
#     print("Welcome to Kon Bnega Cror Pati")
#     time.sleep(1)

#     for  i, q in enumerate(question):
#         print(f"The firs questin {i+1} on your screen is here")
#         print(q["question"])
#         for opt in q["options"]:
#             print(opt)

#             user_put = input("Enter your answer (A, B, C, D):").upper()

#         if user_put == q["answer"]:
#             total_money = q["money"]
#             print(f"congratulation you win and you won {total_money}")
#             time.sleep(1)
#         else:
#           print(f"Sorry! You loose the game. You go home with the {total_money} money.")
#           return

#     print(f"Kamal kar diya bhai {total_money} rupay jeet kar.")
# play_kbc()




# a = input("Enter a string value :=")
# s = str(a)
# if(s == quit):
#     raise ValueError("Enter a string value")


# list = [85, 99, 58, 00, 34, 77, 38]
# for index, list in enumerate(list):
#     print(list)
#     if(index==3):
#         print("You are Aweosome")


import math 

print(dir(math))