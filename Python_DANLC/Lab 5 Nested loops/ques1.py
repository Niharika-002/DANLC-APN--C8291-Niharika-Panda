# Wap to print first 10 prime numbers

# 1, 13, 17

# 17 - check division until its half meaning division till 6

n = int(input("Enter the number of prime numbers you want : "))
prime_number = []
num = 2

while len(prime_number) < n:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if num % i == 0:
            is_prime = False
        else:
            is_prime = True
    if is_prime == True:
        prime_number.append(num)
    num += 1

print(prime_number)






































