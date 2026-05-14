

# #MY first notification code
# import time
# from plyer import notification

# time_hour = float(input("set the alert after you want to drink water:"))
# for i in range(5):
# #     time.sleep(10)
#     notification.notify(title = "water", message = "you should drink water", timeout = 2)
    # time.sleep(5)


# num1 = float(input("Enter a value :"))
# num2 = float(input("Enter second value :"))

# print("Choose optrator = +, -, *, /, %")
# op = input("Operator (*, /, -, +, /) :")

# if op =="+":
#     print("Result", num1 + num2)

# elif op == "-":
#     print("Result", num1 - num2)

# elif op == "/":
#      if num2 != 0:
#        print("Result", num1 / num2)
#      else:
#          print("Error! Zero se koi divide nhi kar sakta.")

# elif op == "*":
#     print("Result", num1 * num2)

# elif op == "%":
#     print("Result", num1 % num2)

# else:
#     print("Invalide operation.")

# name = input("Ek naam likhe :")
# adj = input("adjective likhen(mazedaar, achha, etc. :)")
# verb = input("ek verrb likhen (naachna, gaana etc)")
# place = input("Ek jagh ka naam likhein :")

# story = (f"Ek baar ki baat hai ek {name} naam kabanda tha bo ghoommne{place} jaata hai to use baha ek bhoot milta hai use {verb} bohot pasand hota hai story {adj} lagi ")
# print("\n--- Apki mad Lips story ---")
# print(story)

# def  binary_serach(arr, target):
#     low = 0
#     high =len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target: 
#              high = mid-1
        
#         else:
#              low = mid+1

#     return -1
# num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 6]
# result = binary_serach(num, 5 )
# print(result)

# import datetime
# import time
# from playsound import playsound 
# from plyer import notification

# def set_alarn(alrm_time):
#     print(f"Alarm {alrm_time} time ka set ho gya hai.")

#     while True:
#         now = datetime.datetime.now().strftime("%H:%M")

#         if now == alrm_time:

#             notification.notify(title = "Alarm Clock", message = "Utho waqt ho gya hai uthne ka.", app_icon = None, timeout = 10)
#             print("utho alrm baj rha hai.")

#             try:
#                 playsound(r' C:\Users\abdee\Desktop\cscorner\GITDEMO\alarm.mp3')

#             except Exception as e:
#                 print(f"playsound error! {e}")
#                 import winsound
#                 winsound.Beep(1000, 2000)

#             break 


#         time.sleep(1)

# user_time = input("Alar ka time dalien :")
# set_alarn(user_time)


# import math
# def scintific_calc():
#     print("---Scintific Calculator---")
#     print("Option: 1.Square, Root 2.Power\n3.log, 4.sin, 5.factorial")

#     choice = input("Kiya calculate karen? (1-5)")


#     if choice == '1':
#         num = float(input("Number Dalien: "))
#         print(f"Square Root {math.sqrt(num)}")

#     elif choice == '2':
#         base = float(input("Number Dalein: "))
#         exp = float(input("Power dalien: "))
#         print(f"Result {math.pow(base, exp)}")

#     elif choice == '3':
#         num = float(input("Number dein: "))
#         print(f"log (base 10) {math.log10(num)}")

#     elif choice == '4':
#         angle = float(input("Angle (degree mein): "))
#         res = math.sin(math.radians(angle))
#         print(f"sin{angle}: {res}")

#     elif choice == '5':
#         num = int(input("Enter a full number: "))
#         print(f"Factorial {math.factorial(num)}")

# scintific_calc()

# import requests

# def get_exchange(base_currency, target_currency):
#     url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
#     response = requests.get(url)
#     data = response.json()
#     return data['rates'][target_currency]

# def return_currancy(amount, rate):
#     return amount * rate
# from_currency = input("Kis currency me badlna chahte hai (like = USD, DINAR etc.) :").upper()
# to_currency = input("Kis currency ko badlna chahte hai (like = INR, PKR etc.): ").upper()
# amt = float(input("Kitne oaise badlne hai : "))



# rate = get_exchange(from_currency, to_currency)
# result = return_currancy(amt, rate)

# print(f"{amt} {from_currency} ki value {result} {to_currency} hai .")


# import instaloader

# bot = instaloader.Instaloader()
# post_url = input("Instagram post ka url yha paste karen :")

# try:
#     shortcode = post_url.split("/")[-2]
#     post = instaloader.Post.from_shortcode(bot.context, shortcode)
#     bot.download_post(post, target=f"{post.owner_username}_post")
#     print("Congratulation! Photo download ho gyi.")

# except Exception as e:
#     print(f"Something went wrong! {e}")


# import instaloader
# import os
# from moviepy import VideoFileClip, AudioFileClip

# # 1. बॉट तैयार करें
# bot = instaloader.Instaloader()

# # 2. लॉगिन (वीडियो/ऑडियो के लिए अक्सर ज़रूरी होता है)
# USER = "your_username"
# PASS = "your_password"
# bot.login(USER, PASS) 

# post_url = input("Instagram post ka url yha paste karen: ")

# try:
#     # URL से शॉर्टकोड निकालना
#     shortcode = post_url.strip("/").split("/")[-1]
#     post = instaloader.Post.from_shortcode(bot.context, shortcode)
    
#     # डाउनलोड फोल्डर का नाम
#     target_dir = f"{post.owner_username}_post"
    
#     # डाउनलोड शुरू करें
#     bot.download_post(post, target=target_dir)
#     print("Files download ho gayi hain. Ab merging shuru ho rahi hai...")

#     # अगर यह एक वीडियो है, तो MoviePy का इस्तेमाल करें
#     if post.is_video:
#         video_file = ""
#         audio_file = ""

#         # फोल्डर के अंदर वीडियो और ऑडियो फाइलें ढूंढें
#         for file in os.listdir(target_dir):
#             if file.endswith(".mp4"):
#                 video_file = os.path.join(target_dir, file)
#             elif file.endswith(".m4a"): # इंस्टाग्राम अक्सर .m4a में ऑडियो देता है
#                 audio_file = os.path.join(target_dir, file)

#         if video_file and audio_file:
#             # MoviePy से मर्ज करना
#             video_clip = VideoFileClip(video_file)
#             audio_clip = AudioFileClip(audio_file)
            
#             final_clip = video_clip.set_audio(audio_clip)
#             final_clip.write_videofile(os.path.join(target_dir, "final_video_with_sound.mp4"))
            
#             print("Congratulation! Video with sound ready hai.")
#         else:
#             print("Video ya Audio file nahi mili.")
#     else:
#         print("Ye ek Photo post thi, download ho gayi hai.")

# except Exception as e:
#     print(f"Something went wrong! {e}")

# import yt_dlp

# url = input("Link:") 
# with yt_dlp.YoutubeDL({'formate' : 'best'}) as ydl:
#     ydl.download(url)


import yt_dlp

def download_with_audio(url):
    try:
        # ये सेटिंग्स वीडियो और ऑडियो को अपने आप मर्च कर देंगी
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s', # फाइल का नाम
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading... please wait.")
            ydl.download([url])
            
        print("\nSuccess! Video with audio download ho gayi hai.")

    except Exception as e:
        print(f"Error: {e}")

link = input("Instagram video/reel ka link yaha dale: ")
download_with_audio(link)
