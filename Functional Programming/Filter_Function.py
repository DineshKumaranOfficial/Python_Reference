def give_odd_numbers(item):
    return item % 2 != 0


my_list = [1, 2, 3, 4, 5, 6, 7]
print(list(filter(give_odd_numbers, my_list)))
print(my_list)
