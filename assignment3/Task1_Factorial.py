"""
------------------------------------------------------------
Title: Assignment 3 Task 1 - Factorial Program
Author: Ankita Bhardwaj
Date: November 2025
Description:
    This program takes a number as input from the user and
    calculates the factorial of that number using a for loop.
------------------------------------------------------------
"""
# function for calculating Factorial
def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r = r * i
    return r

# Taking user input
n = int(input("Enter a number: "))

# Displaying result
print(f"Factorial of {n} is: {factorial(n)}")
