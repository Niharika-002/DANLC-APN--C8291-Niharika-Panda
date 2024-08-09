# Wap to print multiplication tables from a given range.

s = int(input("enter the number for starting : "))
i = int(input("enter the number for ending : "))
for k in range(1, 11):
    for j in range(s, i + 1):
         print(j*k, "\t", end="   ")
    print()
