"""
Reversed Words

Complete the solution so that it reverses all of the words within the string passed in.

https://www.codewars.com/kata/51c8991dee245d7ddf00000e
"""


def reverse_words(s):
    return " ".join(s.split()[::-1])