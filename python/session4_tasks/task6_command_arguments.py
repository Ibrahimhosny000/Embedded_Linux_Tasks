# -------------------------------------------------------------------------
# ---------                                          ----------------
#     Write a Python program to get the command-line arguments:-
# ---------                                          ----------------
# --------------------------------------------------------------------------

import sys

arguments = sys.argv
number = len(arguments)
print(f"The number of arguments: {number}")
print(f"The arguments are ({sys.argv})")
