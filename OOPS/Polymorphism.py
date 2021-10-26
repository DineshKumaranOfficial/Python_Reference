class Laptop:
    def __init__(self, name):
        self.name = name

    def status(self):
        print(f"This is a {self.name} Laptop", end="")


class Ram(Laptop):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def status(self):
        super().status()
        print(f" with {self.size} GB Ram")


if __name__ == "__main__":

    ram = Ram("Lenovo", 8)
    ram.status()
