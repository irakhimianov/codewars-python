"""
Exclamation marks series #1: Remove an exclamation mark from the end of string

Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

https://www.codewars.com/kata/57fae964d80daa229d000126
"""


def remove(s):
    if s and s[-1] == "!":
        return s[:-1]
    else:
        return s