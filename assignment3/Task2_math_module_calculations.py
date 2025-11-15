"""
------------------------------------------------------------
Title: Assignment 3 Task 2 - Using the Math Module for Calculations
Author: Ankita Bhardwaj
Date: November 2025
Description:
    This program takes a number as input from the user, uses the math module and
    calculates:
    --> Square root of the number
    --> Natural Logarithm (log base e) of the number
    --> Sine of the number (in radians)
------------------------------------------------------------
"""
import math

# taking input from user
n = float(input("Enter a number: "))

# calculating and printing Square root of the number
print(f"Square root: {math.sqrt(n)}")

# calculating and printing Natural logarithm (only valid for n > 0)
if n > 0:
    print(f"Logarithm: {math.log(n)}")
else:
    print("Logarithm: Undefined for zero or negative numbers")

# calculating and printing Sine of the number (in radians)
print(f"Sine: {math.sin(n)}")
