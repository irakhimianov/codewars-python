"""
Case Swapping

Given a string, swap the case for each of the letters.

https://www.codewars.com/kata/5590961e6620c0825000008f
"""


def swap(string_):
    res = ""
    for char in string_:
        if char.isupper():
            res += char.lower()
        else:
            res += char.upper()
    return res