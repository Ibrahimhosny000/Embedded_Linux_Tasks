#!/usr/bin/python3
# ---------------------------------------------------------------
# ----------                                   ----------
#       write a python code that handel login system:-
# ----------                                   ----------
# ---------------------------------------------------------------
userdata = {"Ahmed": "1394", "Ali": "6078", "Amr": "9345"}
username = input("enter your username ")
password = input("enter your password ")

if username in userdata:
    if userdata[username] == password:
        print(f"welcome {username}")
    else:
        print(f"{username} your password is incorrect")
else:
    print("incorrect entry")
