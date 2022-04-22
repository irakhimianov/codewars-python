"""
Dbftbs Djqifs
Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers, spaces,
and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!


https://www.codewars.com/kata/546937989c0b6ab3c5000183
"""


def encryptor(key, message):
    alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                      'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    new_text = ''
    for char in message:
        if char in alphabet_upper:
            new_text += alphabet_upper[(alphabet_upper.index(char) + key) % 26]
        elif char in alphabet_lower:
            new_text += alphabet_lower[(alphabet_lower.index(char) + key) % 26]
        else:
            new_text += char
    return new_text