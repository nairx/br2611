class Employee:
    def display(self):
        print("Employee")

class Developer(Employee):
    def display(self):
        print("Developer")

class Manager(Employee):
    def display(self):
        print("Manager")

e1 = Developer()
e1.display()

e2 = Manager()
e2.display()