"""
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none.

For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

https://www.codewars.com/kata/523a86aa4230ebb5420001e1
"""


def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]
