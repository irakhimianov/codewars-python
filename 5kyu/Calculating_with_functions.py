"""
This time we want to write calculations using functions and get the results.

Let's have a look at some examples:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand

Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))

https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
"""


def zero(func=None):
    if not func:
        return 0
    return func(0)


def one(func=None):
    if not func:
        return 1
    return func(1)


def two(func=None):
    if not func:
        return 2
    return func(2)


def three(func=None):
    if not func:
        return 3
    return func(3)


def four(func=None):
    if not func:
        return 4
    return func(4)


def five(func=None):
    if not func:
        return 5
    return func(5)


def six(func=None):
    if not func:
        return 6
    return func(6)


def seven(func=None):
    if not func:
        return 7
    return func(7)


def eight(func=None):
    if not func:
        return 8
    return func(8)


def nine(func=None):
    if not func:
        return 9
    return func(9)


def plus(num):
    return lambda x: x + num


def minus(num):
    return lambda x: x - num


def times(num):
    return lambda x: x * num


def divided_by(num):
    return lambda x: int(x / num)
