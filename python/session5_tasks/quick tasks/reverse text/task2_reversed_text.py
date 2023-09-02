# ------------------------------------------------------------------------------------------
# ---------                                                                  -----------
#     Write a program that asks the user to type a word and return him its reverse
# ---------                                                                  -----------
# ------------------------------------------------------------------------------------------
from tkinter import *


def reverse_word():
    str = e1.get()
    clear_text()
    e2.insert(index=0, string=str[::-1])


def clear_text():
    e2.delete(0, "end")


master = Tk()

master.geometry("300x100+200+200")
Label(master, text="Enter words").grid(row=0, column=0)
# input box
e1 = Entry(master)
e1.grid(row=0, column=1)
# output box
e2 = Entry(master)
e2.grid(row=1, column=1)
# validation button
btn = Button(master, text="validation", command=reverse_word, width=13)
btn.grid(row=3, column=1)


master.mainloop()
