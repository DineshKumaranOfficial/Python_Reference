my_list = [1, 2, 3, 4, 5, 6, 7]

print(list(map(lambda num: num**2, my_list)))
print(list(filter(lambda num: num % 2 != 0, my_list)))
