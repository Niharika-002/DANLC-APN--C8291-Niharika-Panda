
# wap to find the sum of first 10 natural numbers.

n = int(input("enter the number : "))
sum = 0
i = 0
# for i in range(1, n+1):
#     sum = sum + i
#
# print(sum)

while i <= n:
    sum = sum + i
    i += 1

print(f"sum of 10 natural number is : {sum}")

