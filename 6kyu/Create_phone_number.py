"""
Create Phone Number

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those
numbers in the form of a phone number.

https://www.codewars.com/kata/525f50e3b73515a6db000b83
"""


def create_phone_number(numbers):
    #your code here
    n = ''.join([str(num) for num in numbers])
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"