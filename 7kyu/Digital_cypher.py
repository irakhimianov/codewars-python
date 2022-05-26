"""
Digital cypher

Task
Write a function that accepts str string and key number and returns an array of integers representing encoded str.

Input / Output
The str input string consists of lowercase characters only.
The key input number is a positive integer.

Example
Encode("scout",1939);  ==>  [ 20, 12, 18, 30, 21]
Encode("masterpiece",1939);  ==>  [ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]

https://www.codewars.com/kata/592e830e043b99888600002d
"""


def encode(message, key):
    dictionary = dict(zip((chr(i) for i in range(97, 123)), range(1, 27)))
    res = []
    for index, symbol in enumerate(message):
        res.append(dictionary[symbol] + int(str(key)[index % len(str(key))]))
    return res

