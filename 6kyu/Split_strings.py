"""
Split Strings

Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final
pair with an underscore ('_').

https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
"""


def solution(text):
    res = []
    if len(text) % 2 == 1:
        text += "_"
    for i in range(0, len(text), 2):
        res.append(text[i:i+2])
    return res
