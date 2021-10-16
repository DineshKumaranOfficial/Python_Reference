from functools import reduce

my_list = [1, 2, 3, 4, 5, 6, 7]


def sumoflist(sum, num):
    print(sum, num)
    return sum + num


print(reduce(sumoflist, my_list))
