import tkinter as t
from tkinter import font


window = t.Tk()
window.title("Example")
window.geometry("400x155")


dogphoto = t.PhotoImage(file="dog.png")
dog = t.Label(window, image=dogphoto)
poch = t.Label(window, text="Pochacco!!", font=("calibri", 15))
text = t.Label(window, text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and KeroKero", bg="#add8e6", font=("calibri", 15), borderwidth=3)


dog.place(x=130, y=0)
poch.place(x=200, y=50)

text.place(x=0, y=100)

window.mainloop()