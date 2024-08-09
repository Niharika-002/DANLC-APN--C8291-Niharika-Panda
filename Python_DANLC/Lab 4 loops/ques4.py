# Wap to print the factorial of a number.

# N=6  fact= 6*5*4*3*2*1

num = int(input("Enter the number for factorial : "))
fact = 1

for i in range(1, num+1):
    fact = fact * i
    i += 1

print(f"Factorial is {fact}")



