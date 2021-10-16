a = 1

# Since a is in functional scope it is treated as a local variable for the function


def someFunc():
    a = 3
    return a


print(a)
print(someFunc())


def parent():
    a = 10

    def child():
        return a
    return child()


print(parent())

# Accessing different Scopes

total = 0
mylist = [1, 2, 3]


def count(list):
    global total    # We can avoid this dependency by passing the value as argument and using it inside the function
    list.pop(1)     # Using global will create a dependency between functions
    total += 1
    return total


""" count()
count()
print(count()) """
count(mylist)
print(mylist)


""" 
#1 Start with local scope
#2 If Not Parent Local Scope
#3 If Not Global Scope
#4 If Not Built In Python Functions
"""
# Parameters are generally considered as local scope
