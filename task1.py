import tkinter as t
from tkinter import font

window = t.Tk()
window.title("Tk")
window.geometry("600x40")

def X():
    
    try:
        num1_get = float(num1.get())
        num2_get = float(num2.get())
    
        final = num1_get * num2_get
        answer = t.Label(window, text=final, font=("calibri", 18))
        answer.grid(row=1, column=7)
    except:
        answer = t.Label(window, text="Error", font=("calibri", 18))
        answer.grid(row=1, column=7)
num1 = t.Entry(window, width=15, font=("calibri", 18))
Bx = t.Label(window, text="X")
num2 =t.Entry(window, width=15, font=("calibri", 18))
eq = t.Button(window, text="=", command=X)
padding = t.Label(window, text="             ")

num1.grid(row=1, column=1)
Bx.grid(row=1, column=2)
num2.grid(row=1, column=3)
eq.grid(row=1, column=4)
padding.grid(row=1, column=5)
window.mainloop()