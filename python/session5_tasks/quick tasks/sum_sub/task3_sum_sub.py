# ------------------------------------------------------------------------------------------
# ---------                                                                  -----------
#     code that asks the user to enter two numbers a sub or sum and print result:-
# ---------                                                                  -----------
# ------------------------------------------------------------------------------------------


from tkinter import *

master = Tk()


def operation():
    global v
    if v.get() == "add":
        result = float(e1.get()) + float(e2.get())
        operand = "Sum"
    elif v.get() == "sub":
        result = float(e1.get()) - float(e2.get())
        operand = "diffrence"
    str = f"The {operand} is {result}"
    e3.delete(0, "end")
    e3.insert(index=0, string=str)


master.geometry("330x140+200+200")
Label(master, text="Enter The value of x:").grid(row=0, column=0)
Label(master, text="Enter The value of y:").grid(row=1, column=0)


e1 = Entry(master)
e1.grid(row=0, column=1)

e2 = Entry(master)
e2.grid(row=1, column=1)

e3 = Entry(master, bd=2)
e3.grid(row=2, column=1)

btn = Button(master, text="validate", width=10, command=operation)
btn.grid(row=5, column=1)

v = StringVar()
Radiobutton(master, text="sum", variable=v, value="add").grid(row=4, column=0)
Radiobutton(master, text="sub", variable=v, value="sub").grid(row=5, column=0)


master.mainloop()
