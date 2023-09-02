# ------------------------------------------------------------------------------------------------------------
# ---------                                                                                     ----------
#     Write a program in Python that displays a window to the user that asks them to enter an integer
# N and displays its factorial
# ---------                                                                                     ----------
# --------------------------------------------------------------------------------------------------------S----
from tkinter import *
import math

window = Tk()


def validation():
    num = int(e1.get())
    factorial_result = math.factorial(num)
    result.config(text=f"factorial {num} is {factorial_result}")


window.geometry("350x100")


input_num = Label(window, text="Enter a number: ")
input_num.pack()

e1 = entry = Entry(window)
entry.pack()

result = Label(window, text="")
result.pack()


output = Button(window, text="Validate", command=validation)
output.pack()


window.mainloop()
