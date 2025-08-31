import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Digital Clock")


label = tk.Label(root, font=("Calibri", 50, "bold"), background="yellow", foreground="black")
label.pack(anchor="center")


def update_time():
    string = strftime("%H:%M:%S %p\n%d/%m/%y")  
    label.config(text=string)
    label.after(1000, update_time)  

update_time()


root.mainloop()
