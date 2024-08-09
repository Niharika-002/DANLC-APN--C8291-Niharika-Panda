# wap to calculate the salary slip
# Basic  salary : input from user  // salary=60000
# Da     :    2% of basic   // da=0.02*salary
# Ta      :   3% of salary
# Hra  :      10% salary
# PF     :    15% of salary
# Total salary=    basic+da+ta+hra+pf;’
# Net salary =   total-pf;
# Calculate bonus of employee to 25 % of salary by shift operators.

bs = float(input("Enter your basic salary : "))
da = 0.02*bs
ta = 0.03*bs
hra = 0.10 *bs
pf = 0.15*bs
totalSalary = bs + da + ta + hra + pf
netSalary = totalSalary - pf
print(f"Net Salary is Rs {netSalary}")
bonus = 0.25*netSalary
print(f"Bonus will be of Rs {bonus}")