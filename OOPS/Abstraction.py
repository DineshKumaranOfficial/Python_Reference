class oops:
    """ We cannot declare private variables or methods in python,
     instead it will be prefixed with an underscore to notify that it is a private variable
     Variables or methods prefixed with an underscore should not be overrided
     In python developers are responsible for handling privacy by not reconfiguring other class variables or methods that are prefixed with _ """
    def __init__(sel, name, age):
        sel._name = name
        sel._age = age

    def _printinfo(self):
        print(f"Name is {self._name} and Age is {self._age}")


oopsobj = oops("NDK", 23)
oopsobj._printinfo()
