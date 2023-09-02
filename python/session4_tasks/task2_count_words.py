# -----------------------------------------------------------------------------
# ---------                                                  -------------
# Write a Python program to count the number of words in a text file.
# ---------                                                  -------------
# -----------------------------------------------------------------------------


file = open("newfile.txt", "r")  # insted of newfile enter any file name you have
text = file.read().split()
print(f"the number of words equals:{len(text)}")
