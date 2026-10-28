class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Employee Details")
        print(self.name,self.age)

e = Employee("John",21)
e.display()



# class Employee:
#     def display(self):
#         print("Employee Details")

# e = Employee()
# e.display()