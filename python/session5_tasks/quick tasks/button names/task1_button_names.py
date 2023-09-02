# -----------------------------------------------------------------------------
# ---------                                                  -------------
#      Make a template and each button display different name:-
# ---------                                                  -------------
# -----------------------------------------------------------------------------
import tkinter as tk

m = tk.Tk()


# button1_fuction
def button1():
    print("python")


bt1 = tk.Button(m, text="Button1", width=8, command=button1)
bt1.grid(row=0, column=1)


# button2_function:-
def button2():
    print("c++")


bt2 = tk.Button(m, text="Button2", width=8, command=button2)
bt2.grid(row=1, column=0)


# button3_function
def button3():
    print("bash")


bt3 = tk.Button(m, text="Button3", width=8, command=button3)
bt3.grid(row=1, column=2)

# buttin4_function


def button4():
    print("Rust")


bt4 = tk.Button(m, text="Button4", width=8, command=button4)
bt4.grid(row=2, column=1)


m.title("Quik Task one")
m.geometry("275x100+700+200")

m.mainloop()
