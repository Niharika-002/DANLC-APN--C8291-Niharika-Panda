def emp(x):
    print(f"Name: {x[0]}")
    print(f"Employee ID: {x[1]}")
    print(f"Department: {x[2]}")
    print(f"Salary: {x[3]}\n")


employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

print("Employee Records: ")
emp(employee1)
emp(employee2)
emp(employee3)
