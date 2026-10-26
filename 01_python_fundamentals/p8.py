employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))
 
gross_salary = basic_salary + hra + da
annual_salary = gross_salary * 12
 
print(f"Employee Name: {employee_name}")
print(f"Employee ID: {employee_id}")
print(f"Basic Salary: {basic_salary}")
print(f"HRA: {hra}")
print(f"DA: {da}")
print(f"Gross Salary: {gross_salary}")
print(f"Annual Salary: {annual_salary}"