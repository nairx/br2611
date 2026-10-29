class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Employee Details")
        print(self.name,self.age)

class Developer(Employee):
    def skills(self):
        print("Java")

class Manager(Employee):
    def dept(self):
        print("IT")


e = Developer("John",21)
e.display()
e.skills()


e1 = Manager("Amy",23)
e1.display()
e1.dept()












# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Employee Details")
#         print(self.name,self.age)

# class Developer(Employee):
#     pass

# class Manager(Employee):
#     pass



