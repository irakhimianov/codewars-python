"""
Write a program to determine if the two given numbers are coprime.
A pair of numbers are coprime if their greatest shared factor is 1.

The inputs will always be two positive integers between 2 and 99.

Examples
20 and 27:

Factors of 20: 1, 2, 4, 5, 10, 20
Factors of 27: 1, 3, 9, 27
Greatest shared factor: 1
Result: 20 and 27 are coprime

https://www.codewars.com/kata/585c50e75d0930e6a7000336
"""


def dividers(n):
    return [i for i in range(n, 0, -1) if not n % i]


def are_coprime(n, m):
    return 1 == max(set(dividers(n)) & set(dividers(m)))
