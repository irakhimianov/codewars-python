"""
RGB To Hex Conversion

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

https://www.codewars.com/kata/513e08acc600c94f01000001
"""



def rgb(r, g, b):
    RGB = (r, g, b)
    s = ""
    for num in RGB:
        if num > 255:
            s += 'FF'
        elif num < 0:
            s += '00'
        elif 0 <= num < 10:
            s += f'0{num}'
        else:
            s += str(hex(num)).upper()[2:]
    return s