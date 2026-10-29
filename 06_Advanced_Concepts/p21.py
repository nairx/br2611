from collections import UserList

class MyList(UserList):
    def pop(self):
        raise Exception("Pop not allowed")

name = MyList(["Amy","John"])

name.pop()

