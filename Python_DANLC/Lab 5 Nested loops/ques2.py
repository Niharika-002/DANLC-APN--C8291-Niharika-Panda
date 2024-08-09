# Wap to print all the Armstrong numbers between a given range

s = int(input("enter the number for starting : "))
i = int(input("enter the number for ending : "))

print(f"Armstrong numbers between {s} and {i} are - ")

for k in range(s, i+1):
    num_str = str(k)
    num_digits = len(num_str)
    sum_of_powers = 0

    for digits in num_str:
        sum_of_powers += int(digits) ** num_digits

    if sum_of_powers == k:
        print(k, end="   ")








