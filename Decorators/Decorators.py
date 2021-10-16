def custom_decorator(func):
    def wrapper_func(*args, **kwargs):
        print("##########")
        func(*args, **kwargs)
        print("##########")
    return wrapper_func


@custom_decorator
def just_a_function(message, offense):
    print(message, offense)


just_a_function("Hi this is Sony", "With an offensive behaviour")
