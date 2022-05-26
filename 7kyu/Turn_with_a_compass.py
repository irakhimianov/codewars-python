"""
Turn with a Compass

You receive the direction you are facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW) and
a certain degree to turn (a multiple of 45, between -1080 and 1080); positive means clockwise,
and negative means counter-clockwise.

Return the direction you will face after the turn.

https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2
"""


def direction(facing, turn):
    # your smart code here
    direction = {'N' : 0,
                 'NE' : 45,
                 'E' : 90,
                 'SE' : 135,
                 'S' : 180,
                 'SW': 225,
                 'W' : 270,
                 'NW' : 315,
                }
    return str([key for key, val in direction.items() if val == (direction[facing] + turn) % 360][0])