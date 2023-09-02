# -----------------------------------------------------------------------------
# ---------                                                  -------------
# Write a Python program to count the number of lines in a text file.
# ---------                                                  -------------
# -----------------------------------------------------------------------------


# -------------   simple way by defining the file name:   ---------------

# file = open("text.txt", "+r")  # instead of text.txt enter a name of another text file
# print(f"The number of lines in file is {len(file.readlines())}")

# ------------   advanced way by choosing the file you want to read: -----------------
# ------------   gets all .txt files in the same directory as this script ------------


import os


def find_txt_files():
    files = os.listdir(".")  # gets all files in directory
    filename = []
    for file in files:
        if file.endswith(".txt"):  # iterates over files and get what ends with .txt
            filename.append(file)

    return filename


filename = find_txt_files()  # returnes the list of .txt files
x = list(filename)

filename = input(
    f"Enter file name you want to count it's number of lines from this list:{filename}  "
)
if filename in x:
    imported = open(f"{filename}", "+r")
    print(f"the number is {len(imported.readlines())}")
else:
    print("file not found")
