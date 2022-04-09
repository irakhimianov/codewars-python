"""
Is it a palindrome?

Write a function that checks if a given string (case insensitive) is a palindrome.

https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
"""


def is_palindrome(s):
    return s.lower() == s.lower()[::-1]