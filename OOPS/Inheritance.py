class Mathoperation():
    def __init__(self):
        print("Math Operation")

    def message(self):
        print("Going to perform Math Operation")


class Add(Mathoperation):
    def operation(self, num1, num2):
        return num1 + num2


class Sub(Mathoperation):
    def operation(self, num1, num2):
        return num1 - num2


if __name__ == "__main__":
    add = Add()
    print(add.message())
    print(add.operation(5, 5))
    sub = Sub()
    print(sub.message())
    print(sub.operation(5, 3))
    print(isinstance(add, Add))
    print(isinstance(add, Mathoperation))
    print(isinstance(add, object))
