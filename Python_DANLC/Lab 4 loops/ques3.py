# Wap to input  10 numbers from user and find their sum and average.

numbers = []
s = 0

for i in range(10):
    n = int(input("enter the number : "))
    numbers.append(n)
    s = s + n

avg = s/10

print(f"sum is : {s}")
print(f"average is : {avg}")





