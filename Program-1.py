employees = {}
while(True):
    name = input("Enter Employee Name:")
    if name == "no":
        break
    salary = input("Enter Employee Salary:")
    employees[name] = salary
print(employees)
print("Done.")