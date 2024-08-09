
# Wap to check if the user has provided the correct currency note for deposit or not.
# The note should be in between the following currencies: -
# 2000, 500, 200, 100, 50

a = [2000, 500, 200, 100, 50]
curr = int(input("enter you currency note value : "))

if curr in a:
    print("correct currency")

else:
    print("invalid currency")