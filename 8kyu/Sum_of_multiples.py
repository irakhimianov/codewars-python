"""
Sum of Multiples

Find the sum of all multiples of n below m

https://www.codewars.com/kata/57241e0f440cd279b5000829
"""


def sum_mul(n, m):
    if n * m <= 0:
        return "INVALID"
    elif n == m:
        return 0
    else:
        sum = 0
        for i in range(n, m, n):
            sum += i
        return sum