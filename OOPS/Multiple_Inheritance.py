class Mathoperation():
    def __init__(self):
        print("Math Operation")

    def message(self):
        print("Going to perform Math Operation")


class Add(Mathoperation):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def operation(self):
        return self.num1 + self.num2


class Sub(Mathoperation):
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def operation(self):
        return self.num1 - self.num2 - self.num3


class MultiOp(Add, Sub):
    def __init__(self, num1, num2, num3):
        Add.__init__(self, num1, num2)
        Sub.__init__(self, num1, num2, num3)

    def operation(self):
        print(Add.operation(self))
        print(Sub.operation(self))
        return self.num1*self.num2*self.num3


if __name__ == '__main__':
    multi = MultiOp(3, 2, 4)
    print(multi.message())
    print(multi.operation())
    # Method Resolution Order defines the checking order for the class during inheritance
    # Methods and attributes are accessed in the order defined in the MRO
    # MRO uses Depth First Search to bring this order
    print(MultiOp.mro())
