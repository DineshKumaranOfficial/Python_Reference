class Laptop:
    brand = "Lenovo"

    def __init__(self, ram, hdd, processor):
        self.ram = ram
        self.hdd = hdd
        self.processor = processor

    def laptopInfo(self):
        print(
            f"{self.brand} Laptop has {self.ram} RAM, {self.hdd} TB HDD and {self.processor}")

    def just_a_method(self, alpha: "str", somelist: "list", some_var) -> "str":
        print(f'{alpha.upper()}')
        somelist.reverse()
        print(f"{somelist}")
        print(f"{some_var}")
    # This method is shared by all the objects and it can be used without instantiating. We can even create an object
    # using the cls parameter

    @classmethod
    def addnumbers(cls, num1, num2):
        return num1 + num2

    # This method is same as class method. The difference is that we don't have access to the class
    @staticmethod
    def addtwonumbers(num1, num2):
        return num1 + num2


if __name__ == "__main__":
    laptop1 = Laptop(4, 1, "Intel")
    laptop2 = Laptop(8, 2, "AMD")

    print(Laptop.addnumbers(4, 4))
    print(laptop1.addtwonumbers(5, 3))

    print(laptop1.laptopInfo())
    Laptop.brand = "Dell"
    print(laptop2.laptopInfo())
    laptop1.brand = "HP"
    print(laptop1.laptopInfo())

    # To display object variables
    print(vars(laptop2))
    # To display all variables in the object including class attributes and parent class attributes
    print(dir(laptop2))
    laptop1.just_a_method("i am fine", [1, 2, 3, 4, 5], ("hi", 100))
