"""
Who likes it?

You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples

https://www.codewars.com/kata/5266876b8f4bf2da9b000362
"""


def likes(names):
    # your code here
    if len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) > 3:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
    else:
        return "no one likes this"