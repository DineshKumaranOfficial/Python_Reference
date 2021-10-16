from typing import List


class Superlist(list):
    def __len__(self):
        return 1000


if __name__ == '__main__':
    superlist = Superlist()
    superlist.append(1)
    superlist.append(2)
    superlist.append(3)
    superlist.append(4)
    superlist.append(5)
    print(superlist)
    print(len(superlist))
    print(issubclass(Superlist, list))
    print(issubclass(list, object))
