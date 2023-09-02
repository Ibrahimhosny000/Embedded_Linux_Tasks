# -----------------------------------------------------------------------------
# ---------                                                -------------
#       Python program to parse header file and read all prototypes:-
# ---------                                                -------------
# -----------------------------------------------------------------------------

# not so will understandable : some parts of code are unknown to me


import re
import openpyxl as xl


types = []
feedback = []
protype = []


def parsing(datafile):
    with open(datafile, "r") as funcs:
        file = funcs.read()

    with open("header.h", "r") as f:
        for line in f:
            return_type = line.split()
            if return_type:
                feedback.append(return_type[0])

    pattern = r"\(.*?\)|\w+ |;|\s"
    founds = re.sub(pattern, " ", file)
    pattern = r"\w+\S"
    founds = re.findall(pattern, founds)
    for word in founds:
        founds = word.split()
        protype.append(founds)

    pattern = r"\(.*?\)"
    matches = re.findall(pattern, file)
    for match in matches:
        types.append(match.strip())

    workbook = xl.Workbook()
    sheet = workbook.active

    sheet["A1"] = "ID"
    sheet["B1"] = "Return"
    sheet["C1"] = "Fun_Prototype"
    sheet["D1"] = "Fun_Arguments"

    row = 0
    for i in range(len(feedback)):
        row = i + 2
        sheet[f"A{row}"] = f"IDX{i}"
        sheet[f"B{row}"] = feedback[i]
        sheet[f"c{row}"] = protype[i][0]
        sheet[f"D{row}"] = types[i]

    workbook.save("Header_File.xlsx")


parsing("header.h")
