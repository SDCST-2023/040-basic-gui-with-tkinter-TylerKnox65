import tkinter as t
from tkinter import font


window = t.Tk()
window.title("Example")
window.geometry("400x155")

padding = t.Label(window, text="                 ")
dogphoto = t.PhotoImage(file="dog.png")
dog = t.Label(window, image=dogphoto)
poch = t.Label(window, text="Pochacco!!", font=("calibri", 15))
text = t.Label(window, text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and KeroKero", bg="#add8e6", font=("calibri", 15), borderwidth=3)


padding.grid(row=1, column=1)
dog.grid(row=1, column=2)
poch.grid(row=1, column=3)

text.grid(row=2, columnspan=5)

window.mainloop()