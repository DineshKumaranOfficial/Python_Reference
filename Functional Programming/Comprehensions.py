mylist = [[i, j, k] for i in range(3) for j in range(3) for k in range(3)]

list2 = [num**2 for num in range(10) if num % 2 == 0]

list3 = [num**2 if num % 2 == 0 else 0 for num in range(10)]

# print(mylist)
print(list2)
print(list3)
