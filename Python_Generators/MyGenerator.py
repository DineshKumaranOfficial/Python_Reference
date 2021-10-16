from typing import Counter


class my_generator():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if my_generator.current < self.last:
            value = my_generator.current
            my_generator.current += 1
            return value
        raise StopIteration


for i in my_generator(0, 100):
    print(i, end=',')
