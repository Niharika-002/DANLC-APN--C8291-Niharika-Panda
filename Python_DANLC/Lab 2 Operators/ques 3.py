
# Wap to check whether an year is leap or not.

year = int(input("enter a year : "))
leap = True if year%4 == 0 and year%100 == 0 and year%400 == 0 else False
print(leap)
