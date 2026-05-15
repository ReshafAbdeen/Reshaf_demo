#THIS MY FIRST DIMPLE GREETING APP

import tkinter as tk
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def greet_user():
    name = entry.get()

    if name.strip():
        msg =  f"Hellow {name}. welcome to pythons world."

        engine.say(msg)
        engine.runAndWait()

        messagebox.showinfo("Message", msg )
    else:
        warning_msg = "Pehle apna naam likhe."
        engine.say(warning_msg)
        engine.runAndWait()
        messagebox.showwarning("Warning", warning_msg)
             
root = tk.Tk()
root.title("My first GUi")
root.geometry("300x200")

label = tk.Label(root, text = "Apna naam likhen", font =("Arial", 10))
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Greet Me!", command=greet_user, bg="lightblue")
button.pack(pady=20)

root.mainloop()