"""
Get the Middle Character


You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"

https://www.codewars.com/kata/56747fd5cb988479af000028
"""

def get_middle(s):
    return f'{s[len(s) // 2 - 1]}{s[len(s) // 2]}' if (not len(s) % 2 and len(s) > 1) else f'{s[len(s) // 2]}'


print(get_middle('test'))
print(get_middle('testa'))
print(get_middle('a'))