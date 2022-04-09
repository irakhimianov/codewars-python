"""
Sum of Digits / Digital Root

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until
a single-digit number is produced. The input will be a non-negative integer.

https://www.codewars.com/kata/541c8630095125aba6000c00
"""


def digital_root(n):
    while True:
        if len(str(n)) > 1:
            res = 0
            for char in str(n):
                res += int(char)
            n = res
        else:
            break
    return n