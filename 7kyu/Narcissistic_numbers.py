"""
Narcissistic Numbers

A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original
number. If this seems confusing, refer to the example below.

Ex: 153, where n = 3 (number of digits in 153)
13 + 53 + 33 = 153
https://www.codewars.com/kata/56b22765e1007b79f2000079
"""


def is_narcissistic(number):
    num_str = str(number)
    length = len(num_str)
    return sum(int(char) ** length for char in num_str) == number