"""
Sum The Strings

Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

https://www.codewars.com/kata/5966e33c4e686b508700002d
"""


def sum_str(a, b):
    a = "0" if a == "" else a
    b = "0" if b == "" else b
    if (a.isdigit() or (a[0] == "-" and a[1:-1].isdigit())) and (b.isdigit() or b[1:-1].isdigit()):
        return str(int(a) + int(b))