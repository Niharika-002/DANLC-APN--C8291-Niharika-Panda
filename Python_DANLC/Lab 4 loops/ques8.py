# Wap to input 10 numbers from user and find the minimum and maximum number.

num = []
max_num = 0
min_num = 0

for i in range(10):
    a = int(input("enter the numbers : "))
    num.append(a)
    max_num.append(max(num))
    min_num.append(min(num))

print("---------")
print(f"Maximum Number is : {max_num}\nMinimum number is : {min_num}", end=" ")


