"""
Is n divisible by x and y?

Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.

https://www.codewars.com/kata/5545f109004975ea66000086
"""

def is_divisible(n, x, y):
    return (n % x == 0) and (n % y == 0)