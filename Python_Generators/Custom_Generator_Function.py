""" Generators are iterables that are used to return each entries one by one without totally consuming the memory.
The Yield keyword returns the item and gets back to the generator method. It keeps track of the last item it has processed.
The next method is used to iterate the items that are in the generator.
The yield returns to the method after passing the value until the range function limit is reached. 
After the limit it throws StopIteration Exception. """


def my_custom_generator(num):
    for num in range(num):
        yield num ** 2


generator_function = my_custom_generator(5)
next(generator_function)
next(generator_function)
next(generator_function)
print(next(generator_function))
