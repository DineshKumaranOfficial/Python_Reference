def fibonacci(num):
    current = -1
    next = 1
    for i in range(num):
        value = next + current
        current = next
        next = value
        yield value


for i in fibonacci(20):
    print(i, end=',')
