from functools import reduce


def add(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        raise TypeError("Hey you should give numbers for adding")
    else:
        return num1 + num2


print(add(1, '2'))
