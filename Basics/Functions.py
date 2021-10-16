def printSomething(name):
    """ Info : This will print the name you pass """
    print(f"Hi {name}")


printSomething('Dinesh')


def args_and_kwargs(*args, **kwargs):
    total = 0
    for value in kwargs.values():
        total += value
    print(args, kwargs, sep='\n')
    return sum(args) + total


print(args_and_kwargs(1, 2, 3, 4, 5, 6, num1=8, num2=10))
