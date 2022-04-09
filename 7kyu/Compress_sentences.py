"""
Compress sentences

Your task is to make a program takes in a sentence (without puncuation), adds all
words to a list and returns the sentence as a string which is the positions of the word in the list.
Casing should not matter too.

https://www.codewars.com/kata/59de469cfc3c492da80000c5
"""


def compress(sentence):
    words = [s.lower() for s in sentence.split()]
    compress = {}
    result = ""
    ind = 0
    for word in words:
        if not word in compress:
            compress[word] = ind
            ind += 1
    for word in sentence.split():
        result += str(compress[word.lower()])
    return result