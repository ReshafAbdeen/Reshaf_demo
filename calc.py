#MY FIRST AI-DS CALCULATER

import tkinter as tk 
def button_click(char):
    global entry
    current = entry.get()

    if char == "c":
        entry.delete(0, tk.END)
    elif char == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error!")

    else:
        entry.insert(tk.END, char)


root = tk.Tk()
root.title("My AI-DS Calculator")
root.geometry("300x400")
root.configure(bg="#45502cff")

entry = tk.Entry(root , font=("Arial", 20), bd =5, insertwidth = 4, width = 14, borderwidth = 0, justify= "right")
entry.grid(row = 0, column = 0, columnspan = 4, ipady = 15, padx = 10, pady = 20)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for btn in buttons:
    action = lambda x=btn: button_click(x)
    button = tk.Button(root, text=btn, padx=20, pady=20, font=("Arial", 14, "bold"),
                       bg="#b8c227", fg="white", activebackground="#1abc9c", borderwidth=0, command=action)
    button.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

    col_val += 1
    if col_val > 3 :
        col_val = 0
        row_val += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1) 


root.mainloop()
