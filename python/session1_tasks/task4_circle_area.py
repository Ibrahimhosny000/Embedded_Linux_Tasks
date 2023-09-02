#!/usr/bin/python3
# --------------------------------------------------------------------------------------------------------------
# ----------                                                                                      ----------
#       Write a Python program which accepts the radius of a circle from the user and compute the area.
# ----------                                                                                      ----------
# --------------------------------------------------------------------------------------------------------------
import math

pi = math.pi
radius = float(input("enter a radius of a circle to calculate it's area "))
area = pi * radius * radius
print(f"area of the circle = {area} cm\u00b2")
