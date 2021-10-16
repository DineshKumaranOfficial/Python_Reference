import Decorators.Performace_Decorator


@Decorators.Performace_Decorator.performance
def add(num1, num2):
    return num1 + num2


@Decorators.Performace_Decorator.performance
def sub(num1, num2):
    return num1 + num2
