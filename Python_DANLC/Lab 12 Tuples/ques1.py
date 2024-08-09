# Write a Python program to find the number of times 4 appears in the tuple.
# Input:
# tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
# Output: 3

tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
count = 0
for i in tuplex:
    if i==4:
       count+=1
print(f"The nummber of time 4 appears in the tuple is {count}")