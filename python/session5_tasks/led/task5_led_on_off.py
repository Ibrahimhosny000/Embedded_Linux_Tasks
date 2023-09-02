# ---------------------------------------------------------------
# ---------                                       -----------
#     Write a program that makes a led goes on and off:-
# ---------                                       -----------
# ---------------------------------------------------------------
from tkinter import *

root = Tk()


def led_on():
    canvas.itemconfig(outled, fill="red")
    label3.config(text="Led is on")


def led_off():
    canvas.itemconfig(outled, fill="white")
    label3.config(text="Led is off")


canvas = Canvas(root, width=180, height=280)
canvas.pack()

outled = canvas.create_oval(20, 20, 80, 80, fill="white")

label3 = Label(root)
label3.pack()

button_on = Button(root, text="LED On", command=led_on)
button_on.pack()

button_off = Button(root, text="LED Off", command=led_off)
button_off.pack()


root.mainloop()
