"""
Find The Parity Outlier

"""

x = [2, 4, 0, 100, 4, 11, 2602, 36]
y = [160, 3, 1719, 19, 11, 13, -21]

def find_outlier(integers):
    for num in integers:
        if sum(integers) % 2:
            if num % 2:
                return num
        else:
            if num % 2 == 0:
                return num

print(find_outlier(y))