# -------------------------------------------
# ---------                    ----------
#      gauge pic that moves randomly :-
# ---------                    ----------
# -------------------------------------------


from tkinter import *
import random


canvas_width = 400
canvas_height = 300


root = Tk()


def move_gauge():
    newvalue = random.randint(low_r, hi_r)
    cnvs.itemconfig(id_text, text=str(newvalue) + " %")
    angle = 120 * (hi_r - newvalue) / (hi_r - low_r) + 30
    cnvs.itemconfig(id_needle, start=angle)
    root.after(3000, move_gauge)


cnvs = Canvas(root, width=canvas_width, height=canvas_height)
cnvs.grid(row=2, column=1)

dimentions = 10, 50, 350, 350
low_r = 0
hi_r = 100

max = 8
for i in range(max):
    cnvs.create_arc(
        dimentions,
        start=(i * (120 / max) + 30),
        extent=(120 / max),
        fill="white",
        width=1,
    )

cnvs.create_arc(
    dimentions, start=30, extent=120, outline="green", style="arc", width=40
)
cnvs.create_arc(dimentions, start=30, extent=20, outline="red", style="arc", width=40)
cnvs.create_arc(
    dimentions, start=50, extent=20, outline="yellow", style="arc", width=40
)
id_needle = cnvs.create_arc(dimentions, start=119, extent=1, width=7)

cnvs.create_text(180, 15, font="Times 18 italic bold", text="Humidity")
cnvs.create_text(25, 140, font="Times 10 bold", text=low_r)
cnvs.create_text(330, 140, font="Times 10 bold", text=hi_r)
id_text = cnvs.create_text(160, 190, font="Times 15 bold")

root.after(3000, move_gauge)
root.mainloop()
