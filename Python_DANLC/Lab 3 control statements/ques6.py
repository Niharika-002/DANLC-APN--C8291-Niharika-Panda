
# Input units of electricity from user and print the bill according to the following criteria
# a.    Less than 200 : no bill
# b.    Next 200-300  -   1.2/perunit       100*1
# c.     Next 300-400  -1.5/perunit           100*2
# d.    Next 400-500  - 2.5/perunit          100*2
# e.    Above 500 -   8/per unit

u = int(input("enter units : "))

bill = 0

if u >= 500:
    bill = (u-500) * 8 + 100 * 2.5 + 100 * 1.5 + 100 * 1.2

elif u >= 400:
    bill = (u-400) * 2.5 + 100 * 1.5 + 100 * 1.2

elif u >= 300:
    bill = (u-300) * 1.5 + 100 * 1.2

elif u >= 200:
    bill = (u-200) * 1.2

elif 0 <= u <= 200:
    bill = 0

else:
    print("units must be positive")

print("your bill is : ", bill)

