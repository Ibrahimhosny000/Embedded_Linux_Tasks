#!/usr/bin/python3
# -----------------------------------------------------------------------------------------------
# ----------                                                                -------------
#       write a python program to test whether a passed letter is a vowel or not.

# ----------                                                                -------------
# -----------------------------------------------------------------------------------------------
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
letter = input("enter a letter to see if it is vowel or not ")
if letter in vowels:
    print(f'entered letter  "{letter}"  is vowel')
else:
    print(f'entered letter  "{letter}"  is NOT vowel')
