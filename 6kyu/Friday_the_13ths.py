"""
Friday the 13ths

Create the function fridayTheThirteenths that accepts a start year and an end year (inclusive), and returns all of the
dates where the 13th of a month lands on a Friday in the given range of year(s).

The return value should be a string where each date is seperated by a space. The date should be formatted like 9/13/2014
where months do not have leading zeroes and are separated with forward slashes.

If no end year is given, only return friday the thirteenths during the start year.

https://www.codewars.com/kata/540954232a3259755d000039
"""


from datetime import date


def friday_the_thirteenths(*years):
    result = ''
    for year in range(years[0], years[-1] + 1):
        for month in range(1, 13):
            if date(year, month, 13).isoweekday() == 5:
                friday = date(year, month, 13)
                result += f"{int(friday.month)}/{friday.day}/{friday.year} "
    return result[:-1]