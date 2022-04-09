"""
Find the Remainder

Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.
Division by zero should return an empty value.

https://www.codewars.com/kata/524f5125ad9c12894e00003f
"""


def remainder(a, b):
    #your code here
    if a >= b and b:
        return a % b
    elif a < b and a:
        return b % a
    else:
        return None