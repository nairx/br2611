class Employee:
    def display(self,name=None):
        print("Employee")
        if name:
            print(name)

e = Employee()
e.display()
e.display("John")