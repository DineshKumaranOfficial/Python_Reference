# This one is a higher order function since it accepts another function


def hi(func):
    func()


# This is a higher order function since it returns another function
def hello():
    def dummy():
        print('this is hello dummy')
    return dummy


def sample():
    print("I'm just a sample")


a = hi(hello())
a = hi(sample)
