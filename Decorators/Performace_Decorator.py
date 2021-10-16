from time import time


def performance(func):
    def wrapper_func(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Took {end_time - start_time: .4f} Sec")
        return result
    return wrapper_func


@performance
def some_long_time_taking_function():
    for i in range(100000000):
        i*8


some_long_time_taking_function()
