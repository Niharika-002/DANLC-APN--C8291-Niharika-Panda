# Write a python program and iterate the given tuples

# Input:
# employee1 = ("John Doe", 101, "Human Resources", 60000)
# employee2 = ("Alice Smith", 102, "Marketing", 55000)
# employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
listx = [employee1, employee2, employee3]

print("Employee Records")
print("------------------------------------------------------")

for i in listx:
    name = i[0]
    employeeId = i[1]
    department = i[2]
    salary = i[3]

    print(f"Name: {name}")
    print(f"Employee ID: {employeeId}")
    print(f"Department: {department}")
    print(f"Salary: {salary}")



