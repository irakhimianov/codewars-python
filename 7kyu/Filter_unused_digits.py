"""
Filter unused digits

Given a varying number of integer arguments, return the digits that are not present in any of them.

Example:
[12, 34, 56, 78]  =>  "09"
[2015, 8, 26]     =>  "3479"

https://www.codewars.com/kata/55de6173a8fbe814ee000061
"""


def unused_digits(*digits):
    unused = "0123456789"
    digits = "".join([str(digit) for digit in digits])
    for digit in digits:
        unused = unused.replace(digit, "")
    return unused