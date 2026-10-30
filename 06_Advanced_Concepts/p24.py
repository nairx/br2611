class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 
    def displaySalary(self):
        print(self.salary)
    def __str__(self):
        return self.name + "-" + str(self.salary)

e = Employee("Brian",45000)

print(e)