"""
Even and Odd !

Given a number N, can you fabricate the two numbers NE and NO such that NE is formed by even digits of N and NO is formed by odd digits of N?
0 is considered as an even number.

https://www.codewars.com/kata/594adadee075005308000122
"""


def even_and_odd(num):
    # your code here
    list_of_num = [int(i) for i in str(num)]
    NE = ''.join(str(e) for e in list(filter(lambda x: x % 2, list_of_num)))
    NO = ''.join(str(e) for e in list(filter(lambda x: x % 2 == 0, list_of_num)))
    return (0 if not NO else int(NO)), (0 if not NE else int(NE))