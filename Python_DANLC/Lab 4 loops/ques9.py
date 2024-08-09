# Wap to print all the leap years from 1 to n.

n = int(input("enter n  = "))

year = 1
print(f"Leap years from 1 to {n}:")

while year<=n:
    if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
        print(year)
        year += 1

print(year)