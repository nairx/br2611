class Employee:
    def __init__(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name


e = Employee("John")
print(e.getName())
e.setName("Cathy")
print(e.getName())