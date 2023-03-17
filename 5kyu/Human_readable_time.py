"""
Write a function, which takes a non-negative integer (seconds) as input and
returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

https://www.codewars.com/kata/52685f7382004e774f0001f7
"""


def make_readable(seconds):
    hh = seconds // 3600
    mm = (seconds - hh * 3600) // 60
    ss = seconds - hh * 3600 - mm * 60
    return f'{hh if hh >= 10 else "0" + str(hh)}:{mm if mm >= 10 else "0" + str(mm)}:{ss if ss >= 10 else "0" + str(ss)}'
