# --------------------------------------------------------------------------------
# ---------                                                        -------------
# Write a Python program to get names from a list and types it in a text file.
# ---------                                                        -------------
# --------------------------------------------------------------------------------
myfullname = ["Ibrahim", "hosny", "ibrahim", "gharib", "sleem"]

with open("myname.txt", "w") as myname:
    myname.write(" ".join(myfullname))

print(open("myname.txt").read())
