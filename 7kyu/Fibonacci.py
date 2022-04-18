"""
Fibonacci

Create function fib that returns n'th element of Fibonacci sequence (classic programming task).

https://www.codewars.com/kata/57a1d5ef7cb1f3db590002af
"""


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return 1 if n == 1 else fib2