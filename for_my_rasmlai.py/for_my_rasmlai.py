import time
import sys
import os

def slow_type(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# === 🎻 WINDOWS DIRECT AUDIO PLAYER BYPASS ===
music_file = "music.mp3"
original_name = "Ab yahaan se kahaan jaayein hum  #TujheDekhaToh  #DilwaleDulhaniaLeJayenge  #ShahRukhKhan #Kajol.mp3"

# Agar rename sahi se nahi hua toh original naam check karega
if not os.path.exists(music_file) and os.path.exists(original_name):
    music_file = original_name

if os.path.exists(music_file):
    # 🎯 JADU: Windows ka apna default player piche background mein chalu ho jayega!
    os.system(f'start /b "" "{music_file}"')
else:
    print("⚠️ Bhai gaane ki file is folder mein nahi mil rahi hai!")
    print("Ek baar check karo ki gaana aur code dono 'gitdemo' folder ke andar hi hain na?\n")

# === 🎤 LYRICS SYNC ===
print("\033[1;35m") # Pink Color
slow_type("Tujhe dekha toh yeh jaana sanam... ❤️", 0.12)
time.sleep(1.2)

slow_type("Pyaar hota hai deewana sanam...", 0.12)
time.sleep(1.5)

print("\033[1;36m") # Cyan Color
slow_type("Ab yahan se kahan jaayein hum?", 0.1)
time.sleep(0.8)
slow_type("Teri baahon mein mar jaayein hum... 😉", 0.1)
time.sleep(2)

# === 💌 SPECIAL MESSAGE ===
print("\033[1;32m") # Green Color
slow_type("\nKhurapaat toh main roz karta hoon...", 0.08)
slow_type("Par aap meri life ka sabse haseen logic ho! 👑✨", 0.08)
time.sleep(2)

print("\033[1;33m") # Yellow Color
slow_type("\nCreating your digital rose...", 0.1)
for _ in range(4):
    sys.stdout.write("🌹 ")
    sys.stdout.flush()
    time.sleep(0.6)
    
print("\n\033[1;31m") # Red Color

# === 🌹 THE FINAL FLOWER ===
flower = """
       _.-.
     .'  _/_
    /   .   \\
   :   .     :
    \   '   /
     '. _\_.'
        ||
     _  ||  _
    (_\ || /_)
       \||/
        ||  
        ||   ❤️ HAPPY SURPRISE! ❤️
        ||   Tu hai meri Simran!
        ||   
"""

for line in flower.split('\n'):
    print(line)
    time.sleep(0.1)

print("\033[0m")