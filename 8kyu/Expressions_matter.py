"""
Task
Given three integers a ,b ,c, return the largest number obtained after
inserting the following operators and brackets: +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return
the Maximum Obtained (Read the notes for more detail about it)

Example
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:
1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9

So the maximum value that you can obtain is 9.

https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
"""


def expression_matter(a, b, c):
    qq = a + b + c
    ww = a * b * c
    ee = (a + b) * c
    rr = a * (b + c)
    return max(qq, ww, ee, rr)