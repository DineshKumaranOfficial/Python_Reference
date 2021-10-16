list1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 3, 2, 7]

duplicates = list({num for num in list1 if list1.count(
    num) > 1})

print(duplicates)
