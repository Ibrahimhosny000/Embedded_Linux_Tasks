# -----------------------------------------------------------------------------
# ---------                                                  -------------
#       Write python code to generate Init function of GPIO for AVR:-
# ---------                                                  -------------
# -----------------------------------------------------------------------------
bitlist = []
for i in range(0, 8):
    bit = input("Enter in/out for data direction for register A :   ").lower().strip()
    con1 = "in"
    con2 = "out"
    if bit == con1:
        bitlist.append(0)

    elif bit == con2:
        bitlist.append(1)
    else:
        print("wrong entery")
        break

bits = "".join([str(i) for i in bitlist])
ddra = f"0b{bits}"
new = open("Direction.c", "a")
x = "{"
y = "}"
new.write(f"void Init_PORTA_DIR (void) \n{x}\n      DDRA = {ddra};\n{y}")
