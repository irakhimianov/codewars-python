"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters
after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

https://www.codewars.com/kata/530e15517bc88ac656000716
"""

from string import ascii_lowercase, ascii_uppercase


def rot13(message):
    s = ''
    for char in message:
        if char in ascii_lowercase:
            s += ascii_lowercase[(ascii_lowercase.find(char) + 13) % 26]
        elif char in ascii_uppercase:
            s += ascii_uppercase[(ascii_uppercase.find(char) + 13) % 26]
        else:
            s += char
    return s
