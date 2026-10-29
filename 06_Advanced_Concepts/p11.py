class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Employee Details")
        print(self.name,self.age)

class Developer(Employee):
    def __init__(self,name,age,skill):
        super().__init__(name,age)
        self.skill = skill
    def skills(self):
        print(self.skill)

class Manager(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept = dept
    def department(self):
        print(self.dept)


e = Developer("John",21,"Python")
e.display()
e.skills()


e1 = Manager("Amy",23,"Admin")
e1.display()
e1.department()