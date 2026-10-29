from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def display(self):
        pass

class Developer(Employee):
    def Skills(self):
        print("Java")
    def display(self):
        print("Developer Details")

class Manager(Employee):
    def display(self):
        print("Manager Details")

e = Developer()
e.Skills()
e.display()

e1 = Manager()
e1.display()