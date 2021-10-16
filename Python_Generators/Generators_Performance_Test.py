from time import time

# Generators costs less memory usage as it doesn't store previous values that are used for the process


def performance(func):
    def wrapper_func(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Took {end_time - start_time: .4f} Sec")
        return result
    return wrapper_func


@performance
def generator_func(num):
    for i in range(num):
        i * 8


@performance
def normal_func_with_list(num):
    for i in list(range(num)):
        i * 8


generator_func(1000000)
normal_func_with_list(1000000)
