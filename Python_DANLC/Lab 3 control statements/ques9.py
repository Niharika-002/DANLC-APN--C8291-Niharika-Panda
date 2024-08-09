
# write a program to generate the following payslip for an employee:-

basicSalary = int(input("Enter Basic Salary: "))
exp = int(input("Enter Experience in Year: "))
name = input("Enter your name: ")
print("-------------------------------------------------------------------------------------------------------")
print("                                               Pay Slip                                    ")
print("-------------------------------------------------------------------------------------------------------")
print(f"Name: {name}")
print(f"Experience: {exp}")
print(f"Basic Salary: {basicSalary}")
print("-------------------------------------------------------------------------------------------------------")


DA = 0.05*basicSalary
TA = 0.065*basicSalary
CCA = 0.08*basicSalary
HRA = 0.1*basicSalary
PF = 0.125*basicSalary
bonus = 0
if exp>25:
    bonus = 0.25*basicSalary
elif exp>20:
    bonus = 0.20*basicSalary
elif exp>15:
    bonus = 0.15*basicSalary
else:
    bonus = 0.1*basicSalary
totalSalary = basicSalary+DA+TA+CCA+HRA+PF+bonus
netSalary = totalSalary - PF

print(f"DA: {DA}")
print(f"TA: {TA}")
print(f"CCA: {CCA}")
print(f"HRA: {HRA}")
print(f"PF: {PF}")
print(f"BONUS: {bonus}")
print(f"TOTAL SALARY: {totalSalary}")
print(f"NET SALARY: {netSalary}")