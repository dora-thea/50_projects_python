import tkinter as tk
from tkinter import messagebox


def is_valid(val):
    for v in val:
        if v not in "-+0123456789.*/)(=":
            return False
    return True


window = tk.Tk()
window.geometry("300x400")
window.title("Calculator")

for c in range(4):
    window.columnconfigure(index=c, weight=1)
for r in range(6):
    window.rowconfigure(index=r, weight=1)

check = (window.register(is_valid), "%P")
calc_entry = tk.Entry(window, validate="key", validatecommand=check)
calc_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

button_list = [
    "C", "±", "(", ")",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

i = 0
for r in range(1, 6):
    for c in range(0, 4):
        tk.Button(window, text=button_list[i],
                  command=(lambda x=button_list[i]: calc(x))).grid(row=r, column=c, sticky="nsew")
        i += 1


def calc(key):
    if key == "=":
        try:
            result = eval(calc_entry.get())
            calc_entry.delete(0, tk.END)
            calc_entry.insert(tk.END, str(result))
        except SyntaxError:
            calc_entry.insert(tk.END, "Error!")
            tk.messagebox.showerror("Error!", "Check the correctness of data")
    elif key == "C":
        calc_entry.delete(0, tk.END)
    elif key == "±":
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        calc_entry.insert(tk.END, key)


window.mainloop()
